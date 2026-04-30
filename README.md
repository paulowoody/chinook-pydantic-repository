# Chinook Database ORM - Python & Pydantic

This project demonstrates a clean, three-tier architecture for interacting with a PostgreSQL database using Python. It bridges raw SQL queries from the `psycopg` (v3) driver with **Pydantic (v2)** models using the **Repository Pattern** and **Connection Pooling**.

## 📖 What is this?

In simple terms, this project is a **fast and well-organized "bridge"** that lets a Python program talk to a database (using the "Chinook" sample data) neatly and efficiently.

- **High-performance**: It's built for speed. It keeps a "pool" of connections ready to go so the computer doesn't waste time opening and closing them constantly.
- **Repository Pattern**: Think of this as a professional filing system. It keeps the "How to fetch data" code separate from the "What the data looks like" code, making it much easier to maintain.
- **Data Access Layer (DAL)**: This is just the technical name for the "bridge" itself—the part of the code whose only job is to translate database rows into Python objects.
- **Chinook**: This is the name of the industry-standard sample database used here, representing a digital music store.

## 📚 Documentation Index

- **Core Infrastructure**
  - [Database Infrastructure](docs/database_infrastructure.md) - Pooling and session management.
  - [Repository Patterns](docs/repository_patterns.md) - Read-only protocols and base classes.
  - [Database Schema](docs/database_schema.md) - ER Diagram and entity relationships.

- **Data Models & Repositories**
  - [Artist](docs/model_artist.md) | [Album](docs/model_album.md) | [Track](docs/model_track.md)
  - [Customer](docs/model_customer.md) | [Employee](docs/model_employee.md) | [Invoice](docs/model_invoice.md)
  - [Genre](docs/model_genre.md) | [MediaType](docs/model_media_type.md) | [Playlist](docs/model_playlist.md)
  - [InvoiceLine](docs/model_invoice_line.md) | [PlaylistTrack](docs/model_playlist_track.md) | [ArtistDocs](docs/model_artist_docs.md)

## Architecture Overview

The project is strictly organized to maintain a clean separation of concerns:

- **`src/chinook_pydantic_repository/models/` (Data Layer)**: Pure Pydantic models representing the database schema. These are "Plain Old Data" objects with no knowledge of the database or connection logic.
- **`src/chinook_pydantic_repository/repository/` (Data Access Layer)**: Object-oriented abstraction for database operations. Repositories handle the SQL logic and map results to Pydantic models. They support both managed pooling and manual connection injection (useful for transactions).
- **`src/chinook_pydantic_repository/database/` (Infrastructure Layer)**: Manages the low-level database lifecycle, including connection pooling via `psycopg-pool`.

## Prerequisites

