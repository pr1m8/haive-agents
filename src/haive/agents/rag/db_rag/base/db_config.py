from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, TypeVar, Generic
from pydantic import BaseModel, Field
import os

# Type variable for the database connection object
T = TypeVar('T')

class BaseDBConfig(ABC, BaseModel, Generic[T]):
    """
    Abstract base configuration model for database connections.
    
    This class defines the common interface that all database
    configurations should implement, regardless of database type.
    """
    
    db_type: str = Field(
        description="Type of database (e.g., 'sql', 'graph', 'document')"
    )
    
    @abstractmethod
    def get_connection_string(self) -> str:
        """Generate a connection string for the database."""
        pass
    
    @abstractmethod
    def get_db(self) -> Optional[T]:
        """Creates and returns a database connection object."""
        pass
    
    @abstractmethod
    def get_db_schema(self) -> Optional[Dict[str, Any]]:
        """Retrieves the schema information from the database."""
        pass