agents.planning.clean_plan_execute
==================================

.. py:module:: agents.planning.clean_plan_execute

.. autoapi-nested-parse::

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


Attributes
----------

.. autoapisummary::

   agents.planning.clean_plan_execute.agent


Classes
-------

.. autoapisummary::

   agents.planning.clean_plan_execute.Act
   agents.planning.clean_plan_execute.Plan
   agents.planning.clean_plan_execute.PlanExecuteState


Functions
---------

.. autoapisummary::

   agents.planning.clean_plan_execute.create_clean_plan_execute_agent
   agents.planning.clean_plan_execute.create_simple_plan_execute
   agents.planning.clean_plan_execute.route_after_replan
   agents.planning.clean_plan_execute.should_continue


Module Contents
---------------

.. py:class:: Act(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Action to take - either respond or replan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Act
      :collapse:

   .. py:attribute:: action
      :type:  Literal['response', 'continue']
      :value: None



   .. py:attribute:: response
      :type:  str
      :value: None



.. py:class:: Plan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A simple plan with list of steps.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Plan
      :collapse:

   .. py:attribute:: steps
      :type:  list[str]
      :value: None



.. py:class:: PlanExecuteState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages.messages_state.MessagesState`


   Clean state schema for Plan and Execute.


   .. autolink-examples:: PlanExecuteState
      :collapse:

   .. py:attribute:: past_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: plan
      :type:  list[str]
      :value: None



   .. py:attribute:: response
      :type:  str
      :value: None



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

.. py:data:: agent

