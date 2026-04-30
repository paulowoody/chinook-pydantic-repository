from pydantic import BaseModel, ConfigDict, Field


class Album(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    album_id: int = Field(description="The unique identifier for the album.")
    title: str = Field(max_length=160, description="The title of the album.")
    artist_id: int = Field(
        description="The foreign key referencing the artist who created the album."
    )
