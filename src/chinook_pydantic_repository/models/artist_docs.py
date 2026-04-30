from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ArtistDocs(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(description="The unique identifier for the artist documentation.")
    body: Any | None = Field(
        default=None, description="A JSONB field storing arbitrary document data."
    )
