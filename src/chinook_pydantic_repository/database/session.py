"""
Infrastructure for database session and pool management.
"""

from __future__ import annotations

from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool


class DatabasePoolManager:
    """
    Singleton class that manages a psycopg connection pool.

    This class abstracts the pool creation, stripping unnecessary prefixes (like 'jdbc:')
    and ensuring rows are returned as dictionaries for Pydantic mapping.
    """

    _instance: DatabasePoolManager | None = None

    def __init__(self, db_url: str, min_size: int = 1, max_size: int = 10):
        """
        Initializes the DatabasePoolManager.

        Args:
            db_url (str): The PostgreSQL connection string.
            min_size (int): Minimum number of connections in the pool.
            max_size (int): Maximum number of connections in the pool.
        """
        # Strip the 'jdbc:' prefix if it was provided (psycopg expects standard URI)
        if db_url.startswith("jdbc:"):
            db_url = db_url.replace("jdbc:", "", 1)

        self.db_url = db_url
        self.pool = ConnectionPool(
            self.db_url,
            min_size=min_size,
            max_size=max_size,
            open=True,
            kwargs={"row_factory": dict_row},
        )

    @classmethod
    def get_instance(cls, db_url: str) -> DatabasePoolManager | None:
        """Static method to get the singleton instance of the manager."""
        if cls._instance is None:
            cls._instance = cls(db_url)
        return cls._instance

    def connection(self):
        """Returns a connection context manager from the pool."""
        return self.pool.connection()

    def close(self):
        """Closes the connection pool."""
        self.pool.close()
