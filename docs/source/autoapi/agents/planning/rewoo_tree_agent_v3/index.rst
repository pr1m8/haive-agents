
:py:mod:`agents.planning.rewoo_tree_agent_v3`
=============================================

.. py:module:: agents.planning.rewoo_tree_agent_v3

ReWOO Tree Agent V3 - Pure Agent Composition for Evidence-Based Planning.

This module provides the **recommended** implementation for research and evidence-based
planning tasks. It represents the latest and most elegant approach to the ReWOO
(Reasoning WithOut Observation) pattern using pure agent composition.

## Key Features

- **Pure Agent Composition**: No manual nodes - agents are automatically wrapped
- **Evidence-Based Planning**: Gather evidence before reasoning for better decisions
- **Parallel Execution**: Evidence collection can happen in parallel
- **Tool Aliasing**: Map abstract tool names to actual implementations
- **Type Safety**: Full Pydantic validation and type checking
- **Clean Architecture**: Leverages MultiAgent patterns for orchestration

## ReWOO Pattern

```
Problem Analysis
    ↓
Evidence Planning (what info needed?)
    ↓
Parallel Evidence Collection
    ↓
Reasoning with Evidence
    ↓
Final Answer
```

## Usage

### Basic Research Task
```python
from haive.agents.planning import create_rewoo_agent_with_tools_v3
from haive.tools import web_search_tool, calculator_tool

agent = create_rewoo_agent_with_tools_v3(
    name="researcher",
    tools=[web_search_tool, calculator_tool],
    model="gpt-4"
)

result = agent.run("What is the economic impact of renewable energy?")
```

### Advanced with Tool Aliases
```python
agent = ReWOOTreeAgent(
    name="advanced_researcher",
    available_tools=[web_search, db_query, api_call],
    tool_aliases={
        "research": ToolAlias(
            alias="research",
            actual_tool="web_search",
            force_choice=True
        ),
        "data": ToolAlias(
            alias="data",
            actual_tool="db_query",
            parameters={"limit": 100}
        )
    },
    max_parallelism=4
)
```

## When to Use

✅ **Use ReWOO V3 when**:
- You need evidence-based decision making
- Research tasks with multiple information sources
- Tasks benefit from parallel evidence gathering
- You want clean, maintainable code

❌ **Consider alternatives when**:
- Simple sequential tasks (use clean_plan_execute)
- No evidence gathering needed (use simple planning)
- Very simple single-step tasks (use ReactAgent directly)

## Advantages over V2

1. **Cleaner Code**: Pure agent composition, no manual node management
2. **Better Type Safety**: Proper Pydantic field initialization
3. **More Maintainable**: Follows framework patterns consistently
4. **Easier Testing**: Standard agent testing patterns apply

## Status: Recommended for Research Tasks

This is the preferred implementation for any task requiring evidence gathering
and research before making decisions.


.. autolink-examples:: agents.planning.rewoo_tree_agent_v3
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.rewoo_tree_agent_v3.ParallelReWOOAgent
   agents.planning.rewoo_tree_agent_v3.ReWOOPlan
   agents.planning.rewoo_tree_agent_v3.ReWOOTreeAgent
   agents.planning.rewoo_tree_agent_v3.ReWOOTreeState
   agents.planning.rewoo_tree_agent_v3.TaskType
   agents.planning.rewoo_tree_agent_v3.ToolAlias


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelReWOOAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelReWOOAgent {
        node [shape=record];
        "ParallelReWOOAgent" [label="ParallelReWOOAgent"];
        "ReWOOTreeAgent" -> "ParallelReWOOAgent";
      }

.. autoclass:: agents.planning.rewoo_tree_agent_v3.ParallelReWOOAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOPlan {
        node [shape=record];
        "ReWOOPlan" [label="ReWOOPlan"];
        "pydantic.BaseModel" -> "ReWOOPlan";
      }

.. autopydantic_model:: agents.planning.rewoo_tree_agent_v3.ReWOOPlan
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOTreeAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOTreeAgent {
        node [shape=record];
        "ReWOOTreeAgent" [label="ReWOOTreeAgent"];
        "haive.agents.multi.agent.MultiAgent" -> "ReWOOTreeAgent";
      }

.. autoclass:: agents.planning.rewoo_tree_agent_v3.ReWOOTreeAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOTreeState:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOTreeState {
        node [shape=record];
        "ReWOOTreeState" [label="ReWOOTreeState"];
        "haive.core.schema.prebuilt.multi_agent_state.MultiAgentState" -> "ReWOOTreeState";
      }

.. autoclass:: agents.planning.rewoo_tree_agent_v3.ReWOOTreeState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaskType:

   .. graphviz::
      :align: center

      digraph inheritance_TaskType {
        node [shape=record];
        "TaskType" [label="TaskType"];
        "str" -> "TaskType";
        "enum.Enum" -> "TaskType";
      }

.. autoclass:: agents.planning.rewoo_tree_agent_v3.TaskType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskType** is an Enum defined in ``agents.planning.rewoo_tree_agent_v3``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ToolAlias:

   .. graphviz::
      :align: center

      digraph inheritance_ToolAlias {
        node [shape=record];
        "ToolAlias" [label="ToolAlias"];
        "pydantic.BaseModel" -> "ToolAlias";
      }

.. autopydantic_model:: agents.planning.rewoo_tree_agent_v3.ToolAlias
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   agents.planning.rewoo_tree_agent_v3.create_rewoo_agent_with_tools

.. py:function:: create_rewoo_agent_with_tools(tools: list[langchain_core.tools.BaseTool], tool_aliases: dict[str, str] | None = None, max_parallelism: int = 4) -> ReWOOTreeAgent

   Factory function to create ReWOO agent with tools.


   .. autolink-examples:: create_rewoo_agent_with_tools
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.rewoo_tree_agent_v3
   :collapse:
   
.. autolink-skip:: next
