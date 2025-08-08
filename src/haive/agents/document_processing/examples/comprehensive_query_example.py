"""Comprehensive example of using DocumentProcessingAgent with QueryState.

This example demonstrates the full capabilities of the document processing system
including query state management, advanced retrieval strategies, and multi-query
workflows.

Examples:
    Basic usage::

        python comprehensive_query_example.py

    With specific strategies::

        python comprehensive_query_example.py --strategy adaptive --query-type research

Author: Claude (Haive AI Agent Framework)
Version: 1.0.0
"""

import asyncio
import traceback
from datetime import datetime, timedelta

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.query_state import (
    QueryComplexity,
    QueryIntent,
    QueryProcessingConfig,
    QueryState,
    QueryType,
    RetrievalStrategy,
)

from haive.agents.document_processing import (
    DocumentProcessingAgent,
    DocumentProcessingConfig,
)


async def basic_query_example():
    """Basic example using DocumentProcessingAgent with QueryState."""
    # Create basic configuration
    doc_config = DocumentProcessingConfig(
        search_enabled=True,
        annotation_enabled=True,
        bulk_processing=True,
        rag_strategy="basic",
    )

    # Create LLM configuration
    llm_config = AugLLMConfig(temperature=0.1, max_tokens=1000)

    # Create agent
    agent = DocumentProcessingAgent(
        config=doc_config, engine=llm_config, name="basic_query_agent"
    )

    # Create query state
    query_state = QueryState(
        original_query="What is artificial intelligence?",
        query_type=QueryType.SIMPLE,
        retrieval_strategy=RetrievalStrategy.BASIC,
        query_complexity=QueryComplexity.LOW,
        query_intent=QueryIntent.INFORMATION_SEEKING,
    )

    # Process query
    result = await agent.process_query(query_state.original_query)

    # Display results

    return result


async def advanced_query_example():
    """Advanced example with query refinement and multiple strategies."""
    # Create advanced configuration
    doc_config = DocumentProcessingConfig(
        search_enabled=True,
        annotation_enabled=True,
        summarization_enabled=True,
        bulk_processing=True,
        rag_strategy="adaptive",
        query_refinement=True,
        multi_query_enabled=True,
    )

    # Create LLM configuration
    llm_config = AugLLMConfig(temperature=0.2, max_tokens=2000)

    # Create agent
    agent = DocumentProcessingAgent(
        config=doc_config, engine=llm_config, name="advanced_query_agent"
    )

    # Create advanced query state
    query_state = QueryState(
        original_query="Analyze the impact of machine learning on healthcare",
        query_type=QueryType.RESEARCH,
        retrieval_strategy=RetrievalStrategy.ADAPTIVE,
        query_complexity=QueryComplexity.HIGH,
        query_intent=QueryIntent.ANALYTICAL,
        # Enable advanced features
        query_expansion_enabled=True,
        query_refinement_enabled=True,
        multi_query_enabled=True,
        # Add refined queries
        refined_queries=[
            "Machine learning applications in medical diagnosis",
            "AI-driven drug discovery and development",
            "Healthcare automation and ML implementation",
            "Clinical decision support systems using ML",
        ],
        # Add filters
        source_filters=["medical_journals", "research_papers", "clinical_studies"],
        metadata_filters={"domain": "healthcare", "topic": "machine_learning"},
        time_range_filter={
            "start": datetime.now() - timedelta(days=365 * 2),  # Last 2 years
            "end": datetime.now(),
        },
        # Configure processing
        processing_config=QueryProcessingConfig(
            max_query_variations=5,
            enable_query_expansion=True,
            enable_query_refinement=True,
            enable_context_compression=True,
            enable_citation_tracking=True,
            enable_confidence_scoring=True,
            max_context_documents=15,
            similarity_threshold=0.75,
        ),
    )

    # Process with multiple queries
    main_result = await agent.process_query(query_state.original_query)

    # Process refined queries
    refined_results = []
    for refined_query in query_state.refined_queries:
        result = await agent.process_query(refined_query)
        refined_results.append(result)

    # Display results

    for _i, result in enumerate(refined_results):
        pass

    return main_result, refined_results


