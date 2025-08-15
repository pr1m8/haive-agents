proper_base
===========

.. py:module:: proper_base

.. autoapi-nested-parse::

   Proper multi-agent base following exact engines dict pattern.


   .. autolink-examples:: proper_base
      :collapse:


Classes
-------

.. autoapisummary::

   proper_base.ProperMultiAgent


Module Contents
---------------

.. py:class:: ProperMultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Multi-agent following exact engines dict pattern.

   Emulates the engines/engine pattern:
   - agents: Dict[str, Agent] = Field(default_factory=dict)
   - agent: Agent | None = Field(default=None)
   - Same normalization logic as engines


   .. autolink-examples:: ProperMultiAgent
      :collapse:

   .. py:method:: _build_branch_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build branching execution edges.


      .. autolink-examples:: _build_branch_edges
         :collapse:


   .. py:method:: _build_conditional_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build conditional execution edges.


      .. autolink-examples:: _build_conditional_edges
         :collapse:


   .. py:method:: _build_parallel_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build parallel execution edges.


      .. autolink-examples:: _build_parallel_edges
         :collapse:


   .. py:method:: _build_sequential_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build sequential execution edges.


      .. autolink-examples:: _build_sequential_edges
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph using AgentNodeV3 properly.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: normalize_agents_and_engines(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Normalize agents dict exactly like engines normalization.


      .. autolink-examples:: normalize_agents_and_engines
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup hook - configure multi-agent state schema using composition.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: agent
      :type:  haive.agents.base.agent.Agent | None
      :value: None



   .. py:attribute:: agents
      :type:  dict[str, haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: branch_condition
      :type:  str | None
      :value: None



   .. py:attribute:: execution_mode
      :type:  str
      :value: None



   .. py:attribute:: parallel_wait_for_all
      :type:  bool
      :value: None



