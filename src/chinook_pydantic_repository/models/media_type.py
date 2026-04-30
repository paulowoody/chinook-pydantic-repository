from pydantic import BaseModel, ConfigDict, Field


class MediaType(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    media_type_id: int = Field(
        description="The unique identifier for the media format."
    )
    name: str | None = Field(
        default=None, max_length=120, description="The name of the media format."
    )
