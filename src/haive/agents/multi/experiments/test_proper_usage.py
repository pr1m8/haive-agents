"""Test cases showing proper usage of MultiAgentState, MetaStateSchema, and AgentNodeV3.

These tests demonstrate the key differences and proper patterns for using
the existing infrastructure correctly.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.agent_node_v3 import create_agent_node_v3
from haive.core.schema.prebuilt.meta_state import MetaStateSchema
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState
from haive.core.tools import tool
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent

from .proper_list_multi_agent import MetaListMultiAgent, ProperListMultiAgent


# Test tools
@tool
def calculator(expression: str) -> float:
    """Calculate mathematical expression."""
    try:
        return eval(expression)
    except:
        return 0.0


@tool
def word_counter(text: str) -> int:
    """Count words in text."""
    return len(text.split())


# Test structured output
class PlanModel(BaseModel):
    """A plan with steps."""

    title: str = Field(description="Plan title")
    steps: list[str] = Field(description="List of steps")


class TestProperMultiAgentUsage:
    """Test cases for proper multi-agent usage patterns."""

    def test_multi_agent_state_basic(self):
        """Test basic MultiAgentState usage."""
        # Create agents
        planner = SimpleAgent(name="planner")
        executor = SimpleAgent(name="executor")

        # Create MultiAgentState
        state = MultiAgentState(
            agents=[planner, executor],  # List gets converted to dict
            messages=[HumanMessage(content="Plan a project")],
        )

        # Verify structure
        assert isinstance(state.agents, dict)
        assert "planner" in state.agents
        assert "executor" in state.agents
        assert state.agent_count == 2

        # Verify agent state isolation
        state.update_agent_state("planner", {"current_task": "planning"})
        state.update_agent_state("executor", {"current_task": "executing"})

        planner_state = state.get_agent_state("planner")
        executor_state = state.get_agent_state("executor")

        assert planner_state["current_task"] == "planning"
        assert executor_state["current_task"] == "executing"
        assert (
            "current_task" not in planner_state
            or planner_state["current_task"] != "executing"
        )

        # Test engine syncing
        assert len(state.engines) > 0  # Engines synced from agents

        print("✅ MultiAgentState basic test passed")

    def test_meta_state_schema_basic(self):
        """Test basic MetaStateSchema usage."""
        # Create an agent
        simple_agent = SimpleAgent(name="embedded_agent")

        # Create MetaStateSchema
        meta_state = MetaStateSchema(
            agent=simple_agent,
            messages=[HumanMessage(content="Process this")],
            agent_input={"task": "analyze"},
            meta_context={"purpose": "testing"},
        )

        # Verify agent embedding
        assert meta_state.agent is not None
        assert meta_state.agent_name == "embedded_agent"
        assert meta_state.agent_type == "SimpleAgent"

        # Test engine syncing
        assert len(meta_state.engines) > 0  # Engines synced from agent

        # Test execution context
        assert meta_state.execution_status == "ready"
        assert meta_state.meta_context["purpose"] == "testing"

        print("✅ MetaStateSchema basic test passed")

    def test_agent_node_v3_basic(self):
        """Test AgentNodeV3 with MultiAgentState."""
        # Create agents
        planner = SimpleAgent(name="planner")
        executor = SimpleAgent(name="executor")

        # Create MultiAgentState
        MultiAgentState(
            agents={"planner": planner, "executor": executor},
            messages=[HumanMessage(content="Plan and execute")],
        )

        # Create AgentNodeV3 config
        node_config = create_agent_node_v3(
            agent_name="planner",
            agent=planner,
            name="planner_node",
            extract_from_container=True,
            project_state=True,
            update_container_state=True,
        )

        # Verify configuration
        assert node_config.agent_name == "planner"
        assert node_config.agent is planner
        assert node_config.extract_from_container
        assert node_config.project_state

        print("✅ AgentNodeV3 basic test passed")

    def test_proper_list_multi_agent(self):
        """Test ProperListMultiAgent with real infrastructure."""
        # Create agents
        planner = SimpleAgent(
            name="planner",
            engine=AugLLMConfig(
                structured_output_model=PlanModel, structured_output_version="v2"
            ),
        )

        executor = ReactAgent(name="executor", engine=AugLLMConfig(tools=[calculator]))

        # Create ProperListMultiAgent
        multi = ProperListMultiAgent(name="project_team")
        multi.append(planner)
        multi.append(executor)

        # Verify list interface
        assert len(multi) == 2
        assert multi[0] == planner
        assert multi[1] == executor
        assert list(multi) == [planner, executor]

        # Verify agent index
        assert multi._agent_index["planner"] == 0
        assert multi._agent_index["executor"] == 1

        # Verify state schema
        assert multi.state_schema == MultiAgentState

        # Test building graph
        graph = multi.build_graph()
        assert graph is not None

        # Should have init node + 2 agent nodes
        assert len(graph.nodes) >= 3

        print("✅ ProperListMultiAgent test passed")

    def test_meta_list_multi_agent(self):
        """Test MetaListMultiAgent with MetaStateSchema."""
        # Create agents
        analyzer = SimpleAgent(name="analyzer")
        reporter = SimpleAgent(name="reporter")

        # Create MetaListMultiAgent
        meta_multi = MetaListMultiAgent(name="analysis_pipeline")
        meta_multi.append(analyzer)
        meta_multi.append(reporter)

        # Verify list interface
        assert len(meta_multi) == 2
        assert meta_multi[0] == analyzer

        # Verify state schema
        assert meta_multi.state_schema == MetaStateSchema

        # Test building graph
        graph = meta_multi.build_graph()
        assert graph is not None

        print("✅ MetaListMultiAgent test passed")

    def test_conditional_routing(self):
        """Test conditional routing with ProperListMultiAgent."""
        # Create agents
        classifier = SimpleAgent(name="classifier")
        tech_expert = SimpleAgent(name="tech_expert")
        biz_expert = SimpleAgent(name="biz_expert")

        # Create multi-agent with routing
        multi = ProperListMultiAgent(name="routing_system")
        multi.append(classifier)
        multi.append(tech_expert)
        multi.append(biz_expert)

        # Add routing rule
        multi.when(
            condition=lambda state: state.get("category", "tech"),
            routes={"tech": tech_expert, "business": biz_expert},
        )

        # Verify routing rule added
        assert "classifier" in multi.routing_rules
        assert not multi.sequential  # Switched to conditional

        # Test building graph
        graph = multi.build_graph()
        assert graph is not None

        print("✅ Conditional routing test passed")

    def test_builder_pattern(self):
        """Test fluent builder pattern."""
        # Create agents
        planner = SimpleAgent(name="planner")
        researcher = SimpleAgent(name="researcher")
        writer = SimpleAgent(name="writer")
        reviewer = SimpleAgent(name="reviewer")

        # Build using fluent interface
        multi = (
            ProperListMultiAgent(name="content_pipeline")
            .then(planner)
            .then(researcher)
            .then(writer)
            .when(
                condition=lambda state: (
                    "approved" if state.get("quality", 0) > 0.8 else "revision"
                ),
                routes={"approved": "END", "revision": reviewer},
            )
            .then(reviewer)
        )

        # Verify structure
        assert len(multi) == 4
        assert multi.get_agent_names() == [
            "planner",
            "researcher",
            "writer",
            "reviewer",
        ]
        assert "writer" in multi.routing_rules

        print("✅ Builder pattern test passed")

    def test_recompilation_tracking(self):
        """Test recompilation tracking integration."""
        multi = ProperListMultiAgent(name="recompile_test")

        # Start with no recompilation needed
        assert not multi.needs_recompile
        assert multi.recompile_count == 0

        # Add agent - should trigger recompile
        agent = SimpleAgent(name="test_agent")
        multi.append(agent)

        assert multi.needs_recompile
        assert len(multi.recompile_reasons) > 0

        # Resolve recompilation
        multi.resolve_recompile()
        assert not multi.needs_recompile
        assert multi.recompile_count == 1

        print("✅ Recompilation tracking test passed")

    def test_tool_integration(self):
        """Test that tools work properly through agents."""
        # Create agents with tools
        math_agent = ReactAgent(
            name="math_agent", engine=AugLLMConfig(tools=[calculator])
        )

        text_agent = ReactAgent(
            name="text_agent", engine=AugLLMConfig(tools=[word_counter])
        )

        # Create multi-agent
        multi = ProperListMultiAgent(name="tool_test")
        multi.append(math_agent)
        multi.append(text_agent)

        # Verify tools are in agents (not in multi-agent)
        math_tools = multi.agents[0].get_all_tools()
        text_tools = multi.agents[1].get_all_tools()

        assert len(math_tools) > 0
        assert len(text_tools) > 0

        # Tools should be different for each agent
        math_tool_names = {t.name for t in math_tools}
        text_tool_names = {t.name for t in text_tools}

        assert "calculator" in math_tool_names
        assert "word_counter" in text_tool_names

        print("✅ Tool integration test passed")

    def run_all_tests(self):
        """Run all test cases."""
        print("🧪 Running proper multi-agent usage tests...\n")

        try:
            self.test_multi_agent_state_basic()
            self.test_meta_state_schema_basic()
            self.test_agent_node_v3_basic()
            self.test_proper_list_multi_agent()
            self.test_meta_list_multi_agent()
            self.test_conditional_routing()
            self.test_builder_pattern()
            self.test_recompilation_tracking()
            self.test_tool_integration()

            print("\n🎉 All tests passed!")

        except Exception as e:
            print(f"\n❌ Test failed: {e}")
            raise


def demonstration_usage():
    """Demonstrate proper usage patterns."""
    print("📚 Demonstration of proper multi-agent patterns:\n")

    # 1. Basic sequential multi-agent
    print("1. Basic Sequential Multi-Agent:")
    multi = ProperListMultiAgent("demo_sequential")
    multi.append(SimpleAgent(name="planner"))
    multi.append(SimpleAgent(name="executor"))
    multi.append(SimpleAgent(name="reviewer"))

    print(f"   Created: {multi}")
    print(f"   Agents: {multi.get_agent_names()}")
    print(f"   Uses: {multi.state_schema.__name__}")
    print()

    # 2. Conditional routing
    print("2. Conditional Routing:")
    conditional = ProperListMultiAgent("demo_conditional")
    conditional.append(SimpleAgent(name="classifier"))
    conditional.when(
        condition=lambda state: state.get("category", "general"),
        routes={
            "technical": SimpleAgent(name="tech_expert"),
            "business": SimpleAgent(name="biz_expert"),
            "general": SimpleAgent(name="generalist"),
        },
    )

    print(f"   Created: {conditional}")
    print(f"   Routing from: {list(conditional.routing_rules.keys())}")
    print(f"   Sequential: {conditional.sequential}")
    print()

    # 3. Meta multi-agent
    print("3. Meta Multi-Agent:")
    meta = MetaListMultiAgent("demo_meta")
    meta.append(SimpleAgent(name="analyzer"))
    meta.append(SimpleAgent(name="summarizer"))

    print(f"   Created: {meta}")
    print(f"   Uses: {meta.state_schema.__name__}")
    print()

    # 4. Builder pattern
    print("4. Builder Pattern:")
    builder = (
        ProperListMultiAgent("demo_builder")
        .then(SimpleAgent(name="step1"))
        .then(SimpleAgent(name="step2"))
        .when(
            condition=lambda s: "continue" if s.get("success") else "retry",
            routes={"continue": "END", "retry": SimpleAgent(name="retry_agent")},
        )
    )

    print(f"   Created: {builder}")
    print(f"   Final agents: {builder.get_agent_names()}")
    print()


if __name__ == "__main__":
    # Run tests
    tester = TestProperMultiAgentUsage()
    tester.run_all_tests()

    print("\n" + "=" * 50)

    # Run demonstrations
    demonstration_usage()
