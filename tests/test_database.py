import pytest
from unittest.mock import MagicMock, patch
from chinook_pydantic_repository.database.session import DatabasePoolManager

# Dummy connection string
TEST_DB_URL = "postgresql://user:pass@localhost:5432/testdb"

@pytest.fixture(autouse=True)
def reset_singleton():
    """Reset the DatabasePoolManager singleton before each test."""
    DatabasePoolManager._instance = None
    yield

def test_pool_manager_singleton():
    """Verify that DatabasePoolManager follows the singleton pattern."""
    with patch("chinook_pydantic_repository.database.session.ConnectionPool"):
        manager1 = DatabasePoolManager.get_instance(TEST_DB_URL)
        manager2 = DatabasePoolManager.get_instance(TEST_DB_URL)
        
        assert manager1 is manager2

def test_pool_manager_initialization():
    """Verify that the pool is initialized with correct parameters."""
    with patch("chinook_pydantic_repository.database.session.ConnectionPool") as mock_pool_cls:
        manager = DatabasePoolManager(TEST_DB_URL, min_size=2, max_size=5)
        
        mock_pool_cls.assert_called_once()
        args, kwargs = mock_pool_cls.call_args
        assert args[0] == TEST_DB_URL
        assert kwargs["min_size"] == 2
        assert kwargs["max_size"] == 5
        assert "row_factory" in kwargs["kwargs"]

def test_pool_manager_jdbc_strip():
    """Verify that 'jdbc:' prefix is stripped from the URL."""
    jdbc_url = "jdbc:postgresql://localhost:5432/db"
    expected_url = "postgresql://localhost:5432/db"
    
    with patch("chinook_pydantic_repository.database.session.ConnectionPool") as mock_pool_cls:
        DatabasePoolManager(jdbc_url)
        assert mock_pool_cls.call_args[0][0] == expected_url

def test_pool_manager_connection_call():
    """Verify that connection() calls the underlying pool's connection method."""
    with patch("chinook_pydantic_repository.database.session.ConnectionPool") as mock_pool_cls:
        mock_pool_instance = mock_pool_cls.return_value
        manager = DatabasePoolManager(TEST_DB_URL)
        
        manager.connection()
        mock_pool_instance.connection.assert_called_once()

def test_pool_manager_close():
    """Verify that close() closes the underlying pool."""
    with patch("chinook_pydantic_repository.database.session.ConnectionPool") as mock_pool_cls:
        mock_pool_instance = mock_pool_cls.return_value
        manager = DatabasePoolManager(TEST_DB_URL)
        
        manager.close()
        mock_pool_instance.close.assert_called_once()
