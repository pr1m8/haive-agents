
:py:mod:`agents.rag.document_grading.agent`
===========================================

.. py:module:: agents.rag.document_grading.agent

Document Grading RAG Agent.

from typing import Any
Iterative document grading with structured output.
Uses CallableNodeConfig to iterate over retrieved documents.


.. autolink-examples:: agents.rag.document_grading.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.document_grading.agent.DocumentGradingAgent
   agents.rag.document_grading.agent.DocumentGradingRAGAgent
   agents.rag.document_grading.agent.SingleDocumentGrade


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentGradingAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentGradingAgent {
        node [shape=record];
        "DocumentGradingAgent" [label="DocumentGradingAgent"];
        "haive.agents.base.agent.Agent" -> "DocumentGradingAgent";
      }

.. autoclass:: agents.rag.document_grading.agent.DocumentGradingAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DocumentGradingRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DocumentGradingRAGAgent {
        node [shape=record];
        "DocumentGradingRAGAgent" [label="DocumentGradingRAGAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "DocumentGradingRAGAgent";
      }

.. autoclass:: agents.rag.document_grading.agent.DocumentGradingRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SingleDocumentGrade:

   .. graphviz::
      :align: center

      digraph inheritance_SingleDocumentGrade {
        node [shape=record];
        "SingleDocumentGrade" [label="SingleDocumentGrade"];
        "pydantic.BaseModel" -> "SingleDocumentGrade";
      }

.. autopydantic_model:: agents.rag.document_grading.agent.SingleDocumentGrade
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





.. rubric:: Related Links

.. autolink-examples:: agents.rag.document_grading.agent
   :collapse:
   
.. autolink-skip:: next
