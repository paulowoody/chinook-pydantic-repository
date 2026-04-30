from datetime import datetime
from decimal import Decimal
from unittest.mock import MagicMock, patch

import pytest

from chinook_pydantic_repository.models import Album, Artist, Invoice, PlaylistTrack
from chinook_pydantic_repository.repository import (
    AlbumRepository,
    ArtistRepository,
    InvoiceRepository,
    PlaylistTrackRepository,
)

# Dummy connection string for testing
TEST_DB_URL = "postgresql://user:pass@localhost:5432/testdb"


@pytest.fixture
def mock_cursor():
    """
    A pytest fixture that mocks the DatabasePoolManager and the resulting
    database connection and cursor.
    """
    # NOTE: We now patch the class where it's DEFINED or where it's USED in repository.base
    with patch(
        "chinook_pydantic_repository.repository.base.DatabasePoolManager"
    ) as mock_pool_mgr_cls:
        # Mock the DatabasePoolManager instance
        mock_pool_mgr = MagicMock()
        mock_pool_mgr_cls.get_instance.return_value = mock_pool_mgr

        # Mock the connection context manager returned by pool_manager.connection()
        mock_conn = MagicMock()
        mock_pool_mgr.connection.return_value = mock_conn
        mock_conn.__enter__.return_value = mock_conn

        # Mock the connection's cursor() method context manager
        mock_cursor_context = MagicMock()
        mock_conn.cursor.return_value = mock_cursor_context

        # Mock the cursor object returned by entering the cursor context manager
        mock_cur = MagicMock()
        mock_cursor_context.__enter__.return_value = mock_cur

        yield mock_cur


def test_artist_repository_get_by_id(mock_cursor):
    # Setup mock data (simulating a dictionary row from psycopg dict_row)
    mock_cursor.fetchone.return_value = {"artist_id": 1, "name": "AC/DC"}

    repo = ArtistRepository(TEST_DB_URL)
    artist = repo.get_by_id(1)

    # Assertions
    assert isinstance(artist, Artist)
    assert artist.artist_id == 1
    assert artist.name == "AC/DC"

    # Verify the SQL query was generated correctly
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM artist WHERE artist_id = %s;", (1,)
    )


def test_artist_repository_get_by_id_not_found(mock_cursor):
    mock_cursor.fetchone.return_value = None

    repo = ArtistRepository(TEST_DB_URL)
    artist = repo.get_by_id(999)

    assert artist is None


def test_album_repository_get_all(mock_cursor):
    # Setup mock data for multiple rows
    mock_cursor.fetchall.return_value = [
        {"album_id": 1, "title": "Album One", "artist_id": 1},
        {"album_id": 2, "title": "Album Two", "artist_id": 2},
    ]

    repo = AlbumRepository(TEST_DB_URL)
    albums = repo.get_all(limit=10, offset=0)

    # Assertions
    assert len(albums) == 2
    assert all(isinstance(a, Album) for a in albums)
    assert albums[0].title == "Album One"
    assert albums[1].album_id == 2

    # Verify the pagination SQL query
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM album ORDER BY album_id LIMIT %s OFFSET %s;", (10, 0)
    )


def test_album_repository_get_by_artist_id(mock_cursor):
    # Setup mock data
    mock_cursor.fetchall.return_value = [
        {"album_id": 1, "title": "Album One", "artist_id": 1},
        {"album_id": 3, "title": "Album Three", "artist_id": 1},
    ]

    repo = AlbumRepository(TEST_DB_URL)
    albums = repo.get_by_artist_id(1)

    # Assertions
    assert len(albums) == 2
    assert all(a.artist_id == 1 for a in albums)
    assert albums[0].title == "Album One"
    assert albums[1].title == "Album Three"

    # Verify the SQL query
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM album WHERE artist_id = %s ORDER BY title;", (1,)
    )


def test_invoice_repository_mapping(mock_cursor):
    """Test a repository with complex data types like datetime and Decimal."""
    mock_cursor.fetchone.return_value = {
        "invoice_id": 1,
        "customer_id": 5,
        "invoice_date": datetime(2021, 1, 1, 10, 0),
        "billing_address": "123 Main St",
        "billing_city": "Cityville",
        "billing_state": "CA",
        "billing_country": "USA",
        "billing_postal_code": "12345",
        "total": Decimal("15.99"),
    }

    repo = InvoiceRepository(TEST_DB_URL)
    invoice = repo.get_by_id(1)

    assert isinstance(invoice, Invoice)
    assert invoice.total == Decimal("15.99")
    assert invoice.invoice_date == datetime(2021, 1, 1, 10, 0)


def test_playlist_track_repository_get_by_composite_id(mock_cursor):
    """Test the specialized get_by_composite_id method."""
    mock_cursor.fetchone.return_value = {"playlist_id": 1, "track_id": 5}

    repo = PlaylistTrackRepository(TEST_DB_URL)
    playlist_track = repo.get_by_composite_id(playlist_id=1, track_id=5)

    assert isinstance(playlist_track, PlaylistTrack)
    assert playlist_track.playlist_id == 1
    assert playlist_track.track_id == 5

    # Verify the composite key query
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM playlist_track WHERE playlist_id = %s AND track_id = %s;", (1, 5)
    )


def test_playlist_track_repository_get_by_id_raises_error():
    """Verify that calling get_by_id on a composite key table raises an exception."""
    # We still need to mock DatabasePoolManager because the constructor calls get_instance
    with patch("chinook_pydantic_repository.repository.base.DatabasePoolManager"):
        repo = PlaylistTrackRepository(TEST_DB_URL)

        with pytest.raises(NotImplementedError) as exc_info:
            repo.get_by_id(1)

        assert "uses a composite key" in str(exc_info.value)
