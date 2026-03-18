"""
Chinook Pydantic Repository - A clean architecture for the Chinook database.
"""

from .database import DatabasePoolManager
from .models import (
    Album, Artist, ArtistDocs, Customer, Employee, Genre,
    Invoice, InvoiceLine, MediaType, Playlist, PlaylistTrack, Track
)
from .repository import (
    AlbumRepository, ArtistRepository, ArtistDocsRepository,
    CustomerRepository, EmployeeRepository, GenreRepository,
    InvoiceRepository, InvoiceLineRepository, MediaTypeRepository,
    PlaylistRepository, PlaylistTrackRepository, TrackRepository
)

__all__ = [
    "DatabasePoolManager",
    "Album", "Artist", "ArtistDocs", "Customer", "Employee", "Genre",
    "Invoice", "InvoiceLine", "MediaType", "Playlist", "PlaylistTrack", "Track",
    "AlbumRepository", "ArtistRepository", "ArtistDocsRepository",
    "CustomerRepository", "EmployeeRepository", "GenreRepository",
    "InvoiceRepository", "InvoiceLineRepository", "MediaTypeRepository",
    "PlaylistRepository", "PlaylistTrackRepository", "TrackRepository"
]
