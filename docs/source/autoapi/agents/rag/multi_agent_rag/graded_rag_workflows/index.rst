agents.rag.multi_agent_rag.graded_rag_workflows
===============================================

.. py:module:: agents.rag.multi_agent_rag.graded_rag_workflows

.. autoapi-nested-parse::

   Graded RAG Workflows - RAG with comprehensive grading and evaluation.

   from typing import Any
   This module implements RAG workflows with integrated document grading,
   answer quality assessment, and hallucination detection.


   .. autolink-examples:: agents.rag.multi_agent_rag.graded_rag_workflows
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.graded_rag_workflows.AdaptiveGradedRAGAgent
   agents.rag.multi_agent_rag.graded_rag_workflows.FullyGradedRAGAgent
   agents.rag.multi_agent_rag.graded_rag_workflows.GradedRAGState
   agents.rag.multi_agent_rag.graded_rag_workflows.MultiCriteriaGradedRAGAgent
   agents.rag.multi_agent_rag.graded_rag_workflows.ReflexiveGradedRAGAgent


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.graded_rag_workflows.build_custom_graph


Module Contents
---------------

.. py:class:: AdaptiveGradedRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Adaptive Graded RAG - adjusts grading thresholds based on query complexity.
   and document availability.


   .. autolink-examples:: AdaptiveGradedRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for adaptive graded RAG.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:class:: FullyGradedRAGAgent(relevance_threshold: float = 0.5, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Fully Graded RAG - comprehensive grading at every step of the RAG pipeline.
   Includes query analysis, document grading, prioritization, answer quality,
   and hallucination detection.


   .. autolink-examples:: FullyGradedRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for graded RAG workflow.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: _relevance_threshold
      :value: 0.5



.. py:class:: GradedRAGState

   Bases: :py:obj:`haive.core.schema.prebuilt.rag_state.RAGState`


   RAG state with grading information.


   .. autolink-examples:: GradedRAGState
      :collapse:

   .. py:attribute:: answer_grade
      :type:  haive.agents.rag.multi_agent_rag.grading_components.AnswerGrade | None
      :value: None



   .. py:attribute:: document_grades
      :type:  list[haive.agents.rag.multi_agent_rag.grading_components.DocumentGrade]
      :value: []



   .. py:attribute:: filtered_documents
      :type:  list[str]
      :value: []



   .. py:attribute:: hallucination_grade
      :type:  haive.agents.rag.multi_agent_rag.grading_components.HallucinationGrade | None
      :value: None



   .. py:attribute:: improvement_suggestions
      :type:  list[str]
      :value: []



   .. py:attribute:: key_entities
      :type:  list[str]
      :value: []



   .. py:attribute:: overall_score
      :type:  float
      :value: 0.0



   .. py:attribute:: priority_ranking
      :type:  dict[str, float]


   .. py:attribute:: query_complexity
      :type:  str
      :value: ''



   .. py:attribute:: query_type
      :type:  str
      :value: ''



.. py:class:: MultiCriteriaGradedRAGAgent(grading_criteria: list[str] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Multi-Criteria Graded RAG - uses multiple grading criteria and perspectives.
   to evaluate documents and answers.


   .. autolink-examples:: MultiCriteriaGradedRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for multi-criteria graded RAG.


      .. autolink-examples:: build_custom_graph
         :collapse:


   .. py:attribute:: _grading_criteria
      :value: None



.. py:class:: ReflexiveGradedRAGAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.base.MultiAgent`


   Reflexive Graded RAG - uses grading feedback to improve its own performance.
   through self-reflection and strategy adjustment.


   .. autolink-examples:: ReflexiveGradedRAGAgent
      :collapse:

   .. py:method:: build_custom_graph() -> Any

      Build the custom graph for reflexive graded RAG.


      .. autolink-examples:: build_custom_graph
         :collapse:


.. py:function:: build_custom_graph() -> Any

   Build custom graph for graded RAG workflows.

   This is a utility function for creating custom graphs for
   graded RAG workflows in this module.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:

