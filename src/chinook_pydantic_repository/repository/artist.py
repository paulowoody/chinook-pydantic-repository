"""
This module defines the ArtistRepository class.
"""

from psycopg_pool import ConnectionPool

from chinook_pydantic_repository.database.session import DatabasePoolManager
from chinook_pydantic_repository.models.artist import Artist

from .base import BasePgRepository


class ArtistRepository(BasePgRepository[Artist]):
    """
    Repository for accessing Artist data.
    """

    def __init__(self, db_url_or_pool: str | ConnectionPool | DatabasePoolManager):
        super().__init__(db_url_or_pool, Artist, "artist", "artist_id")
