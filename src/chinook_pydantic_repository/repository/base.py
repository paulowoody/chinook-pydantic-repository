"""
Core repository abstractions for PostgreSQL database access.

This module defines the protocol and base class for all repositories, supporting
both pooled connections and explicit connection injection.
"""

from contextlib import nullcontext
from typing import Any, Generic, Protocol, TypeVar

import psycopg
from psycopg_pool import ConnectionPool
from pydantic import BaseModel

from chinook_pydantic_repository.database.session import DatabasePoolManager

# Type variable for the Protocol (Covariant for read operations)
T_co = TypeVar("T_co", bound=BaseModel, covariant=True)


class ReadOnlyRepository(Protocol[T_co]):
    """
    Structural interface defining read-only database operations.
    """

    def get_by_id(
        self, id_value: int, conn: psycopg.Connection | None = None
    ) -> T_co | None:
        """Fetch a single record by its primary key."""
        ...

    def get_all(
        self, limit: int = 100, offset: int = 0, conn: psycopg.Connection | None = None
    ) -> list[T_co]:
        """Fetch a list of records with optional pagination."""
        ...


# Type variable for the BasePgRepository implementation
T = TypeVar("T", bound=BaseModel)


class BasePgRepository(Generic[T]):
    """
    Concrete generic base class for PostgreSQL repositories.

    Provides standard implementations for fetching data and handles the
    logic for using either a managed pool or an injected connection.
    """

    def __init__(
        self,
        db_url_or_pool: str | ConnectionPool | DatabasePoolManager,
        model_class: type[T],
        table_name: str,
        primary_key: str,
    ):
        """
        Initializes the repository.

        Args:
            db_url_or_pool: A DB URL (string), a ConnectionPool instance, or a DatabasePoolManager.
            model_class: The Pydantic model class used for mapping results.
            table_name: The database table name.
            primary_key: The name of the primary key column.
        """
        if isinstance(db_url_or_pool, str):
            self.pool_manager = DatabasePoolManager.get_instance(db_url_or_pool)
        else:
            self.pool_manager = db_url_or_pool

        self.model_class = model_class
        self.table_name = table_name
        self.primary_key = primary_key

    def _get_connection(self, conn: psycopg.Connection | None = None) -> Any:
        """
        Provides a connection context manager.

        If `conn` is provided, it returns a nullcontext that simply wraps the
        provided connection (useful for sharing a connection in a transaction).
        Otherwise, it retrieves a connection from the managed pool.
        """
        if conn is not None:
            return nullcontext(conn)

        if hasattr(self.pool_manager, "connection"):
            return self.pool_manager.connection()
        elif hasattr(self.pool_manager, "pool"):
            return self.pool_manager.pool.connection()
        else:
            return self.pool_manager.connection()

    def get_by_id(
        self, id_value: int, conn: psycopg.Connection | None = None
    ) -> T | None:
        """Fetches a record by primary key."""
        with self._get_connection(conn) as c:
            with c.cursor() as cur:
                query = (
                    f"SELECT * FROM {self.table_name} WHERE {self.primary_key} = %s;"
                )
                cur.execute(query, (id_value,))
                row = cur.fetchone()

                if row:
                    return self.model_class.model_validate(row)
        return None

    def get_all(
        self, limit: int = 100, offset: int = 0, conn: psycopg.Connection | None = None
    ) -> list[T]:
        """Fetches multiple records with pagination support."""
        with self._get_connection(conn) as c:
            with c.cursor() as cur:
                query = f"SELECT * FROM {self.table_name} ORDER BY {self.primary_key} LIMIT %s OFFSET %s;"
                cur.execute(query, (limit, offset))
                rows = cur.fetchall()

                return [self.model_class.model_validate(row) for row in rows]
