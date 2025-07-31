#!/usr/bin/env python3
"""Comprehensive tests for ReWOO Tree Agent with real components.

This test suite validates all aspects of the ReWOO Tree Agent:
- Structured output models with field validators
- Tool aliasing and forced tool choice
- Parallelizable tree planning
- Recursive planning capabilities
- Real LLM integration (no mocks)
- BaseGraph integration
- Error handling and fallback strategies
"""

import asyncio

from langchain_core.tools import tool
import pytest

from haive.agents.planning.rewoo_tree_agent import (
    PlanNode,
    PlanTree,
    ReWOOTreeAgent,
    ReWOOTreeAgentState,
    ReWOOTreeExecutorOutput,
    ReWOOTreePlannerOutput,
    TaskPriority,
    TaskStatus,
    TaskType,
    ToolAlias,
)
from haive.core.engine.aug_llm import AugLLMConfig


# Test Tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e!s}"


@tool
def text_analyzer(text: str) -> str:
    """Analyze text and return insights."""
    word_count = len(text.split())
    char_count = len(text)
    return f"Analysis: {word_count} words, {char_count} characters"


@tool
def data_processor(data: str) -> str:
    """Process data and return formatted output."""
    lines = data.strip().split("\n")
    return f"Processed {len(lines)} lines of data"


@tool
def web_search(query: str) -> str:
    """Simulate web search (mock for testing)."""
    return f"Search results for: {query}"


@tool
def code_generator(specification: str) -> str:
    """Generate code based on specification."""
    return f"Generated code for: {specification}"


class TestStructuredOutputModels:
    """Test structured output models with field validators."""

    def test_tool_alias_validation(self):
        """Test ToolAlias model validation."""
        # Valid alias
        alias = ToolAlias(
            alias="calc",
            actual_tool="calculator",
            force_choice=True,
            parameters={"precision": 2},
        )
        assert alias.alias == "calc"
        assert alias.actual_tool == "calculator"
        assert alias.force_choice is True

        # Invalid alias (special characters)
        with pytest.raises(ValueError, match="alphanumeric"):
            ToolAlias(alias="calc-tool!", actual_tool="calculator")

    def test_plan_node_validation(self):
        """Test PlanNode model validation."""
        # Valid node
        node = PlanNode(
            id="test_node_1",
            name="Test Task",
            task_type=TaskType.EXECUTION,
            description="Test task description",
            priority=TaskPriority.HIGH,
        )
        assert node.id == "test_node_1"
        assert node.task_type == TaskType.EXECUTION
        assert node.status == TaskStatus.PENDING

        # Invalid node (self-dependency)
        with pytest.raises(ValueError, match="cannot depend on itself"):
            PlanNode(
                id="test_node_2",
                name="Test Task",
                description="Test description",
                dependencies=["test_node_2"],
            )

    def test_plan_tree_validation(self):
        """Test PlanTree model validation."""
        # Valid tree
        tree = PlanTree(
            id="test_tree_1", name="Test Plan", description="Test plan description"
        )

        # Add nodes
        root_node = PlanNode(
            id="root", name="Root Task", description="Root task description"
        )
        tree.add_node(root_node)

        assert tree.root_id == "root"
        assert len(tree.nodes) == 1
        assert tree.total_nodes == 1

        # Add child node
        child_node = PlanNode(
            id="child",
            name="Child Task",
            description="Child task description",
            parent_id="root",
        )
        tree.add_node(child_node)

        assert len(tree.nodes) == 2
        assert "child" in tree.nodes["root"].children_ids

    def test_rewoo_planner_output_validation(self):
        """Test ReWOOTreePlannerOutput validation."""
        # Create valid plan tree
        tree = PlanTree(
            id="plan_123", name="Test Plan", description="Test plan description"
        )

        # Valid output
        output = ReWOOTreePlannerOutput(
            plan_id="plan_123",
            plan_name="Test Plan",
            problem_analysis="Analysis of the problem",
            approach_strategy="Strategy for solving",
            plan_tree=tree,
            estimated_duration=60.0,
            parallelization_factor=2.0,
            required_tools=["calculator", "text_analyzer"],
            tool_aliases={"calc": ToolAlias(alias="calc", actual_tool="calculator")},
        )

        assert output.plan_id == "plan_123"
        assert output.plan_tree.id == "plan_123"
        assert "calculator" in output.required_tools


