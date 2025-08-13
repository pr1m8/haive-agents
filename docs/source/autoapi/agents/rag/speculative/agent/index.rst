
:py:mod:`agents.rag.speculative.agent`
======================================

.. py:module:: agents.rag.speculative.agent

Speculative RAG Agents.

from typing import Any
Implementation of speculative RAG with parallel hypothesis generation and verification.
Uses structured output models for hypothesis planning and iterative refinement.


.. autolink-examples:: agents.rag.speculative.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.speculative.agent.Hypothesis
   agents.rag.speculative.agent.HypothesisConfidence
   agents.rag.speculative.agent.HypothesisGeneratorAgent
   agents.rag.speculative.agent.ParallelVerificationAgent
   agents.rag.speculative.agent.SpeculativeExecutionPlan
   agents.rag.speculative.agent.SpeculativeRAGAgent
   agents.rag.speculative.agent.SpeculativeResult
   agents.rag.speculative.agent.VerificationStatus


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Hypothesis:

   .. graphviz::
      :align: center

      digraph inheritance_Hypothesis {
        node [shape=record];
        "Hypothesis" [label="Hypothesis"];
        "pydantic.BaseModel" -> "Hypothesis";
      }

.. autopydantic_model:: agents.rag.speculative.agent.Hypothesis
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

   Inheritance diagram for HypothesisConfidence:

   .. graphviz::
      :align: center

      digraph inheritance_HypothesisConfidence {
        node [shape=record];
        "HypothesisConfidence" [label="HypothesisConfidence"];
        "str" -> "HypothesisConfidence";
        "enum.Enum" -> "HypothesisConfidence";
      }

.. autoclass:: agents.rag.speculative.agent.HypothesisConfidence
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **HypothesisConfidence** is an Enum defined in ``agents.rag.speculative.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HypothesisGeneratorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_HypothesisGeneratorAgent {
        node [shape=record];
        "HypothesisGeneratorAgent" [label="HypothesisGeneratorAgent"];
        "haive.agents.base.agent.Agent" -> "HypothesisGeneratorAgent";
      }

.. autoclass:: agents.rag.speculative.agent.HypothesisGeneratorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ParallelVerificationAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ParallelVerificationAgent {
        node [shape=record];
        "ParallelVerificationAgent" [label="ParallelVerificationAgent"];
        "haive.agents.base.agent.Agent" -> "ParallelVerificationAgent";
      }

.. autoclass:: agents.rag.speculative.agent.ParallelVerificationAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SpeculativeExecutionPlan:

   .. graphviz::
      :align: center

      digraph inheritance_SpeculativeExecutionPlan {
        node [shape=record];
        "SpeculativeExecutionPlan" [label="SpeculativeExecutionPlan"];
        "pydantic.BaseModel" -> "SpeculativeExecutionPlan";
      }

.. autopydantic_model:: agents.rag.speculative.agent.SpeculativeExecutionPlan
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

   Inheritance diagram for SpeculativeRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SpeculativeRAGAgent {
        node [shape=record];
        "SpeculativeRAGAgent" [label="SpeculativeRAGAgent"];
        "haive.agents.multi.base.SequentialAgent" -> "SpeculativeRAGAgent";
      }

.. autoclass:: agents.rag.speculative.agent.SpeculativeRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SpeculativeResult:

   .. graphviz::
      :align: center

      digraph inheritance_SpeculativeResult {
        node [shape=record];
        "SpeculativeResult" [label="SpeculativeResult"];
        "pydantic.BaseModel" -> "SpeculativeResult";
      }

.. autopydantic_model:: agents.rag.speculative.agent.SpeculativeResult
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

   Inheritance diagram for VerificationStatus:

   .. graphviz::
      :align: center

      digraph inheritance_VerificationStatus {
        node [shape=record];
        "VerificationStatus" [label="VerificationStatus"];
        "str" -> "VerificationStatus";
        "enum.Enum" -> "VerificationStatus";
      }

.. autoclass:: agents.rag.speculative.agent.VerificationStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **VerificationStatus** is an Enum defined in ``agents.rag.speculative.agent``.



Functions
---------

.. autoapisummary::

   agents.rag.speculative.agent.create_speculative_rag_agent
   agents.rag.speculative.agent.get_speculative_rag_io_schema

.. py:function:: create_speculative_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, speculation_mode: str = 'balanced', **kwargs) -> SpeculativeRAGAgent

   Create a Speculative RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param speculation_mode: Mode ("conservative", "balanced", "aggressive")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Speculative RAG agent


   .. autolink-examples:: create_speculative_rag_agent
      :collapse:

.. py:function:: get_speculative_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Speculative RAG agents.


   .. autolink-examples:: get_speculative_rag_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.speculative.agent
   :collapse:
   
.. autolink-skip:: next
