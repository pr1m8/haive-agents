"""Comprehensive BaseRAG to SimpleAgent flow with detailed prompt template."""

import asyncio
from datetime import datetime
from typing import List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.embedding.providers.HuggingFaceEmbeddingConfig import (
    HuggingFaceEmbeddingConfig,
)
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.simple.agent import SimpleAgent

# Comprehensive RAG Answer Generation Prompt
RAG_ANSWER_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an advanced AI assistant specializing in retrieval-augmented generation (RAG). 
Your role is to provide accurate, comprehensive, and well-reasoned answers based solely on the retrieved documents provided to you.

**Core Principles:**
1. **Accuracy First**: Base all answers strictly on the retrieved documents
2. **Source Attribution**: Always cite which document(s) support each claim
3. **Transparency**: Clearly indicate when information is insufficient or unavailable
4. **Synthesis**: Intelligently combine information from multiple documents when relevant
5. **Context Awareness**: Consider the relationships between different pieces of information

**Response Guidelines:**
- Start with a direct answer to the question
- Provide detailed explanations with supporting evidence
- Use quotes when citing specific passages
- Acknowledge any limitations or gaps in the available information
- Suggest related topics or follow-up questions when appropriate

**Quality Standards:**
- Ensure factual accuracy by cross-referencing multiple sources when available
- Maintain objectivity and avoid speculation beyond the documents
- Present information in a clear, logical structure
- Use appropriate technical language while remaining accessible

**Special Instructions:**
- For technical topics: Include definitions and explanations of key terms
- For procedural questions: Provide step-by-step guidance if available
- For comparative questions: Highlight similarities and differences
- For analytical questions: Break down complex concepts systematically""",
        ),
        (
            "human",
            """Please answer the following question based on the retrieved documents provided below.

**Retrieved Documents:**
{retrieved_documents}

**Question:** {query}

**Additional Context (if any):** {context}

**Answer Requirements:**
1. Provide a comprehensive answer using only information from the retrieved documents
2. Include specific citations for each major claim (e.g., [Source: Document Name])
3. If the documents don't fully answer the question, explicitly state what information is missing
4. Organize your response with clear structure (introduction, main points, conclusion if appropriate)
5. Highlight any particularly important or relevant findings
6. If multiple documents provide different perspectives, present all viewpoints fairly

**Response Format:**
- Start with a brief direct answer (1-2 sentences)
- Provide detailed explanation with evidence
- Include a summary of key points at the end
- Note any limitations or areas where more information would be helpful

