agents.rag.multi_agent_rag.grading_components
=============================================

.. py:module:: agents.rag.multi_agent_rag.grading_components

.. autoapi-nested-parse::

   Grading Components for RAG Workflows.

   This module provides reusable grading agents for document relevance,
   answer quality, and hallucination detection.


   .. autolink-examples:: agents.rag.multi_agent_rag.grading_components
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.rag.multi_agent_rag.grading_components.ANSWER_QUALITY_PROMPT
   agents.rag.multi_agent_rag.grading_components.DOCUMENT_RELEVANCE_PROMPT
   agents.rag.multi_agent_rag.grading_components.HALLUCINATION_DETECTION_PROMPT
   agents.rag.multi_agent_rag.grading_components.PRIORITY_RANKING_PROMPT
   agents.rag.multi_agent_rag.grading_components.QUERY_ANALYSIS_PROMPT


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.grading_components.AnswerGrade
   agents.rag.multi_agent_rag.grading_components.CompositeGradingAgent
   agents.rag.multi_agent_rag.grading_components.DocumentGrade
   agents.rag.multi_agent_rag.grading_components.HallucinationGrade


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.grading_components.create_answer_grader
   agents.rag.multi_agent_rag.grading_components.create_document_grader
   agents.rag.multi_agent_rag.grading_components.create_hallucination_grader
   agents.rag.multi_agent_rag.grading_components.create_priority_ranker
   agents.rag.multi_agent_rag.grading_components.create_query_analyzer


Module Contents
---------------

.. py:class:: AnswerGrade(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Grade for generated answer quality.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AnswerGrade
      :collapse:

   .. py:attribute:: accuracy_score
      :type:  float
      :value: None



   .. py:attribute:: clarity_score
      :type:  float
      :value: None



   .. py:attribute:: completeness_score
      :type:  float
      :value: None



   .. py:attribute:: overall_score
      :type:  float
      :value: None



   .. py:attribute:: strengths
      :type:  list[str]
      :value: []



   .. py:attribute:: suggestions
      :type:  list[str]
      :value: []



   .. py:attribute:: weaknesses
      :type:  list[str]
      :value: []



.. py:class:: CompositeGradingAgent

   Combines multiple grading components for comprehensive evaluation.


   .. autolink-examples:: CompositeGradingAgent
      :collapse:

   .. py:method:: _calculate_overall_score(document_grades: list[dict], answer_grade: dict, hallucination_grade: dict) -> float

      Calculate overall pipeline score.


      .. autolink-examples:: _calculate_overall_score
         :collapse:


   .. py:method:: grade_rag_pipeline(query: str, documents: list[dict[str, Any]], answer: str) -> dict[str, Any]
      :async:


      Perform comprehensive grading of entire RAG pipeline.


      .. autolink-examples:: grade_rag_pipeline
         :collapse:


   .. py:attribute:: answer_grader


   .. py:attribute:: document_grader


   .. py:attribute:: hallucination_grader


   .. py:attribute:: priority_ranker


   .. py:attribute:: query_analyzer


.. py:class:: DocumentGrade(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Grade for a retrieved document.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DocumentGrade
      :collapse:

   .. py:attribute:: document_id
      :type:  str


   .. py:attribute:: is_relevant
      :type:  bool


   .. py:attribute:: key_information
      :type:  list[str]
      :value: []



   .. py:attribute:: reasoning
      :type:  str


   .. py:attribute:: relevance_score
      :type:  float
      :value: None



.. py:class:: HallucinationGrade(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Grade for hallucination detection.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HallucinationGrade
      :collapse:

   .. py:attribute:: hallucination_score
      :type:  float
      :value: None



   .. py:attribute:: hallucination_types
      :type:  list[str]
      :value: []



   .. py:attribute:: has_hallucination
      :type:  bool


   .. py:attribute:: specific_issues
      :type:  list[str]
      :value: []



   .. py:attribute:: supported_claims
      :type:  list[str]
      :value: []



   .. py:attribute:: unsupported_claims
      :type:  list[str]
      :value: []



.. py:function:: create_answer_grader(name: str = 'answer_grader') -> haive.agents.simple.SimpleAgent

   Create an answer quality grading agent.


   .. autolink-examples:: create_answer_grader
      :collapse:

.. py:function:: create_document_grader(name: str = 'document_grader') -> haive.agents.simple.SimpleAgent

   Create a document relevance grading agent.


   .. autolink-examples:: create_document_grader
      :collapse:

.. py:function:: create_hallucination_grader(name: str = 'hallucination_grader') -> haive.agents.simple.SimpleAgent

   Create a hallucination detection agent.


   .. autolink-examples:: create_hallucination_grader
      :collapse:

.. py:function:: create_priority_ranker(name: str = 'priority_ranker') -> haive.agents.simple.SimpleAgent

   Create a document priority ranking agent.


   .. autolink-examples:: create_priority_ranker
      :collapse:

.. py:function:: create_query_analyzer(name: str = 'query_analyzer') -> haive.agents.simple.SimpleAgent

   Create a query analysis agent.


   .. autolink-examples:: create_query_analyzer
      :collapse:

.. py:data:: ANSWER_QUALITY_PROMPT

.. py:data:: DOCUMENT_RELEVANCE_PROMPT

.. py:data:: HALLUCINATION_DETECTION_PROMPT

.. py:data:: PRIORITY_RANKING_PROMPT

.. py:data:: QUERY_ANALYSIS_PROMPT

