[Back to Index](../README.md)

---

# Genre Model & Repository

This document details the `Genre` Pydantic model and its corresponding `GenreRepository`.

## Pydantic Model: Genre

The `Genre` model represents a music genre in the database.

- **`genre_id`**: The unique identifier for the genre.
- **`name`**: The name of the genre (max length 120).

## Repository: GenreRepository

`GenreRepository` provides access to the `genre` table.

### Example Usage

```python
from chinook_pydantic_repository.database import DatabasePoolManager
from chinook_pydantic_repository.repository import GenreRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = GenreRepository(pool)

# Get a genre by ID
genre = repo.get_by_id(1)
print(f"Genre: {genre.name}")
```
