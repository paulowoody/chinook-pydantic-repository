[Back to Index](../README.md)

---

# Invoice Model & Repository

This document details the `Invoice` Pydantic model and its corresponding `InvoiceRepository`.

## Pydantic Model: Invoice

The `Invoice` model represents a customer invoice in the database.

- **`invoice_id`**: The unique identifier for the invoice.
- **`customer_id`**: The foreign key referencing the customer associated with the invoice.
- **`invoice_date`**: The date the invoice was generated (datetime).
- **`billing_address`**: The billing street address (max length 70).
- **`billing_city`**: The billing city (max length 40).
- **`billing_state`**: The billing state or province (max length 40).
- **`billing_country`**: The billing country (max length 40).
- **`billing_postal_code`**: The billing postal code (max length 10).
- **`total`**: The total amount for the invoice (Decimal).

## Repository: InvoiceRepository

`InvoiceRepository` provides access to the `invoice` table.

### Example Usage

```python
from database import DatabasePoolManager
from repository import InvoiceRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = InvoiceRepository(pool)

# Get an invoice by ID
invoice = repo.get_by_id(1)
print(f"Invoice Date: {invoice.invoice_date}, Total: ${invoice.total}")
```
