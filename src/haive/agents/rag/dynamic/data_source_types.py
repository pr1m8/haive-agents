from enum import Enum
from pydantic import BaseModel, Field
from haive.core.models.retriever.base import RetrieverConfig
from typing import Optional, Dict, Any

class DataSourceType(str, Enum):
    """Types of data sources available."""
    VECTOR_DB = "vector_db"
    GRAPH_DB = "graph_db"
    WEB_SEARCH = "web_search"
    SQL_DB = "sql_db"
    API = "api"
    DOCUMENT_STORE = "document_store"

