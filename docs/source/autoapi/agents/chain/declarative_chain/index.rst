agents.chain.declarative_chain
==============================

.. py:module:: agents.chain.declarative_chain

.. autoapi-nested-parse::

   Declarative chain building for complex agent workflows.

   Provides declarative specification and building of complex agent chains
   with branching, loops, and conditional execution.


   .. autolink-examples:: agents.chain.declarative_chain
      :collapse:


Classes
-------

.. autoapisummary::

   agents.chain.declarative_chain.BranchSpec
   agents.chain.declarative_chain.ChainBuilder
   agents.chain.declarative_chain.ChainSpec
   agents.chain.declarative_chain.DeclarativeChainAgent
   agents.chain.declarative_chain.LoopSpec
   agents.chain.declarative_chain.NodeSpec
   agents.chain.declarative_chain.SequenceSpec


Functions
---------

.. autoapisummary::

   agents.chain.declarative_chain.complex_rag


Module Contents
---------------

.. py:class:: BranchSpec

   Specification for conditional branching.


   .. autolink-examples:: BranchSpec
      :collapse:

   .. py:attribute:: branches
      :type:  dict[Any, str]


   .. py:attribute:: condition
      :type:  str | collections.abc.Callable[[dict[str, Any]], Any]


   .. py:attribute:: default
      :type:  str | None
      :value: None



   .. py:attribute:: from_node
      :type:  str


.. py:class:: ChainBuilder(name: str)

   Builder for creating declarative chains.


   .. autolink-examples:: ChainBuilder
      :collapse:

   .. py:method:: add_branch(from_node: str, condition: str | collections.abc.Callable, branches: dict[Any, str], default: str | None = None) -> ChainBuilder

      Add conditional branching.


      .. autolink-examples:: add_branch
         :collapse:


   .. py:method:: add_loop(start_node: str, end_node: str, condition: str | collections.abc.Callable, max_iterations: int = 10) -> ChainBuilder

      Add a loop.


      .. autolink-examples:: add_loop
         :collapse:


   .. py:method:: add_node(name: str, node: Any, node_type: str = 'agent') -> ChainBuilder

      Add a node to the chain.


      .. autolink-examples:: add_node
         :collapse:


   .. py:method:: add_sequence(*nodes: str) -> ChainBuilder

      Add a sequence of nodes.


      .. autolink-examples:: add_sequence
         :collapse:


   .. py:method:: build() -> DeclarativeChainAgent

      Build the final chain agent.


      .. autolink-examples:: build
         :collapse:


   .. py:attribute:: branches
      :type:  list[BranchSpec]
      :value: []



   .. py:attribute:: entry_point
      :value: 'START'



   .. py:attribute:: exit_points
      :value: ['END']



   .. py:attribute:: loops
      :type:  list[LoopSpec]
      :value: []



   .. py:attribute:: name


   .. py:attribute:: nodes
      :type:  list[NodeSpec]
      :value: []



   .. py:attribute:: sequences
      :type:  list[SequenceSpec]
      :value: []



.. py:class:: ChainSpec

   Complete specification for a declarative chain.


   .. autolink-examples:: ChainSpec
      :collapse:

   .. py:attribute:: branches
      :type:  list[BranchSpec]
      :value: None



   .. py:attribute:: entry_point
      :type:  str
      :value: 'START'



   .. py:attribute:: exit_points
      :type:  list[str]
      :value: None



   .. py:attribute:: loops
      :type:  list[LoopSpec]
      :value: None



   .. py:attribute:: nodes
      :type:  list[NodeSpec]


   .. py:attribute:: sequences
      :type:  list[SequenceSpec]
      :value: None



.. py:class:: DeclarativeChainAgent(name: str, chain_spec: ChainSpec)

   Agent that executes a declaratively defined chain.


   .. autolink-examples:: DeclarativeChainAgent
      :collapse:

   .. py:method:: _compile_graph()

      Compile the chain specification into an executable graph.


      .. autolink-examples:: _compile_graph
         :collapse:


   .. py:method:: arun(input_data: dict[str, Any]) -> dict[str, Any]
      :async:


      Execute the chain asynchronously.


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: run(input_data: dict[str, Any]) -> dict[str, Any]

      Execute the chain.


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: _compiled_graph
      :value: None



   .. py:attribute:: chain_spec


   .. py:attribute:: name


.. py:class:: LoopSpec

   Specification for loops in the chain.


   .. autolink-examples:: LoopSpec
      :collapse:

   .. py:attribute:: condition
      :type:  str | collections.abc.Callable[[dict[str, Any]], bool]


   .. py:attribute:: end_node
      :type:  str


   .. py:attribute:: max_iterations
      :type:  int
      :value: 10



   .. py:attribute:: start_node
      :type:  str


.. py:class:: NodeSpec

   Specification for a single node in a chain.


   .. autolink-examples:: NodeSpec
      :collapse:

   .. py:attribute:: name
      :type:  str


   .. py:attribute:: node
      :type:  Any


   .. py:attribute:: node_type
      :type:  str
      :value: 'agent'



.. py:class:: SequenceSpec

   Specification for a sequence of nodes.


   .. autolink-examples:: SequenceSpec
      :collapse:

   .. py:attribute:: nodes
      :type:  list[str]


.. py:function:: complex_rag(*args, **kwargs)

   Create a complex RAG chain using declarative building.


   .. autolink-examples:: complex_rag
      :collapse:

