agents.rag.simple.enhanced_v3.agent
===================================

.. py:module:: agents.rag.simple.enhanced_v3.agent

.. autoapi-nested-parse::

   SimpleRAG V3 - Enhanced MultiAgent Implementation.

   This module implements SimpleRAG using Enhanced MultiAgent V3 with the pattern:
   SimpleRAG = EnhancedMultiAgent[RetrieverAgent, SimpleAnswerAgent]

   The implementation provides:
   - Type-safe agent composition
   - Performance tracking and optimization
   - Debug support and monitoring
   - Adaptive routing capabilities
   - Comprehensive state management

   .. rubric:: Examples

   Basic usage::

       rag = SimpleRAGV3.from_documents(
           documents=documents,
           embedding_config=embedding_config,
           performance_mode=True
       )

       result = await rag.arun("What is machine learning?")

   Advanced usage with monitoring::

       rag = SimpleRAGV3(
           name="qa_system",
           vector_store_config=vector_store_config,
           performance_mode=True,
           debug_mode=True,
           adaptation_rate=0.2
       )

       result = await rag.arun("Complex query")
       analysis = rag.analyze_agent_performance()


   .. autolink-examples:: agents.rag.simple.enhanced_v3.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.simple.enhanced_v3.agent.EnhancedSimpleRAG
   agents.rag.simple.enhanced_v3.agent.RAGAgentCollection
   agents.rag.simple.enhanced_v3.agent.SimpleRAGAgent


Classes
-------

.. autoapisummary::

   agents.rag.simple.enhanced_v3.agent.SimpleRAGV3


Module Contents
---------------

