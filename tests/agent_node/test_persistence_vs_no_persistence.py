#!/usr/bin/env python3
"""Test AgentNodeV3 with and without persistence to isolate the structured output issue.

This will help us understand if persistence is interfering with structured output extraction.
"""

import logging

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.models.llm.base import AzureLLMConfig
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Test model
class SimpleTestModel(BaseModel):
    """Simple test model for structured output."""

    message: str = Field(description="The message content")
    count: int = Field(description="A count value", default=1)


def test_agent_direct_execution():
    """Test agent execution directly - no AgentNodeV3."""
    print("\n" + "=" * 80)
    print("🧪 TEST: Direct Agent Execution (Baseline)")
    print("=" * 80)

    # Create agent with structured output
    agent = SimpleAgentV3(
        name="direct_test",
        engine=AugLLMConfig(
            structured_output_model=SimpleTestModel,
            structured_output_version="v2",
            temperature=0.1,
            max_tokens=100,
            llm_config=AzureLLMConfig(),
        ),
        debug=True,
    )

    query = "Respond with the message 'Hello World' and count 42"

    print(f"📝 Query: {query}")
    print("🎯 Expected: SimpleTestModel(message='Hello World', count=42)"2)")"

    # Test agent.run()
    print("\n🔄 Testing agent.run()...")
    try:
        result_run = agent.run(query)
        print("✅ agent.run() completed")
        print(f"   Type: {type(result_run)}")
        print(
            f"   Has get_latest_structured_output: {
                hasattr(
                    result_run,
                    'get_latest_structured_output')}")

        if hasattr(result_run, "get_latest_structured_output"):
            structured = result_run.get_latest_structured_output()
            print(f"   Structured output: {type(structured)} = {structured}")
            if isinstance(structured, SimpleTestModel):
                print("   ✅ SUCCESS: Got SimpleTestModel directly")
                print(f"      message: {structured.message}")
                print(f"      count: {structured.count}")
            else:
                print(
                    f"   ❌ WRONG TYPE: Expected SimpleTestModel, got {
                        type(structured)}")
        else:
            print("   ❌ NO METHOD: Missing get_latest_structured_output()")""
    except Exception as e:
        print(f"❌ agent.run() failed: {e}")
        logger.exception("agent.run() error")

    # Test agent.invoke()
    print("\n🔄 Testing agent.invoke()...")
    try:
        input_dict = {"messages": [{"role": "user", "content": query}]}
        result_invoke = agent.invoke(input_dict)
        print("✅ agent.invoke() completed")
        print(f"   Type: {type(result_invoke)}")

        if isinstance(result_invoke, dict):
            print(f"   Dict keys: {list(result_invoke.keys())}")

            # Look for structured output in various places
            for key, value in result_invoke.items():
                if isinstance(value, dict) and "content" in value:
                    print(f"   {key}: {value}")
                elif isinstance(value, list) and key == "messages":
                    print(f"   {key}: {len(value)} messages")
                    for i, msg in enumerate(value):
                        if hasattr(msg, "tool_calls") and msg.tool_calls:
                            print(
                                f"     Message {i} has {len(msg.tool_calls)} tool calls"
                            )
                            for j, tool_call in enumerate(msg.tool_calls):
                                print(
                                    f"       Tool call {j}: {
                                        tool_call.name} = {
                                        tool_call.args}")
                        else:
                            print(f"     Message {i}: {type(msg).__name__}")

    except Exception as e:
        print(f"❌ agent.invoke() failed: {e}")
        logger.exception("agent.invoke() error")


