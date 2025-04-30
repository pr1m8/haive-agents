from pydantic import BaseModel, Field
from typing import Dict, Any, Optional      

class MemoryItem(BaseModel):
    """Base memory item class for structured and unstructured memories."""
    content: str
    source: str = Field(default="conversation")
    timestamp: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class KnowledgeTriple(BaseModel):
    """Structured knowledge triple for graph-based memory."""
    subject: str
    predicate: str
    object_: str
    confidence: float = Field(default=1.0)
    source: str = Field(default="conversation")
    timestamp: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)