#!/usr/bin/env python3
"""Verbose debug of SimpleAgentV3 validation node engine lookup.

This will show exactly what's happening when ValidationNodeConfigV2 tries to find
the Pydantic model from the engine.

Date: August 7, 2025
"""

import asyncio
import logging
import os

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3

# Enable verbose logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("haive.core.graph.node.validation_node_config_v2").setLevel(
    logging.DEBUG
)
logging.getLogger("haive.agents.simple.agent_v3").setLevel(logging.DEBUG)

# Disable postgres to focus on validation issue
os.environ["HAIVE_DISABLE_POSTGRES"] = "1"


# Simple model for testing
class TestAnalysis(BaseModel):
    """Simple test analysis."""

    result: str = Field(description="Analysis result")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")


async def debug_validation_lookup():
    """Debug the validation node engine lookup process."""

    print("🔍 DEBUGGING VALIDATION NODE ENGINE LOOKUP")
    print("=" * 70)

    # Create agent with v2 structured output
    agent = SimpleAgentV3(
        name="debug_validation_agent",
        engine=AugLLMConfig(
            temperature=0.3,
            max_tokens=150,
            system_message="You are a test analyst.",
            structured_output_model=TestAnalysis,
            structured_output_version="v2",  # This will trigger the validation issue
        ),
    )

    print(f"\n📋 AGENT CONFIGURATION:")
    print(f"- Agent name: {agent.name}")
    print(f"- Engine name: {agent.engine.name}")
    print(f"- Engine ID: {agent.engine.id}")
    print(f"- Structured model: {agent.engine.structured_output_model}")
    print(f"- Model name: {agent.engine.structured_output_model.__name__}")
    print(f"- Pydantic tools: {agent.engine.pydantic_tools}")
    print(f"- Tool routes: {agent.engine.tool_routes}")

    print(f"\n🏗️ GRAPH STRUCTURE:")
    if hasattr(agent, "_app") and agent._app:
        print(f"- Graph nodes: {list(agent._app.get_graph().nodes.keys())}")

        # Check if validation node exists and its config
        graph_dict = agent._app.get_graph().to_json()
        for node_name, node_data in graph_dict.get("nodes", {}).items():
            if node_name == "validation":
                print(f"\n🔍 VALIDATION NODE CONFIG:")
                print(f"- Node type: {type(node_data.get('data', {}))}")
                if hasattr(node_data.get("data"), "engine_name"):
                    validation_config = node_data["data"]
                    print(
                        f"- Engine name in validation: {validation_config.engine_name}"
                    )
                    print(
                        f"- Pydantic models dict: {validation_config.pydantic_models}"
                    )
                    print(f"- Available nodes: {validation_config.available_nodes}")

    print(f"\n🎯 TESTING EXECUTION...")
    try:
        # This will trigger the validation error
        result = await agent.arun(
            {"messages": [HumanMessage(content="Analyze: Test data")]}
        )

        print(f"\n✅ EXECUTION COMPLETED")
        print(f"Result type: {type(result).__name__}")

        # Check the state
        if hasattr(result, "engines"):
            print(f"\n🔍 STATE ENGINES:")
            for engine_name, engine in result.engines.items():
                print(f"- {engine_name}: {type(engine).__name__}")
                if hasattr(engine, "structured_output_model"):
                    print(f"  - Structured model: {engine.structured_output_model}")
                    if engine.structured_output_model:
                        print(
                            f"  - Model name: {engine.structured_output_model.__name__}"
                        )

    except Exception as e:
        print(f"\n❌ EXECUTION FAILED: {type(e).__name__}: {e}")

        # Show the validation flow that failed
        print(f"\n🔍 VALIDATION FLOW ANALYSIS:")
        print(
            f"1. ValidationNodeConfigV2 created with engine_name: {agent.engine.name}"
        )
        print(f"2. When validating 'TestAnalysis' tool call:")
        print(f"   - Looks in pydantic_models dict: empty by default")
        print(f"   - Falls back to _find_model_class_from_engine()")
        print(
            f"   - Calls _get_engine_from_state() with engine_name: {agent.engine.name}"
        )
        print(f"   - Should find engine in state.engines['{agent.engine.name}']")
        print(
            f"   - Should get engine.structured_output_model: {agent.engine.structured_output_model}"
        )
        print(f"   - Should match model name 'TestAnalysis' == 'TestAnalysis'")

        if "Unknown Pydantic model" in str(e):
            print(
                f"\n💡 ROOT CAUSE: Engine lookup in ValidationNodeConfigV2 is failing!"
            )
            print(f"   Either:")
            print(f"   1. Engine not found in state.engines")
            print(f"   2. Engine found but structured_output_model is None")
            print(f"   3. Model name mismatch")

        import traceback

        traceback.print_exc()

    print(f"\n🎯 NEXT STEPS:")
    print(f"1. Check if state.engines contains the correct engine")
    print(f"2. Verify engine_name matches between validation node and state")
    print(f"3. Confirm engine.structured_output_model is properly set")


if __name__ == "__main__":
    asyncio.run(debug_validation_lookup())
