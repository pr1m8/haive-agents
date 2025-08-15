agents.rag.base.config
======================

.. py:module:: agents.rag.base.config


Classes
-------

.. autoapisummary::

   agents.rag.base.config.BaseRAGConfig


Module Contents
---------------

.. py:class:: BaseRAGConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for a basic RAG agent.


   .. autolink-examples:: BaseRAGConfig
      :collapse:

   .. py:method:: convert_vector_store_to_retriever(data: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Pre-validation converter from VectorStoreConfig to RetrieverConfig.
      This runs before Pydantic validation, ensuring the type checking works.


      .. autolink-examples:: convert_vector_store_to_retriever
         :collapse:


   .. py:method:: setup_engine() -> BaseRAGConfig

      After validation, set the engine property to the retriever_config.
      This ensures the agent can use the retriever directly.


      .. autolink-examples:: setup_engine
         :collapse:


   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: input_schema
      :type:  type[pydantic.BaseModel]


   .. py:attribute:: model_config


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: output_schema
      :type:  type[pydantic.BaseModel]


   .. py:attribute:: retriever_config
      :type:  haive.core.engine.retriever.BaseRetrieverConfig | haive.core.engine.vectorstore.VectorStoreConfig
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]


