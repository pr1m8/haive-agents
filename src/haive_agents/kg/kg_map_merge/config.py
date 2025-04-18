from haive_core.engine.agent.agent import AgentConfig
from haive_core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List
from langchain_core.documents import Document   
from haive_agents.document_agents.kg.kg_map_merge.models import KnowledgeGraph,EntityNode,EntityRelationship
class ParallelKGTransformerConfig(AgentConfig):
    """
    Configuration for the Parallel Knowledge Graph Transformer.
    """
    contents: List[Document]
    graph_extraction_config: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            name="graph_extractor",
            prompt_template=ChatPromptTemplate.from_messages([
                ("system", """Extract and refine the knowledge graph from the given text.
                Focus on identifying key entities and their relationships.
                Provide a comprehensive and accurate representation."""),
                ("human", "Extract knowledge graph from this text:\n{context}")
            ])
        )
    )
    graph_merge_config: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            name="graph_merger",
            prompt_template=ChatPromptTemplate.from_messages([
                ("system", """Merge and reconcile multiple knowledge graphs.
                Identify consistent relationships, resolve conflicts,
                and create a comprehensive knowledge representation."""),
                ("human", """Merge these knowledge graphs:
                {graph_contexts}
                
                Provide a unified and refined knowledge graph.""")
            ])
        )
    )
