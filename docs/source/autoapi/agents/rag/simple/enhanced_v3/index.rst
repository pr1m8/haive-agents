agents.rag.simple.enhanced_v3
=============================

.. py:module:: agents.rag.simple.enhanced_v3

.. autoapi-nested-parse::

   Enhanced SimpleRAG V3 using Enhanced MultiAgent V3.

   This package provides SimpleRAG implementation using the Enhanced MultiAgent V3 pattern
   with performance tracking, debug support, and adaptive routing capabilities.

   Classes:
       - SimpleRAGV3: Main SimpleRAG implementation with Enhanced MultiAgent V3
       - RetrieverAgent: Specialized agent for document retrieval
       - AnswerGeneratorAgent: Specialized agent for answer generation
       - SimpleRAGState: Enhanced state schema for SimpleRAG pipeline

   .. rubric:: Examples

   Basic usage::

       from haive.agents.rag.simple.enhanced_v3 import SimpleRAGV3

       rag = SimpleRAGV3.from_documents(
           documents=documents,
           embedding_config=embedding_config,
           performance_mode=True
       )

       result = await rag.arun("What is machine learning?")

   With performance tracking::

       rag = SimpleRAGV3(
           name="qa_system",
           vector_store_config=vs_config,
           performance_mode=True,
           debug_mode=True
       )

       result = await rag.arun("Complex query")

       # Monitor performance
       analysis = rag.analyze_agent_performance()
       print(f"Retriever success rate: {analysis['agents']['retriever']['success_rate']}")


   .. autolink-examples:: agents.rag.simple.enhanced_v3
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/rag/simple/enhanced_v3/agent/index
   /autoapi/agents/rag/simple/enhanced_v3/answer_generator_agent/index
   /autoapi/agents/rag/simple/enhanced_v3/retriever_agent/index
   /autoapi/agents/rag/simple/enhanced_v3/state/index


Classes
-------

.. autoapisummary::

   agents.rag.simple.enhanced_v3.RetrieverAgent
   agents.rag.simple.enhanced_v3.SimpleAnswerAgent
   agents.rag.simple.enhanced_v3.SimpleRAGState
   agents.rag.simple.enhanced_v3.SimpleRAGV3


Package Contents
----------------

.. py:class:: RetrieverAgent

   Bases: :py:obj:`haive.agents.rag.base.agent.BaseRAGAgent`


   Specialized retriever agent for SimpleRAG V3.

   This agent extends BaseRAGAgent with enhanced features:
   - Performance tracking and timing
   - Debug information collection
   - Enhanced document metadata
   - Quality scoring for retrieved documents
   - Configurable retrieval parameters

   Designed to work as the first agent in Enhanced MultiAgent V3 sequential pattern:
   RetrieverAgent → SimpleAnswerAgent

   .. rubric:: Examples

   Basic usage::

       retriever = RetrieverAgent(
           name="document_retriever",
           engine=vector_store_config,
           top_k=5,
           score_threshold=0.7
       )

       result = await retriever.arun("What is machine learning?")

   With performance tracking::

       retriever = RetrieverAgent(
           name="enhanced_retriever",
           engine=vector_store_config,
           performance_mode=True,
           debug_mode=True
       )


   .. autolink-examples:: RetrieverAgent
      :collapse:

   .. py:method:: _build_metadata(documents: list[langchain_core.documents.Document], query: str, retrieval_time: float) -> dict[str, Any]

      Build metadata for retrieval operation.


      .. autolink-examples:: _build_metadata
         :collapse:


   .. py:method:: _calculate_performance_metrics(documents: list[langchain_core.documents.Document], retrieval_time: float, query: str) -> dict[str, float]

      Calculate performance metrics for retrieval operation.


      .. autolink-examples:: _calculate_performance_metrics
         :collapse:


   .. py:method:: _calculate_quality_score(document: langchain_core.documents.Document, query: str) -> float

      Calculate quality score for a document relative to query.


      .. autolink-examples:: _calculate_quality_score
         :collapse:


   .. py:method:: _collect_debug_info(documents: list[langchain_core.documents.Document], retrieval_time: float, query: str) -> dict[str, Any]

      Collect debug information for retrieval operation.


      .. autolink-examples:: _collect_debug_info
         :collapse:


   .. py:method:: _extract_documents(retrieval_result: Any) -> list[langchain_core.documents.Document]

      Extract documents from various result formats.


      .. autolink-examples:: _extract_documents
         :collapse:


   .. py:method:: _filter_and_score_documents(documents: list[langchain_core.documents.Document], query: str, debug: bool = False) -> list[langchain_core.documents.Document]

      Filter documents by score threshold and apply quality scoring.


      .. autolink-examples:: _filter_and_score_documents
         :collapse:


   .. py:method:: arun(input_data: str | dict[str, Any], debug: bool = False, **kwargs) -> dict[str, Any]
      :async:


      Enhanced retrieval with performance tracking and debug info.

      :param input_data: Query string or dict with 'query' field
      :param debug: Enable debug output
      :param \*\*kwargs: Additional retrieval parameters

      :returns:     - documents: List of retrieved documents
                    - metadata: Retrieval metadata (if performance_mode)
                    - debug_info: Debug information (if debug_mode)
                    - performance_metrics: Timing and quality metrics
      :rtype: Dict containing


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: get_retrieval_summary() -> dict[str, Any]

      Get summary of retriever configuration.


      .. autolink-examples:: get_retrieval_summary
         :collapse:


   .. py:attribute:: debug_mode
      :type:  bool
      :value: None



   .. py:attribute:: include_metadata
      :type:  bool
      :value: None



   .. py:attribute:: performance_mode
      :type:  bool
      :value: None



   .. py:attribute:: quality_scoring
      :type:  bool
      :value: None



   .. py:attribute:: score_threshold
      :type:  float
      :value: None



   .. py:attribute:: top_k
      :type:  int
      :value: None



