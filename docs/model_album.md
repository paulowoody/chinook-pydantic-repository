[Back to Index](../README.md)

---

# Album Model & Repository

This document details the `Album` Pydantic model and its corresponding `AlbumRepository`.

## Pydantic Model: Album

The `Album` model represents an album in the music database.

- **`album_id`**: The unique identifier for the album.
- **`title`**: The title of the album (max length 160).
- **`artist_id`**: The foreign key referencing the artist who created the album.

## Relationships

- **Artist**: Each album belongs to a single artist.
- **Tracks**: An album contains multiple tracks.

## Repository: AlbumRepository

`AlbumRepository` provides access to the `album` table and handles related data fetching.

### Specialized Methods

In addition to standard `get_by_id` and `get_all`, `AlbumRepository` includes:

- **`get_by_artist_id(artist_id: int, conn: Optional[psycopg.Connection] = None)`**: Fetches all albums associated with a specific artist.

### Example Usage

```python
from chinook_pydantic_repository.database import DatabasePoolManager
from chinook_pydantic_repository.repository import AlbumRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = AlbumRepository(pool)

# Get an album by ID
album = repo.get_by_id(1)
print(album.title)

# Get all albums for an artist
albums = repo.get_by_artist_id(1)
for a in albums:
    print(a.title)
```
