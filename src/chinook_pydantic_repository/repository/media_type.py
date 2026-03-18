"""
This module defines the MediaTypeRepository class.
"""

from typing import Union
from psycopg_pool import ConnectionPool
from chinook_pydantic_repository.models.media_type import MediaType
from .base import BasePgRepository
from chinook_pydantic_repository.database.session import DatabasePoolManager

class MediaTypeRepository(BasePgRepository[MediaType]):
    """
    Repository for accessing MediaType data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, MediaType, "media_type", "media_type_id")
