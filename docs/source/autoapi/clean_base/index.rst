clean_base
==========

.. py:module:: clean_base

.. autoapi-nested-parse::

   Clean multi-agent base following proper Agent patterns.


   .. autolink-examples:: clean_base
      :collapse:


Classes
-------

.. autoapisummary::

   clean_base.CleanMultiAgent


Module Contents
---------------

.. py:class:: CleanMultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Clean multi-agent following base Agent patterns.

   This properly follows the base Agent class patterns:
   - Uses agents field similar to engines field
   - Lets base agent handle schema generation
   - Implements setup_agent() and build_graph() properly


   .. autolink-examples:: CleanMultiAgent
      :collapse:

   .. py:method:: _build_sequential_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build sequential execution edges.


      .. autolink-examples:: _build_sequential_edges
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph using AgentNodeV3 properly.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: normalize_agents() -> CleanMultiAgent

      Normalize agents similar to how base Agent normalizes engines.


      .. autolink-examples:: normalize_agents
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup hook - let base agent handle schema generation.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: agents
      :type:  list[haive.agents.base.agent.Agent] | dict[str, haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: execution_mode
      :type:  str
      :value: None



