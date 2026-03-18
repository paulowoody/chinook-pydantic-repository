"""
This module defines the CustomerRepository class.
"""

from typing import Union
from psycopg_pool import ConnectionPool
from chinook_pydantic_repository.models.customer import Customer
from .base import BasePgRepository
from chinook_pydantic_repository.database.session import DatabasePoolManager

class CustomerRepository(BasePgRepository[Customer]):
    """
    Repository for accessing Customer data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, Customer, "customer", "customer_id")
