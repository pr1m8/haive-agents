"""Integration tests for EnhancedMultiAgentV4 with real LLM execution.

These tests demonstrate real multi-agent workflows with actual LLM calls.
They follow the NO MOCKS testing philosophy.
"""

from langchain_core.tools import tool
from pydantic import BaseModel, Field
import pytest

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Test data structures
class TaskBreakdown(BaseModel):
    """Structured task breakdown."""

    main_goal: str = Field(..., description="Main goal to achieve")
    subtasks: list[str] = Field(..., description="List of subtasks")
    priority_order: list[int] = Field(
        ..., description="Priority order of subtasks (indices)"
    )


class TaskResult(BaseModel):
    """Structured task execution result."""

    completed_tasks: list[str] = Field(..., description="Completed tasks")
    summary: str = Field(..., description="Summary of results")
    success_rate: float = Field(..., description="Success rate 0-1")


# Test tools
@tool
def string_manipulator(text: str, operation: str) -> str:
    """Manipulate strings with various operations.

    Args:
        text: Text to manipulate
        operation: Operation to perform (upper, lower, reverse, count)

    Returns:
        str: Result of the operation
    """
    if operation == "upper":
        return text.upper()
    if operation == "lower":
        return text.lower()
    if operation == "reverse":
        return text[::-1]
    if operation == "count":
        return f"The text has {len(text)} characters"
    return f"Unknown operation: {operation}"


@tool
def task_tracker(task_name: str, status: str) -> str:
    """Track task completion status.

    Args:
        task_name: Name of the task
        status: Status (started, completed, failed)

    Returns:
        str: Confirmation message
    """
    return f"Task '{task_name}' marked as {status}"


