"""Planning Agents - Strategic task decomposition and execution patterns.

The planning module provides various planning agent implementations following different
architectural patterns for task decomposition, execution, and adaptation. These agents
excel at breaking down complex objectives into manageable steps and executing them
systematically.

## Key Planning Patterns

### 1. Plan & Execute (Sequential Planning)
- **Clean Plan Execute**: Simple, clean implementation following LangGraph patterns
- **Proper Plan Execute**: Full-featured with search integration
- **LangGraph Plan Execute**: Direct LangGraph compatibility

### 2. ReWOO (Evidence-Based Planning)
- **ReWOO Tree Agent V3**: Pure agent composition (recommended)
- **ReWOO Tree Agent V2**: Enhanced with parallel execution
- **Parallel ReWOO**: Optimized for concurrent evidence gathering

### 3. Multi-Agent Planning
- **Plan and Execute Multi**: Multi-agent orchestration for planning

## Quick Start

### Simple Plan & Execute
```python
from haive.agents.planning import create_simple_plan_execute
from haive.tools import calculator_tool, web_search_tool

# Create a planning agent with tools
agent = create_simple_plan_execute(
    tools=[calculator_tool, web_search_tool]
)

# Execute a complex task
result = agent.run("Research the GDP of France and calculate 15% of it")
```

### ReWOO Evidence-Based Planning
```python
from haive.agents.planning import create_rewoo_agent_with_tools_v3
from haive.tools import web_search_tool, document_reader

# Create ReWOO agent for research tasks
agent = create_rewoo_agent_with_tools_v3(
    name="researcher",
    tools=[web_search_tool, document_reader],
    model="gpt-4"
)

# Execute research with evidence gathering
result = agent.run("What are the main causes of climate change?")
```

### Advanced Plan & Execute with Search
```python
from haive.agents.planning import create_plan_execute_with_search

# Create planning agent with integrated search
agent = create_plan_execute_with_search(
    name="research_planner",
    planner_model="gpt-4",
    executor_model="gpt-4"
)

result = agent.run("Plan a sustainable city development project")
```

## Planning Patterns Guide

For comprehensive planning patterns and implementation details, see:
`PLANNING_AGENT_MEMORY_GUIDE.md`

## Version Guidance

### Recommended Implementations
- **Simple Tasks**: Use `create_simple_plan_execute()` - clean and straightforward
- **Research Tasks**: Use `create_rewoo_agent_with_tools_v3()` - evidence-based
- **Complex Tasks**: Use `create_proper_plan_execute()` - full-featured

### Pattern Selection
1. **Sequential Planning**: When tasks have clear dependencies
2. **Parallel Planning**: When tasks can be executed concurrently
3. **Evidence-Based**: When decisions require research and validation
4. **Adaptive Planning**: When plans need runtime adjustment

## Module Organization

### Core Implementations
- `clean_plan_execute.py` - Clean, simple Plan & Execute pattern
- `proper_plan_execute.py` - Full-featured with advanced routing
- `langgraph_plan_execute.py` - LangGraph-compatible implementation

### ReWOO Implementations
- `rewoo_tree_agent_v3.py` - Latest pure agent composition (recommended)
- `rewoo_tree_agent_v2.py` - Enhanced with task management
- `rewoo/` - ReWOO-specific components and models

### Supporting Components
- `models/` - Pydantic models for plans and steps
- `llm_compiler/` - LLM Compiler pattern implementation
- `plan_and_execute/` - Additional P&E components

## Integration with Other Agents

Planning agents work well with:
- **SimpleAgent**: For plan generation and replanning
- **ReactAgent**: For step execution with tools
- **MultiAgent**: For complex orchestration
- **RAG Agents**: For knowledge-augmented planning

## Best Practices

1. **Start Simple**: Use clean_plan_execute for straightforward tasks
2. **Add Tools Gradually**: Test with basic tools before adding complexity
3. **Monitor Execution**: Track step completion and handle failures
4. **Use Structured Output**: Leverage Pydantic models for plans
5. **Consider Parallelism**: Use ReWOO for parallelizable tasks

See PLANNING_AGENT_MEMORY_GUIDE.md for detailed patterns and examples.
"""

