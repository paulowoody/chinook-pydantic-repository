[Back to Index](../README.md)

---

# Repository Patterns

This document explains the repository abstractions used in this project to facilitate a clean separation of concerns and robust data access.

## Terminology

Before diving into the implementation, it's important to understand the core concepts used in this layer:

- **Data Access Layer (DAL)**: A specialized layer of an application that provides simplified access to data stored in persistent storage, such as a database. Its primary goal is to hide the complexities of the database (like SQL queries) from the rest of the application.
- **Repository Pattern**: A design pattern that mediates between the domain (Models) and data mapping layers (SQL) using a collection-like interface for accessing domain objects. It encapsulates the logic required to access data sources and centralizes common data access functionality.

## ReadOnlyRepository (Protocol)

The `ReadOnlyRepository` is a structural protocol located in `repository/base.py`. It defines a clear contract for any repository that can read data from the database.

### The Contract

```python
from typing import TypeVar, List, Optional, Protocol
from pydantic import BaseModel
import psycopg

T_co = TypeVar('T_co', bound=BaseModel, covariant=True)

class ReadOnlyRepository(Protocol[T_co]):
    def get_by_id(self, id_value: int, conn: Optional[psycopg.Connection] = None) -> Optional[T_co]:
        """Fetch a single record by its primary key."""
        ...

    def get_all(self, limit: int = 100, offset: int = 0, conn: Optional[psycopg.Connection] = None) -> List[T_co]:
        """Fetch a list of records with optional pagination."""
        ...
```

### Why Use a Protocol?

1.  **Duck Typing Support**: Allows any class that implements the required methods to be treated as a `ReadOnlyRepository` without needing to explicitly inherit from it.
2.  **Type Safety**: Enables better static analysis and IDE autocomplete for code that uses repositories.
3.  **Covariance**: The `T_co` type variable is covariant, which is appropriate for a read-only interface that only *returns* data.

## BasePgRepository

The `BasePgRepository` is a concrete generic base class that provides the actual PostgreSQL implementation logic for the `ReadOnlyRepository` contract.

### Key Features

1.  **Generic Data Mapping**: Automatically maps PostgreSQL dictionary rows to Pydantic models using `model_validate`.
2.  **Connection Injection & Pooling**: Supports both using a managed connection pool and an optional injected connection.
3.  **Simplified Queries**: Provides standard implementations for `get_by_id` and `get_all`, reducing boilerplate code in entity-specific repositories.

### Using Injected Connections

A crucial feature of `BasePgRepository` is its ability to accept an optional `conn` parameter in all its methods. This is particularly useful for **transactional integrity**:

```python
with pool_manager.connection() as conn:
    # Use the same connection for multiple repository calls in a single transaction
    artist = artist_repo.get_by_id(1, conn=conn)
    albums = album_repo.get_by_artist_id(artist.artist_id, conn=conn)
```

If `conn` is not provided, the repository will automatically retrieve a new connection from the managed pool and close it once the operation is complete.