class TestReWOOTreeAgent:
    """Test ReWOO Tree Agent functionality."""

    @pytest.fixture
    def test_tools(self):
        """Provide test tools."""
        return [calculator, text_analyzer, data_processor, web_search, code_generator]

    @pytest.fixture
    def rewoo_agent(self, test_tools):
        """Create ReWOO Tree Agent for testing."""
        agent = ReWOOTreeAgent(
            name="test_rewoo_agent",
            engine=AugLLMConfig(temperature=0.1),
            available_tools=test_tools,
            max_planning_depth=3,
            max_parallelism=2,
        )

        # Add tool aliases
        agent.add_tool_alias("calc", "calculator", force_choice=True)
        agent.add_tool_alias("analyze", "text_analyzer", force_choice=True)
        agent.add_tool_alias("process", "data_processor", force_choice=True)

        return agent

    def test_agent_initialization(self, rewoo_agent):
        """Test agent initialization."""
        assert rewoo_agent.name == "test_rewoo_agent"
        assert len(rewoo_agent.available_tools) == 5
        assert len(rewoo_agent.tool_aliases) == 3
        assert rewoo_agent.max_planning_depth == 3
        assert rewoo_agent.max_parallelism == 2

        # Check specialized agents
        assert rewoo_agent.planner_agent is not None
        assert rewoo_agent.executor_agent is not None
        assert rewoo_agent.planner_agent.name == "test_rewoo_agent_planner"
        assert rewoo_agent.executor_agent.name == "test_rewoo_agent_executor"

    def test_tool_alias_management(self, rewoo_agent):
        """Test tool alias management."""
        # Add new alias
        rewoo_agent.add_tool_alias(
            "search", "web_search", force_choice=True, max_results=10
        )

        assert "search" in rewoo_agent.tool_aliases
        alias = rewoo_agent.tool_aliases["search"]
        assert alias.actual_tool == "web_search"
        assert alias.force_choice is True
        assert alias.parameters["max_results"] == 10

    def test_graph_building(self, rewoo_agent):
        """Test graph building."""
        graph = rewoo_agent.build_graph()

        # Check nodes
        expected_nodes = ["planner", "executor", "aggregator", "recursive_check"]
        for node_name in expected_nodes:
            assert node_name in graph.nodes

        # Check edges
        expected_edges = [
            ("__start__", "planner"),
            ("planner", "executor"),
            ("executor", "recursive_check"),
            ("recursive_check", "aggregator"),
            ("aggregator", "__end__"),
            ("recursive_check", "planner"),  # Recursive edge
        ]

        for edge in expected_edges:
            assert edge in graph.edges

    @pytest.mark.asyncio
    async def test_basic_execution(self, rewoo_agent):
        """Test basic agent execution with real LLM."""
        # Simple mathematical problem
        result = await rewoo_agent.arun("Calculate 15 * 23 and then analyze the result")

        assert isinstance(result, str)
        assert len(result) > 0
        # Should contain mathematical result
        assert "345" in result or "calculation" in result.lower()

        # Check state after execution
        assert rewoo_agent.conversation_history
        assert len(rewoo_agent.conversation_history) > 0

    @pytest.mark.asyncio
    async def test_complex_planning_task(self, rewoo_agent):
        """Test complex task requiring planning."""
        complex_task = """
        Create a comprehensive analysis of a simple calculator application:
        1. Calculate some basic math operations (5+3, 10*2, 15/3)
        2. Analyze the text description of calculator features
        3. Process the data about calculator usage
        4. Generate a summary report
        """

        result = await rewoo_agent.arun(complex_task)

        assert isinstance(result, str)
        assert len(result) > 0

        # Should contain evidence of planning and execution
        assert "plan" in result.lower() or "execution" in result.lower()

        # Check for mathematical results
        assert any(num in result for num in ["8", "20", "5"])  # Results of calculations

    @pytest.mark.asyncio
    async def test_tool_aliasing_execution(self, rewoo_agent):
        """Test execution with tool aliasing."""
        # Task that should use aliased tools
        result = await rewoo_agent.arun(
            "Use calc to compute 25 * 4, then analyze the result"
        )

        assert isinstance(result, str)
        assert len(result) > 0

        # Should contain the calculation result
        assert "100" in result or "calculation" in result.lower()

    @pytest.mark.asyncio
    async def test_parallel_execution_task(self, rewoo_agent):
        """Test task designed for parallel execution."""
        parallel_task = """
        Perform these independent tasks in parallel:
        1. Calculate 12 * 8
        2. Analyze the text "This is a test for parallel processing"
        3. Process the data "line1\nline2\nline3"
        4. Search for information about "parallel computing"
        """

        result = await rewoo_agent.arun(parallel_task)

        assert isinstance(result, str)
        assert len(result) > 0

        # Should contain results from all parallel tasks
        assert "96" in result  # 12 * 8
        assert "parallel" in result.lower()
        assert "3 lines" in result or "line" in result.lower()

    @pytest.mark.asyncio
    async def test_error_handling(self, rewoo_agent):
        """Test error handling and fallback strategies."""
        # Task with potential errors
        error_task = "Calculate 1/0 and handle any errors gracefully"

        result = await rewoo_agent.arun(error_task)

        assert isinstance(result, str)
        assert len(result) > 0

        # Should handle division by zero gracefully
        assert "error" in result.lower() or "fallback" in result.lower()

    @pytest.mark.asyncio
    async def test_state_management(self, rewoo_agent):
        """Test state management throughout execution."""
        # Execute a task
        await rewoo_agent.arun("Calculate 7 * 6 and analyze the result")

        # Check that state is properly maintained
        assert rewoo_agent.conversation_history

        # Get the last state (if available)
        if hasattr(rewoo_agent, "last_state"):
            state = rewoo_agent.last_state
            assert isinstance(state, ReWOOTreeAgentState)

            # Check state components
            if state.current_plan:
                assert isinstance(state.current_plan, ReWOOTreePlannerOutput)

            if state.current_execution:
                assert isinstance(state.current_execution, ReWOOTreeExecutorOutput)


