"""
This module defines the PlaylistRepository class.
"""

from typing import Union
from psycopg_pool import ConnectionPool
from chinook_pydantic_repository.models.playlist import Playlist
from .base import BasePgRepository
from chinook_pydantic_repository.database.session import DatabasePoolManager

class PlaylistRepository(BasePgRepository[Playlist]):
    """
    Repository for accessing Playlist data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, Playlist, "playlist", "playlist_id")
