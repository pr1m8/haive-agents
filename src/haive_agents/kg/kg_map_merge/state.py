from typing import List, Optional, Dict, Any, Literal, Annotated
from pydantic import BaseModel, Field
from langchain_core.documents import Document
from langchain_community.graphs.graph_document import GraphDocument
from langgraph.graph import START, END
from langgraph.types import Command, Send
import operator

# Import models
from haive_agents.document_agents.kg.kg_map_merge.models import (
    KnowledgeGraph, 
    EntityNode, 
    EntityRelationship
)

class KnowledgeGraphState(BaseModel):
    """
    State model for the parallel knowledge graph transformer.
    """
    contents: List[Document]
    
    # Graph documents and knowledge graphs
    graph_documents: Annotated[List[GraphDocument], operator.add] = Field(default_factory=list)
    knowledge_graphs: Annotated[List[KnowledgeGraph], operator.add] = Field(default_factory=list)
    final_knowledge_graph: Optional[KnowledgeGraph] = Field(default=None)
    
    # Extracted components
    nodes: List[EntityNode] = Field(default_factory=list)
    relationships: List[EntityRelationship] = Field(default_factory=list)
    
    # Concurrent-safe index tracking
    index: int = Field(default=0)
    
    def should_continue(self) -> Literal["map_graph_documents", "map_nodes", "map_relationships", "merge_graphs", "end"]:
        """
        Determine the next step in the graph creation process.
        """
        if self.index < len(self.contents):
            return "map_graph_documents"
        elif not self.nodes:
            return "map_nodes"
        elif not self.relationships:
            return "map_relationships"
        elif self.graph_documents or self.knowledge_graphs:
            return "merge_graphs"
        else:
            return "end"