"""
This module defines the InvoiceLineRepository class.
"""

from typing import Union
from psycopg_pool import ConnectionPool
from models.invoice_line import InvoiceLine
from .base import BasePgRepository
from database.session import DatabasePoolManager

class InvoiceLineRepository(BasePgRepository[InvoiceLine]):
    """
    Repository for accessing InvoiceLine data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, InvoiceLine, "invoice_line", "invoice_line_id")
