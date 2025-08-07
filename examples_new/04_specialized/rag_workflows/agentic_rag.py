"""
Agentic RAG Example - Advanced RAG with Document Grading and Query Rewriting
===========================================================================

This example demonstrates an advanced RAG system with:
- Query analysis and rewriting for better retrieval
- Document relevance grading
- Multi-step reasoning with fallback strategies
- Source citation and confidence scoring

This represents a more sophisticated approach to RAG that can handle
complex queries and provide more accurate, well-sourced answers.
"""

import asyncio
from typing import Any, Dict, List, Optional

from haive.core.embeddings import HuggingFaceEmbeddings
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Structured output models
class QueryAnalysis(BaseModel):
    """Analysis of user query for optimization."""

    original_query: str = Field(description="The original user query")
    query_type: str = Field(
        description="Type: factual, analytical, comparative, or exploratory"
    )
    key_concepts: List[str] = Field(description="Main concepts to search for")
    rewritten_query: str = Field(description="Optimized query for better retrieval")
    search_strategy: str = Field(description="Strategy: exact, semantic, or hybrid")


class DocumentRelevance(BaseModel):
    """Relevance assessment of retrieved documents."""

    document_id: int = Field(description="Document index")
    relevance_score: float = Field(ge=0.0, le=1.0, description="Relevance score 0-1")
    is_relevant: bool = Field(description="Whether document is relevant")
    reasoning: str = Field(description="Why this document is/isn't relevant")


class AnswerWithSources(BaseModel):
    """Structured answer with sources and confidence."""

    answer: str = Field(description="The complete answer to the user's question")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence in the answer")
    sources: List[str] = Field(description="Source documents used")
    key_facts: List[str] = Field(description="Key facts extracted from sources")
    needs_clarification: bool = Field(
        description="Whether the query needs clarification"
    )
    clarification_questions: Optional[List[str]] = Field(default=None)


