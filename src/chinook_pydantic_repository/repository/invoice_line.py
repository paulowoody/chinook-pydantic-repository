"""
This module defines the InvoiceLineRepository class.
"""

from psycopg_pool import ConnectionPool

from chinook_pydantic_repository.database.session import DatabasePoolManager
from chinook_pydantic_repository.models.invoice_line import InvoiceLine

from .base import BasePgRepository


class InvoiceLineRepository(BasePgRepository[InvoiceLine]):
    """
    Repository for accessing InvoiceLine data.
    """

    def __init__(self, db_url_or_pool: str | ConnectionPool | DatabasePoolManager):
        super().__init__(db_url_or_pool, InvoiceLine, "invoice_line", "invoice_line_id")
