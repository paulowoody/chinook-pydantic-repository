"""
Package for core database infrastructure and session management.

This `__init__.py` re-exports the DatabasePoolManager to provide
a clean entry point for database configuration.
"""

from .session import DatabasePoolManager

# The `__all__` list defines the public interface of the `database` package.
#
# By exporting `DatabasePoolManager` here, we allow users to import it
# directly from the package root:
# `from chinook_pydantic_repository.database import DatabasePoolManager`
#
# This keeps the consumer's code cleaner by hiding the internal module
# structure (`.session`).
__all__ = [
    "DatabasePoolManager",
]
