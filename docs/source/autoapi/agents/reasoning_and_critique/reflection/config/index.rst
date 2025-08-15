agents.reasoning_and_critique.reflection.config
===============================================

.. py:module:: agents.reasoning_and_critique.reflection.config

.. autoapi-nested-parse::

   Configuration for the Reflection Agent.


   .. autolink-examples:: agents.reasoning_and_critique.reflection.config
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.reflection.config.logger


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.reflection.config.ReflectionAgentConfig
   agents.reasoning_and_critique.reflection.config.ReflectionConfig


Module Contents
---------------

.. py:class:: ReflectionAgentConfig

   Bases: :py:obj:`haive.agents.simple.config.SimpleAgentConfig`


   Configuration for an agent that uses reflection to improve responses.


   .. autolink-examples:: ReflectionAgentConfig
      :collapse:

   .. py:method:: from_aug_llm(aug_llm: haive.core.engine.aug_llm.AugLLMConfig, name: str | None = None, system_prompt: str | None = None, **kwargs) -> ReflectionAgentConfig
      :classmethod:


      Create a ReflectionAgentConfig from an existing AugLLMConfig.


      .. autolink-examples:: from_aug_llm
         :collapse:


   .. py:method:: from_scratch(system_prompt: str | None = None, model: str = 'gpt-4o', temperature: float = 0.7, name: str | None = None, **kwargs) -> ReflectionAgentConfig
      :classmethod:


      Create a ReflectionAgentConfig from scratch.


      .. autolink-examples:: from_scratch
         :collapse:


   .. py:attribute:: agent_output_model
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: evaluation_node_name
      :type:  str
      :value: None



   .. py:attribute:: improvement_node_name
      :type:  str
      :value: None



   .. py:attribute:: initial_node_name
      :type:  str
      :value: None



   .. py:attribute:: reflection
      :type:  ReflectionConfig
      :value: None



   .. py:attribute:: reflection_node_name
      :type:  str
      :value: None



   .. py:attribute:: reflection_output_model
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: search_node_name
      :type:  str
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



.. py:class:: ReflectionConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration specific to the reflection mechanism.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReflectionConfig
      :collapse:

   .. py:attribute:: auto_accept_threshold
      :type:  float | None
      :value: None



   .. py:attribute:: enabled
      :type:  bool
      :value: None



   .. py:attribute:: improvement_prompt_template
      :type:  str
      :value: None



   .. py:attribute:: max_reflection_rounds
      :type:  int
      :value: None



   .. py:attribute:: reflection_llm
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: reflection_prompt_template
      :type:  str
      :value: None



   .. py:attribute:: search_query_prompt_template
      :type:  str
      :value: None



   .. py:attribute:: use_search
      :type:  bool
      :value: None



.. py:data:: logger

