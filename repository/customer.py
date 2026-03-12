"""
This module defines the CustomerRepository class.
"""

from typing import Union
from psycopg_pool import ConnectionPool
from models.customer import Customer
from .base import BasePgRepository
from database.session import DatabasePoolManager

class CustomerRepository(BasePgRepository[Customer]):
    """
    Repository for accessing Customer data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, Customer, "customer", "customer_id")
