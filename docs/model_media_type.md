[Back to Index](../README.md)

---

# MediaType Model & Repository

This document details the `MediaType` Pydantic model and its corresponding `MediaTypeRepository`.

## Pydantic Model: MediaType

The `MediaType` model represents a media format (MPEG, AAC, etc.) for tracks.

- **`media_type_id`**: The unique identifier for the media format.
- **`name`**: The name of the media format (max length 120).

## Repository: MediaTypeRepository

`MediaTypeRepository` provides access to the `media_type` table.

### Example Usage

```python
from database import DatabasePoolManager
from repository import MediaTypeRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = MediaTypeRepository(pool)

# Get a media type by ID
media_type = repo.get_by_id(1)
print(f"Media Type: {media_type.name}")
```
