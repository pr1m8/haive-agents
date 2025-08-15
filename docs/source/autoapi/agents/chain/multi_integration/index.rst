agents.chain.multi_integration
==============================

.. py:module:: agents.chain.multi_integration

.. autoapi-nested-parse::

   Integration of ChainAgent with Multi-Agent Base.

   Makes ChainAgent work seamlessly with the multi-agent framework.


   .. autolink-examples:: agents.chain.multi_integration
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.chain.multi_integration.logger


Classes
-------

.. autoapisummary::

   agents.chain.multi_integration.ChainMultiAgent
   agents.chain.multi_integration.ChainNodeWrapper
   agents.chain.multi_integration.ExtendedExecutionMode


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


Module Contents
---------------

.. py:class:: ChainMultiAgent

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   ChainAgent that works with the multi-agent framework.

   Combines the simplicity of ChainAgent with the power of MultiAgent.


   .. autolink-examples:: ChainMultiAgent
      :collapse:

   .. py:method:: from_chain(chain: haive.agents.chain.chain_agent_simple.ChainAgent, name: str | None = None, **kwargs) -> ChainMultiAgent
      :classmethod:


      Create a MultiAgent from a ChainAgent.


      .. autolink-examples:: from_chain
         :collapse:


   .. py:method:: from_nodes(nodes: list[haive.agents.chain.chain_agent_simple.NodeLike], edges: list | None = None, name: str = 'Chain Multi Agent', **kwargs) -> ChainMultiAgent
      :classmethod:


      Create directly from nodes and edges.


      .. autolink-examples:: from_nodes
         :collapse:


   .. py:attribute:: chain_config
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: execution_mode
      :type:  haive.agents.multi.utils.compatibility.ExecutionMode
      :value: None



.. py:class:: ChainNodeWrapper

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Wrapper to make non-agent nodes work in multi-agent framework.


   .. autolink-examples:: ChainNodeWrapper
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build a simple graph with just this node.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: 'Chain Node Wrapper'



   .. py:attribute:: node
      :type:  haive.agents.chain.chain_agent_simple.NodeLike
      :value: None



.. py:class:: ExtendedExecutionMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Extended execution modes including chain-based.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExtendedExecutionMode
      :collapse:

   .. py:attribute:: BRANCH
      :value: 'branch'



   .. py:attribute:: CHAIN
      :value: 'chain'



   .. py:attribute:: CONDITIONAL
      :value: 'conditional'



   .. py:attribute:: INFER
      :value: 'infer'



   .. py:attribute:: PARALLEL
      :value: 'parallel'



   .. py:attribute:: SEQUENTIAL
      :value: 'sequential'



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

.. py:data:: logger

