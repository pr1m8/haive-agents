agents.chain.extended_chain
===========================

.. py:module:: agents.chain.extended_chain

.. autoapi-nested-parse::

   Extended Chain Agent with simplified chain building capabilities.

   This module provides the ExtendedChainAgent class and utilities for building
   complex multi-step agent workflows with easy-to-use chain syntax.


   .. autolink-examples:: agents.chain.extended_chain
      :collapse:


Classes
-------

.. autoapisummary::

   agents.chain.extended_chain.ChainBuilder
   agents.chain.extended_chain.ChainConfig
   agents.chain.extended_chain.ChainEdge
   agents.chain.extended_chain.ChainNode
   agents.chain.extended_chain.ChainState
   agents.chain.extended_chain.ExtendedChainAgent


Functions
---------

.. autoapisummary::

   agents.chain.extended_chain.chain
   agents.chain.extended_chain.chain_with_edges


Module Contents
---------------

.. py:class:: ChainBuilder

   Builder class for creating chain workflows.


   .. autolink-examples:: ChainBuilder
      :collapse:

   .. py:method:: add_edge(from_node: str, to_node: str, condition: collections.abc.Callable | None = None) -> ChainBuilder

      Add an edge between nodes.


      .. autolink-examples:: add_edge
         :collapse:


   .. py:method:: add_node(name: str, agent: Any, config: dict[str, Any] | None = None) -> ChainBuilder

      Add a node to the chain.


      .. autolink-examples:: add_node
         :collapse:


   .. py:method:: build() -> ChainConfig

      Build the chain configuration.


      .. autolink-examples:: build
         :collapse:


   .. py:attribute:: edges
      :type:  list[ChainEdge]
      :value: []



   .. py:attribute:: nodes
      :type:  list[ChainNode]
      :value: []



.. py:class:: ChainConfig

   Bases: :py:obj:`haive.core.engine.agent.AgentConfig`


   Configuration for ExtendedChainAgent.


   .. autolink-examples:: ChainConfig
      :collapse:

   .. py:attribute:: edges
      :type:  list[ChainEdge]
      :value: None



   .. py:attribute:: execution_mode
      :type:  str
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: nodes
      :type:  list[ChainNode]
      :value: None



.. py:class:: ChainEdge(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   An edge connection between chain nodes.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ChainEdge
      :collapse:

   .. py:attribute:: condition
      :type:  collections.abc.Callable | None
      :value: None



   .. py:attribute:: from_node
      :type:  str
      :value: None



   .. py:attribute:: to_node
      :type:  str
      :value: None



.. py:class:: ChainNode(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A node in a chain workflow.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ChainNode
      :collapse:

   .. py:attribute:: agent
      :type:  Any
      :value: None



   .. py:attribute:: config
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: dependencies
      :type:  list[str]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: ChainState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   State schema for chain execution.


   .. autolink-examples:: ChainState
      :collapse:

   .. py:attribute:: chain_complete
      :type:  bool
      :value: None



   .. py:attribute:: completed_nodes
      :type:  list[str]
      :value: None



   .. py:attribute:: current_node
      :type:  str
      :value: None



   .. py:attribute:: iteration_count
      :type:  int
      :value: None



   .. py:attribute:: node_results
      :type:  dict[str, Any]
      :value: None



.. py:class:: ExtendedChainAgent(config: ChainConfig)

   Bases: :py:obj:`haive.core.engine.agent.Agent`


   Extended chain agent for complex multi-step workflows.

   This agent provides a simplified interface for building complex chains
   of agents with dependencies, conditional execution, and state management.


   .. autolink-examples:: ExtendedChainAgent
      :collapse:

   .. py:method:: execute_node(node_name: str, state: ChainState) -> Any

      Execute a specific node in the chain.


      .. autolink-examples:: execute_node
         :collapse:


   .. py:method:: get_next_nodes(current_node: str, state: ChainState) -> list[str]

      Get the next nodes to execute based on current state.


      .. autolink-examples:: get_next_nodes
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the chain workflow.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: chain_config


   .. py:attribute:: state_schema


.. py:function:: chain(*agents: Any) -> ChainBuilder

   Create a simple sequential chain from a list of agents.

   :param \*agents: Variable number of agents to chain together

   :returns: ChainBuilder instance with sequential chain setup


   .. autolink-examples:: chain
      :collapse:

.. py:function:: chain_with_edges(nodes: dict[str, Any], edges: list[tuple]) -> ChainBuilder

   Create a chain with explicit nodes and edges.

   :param nodes: Dictionary mapping node names to agents
   :param edges: List of (from_node, to_node) tuples

   :returns: ChainBuilder instance with the specified structure


   .. autolink-examples:: chain_with_edges
      :collapse:

