agents.planning_v2.base.planner.agent
=====================================

.. py:module:: agents.planning_v2.base.planner.agent

.. autoapi-nested-parse::

   Planner agent - just prompt template + structured output model.


   .. autolink-examples:: agents.planning_v2.base.planner.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning_v2.base.planner.agent.PlannerAgent


Module Contents
---------------

.. py:class:: PlannerAgent

   Bases: :py:obj:`haive.agents.simple.SimpleAgent`


   Planner agent = ChatPromptTemplate + TaskPlan structured output.


   .. autolink-examples:: PlannerAgent
      :collapse:

   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: prompt_template
      :type:  Any
      :value: None