class AgenticRAG:
    """Advanced RAG system with multiple specialized agents."""

    def __init__(self):
        # Initialize embeddings and vector store
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vector_store = InMemoryVectorStore(self.embeddings)

        # Query Analyzer Agent
        self.query_analyzer = SimpleAgentV3(
            name="query_analyzer",
            engine=AugLLMConfig(
                temperature=0.3,
                structured_output_model=QueryAnalysis,
                system_message="""You are a query analysis expert. Analyze user queries to:
                1. Identify the query type and intent
                2. Extract key concepts for search
                3. Rewrite queries for better retrieval
                4. Suggest appropriate search strategies""",
            ),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    ("system", "{system_message}"),
                    ("human", "Analyze this query: {query}"),
                ]
            ),
        )

        # Document Grader Agent
        self.doc_grader = SimpleAgentV3(
            name="document_grader",
            engine=AugLLMConfig(
                temperature=0.2,
                structured_output_model=DocumentRelevance,
                system_message="""You are a document relevance expert. Grade documents based on:
                1. Direct relevance to the query
                2. Information quality and completeness
                3. Factual accuracy
                Be strict - only mark truly relevant documents as relevant.""",
            ),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    ("system", "{system_message}"),
                    (
                        "human",
                        """Query: {query}
                
Document to grade:
{document}

Assess the relevance of this document to the query.""",
                    ),
                ]
            ),
        )

        # Answer Generator Agent
        self.answer_generator = SimpleAgentV3(
            name="answer_generator",
            engine=AugLLMConfig(
                temperature=0.4,
                structured_output_model=AnswerWithSources,
                system_message="""You are an expert at generating comprehensive answers from sources.
                - Synthesize information from multiple sources
                - Cite sources for key claims
                - Express appropriate confidence levels
                - Identify when information is incomplete""",
            ),
            prompt_template=ChatPromptTemplate.from_messages(
                [
                    ("system", "{system_message}"),
                    (
                        "human",
                        """Query: {query}

Relevant Documents:
{context}

Generate a comprehensive answer with sources and confidence assessment.""",
                    ),
                ]
            ),
        )

        # Create retrieval tool
        @tool
        def search_documents(query: str, k: int = 5) -> List[Dict[str, Any]]:
            """Search for relevant documents in the knowledge base."""
            # Note: In real implementation, this would be async
            # For now, using sync for simplicity
            docs = asyncio.run(self.vector_store.asimilarity_search(query, k=k))
            return [
                {"content": doc.page_content, "metadata": doc.metadata, "id": i}
                for i, doc in enumerate(docs)
            ]

        # Reasoning Agent with tools
        self.reasoning_agent = ReactAgent(
            name="rag_reasoner",
            engine=AugLLMConfig(
                temperature=0.5,
                system_message="""You are a RAG orchestrator. Your job is to:
                1. Use the search tool to find relevant documents
                2. Reason about whether you have enough information
                3. Search again with different queries if needed
                4. Compile the final context for answer generation""",
            ),
            tools=[search_documents],
        )

    async def add_documents(self, documents: List[Document]):
        """Add documents to the vector store."""
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300, chunk_overlap=50, length_function=len
        )

        all_chunks = []
        for doc in documents:
            chunks = text_splitter.split_documents([doc])
            all_chunks.extend(chunks)

        await self.vector_store.aadd_documents(all_chunks)
        return len(all_chunks)

    async def process_query(self, query: str) -> AnswerWithSources:
        """Process a query through the full agentic RAG pipeline."""
        print(f"\n🔍 Processing query: {query}")

        # Step 1: Analyze and rewrite query
        print("\n1️⃣ Analyzing query...")
        analysis = await self.query_analyzer.arun({"query": query})
        print(f"   Query type: {analysis.query_type}")
        print(f"   Key concepts: {', '.join(analysis.key_concepts)}")
        print(f"   Rewritten: {analysis.rewritten_query}")

        # Step 2: Use reasoning agent to search iteratively
        print("\n2️⃣ Searching for relevant documents...")
        search_prompt = f"""Find relevant documents for this query: {analysis.rewritten_query}
        
Focus on these concepts: {', '.join(analysis.key_concepts)}
Search strategy: {analysis.search_strategy}

If initial results aren't sufficient, try alternative search terms."""

        reasoning_result = await self.reasoning_agent.arun(search_prompt)

        # Step 3: Extract documents from reasoning (in real implementation)
        # For this example, we'll do a direct search
        retrieved_docs = await self.vector_store.asimilarity_search(
            analysis.rewritten_query, k=5
        )

        # Step 4: Grade documents for relevance
        print("\n3️⃣ Grading document relevance...")
        graded_docs = []
        for i, doc in enumerate(retrieved_docs):
            grade = await self.doc_grader.arun(
                {"query": query, "document": doc.page_content}
            )

            if grade.is_relevant:
                graded_docs.append((doc, grade))
                print(f"   ✅ Doc {i+1}: Relevant (score: {grade.relevance_score:.2f})")
            else:
                print(f"   ❌ Doc {i+1}: Not relevant - {grade.reasoning}")

        # Step 5: Generate answer from relevant documents
        print("\n4️⃣ Generating answer...")
        if graded_docs:
            context = "\n\n".join(
                [
                    f"[Source {i+1} - {doc.metadata.get('source', 'Unknown')}]:\n{doc.page_content}"
                    for i, (doc, _) in enumerate(graded_docs)
                ]
            )

            answer = await self.answer_generator.arun(
                {"query": query, "context": context}
            )
        else:
            # No relevant documents found
            answer = AnswerWithSources(
                answer="I couldn't find relevant information to answer your question.",
                confidence=0.1,
                sources=[],
                key_facts=[],
                needs_clarification=True,
                clarification_questions=[
                    "Could you provide more context?",
                    "What specific aspect interests you?",
                ],
            )

        return answer


