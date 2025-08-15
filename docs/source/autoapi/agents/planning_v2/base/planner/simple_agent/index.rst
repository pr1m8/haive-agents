agents.planning_v2.base.planner.simple_agent
============================================

.. py:module:: agents.planning_v2.base.planner.simple_agent

.. autoapi-nested-parse::

   Simple planner agent - just prompt + structured output.


   .. autolink-examples:: agents.planning_v2.base.planner.simple_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning_v2.base.planner.simple_agent.PlannerAgent


Module Contents
---------------

.. py:class:: PlannerAgent

   Bases: :py:obj:`haive.agents.simple.SimpleAgent`


   Planner agent - literally just prompt template + structured output model.


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



