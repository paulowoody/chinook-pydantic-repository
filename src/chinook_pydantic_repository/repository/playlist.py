"""
This module defines the PlaylistRepository class.
"""

from psycopg_pool import ConnectionPool

from chinook_pydantic_repository.database.session import DatabasePoolManager
from chinook_pydantic_repository.models.playlist import Playlist

from .base import BasePgRepository


class PlaylistRepository(BasePgRepository[Playlist]):
    """
    Repository for accessing Playlist data.
    """

    def __init__(self, db_url_or_pool: str | ConnectionPool | DatabasePoolManager):
        super().__init__(db_url_or_pool, Playlist, "playlist", "playlist_id")
