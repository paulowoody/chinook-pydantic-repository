"""
Package for data models representing the database schema.

This `__init__.py` re-exports all individual Pydantic models to provide 
a flat import space (e.g., `from models import Artist`).
"""

from .album import Album
from .artist import Artist
from .artist_docs import ArtistDocs
from .customer import Customer
from .employee import Employee
from .genre import Genre
from .invoice import Invoice
from .invoice_line import InvoiceLine
from .media_type import MediaType
from .playlist import Playlist
from .playlist_track import PlaylistTrack
from .track import Track

# The `__all__` list is a special Python variable that defines the "public API" 
# of this package. 
# 
# 1. It explicitly tells other developers which symbols are intended to be 
#    exported and used outside of this directory.
# 2. It controls what is imported when a user runs `from models import *`.
# 3. It helps IDEs (like PyCharm or VS Code) and static analysis tools 
#    provide better autocomplete and identify "unused" imports correctly.
__all__ = [
    "Album",
    "Artist",
    "ArtistDocs",
    "Customer",
    "Employee",
    "Genre",
    "Invoice",
    "InvoiceLine",
    "MediaType",
    "Playlist",
    "PlaylistTrack",
    "Track",
]
