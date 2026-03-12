[Back to Index](../README.md)

---

# Artist Model & Repository

This document details the `Artist` Pydantic model and its corresponding `ArtistRepository`.

## Pydantic Model: Artist

The `Artist` model represents an artist (band, singer, etc.) in the database.

- **`artist_id`**: The unique identifier for the artist.
- **`name`**: The name of the artist (max length 120).

## Relationships

- **Albums**: An artist can have multiple albums. These can be fetched using the `AlbumRepository.get_by_artist_id()` method.

## Repository: ArtistRepository

`ArtistRepository` provides access to the `artist` table.

### Example Usage

```python
from database import DatabasePoolManager
from repository import ArtistRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = ArtistRepository(pool)

# Get an artist by ID
artist = repo.get_by_id(1)
print(artist.name)

# Get all artists with pagination
artists = repo.get_all(limit=10, offset=0)
for a in artists:
    print(a.name)
```
