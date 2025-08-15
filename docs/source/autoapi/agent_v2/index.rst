agent_v2
========

.. py:module:: agent_v2

.. autoapi-nested-parse::

   SimpleAgent V2 - Uses V2 validation node + router system.

   This version uses the V2 validation system that can properly:
   1. Add ToolMessages to state for Pydantic model validation
   2. Use separate validation node + router for proper state management
   3. Handle both regular tools and Pydantic models correctly

   Key improvements over V1:
   - Uses ValidationNodeV2 for state updates
   - Uses validation_router_v2 for routing decisions
   - Proper ToolMessage creation for Pydantic models
   - Better error handling and routing


   .. autolink-examples:: agent_v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agent_v2.logger


Classes
-------

.. autoapisummary::

   agent_v2.SimpleAgentV2


Functions
---------

.. autoapisummary::

   agent_v2.has_tool_calls_v2


Module Contents
---------------

.. py:class:: SimpleAgentV2

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   V2 SimpleAgent with improved validation node + router system.

   This version addresses the key issues with tool message handling by using
   a two-step validation process:
   1. ValidationNodeV2: Updates state with ToolMessages
   2. validation_router_v2: Makes routing decisions based on updated state

   This allows proper ToolMessage creation for Pydantic models while
   maintaining clean separation between state updates and routing.


   .. autolink-examples:: SimpleAgentV2
      :collapse:

   .. py:method:: __repr__() -> str


   .. py:method:: _has_force_tool_use() -> bool

      Check if tool use is forced.


      .. autolink-examples:: _has_force_tool_use
         :collapse:


   .. py:method:: _modify_engine_schema() -> None

      MODIFY the engine's output schema to include structured output fields.


      .. autolink-examples:: _modify_engine_schema
         :collapse:


   .. py:method:: _needs_parser_node() -> bool

      Check if we need a parser node for pydantic models.


      .. autolink-examples:: _needs_parser_node
         :collapse:


   .. py:method:: _needs_tool_node() -> bool

      Check if we need a tool node for langchain tools.


      .. autolink-examples:: _needs_tool_node
         :collapse:


   .. py:method:: _register_engine_in_registry() -> None

      Register the engine in EngineRegistry so other nodes can find it by name.


      .. autolink-examples:: _register_engine_in_registry
         :collapse:


   .. py:method:: _sync_fields_to_engine() -> None

      Sync convenience fields to engine.


      .. autolink-examples:: _sync_fields_to_engine
         :collapse:


   .. py:method:: add_prompt_template(name: str, template: langchain_core.prompts.ChatPromptTemplate | langchain_core.prompts.PromptTemplate) -> None

      Add a named prompt template to the engine.

      :param name: Unique name for the template
      :param template: The prompt template to store


      .. autolink-examples:: add_prompt_template
         :collapse:


   .. py:method:: add_system_message(message: str) -> None

      Add or update the system message.

      :param message: System message content


      .. autolink-examples:: add_system_message
         :collapse:


   .. py:method:: add_tool(tool: Any) -> None

      Add a tool to the agent.

      :param tool: Tool to add (LangChain tool, Pydantic model, or callable)


      .. autolink-examples:: add_tool
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the agent graph with V2 validation node + router system.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: clear_structured_output() -> None

      Clear structured output configuration.


      .. autolink-examples:: clear_structured_output
         :collapse:


   .. py:method:: clear_tools() -> None

      Clear all tools from the agent.


      .. autolink-examples:: clear_tools
         :collapse:


   .. py:method:: create_runnable(runnable_config: dict[str, Any] | None = None)

      Override to ensure state includes required fields.


      .. autolink-examples:: create_runnable
         :collapse:


   .. py:method:: create_with_tools(tools: list[Any], name: str | None = None, **kwargs)
      :classmethod:


      Create SimpleAgentV2 with tools.


      .. autolink-examples:: create_with_tools
         :collapse:


   .. py:method:: from_engine(engine: haive.core.engine.aug_llm.AugLLMConfig, name: str | None = None, **kwargs)
      :classmethod:


      Create SimpleAgentV2 from engine.


      .. autolink-examples:: from_engine
         :collapse:


   .. py:method:: get_active_template() -> str | None

      Get the name of the currently active template.


      .. autolink-examples:: get_active_template
         :collapse:


   .. py:method:: get_configuration_summary() -> dict[str, Any]

      Get a summary of current agent configuration.


      .. autolink-examples:: get_configuration_summary
         :collapse:


   .. py:method:: get_structured_output_model() -> type[pydantic.BaseModel] | None

      Get current structured output model.


      .. autolink-examples:: get_structured_output_model
         :collapse:


   .. py:method:: get_tool_routes() -> dict[str, str]

      Get tool routes from engine.


      .. autolink-examples:: get_tool_routes
         :collapse:


   .. py:method:: list_prompt_templates() -> list[str]

      List available template names.


      .. autolink-examples:: list_prompt_templates
         :collapse:


   .. py:method:: remove_prompt_template(name: str | None = None) -> None

      Remove a template or disable the active one.

      :param name: Template name to remove. If None, disables active template.


      .. autolink-examples:: remove_prompt_template
         :collapse:


   .. py:method:: remove_tool(tool: Any) -> None

      Remove a tool from the agent.

      :param tool: Tool instance to remove


      .. autolink-examples:: remove_tool
         :collapse:


   .. py:method:: set_structured_output(model: type[pydantic.BaseModel], version: str = 'v2', include_instructions: bool = True) -> None

      Set structured output model.

      :param model: Pydantic model for structured output
      :param version: Version to use ("v1" or "v2")
      :param include_instructions: Whether to include format instructions


      .. autolink-examples:: set_structured_output
         :collapse:


   .. py:method:: setup_agent() -> None

      Custom setup that modifies the engine and regenerates schemas.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: use_prompt_template(name: str) -> None

      Switch to using a specific template.

      :param name: Name of the template to activate

      :raises ValueError: If template name not found


      .. autolink-examples:: use_prompt_template
         :collapse:


   .. py:method:: validate_engine_type(v) -> Any
      :classmethod:


      Ensure engine is AugLLMConfig.


      .. autolink-examples:: validate_engine_type
         :collapse:


   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: force_tool_use
      :type:  bool | None
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.models.llm.base.LLMConfig | None
      :value: None



   .. py:attribute:: max_tokens
      :type:  int | None
      :value: None



   .. py:attribute:: model_name
      :type:  str | None
      :value: None



   .. py:attribute:: output_parser_field
      :type:  str | None
      :value: None



   .. py:attribute:: parser_safety_net_mode
      :type:  str
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate | langchain_core.prompts.PromptTemplate | None
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: structured_output_version
      :type:  Literal['v1', 'v2'] | None
      :value: None



   .. py:attribute:: system_message
      :type:  str | None
      :value: None



   .. py:attribute:: temperature
      :type:  float | None
      :value: None



   .. py:attribute:: use_parser_safety_net
      :type:  bool
      :value: None



.. py:function:: has_tool_calls_v2(state: dict[str, Any]) -> bool

   Check if the last AI message has tool calls - V2 version.


   .. autolink-examples:: has_tool_calls_v2
      :collapse:

.. py:data:: logger

