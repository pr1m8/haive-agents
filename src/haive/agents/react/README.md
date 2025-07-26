# ReactAgent - Haive Framework

**Reasoning and Acting agents with iterative tool usage and problem solving**

## 🎯 Quick Start - Which Version to Use?

### ✅ **Default (Recommended)**: ReactAgent (Stable)

```python
from haive.agents.react import ReactAgent  # Stable, production-ready
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression))

# Create ReactAgent with tools
agent = ReactAgent(
    name="reasoning_agent",
    engine=AugLLMConfig(
        system_message="You are a step-by-step problem solver.",
        temperature=0.3
    ),
    tools=[calculator]
)

# Execute with reasoning loop
result = await agent.arun("What is 15 * 23 + 45? Show your work.")
print(result)
```

### 🚀 **Enhanced (Newer)**: ReactAgentV3

```python
from haive.agents.react import ReactAgentV3  # Latest with advanced features
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

class AnalysisResult(BaseModel):
    reasoning_steps: list[str] = Field(description="Steps taken to solve")
    final_answer: str = Field(description="Final answer")
    confidence: float = Field(description="Confidence score 0-1")

# Create enhanced ReactAgent with structured output
agent = ReactAgentV3(
    name="enhanced_reasoner",
    engine=AugLLMConfig(
        system_message="You are an expert analyst.",
        structured_output_model=AnalysisResult,
        temperature=0.2
    ),
    tools=[calculator, research_tool]
)

# Add hooks for monitoring
@agent.before_run
def log_start(context):
    print(f"🧠 Starting reasoning: {context.agent_name}")

@agent.after_run
def log_completion(context):
    print(f"✅ Reasoning completed: {context.agent_name}")

# Execute with full tracking
result = await agent.arun("Analyze the economic impact of AI adoption")
```

## 📋 Version Comparison

| Feature                | ReactAgent<br/>(Default Stable)             | ReactAgentV3<br/>(Enhanced Latest)            |
| ---------------------- | ------------------------------------------- | --------------------------------------------- |
| **Import**             | `from haive.agents.react import ReactAgent` | `from haive.agents.react import ReactAgentV3` |
| **Base Class**         | Extends SimpleAgent ✅                      | Enhanced Agent ✅                             |
| **ReAct Loop**         | ✅ Basic implementation                     | ✅ **Advanced with monitoring**               |
| **Structured Output**  | ✅ Basic support                            | ✅ **Full Pydantic integration**              |
| **Hooks System**       | ❌ Limited                                  | ✅ **Complete hook system**                   |
| **Tool Recompilation** | ✅ Auto                                     | ✅ **Real-time detection**                    |
| **Token Tracking**     | ❌ Basic                                    | ✅ **Comprehensive monitoring**               |
| **Meta-Agent Support** | ❌ None                                     | ✅ **MetaStateSchema ready**                  |
| **Status**             | **Current Default**                         | **Latest Features**                           |

The ReactAgent implements the ReAct (Reasoning and Acting) pattern, extending SimpleAgent with looping behavior for iterative reasoning and tool usage. **Default import gets you stable version, V3 available for latest features.**

## Overview

The ReactAgent follows the ReAct paradigm where agents:

1. **Reason** about the current situation
2. **Act** by using tools or generating responses
3. **Observe** the results
4. **Loop** back to reasoning until the task is complete

This creates a powerful reasoning loop that allows agents to break down complex tasks, use tools iteratively, and refine their responses based on observations.

## 🔧 Installation & Setup

```bash
# Install Haive framework
poetry install

# ReactAgent is included in haive-agents package
from haive.agents.react import ReactAgent, ReactAgentV3
```

## 🎯 Use Cases

### ReactAgent (Default Stable) - For Most Users

- **Multi-step problem solving**: Mathematical calculations, analysis
- **Research tasks**: Information gathering with tools
- **Production workflows**: Stable, tested reasoning patterns
- **Tool-heavy applications**: Multiple tool coordination

### ReactAgentV3 (Enhanced Latest) - For Advanced Users

