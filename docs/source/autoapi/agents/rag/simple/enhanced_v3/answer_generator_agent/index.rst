agents.rag.simple.enhanced_v3.answer_generator_agent
====================================================

.. py:module:: agents.rag.simple.enhanced_v3.answer_generator_agent

.. autoapi-nested-parse::

   Specialized Answer Generator Agent for SimpleRAG V3.

   This module provides a specialized answer generation agent that extends SimpleAgent
   with enhanced features for generating answers from retrieved documents.


   .. autolink-examples:: agents.rag.simple.enhanced_v3.answer_generator_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.simple.enhanced_v3.answer_generator_agent.SimpleAnswerAgent


Module Contents
---------------

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



