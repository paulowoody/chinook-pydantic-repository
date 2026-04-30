"""
This module defines the MediaTypeRepository class.
"""

from psycopg_pool import ConnectionPool

from chinook_pydantic_repository.database.session import DatabasePoolManager
from chinook_pydantic_repository.models.media_type import MediaType

from .base import BasePgRepository


class MediaTypeRepository(BasePgRepository[MediaType]):
    """
    Repository for accessing MediaType data.
    """

    def __init__(self, db_url_or_pool: str | ConnectionPool | DatabasePoolManager):
        super().__init__(db_url_or_pool, MediaType, "media_type", "media_type_id")