from haive.agents.planning.clean_plan_execute import (
    Act,
    Plan,
    PlanExecuteState,
    create_clean_plan_execute_agent,
    create_simple_plan_execute,
    route_after_replan,
    should_continue,
)
from haive.agents.planning.langgraph_plan_execute import Act as LanggraphAct
from haive.agents.planning.langgraph_plan_execute import Plan as LanggraphPlan
from haive.agents.planning.langgraph_plan_execute import (
    PlanExecuteState as LanggraphPlanExecuteState,
)
from haive.agents.planning.langgraph_plan_execute import (
    Response,
    create_langgraph_plan_execute,
    create_plan_execute_agent,
    route_replan,
)
from haive.agents.planning.langgraph_plan_execute import (
    should_continue as langgraph_should_continue,
)
from haive.agents.planning.plan_and_execute_multi import (
    PlanAndExecuteAgent,
    create_plan_execute_branches,
)
from haive.agents.planning.proper_plan_execute import (
    create_plan_execute_with_search,
    create_proper_plan_execute,
    process_executor_output,
    process_planner_output,
    process_replanner_output,
)
from haive.agents.planning.proper_plan_execute import (
    route_after_replan as proper_route_after_replan,
)
from haive.agents.planning.proper_plan_execute import (
    should_continue as proper_should_continue,
)
from haive.agents.planning.rewoo_tree_agent_v2 import (
    ParallelReWOOAgent,
    PlanTask,
    ReWOOExecutorAgent,
    ReWOOPlan,
    ReWOOPlannerAgent,
    ReWOOTreeAgent,
    ReWOOTreeState,
    TaskPriority,
    TaskStatus,
    TaskType,
    ToolAlias,
    create_rewoo_agent_with_tools,
)
from haive.agents.planning.rewoo_tree_agent_v3 import (
    ParallelReWOOAgent as ParallelReWOOAgentV3,
)
from haive.agents.planning.rewoo_tree_agent_v3 import ReWOOPlan as ReWOOPlanV3
from haive.agents.planning.rewoo_tree_agent_v3 import ReWOOTreeAgent as ReWOOTreeAgentV3
from haive.agents.planning.rewoo_tree_agent_v3 import ReWOOTreeState as ReWOOTreeStateV3
from haive.agents.planning.rewoo_tree_agent_v3 import TaskType as TaskTypeV3
from haive.agents.planning.rewoo_tree_agent_v3 import ToolAlias as ToolAliasV3
from haive.agents.planning.rewoo_tree_agent_v3 import (
    create_rewoo_agent_with_tools as create_rewoo_agent_with_tools_v3,
)

__all__ = [
    # Clean plan execute
    "Act",
    # Langgraph plan execute
    "LanggraphAct",
    "LanggraphPlan",
    "LanggraphPlanExecuteState",
    # ReWOO V2
    "ParallelReWOOAgent",
    # ReWOO V3
    "ParallelReWOOAgentV3",
    "Plan",
    # Plan and execute multi
    "PlanAndExecuteAgent",
    "PlanExecuteState",
    "PlanTask",
    "ReWOOExecutorAgent",
    "ReWOOPlan",
    "ReWOOPlanV3",
    "ReWOOPlannerAgent",
    "ReWOOTreeAgent",
    "ReWOOTreeAgentV3",
    "ReWOOTreeState",
    "ReWOOTreeStateV3",
    "Response",
    "TaskPriority",
    "TaskStatus",
    "TaskType",
    "TaskTypeV3",
    "ToolAlias",
    "ToolAliasV3",
    "create_clean_plan_execute_agent",
    "create_langgraph_plan_execute",
    "create_plan_execute_agent",
    "create_plan_execute_branches",
    # Proper plan execute
    "create_plan_execute_with_search",
    "create_proper_plan_execute",
    "create_rewoo_agent_with_tools",
    "create_rewoo_agent_with_tools_v3",
    "create_simple_plan_execute",
    "langgraph_should_continue",
    "process_executor_output",
    "process_planner_output",
    "process_replanner_output",
    "proper_route_after_replan",
    "proper_should_continue",
    "route_after_replan",
    "route_replan",
    "should_continue",
]
