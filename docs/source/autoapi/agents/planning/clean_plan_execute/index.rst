
:py:mod:`agents.planning.clean_plan_execute`
============================================

.. py:module:: agents.planning.clean_plan_execute

Clean Plan and Execute Implementation following LangGraph patterns.

This module provides the **recommended** implementation for simple sequential planning tasks.
It follows the standard LangGraph Plan and Execute pattern with minimal complexity and
clear, understandable routing logic.

## Key Features

- **Simple Models**: Clean Plan and Act models without overcomplication
- **MultiAgentBase**: Leverages multi-agent orchestration for clean separation
- **React Agent**: Uses ReactAgent for tool-based step execution
- **Simple Agent**: Uses SimpleAgent for planning and replanning
- **Clean Routing**: Straightforward routing logic with clear decision points

## Architecture

```
Planner (SimpleAgent)
    ↓
Executor (ReactAgent) ←─┐
    ↓                   │
Route Decision ─────────┘
    ↓
Replanner (SimpleAgent)
    ↓
END or back to Executor
```

## Usage

### Basic Example
```python
from haive.agents.planning import create_simple_plan_execute
from haive.tools import calculator_tool

agent = create_simple_plan_execute(tools=[calculator_tool])
result = agent.run("Calculate the compound interest on $1000 at 5% for 10 years")
```

### Advanced Example
```python
from haive.agents.planning import create_clean_plan_execute_agent

agent = create_clean_plan_execute_agent(
    name="MyPlanner",
    planner_model="gpt-4",
    executor_model="gpt-3.5-turbo",
    tools=[web_search, calculator, file_reader]
)

result = agent.run("Research tech stocks and calculate potential returns")
```

## When to Use

✅ **Use this implementation when**:
- You need simple, sequential planning
- Tasks have clear step-by-step execution
- You want minimal complexity
- You're starting with planning agents

❌ **Consider alternatives when**:
- You need parallel execution (use ReWOO)
- You need complex replanning logic (use proper_plan_execute)
- You need DAG-based planning (use llm_compiler)

## Status: Recommended for Simple Planning Tasks

This is the go-to implementation for straightforward planning needs.


.. autolink-examples:: agents.planning.clean_plan_execute
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.clean_plan_execute.Act
   agents.planning.clean_plan_execute.Plan
   agents.planning.clean_plan_execute.PlanExecuteState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Act:

   .. graphviz::
      :align: center

      digraph inheritance_Act {
        node [shape=record];
        "Act" [label="Act"];
        "pydantic.BaseModel" -> "Act";
      }

.. autopydantic_model:: agents.planning.clean_plan_execute.Act
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

   Inheritance diagram for Plan:

   .. graphviz::
      :align: center

      digraph inheritance_Plan {
        node [shape=record];
        "Plan" [label="Plan"];
        "pydantic.BaseModel" -> "Plan";
      }

.. autopydantic_model:: agents.planning.clean_plan_execute.Plan
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

   Inheritance diagram for PlanExecuteState:

   .. graphviz::
      :align: center

      digraph inheritance_PlanExecuteState {
        node [shape=record];
        "PlanExecuteState" [label="PlanExecuteState"];
        "haive.core.schema.prebuilt.messages.messages_state.MessagesState" -> "PlanExecuteState";
      }

.. autoclass:: agents.planning.clean_plan_execute.PlanExecuteState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.planning.clean_plan_execute.create_clean_plan_execute_agent
   agents.planning.clean_plan_execute.create_simple_plan_execute
   agents.planning.clean_plan_execute.route_after_replan
   agents.planning.clean_plan_execute.should_continue

.. py:function:: create_clean_plan_execute_agent(name: str = 'PlanExecute', planner_model: str = 'gpt-4o-mini', executor_model: str = 'gpt-4o-mini', tools: list | None = None) -> haive.agents.multi.archive.enhanced_base.MultiAgentBase

   Create a clean Plan and Execute agent following LangGraph patterns.

   :param name: Name for the agent
   :param planner_model: Model for planning
   :param executor_model: Model for execution
   :param tools: Tools available to executor

   :returns: Clean Plan and Execute system
   :rtype: MultiAgentBase


   .. autolink-examples:: create_clean_plan_execute_agent
      :collapse:

.. py:function:: create_simple_plan_execute(tools: list | None = None) -> haive.agents.multi.archive.enhanced_base.MultiAgentBase

   Create a simple Plan and Execute agent with default settings.


   .. autolink-examples:: create_simple_plan_execute
      :collapse:

.. py:function:: route_after_replan(state: PlanExecuteState) -> str

   Route after replanning decision.


   .. autolink-examples:: route_after_replan
      :collapse:

.. py:function:: should_continue(state: PlanExecuteState) -> str

   Decide whether to continue executing or move to replanning.


   .. autolink-examples:: should_continue
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.clean_plan_execute
   :collapse:
   
.. autolink-skip:: next
