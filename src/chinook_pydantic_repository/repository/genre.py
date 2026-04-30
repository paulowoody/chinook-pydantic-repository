"""
This module defines the GenreRepository class.
"""

from psycopg_pool import ConnectionPool

from chinook_pydantic_repository.database.session import DatabasePoolManager
from chinook_pydantic_repository.models.genre import Genre

from .base import BasePgRepository


class GenreRepository(BasePgRepository[Genre]):
    """
    Repository for accessing Genre data.
    """

    def __init__(self, db_url_or_pool: str | ConnectionPool | DatabasePoolManager):
        super().__init__(db_url_or_pool, Genre, "genre", "genre_id")
