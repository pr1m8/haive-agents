"""Test HyDE RAG Sequential Pattern: Hypothetical Document Generation → Enhanced Retrieval → Answer Generation.

This test demonstrates:
1. HyDE (Hypothetical Document Embeddings) pattern for improved retrieval
2. Sequential multi-agent flow with HyDE → Retrieval → Answer
3. How hypothetical documents bridge the semantic gap between queries and documents
4. Real component testing with no mocks
5. Structured output for hypothetical document generation

Key Pattern:
SimpleAgent (HyDE generator) → BaseRAGAgent (enhanced retrieval) → SimpleAgent (answer generator)

HyDE Process:
1. Generate a hypothetical document that would answer the query
2. Use the hypothetical document for similarity search (better semantic matching)
3. Retrieve real documents based on hypothetical document embeddings
4. Generate final answer from retrieved real documents
"""

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
import pytest

from haive.agents.multi.base import SequentialAgent
from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.vectorstore import VectorStoreConfig, VectorStoreProvider
from haive.core.models.embeddings.base import HuggingFaceEmbeddingConfig
from haive.core.models.llm.base import AzureLLMConfig


# Structured output models
class HyDEResult(BaseModel):
    """Hypothetical Document Enhanced (HyDE) result."""

    hypothetical_doc: str = Field(
        description="Generated hypothetical document that would answer the query"
    )
    refined_query: str = Field(
        description="Query refined based on the hypothetical document"
    )
    confidence: float = Field(
        description="Confidence score in the hypothesis (0.0 to 1.0)", ge=0.0, le=1.0
    )
    key_concepts: list[str] = Field(
        description="Key concepts extracted from the query", default_factory=list
    )


class EnhancedAnswer(BaseModel):
    """Enhanced answer with HyDE context."""

    question: str = Field(description="Original question")
    answer: str = Field(description="Comprehensive answer")
    hypothetical_context: str = Field(
        description="Summary of hypothetical document used"
    )
    retrieved_sources: list[str] = Field(description="Sources from retrieved documents")
    confidence_score: float = Field(description="Overall confidence (0-1)")
    improvements_from_hyde: list[str] = Field(
        description="How HyDE improved the retrieval", default_factory=list
    )


# HyDE Generation Prompt
HYDE_GENERATION_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert at generating hypothetical documents that would answer questions.
Your task is to write a detailed, informative document that contains the information needed to answer the given question.

Guidelines:
- Write as if you are creating an authoritative reference document
- Include specific details, examples, and explanations
- Use clear, factual language
- Make the document comprehensive enough to fully answer the question
- Extract key concepts from the question
- Do not mention that this is hypothetical - write as if stating facts

Focus on creating content that would be semantically similar to real documents about this topic.""",
        ),
        (
            "human",
            """Generate a hypothetical document that would contain the answer to this question:

Question: {query}