async def main():
    """Run the agentic RAG example."""
    print("Agentic RAG Example - Advanced Document Q&A\n")
    print("=" * 50)

    # Initialize the agentic RAG system
    rag_system = AgenticRAG()

    # Create comprehensive documents about machine learning
    documents = [
        Document(
            page_content="""
            Machine learning is a subset of artificial intelligence that enables
            systems to learn and improve from experience without being explicitly
            programmed. It focuses on developing algorithms that can access data
            and use it to learn for themselves. The process involves feeding data
            to algorithms and allowing them to identify patterns and make decisions
            with minimal human intervention.
            """,
            metadata={
                "source": "ml_intro.txt",
                "topic": "introduction",
                "level": "beginner",
            },
        ),
        Document(
            page_content="""
            There are three main types of machine learning:
            1. Supervised Learning: Uses labeled data to train models. The algorithm
               learns from input-output pairs. Common applications include classification
               and regression tasks.
            2. Unsupervised Learning: Works with unlabeled data to discover hidden
               patterns. Includes clustering and dimensionality reduction.
            3. Reinforcement Learning: Learns through interaction with an environment
               using rewards and penalties. Used in game playing and robotics.
            """,
            metadata={
                "source": "ml_types.txt",
                "topic": "types",
                "level": "intermediate",
            },
        ),
        Document(
            page_content="""
            Neural networks are computing systems inspired by biological neural
            networks in animal brains. They consist of interconnected nodes (neurons)
            organized in layers. Deep learning uses neural networks with multiple
            hidden layers. Key architectures include:
            - Convolutional Neural Networks (CNNs) for image processing
            - Recurrent Neural Networks (RNNs) for sequential data
            - Transformers for natural language processing
            - Generative Adversarial Networks (GANs) for content generation
            """,
            metadata={
                "source": "neural_networks.txt",
                "topic": "deep_learning",
                "level": "advanced",
            },
        ),
        Document(
            page_content="""
            Common machine learning algorithms include:
            - Linear Regression: Predicts continuous values
            - Logistic Regression: Binary classification
            - Decision Trees: Tree-like model of decisions
            - Random Forests: Ensemble of decision trees
            - Support Vector Machines (SVM): Classification with hyperplanes
            - K-Means Clustering: Unsupervised grouping
            - Principal Component Analysis (PCA): Dimensionality reduction
            Each algorithm has specific use cases and performance characteristics.
            """,
            metadata={
                "source": "ml_algorithms.txt",
                "topic": "algorithms",
                "level": "intermediate",
            },
        ),
        Document(
            page_content="""
            Machine learning applications are transforming industries:
            - Healthcare: Disease diagnosis, drug discovery, personalized treatment
            - Finance: Fraud detection, algorithmic trading, credit scoring
            - Retail: Recommendation systems, demand forecasting, customer segmentation
            - Transportation: Autonomous vehicles, route optimization, traffic prediction
            - Manufacturing: Quality control, predictive maintenance, supply chain optimization
            The impact continues to grow as models become more sophisticated.
            """,
            metadata={
                "source": "ml_applications.txt",
                "topic": "applications",
                "level": "beginner",
            },
        ),
    ]

    # Add documents to the system
    print("\n📚 Loading knowledge base...")
    num_chunks = await rag_system.add_documents(documents)
    print(f"   Added {len(documents)} documents ({num_chunks} chunks)")

    # Test various types of queries
    test_queries = [
        "What is machine learning and how does it work?",
        "Compare supervised and unsupervised learning with examples",
        "Explain neural networks and their applications in image processing",
        "What are the industrial applications of machine learning in healthcare?",
        "How do transformers differ from traditional RNNs?",
        "What algorithms would you recommend for customer segmentation?",
    ]

    print("\n🤖 Testing agentic RAG system:\n")

    for query in test_queries:
        result = await rag_system.process_query(query)

        print(f"\n{'='*60}")
        print(f"Question: {query}")
        print(f"\nAnswer: {result.answer}")
        print(f"\nConfidence: {result.confidence:.1%}")

        if result.sources:
            print(f"\nSources used: {', '.join(result.sources)}")

        if result.key_facts:
            print("\nKey facts:")
            for fact in result.key_facts:
                print(f"  • {fact}")

        if result.needs_clarification:
            print("\n⚠️  This answer may need clarification:")
            for question in result.clarification_questions or []:
                print(f"  - {question}")

        print(f"\n{'='*60}")

        # Small delay between queries
        await asyncio.sleep(1)

    # Demonstrate handling of out-of-scope queries
    print("\n\n🧪 Testing out-of-scope query handling:")
    out_of_scope = "What's the best pizza topping?"
    result = await rag_system.process_query(out_of_scope)

    print(f"\nQuestion: {out_of_scope}")
    print(f"Answer: {result.answer}")
    print(f"Confidence: {result.confidence:.1%}")
    if result.needs_clarification:
        print("Needs clarification: Yes")


if __name__ == "__main__":
    print("Starting Agentic RAG Example...")
    print("This demonstrates advanced RAG with query rewriting and document grading\n")

    asyncio.run(main())

    print("\n✅ Agentic RAG example completed!")
    print("\nKey features demonstrated:")
    print("- Query analysis and rewriting for better retrieval")
    print("- Document relevance grading to filter results")
    print("- Multi-agent coordination for complex reasoning")
    print("- Structured outputs with confidence and sources")
    print("- Handling of out-of-scope queries")
