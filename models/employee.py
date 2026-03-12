from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class Employee(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    employee_id: int = Field(description="The unique identifier for the employee.")
    last_name: str = Field(max_length=20, description="The last name of the employee.")
    first_name: str = Field(max_length=20, description="The first name of the employee.")
    title: Optional[str] = Field(default=None, max_length=30, description="The job title of the employee.")
    reports_to: Optional[int] = Field(default=None, description="The employee ID of this person's manager.")
    birth_date: Optional[datetime] = Field(default=None, description="The employee's birth date.")
    hire_date: Optional[datetime] = Field(default=None, description="The date the employee was hired.")
    address: Optional[str] = Field(default=None, max_length=70, description="The employee's street address.")
    city: Optional[str] = Field(default=None, max_length=40, description="The city where the employee resides.")
    state: Optional[str] = Field(default=None, max_length=40, description="The state or province where the employee resides.")
    country: Optional[str] = Field(default=None, max_length=40, description="The country where the employee resides.")
    postal_code: Optional[str] = Field(default=None, max_length=10, description="The postal code for the employee's address.")
    phone: Optional[str] = Field(default=None, max_length=24, description="The employee's phone number.")
    fax: Optional[str] = Field(default=None, max_length=24, description="The employee's fax number.")
    email: Optional[str] = Field(default=None, max_length=60, description="The employee's email address.")
