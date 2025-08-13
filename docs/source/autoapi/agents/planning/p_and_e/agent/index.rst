
:py:mod:`agents.planning.p_and_e.agent`
=======================================

.. py:module:: agents.planning.p_and_e.agent


Classes
-------

.. autoapisummary::

   agents.planning.p_and_e.agent.PlanAndExecuteAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlanAndExecuteAgent:

   .. graphviz::
      :align: center

      digraph inheritance_PlanAndExecuteAgent {
        node [shape=record];
        "PlanAndExecuteAgent" [label="PlanAndExecuteAgent"];
        "haive.agents.base.agent.Agent" -> "PlanAndExecuteAgent";
      }

.. autoclass:: agents.planning.p_and_e.agent.PlanAndExecuteAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.planning.p_and_e.agent.check_plan_complete
   agents.planning.p_and_e.agent.route_after_evaluation

.. py:function:: check_plan_complete(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> str

   Check if plan execution is complete or needs more steps.


   .. autolink-examples:: check_plan_complete
      :collapse:

.. py:function:: route_after_evaluation(state: haive.agents.planning.p_and_e.state.PlanExecuteState) -> str

   Route based on evaluation decision.


   .. autolink-examples:: route_after_evaluation
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.p_and_e.agent
   :collapse:
   
.. autolink-skip:: next
