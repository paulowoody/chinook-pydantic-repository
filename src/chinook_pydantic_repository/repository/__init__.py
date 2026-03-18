"""
Package for database repository implementations.

This `__init__.py` re-exports all concrete repository classes to provide 
a flat import space (e.g., `from chinook_pydantic_repository.repository import ArtistRepository`).
"""

from .album import AlbumRepository
from .artist import ArtistRepository
from .artist_docs import ArtistDocsRepository
from .customer import CustomerRepository
from .employee import EmployeeRepository
from .genre import GenreRepository
from .invoice import InvoiceRepository
from .invoice_line import InvoiceLineRepository
from .media_type import MediaTypeRepository
from .playlist import PlaylistRepository
from .playlist_track import PlaylistTrackRepository
from .track import TrackRepository

# The `__all__` list is a special Python variable used to define the public 
# interface (the exported symbols) of this package.
#
# WHY USE `__all__`?
# - Explicit API: It clearly marks which repositories are intended for 
#   external use.
# - Clean Exports: It prevents internal/utility imports (like `from .base ...`) 
#   from being exported when a user runs `from chinook_pydantic_repository.repository import *`.
# - Tooling Support: IDEs and linters use `__all__` to provide better 
#   navigation and to prevent "imported but unused" warnings for re-exports.
__all__ = [
    "AlbumRepository",
    "ArtistRepository",
    "ArtistDocsRepository",
    "CustomerRepository",
    "EmployeeRepository",
    "GenreRepository",
    "InvoiceRepository",
    "InvoiceLineRepository",
    "MediaTypeRepository",
    "PlaylistRepository",
    "PlaylistTrackRepository",
    "TrackRepository",
]
