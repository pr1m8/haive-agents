agents.rag.simple.enhanced_v3.retriever_agent
=============================================

.. py:module:: agents.rag.simple.enhanced_v3.retriever_agent

.. autoapi-nested-parse::

   Specialized Retriever Agent for SimpleRAG V3.

   This module provides a specialized retriever agent that extends BaseRAGAgent
   with enhanced features for use in Enhanced MultiAgent V3 workflows.


   .. autolink-examples:: agents.rag.simple.enhanced_v3.retriever_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.simple.enhanced_v3.retriever_agent.RetrieverAgent


Module Contents
---------------

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



