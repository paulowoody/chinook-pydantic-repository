[Back to Index](../README.md)

---

# ArtistDocs Model & Repository

> **Note**: The `ArtistDocs` model and the `artist_docs` table are **not** part of the standard Chinook database schema. They have been added to this repository specifically to demonstrate and test the handling of PostgreSQL `JSONB` fields with Pydantic.

This document details the `ArtistDocs` Pydantic model and its corresponding `ArtistDocsRepository`.

## Pydantic Model: ArtistDocs

The `ArtistDocs` model represents arbitrary JSON documentation associated with an artist.

- **`id`**: The unique identifier for the artist documentation.
- **`body`**: A JSONB field storing arbitrary document data.

## Database DDL & Population

The `artist_docs` table is defined as follows:

```sql
CREATE TABLE public.artist_docs (
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    body jsonb NOT NULL,
    CONSTRAINT artist_docs_pkey PRIMARY KEY (id)
);
```

### Populating Data (PostgreSQL)

To populate the `artist_docs` table with denormalized artist and album data, you can use the following PostgreSQL-specific query. 

> **Important**: This script uses PostgreSQL's `JSONB` functions (`jsonb_build_object`, `jsonb_agg`). If you are using a different database engine, you will need to adapt the JSON generation logic accordingly.

```sql
INSERT INTO public.artist_docs (body)
SELECT jsonb_build_object(
    'artist_id', a.artist_id,
    'name', a.name,
    'albums', (
        SELECT jsonb_agg(jsonb_build_object('title', al.title))
        FROM album al
        WHERE al.artist_id = a.artist_id
    )
)
FROM artist a;
```

## Repository: ArtistDocsRepository

`ArtistDocsRepository` provides access to the `artist_docs` table.

### Example Usage

```python
from chinook_pydantic_repository.database import DatabasePoolManager
from chinook_pydantic_repository.repository import ArtistDocsRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = ArtistDocsRepository(pool)

# Get artist docs by ID
docs = repo.get_by_id(1)
if docs:
    print(docs.body)
```
