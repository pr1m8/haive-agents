agents.discovery.dynamic_tool_selector
======================================

.. py:module:: agents.discovery.dynamic_tool_selector

.. autoapi-nested-parse::

   Dynamic Tool Selector implementing LangGraph-style tool management patterns.

   This module implements sophisticated tool selection and management patterns
   inspired by LangGraph's many-tools approach, providing dynamic tool binding,
   context-aware selection, and intelligent tool routing.

   Key Features:
   - Dynamic tool selection and binding like LangGraph
   - Context-aware tool recommendation
   - Intelligent tool routing and management
   - State-aware tool selection
   - Tool usage learning and optimization


   .. autolink-examples:: agents.discovery.dynamic_tool_selector
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.discovery.dynamic_tool_selector.logger


Classes
-------

.. autoapisummary::

   agents.discovery.dynamic_tool_selector.ContextAwareSelector
   agents.discovery.dynamic_tool_selector.ContextAwareState
   agents.discovery.dynamic_tool_selector.DynamicToolSelector
   agents.discovery.dynamic_tool_selector.LangGraphStyleSelector
   agents.discovery.dynamic_tool_selector.SelectionMode
   agents.discovery.dynamic_tool_selector.ToolBindingStrategy
   agents.discovery.dynamic_tool_selector.ToolSelectionResult
   agents.discovery.dynamic_tool_selector.ToolSelectionStrategy
   agents.discovery.dynamic_tool_selector.ToolUsageStats


Functions
---------

.. autoapisummary::

   agents.discovery.dynamic_tool_selector.create_context_aware_selector
   agents.discovery.dynamic_tool_selector.create_dynamic_tool_selector
   agents.discovery.dynamic_tool_selector.create_langgraph_style_selector


Module Contents
---------------

.. py:class:: ContextAwareSelector(**kwargs)

   Bases: :py:obj:`DynamicToolSelector`


   Context-aware tool selector that considers conversation history.


   .. autolink-examples:: ContextAwareSelector
      :collapse:

   .. py:method:: _analyze_conversation_patterns(history: list[langchain_core.messages.BaseMessage]) -> dict[str, Any]
      :async:


      Analyze conversation to extract useful patterns.


      .. autolink-examples:: _analyze_conversation_patterns
         :collapse:


   .. py:method:: _extract_previous_tool_usage(history: list[langchain_core.messages.BaseMessage]) -> list[str]

      Extract tools that were used in conversation.


      .. autolink-examples:: _extract_previous_tool_usage
         :collapse:


   .. py:method:: select_with_conversation_context(query: str, conversation_history: list[langchain_core.messages.BaseMessage], user_preferences: dict[str, Any] | None = None) -> ToolSelectionResult
      :async:


      Select tools considering full conversation context.


      .. autolink-examples:: select_with_conversation_context
         :collapse:


   .. py:attribute:: conversation_memory
      :type:  list[dict[str, Any]]
      :value: []



.. py:class:: ContextAwareState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State information for context-aware tool selection.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ContextAwareState
      :collapse:

   .. py:attribute:: conversation_history
      :type:  list[langchain_core.messages.BaseMessage]
      :value: None



   .. py:attribute:: current_context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: current_query
      :type:  str
      :value: ''



   .. py:attribute:: previous_tools_used
      :type:  list[str]
      :value: None



   .. py:attribute:: session_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: user_preferences
      :type:  dict[str, Any]
      :value: None



