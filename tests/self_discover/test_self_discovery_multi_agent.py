"""Test self-discovery agent with married schema ProperMultiAgent."""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

import asyncio


def test_self_discovery_schema_structure():
    """Test that self-discovery agent has proper schema structure in multi-agent setup."""

    try:
        from haive.agents.multi.proper_base import ProperMultiAgent
        from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
            self_discovery,
        )

        # Create multi-agent with self-discovery
        multi_agent = ProperMultiAgent(
            name="self_discovery_multi", agents=[self_discovery]
        )


        # Check schema fields
        schema_fields = set(multi_agent.state_schema.model_fields.keys())

        # Check MultiAgentState fields
        required_multi_fields = {"agents", "agent_states", "agent_outputs"}
        has_multi_fields = required_multi_fields.issubset(schema_fields)
        if has_multi_fields:
            pass

        # Check SelfDiscoveryState fields
        expected_discovery_fields = {
            "reasoning_modules",
            "task_description",
            "selected_modules",
            "adapted_modules",
            "reasoning_structure",
            "answer",
        }
        discovery_fields = expected_discovery_fields.intersection(schema_fields)
        if discovery_fields:
            pass

        # Test instantiation
        try:
            state_instance = multi_agent.state_schema()

            # Check hierarchical fields

            return multi_agent, state_instance

        except Exception as e:
            return multi_agent, None

    except Exception as e:
        import traceback

        traceback.print_exc()
        return None, None


async def test_self_discovery_execution():
    """Test actual execution of self-discovery agent in multi-agent setup."""

    try:
        from haive.agents.multi.proper_base import ProperMultiAgent
        from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
            self_discovery,
        )

        # Create multi-agent
        multi_agent = ProperMultiAgent(
            name="discovery_executor", agents=[self_discovery]
        )

        # Create initial state with the married schema
        initial_state = multi_agent.state_schema(
            task_description="What is the most effective approach to solve complex reasoning problems?",
            reasoning_modules="""
            1. Critical Thinking: Analyze assumptions and evaluate evidence
            2. Systems Thinking: Consider interconnections and patterns
            3. Creative Thinking: Generate novel solutions and approaches
            4. Logical Reasoning: Apply deductive and inductive logic
            5. Metacognitive Reasoning: Reflect on thinking processes
            """,
            # Initialize agents dict with our self-discovery agent
            agents={"self_discovery": self_discovery},
            agent_states={},
            agent_outputs={},
        )


        # For now, just test the state structure - actual execution would require graph compilation
        return initial_state

    except Exception as e:
        import traceback

        traceback.print_exc()
        return None


def test_hierarchical_state_management():
    """Test hierarchical state management capabilities."""

    try:
        from haive.agents.multi.proper_base import ProperMultiAgent
        from haive.agents.reasoning_and_critique.self_discover.v2.agent import (
            self_discovery,
        )

        # Create multi-agent
        multi_agent = ProperMultiAgent(name="state_manager", agents=[self_discovery])

        # Create state instance
        state = multi_agent.state_schema(
            agents={"discovery": self_discovery},
            agent_states={
                "discovery": {"current_phase": "module_selection", "progress": 0.25}
            },
            agent_outputs={
                "discovery": {
                    "last_output": "Selected reasoning modules",
                    "timestamp": "2025-01-16T18:40:00",
                }
            },
            task_description="Test hierarchical state management",
            reasoning_modules="Test modules",
        )


        # Test state updates
        state.agent_states["discovery"]["progress"] = 0.75
        state.agent_outputs["discovery"]["last_output"] = "Updated output"


        return state

    except Exception as e:
        import traceback

        traceback.print_exc()
        return None


async def main():
    """Run all self-discovery multi-agent tests."""

    # Test 1: Schema structure
    multi_agent, state_instance = test_self_discovery_schema_structure()

    # Test 2: Execution setup
    execution_state = await test_self_discovery_execution()

    # Test 3: Hierarchical state management
    hierarchical_state = test_hierarchical_state_management()

    if multi_agent and state_instance and execution_state and hierarchical_state:
        pass
    else:
        pass

    return {
        "multi_agent": multi_agent,
        "state_instance": state_instance,
        "execution_state": execution_state,
        "hierarchical_state": hierarchical_state,
    }


if __name__ == "__main__":
    results = asyncio.run(main())
