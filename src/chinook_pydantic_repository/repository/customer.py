"""
This module defines the CustomerRepository class.
"""

from psycopg_pool import ConnectionPool

from chinook_pydantic_repository.database.session import DatabasePoolManager
from chinook_pydantic_repository.models.customer import Customer

from .base import BasePgRepository


class CustomerRepository(BasePgRepository[Customer]):
    """
    Repository for accessing Customer data.
    """

    def __init__(self, db_url_or_pool: str | ConnectionPool | DatabasePoolManager):
        super().__init__(db_url_or_pool, Customer, "customer", "customer_id")