def test_agent_node_v3_without_persistence():
    """Test AgentNodeV3 without persistence."""
    print("\n" + "=" * 80)
    print("🧪 TEST: AgentNodeV3 WITHOUT Persistence")
    print("=" * 80)

    # Create agent WITHOUT persistence
    agent = SimpleAgentV3(
        name="no_persist_test",
        engine=AugLLMConfig(
            structured_output_model=SimpleTestModel,
            structured_output_version="v2",
            temperature=0.1,
            max_tokens=100,
            llm_config=AzureLLMConfig(),
        ),
        # NO persistence settings - default should be no persistence
        debug=True,
    )

    print("✅ Created agent WITHOUT persistence")
    print(
        f"   Agent persistence config: {
            getattr(
                agent,
                'persistence',
                'None')}")
    print(
        f"   Agent state persistence: {
            getattr(
                agent,
                'state_persistence',
                'None')}")

    # Create AgentNodeV3
    node = create_agent_node_v3(agent_name="no_persist_test", agent=agent)

    # Create test state
    state = MultiAgentState(
        agents={"no_persist_test": agent},
        messages=[
            {
                "role": "user",
                "content": "Respond with message 'No Persistence' and count 100",
            }
        ],
    )

    print("\n🚀 Executing AgentNodeV3 without persistence...")

    try:
        result = node(state)
        print("✅ AgentNodeV3 execution completed")
        print(f"   Type: {type(result)}")

        if hasattr(result, "update") and isinstance(result.update, dict):
            print(f"   Command update keys: {list(result.update.keys())}")

            # Look for structured output fields
            for key, value in result.update.items():
                if key in [
                    "message",
                        "count"]:  # Our expected structured fields
                    print(
                        f"   ✅ DIRECT FIELD: {key} = {value} ({
                            type(value)})")
                elif key == "simple_test_model":  # Field name from model
                    print(f"   📦 MODEL FIELD: {key} = {value}")
                elif isinstance(value, dict) and "content" in value:
                    print(f"   📝 WRAPPED FIELD: {key} = {value}")
                elif key == "messages":
                    print(f"   💬 MESSAGES: {len(value)} messages")
                else:
                    print(f"   🔍 OTHER: {key} = {type(value)}")

    except Exception as e:
        print(f"❌ AgentNodeV3 without persistence failed: {e}")
        logger.exception("AgentNodeV3 no persistence error")


def test_agent_node_v3_with_persistence():
    """Test AgentNodeV3 with persistence enabled."""
    print("\n" + "=" * 80)
    print("🧪 TEST: AgentNodeV3 WITH Persistence")
    print("=" * 80)

    # Create agent WITH persistence
    agent = SimpleAgentV3(
        name="with_persist_test",
        engine=AugLLMConfig(
            structured_output_model=SimpleTestModel,
            structured_output_version="v2",
            temperature=0.1,
            max_tokens=100,
            llm_config=AzureLLMConfig(),
        ),
        # Enable persistence
        state_persistence=True,  # Enable state persistence
        debug=True,
    )

    print("✅ Created agent WITH persistence")
    print(
        f"   Agent persistence config: {
            getattr(
                agent,
                'persistence',
                'None')}")
    print(
        f"   Agent state persistence: {
            getattr(
                agent,
                'state_persistence',
                'None')}")
    print(f"   Agent has checkpointer: {hasattr(agent, 'checkpointer')}")

    # Create AgentNodeV3
    node = create_agent_node_v3(agent_name="with_persist_test", agent=agent)

    # Create test state
    state = MultiAgentState(
        agents={"with_persist_test": agent},
        messages=[
            {
                "role": "user",
                "content": "Respond with message 'With Persistence' and count 200",
            }
        ],
    )

    print("\n🚀 Executing AgentNodeV3 with persistence...")

    try:
        result = node(state)
        print("✅ AgentNodeV3 execution completed")
        print(f"   Type: {type(result)}")

        if hasattr(result, "update") and isinstance(result.update, dict):
            print(f"   Command update keys: {list(result.update.keys())}")

            # Look for structured output fields
            for key, value in result.update.items():
                if key in [
                    "message",
                        "count"]:  # Our expected structured fields
                    print(
                        f"   ✅ DIRECT FIELD: {key} = {value} ({
                            type(value)})")
                elif key == "simple_test_model":  # Field name from model
                    print(f"   📦 MODEL FIELD: {key} = {value}")
                elif isinstance(value, dict) and "content" in value:
                    print(f"   📝 WRAPPED FIELD: {key} = {value}")
                elif key == "messages":
                    print(f"   💬 MESSAGES: {len(value)} messages")
                else:
                    print(f"   🔍 OTHER: {key} = {type(value)}")

    except Exception as e:
        print(f"❌ AgentNodeV3 with persistence failed: {e}")
        logger.exception("AgentNodeV3 with persistence error")


