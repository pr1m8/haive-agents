agents.simple.agent
===================

.. py:module:: agents.simple.agent

.. autoapi-nested-parse::

   Agent_V3 core module.

   This module provides agent v3 functionality for the Haive framework.

   Classes:
       with: with implementation.
       SimpleAgent: SimpleAgent implementation.
       with: with implementation.

   Functions:
       log_execution_start: Log Execution Start functionality.
       log_execution_complete: Log Execution Complete functionality.
       ensure_aug_llm_config_with_debug: Ensure Aug Llm Config With Debug functionality.


   .. autolink-examples:: agents.simple.agent
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/simple/agent/v2/index


Attributes
----------

.. autoapisummary::

   agents.simple.agent.EngineT
   agents.simple.agent.TInput
   agents.simple.agent.TOutput
   agents.simple.agent.logger


Classes
-------

.. autoapisummary::

   agents.simple.agent.SimpleAgent


Module Contents
---------------

.. py:class:: SimpleAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`\ [\ :py:obj:`haive.core.engine.aug_llm.AugLLMConfig`\ ], :py:obj:`haive.core.common.mixins.recompile_mixin.RecompileMixin`, :py:obj:`haive.core.common.mixins.dynamic_tool_route_mixin.DynamicToolRouteMixin`


   SimpleAgent v3 with enhanced dynamic architecture and hooks system.

   This implementation uses the complete Haive dynamic architecture:

   **Enhanced Architecture:**
   - Enhanced base Agent with hooks system integration
   - Uses LLMState for proper state management with token tracking
   - TypeVar defaulted to AugLLMConfig for SimpleAgent
   - Full hooks lifecycle management (before/after execution, setup, etc.)
   - Structured output integration across different agent types
   - Hash-based change detection via RecompileMixin
   - Dynamic tool routing via DynamicToolRouteMixin
   - Graph recompilation on structural changes
   - Meta-agent embedding via MetaStateSchema
   - Type-safe node configuration via GenericEngineNodeConfig

   **Hooks Integration:**
   - Pre/post execution hooks with context
   - Graph building hooks for customization
   - State update hooks for monitoring
   - Error handling hooks for recovery
   - Node-level execution hooks

   **Key Features:**
   - Engine name references (not direct engine objects)
   - Recompilable graph with change tracking
   - Agent-as-tool composition support
   - Async execution patterns with hooks
   - Full observability with debug=True default
   - Cross-agent structured output compatibility

   **Architecture Integration:**
   - Inherits from Agent[AugLLMConfig] with proper TypeVar default
   - Uses RecompileMixin for recompilation management
   - Uses DynamicToolRouteMixin for tool change detection
   - Uses HooksMixin for lifecycle event management
   - Integrates with MetaStateSchema for embedding
   - Uses BaseGraph for dynamic graph management

   .. rubric:: Examples

   Basic usage with hooks and debug::

       agent = SimpleAgent(
           name="enhanced_agent",
           temperature=0.7,
           debug=True,  # Full observability
           auto_recompile=True
       )

       # Add hooks for monitoring
       @agent.before_run
       def log_execution_start(context):
           logger.info(f"Starting execution: {context.input_data}")

       @agent.after_run
       def log_execution_complete(context):
           logger.info(f"Completed execution: {context.output_data}")

       # Agent automatically recompiles on changes with full logging
       agent.add_tool(calculator_tool)  # Triggers recompilation with hooks
       result = await agent.arun("Calculate 15 * 23", debug=True)

   Meta-agent embedding with hooks::

       meta_state = MetaStateSchema.from_agent(agent)
       result = await meta_state.execute_agent(input_data)

   Agent-as-tool with structured output::

       structured_tool = SimpleAgent.as_structured_tool(
           name="data_processor",
           output_model=ProcessedData,
           temperature=0.1,
           debug=True
       )


   .. autolink-examples:: SimpleAgent
      :collapse:

   .. py:method:: _add_agent_node(graph: haive.core.graph.state_graph.base_graph2.BaseGraph, engine_name: str) -> None

      Add the main agent node with enhanced configuration.


      .. autolink-examples:: _add_agent_node
         :collapse:


   .. py:method:: _add_complex_routing(graph: haive.core.graph.state_graph.base_graph2.BaseGraph, engine_name: str, needs_tools: bool, needs_parsing: bool) -> None

      Add complex routing with tools and parsing support.


      .. autolink-examples:: _add_complex_routing
         :collapse:


   .. py:method:: _add_dynamic_tool_nodes(graph: haive.core.graph.state_graph.base_graph2.BaseGraph, engine_name: str) -> None

      Add dynamic tool nodes with change tracking and hooks.


      .. autolink-examples:: _add_dynamic_tool_nodes
         :collapse:


   .. py:method:: _add_parser_nodes(graph: haive.core.graph.state_graph.base_graph2.BaseGraph, engine_name: str) -> None

      Add parser nodes with schema validation and hooks.


      .. autolink-examples:: _add_parser_nodes
         :collapse:


   .. py:method:: _add_tool_nodes(graph: haive.core.graph.state_graph.base_graph2.BaseGraph, engine_name: str) -> None

      Add tool execution nodes to the graph.


      .. autolink-examples:: _add_tool_nodes
         :collapse:


   .. py:method:: _add_validation_nodes(graph: haive.core.graph.state_graph.base_graph2.BaseGraph, engine_name: str, needs_tools: bool, needs_parsing: bool) -> None

      Add validation/routing nodes with hooks.


      .. autolink-examples:: _add_validation_nodes
         :collapse:


   .. py:method:: _always_needs_validation() -> bool

      Check if we always need validation with debug logging.


      .. autolink-examples:: _always_needs_validation
         :collapse:


   .. py:method:: _has_structured_output() -> bool

      Check if agent has structured output with debug logging.


      .. autolink-examples:: _has_structured_output
         :collapse:


   .. py:method:: _has_tools() -> bool

      Check if agent has tools with debug logging.


      .. autolink-examples:: _has_tools
         :collapse:


   .. py:method:: _init_dynamic_tool_routing() -> None

      Initialize dynamic tool routing mixin with debug logging.


      .. autolink-examples:: _init_dynamic_tool_routing
         :collapse:


   .. py:method:: _init_hooks_system() -> None

      Initialize hooks system with debug logging.


      .. autolink-examples:: _init_hooks_system
         :collapse:


   .. py:method:: _init_recompile_mixin() -> None

      Initialize recompilation mixin with debug logging.


      .. autolink-examples:: _init_recompile_mixin
         :collapse:


   .. py:method:: _on_engine_change(change_type: str, **kwargs) -> None

      Handle engine configuration changes with hooks.


      .. autolink-examples:: _on_engine_change
         :collapse:


   .. py:method:: _on_tool_route_change(change_type: str, tool_name: str, **kwargs) -> None

      Handle tool route changes with hooks.


      .. autolink-examples:: _on_tool_route_change
         :collapse:


   .. py:method:: _recompile_graph() -> None

      Recompile the graph with current configuration and hooks.


      .. autolink-examples:: _recompile_graph
         :collapse:


   .. py:method:: _register_change_callbacks() -> None

      Register callbacks for change detection with hooks.


      .. autolink-examples:: _register_change_callbacks
         :collapse:


   .. py:method:: _register_default_hooks() -> None

      Register default hooks for debugging and monitoring.


      .. autolink-examples:: _register_default_hooks
         :collapse:


   .. py:method:: _register_graph_for_recompilation(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Register graph for automatic recompilation with hooks.


      .. autolink-examples:: _register_graph_for_recompilation
         :collapse:


   .. py:method:: _routing_condition_with_hooks(state: dict[str, Any]) -> str

      Determine routing based on state with hooks integration.


      .. autolink-examples:: _routing_condition_with_hooks
         :collapse:


   .. py:method:: _setup_structured_output_compatibility() -> None

      Setup cross-agent structured output compatibility.


      .. autolink-examples:: _setup_structured_output_compatibility
         :collapse:


   .. py:method:: _sync_convenience_fields_with_tracking() -> None

      Sync convenience fields to engine with change tracking and hooks.


      .. autolink-examples:: _sync_convenience_fields_with_tracking
         :collapse:


   .. py:method:: _trigger_initial_compilation() -> None

      Trigger initial graph compilation with hooks.


      .. autolink-examples:: _trigger_initial_compilation
         :collapse:


   .. py:method:: arun(input_data: Any, debug: bool | None = None, **kwargs) -> Any
      :async:


      Enhanced async run with debug=True default and hooks integration.


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: as_meta_capable(initial_state: dict[str, Any] | None = None, graph_context: dict[str, Any] | None = None) -> haive.core.schema.prebuilt.meta_state.MetaStateSchema

      Convert agent to meta-capable agent with hooks integration.


      .. autolink-examples:: as_meta_capable
         :collapse:


   .. py:method:: as_structured_tool(output_model: type[pydantic.BaseModel], name: str | None = None, description: str | None = None, debug: bool = True, **agent_kwargs) -> langchain_core.tools.BaseTool
      :classmethod:


      Convert SimpleAgent to a structured output tool.


      .. autolink-examples:: as_structured_tool
         :collapse:


   .. py:method:: as_tool(name: str | None = None, description: str | None = None, debug: bool = True, **agent_kwargs) -> langchain_core.tools.BaseTool
      :classmethod:


      Convert SimpleAgent to a LangChain tool with debug support.


      .. autolink-examples:: as_tool
         :collapse:


   .. py:method:: build_dynamic_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the dynamic agent graph with hooks integration.

      Creates a recompilable graph with enhanced features:

      1. **LLM Node**: Uses GenericEngineNodeConfig with engine name reference
      2. **Tool Nodes**: Dynamic tool routing with change detection and hooks
      3. **Parser Nodes**: Type-safe parsing with schema validation and hooks
      4. **Validation Nodes**: Conditional routing with hook-based monitoring

      The graph automatically recompiles when:
      - Tools are added/removed/modified (with hooks)
      - Engine configuration changes (with hooks)
      - Node schemas change (with hooks)
      - Routing logic changes (with hooks)

      **Hooks Integration:**
      - Pre/post node execution hooks
      - Graph structure change hooks
      - Routing decision hooks
      - Error handling hooks

      :returns: Compiled graph ready for execution with hooks
      :rtype: BaseGraph


      .. autolink-examples:: build_dynamic_graph
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the enhanced SimpleAgent v3 graph with hooks and dynamic features.

      Creates a graph structure that adapts based on agent configuration:
      1. Basic (no tools/parsing): START → agent_node → END
      2. With tools: START → agent_node → validation → tool_node → agent_node
      3. With parsing: START → agent_node → validation → parse_output → END
      4. With both: Combines tool and parsing flows with validation routing

      Enhanced with:
      - Hooks integration for lifecycle events
      - Dynamic recompilation triggers
      - Change tracking and monitoring
      - Debug logging throughout

      :returns: The compiled agent graph with enhanced capabilities.
      :rtype: BaseGraph


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: compile(**kwargs) -> Any

      Compile the agent's graph.

      This method ensures compatibility with ExecutionMixin.

      :returns: Compiled graph ready for execution


      .. autolink-examples:: compile
         :collapse:


   .. py:method:: create_runnable(runnable_config: Any = None) -> Any

      Create a runnable from this agent configuration.

      :param runnable_config: Optional runtime configuration.

      :returns: The compiled graph as a runnable.


      .. autolink-examples:: create_runnable
         :collapse:


   .. py:method:: ensure_aug_llm_config_with_debug(v)
      :classmethod:


      Ensure engine is AugLLMConfig or create one with debug enabled.


      .. autolink-examples:: ensure_aug_llm_config_with_debug
         :collapse:


   .. py:method:: get_input_fields() -> dict[str, tuple[type, Any]]

      Return input field definitions for SimpleAgent.

      :returns: Dictionary mapping field names to (type, default) tuples for input schema.


      .. autolink-examples:: get_input_fields
         :collapse:


   .. py:method:: get_output_fields() -> dict[str, tuple[type, Any]]

      Return output field definitions for SimpleAgent.

      :returns: Dictionary mapping field names to (type, default) tuples for output schema.


      .. autolink-examples:: get_output_fields
         :collapse:


   .. py:method:: model_post_init(__context: Any) -> None

      Initialize enhanced dynamic architecture components with hooks.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:method:: run(input_data: Any, debug: bool | None = None, **kwargs) -> Any

      Execute the agent with synchronous processing and structured output support.

      This method runs the agent synchronously using the configured LLM engine with
      full hooks integration, debug logging, and structured output validation.
      The execution includes comprehensive observability and automatic recompilation
      when tools or configuration changes are detected.

      The execution flow follows this enhanced pattern:
      1. Pre-execution hooks and validation
      2. Input preprocessing and state initialization
      3. Recompilation check and graph rebuilding if needed
      4. LLM execution with tool calling and structured output
      5. Post-execution hooks and state persistence
      6. Response formatting and debug logging

      :param input_data: Input for the agent execution. Supports multiple formats:
                         - str: Simple text input (automatically converted to HumanMessage)
                         - List[BaseMessage]: Pre-formatted LangChain message history
                         - Dict[str, Any]: Structured input matching agent's schema
                         - BaseModel: Pydantic model instances for type-safe input
      :param debug: Override the agent's default debug setting for this execution.
                    - None: Use agent's configured debug setting (default: True)
                    - True: Enable detailed execution tracing and state inspection
                    - False: Minimal logging for production execution
      :param \*\*kwargs: Additional execution arguments passed to LangGraph:
                         - config: Execution configuration overrides
                         - recursion_limit: Maximum graph traversal steps
                         - configurable: Runtime configuration updates
                         - stream_mode: Streaming execution options

      :returns:

                Execution result format varies based on configuration:
                    - With structured_output_model: Validated Pydantic model instance
                    - With tools only: Final LLM response after tool execution
                    - Basic execution: String response or state object
                    - Debug mode: Enhanced state with execution metadata and timing
      :rtype: Any

      :raises ValidationError: When structured output fails Pydantic model validation.
      :raises RecompilationError: When graph recompilation fails due to invalid changes.
      :raises ToolExecutionError: When tool calls fail during execution.
      :raises HookExecutionError: When before/after hooks raise exceptions.
      :raises LLMProviderError: When LLM provider is unavailable or returns errors.
      :raises StateManagementError: When state persistence or retrieval fails.

      .. rubric:: Examples

      Basic execution with default debug::

          # Agent created with debug=True by default
          agent = SimpleAgent(name="assistant")
          response = agent.run("Explain quantum computing")
          # Shows detailed execution trace by default

      Structured output with validation::

          from pydantic import BaseModel, Field

          class TechnicalExplanation(BaseModel):
              topic: str = Field(description="Technical topic being explained")
              difficulty: int = Field(ge=1, le=5, description="Difficulty level 1-5")
              key_concepts: List[str] = Field(description="Main concepts covered")
              summary: str = Field(description="Clear summary explanation")

          agent = SimpleAgent(
              name="tech_explainer",
              engine=AugLLMConfig(
                  structured_output_model=TechnicalExplanation,
                  temperature=0.3
              )
          )

          explanation = agent.run("Explain machine learning algorithms")
          # Returns TechnicalExplanation with validated structure
          assert isinstance(explanation, TechnicalExplanation)
          print(f"Topic: {explanation.topic}")
          print(f"Difficulty: {explanation.difficulty}/5")

      Tools with structured output and debug::

          @tool
          def search_database(query: str) -> str:
              '''Search internal database for information.'''
              return f"Database results for: {query}"

          class ResearchResult(BaseModel):
              query: str = Field(description="Original research query")
              sources_found: int = Field(description="Number of sources located")
              key_findings: List[str] = Field(description="Main research findings")
              confidence: float = Field(ge=0.0, le=1.0, description="Confidence in results")

          agent = SimpleAgent(
              name="researcher",
              engine=AugLLMConfig(
                  tools=[search_database],
                  structured_output_model=ResearchResult,
                  temperature=0.2
              ),
              debug=True  # Explicit debug enabling
          )

          # Execute with comprehensive logging
          research = agent.run("Research renewable energy trends", debug=True)
          # Shows: tool calls, LLM reasoning, structured output validation

      Production execution with minimal logging::

          agent = SimpleAgent(name="prod_agent", debug=False)
          result = agent.run("Process user request", debug=False)
          # Minimal logging for production performance

      With hooks for monitoring::

          @agent.before_run
          def log_start(context):
              logger.info(f"Starting: {context.input_data}")

          @agent.after_run
          def log_completion(context):
              logger.info(f"Completed in {context.execution_time}ms")

          result = agent.run("Execute with monitoring")
          # Hooks execute automatically during processing

      Dynamic tool addition with recompilation::

          agent = SimpleAgent(name="dynamic_agent", auto_recompile=True)

          # Initial execution
          result1 = agent.run("Hello")

          # Add new tool - triggers automatic recompilation
          @tool
          def new_calculator(expr: str) -> str:
              return str(eval(expr))

          agent.add_tool(new_calculator)  # Graph recompiles automatically
          result2 = agent.run("Calculate 5 * 8")  # Uses new tool

      .. note::

         - Debug mode is enabled by default (debug=True) for development visibility
         - Structured output models are converted to LangChain tools automatically
         - Graph recompilation happens automatically when tools/config changes
         - Hooks execute in order: before_run → execution → after_run
         - State is persisted after successful execution for conversation continuity
         - Token usage is tracked automatically via LLMState integration
         - All exceptions include detailed context for debugging

      Performance Considerations:
          - Debug mode adds ~20-30% execution overhead for logging
          - Structured output validation adds ~5-10ms per response
          - Recompilation takes ~100-200ms when triggered
          - Hook execution is minimal (~1-2ms total)

      .. seealso::

         arun: Asynchronous version with same functionality
         add_tool: Dynamic tool addition with recompilation
         set_structured_output: Runtime structured output configuration
         AugLLMConfig: Engine configuration options
         LLMState: State schema for token tracking and tool management
         RecompileMixin: Automatic recompilation functionality


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup SimpleAgent v3 with enhanced architecture and structured output support.

      This method implements the abstract setup_agent method from the base Agent class
      with comprehensive initialization for structured output, tool management, hooks
      integration, and recompilation capabilities. Called automatically during agent
      instantiation to configure all enhanced features.

      The setup process includes:
      1. Engine registration and configuration validation
      2. Structured output model preparation and tool conversion
      3. Hooks system initialization and event binding
      4. Tool routing configuration and metadata extraction
      5. State schema selection (LLMState for token tracking)
      6. Recompilation system activation with change detection
      7. Debug logging configuration and observability setup

      This method is called automatically and should not be invoked manually
      unless implementing custom agent initialization patterns.

      :raises EngineConfigurationError: If engine configuration is invalid or incompatible.
      :raises StructuredOutputError: If structured_output_model is not a valid Pydantic model.
      :raises HooksInitializationError: If hooks system fails to initialize properly.
      :raises ToolRegistrationError: If tool registration or routing configuration fails.

      .. rubric:: Examples

      Automatic setup during agent creation::

          # Setup is called automatically during __init__
          agent = SimpleAgent(
              name="auto_setup_agent",
              engine=AugLLMConfig(
                  structured_output_model=TaskAnalysis,
                  tools=[calculator_tool],
                  temperature=0.3
              ),
              debug=True
          )
          # setup_agent() has already been called with full configuration

      Manual setup for custom initialization::

          class CustomSimpleAgent(SimpleAgent):
              def setup_agent(self) -> None:
                  # Custom pre-setup logic
                  self.custom_configuration()

                  # Call parent setup for core functionality
                  super().setup_agent()

                  # Custom post-setup logic
                  self.additional_configuration()

      Validation of setup completion::

          agent = SimpleAgent(name="test_agent")

          # Verify setup was completed successfully
          assert hasattr(agent, 'engines')
          assert len(agent.engines) > 0
          assert agent.set_schema is True

      .. note::

         - This method is idempotent and safe to call multiple times
         - Engine configuration is validated during setup
         - Structured output models are converted to tools automatically
         - Tool routing is configured based on available tools and models
         - LLMState is selected as the default state schema for token tracking
         - Debug mode affects the verbosity of setup logging

      .. seealso::

         Agent.setup_agent: Base class abstract method being implemented
         _sync_convenience_fields_with_tracking: Engine synchronization
         AugLLMConfig: Engine configuration options
         LLMState: Default state schema for token tracking


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: change_tracking_enabled
      :type:  bool
      :value: None



   .. py:attribute:: debug
      :type:  bool
      :value: None



   .. py:attribute:: force_tool_use
      :type:  bool | None
      :value: None



   .. py:attribute:: hooks_enabled
      :type:  bool
      :value: None



   .. py:attribute:: max_tokens
      :type:  int | None
      :value: None



   .. py:attribute:: model_name
      :type:  str | None
      :value: None



   .. py:attribute:: output_parser
      :type:  langchain_core.output_parsers.base.BaseOutputParser | None
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate | langchain_core.prompts.PromptTemplate | None
      :value: None



   .. py:attribute:: structured_output_compatible
      :type:  bool
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: system_message
      :type:  str | None
      :value: None



   .. py:attribute:: temperature
      :type:  float | None
      :value: None



.. py:data:: EngineT

.. py:data:: TInput

.. py:data:: TOutput

.. py:data:: logger

