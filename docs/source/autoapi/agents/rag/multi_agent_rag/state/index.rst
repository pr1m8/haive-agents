agents.rag.multi_agent_rag.state
================================

.. py:module:: agents.rag.multi_agent_rag.state

.. autoapi-nested-parse::

   Enhanced RAG State Schema for Multi-Agent RAG Systems.

   This module provides comprehensive state management for complex RAG workflows,
   supporting document processing, grading, multi-step retrieval, and conditional routing.


   .. autolink-examples:: agents.rag.multi_agent_rag.state
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.multi_agent_rag.state.EnhancedRAGState
   agents.rag.multi_agent_rag.state.RAGState


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.state.DocumentGradingResult
   agents.rag.multi_agent_rag.state.MultiAgentRAGState
   agents.rag.multi_agent_rag.state.QueryStatus
   agents.rag.multi_agent_rag.state.RAGOperationType
   agents.rag.multi_agent_rag.state.RAGStep


Module Contents
---------------

.. py:class:: DocumentGradingResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of document grading process.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentGradingResult
      :collapse:

   .. py:attribute:: document
      :type:  langchain_core.documents.Document
      :value: None



   .. py:attribute:: document_id
      :type:  str
      :value: None



   .. py:attribute:: grader_type
      :type:  str
      :value: None



   .. py:attribute:: grading_reason
      :type:  str
      :value: None



   .. py:attribute:: is_relevant
      :type:  bool
      :value: None



   .. py:attribute:: relevance_score
      :type:  float
      :value: None



.. py:class:: MultiAgentRAGState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   Comprehensive state schema for multi-agent RAG systems.

   Supports complex RAG workflows with document grading, multi-step retrieval,
   conditional routing, and state tracking across multiple agents.


   .. autolink-examples:: MultiAgentRAGState
      :collapse:

   .. py:method:: add_workflow_step(operation_type: RAGOperationType, agent_name: str, input_data: dict[str, Any] | None = None, output_data: dict[str, Any] | None = None) -> str

      Add a new workflow step.


      .. autolink-examples:: add_workflow_step
         :collapse:


   .. py:method:: get_latest_step(operation_type: RAGOperationType | None = None) -> RAGStep | None

      Get the most recent workflow step, optionally filtered by operation type.


      .. autolink-examples:: get_latest_step
         :collapse:


   .. py:method:: get_relevant_documents(min_score: float = 0.5) -> list[langchain_core.documents.Document]

      Get documents that passed relevance threshold.


      .. autolink-examples:: get_relevant_documents
         :collapse:


   .. py:method:: should_refine_query() -> bool

      Determine if query should be refined based on state.


      .. autolink-examples:: should_refine_query
         :collapse:


   .. py:method:: update_quality_metrics() -> None

      Update quality metrics based on current state.


      .. autolink-examples:: update_quality_metrics
         :collapse:


   .. py:attribute:: __reducer_fields__


   .. py:attribute:: __shared_fields__
      :value: ['messages', 'queries', 'documents', 'retrieved_documents', 'graded_documents',...



   .. py:attribute:: active_agent
      :type:  str | None
      :value: None



   .. py:attribute:: agent_decisions
      :type:  Annotated[dict[str, Any], operator.add]
      :value: None



   .. py:attribute:: current_operation
      :type:  RAGOperationType | None
      :value: None



   .. py:attribute:: documents
      :type:  Annotated[list[langchain_core.documents.Document], operator.add]
      :value: None



   .. py:attribute:: errors
      :type:  Annotated[list[str], operator.add]
      :value: None



   .. py:attribute:: filtered_documents
      :type:  Annotated[list[langchain_core.documents.Document], operator.add]
      :value: None



   .. py:attribute:: generated_answer
      :type:  str
      :value: None



   .. py:attribute:: generation_confidence
      :type:  float
      :value: None



   .. py:attribute:: generation_config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: graded_documents
      :type:  Annotated[list[DocumentGradingResult], operator.add]
      :value: None



   .. py:attribute:: grading_config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: intermediate_answers
      :type:  Annotated[list[str], operator.add]
      :value: None



   .. py:attribute:: messages
      :type:  Annotated[list[langchain_core.messages.BaseMessage], operator.add]
      :value: None



   .. py:attribute:: next_operation
      :type:  RAGOperationType | None
      :value: None



   .. py:attribute:: overall_quality_score
      :type:  float
      :value: None



   .. py:attribute:: queries
      :type:  Annotated[list[str], operator.add]
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: query_status
      :type:  QueryStatus
      :value: None



   .. py:attribute:: retrieval_confidence
      :type:  float
      :value: None



   .. py:attribute:: retrieval_config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: retrieved_documents
      :type:  Annotated[list[langchain_core.documents.Document], operator.add]
      :value: None



   .. py:attribute:: routing_decisions
      :type:  Annotated[list[dict[str, Any]], operator.add]
      :value: None



   .. py:attribute:: warnings
      :type:  Annotated[list[str], operator.add]
      :value: None



   .. py:attribute:: workflow_steps
      :type:  Annotated[list[RAGStep], operator.add]
      :value: None



.. py:class:: QueryStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status of query processing.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: QueryStatus
      :collapse:

   .. py:attribute:: COMPLETED
      :value: 'completed'



   .. py:attribute:: FAILED
      :value: 'failed'



   .. py:attribute:: IN_PROGRESS
      :value: 'in_progress'



   .. py:attribute:: NEEDS_REFINEMENT
      :value: 'needs_refinement'



   .. py:attribute:: PENDING
      :value: 'pending'



.. py:class:: RAGOperationType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of RAG operations that can be performed.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGOperationType
      :collapse:

   .. py:attribute:: GENERATE
      :value: 'generate'



   .. py:attribute:: GRADE
      :value: 'grade'



   .. py:attribute:: REFINE
      :value: 'refine'



   .. py:attribute:: RETRIEVE
      :value: 'retrieve'



   .. py:attribute:: ROUTE
      :value: 'route'



   .. py:attribute:: VERIFY
      :value: 'verify'



.. py:class:: RAGStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a single step in the RAG workflow.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RAGStep
      :collapse:

   .. py:attribute:: agent_name
      :type:  str | None
      :value: None



   .. py:attribute:: input_data
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: operation_type
      :type:  RAGOperationType
      :value: None



   .. py:attribute:: output_data
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



   .. py:attribute:: timestamp
      :type:  str | None
      :value: None



.. py:data:: EnhancedRAGState

.. py:data:: RAGState