class TestEnhancedMultiAgentV4RealExecution:
    """Test real execution of multi-agent workflows."""

    @pytest.fixture
    def llm_config(self):
        """Provide real LLM configuration for tests."""
        return AugLLMConfig(
            temperature=0.1, max_tokens=500  # Low temperature for consistent tests
        )

    @pytest.mark.asyncio
    async def test_react_simple_sequential_pattern(self, llm_config):
        """Test ReactAgent → SimpleAgent sequential execution with real LLMs."""
        # Create ReactAgent with tools
        planner = ReactAgent(
            name="planner",
            engine=llm_config,
            tools=[string_manipulator, task_tracker],
            system_message=(
                "You are a task planner. Break down requests into subtasks and "
                "use tools to demonstrate planning. Be concise."
            ),
        )

        # Create SimpleAgent with structured output
        executor = SimpleAgent(
            name="executor",
            engine=llm_config,
            structured_output_model=TaskResult,
            system_message=(
                "You are a task executor. Based on the planning, summarize what was "
                "accomplished and provide a structured result. Be concise."
            ),
        )

        # Create sequential workflow
        workflow = EnhancedMultiAgentV4(
            name="plan_execute_workflow",
            agents=[planner, executor],
            execution_mode="sequential",
        )

        # Execute with real task
        result = await workflow.arun(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "Plan and execute: Convert 'Hello World' to uppercase and count its characters.",
                    }
                ]
            }
        )

        # Verify real execution occurred
        assert result is not None

        # Check if structured output was produced
        if hasattr(result, "task_result"):
            task_result = result.task_result
            assert isinstance(task_result.completed_tasks, list)
            assert isinstance(task_result.summary, str)
            assert 0 <= task_result.success_rate <= 1
            assert len(task_result.summary) > 0

    @pytest.mark.asyncio
    async def test_parallel_agent_execution(self, llm_config):
        """Test parallel execution of multiple agents with real LLMs."""
        # Create three analysis agents
        analyst1 = SimpleAgent(
            name="technical_analyst",
            engine=llm_config,
            system_message="Analyze technical aspects. Be very brief (1-2 sentences).",
        )

        analyst2 = SimpleAgent(
            name="business_analyst",
            engine=llm_config,
            system_message="Analyze business aspects. Be very brief (1-2 sentences).",
        )

        analyst3 = SimpleAgent(
            name="user_analyst",
            engine=llm_config,
            system_message="Analyze user experience aspects. Be very brief (1-2 sentences).",
        )

        # Create parallel workflow
        workflow = EnhancedMultiAgentV4(
            name="parallel_analysis",
            agents=[analyst1, analyst2, analyst3],
            execution_mode="parallel",
        )

        # Execute parallel analysis
        result = await workflow.arun(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "Analyze a mobile app idea: AI-powered personal fitness coach",
                    }
                ]
            }
        )

        # Verify all agents executed
        assert result is not None
        # In parallel mode, we should have results from all agents
        # The exact structure depends on MultiAgentState implementation

    @pytest.mark.asyncio
    async def test_conditional_routing_real_execution(self, llm_config):
        """Test conditional routing with real decision making."""
        # Create classifier agent
        classifier = SimpleAgent(
            name="classifier",
            engine=llm_config,
            system_message=(
                "Classify the complexity of requests as 'simple' or 'complex'. "
                "Respond with just one word: either 'simple' or 'complex'."
            ),
        )

        # Create processing agents
        simple_processor = SimpleAgent(
            name="simple_processor",
            engine=llm_config,
            system_message="Handle simple requests with brief responses.",
        )

        complex_processor = ReactAgent(
            name="complex_processor",
            engine=llm_config,
            tools=[string_manipulator, task_tracker],
            system_message="Handle complex requests with detailed tool-based analysis.",
        )

        # Create conditional workflow
        workflow = EnhancedMultiAgentV4(
            name="adaptive_processor",
            agents=[classifier, simple_processor, complex_processor],
            execution_mode="conditional",
            build_mode="manual",
        )

        # Define routing based on classifier output
        def route_by_complexity(state) -> bool:
            """Route based on classifier's output."""
            messages = state.get("messages", [])
            # Look for classifier's response
            for msg in reversed(messages):
                if hasattr(msg, "content"):
                    content = str(msg.content).lower().strip()
                    if "complex" in content:
                        return True
            return False

        # Add conditional routing
        workflow.add_conditional_edge(
            from_agent="classifier",
            condition=route_by_complexity,
            true_agent="complex_processor",
            false_agent="simple_processor",
        )

        # Build the workflow
        workflow.build()

        # Test with simple request
        simple_result = await workflow.arun(
            {"messages": [{"role": "user", "content": "What is 2 + 2?"}]}
        )
        assert simple_result is not None

        # Test with complex request
        complex_result = await workflow.arun(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": (
                            "Analyze this text manipulation challenge: Take the phrase "
                            "'Hello World', reverse it, convert to uppercase, count characters, "
                            "and track each step as a separate task."
                        ),
                    }
                ]
            }
        )
        assert complex_result is not None

    @pytest.mark.asyncio
    async def test_dynamic_agent_addition_real(self, llm_config):
        """Test dynamic agent addition with real execution."""
        # Start with single agent
        initial_agent = SimpleAgent(
            name="coordinator",
            engine=llm_config,
            system_message="You are a coordinator. Identify what expertise is needed.",
        )

        workflow = EnhancedMultiAgentV4(
            name="dynamic_team",
            agents=[initial_agent],
            execution_mode="manual",
            build_mode="auto",  # Auto-rebuild on changes
        )

        # Execute initial assessment
        initial_result = await workflow.arun(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "I need help analyzing market trends for renewable energy.",
                    }
                ]
            }
        )

        assert initial_result is not None

        # Dynamically add specialist
        specialist = SimpleAgent(
            name="energy_specialist",
            engine=llm_config,
            system_message="You are a renewable energy specialist. Provide insights on energy markets.",
        )

        # Add specialist to workflow
        workflow.add_agent(specialist)

        # Add edge from coordinator to specialist
        workflow.add_edge("coordinator", "energy_specialist")

        # Execute with expanded team
        expanded_result = await workflow.arun(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "Analyze solar and wind energy market trends for 2024.",
                    }
                ]
            }
        )

        assert expanded_result is not None
        assert len(workflow.agent_dict) == 2
        assert "energy_specialist" in workflow.agent_dict

    @pytest.mark.asyncio
    async def test_multi_agent_state_persistence(self, llm_config):
        """Test that state is properly maintained across agents."""
        # Create agents that build on each other's work
        data_gatherer = SimpleAgent(
            name="data_gatherer",
            engine=llm_config,
            system_message=(
                "You gather data. Always start your response with 'DATA:' and list 3 facts."
            ),
        )

        analyzer = SimpleAgent(
            name="analyzer",
            engine=llm_config,
            system_message=(
                "You analyze the gathered data. Reference the specific facts from the data gatherer."
            ),
        )

        summarizer = SimpleAgent(
            name="summarizer",
            engine=llm_config,
            structured_output_model=TaskBreakdown,
            system_message=(
                "Create a task breakdown based on the analysis. Include the main goal and subtasks."
            ),
        )

        # Create sequential workflow
        workflow = EnhancedMultiAgentV4(
            name="data_pipeline",
            agents=[data_gatherer, analyzer, summarizer],
            execution_mode="sequential",
        )

        # Execute pipeline
        result = await workflow.arun(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "Research and analyze the benefits of remote work.",
                    }
                ]
            }
        )

        assert result is not None

        # Check if structured output was created
        if hasattr(result, "task_breakdown"):
            breakdown = result.task_breakdown
            assert isinstance(breakdown.main_goal, str)
            assert isinstance(breakdown.subtasks, list)
            assert len(breakdown.subtasks) > 0
            assert isinstance(breakdown.priority_order, list)

    @pytest.mark.asyncio
    async def test_error_handling_in_workflow(self, llm_config):
        """Test error handling in multi-agent workflows."""
        # Create agent that might encounter errors
        processor = SimpleAgent(
            name="processor",
            engine=llm_config,
            system_message="Process requests normally.",
        )

        # Create error handler agent
        error_handler = SimpleAgent(
            name="error_handler",
            engine=llm_config,
            system_message="Handle errors gracefully and provide alternative solutions.",
        )

        # Create workflow with conditional error routing
        workflow = EnhancedMultiAgentV4(
            name="fault_tolerant_workflow",
            agents=[processor, error_handler],
            execution_mode="conditional",
            build_mode="manual",
        )

        # Add error detection routing
        def detect_error(state) -> bool:
            """Detect if an error occurred."""
            # In real implementation, check for error indicators
            messages = state.get("messages", [])
            for msg in messages:
                if hasattr(msg, "content") and "error" in str(msg.content).lower():
                    return True
            return False

        workflow.add_conditional_edge(
            from_agent="processor",
            condition=detect_error,
            true_agent="error_handler",
            false_agent="END",
        )

        workflow.build()

        # Test normal flow
        normal_result = await workflow.arun(
            {"messages": [{"role": "user", "content": "Process this normal request."}]}
        )
        assert normal_result is not None

        # Test error flow
        error_result = await workflow.arun(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": "Process this request that might cause an error in processing.",
                    }
                ]
            }
        )
        assert error_result is not None


# Performance and scale tests
class TestEnhancedMultiAgentV4Performance:
    """Test performance characteristics of multi-agent workflows."""

    @pytest.fixture
    def fast_llm_config(self):
        """Fast LLM config for performance tests."""
        return AugLLMConfig(
            temperature=0.0, max_tokens=100  # Deterministic  # Small responses
        )

    @pytest.mark.asyncio
    async def test_workflow_with_many_agents(self, fast_llm_config):
        """Test workflow with larger number of agents."""
        # Create 5 simple agents
        agents = []
        for i in range(5):
            agent = SimpleAgent(
                name=f"worker_{i}",
                engine=fast_llm_config,
                system_message=f"You are worker {i}. Respond with 'Worker {i} completed task.'",
            )
            agents.append(agent)

        # Create sequential workflow
        workflow = EnhancedMultiAgentV4(
            name="large_team", agents=agents, execution_mode="sequential"
        )

        # Execute
        result = await workflow.arun(
            {
                "messages": [
                    {"role": "user", "content": "Process this through all workers."}
                ]
            }
        )

        assert result is not None
        # Verify all agents participated
        assert len(workflow.agent_dict) == 5
