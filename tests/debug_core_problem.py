"""Debug script to trace the core problem with detailed breakpoints."""

import sys
import traceback

# Add paths
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent


# Monkey patch AgentNodeV3 to add debugging
def debug_agent_node_call(original_call):
    def wrapper(self, state):
        print(f"\n🔍 AGENT NODE DEBUG: {self.name}")
        print(f"   Agent name: {self.agent_name}")
        print(f"   State type: {type(state)}")
        print(f"   State has 'agents': {hasattr(state, 'agents')}")

        if hasattr(state, "agents"):
            print(f"   State.agents type: {type(state.agents)}")
            if hasattr(state.agents, "__len__"):
                print(f"   State.agents length: {len(state.agents)}")
            if isinstance(state.agents, dict):
                print(f"   State.agents keys: {list(state.agents.keys())}")
            elif hasattr(state.agents, "__iter__"):
                print(f"   State.agents items: {list(state.agents)}")
            else:
                print(f"   State.agents value: {state.agents}")

        # Check all state attributes
        print(
            f"   State attributes: {[attr for attr in dir(state) if not attr.startswith('_')][:10]}..."
        )

        # Show state dict if available
        if hasattr(state, "__dict__"):
            print(f"   State.__dict__ keys: {list(state.__dict__.keys())[:10]}...")
            if "agents" in state.__dict__:
                print(f"   State.__dict__['agents']: {type(state.__dict__['agents'])}")
                if isinstance(state.__dict__["agents"], dict):
                    print(
                        f"   State.__dict__['agents'] keys: {list(state.__dict__['agents'].keys())}"
                    )

        # Call original
        try:
            result = original_call(state)
            print("   ✅ Agent node completed successfully")
            return result
        except Exception as e:
            print(f"   ❌ Agent node failed: {e}")
            traceback.print_exc()
            raise

    return wrapper


# Apply monkey patch
from haive.core.graph.node.agent_node_v3 import AgentNodeV3Config

original_call = AgentNodeV3Config.__call__
AgentNodeV3Config.__call__ = debug_agent_node_call(original_call)


# Also patch the set_active_agent method to see what's happening
def debug_set_active_agent(original_method):
    def wrapper(self, agent_name):
        print("\n🔍 SET_ACTIVE_AGENT DEBUG:")
        print(f"   Setting active agent: {agent_name}")
        print(f"   Self type: {type(self)}")
        print(
            f"   Self.agents type: {type(self.agents) if hasattr(self, 'agents') else 'NO AGENTS ATTR'}"
        )

        if hasattr(self, "agents"):
            if isinstance(self.agents, dict):
                print(f"   Available agents: {list(self.agents.keys())}")
            else:
                print(f"   Agents value: {self.agents}")

        # Call original
        return original_method(agent_name)

    return wrapper


from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState

original_set_active = MultiAgentState.set_active_agent
MultiAgentState.set_active_agent = debug_set_active_agent(original_set_active)


# Also patch the schema input preparation
def debug_prepare_schema_input(original_method):
    def wrapper(self, input_data, input_schema):
        print("\n🔍 PREPARE_SCHEMA_INPUT DEBUG:")
        print(f"   Input data type: {type(input_data)}")
        print(f"   Input schema: {input_schema}")
        print(
            f"   Agent has 'agents': {hasattr(self, 'agents') if hasattr(self, 'agents') else 'NO AGENTS'}"
        )

        if hasattr(self, "agents"):
            print(f"   Agent.agents type: {type(self.agents)}")
            if isinstance(self.agents, dict):
                print(f"   Agent.agents keys: {list(self.agents.keys())}")

        # Call original
        result = original_method(input_data, input_schema)

        print(f"   Result type: {type(result)}")
        if hasattr(result, "agents"):
            print(f"   Result.agents type: {type(result.agents)}")
            if isinstance(result.agents, dict):
                print(f"   Result.agents keys: {list(result.agents.keys())}")

        return result

    return wrapper


# Apply to ProperMultiAgent
ProperMultiAgent._prepare_schema_input = debug_prepare_schema_input(
    ProperMultiAgent._prepare_schema_input
)


async def trace_execution():
    """Trace the complete execution with detailed debugging."""

    print("=" * 100)
    print("🔍 CORE PROBLEM DIAGNOSIS")
    print("=" * 100)

    # Step 1: Create agents
    print("\n📌 STEP 1: Creating agents")
    agent1 = SimpleAgent(
        name="agent1",
        engine=AugLLMConfig(system_message="You are agent 1"),
    )
    agent2 = SimpleAgent(
        name="agent2",
        engine=AugLLMConfig(system_message="You are agent 2"),
    )
    print(f"   ✅ Created agents: {agent1.name}, {agent2.name}")

    # Step 2: Create multi-agent
    print("\n📌 STEP 2: Creating multi-agent")
    multi = ProperMultiAgent(
        name="debug_multi", agents=[agent1, agent2], execution_mode="sequential"
    )
    print(f"   ✅ Multi-agent created: {multi.name}")
    print(f"   Multi.agents: {list(multi.agents.keys())}")

    # Step 3: Check state schema
    print("\n📌 STEP 3: Checking state schema")
    print(f"   State schema: {multi.state_schema.__name__}")
    print(f"   Has 'agents' field: {'agents' in multi.state_schema.model_fields}")

    # Step 4: Create test state manually
    print("\n📌 STEP 4: Creating test state manually")
    test_state = multi.state_schema(
        messages=[HumanMessage(content="Test")], agents=multi.agents  # Explicitly set
    )
    print("   ✅ Manual state created")
    print(f"   Manual state.agents: {list(test_state.agents.keys())}")

    # Step 5: Test input preparation
    print("\n📌 STEP 5: Testing input preparation")
    test_input = {"messages": [HumanMessage(content="Test")]}

    # Call the input preparation method directly
    try:
        prepared_input = multi._prepare_schema_input(test_input, multi.state_schema)
        print("   ✅ Input prepared")
    except Exception as e:
        print(f"   ❌ Input preparation failed: {e}")
        # Try without the second parameter
        try:
            prepared_input = multi._prepare_schema_input(test_input)
            print("   ✅ Input prepared (without schema param)")")
        except Exception as e2:
            print(f"   ❌ Input preparation failed again: {e2}")

    # Step 6: Check graph structure
    print("\n📌 STEP 6: Checking graph structure")
    graph = multi.graph
    print(f"   Graph nodes: {list(graph.nodes.keys())}")

    # Step 7: Try to execute
    print("\n📌 STEP 7: Attempting execution")
    print("   🚀 Starting execution...")

    try:
        result = await multi.ainvoke(test_input)
        print("   ✅ Execution completed")
        print(f"   Result type: {type(result)}")

    except Exception as e:
        print(f"   ❌ Execution failed: {e}")
        print(f"   Exception type: {type(e)}")
        traceback.print_exc()

        # Try to get more info about the failure
        print("\n📌 FAILURE ANALYSIS:")
        print(f"   Error message: {str(e)}")

        if "not found in agents" in str(e):
            print("   🔍 This is the 'not found in agents' error!")
            print("   The agents field is empty when it reaches AgentNodeV3")

        return None

    return result


if __name__ == "__main__":
    import asyncio

    print("🚀 Starting core problem diagnosis...")
    print("This will trace through the entire execution with detailed debugging")

    result = asyncio.run(trace_execution())

    if result:
        print("\n✅ Execution completed successfully!")
    else:
        print("\n❌ Execution failed - see debugging output above")

    print("\n" + "=" * 100)
    print("Core problem diagnosis complete")
    print("=" * 100)