- **Python 3.12** or higher.
- [uv](https://github.com/astral-sh/uv) for dependency management and tool isolation.
- **GNU Make** for build automation.
- **A Database Server** (for example, PostgreSQL).

### Required Tools
For building and publishing, you need the following tools installed (recommended via `uv tool`):

```bash
# For signing artifacts
uv tool install sigstore

# For publishing and republishing to Cloudsmith
uv tool install cloudsmith-cli
```

## 🚀 Getting Started

### 1. Database Setup (Example: PostgreSQL)

This project uses the classic **Chinook Sample Database**. To set it up with PostgreSQL:

1.  **Download the PostgreSQL script**: [Chinook_PostgreSql.sql](https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql)
2.  **Create a new database** in your PostgreSQL instance:
    ```sql
    CREATE DATABASE chinook;
    ```
3.  **Run the script** to seed the schema and data:
    ```bash
    psql -d chinook -f Chinook_PostgreSql.sql
    ```

### 2. Installation & Environment Setup

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Configure Environment:**
   Copy the example environment file and update it with your **database credentials** and (optionally) Cloudsmith tokens for publishing:
   ```bash
   cp .env-example .env
   ```
   **CRITICAL:** Edit the `.env` file to set your `DATABASE_URL` (e.g., `postgresql://user:password@localhost:5432/chinook`).

3. **Run tests:**
   ```bash
   uv run pytest -v
   ```

## 🛠️ Build & Development

This project uses a `Makefile` to simplify common development tasks.

- **Build the package:**
  ```bash
  make build
  ```
- **Sign the artifacts:**
  ```bash
  make sign
  ```
- **Publish to Cloudsmith:**
  ```bash
  make publish
  ```
- **Clean build artifacts:**
  ```bash
  make clean
  ```

### Linting & Formatting

The project uses **Ruff** for extremely fast linting and formatting, with configuration managed in `pyproject.toml`.

- **Check for linting issues:**
  ```bash
  uv run ruff check .
  ```
- **Automatically fix linting issues:**
  ```bash
  uv run ruff check . --fix
  ```
- **Format code:**
  ```bash
  uv run ruff format .
  ```

### Development Workflow & Versioning

The project follows a **Development Release** strategy (PEP 440). During active development, versions are suffixed with `.devN` (e.g., `0.1.0.dev1`).

1. **Increment Version:** Update `version` in `pyproject.toml` (e.g., `0.1.0.dev2`).
2. **Push "Snapshots":** The `make publish` command uses `cloudsmith push --republish`. This allows you to overwrite an existing dev version on the repository without bumping the version number if you are iterating on the same "snapshot".

### Cloudsmith Authentication

If you need to access or publish to the private Cloudsmith repository, you should authenticate using `uv` and ensure your API key is available in your environment.

1. **Login to the Cloudsmith index:**
   ```bash
   uv auth login https://dl.cloudsmith.io/public/paulowoody/chinook-pydantic-repository/python/simple/ --username token --password <YOUR_API_KEY>
   ```

2. **Configure Environment:**
   Ensure your `.env` file contains the `UV_PUBLISH_TOKEN` (which is your Cloudsmith API Key):
   ```bash
   UV_PUBLISH_TOKEN=your_cloudsmith_api_key_here
   ```

3. **How it works:**
   `uv` handles dependency resolution, while `cloudsmith-cli` handles the actual upload to ensure support for republishing/overwriting development builds.

## 🔍 Exploration & Examples

The project includes a `samples/` sub-project with detailed example scripts. This folder is configured as a **standalone project** to demonstrate how to consume the library from a remote repository (Cloudsmith) using `uv`.

### Running the Samples

1.  **Navigate to the samples directory:**
    ```bash
    cd samples
    ```
2.  **Ensure a .env exists with your database URL:**
    ```bash
    cp .env-example .env
    # Edit .env to set DATABASE_URL
    ```
3.  **Run Basic Repository Usage (`db_example.py`):**
    Demonstrates simple repository calls where each call opens and closes its own connection.
    ```bash
    uv run --env-file .env db_example.py
    ```
4.  **Run Advanced Pooling (`db_pool_example.py`):**
    Demonstrates professional-grade usage with a managed connection pool and concurrent workers.
    ```bash
    uv run --env-file .env db_pool_example.py
    ```

---

## Usage Examples

### Connection Pooling & Repositories

```python
from chinook_pydantic_repository import DatabasePoolManager, ArtistRepository, AlbumRepository

# 1. Initialize the global pool
pool = DatabasePoolManager("postgresql://user:pass@host/db")

# 2. Use repositories with the pool
artist_repo = ArtistRepository(pool)
artist = artist_repo.get_by_id(1)

# 3. Handle relationships through repositories
album_repo = AlbumRepository(pool)
albums = album_repo.get_by_artist_id(artist.artist_id)
```

## Future Expansion

- **CRUD Support**: Extend `BasePgRepository` to include `create`, `update`, and `delete` methods.
- **Async Support**: Utilize `psycopg.AsyncConnection` for high-concurrency environments like FastAPI.

## ⚖️ Copyright

Copyright (c) 2026 Paul Wood. Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## 📬 Contact

Paul Wood - [paulowoody@users.noreply.github.com](mailto:paulowoody@users.noreply.github.com)

Project Link: [https://github.com/paulowoody/chinook-pydantic-repository](https://github.com/paulowoody/chinook-pydantic-repository)
