from pydantic import BaseModel, ConfigDict, Field

class PlaylistTrack(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    playlist_id: int = Field(description="The foreign key referencing the playlist.")
    track_id: int = Field(description="The foreign key referencing the track.")
