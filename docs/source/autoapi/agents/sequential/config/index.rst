agents.sequential.config
========================

.. py:module:: agents.sequential.config

.. autoapi-nested-parse::

   Configuration for SequentialAgent that connects components in a linear workflow.

   from typing import Any
   This module defines the configuration class for SequentialAgent, which
   automates the process of connecting multiple engine components in a sequence.


   .. autolink-examples:: agents.sequential.config
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.sequential.config.logger


Classes
-------

.. autoapisummary::

   agents.sequential.config.SequentialAgentConfig
   agents.sequential.config.StepConfig


Functions
---------

.. autoapisummary::

   agents.sequential.config.build_agent
   agents.sequential.config.from_aug_llms
   agents.sequential.config.from_components
   agents.sequential.config.from_steps
   agents.sequential.config.get_step_by_name
   agents.sequential.config.setup_components
   agents.sequential.config.validate_steps


Module Contents
---------------

.. py:class:: SequentialAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


   Configuration for a SequentialAgent that connects components linearly.

   This agent automates the process of connecting engine components in a sequence,
   handling the data flow between them through the state schema.

   Components can be any engine types, particularly AugLLMConfig instances
   for chaining language model steps.


   .. autolink-examples:: SequentialAgentConfig
      :collapse:

   .. py:method:: build_agent() -> Any

      Build and return a SequentialAgent instance.


      .. autolink-examples:: build_agent
         :collapse:


   .. py:method:: from_aug_llms(aug_llms: list[haive.core.engine.aug_llm.AugLLMConfig], name: str | None = None, id: str | None = None, state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> SequentialAgentConfig
      :classmethod:


      Create a SequentialAgentConfig from a list of AugLLMConfig instances.

      Convenience method for the common case of chaining LLM steps.

      :param aug_llms: List of AugLLMConfig instances
      :param name: Optional agent name
      :param id: Optional unique identifier
      :param state_schema: Optional state schema
      :param \*\*kwargs: Additional configuration parameters

      :returns: SequentialAgentConfig instance


      .. autolink-examples:: from_aug_llms
         :collapse:


   .. py:method:: from_components(components: list[Any], name: str | None = None, id: str | None = None, state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, step_names: list[str] | None = None, **kwargs) -> SequentialAgentConfig
      :classmethod:


      Create a SequentialAgentConfig from a list of components.

      This automatically creates step configurations for each component.

      :param components: List of components to use as steps (AugLLMConfig, Engine, etc.)
      :param name: Optional agent name
      :param id: Optional unique identifier
      :param state_schema: Optional state schema
      :param step_names: Optional list of step names (must match length of components)
      :param \*\*kwargs: Additional configuration parameters

      :returns: SequentialAgentConfig instance


      .. autolink-examples:: from_components
         :collapse:


   .. py:method:: from_steps(steps: list[StepConfig], name: str | None = None, id: str | None = None, entry_point: str | None = None, state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> SequentialAgentConfig
      :classmethod:


      Create a SequentialAgentConfig from a list of steps.

      :param steps: List of step configurations
      :param name: Optional agent name
      :param id: Optional unique identifier
      :param entry_point: Optional entry point step name
      :param state_schema: Optional state schema
      :param \*\*kwargs: Additional configuration parameters

      :returns: SequentialAgentConfig instance


      .. autolink-examples:: from_steps
         :collapse:


   .. py:method:: get_step_by_name(name: str) -> StepConfig | None

      Get a step configuration by name.


      .. autolink-examples:: get_step_by_name
         :collapse:


   .. py:method:: setup_components() -> SequentialAgentConfig

      Collect all step components into the components list for schema derivation.


      .. autolink-examples:: setup_components
         :collapse:


   .. py:method:: validate_steps(v) -> Any
      :classmethod:


      Ensure we have at least one step.


      .. autolink-examples:: validate_steps
         :collapse:


   .. py:attribute:: components
      :type:  list[Any]
      :value: None



   .. py:attribute:: entry_point
      :type:  str | None
      :value: None



   .. py:attribute:: input_schema
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: output_schema
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.core.schema.state_schema.StateSchema] | None
      :value: None



   .. py:attribute:: steps
      :type:  list[StepConfig]
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



.. py:class:: StepConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for a single step in a sequential workflow.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepConfig
      :collapse:

   .. py:attribute:: component
      :type:  Any
      :value: None



   .. py:attribute:: description
      :type:  str | None
      :value: None



   .. py:attribute:: input_mapping
      :type:  dict[str, str] | None
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: output_mapping
      :type:  dict[str, str] | None
      :value: None



.. py:function:: build_agent(config: SequentialAgentConfig) -> haive.agents.sequential.agent.SequentialAgent

   Build a SequentialAgent from configuration.


   .. autolink-examples:: build_agent
      :collapse:

.. py:function:: from_aug_llms(aug_llms: list[haive.core.engine.aug_llm.AugLLMConfig], name: str | None = None, id: str | None = None, state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> SequentialAgentConfig

   Create a SequentialAgentConfig from a list of AugLLMConfig instances.


   .. autolink-examples:: from_aug_llms
      :collapse:

.. py:function:: from_components(components: list[Any], name: str | None = None, id: str | None = None, state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> SequentialAgentConfig

   Create a SequentialAgentConfig from a list of components.


   .. autolink-examples:: from_components
      :collapse:

.. py:function:: from_steps(steps: list[StepConfig], name: str | None = None, id: str | None = None, entry_point: str | None = None, state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> SequentialAgentConfig

   Create a SequentialAgentConfig from a list of steps.


   .. autolink-examples:: from_steps
      :collapse:

.. py:function:: get_step_by_name(config: SequentialAgentConfig, name: str) -> StepConfig | None

   Get a step configuration by name.


   .. autolink-examples:: get_step_by_name
      :collapse:

.. py:function:: setup_components(config: SequentialAgentConfig) -> SequentialAgentConfig

   Setup components for a configuration.


   .. autolink-examples:: setup_components
      :collapse:

.. py:function:: validate_steps(steps: list[StepConfig]) -> bool

   Validate that steps list is not empty.


   .. autolink-examples:: validate_steps
      :collapse:

.. py:data:: logger

