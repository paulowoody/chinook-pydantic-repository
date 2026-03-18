"""
This module defines the ArtistDocsRepository class.
"""

from typing import Union
from psycopg_pool import ConnectionPool
from chinook_pydantic_repository.models.artist_docs import ArtistDocs
from .base import BasePgRepository
from chinook_pydantic_repository.database.session import DatabasePoolManager

class ArtistDocsRepository(BasePgRepository[ArtistDocs]):
    """
    Repository for accessing ArtistDocs data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, ArtistDocs, "artist_docs", "id")
