"""
This module defines the ArtistDocsRepository class.
"""

from psycopg_pool import ConnectionPool

from chinook_pydantic_repository.database.session import DatabasePoolManager
from chinook_pydantic_repository.models.artist_docs import ArtistDocs

from .base import BasePgRepository


class ArtistDocsRepository(BasePgRepository[ArtistDocs]):
    """
    Repository for accessing ArtistDocs data.
    """

    def __init__(self, db_url_or_pool: str | ConnectionPool | DatabasePoolManager):
        super().__init__(db_url_or_pool, ArtistDocs, "artist_docs", "id")
