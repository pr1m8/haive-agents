agents.simple.agent_with_validation
===================================

.. py:module:: agents.simple.agent_with_validation


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/simple/agent_with_validation/v2/index


Attributes
----------

.. autoapisummary::

   agents.simple.agent_with_validation.logger


Classes
-------

.. autoapisummary::

   agents.simple.agent_with_validation.SimpleAgentWithValidation


Functions
---------

.. autoapisummary::

   agents.simple.agent_with_validation.has_tool_calls
   agents.simple.agent_with_validation.upgrade_simple_agent_with_validation


Module Contents
---------------

.. py:class:: SimpleAgentWithValidation

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   SimpleAgent with integrated StateUpdatingValidationNode.

   This agent demonstrates how to properly integrate the StateUpdatingValidationNode
   with the existing agent architecture, replacing placeholder nodes with actual
   validation and routing functionality.

   Key improvements over SimpleAgent:
   - Uses StateUpdatingValidationNode instead of placeholder
   - Provides both state updating and routing capabilities
   - Integrates with state schema for validation persistence
   - Supports different validation modes (STRICT, PARTIAL, PERMISSIVE)


   .. autolink-examples:: SimpleAgentWithValidation
      :collapse:

   .. py:method:: __repr__() -> str


   .. py:method:: _create_validation_node() -> haive.core.graph.node.state_updating_validation_node.StateUpdatingValidationNode

      Create the StateUpdatingValidationNode with proper configuration.


      .. autolink-examples:: _create_validation_node
         :collapse:


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


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the agent graph with StateUpdatingValidationNode integration.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_permissive_validation(engine: haive.core.engine.aug_llm.AugLLMConfig, name: str | None = None, **kwargs)
      :classmethod:


      Create agent with permissive validation mode.


      .. autolink-examples:: create_permissive_validation
         :collapse:


   .. py:method:: create_runnable(runnable_config: haive.core.graph.node.state_updating_validation_node.Dict[str, Any] = None) -> Any

      Override to ensure state is properly initialized.


      .. autolink-examples:: create_runnable
         :collapse:


   .. py:method:: create_strict_validation(engine: haive.core.engine.aug_llm.AugLLMConfig, name: str | None = None, **kwargs)
      :classmethod:


      Create agent with strict validation mode.


      .. autolink-examples:: create_strict_validation
         :collapse:


   .. py:method:: create_with_tools(tools: list[Any], name: str | None = None, **kwargs)
      :classmethod:


      Create SimpleAgentWithValidation with tools.


      .. autolink-examples:: create_with_tools
         :collapse:


   .. py:method:: from_engine(engine: haive.core.engine.aug_llm.AugLLMConfig, name: str | None = None, **kwargs)
      :classmethod:


      Create SimpleAgentWithValidation from engine.


      .. autolink-examples:: from_engine
         :collapse:


   .. py:method:: get_tool_routes() -> dict[str, str]

      Get tool routes from engine.


      .. autolink-examples:: get_tool_routes
         :collapse:


   .. py:method:: setup_agent() -> None

      Custom setup that modifies the engine and regenerates schemas.


      .. autolink-examples:: setup_agent
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



   .. py:attribute:: output_parser
      :type:  langchain_core.output_parsers.base.BaseOutputParser | None
      :value: None



   .. py:attribute:: output_parser_field
      :type:  str | None
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate | langchain_core.prompts.PromptTemplate | None
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: structured_output_version
      :type:  int | str | None
      :value: None



   .. py:attribute:: system_message
      :type:  str | None
      :value: None



   .. py:attribute:: temperature
      :type:  float | None
      :value: None



   .. py:attribute:: tools
      :type:  list[Any] | None
      :value: None



   .. py:attribute:: track_error_tools
      :type:  bool
      :value: None



   .. py:attribute:: update_validation_messages
      :type:  bool
      :value: None



   .. py:attribute:: validation_mode
      :type:  haive.core.graph.node.state_updating_validation_node.ValidationMode
      :value: None



.. py:function:: has_tool_calls(state: haive.core.graph.node.state_updating_validation_node.Dict[str, Any]) -> bool

   Check if the last AI message has tool calls.


   .. autolink-examples:: has_tool_calls
      :collapse:

.. py:function:: upgrade_simple_agent_with_validation(simple_agent: SimpleAgent) -> SimpleAgentWithValidation

   Upgrade a SimpleAgent to use StateUpdatingValidationNode.


   .. autolink-examples:: upgrade_simple_agent_with_validation
      :collapse:

.. py:data:: logger