def test_compare_agent_invoke_vs_node():
    """Compare what agent.invoke() returns vs what AgentNodeV3 processes."""
    print("\n" + "=" * 80)
    print("🧪 TEST: Compare agent.invoke() vs AgentNodeV3 Processing")
    print("=" * 80)

    # Create agent
    agent = SimpleAgentV3(
        name="compare_test",
        engine=AugLLMConfig(
            structured_output_model=SimpleTestModel,
            structured_output_version="v2",
            temperature=0.1,
            max_tokens=100,
            llm_config=AzureLLMConfig(),
        ),
        debug=True,
    )

    query = "Respond with message 'Compare Test' and count 999"

    print(f"📝 Query: {query}")

    # Test 1: Direct agent.invoke()
    print("\n🔄 Step 1: Direct agent.invoke()")
    input_dict = {"messages": [{"role": "user", "content": query}]}
    raw_result = agent.invoke(input_dict)

    print(f"   Raw result type: {type(raw_result)}")
    print(
        f"   Raw result keys: {
            list(
                raw_result.keys()) if isinstance(
                raw_result,
                dict) else 'Not dict'}")

    # Analyze the raw result in detail
    if isinstance(raw_result, dict):
        for key, value in raw_result.items():
            print(f"   {key}: {type(value)}")
            if key == "messages" and isinstance(value, list):
                for i, msg in enumerate(value):
                    print(f"     Message {i}: {type(msg).__name__}")
                    if hasattr(msg, "tool_calls") and msg.tool_calls:
                        for j, tc in enumerate(msg.tool_calls):
                            print(
                                f"       Tool call {j}: {tc.name} -> {tc.args}")
            elif isinstance(value, dict):
                print(f"     Dict contents: {value}")

    # Test 2: AgentNodeV3._process_agent_output() simulation
    print("\n🔄 Step 2: Simulate AgentNodeV3._process_agent_output()")

    # Check what _process_agent_output would do
    has_output_schema = hasattr(agent, "output_schema") and agent.output_schema
    print(f"   Agent has output_schema: {has_output_schema}")
    print(f"   Agent output_schema: {getattr(agent, 'output_schema', None)}")

    if has_output_schema:
        if isinstance(raw_result, BaseModel):
            print("   ✅ Result is BaseModel - would use result.model_dump()")
            state_update = raw_result.model_dump()
        elif isinstance(raw_result, dict):
            print("   ⚠️  Result is dict - would use result directly")
            state_update = raw_result
        else:
            print("   ❌ Result is other - would wrap in fallback")
            state_update = {"result": raw_result}

        print(f"   Simulated state_update keys: {list(state_update.keys())}")

        # Check for our expected structured fields
        if "message" in state_update and "count" in state_update:
            print("   ✅ SUCCESS: Found direct structured fields!")
            print(f"      message: {state_update['message']}")
            print(f"      count: {state_update['count']}")
        else:
            print("   ⚠️  No direct structured fields found")

            # Look for wrapped fields
            model_name_lower = SimpleTestModel.__name__.lower()
            for key, value in state_update.items():
                if model_name_lower in key.lower():
                    print(f"   📦 Found model field: {key} = {value}")

    # Test 3: Actual AgentNodeV3 execution
    print("\n🔄 Step 3: Actual AgentNodeV3 execution")

    node = create_agent_node_v3(agent_name="compare_test", agent=agent)
    state = MultiAgentState(agents={"compare_test": agent}, messages=[
        {"role": "user", "content": query}])

    try:
        node_result = node(state)
        print(f"   Node result type: {type(node_result)}")

        if hasattr(node_result, "update"):
            update_dict = node_result.update
            print(f"   Node update keys: {list(update_dict.keys())}")

            # Compare with our simulation
            print("\n📊 COMPARISON:")
            print(
                f"   Raw result keys: {
                    list(
                        raw_result.keys()) if isinstance(
                        raw_result,
                        dict) else 'Not dict'}")
            print(f"   Node update keys: {list(update_dict.keys())}")

            # Check if they match
            if isinstance(raw_result, dict):
                common_keys = set(raw_result.keys()) & set(update_dict.keys())
                only_raw = set(raw_result.keys()) - set(update_dict.keys())
                only_node = set(update_dict.keys()) - set(raw_result.keys())

                print(f"   Common keys: {common_keys}")
                print(f"   Only in raw: {only_raw}")
                print(f"   Only in node: {only_node}")

    except Exception as e:
        print(f"❌ AgentNodeV3 execution failed: {e}")
        logger.exception("AgentNodeV3 comparison error")


def main():
    """Run all persistence comparison tests."""
    print("🎯 PERSISTENCE vs NO-PERSISTENCE COMPARISON")
    print("=" * 80)
    print("Testing if persistence affects structured output extraction")
    print("=" * 80)

    # Run all tests
    test_agent_direct_execution()
    test_agent_node_v3_without_persistence()
    test_agent_node_v3_with_persistence()
    test_compare_agent_invoke_vs_node()

    print("\n" + "=" * 80)
    print("📊 PERSISTENCE COMPARISON COMPLETE")
    print("=" * 80)
    print("Review the output above to understand:")
    print("1. Does persistence affect structured output extraction?")
    print("2. What's the difference between agent.run() and agent.invoke()?")
    print("3. How does AgentNodeV3._process_agent_output() handle the results?")
    print("4. Where exactly are the structured output fields going?")


if __name__ == "__main__":
    main()