class TestParallelizationAndTreeStructure:
    """Test parallelization and tree structure functionality."""

    def test_plan_tree_parallelization(self):
        """Test plan tree parallelization logic."""
        # Create a tree with parallelizable nodes
        tree = PlanTree(
            id="parallel_test",
            name="Parallel Test Plan",
            description="Test parallelization",
        )

        # Root node
        root = PlanNode(
            id="root",
            name="Root Task",
            description="Root task",
            task_type=TaskType.PLANNING,
        )
        tree.add_node(root)

        # Parallel children
        child1 = PlanNode(
            id="child1",
            name="Child 1",
            description="Independent task 1",
            task_type=TaskType.EXECUTION,
            parent_id="root",
            dependencies=["root"],
        )
        tree.add_node(child1)

        child2 = PlanNode(
            id="child2",
            name="Child 2",
            description="Independent task 2",
            task_type=TaskType.EXECUTION,
            parent_id="root",
            dependencies=["root"],
        )
        tree.add_node(child2)

        # Dependent child
        child3 = PlanNode(
            id="child3",
            name="Child 3",
            description="Dependent task",
            task_type=TaskType.VALIDATION,
            parent_id="root",
            dependencies=["root", "child1", "child2"],
        )
        tree.add_node(child3)

        # Test parallelization
        levels = tree.get_parallelizable_nodes()

        # Should have 3 levels: root, [child1, child2], child3
        assert len(levels) >= 2

        # First level should be root
        assert any(node.id == "root" for node in levels[0])

        # Second level should have child1 and child2
        level2_ids = [node.id for node in levels[1]]
        assert "child1" in level2_ids
        assert "child2" in level2_ids

    def test_node_execution_readiness(self):
        """Test node execution readiness logic."""
        # Create nodes with dependencies
        node1 = PlanNode(
            id="node1",
            name="Node 1",
            description="First node",
            status=TaskStatus.PENDING,
        )

        node2 = PlanNode(
            id="node2",
            name="Node 2",
            description="Second node",
            status=TaskStatus.PENDING,
            dependencies=["node1"],
        )

        node3 = PlanNode(
            id="node3",
            name="Node 3",
            description="Third node",
            status=TaskStatus.PENDING,
            dependencies=["node1", "node2"],
        )

        # Test execution readiness
        completed_nodes = set()

        # Initially, only node1 can execute
        assert node1.can_execute(completed_nodes)
        assert not node2.can_execute(completed_nodes)
        assert not node3.can_execute(completed_nodes)

        # After node1 completes
        completed_nodes.add("node1")
        assert node2.can_execute(completed_nodes)
        assert not node3.can_execute(completed_nodes)

        # After node2 completes
        completed_nodes.add("node2")
        assert node3.can_execute(completed_nodes)

    def test_tree_completion_tracking(self):
        """Test tree completion tracking."""
        tree = PlanTree(
            id="completion_test",
            name="Completion Test",
            description="Test completion tracking",
        )

        # Add nodes
        for i in range(3):
            node = PlanNode(
                id=f"node{i}", name=f"Node {i}", description=f"Node {i} description"
            )
            tree.add_node(node)

        # Initially 0% complete
        assert tree.get_completion_percentage() == 0.0
        assert not tree.is_complete()

        # Mark first node complete
        tree.mark_node_completed("node0", "result0")
        assert tree.get_completion_percentage() == pytest.approx(33.33, rel=1e-2)
        assert not tree.is_complete()

        # Mark second node complete
        tree.mark_node_completed("node1", "result1")
        assert tree.get_completion_percentage() == pytest.approx(66.67, rel=1e-2)
        assert not tree.is_complete()

        # Mark third node complete
        tree.mark_node_completed("node2", "result2")
        assert tree.get_completion_percentage() == 100.0
        assert tree.is_complete()

    def test_failure_handling(self):
        """Test failure handling in tree execution."""
        tree = PlanTree(
            id="failure_test", name="Failure Test", description="Test failure handling"
        )

        # Add nodes
        node1 = PlanNode(id="node1", name="Node 1", description="Node 1")
        node2 = PlanNode(id="node2", name="Node 2", description="Node 2")

        tree.add_node(node1)
        tree.add_node(node2)

        # Mark one node as failed
        tree.mark_node_failed("node1", "Test error")

        assert tree.has_failures()
        assert tree.failed_nodes == 1
        assert tree.nodes["node1"].status == TaskStatus.FAILED
        assert tree.nodes["node1"].error == "Test error"


