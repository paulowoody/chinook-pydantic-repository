"""
This module defines the AlbumRepository class.
"""

from typing import Union, List, Optional
import psycopg
from psycopg_pool import ConnectionPool
from chinook_pydantic_repository.models.album import Album
from .base import BasePgRepository
from chinook_pydantic_repository.database.session import DatabasePoolManager

class AlbumRepository(BasePgRepository[Album]):
    """
    Repository for accessing Album data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, Album, "album", "album_id")

    def get_by_artist_id(self, artist_id: int, conn: Optional[psycopg.Connection] = None) -> List[Album]:
        """
        Fetches all albums for a specific artist.
        """
        with self._get_connection(conn) as c:
            with c.cursor() as cur:
                query = f"SELECT * FROM {self.table_name} WHERE artist_id = %s ORDER BY title;"
                cur.execute(query, (artist_id,))
                rows = cur.fetchall()
                return [self.model_class.model_validate(row) for row in rows]
