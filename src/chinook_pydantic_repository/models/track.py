from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class Track(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    track_id: int = Field(description="The unique identifier for the track.")
    name: str = Field(max_length=200, description="The name or title of the track.")
    album_id: int | None = Field(
        default=None,
        description="The foreign key referencing the album this track belongs to.",
    )
    media_type_id: int = Field(
        description="The foreign key referencing the media format of the track."
    )
    genre_id: int | None = Field(
        default=None, description="The foreign key referencing the genre of the track."
    )
    composer: str | None = Field(
        default=None,
        max_length=220,
        description="The name of the composer(s) of the track.",
    )
    milliseconds: int = Field(description="The duration of the track in milliseconds.")
    bytes: int | None = Field(
        default=None, description="The file size of the track in bytes."
    )
    unit_price: Decimal = Field(description="The standard purchase price of the track.")
