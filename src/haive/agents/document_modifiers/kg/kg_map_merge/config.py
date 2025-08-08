from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from pydantic import Field


class ParallelKGTransformerConfig(AgentConfig):
    """Configuration for the Parallel Knowledge Graph Transformer."""

    contents: list[Document]
    graph_extraction_config: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            name="graph_extractor",
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        """Extract and refine the knowledge graph from the given text.
                Focus on identifying key entities and their relationships.
                Provide a comprehensive and accurate representation.""",
                    ),
                    ("human", "Extract knowledge graph from this text:\n{context}"),
                ]
            ),
        )
    )
    graph_merge_config: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            name="graph_merger",
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        """Merge and reconcile multiple knowledge graphs.
                Identify consistent relationships, resolve conflicts,
                and create a comprehensive knowledge representation.""",
                    ),
                    (
                        "human",
                        """Merge these knowledge graphs:
                {graph_contexts}

                Provide a unified and refined knowledge graph.""",
                    ),
                ]
            ),
        )
    )
    checkpoint_mode: str = Field(
        default="async", description="The checkpoint mode for the iterative summarizer."
    )


class ParallelKGAgentConfig(AgentConfig):
    """Configuration for the Parallel Knowledge Graph Agent with structured extraction."""

    contents: list[Document] = Field(
        default_factory=list,
        description="Documents to process for knowledge graph extraction",
    )

    max_parallel_workers: int = Field(
        default=4,
        description="Maximum number of parallel workers for document processing",
    )

    schema_extraction_config: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            name="schema_extractor",
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        """Analyze the documents and extract the schema for entities and relationships.
                    Identify what types of entities and relationships are present in the content.""",
                    ),
                    ("human", "Extract schema from these documents:\n{contents}"),
                ]
            ),
        )
    )

    kg_extraction_config: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            name="kg_extractor",
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        """Extract entities and relationships from the document following the provided schema.
                    Be precise and comprehensive in your extraction.""",
                    ),
                    ("human", "Schema:\n{schema}\n\nDocument:\n{document}"),
                ]
            ),
        )
    )

    merge_analysis_config: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            name="merge_analyzer",
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        """Analyze multiple knowledge graph fragments and merge them into a unified graph.
                    Resolve entity duplicates and relationship conflicts.""",
                    ),
                    ("human", "Merge these knowledge graph fragments:\n{fragments}"),
                ]
            ),
        )
    )
