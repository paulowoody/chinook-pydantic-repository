from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class Customer(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    customer_id: int = Field(description="The unique identifier for the customer.")
    first_name: str = Field(max_length=40, description="The first name of the customer.")
    last_name: str = Field(max_length=20, description="The last name of the customer.")
    company: Optional[str] = Field(default=None, max_length=80, description="The company the customer works for.")
    address: Optional[str] = Field(default=None, max_length=70, description="The customer's street address.")
    city: Optional[str] = Field(default=None, max_length=40, description="The city where the customer resides.")
    state: Optional[str] = Field(default=None, max_length=40, description="The state or province where the customer resides.")
    country: Optional[str] = Field(default=None, max_length=40, description="The country where the customer resides.")
    postal_code: Optional[str] = Field(default=None, max_length=10, description="The postal code for the customer's address.")
    phone: Optional[str] = Field(default=None, max_length=24, description="The customer's phone number.")
    fax: Optional[str] = Field(default=None, max_length=24, description="The customer's fax number.")
    email: str = Field(max_length=60, description="The customer's email address.")
    support_rep_id: Optional[int] = Field(default=None, description="The ID of the employee who provides support to this customer.")
