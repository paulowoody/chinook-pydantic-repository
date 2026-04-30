"""
Chinook Pydantic Repository - A clean architecture for the Chinook database.
"""

from .database import DatabasePoolManager
from .models import (
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
from .repository import (
    AlbumRepository,
    ArtistDocsRepository,
    ArtistRepository,
    CustomerRepository,
    EmployeeRepository,
    GenreRepository,
    InvoiceLineRepository,
    InvoiceRepository,
    MediaTypeRepository,
    PlaylistRepository,
    PlaylistTrackRepository,
    TrackRepository,
)

__all__ = [
    "Album",
    "AlbumRepository",
    "Artist",
    "ArtistDocs",
    "ArtistDocsRepository",
    "ArtistRepository",
    "Customer",
    "CustomerRepository",
    "DatabasePoolManager",
    "Employee",
    "EmployeeRepository",
    "Genre",
    "GenreRepository",
    "Invoice",
    "InvoiceLine",
    "InvoiceLineRepository",
    "InvoiceRepository",
    "MediaType",
    "MediaTypeRepository",
    "Playlist",
    "PlaylistRepository",
    "PlaylistTrack",
    "PlaylistTrackRepository",
    "Track",
    "TrackRepository",
]