.. py:class:: SimpleRAGV3

   Bases: :py:obj:`haive.agents.multi.enhanced_multi_agent_v3.EnhancedMultiAgent`\ [\ :py:obj:`RAGAgentCollection`\ ]


   SimpleRAG V3 - Enhanced MultiAgent implementation.

   This class implements SimpleRAG using Enhanced MultiAgent V3 with the pattern:
   SimpleRAGV3 = EnhancedMultiAgent[RetrieverAgent, SimpleAnswerAgent]

   The sequential execution flow is:
   1. RetrieverAgent: Retrieves relevant documents from vector store
   2. SimpleAnswerAgent: Generates answer using retrieved documents

   Key Features:
       - Type-safe agent composition using Enhanced MultiAgent V3
       - Performance tracking and adaptive optimization
       - Debug support with comprehensive monitoring
       - Automatic state management and transfer
       - Factory methods for easy creation
       - Backward compatibility with existing SimpleRAG

   State Management:
       Uses SimpleRAGState when enhanced features are enabled,
       falls back to EnhancedMultiAgentState for basic usage.

   .. rubric:: Examples

   From documents::

       rag = SimpleRAGV3.from_documents(
           documents=my_documents,
           embedding_config=embedding_config,
           performance_mode=True,
           debug_mode=True
       )

       result = await rag.arun("What is machine learning?")

   From vector store::

       rag = SimpleRAGV3.from_vectorstore(
           vector_store_config=vs_config,
           llm_config=AugLLMConfig(temperature=0.7),
           performance_mode=True
       )

   With structured output::

       class QAResponse(BaseModel):
           answer: str
           sources: List[str]
           confidence: float

       rag = SimpleRAGV3(
           name="structured_rag",
           vector_store_config=vs_config,
           structured_output_model=QAResponse,
           performance_mode=True
       )


   .. autolink-examples:: SimpleRAGV3
      :collapse:

   .. py:method:: __repr__() -> str

      String representation showing Enhanced MultiAgent V3 structure.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: arun(input_data: str | dict[str, Any], debug: bool = False, **kwargs) -> Any
      :async:


      Execute RAG pipeline using Enhanced MultiAgent V3 sequential execution.

      This leverages the Enhanced MultiAgent V3 infrastructure for:
      - Performance tracking and optimization
      - Debug support and monitoring
      - Adaptive routing capabilities
      - Comprehensive state management

      :param input_data: Query string or structured input with 'query' field
      :param debug: Enable debug logging and detailed output
      :param \*\*kwargs: Additional execution parameters

      :returns: Generated response from the answer generation agent

      :raises ValueError: If input validation fails
      :raises RuntimeError: If pipeline execution fails


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: ensure_agents_is_list(values: dict) -> dict
      :classmethod:


      Ensure agents field starts as an empty list for our List type.


      .. autolink-examples:: ensure_agents_is_list
         :collapse:


   .. py:method:: from_documents(documents: list[langchain_core.documents.Document], embedding_config: Any, llm_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, name: str | None = None, **kwargs) -> SimpleRAGV3
      :classmethod:


      Create SimpleRAG V3 from a list of documents.

      :param documents: List of documents to create vector store from
      :param embedding_config: Embedding configuration for vector store
      :param llm_config: LLM configuration for answer generation
      :param name: Name for the RAG system
      :param \*\*kwargs: Additional configuration parameters

      :returns: Configured SimpleRAGV3 instance

      .. rubric:: Examples

      Basic usage::

          rag = SimpleRAGV3.from_documents(
              documents=my_documents,
              embedding_config=embedding_config
          )

      With enhanced features::

          rag = SimpleRAGV3.from_documents(
              documents=my_documents,
              embedding_config=embedding_config,
              llm_config=AugLLMConfig(temperature=0.3),
              performance_mode=True,
              debug_mode=True,
              top_k=10
          )


      .. autolink-examples:: from_documents
         :collapse:


   .. py:method:: from_vectorstore(vector_store_config: haive.core.engine.vectorstore.VectorStoreConfig, llm_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, name: str | None = None, **kwargs) -> SimpleRAGV3
      :classmethod:


      Create SimpleRAG V3 from existing vector store configuration.

      :param vector_store_config: Vector store configuration
      :param llm_config: LLM configuration for answer generation
      :param name: Name for the RAG system
      :param \*\*kwargs: Additional configuration parameters

      :returns: Configured SimpleRAGV3 instance

      .. rubric:: Examples

      Basic usage::

          rag = SimpleRAGV3.from_vectorstore(
              vector_store_config=vs_config,
              llm_config=AugLLMConfig()
          )

      With monitoring::

          rag = SimpleRAGV3.from_vectorstore(
              vector_store_config=vs_config,
              llm_config=AugLLMConfig(temperature=0.5),
              performance_mode=True,
              adaptation_rate=0.2
          )


      .. autolink-examples:: from_vectorstore
         :collapse:


   .. py:method:: generate_answer(query: str, documents: list[langchain_core.documents.Document], **kwargs) -> Any
      :async:


      Generate answer using the answer generation agent.

      :param query: Original query
      :param documents: Retrieved documents for context
      :param \*\*kwargs: Additional generation parameters

      :returns: Generated answer (format depends on structured_output_model)


      .. autolink-examples:: generate_answer
         :collapse:


   .. py:method:: get_answer_agent() -> agents.rag.simple.enhanced_v3.answer_generator_agent.SimpleAnswerAgent

      Get the answer generation agent.


      .. autolink-examples:: get_answer_agent
         :collapse:


   .. py:method:: get_rag_info() -> dict[str, Any]

      Get comprehensive information about the RAG configuration.


      .. autolink-examples:: get_rag_info
         :collapse:


   .. py:method:: get_retriever_agent() -> agents.rag.simple.enhanced_v3.retriever_agent.RetrieverAgent

      Get the retriever agent.


      .. autolink-examples:: get_retriever_agent
         :collapse:


   .. py:method:: retrieve_documents(query: str, k: int | None = None, score_threshold: float | None = None, **kwargs) -> dict[str, Any]
      :async:


      Retrieve documents using the retriever agent.

      :param query: Query string for retrieval
      :param k: Number of documents to retrieve (defaults to self.top_k)
      :param score_threshold: Minimum similarity score (defaults to self.similarity_threshold)
      :param \*\*kwargs: Additional retrieval parameters

      :returns: Retrieval result with documents and metadata


      .. autolink-examples:: retrieve_documents
         :collapse:


   .. py:method:: setup_rag_pipeline() -> SimpleRAGV3

      Setup the RAG pipeline with RetrieverAgent and SimpleAnswerAgent.


      .. autolink-examples:: setup_rag_pipeline
         :collapse:


   .. py:method:: validate_citation_style(v: str) -> str
      :classmethod:


      Validate citation style.


      .. autolink-examples:: validate_citation_style
         :collapse:


   .. py:attribute:: citation_style
      :type:  str
      :value: None



   .. py:attribute:: context_template
      :type:  str | None
      :value: None



   .. py:attribute:: include_citations
      :type:  bool
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: max_context_length
      :type:  int
      :value: None



   .. py:attribute:: similarity_threshold
      :type:  float
      :value: None



   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel] | None
      :value: None



   .. py:attribute:: system_prompt_template
      :type:  str | None
      :value: None



   .. py:attribute:: top_k
      :type:  int
      :value: None



   .. py:attribute:: vector_store_config
      :type:  haive.core.engine.vectorstore.VectorStoreConfig
      :value: None



.. py:data:: EnhancedSimpleRAG

.. py:data:: RAGAgentCollection

.. py:data:: SimpleRAGAgent

