[Back to Index](../README.md)

---

# Database Infrastructure

This document explains the low-level database connection and session management infrastructure of the project.

## DatabasePoolManager

The `DatabasePoolManager` is a singleton class located in `src/chinook_pydantic_repository/database/session.py`. It is responsible for managing a connection pool using `psycopg-pool`.

### Responsibilities

1.  **Connection Pooling**: Manages a pool of PostgreSQL connections to improve performance by reusing existing connections instead of opening a new one for every query.
2.  **Concurrency Support**: Safely handles multiple concurrent requests (e.g., from different threads) by providing distinct connections from the pool up to the `max_size` limit.
3.  **Singleton Pattern**: Ensures that only one pool manager (and thus one connection pool) is created for a given database URL, preventing excessive connection usage.
4.  **URL Normalization**: Automatically strips the `jdbc:` prefix from connection strings, allowing it to be compatible with tools that provide JDBC-style URLs.
5.  **Dictionary Row Factory**: Configures the pool to use `psycopg.rows.dict_row`, ensuring that all queries return rows as dictionaries. This is crucial for seamless mapping to Pydantic models.

### Initialization

The pool manager is typically initialized once at the start of the application:

```python
from chinook_pydantic_repository.database import DatabasePoolManager

DB_URL = "postgresql://user:pass@host:5432/db"
pool_manager = DatabasePoolManager.get_instance(DB_URL)
```

### Getting a Connection

To get a connection from the pool, use the `connection()` context manager:

```python
with pool_manager.connection() as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT 1")
```

### Closing the Pool

When the application shuts down, you should close the pool to release all connections:

```python
pool_manager.close()
```
