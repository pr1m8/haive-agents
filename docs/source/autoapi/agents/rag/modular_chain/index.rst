agents.rag.modular_chain
========================

.. py:module:: agents.rag.modular_chain

.. autoapi-nested-parse::

   Modular RAG using ChainAgent.

   Build configurable RAG pipelines with modular components.


   .. autolink-examples:: agents.rag.modular_chain
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.modular_chain.ModularConfig
   agents.rag.modular_chain.RAGModule


Functions
---------

.. autoapisummary::

   agents.rag.modular_chain.create_comprehensive_modular_rag
   agents.rag.modular_chain.create_custom_modular_rag
   agents.rag.modular_chain.create_modular_rag
   agents.rag.modular_chain.create_simple_modular_rag


Module Contents
---------------

.. py:class:: ModularConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for modular RAG.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ModularConfig
      :collapse:

   .. py:attribute:: modules
      :type:  list[RAGModule]
      :value: None



   .. py:attribute:: quality_gates
      :type:  bool
      :value: None



   .. py:attribute:: routing_strategy
      :type:  Literal['sequential', 'conditional', 'parallel']
      :value: None



.. py:class:: RAGModule

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Available RAG modules.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGModule
      :collapse:

   .. py:attribute:: ANSWER_GENERATION
      :value: 'answer_generation'



   .. py:attribute:: ANSWER_VERIFICATION
      :value: 'answer_verification'



   .. py:attribute:: CONTEXT_RANKING
      :value: 'context_ranking'



   .. py:attribute:: DOCUMENT_FILTERING
      :value: 'document_filtering'



   .. py:attribute:: QUERY_EXPANSION
      :value: 'query_expansion'



   .. py:attribute:: RESPONSE_SYNTHESIS
      :value: 'response_synthesis'



.. py:function:: create_comprehensive_modular_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create a comprehensive modular RAG with all modules.


   .. autolink-examples:: create_comprehensive_modular_rag
      :collapse:

.. py:function:: create_custom_modular_rag(documents: list[langchain_core.documents.Document], modules: list[str], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create a custom modular RAG with specified modules.


   .. autolink-examples:: create_custom_modular_rag
      :collapse:

.. py:function:: create_modular_rag(documents: list[langchain_core.documents.Document], config: ModularConfig, llm_config: haive.core.models.llm.base.LLMConfig | None = None, name: str = 'Modular RAG') -> haive.agents.chain.ChainAgent

   Create a modular RAG system with configurable components.


   .. autolink-examples:: create_modular_rag
      :collapse:

.. py:function:: create_simple_modular_rag(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None) -> haive.agents.chain.ChainAgent

   Create a simple modular RAG with basic modules.


   .. autolink-examples:: create_simple_modular_rag
      :collapse:

