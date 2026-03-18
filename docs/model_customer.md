[Back to Index](../README.md)

---

# Customer Model & Repository

This document details the `Customer` Pydantic model and its corresponding `CustomerRepository`.

## Pydantic Model: Customer

The `Customer` model represents a customer in the music database.

- **`customer_id`**: The unique identifier for the customer.
- **`first_name`**: The first name of the customer (max length 40).
- **`last_name`**: The last name of the customer (max length 20).
- **`company`**: The company the customer works for (max length 80).
- **`address`**: The customer's street address (max length 70).
- **`city`**: The city where the customer resides (max length 40).
- **`state`**: The state or province where the customer resides (max length 40).
- **`country`**: The country where the customer resides (max length 40).
- **`postal_code`**: The postal code for the customer's address (max length 10).
- **`phone`**: The customer's phone number (max length 24).
- **`fax`**: The customer's fax number (max length 24).
- **`email`**: The customer's email address (max length 60).
- **`support_rep_id`**: The ID of the employee who provides support to this customer.

## Repository: CustomerRepository

`CustomerRepository` provides access to the `customer` table.

### Example Usage

```python
from chinook_pydantic_repository.database import DatabasePoolManager
from chinook_pydantic_repository.repository import CustomerRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = CustomerRepository(pool)

# Get a customer by ID
customer = repo.get_by_id(1)
print(f"Customer: {customer.first_name} {customer.last_name}")

# Get all customers with pagination
customers = repo.get_all(limit=10)
for c in customers:
    print(c.email)
```