Please provide a comprehensive hypothetical document that addresses all aspects of the question.""",
        ),
    ]
)


class TestHyDERAGSequential:
    """Test HyDE RAG sequential pattern."""

    @pytest.fixture
    def technical_documents(self):
        """Create technical documents for testing HyDE effectiveness."""
        return [
            Document(
                page_content="""Distributed systems are computing infrastructures where components
                located on networked computers communicate and coordinate through message passing.
                Key characteristics include concurrency, lack of global clock, and independent failures.
                Common patterns include master-slave, peer-to-peer, and microservices architectures.""",
                metadata={
                    "source": "distributed_systems_overview.md",
                    "topic": "architecture",
                },
            ),
            Document(
                page_content="""Consensus algorithms like Raft and Paxos ensure distributed systems
                maintain consistency despite failures. Raft divides time into terms and uses leader
                election. Paxos uses a two-phase protocol with prepare and accept phases. Both
                guarantee safety but differ in understandability and implementation complexity.""",
                metadata={"source": "consensus_algorithms.md", "topic": "algorithms"},
            ),
            Document(
                page_content="""CAP theorem states that distributed systems can guarantee at most two
                of: Consistency, Availability, and Partition tolerance. Modern systems often choose
                AP (eventually consistent) or CP (strongly consistent) based on requirements.
                Examples: Cassandra (AP), Zookeeper (CP), DynamoDB (configurable).""",
                metadata={"source": "cap_theorem.md", "topic": "theory"},
            ),
            Document(
                page_content="""Microservices architecture decomposes applications into small,
                independent services. Benefits include independent deployment, technology diversity,
                and fault isolation. Challenges include distributed debugging, network latency,
                and data consistency. Common patterns: API Gateway, Service Mesh, Saga pattern.""",
                metadata={"source": "microservices_patterns.md", "topic": "patterns"},
            ),
            Document(
                page_content="""Event-driven architectures use events to trigger actions across
                distributed components. Patterns include Event Sourcing (storing state changes as
                events), CQRS (separating reads and writes), and Event Streaming with platforms
                like Kafka. Benefits: loose coupling, scalability, audit trails.""",
                metadata={"source": "event_driven_systems.md", "topic": "patterns"},
            ),
        ]

    @pytest.fixture
    def vector_store_config(self, technical_documents):
        """Create vector store with technical documents."""
        return VectorStoreConfig(
            name="hyde_test_store",
            documents=technical_documents,
            vector_store_provider=VectorStoreProvider.FAISS,
            embedding_model=HuggingFaceEmbeddingConfig(
                model="sentence-transformers/all-MiniLM-L6-v2"
            ),
        )

    @pytest.fixture
    def hyde_generator(self):
        """Create HyDE generator agent."""
        return SimpleAgent(
            name="hyde_generator",
            engine=AugLLMConfig(
                llm_config=AzureLLMConfig(
                    model="gpt-4o",
                    temperature=0.7,  # Some creativity for hypothetical documents
                ),
                prompt_template=HYDE_GENERATION_PROMPT,
                system_message="Generate comprehensive hypothetical documents.",
            ),
            structured_output_model=HyDEResult,
            structured_output_version="v2",
        )

    @pytest.fixture
    def rag_retriever(self, vector_store_config):
        """Create RAG retriever agent."""
        return BaseRAGAgent(name="enhanced_retriever", engine=vector_store_config)

    @pytest.fixture
    def answer_generator(self):
        """Create answer generator with HyDE awareness."""
        return SimpleAgent(
            name="hyde_aware_answerer",
            engine=AugLLMConfig(
                llm_config=AzureLLMConfig(model="gpt-4o", temperature=0.3),
                system_message="""You are an expert answer generator that uses HyDE-enhanced retrieval.
                Given a hypothetical document and retrieved real documents, generate a comprehensive answer.
                Explain how the hypothetical document helped improve retrieval.""",
            ),
            structured_output_model=EnhancedAnswer,
            structured_output_version="v2",
        )

    def test_hyde_components_creation(
        self, hyde_generator, rag_retriever, answer_generator
    ):
        """Test all HyDE components are created correctly."""
        assert hyde_generator.name == "hyde_generator"
        assert hyde_generator.structured_output_model == HyDEResult

        assert rag_retriever.name == "enhanced_retriever"
        assert hasattr(rag_retriever, "retriever")

        assert answer_generator.name == "hyde_aware_answerer"
        assert answer_generator.structured_output_model == EnhancedAnswer

    def test_hyde_generation(self, hyde_generator):
        """Test hypothetical document generation."""
        query = "How do consensus algorithms work in distributed systems?"

        # Generate hypothetical document
        result = hyde_generator.run(query)

        # Check for HyDEResult
        if hasattr(result, "hypothetical_doc"):

            assert len(result.hypothetical_doc) > 100
            assert 0.0 <= result.confidence <= 1.0
        else:
            pass

    def test_manual_hyde_rag_flow(
        self, hyde_generator, rag_retriever, answer_generator
    ):
        """Test manual HyDE → Retrieval → Answer flow."""
        query = "What are the trade-offs in the CAP theorem for distributed databases?"

        # Step 1: Generate hypothetical document
        hyde_result = hyde_generator.run(query)

        if hasattr(hyde_result, "hypothetical_doc"):
            hypothetical_doc = hyde_result.hypothetical_doc
        else:
            hypothetical_doc = str(hyde_result)

        # Step 2: Use hypothetical document for retrieval
        # Use the hypothetical document as the query for better semantic matching
        retrieval_result = rag_retriever.run({"query": hypothetical_doc})

        retrieved_docs = []
        if (
            isinstance(retrieval_result, dict)
            and "retrieved_documents" in retrieval_result
        ):
            retrieved_docs = retrieval_result["retrieved_documents"]

            for _i, _doc in enumerate(retrieved_docs[:3]):
                pass

        # Step 3: Generate answer with HyDE context

        answer_context = f"""Original Question: {query}

Hypothetical Document Used for Retrieval:
{hypothetical_doc}

Retrieved Real Documents:
{chr(10).join([f"{i+1}. From {doc.metadata.get('source')}: {doc.page_content}"
                for i, doc in enumerate(retrieved_docs)])}

