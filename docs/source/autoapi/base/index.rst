base
====

.. py:module:: base

.. autoapi-nested-parse::

   Base multi-agent implementation with branching and conditional routing support.

   This module provides an abstract base class for multi-agent systems that can:
   - Execute agents in sequence, parallel, or with conditional branching
   - Maintain private agent state schemas while sharing a global state
   - Support complex routing patterns including loops and conditional paths


   .. autolink-examples:: base
      :collapse:


Attributes
----------

.. autoapisummary::

   base.console
   base.logger


Classes
-------

.. autoapisummary::

   base.ConditionalAgent
   base.ExecutionMode
   base.MultiAgent
   base.ParallelAgent
   base.SequentialAgent


Module Contents
---------------

.. py:class:: ConditionalAgent

   Bases: :py:obj:`MultiAgent`


   Pre-configured conditional multi-agent with branching.


   .. autolink-examples:: ConditionalAgent
      :collapse:

   .. py:method:: build_custom_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Not needed for conditional mode.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: execution_mode
      :type:  ExecutionMode
      :value: None



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



.. py:class:: MultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Abstract base class for multi-agent systems with branching support.

   This class provides:
   - Automatic schema composition from child agents
   - Support for sequential, parallel, and conditional execution
   - Private agent state management
   - Complex routing patterns via conditional edges
   - Meta state for agent coordination


   .. autolink-examples:: MultiAgent
      :collapse:

   .. py:method:: _build_conditional_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Build a conditional execution graph.


      .. autolink-examples:: _build_conditional_graph
         :collapse:


   .. py:method:: _build_hierarchical_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Build a hierarchical execution graph.


      .. autolink-examples:: _build_hierarchical_graph
         :collapse:


   .. py:method:: _build_parallel_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Build a parallel execution graph.


      .. autolink-examples:: _build_parallel_graph
         :collapse:


   .. py:method:: _build_sequence_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Build a sequential execution graph.


      .. autolink-examples:: _build_sequence_graph
         :collapse:


   .. py:method:: _get_agent_node_name(agent: haive.agents.base.agent.Agent) -> str

      Get the unique node name for an agent.


      .. autolink-examples:: _get_agent_node_name
         :collapse:


   .. py:method:: _get_build_mode() -> haive.core.schema.agent_schema_composer.BuildMode

      Map execution mode to build mode.


      .. autolink-examples:: _get_build_mode
         :collapse:


   .. py:method:: _get_node_name(agent: str | haive.agents.base.agent.Agent) -> str

      Get the node name for an agent.


      .. autolink-examples:: _get_node_name
         :collapse:


   .. py:method:: _setup_io_schemas() -> None

      Set up input and output schemas based on execution mode.


      .. autolink-examples:: _setup_io_schemas
         :collapse:


   .. py:method:: add_conditional_edge(source_agent: str | haive.agents.base.agent.Agent, condition: collections.abc.Callable[[Any], str | bool], destinations: dict[str | bool, str | haive.agents.base.agent.Agent], default: str | haive.agents.base.agent.Agent | None = None) -> None

      Add a conditional edge between agents.

      :param source_agent: Source agent or its name/id
      :param condition: Function that returns a routing key
      :param destinations: Mapping of condition results to target agents
      :param default: Default destination if no match


      .. autolink-examples:: add_conditional_edge
         :collapse:


   .. py:method:: build_custom_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> haive.core.graph.state_graph.base_graph2.BaseGraph
      :abstractmethod:


      Build a custom graph - must be implemented by subclasses if using CUSTOM mode.

      :param graph: The graph to build on

      :returns: The modified graph


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the graph based on execution mode.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_agent_by_name(name: str) -> haive.agents.base.agent.Agent | None

      Get an agent by name or id.


      .. autolink-examples:: get_agent_by_name
         :collapse:


   .. py:method:: setup_multi_agent() -> MultiAgent

      Set up the multi-agent system after initialization.


      .. autolink-examples:: setup_multi_agent
         :collapse:


   .. py:method:: validate_agents(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Ensure agents list is not empty.


      .. autolink-examples:: validate_agents
         :collapse:


   .. py:method:: visualize_structure() -> None

      Visualize the multi-agent structure.


      .. autolink-examples:: visualize_structure
         :collapse:


   .. py:attribute:: _agent_node_mapping
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: _agent_private_states
      :type:  dict[str, type[pydantic.BaseModel]]
      :value: None



   .. py:attribute:: agents
      :type:  collections.abc.Sequence[haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: branches
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: execution_mode
      :type:  ExecutionMode
      :value: None



   .. py:attribute:: include_meta
      :type:  bool
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: schema_separation
      :type:  Literal['smart', 'shared', 'namespaced']
      :value: None



.. py:class:: ParallelAgent

   Bases: :py:obj:`MultiAgent`


   Pre-configured parallel multi-agent.


   .. autolink-examples:: ParallelAgent
      :collapse:

   .. py:method:: build_custom_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Not needed for parallel mode.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: execution_mode
      :type:  ExecutionMode
      :value: None



.. py:class:: SequentialAgent

   Bases: :py:obj:`MultiAgent`


   Pre-configured sequential multi-agent.


   .. autolink-examples:: SequentialAgent
      :collapse:

   .. py:method:: build_custom_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Not needed for sequential mode.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: execution_mode
      :type:  ExecutionMode
      :value: None



.. py:data:: console

.. py:data:: logger

