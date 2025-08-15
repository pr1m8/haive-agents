agents.planning.proper_plan_execute
===================================

.. py:module:: agents.planning.proper_plan_execute

.. autoapi-nested-parse::

   Proper Plan & Execute Implementation - Full-Featured Planning with Advanced Routing.

   This module provides the **advanced** implementation for complex planning tasks that
   require sophisticated routing, state management, and search integration. It builds
   on the clean implementation with additional capabilities.

   ## Key Features

   - **Advanced State Management**: Rich state tracking with PlanExecuteState
   - **Search Integration**: Built-in web search capabilities via duckduckgo
   - **Complex Routing**: Sophisticated decision logic for replanning
   - **Execution Tracking**: Detailed tracking of step execution and results
   - **Reusable Components**: Leverages existing p_and_e models and prompts

   ## Architecture

   ```
   Planner (SimpleAgent with Plan model)
       ↓
   Executor (ReactAgent with tools + ExecutionResult)
       ↓
   Routing Decision (should_continue)
       ├──→ Continue: back to Executor
       ├──→ Replan: to Replanner
       └──→ End: final answer
            ↓
   Replanner (SimpleAgent with Act model)
       ↓
   Routing Decision (route_after_replan)
       ├──→ Execute: back to Executor
       └──→ End: final answer
   ```

   ## Usage

   ### With Search Integration
   ```python
   from haive.agents.planning import create_plan_execute_with_search

   agent = create_plan_execute_with_search(
       name="research_planner",
       planner_model="gpt-4",
       executor_model="gpt-3.5-turbo"
   )

   result = agent.run(
       "Research the latest AI developments and create a summary report"
   )
   ```

   ### Custom Configuration
   ```python
   from haive.agents.planning import create_proper_plan_execute
   from haive.tools import custom_api_tool, database_tool

   agent = create_proper_plan_execute(
       name="data_planner",
       planner_model="gpt-4",
       executor_model="gpt-4",
       tools=[custom_api_tool, database_tool],
       max_replanning_steps=5,
       allow_parallel_execution=True
   )

   result = agent.run("Analyze customer data and generate insights")
   ```

   ## Advanced Features

   ### State Processing Functions
   - `process_planner_output`: Extracts and validates plans
   - `process_executor_output`: Tracks execution results
   - `process_replanner_output`: Handles replanning decisions

   ### Routing Logic
   - `should_continue`: Determines next step after execution
   - `route_after_replan`: Routes after replanning decision

   ## When to Use

   ✅ **Use this implementation when**:
   - You need sophisticated planning with search
   - Complex routing logic is required
   - Detailed execution tracking is important
   - You need production-ready error handling

   ❌ **Consider alternatives when**:
   - Simple sequential planning suffices (use clean_plan_execute)
   - You need evidence-based planning (use ReWOO)
   - Tasks are very straightforward (use ReactAgent directly)

   ## Status: Recommended for Complex Planning Tasks

   This is the go-to implementation for production systems requiring robust
   planning capabilities with search integration and advanced state management.


   .. autolink-examples:: agents.planning.proper_plan_execute
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.proper_plan_execute.agent


Functions
---------

.. autoapisummary::

   agents.planning.proper_plan_execute.create_plan_execute_with_search
   agents.planning.proper_plan_execute.create_proper_plan_execute
   agents.planning.proper_plan_execute.process_executor_output
   agents.planning.proper_plan_execute.process_planner_output
   agents.planning.proper_plan_execute.process_replanner_output
   agents.planning.proper_plan_execute.route_after_replan
   agents.planning.proper_plan_execute.should_continue


Module Contents
---------------

.. py:function:: create_plan_execute_with_search(tools: list | None = None) -> haive.agents.multi.archive.enhanced_base.MultiAgentBase

   Create Plan & Execute agent with search tools.


   .. autolink-examples:: create_plan_execute_with_search
      :collapse:

.. py:function:: create_proper_plan_execute(name: str = 'ProperPlanExecute', planner_model: str = 'gpt-4o-mini', executor_model: str = 'gpt-4o-mini', replanner_model: str = 'gpt-4o-mini', tools: list | None = None) -> haive.agents.multi.archive.enhanced_base.MultiAgentBase

   Create proper Plan & Execute agent using existing p_and_e components.

   :param name: Name for the agent system
   :param planner_model: Model for planning agent
   :param executor_model: Model for execution agent
   :param replanner_model: Model for replanning agent
   :param tools: Tools available to executor

   :returns: Complete Plan & Execute system
   :rtype: MultiAgentBase


   .. autolink-examples:: create_proper_plan_execute
      :collapse:

.. py:function:: process_executor_output(state: haive.agents.planning.p_and_e.state.PlanExecuteState, executor_result) -> dict

   Process executor output and update state.


   .. autolink-examples:: process_executor_output
      :collapse:

.. py:function:: process_planner_output(state: haive.agents.planning.p_and_e.state.PlanExecuteState, planner_result) -> dict

   Process planner output and update state.


   .. autolink-examples:: process_planner_output
      :collapse:

.. py:function:: process_replanner_output(state: haive.agents.planning.p_and_e.state.PlanExecuteState, replanner_result) -> dict

   Process replanner output and update state.


   .. autolink-examples:: process_replanner_output
      :collapse:

.. py:function:: route_after_replan(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> str

   Route after replanning: continue or end.


   .. autolink-examples:: route_after_replan
      :collapse:

.. py:function:: should_continue(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> str

   Route after execution: continue, replan, or end.


   .. autolink-examples:: should_continue
      :collapse:

.. py:data:: agent

