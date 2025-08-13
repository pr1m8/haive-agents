
:py:mod:`agents.planning.p_and_e.multi_agent`
=============================================

.. py:module:: agents.planning.p_and_e.multi_agent

Plan and Execute Multi-Agent System using Configurable Base.

from typing import Any
This module demonstrates how to use the configurable multi-agent base
for building Plan and Execute workflows with branches.


.. autolink-examples:: agents.planning.p_and_e.multi_agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.p_and_e.multi_agent.PlanAndExecuteAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanAndExecuteAgent:

   .. graphviz::
      :align: center

      digraph inheritance_PlanAndExecuteAgent {
        node [shape=record];
        "PlanAndExecuteAgent" [label="PlanAndExecuteAgent"];
        "haive.agents.multi.archive.configurable_base.ConfigurableMultiAgent" -> "PlanAndExecuteAgent";
      }

.. autoclass:: agents.planning.p_and_e.multi_agent.PlanAndExecuteAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.planning.p_and_e.multi_agent.create_custom_branching_system
   agents.planning.p_and_e.multi_agent.create_custom_plan_execute_system
   agents.planning.p_and_e.multi_agent.create_plan_execute_system
   agents.planning.p_and_e.multi_agent.create_simple_sequential_system

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



.. rubric:: Related Links

.. autolink-examples:: agents.planning.p_and_e.multi_agent
   :collapse:
   
.. autolink-skip:: next
