agents.planning.p_and_e.multi_agent
===================================

.. py:module:: agents.planning.p_and_e.multi_agent

.. autoapi-nested-parse::

   Plan and Execute Multi-Agent System using Configurable Base.

   from typing import Any
   This module demonstrates how to use the configurable multi-agent base
   for building Plan and Execute workflows with branches.


   .. autolink-examples:: agents.planning.p_and_e.multi_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.p_and_e.multi_agent.logger


Classes
-------

.. autoapisummary::

   agents.planning.p_and_e.multi_agent.PlanAndExecuteAgent


Functions
---------

.. autoapisummary::

   agents.planning.p_and_e.multi_agent.create_custom_branching_system
   agents.planning.p_and_e.multi_agent.create_custom_plan_execute_system
   agents.planning.p_and_e.multi_agent.create_plan_execute_system
   agents.planning.p_and_e.multi_agent.create_simple_sequential_system


Module Contents
---------------

.. py:class:: PlanAndExecuteAgent(agents: list[Any], branches: list[haive.agents.multi.archive.configurable_base.AgentBranch] | None = None, state_schema=None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.archive.configurable_base.ConfigurableMultiAgent`


   Plan and Execute multi-agent using the configurable base.

   Initialize Plan and Execute multi-agent.

   :param agents: List of [planner, executor, replanner] agents
   :param branches: Optional custom branches (defaults to Plan & Execute workflow)
   :param state_schema: Optional state schema override
   :param \*\*kwargs: Additional arguments


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanAndExecuteAgent
      :collapse:

   .. py:method:: _prepare_execution_step(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> langgraph.types.Command

      Prepare the next execution step.


      .. autolink-examples:: _prepare_execution_step
         :collapse:


   .. py:method:: _prepare_replan_step(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> langgraph.types.Command

      Prepare for replanning.


      .. autolink-examples:: _prepare_replan_step
         :collapse:


   .. py:method:: _process_execution_result(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> langgraph.types.Command

      Process the execution result and update the plan.


      .. autolink-examples:: _process_execution_result
         :collapse:


   .. py:method:: _process_replan_decision(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> langgraph.types.Command

      Process the replanning decision.


      .. autolink-examples:: _process_replan_decision
         :collapse:


   .. py:method:: _route_after_execution(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> str

      Route after execution based on plan status.


      .. autolink-examples:: _route_after_execution
         :collapse:


   .. py:method:: _route_after_replan(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> str

      Route after replanning decision.


      .. autolink-examples:: _route_after_replan
         :collapse:


.. py:function:: create_custom_branching_system(agents: Any, branches)

   Create custom branching multi-agent system.


   .. autolink-examples:: create_custom_branching_system
      :collapse:

.. py:function:: create_custom_plan_execute_system(planner_agent, executor_agent, replanner_agent, custom_branches: list[haive.agents.multi.archive.configurable_base.AgentBranch])

   Create Plan and Execute system with custom branches.


   .. autolink-examples:: create_custom_plan_execute_system
      :collapse:

.. py:function:: create_plan_execute_system(planner_agent: Any, executor_agent: Any, replanner_agent: Any)

   Create Plan and Execute system with default workflow.


   .. autolink-examples:: create_plan_execute_system
      :collapse:

.. py:function:: create_simple_sequential_system(agents: Any)

   Create simple sequential multi-agent system.


   .. autolink-examples:: create_simple_sequential_system
      :collapse:

.. py:data:: logger

