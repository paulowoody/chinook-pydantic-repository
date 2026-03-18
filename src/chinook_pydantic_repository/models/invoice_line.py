from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

class InvoiceLine(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    invoice_line_id: int = Field(description="The unique identifier for the invoice line item.")
    invoice_id: int = Field(description="The foreign key referencing the invoice this line belongs to.")
    track_id: int = Field(description="The foreign key referencing the track that was purchased.")
    unit_price: Decimal = Field(description="The unit price of the track at the time of purchase.")
    quantity: int = Field(description="The quantity of the track purchased (typically 1).")
