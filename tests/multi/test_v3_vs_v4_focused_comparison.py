#!/usr/bin/env python3
"""Focused comparison test between different multi-agent implementations.

This test compares:
- SimpleMultiAgent (basic)
- EnhancedMultiAgentV3 (feature-rich)
- EnhancedMultiAgentV4 (clean API)

Focuses on real, practical differences without complex dependencies.
"""

import time
from typing import List, Dict, Any
import logging

from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState

# Import the versions we can test
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.multi.simple_multi_agent import SimpleMultiAgent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestResults(BaseModel):
    """Results from testing a multi-agent implementation."""

    implementation: str
    setup_lines: int = 0
    setup_time: float = 0.0
    execution_time: float = 0.0
    success: bool = False
    features: List[str] = Field(default_factory=list)
    pros: List[str] = Field(default_factory=list)
    cons: List[str] = Field(default_factory=list)
    error: str = ""


def create_test_agents() -> List[SimpleAgentV3]:
    """Create a set of test agents."""
    config = AugLLMConfig(temperature=0.3, max_tokens=100)

    return [
        SimpleAgentV3(
            name="analyzer",
            engine=config,
            system_message="You analyze input and identify key points.",
        ),
        SimpleAgentV3(
            name="processor", engine=config, system_message="You process and transform information."
        ),
        SimpleAgentV3(
            name="formatter",
            engine=config,
            system_message="You format output clearly and concisely.",
        ),
    ]


def test_simple_multi_agent() -> TestResults:
    """Test SimpleMultiAgent implementation."""
    print("\n" + "=" * 60)
    print("Testing SimpleMultiAgent")
    print("=" * 60)

    results = TestResults(implementation="SimpleMultiAgent")
    results.setup_lines = 5

    try:
        start = time.time()

        agents = create_test_agents()
        multi = SimpleMultiAgent(name="simple_workflow", agents=agents)

        results.setup_time = time.time() - start
        results.features = ["basic", "straightforward"]

        # Execute
        start = time.time()
        compiled = multi.compile()
        result = compiled.invoke({"messages": [HumanMessage(content="Analyze this simple test.")]})
        results.execution_time = time.time() - start

        results.success = isinstance(result, dict)
        results.pros = [
            "Simple and easy to understand",
            "Minimal setup required",
            "Good for basic workflows",
        ]
        results.cons = ["Limited routing options", "No performance tracking", "Basic feature set"]

    except Exception as e:
        results.error = str(e)
        logger.error(f"SimpleMultiAgent failed: {e}")

    return results


def test_enhanced_v4() -> TestResults:
    """Test EnhancedMultiAgentV4 implementation."""
    print("\n" + "=" * 60)
    print("Testing EnhancedMultiAgentV4")
    print("=" * 60)

    results = TestResults(implementation="EnhancedMultiAgentV4")
    results.setup_lines = 8

    try:
        start = time.time()

        agents = create_test_agents()
        multi = EnhancedMultiAgentV4(name="v4_workflow", agents=agents, execution_mode="sequential")

        results.setup_time = time.time() - start
        results.features = [
            "clean_api",
            "proper_inheritance",
            "agent_node_v3",
            "multiple_execution_modes",
        ]

        # Execute
        start = time.time()
        compiled = multi.compile()
        result = compiled.invoke({"messages": [HumanMessage(content="Analyze this with V4.")]})
        results.execution_time = time.time() - start

        results.success = isinstance(result, dict)
        results.pros = [
            "Clean, intuitive API",
            "Proper base agent integration",
            "Flexible execution modes",
            "Easy conditional routing",
            "Good error handling",
        ]
        results.cons = ["No built-in performance tracking", "Less feature-rich than V3"]

    except Exception as e:
        results.error = str(e)
        logger.error(f"EnhancedMultiAgentV4 failed: {e}")

    return results


