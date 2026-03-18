"""
This module defines the EmployeeRepository class.
"""

from typing import Union
from psycopg_pool import ConnectionPool
from chinook_pydantic_repository.models.employee import Employee
from .base import BasePgRepository
from chinook_pydantic_repository.database.session import DatabasePoolManager

class EmployeeRepository(BasePgRepository[Employee]):
    """
    Repository for accessing Employee data.
    """
    def __init__(self, db_url_or_pool: Union[str, ConnectionPool, DatabasePoolManager]):
        super().__init__(db_url_or_pool, Employee, "employee", "employee_id")
