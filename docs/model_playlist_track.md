[Back to Index](../README.md)

---

# PlaylistTrack Model & Repository

This document details the `PlaylistTrack` Pydantic model and its corresponding `PlaylistTrackRepository`.

## Pydantic Model: PlaylistTrack

The `PlaylistTrack` model represents the association between a playlist and its tracks.

- **`playlist_id`**: The foreign key referencing the playlist.
- **`track_id`**: The foreign key referencing the track.

## Repository: PlaylistTrackRepository

`PlaylistTrackRepository` provides access to the `playlist_track` table.

### Specialized Methods

This repository overrides standard behavior to handle the composite primary key:

- **`get_by_composite_id(playlist_id: int, track_id: int, conn: Optional[psycopg.Connection] = None)`**: Fetches a single association record.
- **`get_by_id(id_value: int)`**: This method raises a `NotImplementedError` as the table uses a composite key.

### Example Usage

```python
from chinook_pydantic_repository.database import DatabasePoolManager
from chinook_pydantic_repository.repository import PlaylistTrackRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = PlaylistTrackRepository(pool)

# Get a playlist-track association by composite ID
pt = repo.get_by_composite_id(playlist_id=1, track_id=5)
if pt:
    print(f"Playlist ID: {pt.playlist_id}, Track ID: {pt.track_id}")
```
