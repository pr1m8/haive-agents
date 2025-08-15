agents.chain.chain_agent_simple
===============================

.. py:module:: agents.chain.chain_agent_simple

.. autoapi-nested-parse::

   ChainAgent - The simplest way to build agent chains.

   Just list your nodes and define the flow. That's it.


   .. autolink-examples:: agents.chain.chain_agent_simple
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.chain.chain_agent_simple.EdgeLike
   agents.chain.chain_agent_simple.NodeLike
   agents.chain.chain_agent_simple.logger


Classes
-------

.. autoapisummary::

   agents.chain.chain_agent_simple.ChainAgent
   agents.chain.chain_agent_simple.FlowBuilder


Functions
---------

.. autoapisummary::

   agents.chain.chain_agent_simple.flow
   agents.chain.chain_agent_simple.flow_with_edges


Module Contents
---------------

.. py:class:: ChainAgent(*nodes: NodeLike, **kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   The simplest way to build chains - just list nodes and edges.

   Initialize with nodes directly.

   .. rubric:: Examples

   ChainAgent(node1, node2, node3)  # Auto-sequential
   ChainAgent(node1, node2, edges=["0->1"])


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ChainAgent
      :collapse:

   .. py:method:: _add_edge_to_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph, edge: EdgeLike, node_names: dict[int, str])

      Add an edge to the graph.


      .. autolink-examples:: _add_edge_to_graph
         :collapse:


   .. py:method:: add(node: NodeLike) -> ChainAgent

      Add a node and auto-link from previous.


      .. autolink-examples:: add
         :collapse:


   .. py:method:: branch(condition: collections.abc.Callable, **branches: NodeLike) -> ChainAgent

      Add conditional branching.


      .. autolink-examples:: branch
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the graph from nodes and edges.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: merge_to(target_idx: int) -> ChainAgent

      Merge the last node to a target node.


      .. autolink-examples:: merge_to
         :collapse:


   .. py:attribute:: edges
      :type:  list[EdgeLike]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'Chain Agent'



   .. py:attribute:: nodes
      :type:  list[NodeLike]
      :value: None



.. py:class:: FlowBuilder(initial: NodeLike | None = None)

   Builder for method chaining.


   .. autolink-examples:: FlowBuilder
      :collapse:

   .. py:method:: add(node: NodeLike) -> FlowBuilder

      Add a node.


      .. autolink-examples:: add
         :collapse:


   .. py:method:: branch(condition: collections.abc.Callable, **branches: NodeLike) -> FlowBuilder

      Add branching.


      .. autolink-examples:: branch
         :collapse:


   .. py:method:: build() -> ChainAgent

      Get the chain.


      .. autolink-examples:: build
         :collapse:


   .. py:method:: merge_to(target_idx: int) -> FlowBuilder

      Merge to a previous node.


      .. autolink-examples:: merge_to
         :collapse:


   .. py:attribute:: chain


.. py:function:: flow(*nodes: NodeLike, **kwargs) -> ChainAgent

   Create a flow chain - the simplest way.

   .. rubric:: Examples

   # Sequential
   chain = flow(node1, node2, node3)

   # With edges
   chain = flow(node1, node2, node3, edges=["0->2"])  # Skip node2

   # With name
   chain = flow(node1, node2, name="My Flow")


   .. autolink-examples:: flow
      :collapse:

.. py:function:: flow_with_edges(nodes: list[NodeLike], *edges: EdgeLike) -> ChainAgent

   Create a flow with custom edges.

   .. rubric:: Example

   chain = flow_with_edges(
       [classifier, simple, complex, output],
       (0, {"simple": 1, "complex": 2}, lambda s: s.type),
       "1->3",
       "2->3"
   )


   .. autolink-examples:: flow_with_edges
      :collapse:

.. py:data:: EdgeLike

.. py:data:: NodeLike

.. py:data:: logger

