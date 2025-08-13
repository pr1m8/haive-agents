
:py:mod:`agents.rag.step_back.agent`
====================================

.. py:module:: agents.rag.step_back.agent

Step-Back Prompting RAG Agents.

from typing import Any
Implementation of step-back prompting for abstract reasoning.
Generates broader conceptual queries for enhanced context retrieval.


.. autolink-examples:: agents.rag.step_back.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.step_back.agent.DualRetrievalAgent
   agents.rag.step_back.agent.StepBackQuery
   agents.rag.step_back.agent.StepBackQueryGeneratorAgent
   agents.rag.step_back.agent.StepBackRAGAgent
   agents.rag.step_back.agent.StepBackResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DualRetrievalAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DualRetrievalAgent {
        node [shape=record];
        "DualRetrievalAgent" [label="DualRetrievalAgent"];
        "haive.agents.base.agent.Agent" -> "DualRetrievalAgent";
      }

.. autoclass:: agents.rag.step_back.agent.DualRetrievalAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StepBackQuery:

   .. graphviz::
      :align: center

      digraph inheritance_StepBackQuery {
        node [shape=record];
        "StepBackQuery" [label="StepBackQuery"];
        "pydantic.BaseModel" -> "StepBackQuery";
      }

.. autopydantic_model:: agents.rag.step_back.agent.StepBackQuery
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

   Inheritance diagram for StepBackQueryGeneratorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_StepBackQueryGeneratorAgent {
        node [shape=record];
        "StepBackQueryGeneratorAgent" [label="StepBackQueryGeneratorAgent"];
        "haive.agents.base.agent.Agent" -> "StepBackQueryGeneratorAgent";
      }

.. autoclass:: agents.rag.step_back.agent.StepBackQueryGeneratorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StepBackRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_StepBackRAGAgent {
        node [shape=record];
        "StepBackRAGAgent" [label="StepBackRAGAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "StepBackRAGAgent";
      }

.. autoclass:: agents.rag.step_back.agent.StepBackRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StepBackResult:

   .. graphviz::
      :align: center

      digraph inheritance_StepBackResult {
        node [shape=record];
        "StepBackResult" [label="StepBackResult"];
        "pydantic.BaseModel" -> "StepBackResult";
      }

.. autopydantic_model:: agents.rag.step_back.agent.StepBackResult
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

   agents.rag.step_back.agent.create_step_back_rag_agent
   agents.rag.step_back.agent.get_step_back_rag_io_schema

.. py:function:: create_step_back_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, reasoning_depth: str = 'moderate', **kwargs) -> StepBackRAGAgent

   Create a Step-Back RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param reasoning_depth: Depth of reasoning ("shallow", "moderate", "deep")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Step-Back RAG agent


   .. autolink-examples:: create_step_back_rag_agent
      :collapse:

.. py:function:: get_step_back_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Step-Back RAG agents.


   .. autolink-examples:: get_step_back_rag_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.step_back.agent
   :collapse:
   
.. autolink-skip:: next
