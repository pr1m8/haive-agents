agents.rag.simple.enhanced_v3.state
===================================

.. py:module:: agents.rag.simple.enhanced_v3.state

.. autoapi-nested-parse::

   Enhanced RAG State Schema for SimpleRAG V3.

   This module provides enhanced state management for SimpleRAG using Enhanced MultiAgent V3
   with performance tracking, debug information, and comprehensive metadata.


   .. autolink-examples:: agents.rag.simple.enhanced_v3.state
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.simple.enhanced_v3.state.BaseRAGState


Classes
-------

.. autoapisummary::

   agents.rag.simple.enhanced_v3.state.GenerationDebugInfo
   agents.rag.simple.enhanced_v3.state.RAGMetadata
   agents.rag.simple.enhanced_v3.state.RetrievalDebugInfo
   agents.rag.simple.enhanced_v3.state.SimpleRAGState


Module Contents
---------------

.. py:class:: GenerationDebugInfo(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Debug information for generation operations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GenerationDebugInfo
      :collapse:

   .. py:attribute:: completion_tokens
      :type:  int | None
      :value: None



   .. py:attribute:: context_length
      :type:  int | None
      :value: None



   .. py:attribute:: generation_time
      :type:  float | None
      :value: None



   .. py:attribute:: model_used
      :type:  str | None
      :value: None



   .. py:attribute:: prompt_tokens
      :type:  int | None
      :value: None



   .. py:attribute:: temperature
      :type:  float | None
      :value: None



.. py:class:: RAGMetadata(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Metadata for RAG operations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGMetadata
      :collapse:

   .. py:attribute:: generation_params
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: quality_scores
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: query_analysis
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: retrieval_params
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: timing_info
      :type:  dict[str, float]
      :value: None



.. py:class:: RetrievalDebugInfo(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Debug information for retrieval operations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RetrievalDebugInfo
      :collapse:

   .. py:attribute:: filtered_count
      :type:  int | None
      :value: None



   .. py:attribute:: query_vector_dim
      :type:  int | None
      :value: None



   .. py:attribute:: retrieval_strategy
      :type:  str | None
      :value: None



   .. py:attribute:: search_time
      :type:  float | None
      :value: None



   .. py:attribute:: similarity_scores
      :type:  list[float]
      :value: None



   .. py:attribute:: total_documents
      :type:  int | None
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



.. py:data:: BaseRAGState

