"""
This module defines the TrackRepository class.
"""

from psycopg_pool import ConnectionPool

from chinook_pydantic_repository.database.session import DatabasePoolManager
from chinook_pydantic_repository.models.track import Track

from .base import BasePgRepository


class TrackRepository(BasePgRepository[Track]):
    """
    Repository for accessing Track data.
    """

    def __init__(self, db_url_or_pool: str | ConnectionPool | DatabasePoolManager):
        super().__init__(db_url_or_pool, Track, "track", "track_id")
