from pydantic import BaseModel, ConfigDict, Field


class Artist(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    artist_id: int = Field(description="The unique identifier for the artist.")
    name: str | None = Field(
        default=None, max_length=120, description="The name of the artist."
    )
