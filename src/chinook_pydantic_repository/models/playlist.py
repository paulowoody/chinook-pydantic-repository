from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class Playlist(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    playlist_id: int = Field(description="The unique identifier for the playlist.")
    name: Optional[str] = Field(default=None, max_length=120, description="The name of the playlist.")