.. py:class:: DynamicToolSelector

   Bases: :py:obj:`haive.core.common.mixins.tool_route_mixin.ToolRouteMixin`


   Dynamic tool selector implementing LangGraph-style patterns.

   This class provides sophisticated tool selection capabilities that adapt
   to query content, context, and usage patterns, similar to LangGraph's
   approach to handling many tools.


   .. autolink-examples:: DynamicToolSelector
      :collapse:

   .. py:method:: _convert_to_tools(components: list[haive.core.registry.ComponentMetadata]) -> list[langchain_core.tools.BaseTool]
      :async:


      Convert ComponentMetadata to actual BaseTool instances.


      .. autolink-examples:: _convert_to_tools
         :collapse:


   .. py:method:: _create_tool_from_component(component: haive.core.registry.ComponentMetadata) -> langchain_core.tools.BaseTool | None
      :async:


      Create a BaseTool from ComponentMetadata.


      .. autolink-examples:: _create_tool_from_component
         :collapse:


   .. py:method:: _evaluate_selection_quality(result: ToolSelectionResult, execution_results: dict[str, Any]) -> float
      :async:


      Evaluate the quality of tool selection.


      .. autolink-examples:: _evaluate_selection_quality
         :collapse:


   .. py:method:: _generate_cache_key(query: str, context: dict[str, Any]) -> str

      Generate cache key for tool selection.


      .. autolink-examples:: _generate_cache_key
         :collapse:


   .. py:method:: _generate_tool_recommendations() -> list[str]
      :async:


      Generate recommendations for tool usage optimization.


      .. autolink-examples:: _generate_tool_recommendations
         :collapse:


   .. py:method:: _get_available_components() -> list[haive.core.registry.ComponentMetadata]
      :async:


      Get available components from semantic discovery.


      .. autolink-examples:: _get_available_components
         :collapse:


   .. py:method:: _is_tool_better(new_tool: langchain_core.tools.BaseTool, existing_tool: langchain_core.tools.BaseTool) -> bool
      :async:


      Determine if new tool is better than existing tool.


      .. autolink-examples:: _is_tool_better
         :collapse:


   .. py:method:: _merge_tools_intelligently(existing_tools: list[langchain_core.tools.BaseTool], new_tools: list[langchain_core.tools.BaseTool]) -> list[langchain_core.tools.BaseTool]
      :async:


      Intelligently merge existing and new tools.


      .. autolink-examples:: _merge_tools_intelligently
         :collapse:


   .. py:method:: _refine_query_from_feedback(original_query: str, execution_results: dict[str, Any]) -> str
      :async:


      Refine query based on execution feedback.


      .. autolink-examples:: _refine_query_from_feedback
         :collapse:


   .. py:method:: _select_strategy() -> ToolSelectionStrategy

      Select appropriate tool selection strategy.


      .. autolink-examples:: _select_strategy
         :collapse:


   .. py:method:: _selective_tool_replacement(existing_tools: list[langchain_core.tools.BaseTool], new_tools: list[langchain_core.tools.BaseTool]) -> list[langchain_core.tools.BaseTool]
      :async:


      Selectively replace tools based on performance metrics.


      .. autolink-examples:: _selective_tool_replacement
         :collapse:


   .. py:method:: _setup_default_strategies() -> None

      Setup default tool selection strategies.


      .. autolink-examples:: _setup_default_strategies
         :collapse:


   .. py:method:: _update_context_state(query: str, context: dict[str, Any]) -> None
      :async:


      Update the context state with new information.


      .. autolink-examples:: _update_context_state
         :collapse:


   .. py:method:: _update_usage_stats(query: str, tools: list[langchain_core.tools.BaseTool], context: dict[str, Any] | None) -> None
      :async:


      Update usage statistics for selected tools.


      .. autolink-examples:: _update_usage_stats
         :collapse:


   .. py:method:: analyze_tool_performance() -> dict[str, Any]
      :async:


      Analyze tool performance and provide insights.


      .. autolink-examples:: analyze_tool_performance
         :collapse:


   .. py:method:: bind_tools_to_llm(llm_instance: Any, selected_tools: list[langchain_core.tools.BaseTool], strategy: ToolBindingStrategy = None) -> Any
      :async:


      Bind selected tools to LLM instance using specified strategy.

      This implements the LangGraph pattern of dynamically binding tools
      to the language model based on the current query context.


      .. autolink-examples:: bind_tools_to_llm
         :collapse:


   .. py:method:: iterative_tool_refinement(initial_query: str, llm_response: str, execution_results: dict[str, Any], max_iterations: int = 3) -> ToolSelectionResult
      :async:


      Iteratively refine tool selection based on execution feedback.

      This implements an advanced pattern where tool selection is refined
      based on the results of previous tool executions, similar to
      LangGraph's iterative approaches.


      .. autolink-examples:: iterative_tool_refinement
         :collapse:


   .. py:method:: select_tools_for_query(query: str, available_tools: list[langchain_core.tools.BaseTool] | None = None, context: dict[str, Any] | None = None, force_refresh: bool = False) -> ToolSelectionResult
      :async:


      Select optimal tools for a given query using LangGraph-style selection.

      This is the main entry point for tool selection, implementing the
      LangGraph pattern of dynamically selecting relevant tools based on
      query content and context.


      .. autolink-examples:: select_tools_for_query
         :collapse:


   .. py:method:: setup_selector() -> DynamicToolSelector

      Setup the tool selector with default components.


      .. autolink-examples:: setup_selector
         :collapse:


   .. py:attribute:: binding_strategy
      :type:  ToolBindingStrategy
      :value: None



   .. py:attribute:: cache_ttl_seconds
      :type:  float
      :value: None



   .. py:attribute:: context_state
      :type:  ContextAwareState
      :value: None



   .. py:attribute:: learning_enabled
      :type:  bool
      :value: None



   .. py:attribute:: max_tools_per_query
      :type:  int
      :value: None



   .. py:attribute:: min_confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: selection_mode
      :type:  SelectionMode
      :value: None



   .. py:attribute:: selection_strategies
      :type:  dict[str, ToolSelectionStrategy]
      :value: None



   .. py:attribute:: semantic_discovery
      :type:  SemanticDiscoveryEngine | None
      :value: None



   .. py:attribute:: tool_cache
      :type:  dict[str, list[langchain_core.tools.BaseTool]]
      :value: None



   .. py:attribute:: usage_stats
      :type:  dict[str, ToolUsageStats]
      :value: None