- **Complex analysis workflows**: With structured output models
- **Monitoring & debugging**: Full hook system integration
- **Agent composition**: Meta-agent embedding support
- **Research & experimentation**: Latest features and patterns

## Key Components

- **ReactAgent**: Main agent class extending SimpleAgent
- **ReactAgentV3**: Enhanced agent with full feature set
- **ReAct Loop**: Graph modification for continuous reasoning
- **Tool Integration**: Seamless tool usage within the loop
- **State Management**: Maintains conversation and execution state
- **Hooks System**: Complete lifecycle monitoring (V3)

## Usage Examples

### Basic Usage

```python
from haive.agents.react import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    \"\"\"Calculate mathematical expressions.\"\"\"
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error in calculation"

# Create React agent
agent = ReactAgent(
    name="reasoning_agent",
    engine=AugLLMConfig(
        model="gpt-4",
        tools=[calculator],
        system_message="You are a helpful assistant that thinks step by step."
    )
)

# Run with reasoning loop
result = await agent.arun("What is 15 * 23 + 7?")
```

### Advanced Multi-Tool Usage

```python
from haive.agents.react import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Create agent with multiple tools
agent = ReactAgent(
    name="multi_tool_agent",
    engine=AugLLMConfig(
        model="gpt-4",
        tools=[search_tool, calculator_tool, file_tool],
        system_message=\"\"\"You are a research assistant. For each query:
        1. Think about what information you need
        2. Use appropriate tools to gather information
        3. Analyze the results
        4. Provide a comprehensive answer
        \"\"\"
    )
)

# Complex multi-step task
result = await agent.arun(
    "Find the current population of Tokyo and calculate the population density"
)
```

### Custom State Management

```python
from haive.core.schema import StateSchema
from pydantic import Field
from typing import List

class CustomReactState(StateSchema):
    reasoning_steps: List[str] = Field(default_factory=list)
    tool_usage_count: int = Field(default=0)
    current_objective: str = Field(default="")

agent = ReactAgent(
    name="custom_agent",
    engine=engine,
    state_schema=CustomReactState
)
```

## Architecture

### ReAct Loop Implementation

The React Agent modifies the SimpleAgent graph to create loops:

```python
def build_graph(self) -> BaseGraph:
    \"\"\"Build ReAct graph with proper looping.\"\"\"
    # Build base graph first
    graph = super().build_graph()

    # Modify connections for ReAct looping
    if self._needs_tool_node() and "tool_node" in graph.nodes:
        graph.remove_edge("tool_node", END)
        graph.add_edge("tool_node", "agent_node")  # Loop back

    return graph
```

### Execution Flow

1. **Agent Node**: Reasoning and decision making
2. **Tool Node**: Execute selected tools
3. **Parse Node**: Process tool results (if needed)
4. **Loop Back**: Return to agent node for continued reasoning
5. **End**: Complete when task is finished

## Testing

```bash
# Run React agent tests
poetry run pytest tests/react/ -v

# Run specific test
poetry run pytest tests/react/test_react_agent.py -v
```

## Best Practices

1. **Clear System Messages**: Provide explicit reasoning instructions
2. **Tool Design**: Create tools with clear descriptions and error handling
3. **Iteration Limits**: Set max_iterations to prevent infinite loops
4. **State Management**: Use appropriate state schemas for complex tasks
5. **Error Handling**: Implement robust error handling for tool failures

## Common Use Cases

- **Mathematical Problem Solving**: Break down complex calculations
- **Research and Analysis**: Gather information from multiple sources
- **Data Analysis**: Process and analyze data iteratively
- **Content Generation**: Create content with research and refinement
- **Code Development**: Write and test code iteratively

## API Reference

### ReactAgent

Main React agent class inheriting from SimpleAgent with ReAct loop capabilities.

For detailed API documentation, see the inline docstrings in the source code.

## See Also

- [SimpleAgent](../simple/) - Base agent implementation
- [Dynamic Supervisor](../dynamic_supervisor/) - Multi-agent coordination
- [Examples](../../../examples/react/) - Usage examples and patterns
- [Tests](../../../tests/react/) - Test implementations
