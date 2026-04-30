"""
Example script demonstrating basic Repository usage with a direct connection string.

This script shows how to:
1. Load database credentials from the environment.
2. Instantiate repositories.
3. Fetch multiple records with pagination.
4. Fetch a single record by ID.
"""

import os

import psycopg

from chinook_pydantic_repository import (
    AlbumRepository,
    ArtistRepository,
    TrackRepository,
)

# The DATABASE_URL should be set in your .env file or environment.
# UV will load this if you use the --env-file flag or set UV_ENV_FILE.
DB_URL = os.environ.get("DATABASE_URL")


def main():
    # Safety check: Ensure the database URL is provided
    if not DB_URL:
        print("Error: DATABASE_URL environment variable is not set.")
        print("Please copy .env-example to .env and configure your database URL.")
        return

    # Initialize the repositories with the DB URL.
    # In this basic example, each repository call will open/close its own connection.
    artist_repo = ArtistRepository(DB_URL)
    album_repo = AlbumRepository(DB_URL)
    track_repo = TrackRepository(DB_URL)

    try:
        # --- Example 1: Fetching multiple records ---
        print("--- Fetching Artists via Repository ---")
        # get_all supports limit and offset for pagination
        artists = artist_repo.get_all(limit=3)
        for artist in artists:
            # Results are automatically mapped to Pydantic models
            print(f"Loaded Artist Model: {artist}")

        print("\n--- Fetching Albums via Repository ---")
        albums = album_repo.get_all(limit=3)
        for album in albums:
            print(f"Loaded Album Model: '{album.title}' (Artist ID: {album.artist_id})")

        print("\n--- Fetching Tracks via Repository ---")
        tracks = track_repo.get_all(limit=3)
        for track in tracks:
            print(f"Loaded Track Model: '{track.name}' priced at ${track.unit_price}")

        # --- Example 2: Fetching a single record ---
        print("\n--- Fetching a Single Artist by ID ---")
        single_artist = artist_repo.get_by_id(1)
        if single_artist:
            print(f"Found specific artist: {single_artist.name}")

    except psycopg.OperationalError as e:
        # Handle connection failures gracefully
        print(f"Could not connect to the database at {DB_URL}")
        print(f"Error details: {e}")
        print(
            "\nPlease ensure your PostgreSQL server is running and the credentials are correct."
        )


if __name__ == "__main__":
    main()