class TestPerformanceAndOptimization:
    """Test performance and optimization features."""

    @pytest.mark.asyncio
    async def test_execution_timing(self):
        """Test execution timing and performance tracking."""
        # This test checks that timing is tracked properly
        node = PlanNode(
            id="timing_test",
            name="Timing Test",
            description="Test timing functionality",
        )

        # Test timing functions
        assert node.started_at is None
        assert node.completed_at is None

        node.mark_started()
        assert node.started_at is not None
        assert node.status == TaskStatus.IN_PROGRESS

        # Small delay to ensure timing difference
        await asyncio.sleep(0.01)

        node.mark_completed("test result")
        assert node.completed_at is not None
        assert node.status == TaskStatus.COMPLETED
        assert node.result == "test result"

        # Verify timing makes sense
        assert node.completed_at > node.started_at

    @pytest.mark.asyncio
    async def test_concurrent_execution_simulation(self):
        """Test concurrent execution simulation."""
        # Create tasks that can run concurrently
        tasks = []

        async def mock_task(task_id: str, duration: float):
            await asyncio.sleep(duration)
            return f"Task {task_id} completed"

        # Create multiple tasks
        for i in range(3):
            task = asyncio.create_task(mock_task(f"task_{i}", 0.01))
            tasks.append(task)

        # Wait for all tasks
        results = await asyncio.gather(*tasks)

        # Verify all tasks completed
        assert len(results) == 3
        for i, result in enumerate(results):
            assert result == f"Task task_{i} completed"


