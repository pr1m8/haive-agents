"""Test MultiMemoryAgent coordination and routing functionality."""

import asyncio
import contextlib

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.memory_v2.multi_memory_agent import (
    MemoryStrategy,
    MultiMemoryAgent,
    MultiMemoryConfig,
    QueryType)


def test_multi_memory_config():
    """Test MultiMemoryAgent configuration creation."""
    # Test default config
    MultiMemoryConfig()

    # Test custom config
    MultiMemoryConfig(
        name="custom_coordinator",
        default_strategy=MemoryStrategy.HYBRID,
        enable_graph_memory=False,
        enable_rag_memory=False)


def test_memory_strategies():
    """Test memory strategy enums."""
    strategies = list(MemoryStrategy)
    for _strategy in strategies:
        pass

    query_types = list(QueryType)
    for _query_type in query_types:
        pass


def test_multi_memory_agent_creation():
    """Test MultiMemoryAgent creation and initialization."""
    # Create config with only SimpleMemoryAgent enabled (to avoid dependencies)
    config = MultiMemoryConfig(
        name="test_coordinator",
        enable_simple_memory=True,
        enable_graph_memory=False,  # Disable to avoid Neo4j dependency
        enable_rag_memory=False,  # Disable to avoid complex dependencies
        llm_config=AugLLMConfig(
            llm_config=DeepSeekLLMConfig(model="deepseek-chat", temperature=0.1)
        ))

    try:
        agent = MultiMemoryAgent(config)

        # Test coordination stats
        agent.get_coordination_stats()

        return agent

    except Exception:
        return None


async def test_query_classification():
    """Test query classification functionality."""
    # Try to create minimal agent
    config = MultiMemoryConfig(
        enable_simple_memory=False,  # Disable all memory agents for minimal test
        enable_graph_memory=False,
        enable_rag_memory=False)

    try:
        agent = MultiMemoryAgent(config)

        # Test query classification
        test_queries = [
            "Hello, how are you today?",
            "What did we discuss last week?",
            "Who works at Google in my network?",
            "I prefer dark mode in applications",
            "What's the capital of France?",
        ]

        for query in test_queries:
            try:
                classification = await agent.classify_query(query)

                # Test routing
                agent.route_query(
                    classification.get("query_type", QueryType.CONVERSATIONAL),
                    classification.get("confidence", 0.5))

            except Exception:
                pass

    except Exception:
        pass


def test_routing_rules():
    """Test routing rules configuration."""
    config = MultiMemoryConfig()
    agent = MultiMemoryAgent(config)

    # Test different query types and routing
    test_cases = [
        (QueryType.CONVERSATIONAL, MemoryStrategy.SIMPLE),
        (QueryType.FACTUAL, MemoryStrategy.RAG),
        (QueryType.RELATIONSHIP, MemoryStrategy.GRAPH),
        (QueryType.PREFERENCE, MemoryStrategy.SIMPLE),
        (QueryType.MIXED, MemoryStrategy.ADAPTIVE),
    ]

    for query_type, _expected_strategy in test_cases:
        routing = agent.route_query(query_type, 0.8)  # High confidence
        if routing["fallback_used"]:
            pass


def comprehensive_test():
    """Run all tests in sequence."""
    # Test configuration
    test_multi_memory_config()

    # Test enums
    test_memory_strategies()

    # Test agent creation
    agent = test_multi_memory_agent_creation()

    # Test routing rules
    test_routing_rules()

    # Test query classification (async)
    with contextlib.suppress(Exception):
        asyncio.run(test_query_classification())

    if agent:
        pass
    else:
        pass


if __name__ == "__main__":
    comprehensive_test()
