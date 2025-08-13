
:py:mod:`agents.chain.multi_integration`
========================================

.. py:module:: agents.chain.multi_integration

Integration of ChainAgent with Multi-Agent Base.

Makes ChainAgent work seamlessly with the multi-agent framework.


.. autolink-examples:: agents.chain.multi_integration
   :collapse:

Classes
-------

.. autoapisummary::

   agents.chain.multi_integration.ChainMultiAgent
   agents.chain.multi_integration.ChainNodeWrapper
   agents.chain.multi_integration.ExtendedExecutionMode


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChainMultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ChainMultiAgent {
        node [shape=record];
        "ChainMultiAgent" [label="ChainMultiAgent"];
        "haive.agents.multi.base.MultiAgent" -> "ChainMultiAgent";
      }

.. autoclass:: agents.chain.multi_integration.ChainMultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChainNodeWrapper:

   .. graphviz::
      :align: center

      digraph inheritance_ChainNodeWrapper {
        node [shape=record];
        "ChainNodeWrapper" [label="ChainNodeWrapper"];
        "haive.agents.base.agent.Agent" -> "ChainNodeWrapper";
      }

.. autoclass:: agents.chain.multi_integration.ChainNodeWrapper
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExtendedExecutionMode:

   .. graphviz::
      :align: center

      digraph inheritance_ExtendedExecutionMode {
        node [shape=record];
        "ExtendedExecutionMode" [label="ExtendedExecutionMode"];
        "str" -> "ExtendedExecutionMode";
        "enum.Enum" -> "ExtendedExecutionMode";
      }

.. autoclass:: agents.chain.multi_integration.ExtendedExecutionMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ExtendedExecutionMode** is an Enum defined in ``agents.chain.multi_integration``.



Functions
---------

.. autoapisummary::

   agents.chain.multi_integration.build_graph
   agents.chain.multi_integration.chain_multi
   agents.chain.multi_integration.chain_to_multi
   agents.chain.multi_integration.chain_to_multi
   agents.chain.multi_integration.conditional_multi
   agents.chain.multi_integration.from_chain
   agents.chain.multi_integration.from_nodes
   agents.chain.multi_integration.multi_to_chain
   agents.chain.multi_integration.multi_to_chain
   agents.chain.multi_integration.sequential_multi

.. py:function:: build_graph(*args, **kwargs)

   Stub function for build_graph - temporarily disabled.


   .. autolink-examples:: build_graph
      :collapse:

.. py:function:: chain_multi(*nodes: haive.agents.chain.chain_agent_simple.NodeLike, name: str = 'Chain Multi') -> ChainMultiAgent

   Create a ChainMultiAgent from nodes.


   .. autolink-examples:: chain_multi
      :collapse:

.. py:function:: chain_to_multi(chain: haive.agents.chain.chain_agent_simple.ChainAgent) -> ChainMultiAgent

   Convert a ChainAgent to a MultiAgent.


   .. autolink-examples:: chain_to_multi
      :collapse:

.. py:function:: chain_to_multi(*args, **kwargs)

   Stub function for chain_to_multi - temporarily disabled.


   .. autolink-examples:: chain_to_multi
      :collapse:

.. py:function:: conditional_multi(agents: list[haive.agents.base.agent.Agent], conditions: dict[str, collections.abc.Callable], name: str = 'Conditional Multi') -> ChainMultiAgent

   Create a conditional multi-agent system.


   .. autolink-examples:: conditional_multi
      :collapse:

.. py:function:: from_chain(*args, **kwargs)

   Stub function for from_chain - temporarily disabled.


   .. autolink-examples:: from_chain
      :collapse:

.. py:function:: from_nodes(*args, **kwargs)

   Stub function for from_nodes - temporarily disabled.


   .. autolink-examples:: from_nodes
      :collapse:

.. py:function:: multi_to_chain(multi: haive.agents.multi.base.MultiAgent) -> haive.agents.chain.chain_agent_simple.ChainAgent

   Convert a MultiAgent to a ChainAgent (if possible).


   .. autolink-examples:: multi_to_chain
      :collapse:

.. py:function:: multi_to_chain(*args, **kwargs)

   Stub function for multi_to_chain - temporarily disabled.


   .. autolink-examples:: multi_to_chain
      :collapse:

.. py:function:: sequential_multi(*agents: haive.agents.base.agent.Agent, name: str = 'Sequential Multi') -> ChainMultiAgent

   Create a sequential multi-agent system.


   .. autolink-examples:: sequential_multi
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.chain.multi_integration
   :collapse:
   
.. autolink-skip:: next
