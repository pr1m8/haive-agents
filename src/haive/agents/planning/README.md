# Planning Agents Module

**Version**: 1.0  
**Status**: Active Development  
**Purpose**: Strategic task decomposition and execution patterns

## Overview

The planning module provides sophisticated agent implementations for breaking down complex objectives into executable steps. These agents excel at:

- **Task Decomposition**: Breaking complex goals into manageable steps
- **Dependency Management**: Handling task dependencies and ordering
- **Adaptive Execution**: Adjusting plans based on intermediate results
- **Evidence-Based Reasoning**: Gathering and using evidence for decisions
- **Parallel Execution**: Running independent tasks concurrently

## Planning Patterns

### 1. Sequential Planning (Plan & Execute)

Linear step-by-step execution with replanning capabilities.

```python
from haive.agents.planning import create_simple_plan_execute

# Create a sequential planner
agent = create_simple_plan_execute(tools=[web_search, calculator])
result = agent.run("Research and calculate market statistics")
```

**Best for**: Tasks with clear sequential dependencies

### 2. Evidence-Based Planning (ReWOO)

Gather evidence first, then reason with collected information.

```python
from haive.agents.planning import create_rewoo_agent_with_tools_v3

# Create evidence-based planner
agent = create_rewoo_agent_with_tools_v3(
    tools=[search_tool, analyze_tool],
    model="gpt-4"
)
result = agent.run("What are the environmental impacts of EVs?")
```

**Best for**: Research tasks requiring validation and evidence

### 3. DAG Planning (LLM Compiler Pattern)

Directed Acyclic Graph planning with parallel execution.

```python
from haive.agents.planning.llm_compiler import create_llm_compiler_agent

# Create DAG planner for parallel tasks
agent = create_llm_compiler_agent(
    tools=[api_tool, db_tool, calc_tool]
)
result = agent.run("Analyze data from multiple sources")
```

**Best for**: Tasks with parallelizable subtasks

### 4. Adaptive Planning (Dynamic Replanning)

Plans that adapt based on execution results.

```python
from haive.agents.planning import create_proper_plan_execute

# Create adaptive planner
agent = create_proper_plan_execute(
    tools=[search_tool, api_tool],
    allow_replanning=True
)
result = agent.run("Find and book the best flight options")
```

**Best for**: Tasks where requirements may change during execution

## Key Components

### Core Implementations

#### clean_plan_execute.py

- **Purpose**: Simple, clean Plan & Execute following LangGraph patterns
- **Features**: Minimal complexity, clear routing, easy to understand
- **Status**: ✅ Recommended for simple sequential tasks

#### proper_plan_execute.py

- **Purpose**: Full-featured Plan & Execute with advanced capabilities
- **Features**: Search integration, complex routing, state management
- **Status**: ✅ Recommended for complex planning tasks

#### rewoo_tree_agent_v3.py

- **Purpose**: Evidence-based planning with pure agent composition
- **Features**: Parallel evidence gathering, tree-based reasoning
- **Status**: ✅ Recommended for research tasks

### Submodules

- **plan_and_execute/**: Core P&E components (models, prompts, state)
- **rewoo/**: ReWOO-specific implementations and utilities
- **models/**: Shared Pydantic models for plans and steps
- **llm_compiler/**: DAG-based planning with parallelism

## Installation

This module is part of the `haive-agents` package:

```bash
pip install haive-agents
```

## Usage Examples

### Example 1: Simple Planning Task

```python
from haive.agents.planning import create_simple_plan_execute
from haive.tools import calculator_tool, web_search_tool

# Create agent
agent = create_simple_plan_execute(
    tools=[calculator_tool, web_search_tool]
)

# Execute task
result = agent.run(
    "Find the population of Japan and calculate how many "
    "people that would be per square kilometer"
)

print(result)
# Output includes:
# - Plan: [Search population, Search area, Calculate density]
# - Execution: Step-by-step results
# - Final answer: ~340 people per square km
```

### Example 2: Research with Evidence

```python
from haive.agents.planning import create_rewoo_agent_with_tools_v3
from haive.tools import web_search_tool, document_analyzer

# Create research agent
researcher = create_rewoo_agent_with_tools_v3(
    name="researcher",
    tools=[web_search_tool, document_analyzer],
    model="gpt-4"
)

# Execute research task
result = researcher.run(
    "What are the main arguments for and against "
    "universal basic income? Provide evidence."
)

# Result includes evidence references and reasoning
```

### Example 3: Complex Multi-Step Planning

```python
from haive.agents.planning import create_proper_plan_execute
from haive.tools import api_tool, db_tool, email_tool

# Create sophisticated planner
planner = create_proper_plan_execute(
    name="project_planner",
    tools=[api_tool, db_tool, email_tool],
    planner_model="gpt-4",
    executor_model="gpt-4",
    max_replanning_steps=3
)

# Execute complex task
result = planner.run(
    "Analyze last quarter's sales data, identify top performers, "
    "and send personalized congratulation emails"
)
```

## State Management

Planning agents use specialized state schemas:

- **PlanExecuteState**: Tracks plan, completed steps, and results
- **ReWOOTreeState**: Manages evidence collection and reasoning
- **LLMCompilerState**: Handles DAG execution and parallelism

All states extend from base schemas with proper validation.

## Best Practices

1. **Choose the Right Pattern**
   - Sequential for simple linear tasks
   - ReWOO for research and evidence-based decisions
   - DAG for parallelizable subtasks

2. **Tool Selection**
   - Provide only necessary tools to reduce complexity
   - Ensure tools have clear descriptions
   - Test tools independently first

3. **Error Handling**
   - Planning agents include retry logic
   - Failed steps trigger replanning
   - Set reasonable max_steps limits

4. **Performance**
   - Use simpler models for planning (gpt-3.5-turbo)
   - Use stronger models for execution (gpt-4)
   - Enable parallelism where possible

## Advanced Topics

See [PLANNING_AGENT_MEMORY_GUIDE.md](./PLANNING_AGENT_MEMORY_GUIDE.md) for:

- Detailed pattern explanations
- State schema design
- Custom planning agent creation
- Testing strategies
- Performance optimization

## API Reference

For detailed API documentation, see the [API Reference](../../../docs/source/api/planning/index.rst).

## See Also

- [Multi-Agent Module](../multi/): For agent orchestration
- [React Agents](../react/): For tool-using execution agents
- [Simple Agents](../simple/): For basic planning agents
- [RAG Agents](../rag/): For knowledge-augmented planning