async def multi_source_example():
    """Example with specific document sources."""
    # Create configuration for document processing
    doc_config = DocumentProcessingConfig(
        search_enabled=False,  # Disable search, use provided sources
        annotation_enabled=True,
        bulk_processing=True,
        rag_strategy="adaptive",
        structured_output=True,
    )

    # Create LLM configuration
    llm_config = AugLLMConfig(temperature=0.1, max_tokens=1500)

    # Create agent
    agent = DocumentProcessingAgent(
        config=doc_config, engine=llm_config, name="multi_source_agent"
    )

    # Create query state
    query_state = QueryState(
        original_query="Compare different approaches to sustainable energy",
        query_type=QueryType.COMPARISON,
        retrieval_strategy=RetrievalStrategy.ENSEMBLE,
        query_complexity=QueryComplexity.MEDIUM,
        query_intent=QueryIntent.DECISION_MAKING,
        # Add specific queries for comparison
        refined_queries=[
            "Solar energy advantages and limitations",
            "Wind power efficiency and scalability",
            "Nuclear energy safety and sustainability",
            "Hydroelectric power environmental impact",
        ],
        # Configuration for comparison
        processing_config=QueryProcessingConfig(
            enable_query_expansion=True,
            enable_result_reranking=True,
            max_context_documents=20,
            similarity_threshold=0.8,
        ),
    )

    # Sample document sources
    document_sources = [
        "Solar energy harnesses photovoltaic technology to convert sunlight into electricity. It's renewable, environmentally friendly, but requires significant initial investment and is weather-dependent.",
        "Wind power uses turbines to generate electricity from wind kinetic energy. It's cost-effective and scalable, but faces challenges with intermittency and visual impact.",
        "Nuclear energy provides consistent, high-output power with minimal carbon emissions. However, it raises concerns about safety, waste disposal, and high construction costs.",
        "Hydroelectric power generates electricity through flowing water. It's reliable and long-lasting, but can significantly impact local ecosystems and requires suitable geography.",
        "Geothermal energy taps into Earth's internal heat for power generation. It's stable and sustainable, but geographically limited and requires high upfront costs.",
        "Biomass energy converts organic materials into fuel. It's renewable and carbon-neutral, but competes with food production and may cause deforestation.",
    ]

    # Process with document sources
    result = await agent.process_sources(document_sources, query_state.original_query)

    # Display results

    return result


async def structured_query_example():
    """Example with structured query processing."""
    # Create configuration for structured processing
    doc_config = DocumentProcessingConfig(
        search_enabled=True,
        annotation_enabled=True,
        bulk_processing=True,
        rag_strategy="adaptive",
        structured_output=True,
        query_refinement=True,
    )

    # Create LLM configuration
    llm_config = AugLLMConfig(
        temperature=0.0, max_tokens=2000
    )  # Very low temperature for structured output

    # Create agent
    agent = DocumentProcessingAgent(
        config=doc_config, engine=llm_config, name="structured_query_agent"
    )

    # Create structured query state
    query_state = QueryState(
        original_query="Extract key financial metrics from quarterly reports",
        query_type=QueryType.EXTRACTION,
        retrieval_strategy=RetrievalStrategy.SELF_QUERY,
        query_complexity=QueryComplexity.MEDIUM,
        query_intent=QueryIntent.PROBLEM_SOLVING,
        # Enable structured processing
        structured_query_enabled=True,
        # Add specific extraction queries
        refined_queries=[
            "Revenue growth percentage year-over-year",
            "Operating margin and profit margins",
            "EBITDA and net income figures",
            "Cash flow from operations",
            "Debt-to-equity ratio and financial health indicators",
        ],
        # Metadata filters for financial data
        metadata_filters={
            "document_type": "financial_report",
            "report_type": "quarterly",
            "data_type": "numerical",
        },
        # Configuration for extraction
        processing_config=QueryProcessingConfig(
            enable_query_expansion=False,  # Disable expansion for structured extraction
            enable_context_compression=True,
            enable_citation_tracking=True,
            max_context_documents=10,
            similarity_threshold=0.85,
        ),
    )

    # Sample financial document sources
    financial_sources = [
        "Q3 2024 Financial Report: Revenue increased 15% YoY to $2.5M. Operating margin improved to 18.5%. Net income was $425K, up from $350K in Q3 2023.",
        "Q4 2024 Earnings: Total revenue $2.8M (+12% QoQ). EBITDA margin 22.3%. Free cash flow $380K. Debt-to-equity ratio maintained at 0.45.",
        "Annual Report 2024: Full-year revenue $9.8M (+18% YoY). Operating expenses controlled at 68% of revenue. ROE improved to 15.2%.",
        "Q1 2024 Results: Revenue $2.1M. Gross margin 45.2%. Operating cash flow $290K. Working capital efficiency gained 8% improvement.",
        "Q2 2024 Performance: Revenue growth 14% YoY to $2.3M. Operating margin 17.8%. Net profit margin 8.5%. Cash position $1.2M.",
    ]

    # Process with structured extraction
    result = await agent.process_sources(financial_sources, query_state.original_query)

    # Display results

    return result


