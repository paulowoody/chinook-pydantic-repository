from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class Invoice(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    invoice_id: int = Field(description="The unique identifier for the invoice.")
    customer_id: int = Field(description="The foreign key referencing the customer associated with the invoice.")
    invoice_date: datetime = Field(description="The date the invoice was generated.")
    billing_address: Optional[str] = Field(default=None, max_length=70, description="The billing street address.")
    billing_city: Optional[str] = Field(default=None, max_length=40, description="The billing city.")
    billing_state: Optional[str] = Field(default=None, max_length=40, description="The billing state or province.")
    billing_country: Optional[str] = Field(default=None, max_length=40, description="The billing country.")
    billing_postal_code: Optional[str] = Field(default=None, max_length=10, description="The billing postal code.")
    total: Decimal = Field(description="The total amount for the invoice.")
