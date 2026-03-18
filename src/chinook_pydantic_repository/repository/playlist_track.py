"""
This module defines the PlaylistTrackRepository class.
"""

from typing import Optional, Union
import psycopg
from psycopg_pool import ConnectionPool
from chinook_pydantic_repository.models.playlist_track import PlaylistTrack
from .base import BasePgRepository
from chinook_pydantic_repository.database.session import DatabasePoolManager

class PlaylistTrackRepository(BasePgRepository[PlaylistTrack]):
    """
    Repository for accessing PlaylistTrack data.
    Overrides get_by_id since this table has a composite primary key.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, PlaylistTrack, "playlist_track", "playlist_id")

    def get_by_composite_id(self, playlist_id: int, track_id: int, conn: Optional[psycopg.Connection] = None) -> Optional[PlaylistTrack]:
        """
        Fetch a single record by its composite primary key.
        """
        with self._get_connection(conn) as c:
            with c.cursor() as cur:
                query = f"SELECT * FROM {self.table_name} WHERE playlist_id = %s AND track_id = %s;"
                # noinspection SqlInjection
                cur.execute(query, (playlist_id, track_id))
                row = cur.fetchone()
                
                if row:
                    return self.model_class.model_validate(row)
        return None

    def get_by_id(self, id_value: int, conn: Optional[psycopg.Connection] = None) -> Optional[PlaylistTrack]:
        raise NotImplementedError("PlaylistTrack uses a composite key. Use get_by_composite_id(playlist_id, track_id).")
