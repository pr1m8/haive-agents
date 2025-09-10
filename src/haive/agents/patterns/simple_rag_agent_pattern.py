"""Simple RAG Agent Pattern - Using SimpleAgentV3 as base for RAG implementation.

This module demonstrates creating a RAG (Retrieval-Augmented Generation) agent
using SimpleAgentV3 as the foundation, following the user's request to use
agent.py and SimpleAgentV3 patterns.

The pattern shows:
1. Extending SimpleAgentV3 for specialized functionality
2. Proper state schema composition
3. Tool integration for retrieval
4. Structured output for answers
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.messages_state import MessagesState
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


# Structured output models for RAG
class RetrievalResult(BaseModel):
    """Structured retrieval result."""

    query: str = Field(description="Original search query")
    documents: list[str] = Field(description="Retrieved documents")
    relevance_scores: list[float] = Field(description="Relevance scores for each document")
    total_results: int = Field(description="Total number of results found")


class AnswerWithSources(BaseModel):
    """Structured answer with source citations."""

    answer: str = Field(description="The generated answer")
    sources: list[str] = Field(description="Sources used for the answer")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in the answer")
    follow_up_questions: list[str] = Field(description="Suggested follow-up questions")


# Create retrieval tool
@tool
def retrieve_documents(query: str, top_k: int = 5) -> str:
    """Retrieve documents based on query."""
    # This would connect to your actual vector store
    # For demo, return mock results
    return f"""Retrieved {top_k} documents for query: "{query}"

    Document 1: Overview of the topic discussing {query} in detail...
    Document 2: Technical specifications related to {query}...
    Document 3: Best practices and guidelines for {query}...
    Document 4: Common issues and solutions regarding {query}...
    Document 5: Advanced concepts and future directions of {query}..."""


class SimpleRAGAgent(SimpleAgentV3):
    """Simple RAG Agent built on SimpleAgentV3 foundation.

    This agent extends SimpleAgentV3 to provide RAG capabilities:
    - Document retrieval through tools
    - Context-aware answer generation
    - Source attribution
    - Structured output with confidence scores

    Example:
        >>> rag_agent = SimpleRAGAgent(
        ...     name="knowledge_assistant",
        ...     temperature=0.3,
        ...     debug=True
        ... )
        >>> result = await rag_agent.arun("What is quantum computing?")
    """

    # Override default state schema to use MessagesState
    state_schema: type = Field(default=MessagesState, description="RAG-specific state schema")

    # RAG-specific configuration
    retrieval_top_k: int = Field(default=5, description="Number of documents to retrieve")
    include_sources: bool = Field(default=True, description="Include source citations")
    min_confidence_threshold: float = Field(
        default=0.7, description="Minimum confidence for answers"
    )

    def setup_agent(self) -> None:
        """Setup RAG-specific configuration."""
        # Configure engine for RAG
        if not self.engine:
            self.engine = AugLLMConfig(
                temperature=self.temperature or 0.3,
                system_message="""You are a knowledgeable assistant that answers questions based on retrieved documents.
Always cite your sources and indicate confidence in your answers.
If information is not available in the documents, say so clearly.""",
                tools=[retrieve_documents],
                structured_output_model=(AnswerWithSources if self.include_sources else None),
            )

        # Set up RAG-specific prompt template
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Question: {query}

Retrieved Documents:
{retrieved_documents}

Please provide a comprehensive answer based on the retrieved documents.
Include source citations and suggest follow-up questions.""",
                ),
            ]
        )

        # Call parent setup
        super().setup_agent()

        # Use MessagesState as state schema
        self.state_schema = MessagesState

        # Enable structured output compatibility
        self.structured_output_compatible = True


class IterativeRAGAgent(SimpleRAGAgent):
    """Iterative RAG Agent that refines answers through multiple retrievals.

    This variant performs iterative retrieval and refinement:
    1. Initial retrieval and answer generation
    2. Identifies gaps or unclear areas
    3. Performs targeted follow-up retrievals
    4. Refines the answer with additional context
    """

    max_iterations: int = Field(default=3, description="Maximum refinement iterations")
    refinement_threshold: float = Field(
        default=0.8, description="Confidence threshold for refinement"
    )

    def setup_agent(self) -> None:
        """Setup iterative RAG configuration."""
        super().setup_agent()

        # Add refinement prompt
        self.refinement_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are refining a previous answer with additional context."),
                (
                    "human",
                    """Previous Answer: {previous_answer}
Confidence: {confidence}

Additional Retrieved Documents:
{additional_documents}

Please refine the answer with this new information, improving clarity and completeness.""",
                ),
            ]
        )


