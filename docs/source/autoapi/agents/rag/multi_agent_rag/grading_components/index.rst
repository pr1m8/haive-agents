
:py:mod:`agents.rag.multi_agent_rag.grading_components`
=======================================================

.. py:module:: agents.rag.multi_agent_rag.grading_components

Grading Components for RAG Workflows.

This module provides reusable grading agents for document relevance,
answer quality, and hallucination detection.


.. autolink-examples:: agents.rag.multi_agent_rag.grading_components
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.grading_components.AnswerGrade
   agents.rag.multi_agent_rag.grading_components.CompositeGradingAgent
   agents.rag.multi_agent_rag.grading_components.DocumentGrade
   agents.rag.multi_agent_rag.grading_components.HallucinationGrade


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AnswerGrade:

   .. graphviz::
      :align: center

      digraph inheritance_AnswerGrade {
        node [shape=record];
        "AnswerGrade" [label="AnswerGrade"];
        "pydantic.BaseModel" -> "AnswerGrade";
      }

.. autopydantic_model:: agents.rag.multi_agent_rag.grading_components.AnswerGrade
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CompositeGradingAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CompositeGradingAgent {
        node [shape=record];
        "CompositeGradingAgent" [label="CompositeGradingAgent"];
      }

.. autoclass:: agents.rag.multi_agent_rag.grading_components.CompositeGradingAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentGrade:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentGrade {
        node [shape=record];
        "DocumentGrade" [label="DocumentGrade"];
        "pydantic.BaseModel" -> "DocumentGrade";
      }

.. autopydantic_model:: agents.rag.multi_agent_rag.grading_components.DocumentGrade
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HallucinationGrade:

   .. graphviz::
      :align: center

      digraph inheritance_HallucinationGrade {
        node [shape=record];
        "HallucinationGrade" [label="HallucinationGrade"];
        "pydantic.BaseModel" -> "HallucinationGrade";
      }

.. autopydantic_model:: agents.rag.multi_agent_rag.grading_components.HallucinationGrade
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.grading_components.create_answer_grader
   agents.rag.multi_agent_rag.grading_components.create_document_grader
   agents.rag.multi_agent_rag.grading_components.create_hallucination_grader
   agents.rag.multi_agent_rag.grading_components.create_priority_ranker
   agents.rag.multi_agent_rag.grading_components.create_query_analyzer

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



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.grading_components
   :collapse:
   
.. autolink-skip:: next
