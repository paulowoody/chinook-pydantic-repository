[Back to Index](../README.md)

---

# Track Model & Repository

This document details the `Track` Pydantic model and its corresponding `TrackRepository`.

## Pydantic Model: Track

The `Track` model represents an individual song or audio/video file.

- **`track_id`**: The unique identifier for the track.
- **`name`**: The name or title of the track (max length 200).
- **`album_id`**: The foreign key referencing the album this track belongs to.
- **`media_type_id`**: The foreign key referencing the media format.
- **`genre_id`**: The foreign key referencing the genre.
- **`composer`**: The name of the composer(s) (max length 220).
- **`milliseconds`**: The duration of the track in milliseconds.
- **`bytes`**: The file size of the track in bytes.
- **`unit_price`**: The standard purchase price of the track (Decimal).

## Repository: TrackRepository

`TrackRepository` provides access to the `track` table.

### Example Usage

```python
from database import DatabasePoolManager
from repository import TrackRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = TrackRepository(pool)

# Get a track by ID
track = repo.get_by_id(1)
print(f"Track: {track.name}, Price: ${track.unit_price}")
```