.. py:class:: SimpleAnswerAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Specialized answer generation agent for SimpleRAG V3.

   This agent extends SimpleAgent with RAG-specific features:
   - Document-aware prompt templates
   - Context formatting and processing
   - Source citation and attribution
   - Answer quality scoring
   - Enhanced metadata collection

   Designed to work as the second agent in Enhanced MultiAgent V3 sequential pattern:
   RetrieverAgent → SimpleAnswerAgent

   The agent expects input from RetrieverAgent containing:
   - documents: List of retrieved documents
   - query: Original user query
   - metadata: Retrieval metadata

   .. rubric:: Examples

   Basic usage::

       answer_agent = SimpleAnswerAgent(
           name="answer_generator",
           engine=AugLLMConfig(temperature=0.7),
           max_context_length=4000
       )

   With structured output::

       class QAResponse(BaseModel):
           answer: str
           sources: List[str]
           confidence: float

       answer_agent = SimpleAnswerAgent(
           name="structured_answer",
           engine=AugLLMConfig(),
           structured_output_model=QAResponse
       )


   .. autolink-examples:: SimpleAnswerAgent
      :collapse:

   .. py:method:: _build_context_from_documents(documents: list[langchain_core.documents.Document], query: str, debug: bool = False) -> dict[str, Any]

      Build formatted context from retrieved documents.


      .. autolink-examples:: _build_context_from_documents
         :collapse:


   .. py:method:: _enhance_generation_result(generation_result: Any, context_info: dict[str, Any], query: str, documents: list[langchain_core.documents.Document], generation_time: float, retrieval_metadata: dict[str, Any], debug: bool = False) -> dict[str, Any] | str

      Enhance generation result with metadata and citations.


      .. autolink-examples:: _enhance_generation_result
         :collapse:


   .. py:method:: _format_prompt_with_context(query: str, context_info: dict[str, Any], debug: bool = False) -> str

      Format the prompt with context and query.


      .. autolink-examples:: _format_prompt_with_context
         :collapse:


   .. py:method:: _parse_retriever_input(input_data: Any) -> dict[str, Any]

      Parse input from RetrieverAgent, BaseRAGAgent, or direct query.

      Handles multiple input formats:
      - BaseRAGAgent: Uses 'retrieved_documents' field
      - RetrieverAgent: Uses 'documents' field
      - Direct string: Creates empty document list


      .. autolink-examples:: _parse_retriever_input
         :collapse:


   .. py:method:: arun(input_data: str | dict[str, Any], debug: bool = False, **kwargs) -> dict[str, Any] | str
      :async:


      Enhanced answer generation with document processing.

      :param input_data: Input from RetrieverAgent or direct query
      :param debug: Enable debug output
      :param \*\*kwargs: Additional generation parameters

      :returns: Generated answer (format depends on structured_output_model)


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: get_generation_summary() -> dict[str, Any]

      Get summary of answer generator configuration.


      .. autolink-examples:: get_generation_summary
         :collapse:


   .. py:attribute:: citation_style
      :type:  str
      :value: None



   .. py:attribute:: debug_mode
      :type:  bool
      :value: None



   .. py:attribute:: include_citations
      :type:  bool
      :value: None



   .. py:attribute:: max_context_length
      :type:  int
      :value: None



   .. py:attribute:: min_confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: performance_mode
      :type:  bool
      :value: None



   .. py:attribute:: require_source_support
      :type:  bool
      :value: None



   .. py:attribute:: system_prompt_template
      :type:  str
      :value: None



   .. py:attribute:: use_chat_prompt_template
      :type:  bool
      :value: None



