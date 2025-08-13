
:py:mod:`agents.planning.base.agents`
=====================================

.. py:module:: agents.planning.base.agents

Base Planning Agents - Foundational agents for planning workflows.

This module provides the core planning agents that serve as building blocks
for more complex planning systems.


.. autolink-examples:: agents.planning.base.agents
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.base.agents.BasePlannerAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BasePlannerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BasePlannerAgent {
        node [shape=record];
        "BasePlannerAgent" [label="BasePlannerAgent"];
        "SimpleAgentV3" -> "BasePlannerAgent";
      }

.. autoclass:: agents.planning.base.agents.BasePlannerAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.planning.base.agents.create_base_planner
   agents.planning.base.agents.create_conversation_summary_planner

.. py:function:: create_base_planner(name: str = 'base_planner', model: str = 'gpt-4o-mini', temperature: float = 0.3, structured_output_model=None) -> BasePlannerAgent

   Create a base planner agent with default configuration.

   :param name: Name for the planner agent
   :param model: LLM model to use for planning
   :param temperature: Sampling temperature for planning (lower = more focused)
   :param structured_output_model: Custom output model (defaults to BasePlan)

   :returns: Configured planner ready for use
   :rtype: BasePlannerAgent

   .. rubric:: Examples

   Basic planner:

       planner = create_base_planner()

   Custom planner:

       planner = create_base_planner(
           name="strategic_planner",
           model="gpt-4",
           temperature=0.2
       )


   .. autolink-examples:: create_base_planner
      :collapse:

.. py:function:: create_conversation_summary_planner(name: str = 'conversation_planner') -> BasePlannerAgent

   Create a specialized planner for conversation summary tasks.

   This creates a planner specifically tuned for analyzing conversations
   and creating detailed summaries with strategic planning approach.

   :returns: Planner optimized for conversation analysis
   :rtype: BasePlannerAgent


   .. autolink-examples:: create_conversation_summary_planner
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.planning.base.agents
   :collapse:
   
.. autolink-skip:: next
