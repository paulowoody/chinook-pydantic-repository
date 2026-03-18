[Back to Index](../README.md)

---

# InvoiceLine Model & Repository

This document details the `InvoiceLine` Pydantic model and its corresponding `InvoiceLineRepository`.

## Pydantic Model: InvoiceLine

The `InvoiceLine` model represents an individual line item on a customer invoice.

- **`invoice_line_id`**: The unique identifier for the invoice line item.
- **`invoice_id`**: The foreign key referencing the invoice this line belongs to.
- **`track_id`**: The foreign key referencing the track that was purchased.
- **`unit_price`**: The unit price of the track at the time of purchase (Decimal).
- **`quantity`**: The quantity of the track purchased (typically 1).

## Repository: InvoiceLineRepository

`InvoiceLineRepository` provides access to the `invoice_line` table.

### Example Usage

```python
from chinook_pydantic_repository.database import DatabasePoolManager
from chinook_pydantic_repository.repository import InvoiceLineRepository

pool = DatabasePoolManager.get_instance(DB_URL)
repo = InvoiceLineRepository(pool)

# Get an invoice line by ID
line = repo.get_by_id(1)
print(f"Line ID: {line.invoice_line_id}, Unit Price: ${line.unit_price}")
```
