agents.document_modifiers.complex_extraction.config
===================================================

.. py:module:: agents.document_modifiers.complex_extraction.config


Classes
-------

.. autoapisummary::

   agents.document_modifiers.complex_extraction.config.ComplexExtractionAgentConfig


Module Contents
---------------

.. py:class:: ComplexExtractionAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for the complex extraction agent.

   This agent handles the extraction of complex structured data from text
   using a validation and retry mechanism with optional JSONPatch corrections.


   .. autolink-examples:: ComplexExtractionAgentConfig
      :collapse:

   .. py:attribute:: extraction_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: force_tool_choice
      :type:  bool
      :value: None



   .. py:attribute:: input_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: max_retries
      :type:  int
      :value: None



   .. py:attribute:: output_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: parse_pydantic
      :type:  bool
      :value: None



   .. py:attribute:: runnable_config
      :type:  haive.core.engine.agent.agent.RunnableConfig
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: system_prompt
      :type:  str
      :value: None



   .. py:attribute:: use_jsonpatch
      :type:  bool
      :value: None



