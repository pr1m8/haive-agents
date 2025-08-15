agents.research.storm.config
============================

.. py:module:: agents.research.storm.config


Classes
-------

.. autoapisummary::

   agents.research.storm.config.AzureLLMConfig
   agents.research.storm.config.BaseRetrieverConfig
   agents.research.storm.config.InterviewAgentConfig
   agents.research.storm.config.ResearchAgentConfig
   agents.research.storm.config.STORMAgentConfig
   agents.research.storm.config.SequenceAgentConfig
   agents.research.storm.config.VectorStoreConfig
   agents.research.storm.config.VectorStoreRetrieverConfig
   agents.research.storm.config.WritingAgentConfig


Module Contents
---------------

.. py:class:: AzureLLMConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Placeholder for AzureLLMConfig.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AzureLLMConfig
      :collapse:

   .. py:attribute:: model
      :type:  str
      :value: 'gpt-4o'



.. py:class:: BaseRetrieverConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Placeholder for BaseRetrieverConfig.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BaseRetrieverConfig
      :collapse:

   .. py:attribute:: name
      :type:  str
      :value: 'retriever'



.. py:class:: InterviewAgentConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Placeholder for InterviewAgentConfig.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: InterviewAgentConfig
      :collapse:

   .. py:method:: build_agent() -> Any

      Placeholder build method.


      .. autolink-examples:: build_agent
         :collapse:


   .. py:attribute:: llm_config
      :type:  Any | None
      :value: None



   .. py:attribute:: max_turns
      :type:  int
      :value: 5



   .. py:attribute:: name
      :type:  str
      :value: 'interview_agent'



   .. py:attribute:: num_perspectives
      :type:  int
      :value: 3



.. py:class:: ResearchAgentConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Placeholder for ResearchAgentConfig.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResearchAgentConfig
      :collapse:

   .. py:method:: build_agent() -> Any

      Placeholder build method.


      .. autolink-examples:: build_agent
         :collapse:


   .. py:attribute:: llm_config
      :type:  Any | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'research_agent'



   .. py:attribute:: topic
      :type:  str
      :value: ''



.. py:class:: STORMAgentConfig(**data)

   Bases: :py:obj:`SequenceAgentConfig`


   Configuration for the STORM agent - an orchestrator that coordinates research,.
   interviews, and writing to generate comprehensive Wikipedia-style articles.

   STORM follows these stages:
   1. Research: Generate initial outline and identify perspectives
   2. Interview: Conduct expert interviews for diverse insights
   3. Writing: Refine outline, write sections, and assemble final article

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: STORMAgentConfig
      :collapse:

   .. py:method:: _create_default_retriever_config()

      Create the default retriever configuration.


      .. autolink-examples:: _create_default_retriever_config
         :collapse:


   .. py:method:: _create_default_vector_store_config()

      Create the default vector store configuration.


      .. autolink-examples:: _create_default_vector_store_config
         :collapse:


   .. py:method:: _create_interview_agent_config()

      Create the interview agent configuration.


      .. autolink-examples:: _create_interview_agent_config
         :collapse:


   .. py:method:: _create_research_agent_config()

      Create the research agent configuration.


      .. autolink-examples:: _create_research_agent_config
         :collapse:


   .. py:method:: _create_storm_agent_sequence()

      Create the sequence of agents for the STORM workflow.


      .. autolink-examples:: _create_storm_agent_sequence
         :collapse:


   .. py:method:: _create_writing_agent_config()

      Create the writing agent configuration.


      .. autolink-examples:: _create_writing_agent_config
         :collapse:


   .. py:attribute:: default_agent_configs
      :value: False



   .. py:attribute:: fast_llm_config
      :type:  AzureLLMConfig
      :value: None



   .. py:attribute:: interview_agent_config
      :type:  InterviewAgentConfig
      :value: None



   .. py:attribute:: long_context_llm_config
      :type:  AzureLLMConfig
      :value: None



   .. py:attribute:: max_interview_turns
      :type:  int
      :value: None



   .. py:attribute:: num_perspectives
      :type:  int
      :value: None



   .. py:attribute:: research_agent_config
      :type:  ResearchAgentConfig
      :value: None



   .. py:attribute:: retriever_config
      :type:  BaseRetrieverConfig
      :value: None



   .. py:attribute:: topic
      :type:  str
      :value: None



   .. py:attribute:: vector_store_config
      :type:  VectorStoreConfig
      :value: None



   .. py:attribute:: writing_agent_config
      :type:  WritingAgentConfig
      :value: None



.. py:class:: SequenceAgentConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Placeholder for SequenceAgentConfig.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SequenceAgentConfig
      :collapse:

   .. py:attribute:: agent_configs
      :type:  list
      :value: None



   .. py:attribute:: default_agent_configs
      :type:  bool
      :value: True



   .. py:attribute:: name
      :type:  str
      :value: 'sequence_agent'



.. py:class:: VectorStoreConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Placeholder for VectorStoreConfig.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: VectorStoreConfig
      :collapse:

   .. py:attribute:: embedding_model
      :type:  Any | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'vector_store'



   .. py:attribute:: vector_store_provider
      :type:  str
      :value: 'InMemory'



.. py:class:: VectorStoreRetrieverConfig(/, **data: Any)

   Bases: :py:obj:`BaseRetrieverConfig`


   Placeholder for VectorStoreRetrieverConfig.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: VectorStoreRetrieverConfig
      :collapse:

   .. py:attribute:: k
      :type:  int
      :value: 4



   .. py:attribute:: search_type
      :type:  str
      :value: 'similarity'



   .. py:attribute:: vector_store_config
      :type:  Any | None
      :value: None



.. py:class:: WritingAgentConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Placeholder for WritingAgentConfig.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: WritingAgentConfig
      :collapse:

   .. py:method:: build_agent() -> Any

      Placeholder build method.


      .. autolink-examples:: build_agent
         :collapse:


   .. py:attribute:: llm_config
      :type:  Any | None
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: 'writing_agent'



   .. py:attribute:: retriever_config
      :type:  Any | None
      :value: None



