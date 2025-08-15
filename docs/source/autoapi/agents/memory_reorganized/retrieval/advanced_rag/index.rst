agents.memory_reorganized.retrieval.advanced_rag
================================================

.. py:module:: agents.memory_reorganized.retrieval.advanced_rag

.. autoapi-nested-parse::

   Advanced RAG Memory Agent with multi-stage retrieval and reranking.

   This implementation provides state-of-the-art RAG capabilities:
   1. Multi-stage retrieval: dense → sparse → reranking
   2. Hybrid search combining vector, key, and graph
   3. Query decomposition for complex questions
   4. Memory-augmented generation with citations
   5. Adaptive retrieval based on query complexity


   .. autolink-examples:: agents.memory_reorganized.retrieval.advanced_rag
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.retrieval.advanced_rag.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.retrieval.advanced_rag.AdvancedRAGConfig
   agents.memory_reorganized.retrieval.advanced_rag.AdvancedRAGMemoryAgent
   agents.memory_reorganized.retrieval.advanced_rag.QueryComplexity
   agents.memory_reorganized.retrieval.advanced_rag.RetrievalStrategy


Functions
---------

.. autoapisummary::

   agents.memory_reorganized.retrieval.advanced_rag.create_conversational_memory_agent
   agents.memory_reorganized.retrieval.advanced_rag.create_research_memory_agent
   agents.memory_reorganized.retrieval.advanced_rag.example_advanced_rag_usage


Module Contents
---------------

