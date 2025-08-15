agents.base.types
=================

.. py:module:: agents.base.types

.. autoapi-nested-parse::

   Core type system for the Haive agent framework.

   Defines type variables, constraints, and base protocols for type-safe agent design.


   .. autolink-examples:: agents.base.types
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.types.HookFunction
   agents.base.types.TConfig
   agents.base.types.TEngine
   agents.base.types.TInput
   agents.base.types.TInvokableEngine
   agents.base.types.TNode
   agents.base.types.TOutput
   agents.base.types.TState


Classes
-------

.. autoapisummary::

   agents.base.types.Agent
   agents.base.types.AgentInput
   agents.base.types.AgentOutput
   agents.base.types.AgentState
   agents.base.types.EngineProvider
   agents.base.types.GraphProvider
   agents.base.types.GraphSegment
   agents.base.types.HookContext
   agents.base.types.HookPoint
   agents.base.types.Invokable
   agents.base.types.NodeConnection
   agents.base.types.StateProvider


Module Contents
---------------

.. py:class:: Agent

   Bases: :py:obj:`GraphProvider`\ [\ :py:obj:`TState`\ ], :py:obj:`StateProvider`\ [\ :py:obj:`TState`\ ], :py:obj:`Invokable`\ [\ :py:obj:`TInput`\ , :py:obj:`TOutput`\ ], :py:obj:`EngineProvider`\ [\ :py:obj:`TEngine`\ ], :py:obj:`Protocol`\ [\ :py:obj:`TEngine`\ , :py:obj:`TInput`\ , :py:obj:`TOutput`\ , :py:obj:`TState`\ ]


   Complete agent protocol combining all capabilities.


   .. autolink-examples:: Agent
      :collapse:

.. py:class:: AgentInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Default input schema for agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentInput
      :collapse:

   .. py:attribute:: messages
      :type:  list[Any]
      :value: []



.. py:class:: AgentOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Default output schema for agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentOutput
      :collapse:

   .. py:attribute:: messages
      :type:  list[Any]
      :value: []



.. py:class:: AgentState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Default state schema for agents.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentState
      :collapse:

   .. py:attribute:: messages
      :type:  list[Any]
      :value: []



.. py:class:: EngineProvider

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`TEngine`\ ]


   Protocol for objects that provide engines.


   .. autolink-examples:: EngineProvider
      :collapse:

   .. py:property:: engine
      :type: TEngine


      Get the primary engine.

      .. autolink-examples:: engine
         :collapse:


   .. py:property:: engines
      :type: dict[str, haive.core.engine.base.Engine]


      Get all engines.

      .. autolink-examples:: engines
         :collapse:


.. py:class:: GraphProvider

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`TState`\ ]


   Protocol for objects that provide graphs.


   .. autolink-examples:: GraphProvider
      :collapse:

   .. py:method:: build_graph() -> Any

      Build and return the graph.


      .. autolink-examples:: build_graph
         :collapse:


.. py:class:: GraphSegment(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`TState`\ ]


   Represents a segment of a graph that can be composed.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GraphSegment
      :collapse:

   .. py:attribute:: edges
      :type:  list[NodeConnection[TState]]


   .. py:attribute:: entry_point
      :type:  str


   .. py:attribute:: exit_points
      :type:  list[str]


   .. py:attribute:: metadata
      :type:  dict[str, Any]


   .. py:attribute:: nodes
      :type:  dict[str, Any]


.. py:class:: HookContext(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`TState`\ ]


   Context passed to hooks.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HookContext
      :collapse:

   .. py:attribute:: agent_id
      :type:  str


   .. py:attribute:: agent_type
      :type:  str


   .. py:attribute:: hook_point
      :type:  HookPoint


   .. py:attribute:: metadata
      :type:  dict[str, Any]


   .. py:attribute:: state_type
      :type:  type[TState] | None
      :value: None



.. py:class:: HookPoint

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Standard hook points in agent lifecycle.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HookPoint
      :collapse:

   .. py:attribute:: AFTER_GRAPH_BUILD
      :value: 'after_graph_build'



   .. py:attribute:: AFTER_GRAPH_COMPILE
      :value: 'after_graph_compile'



   .. py:attribute:: AFTER_INIT
      :value: 'after_init'



   .. py:attribute:: AFTER_INVOKE
      :value: 'after_invoke'



   .. py:attribute:: AFTER_NODE_ADD
      :value: 'after_node_add'



   .. py:attribute:: AFTER_SCHEMA_BUILD
      :value: 'after_schema_build'



   .. py:attribute:: AFTER_SETUP
      :value: 'after_setup'



   .. py:attribute:: AFTER_STATE_UPDATE
      :value: 'after_state_update'



   .. py:attribute:: BEFORE_GRAPH_BUILD
      :value: 'before_graph_build'



   .. py:attribute:: BEFORE_GRAPH_COMPILE
      :value: 'before_graph_compile'



   .. py:attribute:: BEFORE_INIT
      :value: 'before_init'



   .. py:attribute:: BEFORE_INVOKE
      :value: 'before_invoke'



   .. py:attribute:: BEFORE_NODE_ADD
      :value: 'before_node_add'



   .. py:attribute:: BEFORE_SCHEMA_BUILD
      :value: 'before_schema_build'



   .. py:attribute:: BEFORE_SETUP
      :value: 'before_setup'



   .. py:attribute:: BEFORE_STATE_UPDATE
      :value: 'before_state_update'



.. py:class:: Invokable

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`TInput`\ , :py:obj:`TOutput`\ ]


   Protocol for objects that can be invoked.


   .. autolink-examples:: Invokable
      :collapse:

   .. py:method:: ainvoke(input_data: TInput, config: dict[str, Any] | None = None) -> TOutput
      :async:


      Async invoke with input data.


      .. autolink-examples:: ainvoke
         :collapse:


   .. py:method:: invoke(input_data: TInput, config: dict[str, Any] | None = None) -> TOutput

      Invoke with input data.


      .. autolink-examples:: invoke
         :collapse:


.. py:class:: NodeConnection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`TState`\ ]


   Represents a connection between nodes in a graph.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: NodeConnection
      :collapse:

   .. py:attribute:: condition
      :type:  Any | None
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]


   .. py:attribute:: source
      :type:  str


   .. py:attribute:: target
      :type:  str


.. py:class:: StateProvider

   Bases: :py:obj:`Protocol`\ [\ :py:obj:`TState`\ ]


   Protocol for objects that provide state schemas.


   .. autolink-examples:: StateProvider
      :collapse:

   .. py:property:: state_schema
      :type: type[TState]


      Get the state schema type.

      .. autolink-examples:: state_schema
         :collapse:


.. py:data:: HookFunction

.. py:data:: TConfig

.. py:data:: TEngine

.. py:data:: TInput

.. py:data:: TInvokableEngine

.. py:data:: TNode

.. py:data:: TOutput

.. py:data:: TState

