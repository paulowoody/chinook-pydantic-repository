[Back to Index](../README.md)

---

# Playlist Model & Repository

This document details the `Playlist` Pydantic model and its corresponding `PlaylistRepository`.

## Pydantic Model: Playlist

The `Playlist` model represents a user-defined collection of tracks.

- **`playlist_id`**: The unique identifier for the playlist.
- **`name`**: The name of the playlist (max length 120).

## Repository: PlaylistRepository

`PlaylistRepository` provides access to the `playlist` table.

### Example Usage

```python
from database import DatabasePoolManager
from repository import PlaylistRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = PlaylistRepository(pool)

# Get a playlist by ID
playlist = repo.get_by_id(1)
print(f"Playlist: {playlist.name}")
```