Please provide your answer now:""",
        ),
    ]
).partial(context="No additional context provided")


# Comprehensive Structured Output Model
class DocumentReference(BaseModel):
    """Reference to a specific document used in the answer."""

    source_name: str = Field(description="Name or identifier of the source document")
    relevance_score: float = Field(description="How relevant this document was to the answer (0-1)")
    key_points: List[str] = Field(description="Key points extracted from this document")


class AnswerSection(BaseModel):
    """A section of the structured answer."""

    heading: str = Field(description="Section heading")
    content: str = Field(description="Section content")
    supporting_sources: List[str] = Field(description="Sources that support this section")


class ComprehensiveRAGAnswer(BaseModel):
    """Comprehensive structured answer from RAG system."""

    # Core answer components
    direct_answer: str = Field(description="Brief, direct answer to the question (1-2 sentences)")

    detailed_explanation: str = Field(
        description="Comprehensive explanation with evidence from documents"
    )

    # Structured sections for complex answers
    answer_sections: Optional[List[AnswerSection]] = Field(
        default=None, description="Structured sections for organizing complex answers"
    )

    # Source tracking
    primary_sources: List[DocumentReference] = Field(
        description="Primary documents used for the answer"
    )

    all_sources_used: List[str] = Field(description="List of all source documents referenced")

    # Quality indicators
    confidence_score: float = Field(
        description="Overall confidence in the answer (0-1)", ge=0.0, le=1.0
    )

    answer_completeness: str = Field(
        description="Assessment of how completely the question was answered",
        pattern="^(complete|partial|insufficient)$",
    )

    # Additional insights
    key_findings: List[str] = Field(description="Key findings or insights from the analysis")

    information_gaps: Optional[List[str]] = Field(
        default=None,
        description="Important information that was missing from the documents",
    )

    follow_up_questions: Optional[List[str]] = Field(
        default=None,
        description="Suggested follow-up questions for deeper understanding",
    )

    # Metadata
    answer_type: str = Field(
        description="Type of answer provided",
        pattern="^(factual|analytical|procedural|conceptual|comparative)$",
    )

    synthesis_level: str = Field(
        description="Level of synthesis required",
        pattern="^(single_source|multi_source|complex_synthesis)$",
    )

    timestamp: datetime = Field(
        default_factory=datetime.now, description="When the answer was generated"
    )


async def test_comprehensive_rag_flow():
    """Test BaseRAG → SimpleAgent flow with comprehensive prompt."""
    print("\n=== Comprehensive BaseRAG to SimpleAgent Flow ===\n")

    # 1. Create sample documents with rich content
    documents = [
        Document(
            page_content="""Machine learning is a subset of artificial intelligence that focuses on the development of algorithms and statistical models that enable computer systems to improve their performance on a specific task through experience. Unlike traditional programming where explicit instructions are provided, machine learning systems learn patterns from data and make decisions based on these learned patterns. The field emerged from pattern recognition and computational learning theory in AI.""",
            metadata={
                "source": "ML Fundamentals Guide",
                "chapter": "Introduction",
                "year": 2024,
            },
        ),
        Document(
            page_content="""There are three main types of machine learning: supervised learning, unsupervised learning, and reinforcement learning. Supervised learning uses labeled data to train models for classification or regression tasks. Unsupervised learning discovers hidden patterns in unlabeled data through clustering or dimensionality reduction. Reinforcement learning trains agents to make sequences of decisions by rewarding desired behaviors.""",
            metadata={
                "source": "ML Categories Handbook",
                "chapter": "Learning Paradigms",
                "year": 2024,
            },
        ),
        Document(
            page_content="""Deep learning, a subset of machine learning, uses artificial neural networks with multiple layers (deep architectures) to progressively extract higher-level features from raw input. Inspired by the biological neural networks in human brains, deep learning has revolutionized fields such as computer vision, natural language processing, and speech recognition. Key architectures include Convolutional Neural Networks (CNNs) for image processing and Transformer models for language tasks.""",
            metadata={
                "source": "Deep Learning Comprehensive Guide",
                "chapter": "Neural Architectures",
                "year": 2023,
            },
        ),
        Document(
            page_content="""Applications of machine learning span numerous domains: healthcare (disease diagnosis, drug discovery), finance (fraud detection, algorithmic trading), transportation (autonomous vehicles, route optimization), retail (recommendation systems, demand forecasting), and manufacturing (quality control, predictive maintenance). The impact of ML continues to grow as computational power increases and more data becomes available.""",
            metadata={
                "source": "ML Applications Review",
                "chapter": "Industry Applications",
                "year": 2024,
            },
        ),
        Document(
            page_content="""Key challenges in machine learning include data quality and quantity, model interpretability, computational requirements, and ethical considerations. Bias in training data can lead to discriminatory outcomes. The 'black box' nature of complex models makes it difficult to understand their decision-making process. Additionally, privacy concerns arise when training on sensitive data, necessitating techniques like federated learning and differential privacy.""",
            metadata={
                "source": "ML Challenges and Ethics",
                "chapter": "Current Challenges",
                "year": 2024,
            },
        ),
    ]

    # 2. Create BaseRAGAgent
    print("1. Creating BaseRAGAgent...")
    embedding_config = HuggingFaceEmbeddingConfig(model="sentence-transformers/all-MiniLM-L6-v2")

    base_rag = BaseRAGAgent.from_documents(
        documents=documents,
        embedding_config=embedding_config,
        name="comprehensive_retriever",
        k=4,  # Get top 4 documents for comprehensive answers
    )

    # 3. Create SimpleAgent with comprehensive prompt
    print("\n2. Creating SimpleAgent with comprehensive prompt template...")
    simple_agent = SimpleAgent(
        name="comprehensive_answer_generator",
        engine=AugLLMConfig(
            prompt_template=RAG_ANSWER_PROMPT,
            structured_output_model=ComprehensiveRAGAnswer,
            structured_output_version="v2",  # Using v2 as requested
            temperature=0.7,
            max_tokens=2000,  # Allow for detailed answers
        ),
    )

    # 4. Test with various types of questions
    test_questions = [
        {
            "query": "What is machine learning and how does it differ from traditional programming?",
            "context": "I'm a software developer trying to understand ML basics",
        },
        {
            "query": "What are the main types of machine learning and their applications?",
            "context": "Looking for a comprehensive overview for a presentation",
        },
        {
            "query": "What are the current challenges and ethical considerations in machine learning?",
            "context": "Researching for a paper on AI ethics",
        },
    ]

    for i, question_data in enumerate(test_questions, 1):
        print(f"\n{'=' * 80}")
        print(f"Question {i}: {question_data['query']}")
        print(f"Context: {question_data['context']}")
        print(f"{'=' * 80}\n")

        # Step 1: Retrieve documents
        print("Retrieving relevant documents...")
        retrieval_result = await base_rag.arun(question_data["query"])

        print(f"Retrieved {len(retrieval_result.retrieved_documents)} documents:")
        for doc in retrieval_result.retrieved_documents:
            print(f"  - {doc.metadata.get('source', 'Unknown')}: {doc.page_content[:100]}...")

        # Format retrieved documents
        retrieved_docs_text = "\n\n".join(
            [
                f"[Document {j}: {doc.metadata.get('source', 'Unknown')} - {doc.metadata.get('chapter', 'N/A')}]\n{doc.page_content}"
                for j, doc in enumerate(retrieval_result.retrieved_documents, 1)
            ]
        )

        # Step 2: Generate comprehensive answer
        print("\nGenerating comprehensive answer...")
        answer_input = {
            "retrieved_documents": retrieved_docs_text,
            "query": question_data["query"],
            "context": question_data["context"],
        }

        try:
            answer = await simple_agent.arun(answer_input)

            print("\n📊 Structured Answer:")
            if isinstance(answer, ComprehensiveRAGAnswer):
                print("\n🎯 Direct Answer:")
                print(f"   {answer.direct_answer}")

                print("\n📝 Detailed Explanation:")
                print(
                    f"   {answer.detailed_explanation[:500]}..."
                    if len(answer.detailed_explanation) > 500
                    else f"   {answer.detailed_explanation}"
                )

                print(f"\n📚 Sources Used: {len(answer.all_sources_used)}")
                for source in answer.all_sources_used:
                    print(f"   - {source}")

                print("\n🔍 Key Findings:")
                for finding in answer.key_findings[:3]:  # Show first 3
                    print(f"   • {finding}")

                print("\n📊 Quality Metrics:")
                print(f"   - Confidence: {answer.confidence_score:.2f}")
                print(f"   - Completeness: {answer.answer_completeness}")
                print(f"   - Answer Type: {answer.answer_type}")
                print(f"   - Synthesis Level: {answer.synthesis_level}")

                if answer.information_gaps:
                    print("\n⚠️ Information Gaps:")
                    for gap in answer.information_gaps:
                        print(f"   - {gap}")

                if answer.follow_up_questions:
                    print("\n💡 Suggested Follow-up Questions:")
                    for question in answer.follow_up_questions[:2]:  # Show first 2
                        print(f"   - {question}")
            else:
                print(answer)

        except Exception as e:
            print(f"Error generating answer: {e}")
            import traceback

            traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_comprehensive_rag_flow())
