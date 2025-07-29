#!/usr/bin/env python3
"""Isolated testing of AgentNodeV3 behavior with different agent types.

This test isolates AgentNodeV3 to understand exactly what's happening with:
- SimpleAgentV3 with structured output
- SimpleAgentV3 without structured output
- ReactAgentV3 with structured output
- ReactAgentV3 without structured output

We need to understand why AgentNodeV3 is doing complex output processing
when agents should just return their output_schema directly.
"""

import logging
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.models.llm.base import AzureLLMConfig
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from pydantic import BaseModel, Field

from haive.agents.react.agent_v3 import ReactAgentV3
from haive.agents.simple.agent_v3 import SimpleAgentV3

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Test models
class TestStructuredOutput(BaseModel):
    """Test structured output model."""

    analysis: str = Field(description="Analysis result")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")
    recommendations: List[str] = Field(description="List of recommendations")


class TestAgentNodeV3Isolation:
    """Isolated tests for AgentNodeV3 behavior."""

    def test_simple_agent_v3_with_structured_output(self):
        """Test SimpleAgentV3 with structured output through AgentNodeV3."""
        print("\n" + "=" * 80)
        print("🧪 TEST: SimpleAgentV3 WITH Structured Output")
        print("=" * 80)

        # Create agent with structured output
        agent = SimpleAgentV3(
            name="structured_simple",
            engine=AugLLMConfig(
                structured_output_model=TestStructuredOutput,
                structured_output_version="v2",
                temperature=0.1,
                max_tokens=300,
                llm_config=AzureLLMConfig(),
            ),
            debug=True,
        )

        print(f"✅ Created SimpleAgentV3: {agent.name}")
        print(f"   Has output_schema: {hasattr(agent, 'output_schema')}")
        print(f"   output_schema: {getattr(agent, 'output_schema', None)}")
        print(
            f"   engine.structured_output_model: {
    getattr(
        agent.engine,
        'structured_output_model',
         None)}"
        )

        # Create AgentNodeV3
        node = create_agent_node_v3(
    agent_name="structured_simple", agent=agent)
        print(f"✅ Created AgentNodeV3: {type(node)}")

        # Create test state
        state = MultiAgentState(
            agents={"structured_simple": agent},
            messages=[
                {"role": "user", "content": "Analyze the benefits of renewable energy"}
            ],
        )

        print("\n🚀 Executing through AgentNodeV3...")
        print(f"   State type: {type(state)}")
        print(f"   State has agents: {'agents' in state.__dict__}")

        try:
            # Execute through AgentNodeV3
            result = node(state)

            print("\n📊 AgentNodeV3 Result:")
            print(f"   Type: {type(result)}")
            print(f"   Result: {result}")

            # Analyze what happened
            if hasattr(result, "__dict__"):
                print(f"   Result attributes: {list(result.__dict__.keys())}")

            # Check if structured output was extracted properly
            if isinstance(result, dict):
                print(f"   Dict keys: {list(result.keys())}")
                for key, value in result.items():
                    print(f"     {key}: {type(value)} = {value}")

        except Exception as e:
            print(f"❌ AgentNodeV3 execution failed: {e}")
            logger.exception("AgentNodeV3 execution error")

    def test_simple_agent_v3_without_structured_output(self):
        """Test SimpleAgentV3 without structured output through AgentNodeV3."""
        print("\n" + "=" * 80)
        print("🧪 TEST: SimpleAgentV3 WITHOUT Structured Output")
        print("=" * 80)

        # Create agent without structured output
        agent = SimpleAgentV3(
            name="unstructured_simple",
            engine=AugLLMConfig(
                temperature=0.7, max_tokens=300, llm_config=AzureLLMConfig()
            ),
            debug=True,
        )

        print(f"✅ Created SimpleAgentV3: {agent.name}")
        print(f"   Has output_schema: {hasattr(agent, 'output_schema')}")
        print(f"   output_schema: {getattr(agent, 'output_schema', None)}")
        print(
            f"   engine.structured_output_model: {
    getattr(
        agent.engine,
        'structured_output_model',
         None)}"
        )

        # Create AgentNodeV3
        node = create_agent_node_v3(
    agent_name="unstructured_simple", agent=agent)
        print(f"✅ Created AgentNodeV3: {type(node)}")

        # Create test state
        state = MultiAgentState(
            agents={"unstructured_simple": agent},
            messages=[
                {"role": "user", "content": "Tell me about artificial intelligence"}
            ],
        )

        print("\n🚀 Executing through AgentNodeV3...")

        try:
            # Execute through AgentNodeV3
            result = node(state)

            print("\n📊 AgentNodeV3 Result:")
            print(f"   Type: {type(result)}")
            print(f"   Result: {result}")

            # Analyze what happened
            if hasattr(result, "__dict__"):
                print(f"   Result attributes: {list(result.__dict__.keys())}")

            if isinstance(result, dict):
                print(f"   Dict keys: {list(result.keys())}")
                for key, value in result.items():
                    print(f"     {key}: {type(value)} = {value}")

        except Exception as e:
            print(f"❌ AgentNodeV3 execution failed: {e}")
            logger.exception("AgentNodeV3 execution error")

    def test_react_agent_v3_with_structured_output(self):
        """Test ReactAgentV3 with structured output through AgentNodeV3."""
        print("\n" + "=" * 80)
        print("🧪 TEST: ReactAgentV3 WITH Structured Output")
        print("=" * 80)

        # Create tools for ReactAgent
        from langchain_core.tools import tool

        @tool
        def calculator(expression: str) -> str:
            """Calculate mathematical expressions."""
            try:
                result = eval(expression, {"__builtins__": {}}, {})
                return f"Result: {result}"
            except Exception as e:
                return f"Error: {str(e)}"

        # Create ReactAgent with structured output
        agent = ReactAgentV3(
            name="structured_react",
            engine=AugLLMConfig(
                structured_output_model=TestStructuredOutput,
                structured_output_version="v2",
                temperature=0.1,
                max_tokens=500,
                llm_config=AzureLLMConfig(),
            ),
            tools=[calculator],
            max_iterations=2,
            debug=True,
        )

        print(f"✅ Created ReactAgentV3: {agent.name}")
        print(f"   Has output_schema: {hasattr(agent, 'output_schema')}")
        print(f"   output_schema: {getattr(agent, 'output_schema', None)}")
        print(
            f"   engine.structured_output_model: {
    getattr(
        agent.engine,
        'structured_output_model',
         None)}"
        )
        print(f"   Tools: {[tool.name for tool in agent.tools]}")

        # Create AgentNodeV3
        node = create_agent_node_v3(agent_name="structured_react", agent=agent)
        print(f"✅ Created AgentNodeV3: {type(node)}")

        # Create test state
        state = MultiAgentState(
            agents={"structured_react": agent},
            messages=[
                {"role": "user", "content": "Calculate 15 * 23 and analyze the result"}
            ],
        )

        print("\n🚀 Executing through AgentNodeV3...")

        try:
            # Execute through AgentNodeV3
            result = node(state)

            print("\n📊 AgentNodeV3 Result:")
            print(f"   Type: {type(result)}")
            print(f"   Result: {result}")

            # Analyze what happened
            if hasattr(result, "__dict__"):
                print(f"   Result attributes: {list(result.__dict__.keys())}")

            if isinstance(result, dict):
                print(f"   Dict keys: {list(result.keys())}")
                for key, value in result.items():
                    print(f"     {key}: {type(value)} = {value}")

        except Exception as e:
            print(f"❌ AgentNodeV3 execution failed: {e}")
            logger.exception("AgentNodeV3 execution error")

    def test_direct_agent_execution_comparison(self):
        """Compare direct agent execution vs AgentNodeV3 execution."""
        print("\n" + "=" * 80)
        print("🧪 TEST: Direct Agent vs AgentNodeV3 Comparison")
        print("=" * 80)

        # Create agent with structured output
        agent = SimpleAgentV3(
            name="comparison_agent",
            engine=AugLLMConfig(
                structured_output_model=TestStructuredOutput,
                structured_output_version="v2",
                temperature=0.1,
                max_tokens=300,
                llm_config=AzureLLMConfig(),
            ),
            debug=True,
        )

        query = "Analyze the impact of machine learning on healthcare"

        print(f"🎯 Testing with query: {query}")

        # Test 1: Direct agent.run()
        print("\n🔄 TEST 1: Direct agent.run()"()")"
        try:
            result_run=agent.run(query)
            print(f"   Type: {type(result_run)}")
            print(
                f"   Has get_latest_structured_output: {
    hasattr(
        result_run,
         'get_latest_structured_output')}"
            )

            if hasattr(result_run, "get_latest_structured_output"):
                structured=result_run.get_latest_structured_output()
                print(
    f"   Structured output: {
        type(structured)} = {structured}")
            else:
                print(f"   Raw result: {result_run}")

        except Exception as e:
            print(f"❌ agent.run() failed: {e}")

        # Test 2: Direct agent.invoke()
        print("\n🔄 TEST 2: Direct agent.invoke()"()"" try:
            input_dict={"messages": [{"role": "user", "content": query}]}
            result_invoke=agent.invoke(input_dict)
            print(f"   Type: {type(result_invoke)}")
            print(
                f"   Has get_latest_structured_output: {
    hasattr(
        result_invoke,
         'get_latest_structured_output')}"
            )

            if hasattr(result_invoke, "get_latest_structured_output"):
                structured=result_invoke.get_latest_structured_output()
                print(
    f"   Structured output: {
        type(structured)} = {structured}")
            else:
                print(f"   Raw result: {result_invoke}")
                if isinstance(result_invoke, dict):
                    print(f"   Dict keys: {list(result_invoke.keys())}")

        except Exception as e:
            print(f"❌ agent.invoke() failed: {e}")

        # Test 3: AgentNodeV3 execution
        print("\n🔄 TEST 3: AgentNodeV3 execution")
        try:
            node=create_agent_node_v3(
    agent_name="comparison_agent", agent=agent)
            state=MultiAgentState(
                agents={"comparison_agent": agent},
                messages=[{"role": "user", "content": query}],
            )

            result_node=node(state)
            print(f"   Type: {type(result_node)}")
            print(f"   Result: {result_node}")

            if isinstance(result_node, dict):
                print(f"   Dict keys: {list(result_node.keys())}")
                for key, value in result_node.items():
                    print(f"     {key}: {type(value)}")

        except Exception as e:
            print(f"❌ AgentNodeV3 execution failed: {e}")
            logger.exception("AgentNodeV3 execution error")


def main():
    """Run all isolation tests."""
    print("🎯 AGENT NODE V3 ISOLATION TESTS")
    print("=" * 80)
    print("Testing AgentNodeV3 behavior with different agent configurations")
    print("to understand why complex output processing is needed.")
    print("=" * 80)

    test_suite=TestAgentNodeV3Isolation()

    # Run all tests
    test_suite.test_simple_agent_v3_with_structured_output()
    test_suite.test_simple_agent_v3_without_structured_output()
    test_suite.test_react_agent_v3_with_structured_output()
    test_suite.test_direct_agent_execution_comparison()

    print("\n" + "=" * 80)
    print("📊 ISOLATION TESTS COMPLETE")
    print("=" * 80)
    print("Review the output above to understand:")
    print("1. What AgentNodeV3 actually receives from agent.invoke()")
    print("2. How _process_agent_output() transforms the results")
    print("3. Why agents with output_schema don't return structured output directly")
    print("4. The difference between agent.run() and agent.invoke() behavior")


if __name__ == "__main__":
    main()