def test_integration_with_base_graph():
    """Test integration with BaseGraph system."""
    # Create ReWOO agent
    agent = ReWOOTreeAgent(
        name="integration_test",
        engine=AugLLMConfig(temperature=0.1),
        available_tools=[calculator, text_analyzer],
    )

    # Build graph
    graph = agent.build_graph()

    # Verify graph structure
    assert graph.name == "integration_test_rewoo_graph"
    assert graph.state_schema == ReWOOTreeAgentState

    # Check that all required nodes exist
    required_nodes = ["planner", "executor", "aggregator", "recursive_check"]
    for node_name in required_nodes:
        assert node_name in graph.nodes

    # Verify edges for proper flow
    edges = graph.edges
    assert ("__start__", "planner") in edges
    assert ("planner", "executor") in edges
    assert ("executor", "recursive_check") in edges
    assert ("recursive_check", "aggregator") in edges
    assert ("aggregator", "__end__") in edges


@pytest.mark.asyncio
async def test_end_to_end_workflow():
    """Test complete end-to-end workflow."""
    # Create comprehensive ReWOO agent
    agent = ReWOOTreeAgent(
        name="e2e_test_agent",
        engine=AugLLMConfig(temperature=0.1),
        available_tools=[calculator, text_analyzer, data_processor],
        max_planning_depth=2,
        max_parallelism=3,
    )

    # Add tool aliases
    agent.add_tool_alias("calc", "calculator")
    agent.add_tool_alias("analyze", "text_analyzer")
    agent.add_tool_alias("process", "data_processor")

    # Complex task requiring planning and execution
    complex_task = """
    Create a comprehensive analysis workflow:
    1. Calculate the following: 25 * 4, 100 / 5, 15 + 35
    2. Analyze this text: "The ReWOO Tree Agent provides parallelizable execution with tool aliasing"
    3. Process this data: "item1\nitem2\nitem3\nitem4"
    4. Combine all results into a final report
    """

    # Execute the workflow
    result = await agent.arun(complex_task)

    # Verify results
    assert isinstance(result, str)
    assert len(result) > 0

    # Check for evidence of all operations
    assert "100" in result  # 25 * 4 = 100
    assert "20" in result  # 100 / 5 = 20
    assert "50" in result  # 15 + 35 = 50
    assert "ReWOO" in result or "parallelizable" in result  # Text analysis
    assert "item" in result or "4" in result  # Data processing (4 items)

    # Verify conversation history
    assert agent.conversation_history
    assert len(agent.conversation_history) > 0

    # Check that planning and execution occurred
    assert "plan" in result.lower() or "execution" in result.lower()


if __name__ == "__main__":
    # Run tests

    # Run individual test functions
    asyncio.run(test_end_to_end_workflow())

    # Run structured model tests
    structured_tests = TestStructuredOutputModels()
    structured_tests.test_tool_alias_validation()
    structured_tests.test_plan_node_validation()
    structured_tests.test_plan_tree_validation()
    structured_tests.test_rewoo_planner_output_validation()

    # Run parallelization tests
    parallel_tests = TestParallelizationAndTreeStructure()
    parallel_tests.test_plan_tree_parallelization()
    parallel_tests.test_node_execution_readiness()
    parallel_tests.test_tree_completion_tracking()
    parallel_tests.test_failure_handling()

    # Integration test
    test_integration_with_base_graph()
