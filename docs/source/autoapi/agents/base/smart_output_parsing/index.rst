agents.base.smart_output_parsing
================================

.. py:module:: agents.base.smart_output_parsing

.. autoapi-nested-parse::

   Smart Output Parsing with Post-Hooks Integration.

   This module demonstrates how to use GenericEngineNodeConfig and post-hooks
   to handle specific output parsing in a smart, flexible manner.


   .. autolink-examples:: agents.base.smart_output_parsing
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.smart_output_parsing.TInput
   agents.base.smart_output_parsing.TOutput
   agents.base.smart_output_parsing.TParsed
   agents.base.smart_output_parsing.logger


Classes
-------

.. autoapisummary::

   agents.base.smart_output_parsing.SmartCallableOutputParser
   agents.base.smart_output_parsing.SmartGenericEngineNode
   agents.base.smart_output_parsing.SmartOutputParsingMixin


Functions
---------

.. autoapisummary::

   agents.base.smart_output_parsing.create_smart_engine_node
   agents.base.smart_output_parsing.create_smart_parsing_callable
   agents.base.smart_output_parsing.detect_content_type
   agents.base.smart_output_parsing.parse_json_content
   agents.base.smart_output_parsing.parse_structured_content


Module Contents
---------------

.. py:class:: SmartCallableOutputParser

   Bases: :py:obj:`haive.core.graph.node.callable_node.CallableNodeConfig`


   CallableNodeConfig specialized for output parsing with smart routing.


   .. autolink-examples:: SmartCallableOutputParser
      :collapse:

   .. py:method:: __call__(state, config=None)

      Execute with smart content detection and routing.


      .. autolink-examples:: __call__
         :collapse:


   .. py:attribute:: detection_function
      :type:  collections.abc.Callable | None
      :value: None



   .. py:attribute:: parsing_functions
      :type:  dict[str, collections.abc.Callable]
      :value: None



.. py:class:: SmartGenericEngineNode

   Bases: :py:obj:`haive.core.graph.node.engine_node_generic.GenericEngineNodeConfig`\ [\ :py:obj:`TInput`\ , :py:obj:`TOutput`\ ]


   Enhanced GenericEngineNodeConfig with smart output parsing.


   .. autolink-examples:: SmartGenericEngineNode
      :collapse:

   .. py:method:: __call__(state, config=None)

      Execute with smart output parsing post-processing.


      .. autolink-examples:: __call__
         :collapse:


   .. py:method:: _apply_smart_parsing(update_dict: dict, state) -> dict[str, Any]

      Apply smart parsing to update dictionary.


      .. autolink-examples:: _apply_smart_parsing
         :collapse:


   .. py:method:: _apply_strategy(strategy: str, message: Any, state) -> Any

      Apply a specific parsing strategy.


      .. autolink-examples:: _apply_strategy
         :collapse:


   .. py:method:: _extract_content(message: Any) -> str | None

      Extract content from message.


      .. autolink-examples:: _extract_content
         :collapse:


   .. py:method:: _parse_json_content(message: Any) -> Any

      Parse JSON from message content.


      .. autolink-examples:: _parse_json_content
         :collapse:


   .. py:method:: _parse_list_content(message: Any) -> list | None

      Parse list from message content.


      .. autolink-examples:: _parse_list_content
         :collapse:


   .. py:method:: _parse_pydantic_content(message: Any, state) -> Any

      Parse using structured output model.


      .. autolink-examples:: _parse_pydantic_content
         :collapse:


   .. py:method:: _parse_tool_calls(message: Any) -> list | None

      Parse tool calls from message.


      .. autolink-examples:: _parse_tool_calls
         :collapse:


   .. py:attribute:: custom_parsers
      :type:  dict[str, langchain_core.output_parsers.base.BaseOutputParser]
      :value: None



   .. py:attribute:: enable_smart_parsing
      :type:  bool
      :value: None



   .. py:attribute:: parsing_strategies
      :type:  list[str]
      :value: None



   .. py:attribute:: post_processing_callables
      :type:  list[collections.abc.Callable]
      :value: None



.. py:class:: SmartOutputParsingMixin(*args, **kwargs)

   Mixin to add smart output parsing capabilities to agents.


   .. autolink-examples:: SmartOutputParsingMixin
      :collapse:

   .. py:method:: _apply_parsing_strategy(context: haive.agents.base.hooks.HookContext, strategy: str) -> Any

      Apply the detected parsing strategy.


      .. autolink-examples:: _apply_parsing_strategy
         :collapse:


   .. py:method:: _detect_parsing_strategy(context: haive.agents.base.hooks.HookContext) -> str | None

      Detect what parsing strategy should be applied.


      .. autolink-examples:: _detect_parsing_strategy
         :collapse:


   .. py:method:: _parse_json_content(result: Any) -> Any

      Parse JSON content from message.


      .. autolink-examples:: _parse_json_content
         :collapse:


   .. py:method:: _parse_json_markdown(result: Any) -> Any

      Parse JSON content from markdown code blocks.


      .. autolink-examples:: _parse_json_markdown
         :collapse:


   .. py:method:: _parse_list_content(result: Any) -> Any

      Parse list content from message.


      .. autolink-examples:: _parse_list_content
         :collapse:


   .. py:method:: _parse_pydantic_content(result: Any) -> Any

      Parse content using engine's structured output model.


      .. autolink-examples:: _parse_pydantic_content
         :collapse:


   .. py:method:: _parse_tool_calls(result: Any) -> Any

      Parse tool calls from AI message.


      .. autolink-examples:: _parse_tool_calls
         :collapse:


   .. py:method:: _setup_output_parsing_hooks()

      Setup post-processing hooks for output parsing.


      .. autolink-examples:: _setup_output_parsing_hooks
         :collapse:


   .. py:method:: _smart_output_parsing_hook(context: haive.agents.base.hooks.HookContext)

      Post-hook that intelligently parses agent output based on context.


      .. autolink-examples:: _smart_output_parsing_hook
         :collapse:


   .. py:attribute:: _output_parsing_hooks
      :type:  dict[str, collections.abc.Callable]


.. py:function:: create_smart_engine_node(engine, name: str, input_schema: type[pydantic.BaseModel] | None = None, output_schema: type[pydantic.BaseModel] | None = None, parsing_strategies: list[str] | None = None, **kwargs) -> SmartGenericEngineNode

   Create a smart generic engine node with output parsing.


   .. autolink-examples:: create_smart_engine_node
      :collapse:

.. py:function:: create_smart_parsing_callable(parsing_functions: dict[str, collections.abc.Callable], detection_function: collections.abc.Callable, name: str = 'smart_parser', **kwargs) -> SmartCallableOutputParser

   Create a smart callable parser with content detection.


   .. autolink-examples:: create_smart_parsing_callable
      :collapse:

.. py:function:: detect_content_type(state) -> str

   Example content type detection function.


   .. autolink-examples:: detect_content_type
      :collapse:

.. py:function:: parse_json_content(state) -> dict

   Example JSON parsing function.


   .. autolink-examples:: parse_json_content
      :collapse:

.. py:function:: parse_structured_content(state) -> dict

   Example structured content parsing function.


   .. autolink-examples:: parse_structured_content
      :collapse:

.. py:data:: TInput

.. py:data:: TOutput

.. py:data:: TParsed

.. py:data:: logger