.. py:class:: SimpleRAGState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   Enhanced state schema for SimpleRAG V3 pipeline.

   This state schema extends the basic StateSchema with RAG-specific fields
   and enhanced tracking capabilities when performance_mode or debug_mode
   are enabled.

   Core RAG Fields:
       - query: User query string
       - retrieved_documents: Documents from retrieval step
       - generated_answer: Final answer from generation step

   Enhanced Tracking (when enabled):
       - retrieval_metadata: Retrieval operation metadata
       - generation_metadata: Generation operation metadata
       - performance_metrics: Performance tracking data
       - debug_info: Detailed debug information

   .. rubric:: Examples

   Basic usage (automatic schema selection)::

       # Enhanced features disabled - uses basic fields only
       state = SimpleRAGState(query="What is AI?")

   Enhanced usage::

       # Enhanced features enabled - includes all tracking
       state = SimpleRAGState(
           query="What is AI?",
           retrieval_metadata=RAGMetadata(
               timing_info={"retrieval_time": 0.5}
           ),
           debug_mode=True
       )


   .. autolink-examples:: SimpleRAGState
      :collapse:

   .. py:method:: add_generation_debug(context_length: int | None = None, prompt_tokens: int | None = None, completion_tokens: int | None = None, generation_time: float | None = None, **kwargs) -> None

      Add generation debug information.


      .. autolink-examples:: add_generation_debug
         :collapse:


   .. py:method:: add_retrieval_debug(query_vector_dim: int | None = None, search_time: float | None = None, total_documents: int | None = None, similarity_scores: list[float] | None = None, **kwargs) -> None

      Add retrieval debug information.


      .. autolink-examples:: add_retrieval_debug
         :collapse:


   .. py:method:: get_generation_summary() -> dict[str, Any]

      Get generation operation summary.


      .. autolink-examples:: get_generation_summary
         :collapse:


   .. py:method:: get_pipeline_summary() -> dict[str, Any]

      Get comprehensive pipeline summary.


      .. autolink-examples:: get_pipeline_summary
         :collapse:


   .. py:method:: get_retrieval_summary() -> dict[str, Any]

      Get retrieval operation summary.


      .. autolink-examples:: get_retrieval_summary
         :collapse:


   .. py:method:: update_performance_metric(metric_name: str, value: float) -> None

      Update a performance metric.


      .. autolink-examples:: update_performance_metric
         :collapse:


   .. py:method:: update_stage(stage: str) -> None

      Update current stage and add to history.


      .. autolink-examples:: update_stage
         :collapse:


   .. py:attribute:: citation_info
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: current_stage
      :type:  str
      :value: None



   .. py:attribute:: document_sources
      :type:  list[str]
      :value: None



   .. py:attribute:: generated_answer
      :type:  str
      :value: None



   .. py:attribute:: generation_debug
      :type:  GenerationDebugInfo | None
      :value: None



   .. py:attribute:: generation_metadata
      :type:  RAGMetadata | None
      :value: None



   .. py:attribute:: performance_metrics
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: retrieval_debug
      :type:  RetrievalDebugInfo | None
      :value: None



   .. py:attribute:: retrieval_metadata
      :type:  RAGMetadata | None
      :value: None



   .. py:attribute:: retrieved_documents
      :type:  list[langchain_core.documents.Document]
      :value: None



   .. py:attribute:: stage_history
      :type:  list[str]
      :value: None



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



