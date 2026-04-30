from datetime import datetime
from decimal import Decimal

import pytest
from pydantic import ValidationError

from chinook_pydantic_repository.models import (
    Album,
    Artist,
    ArtistDocs,
    Customer,
    Employee,
    Genre,
    Invoice,
    InvoiceLine,
    MediaType,
    Playlist,
    PlaylistTrack,
    Track,
)


def test_artist_creation_and_validation():
    # Valid Artist
    artist = Artist(artist_id=1, name="AC/DC")
    assert artist.artist_id == 1
    assert artist.name == "AC/DC"

    # Invalid Artist (name exceeds max_length of 120)
    invalid_name = "A" * 150
    with pytest.raises(ValidationError) as exc_info:
        Artist(artist_id=2, name=invalid_name)
    assert "String should have at most 120 characters" in str(exc_info.value)


def test_album_creation():
    album = Album(
        album_id=1, title="For Those About To Rock We Salute You", artist_id=1
    )
    assert album.album_id == 1
    assert album.title == "For Those About To Rock We Salute You"
    assert album.artist_id == 1


def test_genre_creation():
    genre = Genre(genre_id=1, name="Rock")
    assert genre.genre_id == 1
    assert genre.name == "Rock"


def test_media_type_creation():
    media_type = MediaType(media_type_id=1, name="MPEG audio file")
    assert media_type.media_type_id == 1
    assert media_type.name == "MPEG audio file"


def test_track_creation():
    track = Track(
        track_id=1,
        name="For Those About To Rock (We Salute You)",
        album_id=1,
        media_type_id=1,
        genre_id=1,
        composer="Angus Young, Malcolm Young, Brian Johnson",
        milliseconds=343719,
        bytes=11170334,
        unit_price=Decimal("0.99"),
    )
    assert track.track_id == 1
    assert track.name == "For Those About To Rock (We Salute You)"
    assert track.album_id == 1
    assert track.unit_price == Decimal("0.99")


def test_track_validation_errors():
    # Test missing required field (milliseconds is required)
    with pytest.raises(ValidationError) as exc_info:
        Track(
            track_id=1,
            name="Missing Milliseconds",
            media_type_id=1,
            unit_price=Decimal("0.99"),
        )
    assert "Field required" in str(exc_info.value)
    assert "milliseconds" in str(exc_info.value)

    # Test type coercion failure (cannot convert "abc" to integer)
    with pytest.raises(ValidationError) as exc_info_type:
        Track(
            track_id="abc",  # Invalid integer
            name="Bad Track ID",
            media_type_id=1,
            milliseconds=3000,
            unit_price=Decimal("0.99"),
        )
    assert "Input should be a valid integer" in str(exc_info_type.value)


def test_playlist_creation():
    playlist = Playlist(playlist_id=1, name="Heavy Metal Classic")
    assert playlist.playlist_id == 1
    assert playlist.name == "Heavy Metal Classic"


def test_playlist_track_creation():
    playlist_track = PlaylistTrack(playlist_id=1, track_id=1)
    assert playlist_track.playlist_id == 1
    assert playlist_track.track_id == 1


def test_employee_creation():
    employee = Employee(
        employee_id=1,
        last_name="Adams",
        first_name="Andrew",
        title="General Manager",
        hire_date=datetime(2002, 8, 14),
        email="andrew@chinookcorp.com",
    )
    assert employee.employee_id == 1
    assert employee.last_name == "Adams"
    assert employee.first_name == "Andrew"
    assert employee.hire_date == datetime(2002, 8, 14)


def test_customer_creation():
    customer = Customer(
        customer_id=1,
        first_name="Luís",
        last_name="Gonçalves",
        company="Embraer - Empresa Brasileira de Aeronáutica S.A.",
        email="luisg@embraer.com.br",
        support_rep_id=1,
    )
    assert customer.customer_id == 1
    assert customer.first_name == "Luís"
    assert customer.support_rep_id == 1


def test_invoice_creation():
    invoice = Invoice(
        invoice_id=1,
        customer_id=1,
        invoice_date=datetime(2021, 1, 1, 10, 0, 0),
        billing_address="Av. Brigadeiro Faria Lima, 2170",
        billing_city="São José dos Campos",
        billing_country="Brazil",
        total=Decimal("1.98"),
    )
    assert invoice.invoice_id == 1
    assert invoice.customer_id == 1
    assert invoice.total == Decimal("1.98")
    assert invoice.invoice_date == datetime(2021, 1, 1, 10, 0, 0)


def test_invoice_line_creation():
    invoice_line = InvoiceLine(
        invoice_line_id=1,
        invoice_id=1,
        track_id=1,
        unit_price=Decimal("0.99"),
        quantity=2,
    )
    assert invoice_line.invoice_line_id == 1
    assert invoice_line.unit_price == Decimal("0.99")
    assert invoice_line.quantity == 2


def test_artist_docs_creation():
    doc = ArtistDocs(
        id=1, body={"bio": "Australian rock band formed in Sydney in 1973"}
    )
    assert doc.id == 1
    assert doc.body["bio"] == "Australian rock band formed in Sydney in 1973"
