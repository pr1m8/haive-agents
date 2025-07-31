"""Test EnhancedMultiAgentV4 with SimpleAgentV3 and ReactAgentV3."""

from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent_v3 import ReactAgentV3
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Define test tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e!s}"


@tool
def text_formatter(text: str, format_type: str = "uppercase") -> str:
    """Format text in various ways."""
    if format_type == "uppercase":
        return text.upper()
    if format_type == "lowercase":
        return text.lower()
    if format_type == "title":
        return text.title()
    return text


@tool
def data_analyzer(data: str) -> str:
    """Analyze data and return insights."""
    words = data.split()
    return f"Analysis: {len(words)} words, {len(data)} characters"


# Define structured output models
class TaskPlan(BaseModel):
    """Structured output for task planning."""

    task_description: str = Field(description="Description of the task")
    steps: list[str] = Field(description="Steps to complete the task")
    tools_needed: list[str] = Field(description="Tools required")
    estimated_difficulty: float = Field(
        ge=0.0, le=1.0, description="Difficulty estimate"
    )


class TaskResult(BaseModel):
    """Structured output for task results."""

    original_task: str = Field(description="Original task description")
    execution_steps: list[str] = Field(description="Steps that were executed")
    final_result: str = Field(description="Final result of the task")
    success: bool = Field(description="Whether the task was successful")


def test_sequential_flow_simple_to_react():
    """Test sequential flow from SimpleAgentV3 to ReactAgentV3."""
    # Create SimpleAgentV3 for initial processing
    simple_agent = SimpleAgentV3(
        name="preprocessor", engine=AugLLMConfig(temperature=0.1), debug=True
    )

    # Create ReactAgentV3 with tools for processing
    react_agent = ReactAgentV3(
        name="processor",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator, text_formatter],
        max_iterations=3,
        debug=True,
    )

    # Create multi-agent workflow
    workflow = EnhancedMultiAgentV4(
        name="simple_to_react_flow",
        agents=[simple_agent, react_agent],
        execution_mode="sequential",
        debug=True,
    )

    # Test execution
    result = workflow.run(
        "First, prepare a calculation task: 'Calculate 25 * 18'. "
        "Then use the calculator to solve it."
    )

    assert result is not None
    assert "450" in str(result)  # 25 * 18 = 450


def test_parallel_execution():
    """Test parallel execution of multiple agents."""
    # Create multiple SimpleAgentV3 instances
    analyzer1 = SimpleAgentV3(
        name="analyzer1",
        engine=AugLLMConfig(temperature=0.1),
        tools=[data_analyzer],
        debug=True,
    )

    analyzer2 = SimpleAgentV3(
        name="analyzer2",
        engine=AugLLMConfig(temperature=0.1),
        tools=[text_formatter],
        debug=True,
    )

    analyzer3 = SimpleAgentV3(
        name="analyzer3", engine=AugLLMConfig(temperature=0.1), debug=True
    )

    # Create parallel workflow
    workflow = EnhancedMultiAgentV4(
        name="parallel_analysis",
        agents=[analyzer1, analyzer2, analyzer3],
        execution_mode="parallel",
        debug=True,
    )

    # Test execution
    result = workflow.run("Analyze this text in multiple ways")

    assert result is not None


def test_structured_output_flow():
    """Test flow with structured output across agents."""
    # Create planning agent with structured output
    planner = SimpleAgentV3(
        name="planner",
        engine=AugLLMConfig(temperature=0.1, structured_output_model=TaskPlan),
        debug=True,
    )

    # Create execution agent with tools
    executor = ReactAgentV3(
        name="executor",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator, text_formatter, data_analyzer],
        max_iterations=4,
        debug=True,
    )

    # Create reporter with structured output
    reporter = SimpleAgentV3(
        name="reporter",
        engine=AugLLMConfig(temperature=0.1, structured_output_model=TaskResult),
        debug=True,
    )

    # Create workflow: Planner → Executor → Reporter
    workflow = EnhancedMultiAgentV4(
        name="structured_workflow",
        agents=[planner, executor, reporter],
        execution_mode="sequential",
        debug=True,
    )

    # Test execution
    result = workflow.run(
        "Plan and execute: Calculate the total cost if items cost $15 each "
        "and we need 8 items, then format the result nicely"
    )

    assert result is not None


def test_react_to_simple_flow():
    """Test flow from ReactAgentV3 to SimpleAgentV3."""
    # Create ReactAgentV3 for data gathering
    data_gatherer = ReactAgentV3(
        name="gatherer",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator, data_analyzer],
        max_iterations=3,
        debug=True,
    )

    # Create SimpleAgentV3 for formatting
    formatter = SimpleAgentV3(
        name="formatter", engine=AugLLMConfig(temperature=0.1), debug=True
    )

    # Create workflow
    workflow = EnhancedMultiAgentV4(
        name="react_to_simple",
        agents=[data_gatherer, formatter],
        execution_mode="sequential",
        debug=True,
    )

    # Test execution
    result = workflow.run(
        "Calculate 12 * 12 and analyze the result, "
        "then format it as a professional report"
    )

    assert result is not None
    assert "144" in str(result)  # 12 * 12 = 144


def test_conditional_routing():
    """Test conditional routing between agents."""
    # Create classifier agent
    classifier = SimpleAgentV3(
        name="classifier", engine=AugLLMConfig(temperature=0.1), debug=True
    )

    # Create specialized processors
    math_processor = ReactAgentV3(
        name="math_processor",
        engine=AugLLMConfig(temperature=0.1),
        tools=[calculator],
        debug=True,
    )

    text_processor = SimpleAgentV3(
        name="text_processor",
        engine=AugLLMConfig(temperature=0.1),
        tools=[text_formatter],
        debug=True,
    )

    # Create conditional workflow
    workflow = EnhancedMultiAgentV4(
        name="conditional_flow",
        agents=[classifier, math_processor, text_processor],
        execution_mode="conditional",
        build_mode="manual",
        debug=True,
    )

    # Add conditional routing
    def route_condition(state):
        """Route based on classification."""
        messages = state.get("messages", [])
        if messages and "calculate" in str(messages[-1]).lower():
            return "math"
        return "text"

    # Build the graph with conditional edges
    workflow.add_edge(
        "classifier",
        route_condition,
        {"math": "math_processor", "text": "text_processor"},
    )

    workflow.build()

    # Test math routing
    result1 = workflow.run("Please calculate 15 * 20")
    assert "300" in str(result1)

    # Test text routing
    result2 = workflow.run("Format this text nicely")
    assert result2 is not None


if __name__ == "__main__":
    test_sequential_flow_simple_to_react()
    test_parallel_execution()
    test_structured_output_flow()
    test_react_to_simple_flow()
    test_conditional_routing()
