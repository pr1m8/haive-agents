agents.simple.config
====================

.. py:module:: agents.simple.config

.. autoapi-nested-parse::

   Configuration for SimpleAgent with comprehensive schema handling.

   This module defines the configuration class for SimpleAgent with explicit
   input/output schema support, schema composition integration, and improved
   mapping capabilities.


   .. autolink-examples:: agents.simple.config
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/simple/config/v2/index


Attributes
----------

.. autoapisummary::

   agents.simple.config.logger


Classes
-------

.. autoapisummary::

   agents.simple.config.SimpleAgentConfig


Module Contents
---------------

.. py:class:: SimpleAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for a simple single-node agent with comprehensive schema handling.

   This config supports:
   - Explicit input/output schemas
   - Auto-derived state schema
   - Structured output models
   - Intelligent input/output mappings


   .. autolink-examples:: SimpleAgentConfig
      :collapse:

   .. py:method:: from_aug_llm(aug_llm: haive.core.engine.aug_llm.AugLLMConfig, name: str | None = None, id: str | None = None, input_schema: type[pydantic.BaseModel] | None = None, output_schema: type[pydantic.BaseModel] | None = None, state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> SimpleAgentConfig
      :classmethod:


      Create a SimpleAgentConfig from an existing AugLLMConfig.

      :param aug_llm: Existing AugLLMConfig to use
      :param name: Optional agent name
      :param id: Optional unique identifier
      :param input_schema: Optional explicit input schema
      :param output_schema: Optional explicit output schema
      :param state_schema: Optional explicit state schema
      :param \*\*kwargs: Additional kwargs for the config

      :returns: SimpleAgentConfig instance


      .. autolink-examples:: from_aug_llm
         :collapse:


   .. py:method:: from_scratch(system_prompt: str = 'You are a helpful assistant.', model: str = 'gpt-4o', temperature: float = 0.7, structured_output_model: type[pydantic.BaseModel] | None = None, name: str | None = None, id: str | None = None, input_schema: type[pydantic.BaseModel] | None = None, output_schema: type[pydantic.BaseModel] | None = None, state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> SimpleAgentConfig
      :classmethod:


      Create a SimpleAgentConfig from scratch with a new AugLLMConfig.

      :param system_prompt: System prompt for the LLM
      :param model: Model identifier to use
      :param temperature: Generation temperature
      :param structured_output_model: Optional model for structured outputs
      :param name: Optional agent name
      :param id: Optional unique identifier
      :param input_schema: Optional explicit input schema
      :param output_schema: Optional explicit output schema
      :param state_schema: Optional explicit state schema
      :param \*\*kwargs: Additional kwargs for the config

      :returns: SimpleAgentConfig instance


      .. autolink-examples:: from_scratch
         :collapse:


   .. py:method:: validate_engine(v) -> Any
      :classmethod:


      Ensure engine is an AugLLMConfig instance.


      .. autolink-examples:: validate_engine
         :collapse:


   .. py:method:: validate_mappings(v, info) -> Any
      :classmethod:


      Validate mappings if provided.


      .. autolink-examples:: validate_mappings
         :collapse:


   .. py:method:: with_structured_output(output_model: type[pydantic.BaseModel], system_prompt: str | None = None, model: str = 'gpt-4o', temperature: float = 0.2, name: str | None = None, **kwargs) -> SimpleAgentConfig
      :classmethod:


      Create a SimpleAgentConfig with structured output capabilities.

      :param output_model: Pydantic model for structured output
      :param system_prompt: Optional system prompt (default derived from model)
      :param model: Model identifier
      :param temperature: Generation temperature (lower for structured outputs)
      :param name: Optional agent name
      :param \*\*kwargs: Additional kwargs for the config

      :returns: SimpleAgentConfig with structured output capability


      .. autolink-examples:: with_structured_output
         :collapse:


   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: input_mapping
      :type:  dict[str, str] | None
      :value: None



   .. py:attribute:: input_schema
      :type:  type[pydantic.BaseModel] | type[haive.core.schema.state_schema.StateSchema] | None
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: node_name
      :type:  str
      :value: None



   .. py:attribute:: output_mapping
      :type:  dict[str, str] | None
      :value: None



   .. py:attribute:: output_schema
      :type:  type[pydantic.BaseModel] | type[haive.core.schema.state_schema.StateSchema] | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.core.schema.state_schema.StateSchema] | type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



.. py:data:: logger