Generate a comprehensive answer explaining how HyDE improved the retrieval."""

        answer = answer_generator.run(answer_context)

        if hasattr(answer, "answer"):
            pass

        # Verify the flow
        assert len(hypothetical_doc) > 100
        assert len(retrieved_docs) > 0
        assert answer is not None

    def test_hyde_vs_standard_retrieval(self, hyde_generator, rag_retriever):
        """Compare HyDE retrieval vs standard retrieval."""
        query = "Explain event-driven architecture patterns"

        # Standard retrieval (direct query)
        standard_result = rag_retriever.run({"query": query})
        standard_docs = (
            standard_result.get("retrieved_documents", [])
            if isinstance(standard_result, dict)
            else []
        )

        for _doc in standard_docs[:2]:
            pass

        # HyDE retrieval (using hypothetical document)
        hyde_result = hyde_generator.run(query)
        hypothetical_doc = (
            hyde_result.hypothetical_doc
            if hasattr(hyde_result, "hypothetical_doc")
            else str(hyde_result)
        )

        hyde_retrieval = rag_retriever.run({"query": hypothetical_doc})
        hyde_docs = (
            hyde_retrieval.get("retrieved_documents", [])
            if isinstance(hyde_retrieval, dict)
            else []
        )

        for _doc in hyde_docs[:2]:
            pass

        # Compare results
        {doc.metadata.get("source") for doc in standard_docs}
        {doc.metadata.get("source") for doc in hyde_docs}

    def test_complex_technical_query(
        self, hyde_generator, rag_retriever, answer_generator
    ):
        """Test HyDE with complex technical query."""
        complex_query = """Compare and contrast different consensus algorithms in distributed systems,
        specifically focusing on their fault tolerance, performance characteristics, and use cases."""

        # Generate hypothetical document
        hyde_result = hyde_generator.run(complex_query)

        if hasattr(hyde_result, "key_concepts"):
            pass

        # Retrieve with HyDE
        hypothetical = (
            hyde_result.hypothetical_doc
            if hasattr(hyde_result, "hypothetical_doc")
            else str(hyde_result)
        )
        retrieval = rag_retriever.run({"query": hypothetical})

        docs = (
            retrieval.get("retrieved_documents", [])
            if isinstance(retrieval, dict)
            else []
        )

        # Generate comprehensive answer
        context = f"""Question: {complex_query}

HyDE Document: {hypothetical[:500]}...

Retrieved Documents:
{chr(10).join([f"- {doc.page_content[:200]}..." for doc in docs[:3]])}"""

        answer = answer_generator.run(context)

        assert len(docs) > 0
        assert answer is not None

    def test_sequential_multi_agent_hyde(self, vector_store_config):
        """Test SequentialAgent with HyDE flow."""
        # Create agents
        hyde_gen = SimpleAgent(
            name="hyde_gen",
            engine=AugLLMConfig(
                prompt_template=HYDE_GENERATION_PROMPT,
                system_message="Generate hypothetical documents",
            ),
            structured_output_model=HyDEResult,
            structured_output_version="v2",
        )

        retriever = BaseRAGAgent(name="retriever", engine=vector_store_config)

        answerer = SimpleAgent(
            name="answerer",
            engine=AugLLMConfig(
                system_message="Generate answers from retrieved documents"
            ),
        )

        # Create sequential HyDE system
        hyde_system = SequentialAgent(
            name="hyde_rag_system", agents=[hyde_gen, retriever, answerer]
        )

        # Verify structure
        assert len(hyde_system.agents) == 3
        assert hyde_system.agents[0].name == "hyde_gen"
        assert hyde_system.agents[1].name == "retriever"
        assert hyde_system.agents[2].name == "answerer"

    @pytest.mark.asyncio
    async def test_async_hyde_flow(
        self, hyde_generator, rag_retriever, answer_generator
    ):
        """Test async HyDE flow."""
        query = "What are microservices design patterns?"

        # Async HyDE generation
        hyde_result = await hyde_generator.arun(query)

        # Async retrieval
        hypothetical = (
            hyde_result.hypothetical_doc
            if hasattr(hyde_result, "hypothetical_doc")
            else str(hyde_result)
        )
        retrieval = await rag_retriever.arun({"query": hypothetical})

        docs = (
            retrieval.get("retrieved_documents", [])
            if isinstance(retrieval, dict)
            else []
        )

        # Async answer generation
        context = f"Query: {query}\nHyDE: {hypothetical[:200]}...\nDocs: {len(docs)}"
        answer = await answer_generator.arun(context)

        assert answer is not None

    def test_hyde_edge_cases(self, hyde_generator, rag_retriever):
        """Test HyDE with edge cases."""
        # Very specific technical query
        specific_query = "What is the time complexity of leader election in Raft?"
        hyde_generator.run(specific_query)

        # Very broad query
        broad_query = "Tell me about computer systems"
        hyde_generator.run(broad_query)

        # Query with no good matches
        no_match_query = "What is quantum blockchain?"
        hyde_result3 = hyde_generator.run(no_match_query)

        if hasattr(hyde_result3, "hypothetical_doc"):
            retrieval = rag_retriever.run({"query": hyde_result3.hypothetical_doc})
            (
                retrieval.get("retrieved_documents", [])
                if isinstance(retrieval, dict)
                else []
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
