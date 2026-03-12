"""
This module defines the ArtistRepository class.
"""

from typing import Union
from psycopg_pool import ConnectionPool
from models.artist import Artist
from .base import BasePgRepository
from database.session import DatabasePoolManager

class ArtistRepository(BasePgRepository[Artist]):
    """
    Repository for accessing Artist data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, Artist, "artist", "artist_id")