class HybridRAGAgent(SimpleRAGAgent):
    """Hybrid RAG Agent combining multiple retrieval strategies.

    This variant uses multiple retrieval approaches:
    - Semantic similarity search
    - Keyword-based retrieval
    - Knowledge graph traversal
    - Combines results for comprehensive answers
    """

    use_semantic_search: bool = Field(default=True, description="Enable semantic search")
    use_keyword_search: bool = Field(default=True, description="Enable keyword search")
    use_knowledge_graph: bool = Field(default=False, description="Enable knowledge graph")

    def setup_agent(self) -> None:
        """Setup hybrid retrieval tools."""

        # Create specialized retrieval tools
        @tool
        def semantic_search(query: str) -> str:
            """Perform semantic similarity search."""
            return f"Semantic search results for: {query}"

        @tool
        def keyword_search(query: str) -> str:
            """Perform keyword-based search."""
            return f"Keyword search results for: {query}"

        # Configure engine with multiple tools
        if not self.engine:
            tools = []
            if self.use_semantic_search:
                tools.append(semantic_search)
            if self.use_keyword_search:
                tools.append(keyword_search)

            self.engine = AugLLMConfig(
                temperature=self.temperature or 0.3,
                system_message="You are a hybrid RAG assistant using multiple retrieval strategies.",
                tools=tools,
                structured_output_model=AnswerWithSources,
            )

        super().setup_agent()


# Factory functions for easy creation
def create_simple_rag_agent(
    name: str = "rag_assistant", temperature: float = 0.3, debug: bool = True, **kwargs
) -> SimpleRAGAgent:
    """Create a simple RAG agent with sensible defaults."""
    return SimpleRAGAgent(name=name, temperature=temperature, debug=debug, **kwargs)


def create_iterative_rag_agent(
    name: str = "iterative_rag", max_iterations: int = 3, **kwargs
) -> IterativeRAGAgent:
    """Create an iterative RAG agent for complex queries."""
    return IterativeRAGAgent(
        name=name, max_iterations=max_iterations, temperature=0.3, debug=True, **kwargs
    )


def create_hybrid_rag_agent(
    name: str = "hybrid_rag", retrieval_strategies: list[str] | None = None, **kwargs
) -> HybridRAGAgent:
    """Create a hybrid RAG agent with multiple retrieval strategies."""
    if retrieval_strategies is None:
        retrieval_strategies = ["semantic", "keyword"]

    return HybridRAGAgent(
        name=name,
        use_semantic_search="semantic" in retrieval_strategies,
        use_keyword_search="keyword" in retrieval_strategies,
        use_knowledge_graph="graph" in retrieval_strategies,
        temperature=0.3,
        debug=True,
        **kwargs,
    )


# Example usage patterns
async def example_simple_rag():
    """Example of using SimpleRAGAgent."""
    # Create agent
    rag = create_simple_rag_agent(name="knowledge_bot")

    # Ask a question
    result = await rag.arun("What are the key principles of machine learning?")

    # Access structured output
    if isinstance(result, dict) and "answer" in result:
        pass


async def example_iterative_rag():
    """Example of iterative refinement."""
    # Create iterative agent
    rag = create_iterative_rag_agent(
        name="deep_researcher", max_iterations=3, refinement_threshold=0.85
    )

    # Complex query requiring refinement
    result = await rag.arun("Explain the relationship between quantum computing and cryptography")

    return result


async def example_hybrid_rag():
    """Example of hybrid retrieval."""
    # Create hybrid agent with all strategies
    rag = create_hybrid_rag_agent(
        name="comprehensive_assistant", retrieval_strategies=["semantic", "keyword", "graph"]
    )

    # Query that benefits from multiple retrieval types
    result = await rag.arun("Find all information about transformer architectures in NLP")

    return result