async def comprehensive_workflow_example():
    """Comprehensive workflow combining all features."""
    # Create comprehensive configuration
    doc_config = DocumentProcessingConfig(
        search_enabled=True,
        annotation_enabled=True,
        summarization_enabled=True,
        kg_extraction_enabled=True,
        bulk_processing=True,
        rag_strategy="adaptive",
        query_refinement=True,
        multi_query_enabled=True,
        structured_output=True,
        max_concurrent_loads=5,
    )

    # Create LLM configuration
    llm_config = AugLLMConfig(temperature=0.3, max_tokens=3000)

    # Create agent
    agent = DocumentProcessingAgent(
        config=doc_config, engine=llm_config, name="comprehensive_agent"
    )

    # Create comprehensive query state
    query_state = QueryState(
        original_query="Analyze the evolution of artificial intelligence from 2020 to 2024",
        query_type=QueryType.ANALYTICAL,
        retrieval_strategy=RetrievalStrategy.HYBRID,
        query_complexity=QueryComplexity.EXPERT,
        query_intent=QueryIntent.LEARNING,
        # Enable all features
        query_expansion_enabled=True,
        query_refinement_enabled=True,
        multi_query_enabled=True,
        structured_query_enabled=True,
        time_weighted_retrieval=True,
        # Add comprehensive queries
        refined_queries=[
            "AI breakthroughs and milestones 2020-2024",
            "Machine learning model improvements over time",
            "Natural language processing advances",
            "Computer vision developments and applications",
            "AI ethics and governance evolution",
            "Industry adoption patterns and trends",
        ],
        # Expanded queries for broader coverage
        expanded_queries=[
            "Deep learning transformer architectures",
            "Large language model scaling",
            "AI safety and alignment research",
            "Multimodal AI systems development",
            "AI hardware and infrastructure evolution",
        ],
        # Time-based filtering
        time_range_filter={
            "start": datetime(2020, 1, 1),
            "end": datetime(2024, 12, 31),
        },
        # Source and metadata filters
        source_filters=["research_papers", "tech_reports", "industry_analyses"],
        metadata_filters={
            "domain": "artificial_intelligence",
            "timeframe": "2020-2024",
            "type": "evolution_analysis",
        },
        # Advanced processing configuration
        processing_config=QueryProcessingConfig(
            max_query_variations=10,
            enable_query_expansion=True,
            enable_query_refinement=True,
            enable_context_compression=True,
            enable_result_reranking=True,
            enable_citation_tracking=True,
            enable_confidence_scoring=True,
            max_context_documents=25,
            similarity_threshold=0.7,
            time_weight_decay=0.1,
            enable_caching=True,
        ),
    )

    # Process main query
    datetime.now()
    result = await agent.process_query(query_state.original_query)
    datetime.now()

    # Display comprehensive results

    # Create summary
    query_state.get_processing_summary()

    return result, query_state


async def main():
    """Run all examples."""
    try:
        # Run examples
        await basic_query_example()
        await advanced_query_example()
        await multi_source_example()
        await structured_query_example()
        await comprehensive_workflow_example()

    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
