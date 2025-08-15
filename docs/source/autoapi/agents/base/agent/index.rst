agents.base.agent
=================

.. py:module:: agents.base.agent

.. autoapi-nested-parse::

   Enhanced Agent hierarchy with engine-focused generics and backward compatibility.

   This module provides the enhanced agent architecture:
   - Workflow: Pure orchestration without LLM
   - Agent: Workflow + Engine (generic on engine type)
   - MultiAgent: Agent + multi-agent coordination

   Key features:
   - Engine-centric generics: Agent[EngineT]
   - Full backward compatibility with existing code
   - Clear separation of concerns: orchestration vs LLM vs coordination
   - Type safety when needed, flexibility when desired


   .. autolink-examples:: agents.base.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.agent.EngineT
   agents.base.agent.logger


Classes
-------

.. autoapisummary::

   agents.base.agent.Agent
   agents.base.agent.TypedInvokableEngine


Module Contents
---------------

.. py:class:: Agent

   Bases: :py:obj:`TypedInvokableEngine`\ [\ :py:obj:`EngineT`\ ], :py:obj:`haive.agents.base.mixins.execution_mixin.ExecutionMixin`, :py:obj:`haive.agents.base.mixins.state_mixin.StateMixin`, :py:obj:`haive.agents.base.mixins.persistence_mixin.PersistenceMixin`, :py:obj:`haive.agents.base.serialization_mixin.SerializationMixin`, :py:obj:`haive.agents.base.agent_structured_output_mixin.StructuredOutputMixin`, :py:obj:`haive.agents.base.pre_post_agent_mixin.PrePostAgentMixin`, :py:obj:`abc.ABC`


   Enhanced Agent with engine-focused generics and full backward compatibility.

   Agent = Workflow + Engine. The engine type is the primary generic parameter,
   enabling type-safe engine-specific functionality while maintaining full
   backward compatibility.

   Generic Parameters:
       EngineT: Type of engine (defaults to InvokableEngine for backward compatibility)

   Key Benefits:
       - Engine-specific type safety: Agent[AugLLMConfig] vs Agent[ReactEngine]
       - Backward compatible: existing Agent() calls work unchanged
       - Engine-specific methods: BaseRAGAgent[RetrieverEngine] gets retriever methods
       - Flexible composition: Any engine type can be used

   .. rubric:: Examples

   # Backward compatible - works unchanged
   agent = SimpleAgent(name="test")

   # Engine-specific typing
   aug_agent: SimpleAgent[AugLLMConfig] = SimpleAgent(engine=aug_config)
   rag_agent: BaseRAGAgent[RetrieverEngine] = BaseRAGAgent(engine=retriever_engine)

   # Mixed usage - all compatible
   agents = [agent, aug_agent, rag_agent]


   .. autolink-examples:: Agent
      :collapse:

   .. py:method:: __repr__() -> str


   .. py:method:: _auto_derive_io_schemas() -> None

      Automatically derive input and output schemas with intelligent defaults.

      This method:
      1. Derives input schema from state schema or first engine
      2. Derives output schema considering structured output models
      3. Falls back to messages-based schemas when appropriate


      .. autolink-examples:: _auto_derive_io_schemas
         :collapse:


   .. py:method:: _build_initial_graph() -> None

      Build the initial graph.


      .. autolink-examples:: _build_initial_graph
         :collapse:


   .. py:method:: _build_wrapped_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build a multi-agent graph with structured output wrapper.


      .. autolink-examples:: _build_wrapped_graph
         :collapse:


   .. py:method:: _check_and_wrap_structured_output() -> None

      Check if agent needs structured output wrapping and prepare for it.

      This method detects if the agent has a structured_output_model but is not
      already a structured output handler (to avoid infinite loops). If so, it
      prepares the agent to be wrapped in a multi-agent workflow.


      .. autolink-examples:: _check_and_wrap_structured_output
         :collapse:


   .. py:method:: _setup_hooks() -> None

      Initialize the hooks system properly.


      .. autolink-examples:: _setup_hooks
         :collapse:


   .. py:method:: _setup_persistence_from_config() -> None

      Setup persistence using the PersistenceMixin.


      .. autolink-examples:: _setup_persistence_from_config
         :collapse:


   .. py:method:: _setup_schemas() -> None

      Generate schemas from available engines using SchemaComposer.

      This method:
      1. Uses the SchemaComposer API
      2. Leverages automatic engine management
      3. Supports token usage tracking
      4. Automatically derives I/O schemas


      .. autolink-examples:: _setup_schemas
         :collapse:


   .. py:method:: _trigger_auto_recompile() -> None

      Override RecompileMixin's auto-recompile to trigger graph rebuilding.


      .. autolink-examples:: _trigger_auto_recompile
         :collapse:


   .. py:method:: add_hook(event: haive.agents.base.hooks.HookEvent, hook: haive.agents.base.hooks.HookFunction) -> None

      Add a hook function for an event.


      .. autolink-examples:: add_hook
         :collapse:


   .. py:method:: after_arun(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add an after_arun hook.


      .. autolink-examples:: after_arun
         :collapse:


   .. py:method:: after_build_graph(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add an after_build_graph hook.


      .. autolink-examples:: after_build_graph
         :collapse:


   .. py:method:: after_grading(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add an after_grading hook.


      .. autolink-examples:: after_grading
         :collapse:


   .. py:method:: after_message_transform(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add an after_message_transform hook.


      .. autolink-examples:: after_message_transform
         :collapse:


   .. py:method:: after_reflection(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add an after_reflection hook.


      .. autolink-examples:: after_reflection
         :collapse:


   .. py:method:: after_run(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add an after_run hook.


      .. autolink-examples:: after_run
         :collapse:


   .. py:method:: after_setup(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add an after_setup hook.


      .. autolink-examples:: after_setup
         :collapse:


   .. py:method:: after_state_update(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add an after_state_update hook.


      .. autolink-examples:: after_state_update
         :collapse:


   .. py:method:: after_structured_output(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add an after_structured_output hook.


      .. autolink-examples:: after_structured_output
         :collapse:


   .. py:method:: before_arun(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add a before_arun hook.


      .. autolink-examples:: before_arun
         :collapse:


   .. py:method:: before_build_graph(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add a before_build_graph hook.


      .. autolink-examples:: before_build_graph
         :collapse:


   .. py:method:: before_grading(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add a before_grading hook.


      .. autolink-examples:: before_grading
         :collapse:


   .. py:method:: before_message_transform(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add a before_message_transform hook.


      .. autolink-examples:: before_message_transform
         :collapse:


   .. py:method:: before_reflection(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add a before_reflection hook.


      .. autolink-examples:: before_reflection
         :collapse:


   .. py:method:: before_run(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add a before_run hook.


      .. autolink-examples:: before_run
         :collapse:


   .. py:method:: before_setup(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add a before_setup hook.


      .. autolink-examples:: before_setup
         :collapse:


   .. py:method:: before_state_update(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add a before_state_update hook.


      .. autolink-examples:: before_state_update
         :collapse:


   .. py:method:: before_structured_output(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add a before_structured_output hook.


      .. autolink-examples:: before_structured_output
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph
      :abstractmethod:


      Abstract method to build the agent's graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: clear_hooks(event: haive.agents.base.hooks.HookEvent | None = None) -> None

      Clear hooks for an event or all events.


      .. autolink-examples:: clear_hooks
         :collapse:


   .. py:method:: compile(**kwargs) -> Any

      Compile the graph and cache the result.

      :param \*\*kwargs: Additional compilation arguments

      :returns: The compiled graph


      .. autolink-examples:: compile
         :collapse:


   .. py:method:: complete_agent_setup()

      STEP 2-5: Complete agent setup in proper order.


      .. autolink-examples:: complete_agent_setup
         :collapse:


   .. py:method:: create_runnable(runnable_config: dict[str, Any] | None = None) -> Any

      Create and compile the runnable with proper schema kwargs.

      This implements the abstract method from Engine base class.


      .. autolink-examples:: create_runnable
         :collapse:


   .. py:method:: execute(input_data: Any) -> Any
      :async:


      Execute the agent (bridges Workflow API with Agent API).


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: execute_hooks(event: haive.agents.base.hooks.HookEvent, **context_kwargs) -> list[Any]

      Execute all hooks for an event.


      .. autolink-examples:: execute_hooks
         :collapse:


   .. py:method:: get_engine() -> EngineT | None

      Get the main engine with proper typing.


      .. autolink-examples:: get_engine
         :collapse:


   .. py:method:: get_input_fields() -> dict[str, tuple[type, Any]]

      Return input field definitions as field_name -> (type, default) pairs.

      This implements the abstract method from Engine base class.


      .. autolink-examples:: get_input_fields
         :collapse:


   .. py:method:: get_output_fields() -> dict[str, tuple[type, Any]]

      Return output field definitions as field_name -> (type, default) pairs.

      This implements the abstract method from Engine base class.


      .. autolink-examples:: get_output_fields
         :collapse:


   .. py:method:: normalize_engines_and_name(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      STEP 1: Normalize engines dict and auto-generate name.


      .. autolink-examples:: normalize_engines_and_name
         :collapse:


   .. py:method:: on_error(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add an on_error hook.


      .. autolink-examples:: on_error
         :collapse:


   .. py:method:: post_process(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add a post_process hook.


      .. autolink-examples:: post_process
         :collapse:


   .. py:method:: pre_process(func: haive.agents.base.hooks.HookFunction) -> haive.agents.base.hooks.HookFunction

      Decorator to add a pre_process hook.


      .. autolink-examples:: pre_process
         :collapse:


   .. py:method:: remove_hook(event: haive.agents.base.hooks.HookEvent, hook: haive.agents.base.hooks.HookFunction) -> None

      Remove a hook function.


      .. autolink-examples:: remove_hook
         :collapse:


   .. py:method:: set_engine(engine: EngineT) -> None

      Set the main engine with proper typing.


      .. autolink-examples:: set_engine
         :collapse:


   .. py:method:: setup_agent() -> None

      Hook for subclasses to perform field syncing and custom setup.

      This method is called BEFORE schema generation and graph building,
      allowing subclasses to sync fields to engines properly.

      Override this method in subclasses for custom setup logic.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: _app
      :type:  Any | None
      :value: None



   .. py:attribute:: _async_checkpointer
      :type:  Any | None
      :value: None



   .. py:attribute:: _async_setup_pending
      :type:  bool
      :value: None



   .. py:attribute:: _checkpoint_mode
      :type:  str
      :value: None



   .. py:attribute:: _compiled_graph
      :type:  langgraph.graph.graph.CompiledGraph | None
      :value: None



   .. py:attribute:: _graph_built
      :type:  bool
      :value: None



   .. py:attribute:: _hooks
      :type:  dict[haive.agents.base.hooks.HookEvent, list[haive.agents.base.hooks.HookFunction]]
      :value: None



   .. py:attribute:: _is_compiled
      :type:  bool
      :value: None



   .. py:attribute:: _setup_complete
      :type:  bool
      :value: None



   .. py:attribute:: add_store
      :type:  bool
      :value: None



   .. py:attribute:: checkpoint_mode
      :type:  Literal['sync', 'async']
      :value: None



   .. py:attribute:: checkpointer
      :type:  Any
      :value: None



   .. py:attribute:: debug
      :type:  bool
      :value: None



   .. py:attribute:: engine
      :type:  EngineT | None
      :value: None



   .. py:attribute:: engine_type
      :type:  Literal[haive.core.engine.base.EngineType.AGENT]
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.base.Engine]
      :value: None



   .. py:attribute:: graph
      :type:  haive.core.graph.state_graph.base_graph2.BaseGraph | None
      :value: None



   .. py:attribute:: hooks_enabled
      :type:  bool
      :value: None



   .. py:attribute:: input_schema
      :type:  type[pydantic.BaseModel] | dict[str, Any] | None
      :value: None



   .. py:attribute:: output_schema
      :type:  type[pydantic.BaseModel] | dict[str, Any] | None
      :value: None



   .. py:attribute:: persistence
      :type:  Any | None
      :value: None



   .. py:attribute:: runnable_config
      :type:  langchain_core.runnables.RunnableConfig | None
      :value: None



   .. py:attribute:: save_history
      :type:  bool
      :value: None



   .. py:attribute:: set_schema
      :type:  Literal[True, False]
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel] | dict[str, Any] | None
      :value: None



   .. py:attribute:: store
      :type:  Any | None
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: use_prebuilt_base
      :type:  bool
      :value: None



   .. py:attribute:: verbose
      :type:  bool
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



.. py:class:: TypedInvokableEngine

   Bases: :py:obj:`haive.core.engine.base.InvokableEngine`\ [\ :py:obj:`pydantic.BaseModel`\ , :py:obj:`pydantic.BaseModel`\ ], :py:obj:`Generic`\ [\ :py:obj:`EngineT`\ ]


   InvokableEngine that's parameterized by the engine type.


   .. autolink-examples:: TypedInvokableEngine
      :collapse:

.. py:data:: EngineT

.. py:data:: logger