.. py:class:: LangGraphStyleSelector

   Bases: :py:obj:`DynamicToolSelector`


   LangGraph-style tool selector with state-based selection.

   This class specifically implements the LangGraph pattern of using
   state to determine tool selection and binding.


   .. autolink-examples:: LangGraphStyleSelector
      :collapse:

   .. py:method:: create_tool_selection_node() -> collections.abc.Callable

      Create a node function for LangGraph that selects tools.

      This returns a function that can be used as a node in a LangGraph
      workflow for dynamic tool selection.


      .. autolink-examples:: create_tool_selection_node
         :collapse:


   .. py:method:: select_tools_with_state(state: dict[str, Any], available_tools: list[langchain_core.tools.BaseTool] | None = None) -> ToolSelectionResult
      :async:


      Select tools based on LangGraph-style state.

      This method implements the LangGraph pattern where tool selection
      is based on the current state of the conversation/workflow.


      .. autolink-examples:: select_tools_with_state
         :collapse:


.. py:class:: SelectionMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Tool selection modes.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SelectionMode
      :collapse:

   .. py:attribute:: ADAPTIVE
      :value: 'adaptive'



   .. py:attribute:: CONTEXTUAL
      :value: 'contextual'



   .. py:attribute:: DYNAMIC
      :value: 'dynamic'



   .. py:attribute:: ITERATIVE
      :value: 'iterative'



   .. py:attribute:: STATIC
      :value: 'static'



.. py:class:: ToolBindingStrategy

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Strategies for binding tools to LLM.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToolBindingStrategy
      :collapse:

   .. py:attribute:: APPEND
      :value: 'append'



   .. py:attribute:: MERGE
      :value: 'merge'



   .. py:attribute:: REPLACE_ALL
      :value: 'replace_all'



   .. py:attribute:: SELECTIVE
      :value: 'selective'



.. py:class:: ToolSelectionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of tool selection process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToolSelectionResult
      :collapse:

   .. py:attribute:: fallback_used
      :type:  bool
      :value: None



   .. py:attribute:: query_analysis
      :type:  QueryAnalysis | None
      :value: None



   .. py:attribute:: selected_tools
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



   .. py:attribute:: selection_confidence
      :type:  float
      :value: None



   .. py:attribute:: selection_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: selection_time_ms
      :type:  float
      :value: None



.. py:class:: ToolSelectionStrategy

   Bases: :py:obj:`Protocol`


   Protocol for tool selection strategies.


   .. autolink-examples:: ToolSelectionStrategy
      :collapse:

   .. py:method:: select_tools(query: str, available_tools: list[haive.core.registry.ComponentMetadata], context: ContextAwareState, max_tools: int = 5) -> ToolSelectionResult
      :async:


      Select tools based on strategy.


      .. autolink-examples:: select_tools
         :collapse:


.. py:class:: ToolUsageStats(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Statistics for tool usage and performance.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToolUsageStats
      :collapse:

   .. py:attribute:: avg_execution_time
      :type:  float
      :value: 0.0



   .. py:attribute:: contexts_used
      :type:  list[str]
      :value: None



   .. py:attribute:: error_count
      :type:  int
      :value: 0



   .. py:attribute:: last_used
      :type:  str | None
      :value: None



   .. py:attribute:: success_count
      :type:  int
      :value: 0



   .. py:attribute:: tool_name
      :type:  str


   .. py:attribute:: usage_count
      :type:  int
      :value: 0



.. py:function:: create_context_aware_selector(max_tools: int = 5, min_confidence: float = 0.7) -> ContextAwareSelector

   Create a context-aware tool selector.


   .. autolink-examples:: create_context_aware_selector
      :collapse:

.. py:function:: create_dynamic_tool_selector(selection_mode: SelectionMode = SelectionMode.DYNAMIC, max_tools: int = 5, semantic_discovery: SemanticDiscoveryEngine | None = None) -> DynamicToolSelector

   Create a dynamic tool selector with sensible defaults.


   .. autolink-examples:: create_dynamic_tool_selector
      :collapse:

.. py:function:: create_langgraph_style_selector(max_tools: int = 5, learning_enabled: bool = True) -> LangGraphStyleSelector

   Create a LangGraph-style tool selector.


   .. autolink-examples:: create_langgraph_style_selector
      :collapse:

.. py:data:: logger