.. py:class:: AdvancedRAGConfig

   Configuration for Advanced RAG Memory Agent.


   .. autolink-examples:: AdvancedRAGConfig
      :collapse:

   .. py:method:: __post_init__()


   .. py:attribute:: bm25_b
      :type:  float
      :value: 0.75



   .. py:attribute:: bm25_k1
      :type:  float
      :value: 1.2



   .. py:attribute:: citation_format
      :type:  str
      :value: '[{doc_id}]'



   .. py:attribute:: dense_weight
      :type:  float
      :value: 0.6



   .. py:attribute:: embedding_model
      :type:  str
      :value: 'openai'



   .. py:attribute:: enable_bm25
      :type:  bool
      :value: True



   .. py:attribute:: enable_query_expansion
      :type:  bool
      :value: True



   .. py:attribute:: enable_reranking
      :type:  bool
      :value: True



   .. py:attribute:: enable_time_weighting
      :type:  bool
      :value: True



   .. py:attribute:: importance_boost
      :type:  float
      :value: 1.2



   .. py:attribute:: include_citations
      :type:  bool
      :value: True



   .. py:attribute:: k_final
      :type:  int
      :value: 5



   .. py:attribute:: k_initial
      :type:  int
      :value: 20



   .. py:attribute:: llm_config
      :type:  langchain.retrievers.document_compressors.Optional[haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: max_context_length
      :type:  int
      :value: 4000



   .. py:attribute:: max_query_variations
      :type:  int
      :value: 3



   .. py:attribute:: memory_store_path
      :type:  langchain.retrievers.document_compressors.Optional[str]
      :value: None



   .. py:attribute:: recency_decay
      :type:  float
      :value: 0.01



   .. py:attribute:: rerank_top_k
      :type:  int
      :value: 10



   .. py:attribute:: reranker_model
      :type:  str
      :value: 'BAAI/bge-reranker-large'



   .. py:attribute:: sparse_weight
      :type:  float
      :value: 0.4



   .. py:attribute:: strategy
      :type:  RetrievalStrategy


   .. py:attribute:: user_id
      :type:  str
      :value: 'default_user'



   .. py:attribute:: vector_store_type
      :type:  str
      :value: 'faiss'



.. py:class:: AdvancedRAGMemoryAgent(config: AdvancedRAGConfig)

   Advanced RAG Memory Agent with multi-stage retrieval.

   This agent implements state-of-the-art retrieval-augmented generation with
   sophisticated memory management capabilities.


   .. autolink-examples:: AdvancedRAGMemoryAgent
      :collapse:

   .. py:method:: _apply_importance_boost(docs: list[langchain_core.documents.Document]) -> list[langchain_core.documents.Document]

      Boost important documents in ranking.


      .. autolink-examples:: _apply_importance_boost
         :collapse:


   .. py:method:: _create_new_vector_store(embeddings)

      Create new vector store.


      .. autolink-examples:: _create_new_vector_store
         :collapse:


   .. py:method:: _init_contextual_retriever()

      Initialize contextual compression retriever.


      .. autolink-examples:: _init_contextual_retriever
         :collapse:


   .. py:method:: _init_generation_components()

      Initialize components for generation.


      .. autolink-examples:: _init_generation_components
         :collapse:


   .. py:method:: _init_reranking_retriever()

      Initialize reranking retriever.


      .. autolink-examples:: _init_reranking_retriever
         :collapse:


   .. py:method:: _init_retrievers()

      Initialize all retrieval components.


      .. autolink-examples:: _init_retrievers
         :collapse:


   .. py:method:: _init_vector_store()

      Initialize vector store for dense retrieval.


      .. autolink-examples:: _init_vector_store
         :collapse:


   .. py:method:: add_memory(content: str, metadata: dict[str, Any] | None = None, importance: str = 'normal') -> dict[str, Any]
      :async:


      Add new memory to the system.


      .. autolink-examples:: add_memory
         :collapse:


   .. py:method:: analyze_query_complexity(query: str) -> QueryComplexity

      Analyze query complexity to choose optimal strategy.


      .. autolink-examples:: analyze_query_complexity
         :collapse:


   .. py:method:: choose_retrieval_strategy(query: str, complexity: QueryComplexity) -> RetrievalStrategy

      Choose optimal retrieval strategy based on query and complexity.


      .. autolink-examples:: choose_retrieval_strategy
         :collapse:


   .. py:method:: generate_with_citations(query: str, retrieved_docs: list[langchain_core.documents.Document], include_citations: langchain.retrievers.document_compressors.Optional[bool] = None) -> dict[str, Any]
      :async:


      Generate response with citations.


      .. autolink-examples:: generate_with_citations
         :collapse:


   .. py:method:: get_memory_analytics() -> dict[str, Any]
      :async:


      Get comprehensive analytics about memory usage.


      .. autolink-examples:: get_memory_analytics
         :collapse:


   .. py:method:: query_memory(query: str, strategy: langchain.retrievers.document_compressors.Optional[RetrievalStrategy] = None, include_analysis: bool = True) -> dict[str, Any]
      :async:


      Query memory with advanced RAG capabilities.


      .. autolink-examples:: query_memory
         :collapse:


   .. py:method:: retrieve_documents(query: str, strategy: langchain.retrievers.document_compressors.Optional[RetrievalStrategy] = None, k: langchain.retrievers.document_compressors.Optional[int] = None) -> list[langchain_core.documents.Document]
      :async:


      Retrieve documents using specified strategy.


      .. autolink-examples:: retrieve_documents
         :collapse:


   .. py:method:: save_memory_store(path: langchain.retrievers.document_compressors.Optional[str] = None)

      Save the vector store and metadata.


      .. autolink-examples:: save_memory_store
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: document_metadata
      :type:  dict[str, dict[str, Any]]


   .. py:attribute:: documents
      :type:  list[langchain_core.documents.Document]
      :value: []



   .. py:attribute:: logger


   .. py:attribute:: query_history
      :type:  list[dict[str, Any]]
      :value: []



.. py:class:: QueryComplexity

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Query complexity levels.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryComplexity
      :collapse:

   .. py:attribute:: COMPLEX
      :value: 'complex'



   .. py:attribute:: MEDIUM
      :value: 'medium'



   .. py:attribute:: SIMPLE
      :value: 'simple'



.. py:class:: RetrievalStrategy

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Different retrieval strategies available.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RetrievalStrategy
      :collapse:

   .. py:attribute:: ADAPTIVE
      :value: 'adaptive'



   .. py:attribute:: CONTEXTUAL
      :value: 'contextual'



   .. py:attribute:: DENSE_ONLY
      :value: 'dense_only'



   .. py:attribute:: HYBRID
      :value: 'hybrid'



   .. py:attribute:: MULTI_QUERY
      :value: 'multi_query'



   .. py:attribute:: RERANKED
      :value: 'reranked'



   .. py:attribute:: SPARSE_ONLY
      :value: 'sparse_only'



.. py:function:: create_conversational_memory_agent() -> AdvancedRAGMemoryAgent
   :async:


   Create a conversation-focused memory agent.


   .. autolink-examples:: create_conversational_memory_agent
      :collapse:

.. py:function:: create_research_memory_agent() -> AdvancedRAGMemoryAgent
   :async:


   Create a research-focused memory agent.


   .. autolink-examples:: create_research_memory_agent
      :collapse:

.. py:function:: example_advanced_rag_usage()
   :async:


   Example of using Advanced RAG Memory Agent.


   .. autolink-examples:: example_advanced_rag_usage
      :collapse:

.. py:data:: logger

