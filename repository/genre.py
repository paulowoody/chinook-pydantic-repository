"""
This module defines the GenreRepository class.
"""

from typing import Union
from psycopg_pool import ConnectionPool
from models.genre import Genre
from .base import BasePgRepository
from database.session import DatabasePoolManager

class GenreRepository(BasePgRepository[Genre]):
    """
    Repository for accessing Genre data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, Genre, "genre", "genre_id")
