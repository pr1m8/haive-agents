
:py:mod:`agents.chain.chain_agent_simple`
=========================================

.. py:module:: agents.chain.chain_agent_simple

ChainAgent - The simplest way to build agent chains.

Just list your nodes and define the flow. That's it.


.. autolink-examples:: agents.chain.chain_agent_simple
   :collapse:

Classes
-------

.. autoapisummary::

   agents.chain.chain_agent_simple.ChainAgent
   agents.chain.chain_agent_simple.FlowBuilder


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChainAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ChainAgent {
        node [shape=record];
        "ChainAgent" [label="ChainAgent"];
        "haive.agents.base.agent.Agent" -> "ChainAgent";
      }

.. autoclass:: agents.chain.chain_agent_simple.ChainAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FlowBuilder:

   .. graphviz::
      :align: center

      digraph inheritance_FlowBuilder {
        node [shape=record];
        "FlowBuilder" [label="FlowBuilder"];
      }

.. autoclass:: agents.chain.chain_agent_simple.FlowBuilder
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.chain.chain_agent_simple.flow
   agents.chain.chain_agent_simple.flow_with_edges

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



.. rubric:: Related Links

.. autolink-examples:: agents.chain.chain_agent_simple
   :collapse:
   
.. autolink-skip:: next
