
:py:mod:`agents.rag.flare.agent`
================================

.. py:module:: agents.rag.flare.agent

FLARE (Forward-Looking Active REtrieval) RAG Agents.

from typing import Any
Implementation of FLARE RAG with forward-looking retrieval and iterative generation.
Uses structured output models for planning and managing active retrieval decisions.


.. autolink-examples:: agents.rag.flare.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.flare.agent.ActiveRetrievalAgent
   agents.rag.flare.agent.ConfidenceLevel
   agents.rag.flare.agent.FLAREPlan
   agents.rag.flare.agent.FLAREPlannerAgent
   agents.rag.flare.agent.FLARERAGAgent
   agents.rag.flare.agent.FLAREResult
   agents.rag.flare.agent.RetrievalDecision


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ActiveRetrievalAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ActiveRetrievalAgent {
        node [shape=record];
        "ActiveRetrievalAgent" [label="ActiveRetrievalAgent"];
        "haive.agents.base.agent.Agent" -> "ActiveRetrievalAgent";
      }

.. autoclass:: agents.rag.flare.agent.ActiveRetrievalAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfidenceLevel:

   .. graphviz::
      :align: center

      digraph inheritance_ConfidenceLevel {
        node [shape=record];
        "ConfidenceLevel" [label="ConfidenceLevel"];
        "str" -> "ConfidenceLevel";
        "enum.Enum" -> "ConfidenceLevel";
      }

.. autoclass:: agents.rag.flare.agent.ConfidenceLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ConfidenceLevel** is an Enum defined in ``agents.rag.flare.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FLAREPlan:

   .. graphviz::
      :align: center

      digraph inheritance_FLAREPlan {
        node [shape=record];
        "FLAREPlan" [label="FLAREPlan"];
        "pydantic.BaseModel" -> "FLAREPlan";
      }

.. autopydantic_model:: agents.rag.flare.agent.FLAREPlan
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

   Inheritance diagram for FLAREPlannerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_FLAREPlannerAgent {
        node [shape=record];
        "FLAREPlannerAgent" [label="FLAREPlannerAgent"];
        "haive.agents.base.agent.Agent" -> "FLAREPlannerAgent";
      }

.. autoclass:: agents.rag.flare.agent.FLAREPlannerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FLARERAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_FLARERAGAgent {
        node [shape=record];
        "FLARERAGAgent" [label="FLARERAGAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "FLARERAGAgent";
      }

.. autoclass:: agents.rag.flare.agent.FLARERAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FLAREResult:

   .. graphviz::
      :align: center

      digraph inheritance_FLAREResult {
        node [shape=record];
        "FLAREResult" [label="FLAREResult"];
        "pydantic.BaseModel" -> "FLAREResult";
      }

.. autopydantic_model:: agents.rag.flare.agent.FLAREResult
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

   Inheritance diagram for RetrievalDecision:

   .. graphviz::
      :align: center

      digraph inheritance_RetrievalDecision {
        node [shape=record];
        "RetrievalDecision" [label="RetrievalDecision"];
        "str" -> "RetrievalDecision";
        "enum.Enum" -> "RetrievalDecision";
      }

.. autoclass:: agents.rag.flare.agent.RetrievalDecision
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RetrievalDecision** is an Enum defined in ``agents.rag.flare.agent``.



Functions
---------

.. autoapisummary::

   agents.rag.flare.agent.create_active_retrieval_callable
   agents.rag.flare.agent.create_flare_planner_callable
   agents.rag.flare.agent.create_flare_rag_agent
   agents.rag.flare.agent.get_flare_rag_io_schema

.. py:function:: create_active_retrieval_callable(documents: list[langchain_core.documents.Document], embedding_model: str | None = None)

   Create callable function for active retrieval.


   .. autolink-examples:: create_active_retrieval_callable
      :collapse:

.. py:function:: create_flare_planner_callable(llm_config: haive.core.models.llm.base.LLMConfig)

   Create callable function for FLARE planning.


   .. autolink-examples:: create_flare_planner_callable
      :collapse:

.. py:function:: create_flare_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, flare_mode: str = 'adaptive', **kwargs) -> FLARERAGAgent

   Create a FLARE RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param flare_mode: FLARE mode ("conservative", "adaptive", "aggressive")
   :param \*\*kwargs: Additional arguments

   :returns: Configured FLARE RAG agent


   .. autolink-examples:: create_flare_rag_agent
      :collapse:

.. py:function:: get_flare_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for FLARE RAG agents.


   .. autolink-examples:: get_flare_rag_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.flare.agent
   :collapse:
   
.. autolink-skip:: next
