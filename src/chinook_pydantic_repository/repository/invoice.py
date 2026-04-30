"""
This module defines the InvoiceRepository class.
"""

from psycopg_pool import ConnectionPool

from chinook_pydantic_repository.database.session import DatabasePoolManager
from chinook_pydantic_repository.models.invoice import Invoice

from .base import BasePgRepository


class InvoiceRepository(BasePgRepository[Invoice]):
    """
    Repository for accessing Invoice data.
    """

    def __init__(self, db_url_or_pool: str | ConnectionPool | DatabasePoolManager):
        super().__init__(db_url_or_pool, Invoice, "invoice", "invoice_id")
