from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class Genre(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    genre_id: int = Field(description="The unique identifier for the genre.")
    name: Optional[str] = Field(default=None, max_length=120, description="The name of the genre.")
