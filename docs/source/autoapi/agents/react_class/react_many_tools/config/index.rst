agents.react_class.react_many_tools.config
==========================================

.. py:module:: agents.react_class.react_many_tools.config


Classes
-------

.. autoapisummary::

   agents.react_class.react_many_tools.config.ReactManyToolsConfig


Module Contents
---------------

.. py:class:: ReactManyToolsConfig

   Bases: :py:obj:`haive.agents.react.react.config.ReactAgentConfig`


   Configuration for React Agent with many tools.

   Extends ReactAgentConfig with features for handling large numbers of tools
   and integrates with RAG capabilities.


   .. autolink-examples:: ReactManyToolsConfig
      :collapse:

   .. py:method:: ensure_valid_configuration() -> Any

      Validate the configuration.


      .. autolink-examples:: ensure_valid_configuration
         :collapse:


   .. py:attribute:: answer_generator
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: embeddings_model
      :type:  langchain_core.embeddings.Embeddings | None
      :value: None



   .. py:attribute:: max_tools_per_request
      :type:  int
      :value: None



   .. py:attribute:: rag_config
      :type:  haive.agents.rag.base.config.BaseRAGConfig | None
      :value: None



   .. py:attribute:: retriever_config
      :type:  haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.VectorStoreConfig | None
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: tool_categories
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: tool_filter_prompt
      :type:  str | None
      :value: None



   .. py:attribute:: tool_selection_mode
      :type:  Literal['semantic', 'categorical', 'keyword', 'auto']
      :value: None



   .. py:attribute:: use_rag
      :type:  bool
      :value: None



