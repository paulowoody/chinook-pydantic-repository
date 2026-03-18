"""
This module defines the InvoiceRepository class.
"""

from typing import Union
from psycopg_pool import ConnectionPool
from chinook_pydantic_repository.models.invoice import Invoice
from .base import BasePgRepository
from chinook_pydantic_repository.database.session import DatabasePoolManager

class InvoiceRepository(BasePgRepository[Invoice]):
    """
    Repository for accessing Invoice data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, Invoice, "invoice", "invoice_id")
