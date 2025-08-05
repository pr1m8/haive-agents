"""Test Enhanced MultiAgent V4 - Enhanced base agent pattern."""

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState


class TestEnhancedMultiAgentV4:
    """Test Enhanced MultiAgent V4 with enhanced base agent pattern."""

    def test_basic_creation_with_agent_list(self):
        """Test basic creation with list of agents."""
        agents = [
            SimpleAgent(name="agent1", engine=AugLLMConfig()),
            SimpleAgent(name="agent2", engine=AugLLMConfig()),
        ]

        workflow = EnhancedMultiAgentV4(
            name="test_workflow",
            agents=agents,
            execution_mode="sequential",
            build_mode="manual",  # Don't auto-build for testing
        )

        # Verify setup
        assert workflow.name == "test_workflow"
        assert len(workflow.agents) == 2
        assert len(workflow.agent_dict) == 2
        assert "agent1" in workflow.agent_dict
        assert "agent2" in workflow.agent_dict
        assert workflow.execution_mode == "sequential"
        assert workflow.build_mode == "manual"

    def test_enhanced_base_agent_integration(self):
        """Test that it properly extends enhanced base agent."""
        agents = [SimpleAgent(name="test_agent", engine=AugLLMConfig())]

        workflow = EnhancedMultiAgentV4(name="integration_test", agents=agents, build_mode="manual")

        # Should inherit from Agent
        from haive.agents.base.agent import Agent

        assert isinstance(workflow, Agent)

        # Should have enhanced base agent capabilities
        assert hasattr(workflow, "build_graph")  # Abstract method
        assert hasattr(workflow, "state_schema")  # Schema management
        assert hasattr(workflow, "run")  # Execution interface
        assert hasattr(workflow, "arun")  # Async execution

        # Should use MultiAgentState by default
        assert workflow.state_schema == MultiAgentState

    def test_build_graph_implementation(self):
        """Test build_graph() implementation."""
        agents = [
            SimpleAgent(name="planner", engine=AugLLMConfig()),
            SimpleAgent(name="executor", engine=AugLLMConfig()),
        ]

        workflow = EnhancedMultiAgentV4(
            name="build_test",
            agents=agents,
            execution_mode="sequential",
            build_mode="manual",
        )

        # Build graph manually
        graph = workflow.build_graph()

        # Verify graph creation
        assert graph is not None
        from haive.core.graph.state_graph.base_graph2 import BaseGraph

        assert isinstance(graph, BaseGraph)

        # Verify agents were added as nodes
        assert "planner" in graph.nodes
        assert "executor" in graph.nodes

    def test_execution_modes(self):
        """Test different execution modes."""
        agents = [
            SimpleAgent(name="agent1", engine=AugLLMConfig()),
            SimpleAgent(name="agent2", engine=AugLLMConfig()),
            SimpleAgent(name="agent3", engine=AugLLMConfig()),
        ]

        # Sequential mode
        sequential = EnhancedMultiAgentV4(
            name="sequential_test",
            agents=agents,
            execution_mode="sequential",
            build_mode="manual",
        )
        seq_graph = sequential.build_graph()
        assert seq_graph is not None

        # Parallel mode
        parallel = EnhancedMultiAgentV4(
            name="parallel_test",
            agents=agents,
            execution_mode="parallel",
            build_mode="manual",
        )
        par_graph = parallel.build_graph()
        assert par_graph is not None

        # Manual mode
        manual = EnhancedMultiAgentV4(
            name="manual_test",
            agents=agents,
            execution_mode="manual",
            build_mode="manual",
        )
        man_graph = manual.build_graph()
        assert man_graph is not None

    def test_conditional_edges(self):
        """Test conditional edge functionality."""
        agents = [
            SimpleAgent(name="classifier", engine=AugLLMConfig()),
            SimpleAgent(name="simple_processor", engine=AugLLMConfig()),
            SimpleAgent(name="complex_processor", engine=AugLLMConfig()),
        ]

        workflow = EnhancedMultiAgentV4(
            name="conditional_test",
            agents=agents,
            execution_mode="conditional",
            build_mode="manual",
        )

        # Add conditional edge
        def complexity_condition(state):
            return state.get("complexity", 0) > 0.5

        workflow.add_conditional_edge(
            from_agent="classifier",
            condition=complexity_condition,
            true_agent="complex_processor",
            false_agent="simple_processor",
        )

        # Verify configuration
        assert len(workflow.conditional_edges) == 1
        edge = workflow.conditional_edges[0]
        assert edge["from_agent"] == "classifier"
        assert edge["destinations"][True] == "complex_processor"
        assert edge["destinations"][False] == "simple_processor"

        # Build graph
        graph = workflow.build_graph()
        assert graph is not None

    def test_multi_conditional_edge(self):
        """Test multi-way conditional routing."""
        agents = [
            SimpleAgent(name="router", engine=AugLLMConfig()),
            SimpleAgent(name="billing", engine=AugLLMConfig()),
            SimpleAgent(name="technical", engine=AugLLMConfig()),
            SimpleAgent(name="general", engine=AugLLMConfig()),
        ]

        workflow = EnhancedMultiAgentV4(
            name="multi_conditional_test",
            agents=agents,
            execution_mode="conditional",
            build_mode="manual",
        )

        # Add multi-way conditional
        def category_condition(state):
            return state.get("category", "general")

        workflow.add_multi_conditional_edge(
            from_agent="router",
            condition=category_condition,
            routes={
                "billing": "billing",
                "technical": "technical",
                "general": "general",
            },
        )

        # Verify configuration
        assert len(workflow.conditional_edges) == 1
        edge = workflow.conditional_edges[0]
        assert edge["from_agent"] == "router"
        assert "billing" in edge["destinations"]
        assert "technical" in edge["destinations"]
        assert "general" in edge["destinations"]

    def test_build_modes(self):
        """Test different build modes."""
        agents = [SimpleAgent(name="agent1", engine=AugLLMConfig())]

        # Manual mode - no auto build
        manual = EnhancedMultiAgentV4(name="manual_test", agents=agents, build_mode="manual")
        # Graph should not be built automatically
        assert not hasattr(manual, "graph") or manual.graph is None

        # Auto mode - builds on init (via enhanced base agent)
        EnhancedMultiAgentV4(name="auto_test", agents=agents, build_mode="auto")
        # Enhanced base agent should build graph automatically
        # (This depends on enhanced base agent implementation)

    def test_utility_methods(self):
        """Test utility methods."""
        agents = [
            SimpleAgent(name="agent1", engine=AugLLMConfig()),
            SimpleAgent(name="agent2", engine=AugLLMConfig()),
        ]

        workflow = EnhancedMultiAgentV4(name="utility_test", agents=agents, build_mode="manual")

        # Test get_agent_names
        names = workflow.get_agent_names()
        assert names == ["agent1", "agent2"]

        # Test get_agent
        agent1 = workflow.get_agent("agent1")
        assert agent1 is agents[0]

        # Test get non-existent agent
        assert workflow.get_agent("nonexistent") is None

        # Test add_agent
        new_agent = SimpleAgent(name="agent3", engine=AugLLMConfig())
        workflow.add_agent(new_agent)

        assert len(workflow.agent_dict) == 3
        assert "agent3" in workflow.agent_dict
        assert workflow.get_agent("agent3") is new_agent

    def test_display_info(self, capsys):
        """Test workflow info display."""
        agents = [
            SimpleAgent(name="agent1", engine=AugLLMConfig()),
            SimpleAgent(name="agent2", engine=AugLLMConfig()),
        ]

        workflow = EnhancedMultiAgentV4(
            name="info_test",
            agents=agents,
            execution_mode="sequential",
            build_mode="manual",
        )

        # Test display
        workflow.display_info()

        captured = capsys.readouterr()
        assert "Enhanced MultiAgent V4: info_test" in captured.out
        assert "Execution Mode: sequential" in captured.out
        assert "agent1 (SimpleAgent)" in captured.out
        assert "agent2 (SimpleAgent)" in captured.out


# Future integration test with real execution
class TestEnhancedMultiAgentV4Integration:
    """Integration tests - can be expanded for real execution."""

    def test_ready_for_real_execution(self):
        """Test that structure is ready for real execution."""
        # This test verifies the structure is ready
        # Real execution tests can be added when LLM is available

        agents = [
            SimpleAgent(name="greeter", engine=AugLLMConfig(temperature=0.1)),
            SimpleAgent(name="responder", engine=AugLLMConfig(temperature=0.1)),
        ]

        workflow = EnhancedMultiAgentV4(
            name="integration_test",
            agents=agents,
            execution_mode="sequential",
            build_mode="manual",
        )

        # Build graph
        graph = workflow.build_graph()
        assert graph is not None

        # Verify enhanced base agent interface
        assert hasattr(workflow, "arun")
        assert hasattr(workflow, "run")

        # Structure looks good for real execution when LLM available
