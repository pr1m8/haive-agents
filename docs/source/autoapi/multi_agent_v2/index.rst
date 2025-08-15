multi_agent_v2
==============

.. py:module:: multi_agent_v2

.. autoapi-nested-parse::

   Multi-agent V2 with proper state management and rebuilding support.

   This module provides a rebuilt MultiAgent that uses MultiAgentState without
   schema flattening, maintaining type safety and hierarchical access.


   .. autolink-examples:: multi_agent_v2
      :collapse:


Attributes
----------

.. autoapisummary::

   multi_agent_v2.logger


Classes
-------

.. autoapisummary::

   multi_agent_v2.ExecutionMode
   multi_agent_v2.MultiAgentV2


Module Contents
---------------

.. py:class:: ExecutionMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Execution modes for multi-agent systems.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionMode
      :collapse:

   .. py:attribute:: CONDITIONAL
      :value: 'conditional'



   .. py:attribute:: HIERARCHICAL
      :value: 'hierarchical'



   .. py:attribute:: PARALLEL
      :value: 'parallel'



   .. py:attribute:: SEQUENCE
      :value: 'sequence'



.. py:class:: MultiAgentV2

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Rebuilt multi-agent system using proper state management.

   Key improvements:
   - Uses MultiAgentState without schema flattening
   - Each agent maintains its own schema
   - Supports rebuilding with class methods
   - Proper hierarchical state access


   .. autolink-examples:: MultiAgentV2
      :collapse:

   .. py:method:: _aggregate_results(state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> dict[str, Any]

      Aggregate results from parallel execution.


      .. autolink-examples:: _aggregate_results
         :collapse:


   .. py:method:: _build_conditional_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Build conditional execution graph.


      .. autolink-examples:: _build_conditional_graph
         :collapse:


   .. py:method:: _build_hierarchical_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Build hierarchical execution graph.


      .. autolink-examples:: _build_hierarchical_graph
         :collapse:


   .. py:method:: _build_parallel_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Build parallel execution graph.


      .. autolink-examples:: _build_parallel_graph
         :collapse:


   .. py:method:: _build_sequence_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Build sequential execution graph.


      .. autolink-examples:: _build_sequence_graph
         :collapse:


   .. py:method:: _coordinate_parallel(state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> dict[str, Any]

      Coordinate parallel execution.


      .. autolink-examples:: _coordinate_parallel
         :collapse:


   .. py:method:: _route_conditionally(state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> str

      Route based on condition.


      .. autolink-examples:: _route_conditionally
         :collapse:


   .. py:method:: add_agent(agent: haive.agents.base.agent.Agent, rebuild: bool = True) -> MultiAgentV2

      Add an agent and optionally rebuild.

      :param agent: Agent to add
      :param rebuild: Whether to rebuild the graph

      :returns: Self or new instance if rebuilt


      .. autolink-examples:: add_agent
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the multi-agent graph based on execution mode.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: from_agents(agents: list[haive.agents.base.agent.Agent] | dict[str, haive.agents.base.agent.Agent], name: str | None = None, execution_mode: ExecutionMode = ExecutionMode.SEQUENCE, **kwargs) -> MultiAgentV2
      :classmethod:


      Create MultiAgent from a list or dict of agents.

      :param agents: List or dict of agents to coordinate
      :param name: Optional name for the multi-agent
      :param execution_mode: How to execute agents
      :param \*\*kwargs: Additional configuration

      :returns: MultiAgentV2 instance


      .. autolink-examples:: from_agents
         :collapse:


   .. py:method:: from_config(config: dict[str, Any], agents: list[haive.agents.base.agent.Agent] | dict[str, haive.agents.base.agent.Agent] | None = None) -> MultiAgentV2
      :classmethod:


      Create MultiAgent from configuration dict.

      :param config: Configuration dictionary
      :param agents: Optional agents (overrides config)

      :returns: MultiAgentV2 instance


      .. autolink-examples:: from_config
         :collapse:


   .. py:method:: get_agent(agent_name: str) -> haive.agents.base.agent.Agent | None

      Get an agent by name.


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: rebuild_with_agents(original: MultiAgentV2, new_agents: list[haive.agents.base.agent.Agent] | dict[str, haive.agents.base.agent.Agent], **kwargs) -> MultiAgentV2
      :classmethod:


      Rebuild MultiAgent with new agents.

      :param original: Original MultiAgent to rebuild from
      :param new_agents: New agents to use
      :param \*\*kwargs: Additional config overrides

      :returns: New MultiAgentV2 instance


      .. autolink-examples:: rebuild_with_agents
         :collapse:


   .. py:method:: remove_agent(agent_name: str, rebuild: bool = True) -> MultiAgentV2

      Remove an agent and optionally rebuild.

      :param agent_name: Name of agent to remove
      :param rebuild: Whether to rebuild the graph

      :returns: Self or new instance if rebuilt


      .. autolink-examples:: remove_agent
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup hook - MultiAgent uses MultiAgentState by default.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: setup_multi_agent() -> MultiAgentV2

      Set up the multi-agent system.


      .. autolink-examples:: setup_multi_agent
         :collapse:


   .. py:method:: validate_agents(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Ensure agents are provided.


      .. autolink-examples:: validate_agents
         :collapse:


   .. py:attribute:: agents
      :type:  list[haive.agents.base.agent.Agent] | dict[str, haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: execution_mode
      :type:  ExecutionMode
      :value: None



   .. py:attribute:: route_map
      :type:  dict[str, str] | None
      :value: None



   .. py:attribute:: routing_function
      :type:  collections.abc.Callable | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.core.schema.state_schema.StateSchema]
      :value: None



   .. py:attribute:: use_prebuilt_base
      :type:  bool
      :value: None



.. py:data:: logger