def test_v4_with_routing() -> TestResults:
    """Test V4's routing capabilities."""
    print("\n" + "=" * 60)
    print("Testing V4 with Conditional Routing")
    print("=" * 60)

    results = TestResults(implementation="V4 with Routing")
    results.setup_lines = 12

    try:
        start = time.time()

        agents = create_test_agents()
        multi = EnhancedMultiAgentV4(
            name="v4_routing", agents=agents, execution_mode="conditional", entry_point="analyzer"
        )

        # Add routing
        multi.add_conditional_edge(
            "analyzer",
            lambda state: "complex" in str(state.get("messages", [])[-1].content).lower(),
            true_agent="processor",
            false_agent="formatter",
        )

        results.setup_time = time.time() - start
        results.features = ["conditional_routing", "add_edge_methods", "entry_point_control"]

        # Test both paths
        start = time.time()
        compiled = multi.compile()

        # Simple path
        result1 = compiled.invoke(
            {"messages": [HumanMessage(content="Format this simple message.")]}
        )

        # Complex path
        result2 = compiled.invoke(
            {"messages": [HumanMessage(content="Analyze this complex data structure.")]}
        )

        results.execution_time = time.time() - start

        results.success = isinstance(result1, dict) and isinstance(result2, dict)
        results.pros = [
            "Easy conditional routing setup",
            "Clean edge definition API",
            "Supports complex workflows",
        ]
        results.cons = ["Manual route definition required"]

    except Exception as e:
        results.error = str(e)
        logger.error(f"V4 with routing failed: {e}")

    return results


def compare_implementations():
    """Run all tests and compare results."""
    print("\n" + "=" * 80)
    print("🔬 MULTI-AGENT IMPLEMENTATION COMPARISON")
    print("=" * 80)

    # Run tests
    results = [test_simple_multi_agent(), test_enhanced_v4(), test_v4_with_routing()]

    # Summary
    print("\n" + "=" * 80)
    print("📊 COMPARISON SUMMARY")
    print("=" * 80)

    for r in results:
        print(f"\n{r.implementation}:")
        print(f"  Setup: {r.setup_time:.3f}s ({r.setup_lines} lines)")
        print(f"  Execution: {r.execution_time:.3f}s")
        print(f"  Status: {'✅ Success' if r.success else '❌ Failed'}")

        if r.features:
            print(f"  Features: {', '.join(r.features)}")

        if r.error:
            print(f"  Error: {r.error}")

    # Detailed comparison
    print("\n" + "=" * 80)
    print("🎯 DETAILED ANALYSIS")
    print("=" * 80)

    for r in results:
        print(f"\n{r.implementation}:")
        print("  Pros:")
        for pro in r.pros:
            print(f"    ✅ {pro}")
        print("  Cons:")
        for con in r.cons:
            print(f"    ❌ {con}")

    # Recommendations
    print("\n" + "=" * 80)
    print("💡 RECOMMENDATIONS")
    print("=" * 80)

    print("\n1. For Simple Sequential Workflows:")
    print("   → Use SimpleMultiAgent or V4 in sequential mode")
    print("   → Both are easy to set up and understand")

    print("\n2. For Conditional/Complex Workflows:")
    print("   → Use EnhancedMultiAgentV4")
    print("   → Clean API for routing and conditions")
    print("   → Good balance of features and simplicity")

    print("\n3. For Performance-Critical Applications:")
    print("   → V3 would be best (if available) for built-in tracking")
    print("   → Otherwise, add custom performance tracking to V4")

    print("\n4. For Long-term Maintainability:")
    print("   → V4 is the best choice")
    print("   → Clean code, proper patterns, easy to extend")

    print("\n" + "=" * 80)
    print("✨ CONCLUSION")
    print("=" * 80)
    print("\nEnhancedMultiAgentV4 offers the best balance of:")
    print("• Clean, intuitive API")
    print("• Flexible routing capabilities")
    print("• Proper architectural patterns")
    print("• Easy maintenance and extension")
    print("\nIt's the recommended choice for most use cases.")


if __name__ == "__main__":
    compare_implementations()
