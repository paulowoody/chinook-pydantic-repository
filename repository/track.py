"""
This module defines the TrackRepository class.
"""

from typing import Union
from psycopg_pool import ConnectionPool
from models.track import Track
from .base import BasePgRepository
from database.session import DatabasePoolManager

class TrackRepository(BasePgRepository[Track]):
    """
    Repository for accessing Track data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, Track, "track", "track_id")
