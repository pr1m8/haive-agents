
:py:mod:`agents.rag.self_reflective.agent`
==========================================

.. py:module:: agents.rag.self_reflective.agent

Self-Reflective Agentic RAG Agent.

from typing import Any
Implementation of self-reflective RAG with critique and iterative improvement.
Uses reflection loops to assess and enhance answer quality.


.. autolink-examples:: agents.rag.self_reflective.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.self_reflective.agent.ImprovedAnswer
   agents.rag.self_reflective.agent.ReflectionCritique
   agents.rag.self_reflective.agent.ReflectionPlan
   agents.rag.self_reflective.agent.ReflectionType
   agents.rag.self_reflective.agent.SelfReflectiveRAGAgent
   agents.rag.self_reflective.agent.SelfReflectiveResult


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ImprovedAnswer:

   .. graphviz::
      :align: center

      digraph inheritance_ImprovedAnswer {
        node [shape=record];
        "ImprovedAnswer" [label="ImprovedAnswer"];
        "pydantic.BaseModel" -> "ImprovedAnswer";
      }

.. autopydantic_model:: agents.rag.self_reflective.agent.ImprovedAnswer
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

   Inheritance diagram for ReflectionCritique:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionCritique {
        node [shape=record];
        "ReflectionCritique" [label="ReflectionCritique"];
        "pydantic.BaseModel" -> "ReflectionCritique";
      }

.. autopydantic_model:: agents.rag.self_reflective.agent.ReflectionCritique
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

   Inheritance diagram for ReflectionPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionPlan {
        node [shape=record];
        "ReflectionPlan" [label="ReflectionPlan"];
        "pydantic.BaseModel" -> "ReflectionPlan";
      }

.. autopydantic_model:: agents.rag.self_reflective.agent.ReflectionPlan
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

   Inheritance diagram for ReflectionType:

   .. graphviz::
      :align: center

      digraph inheritance_ReflectionType {
        node [shape=record];
        "ReflectionType" [label="ReflectionType"];
        "str" -> "ReflectionType";
        "enum.Enum" -> "ReflectionType";
      }

.. autoclass:: agents.rag.self_reflective.agent.ReflectionType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ReflectionType** is an Enum defined in ``agents.rag.self_reflective.agent``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfReflectiveRAGAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SelfReflectiveRAGAgent {
        node [shape=record];
        "SelfReflectiveRAGAgent" [label="SelfReflectiveRAGAgent"];
        "haive.agents.base.agent.Agent" -> "SelfReflectiveRAGAgent";
      }

.. autoclass:: agents.rag.self_reflective.agent.SelfReflectiveRAGAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SelfReflectiveResult:

   .. graphviz::
      :align: center

      digraph inheritance_SelfReflectiveResult {
        node [shape=record];
        "SelfReflectiveResult" [label="SelfReflectiveResult"];
        "pydantic.BaseModel" -> "SelfReflectiveResult";
      }

.. autopydantic_model:: agents.rag.self_reflective.agent.SelfReflectiveResult
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

   agents.rag.self_reflective.agent.create_self_reflective_rag_agent
   agents.rag.self_reflective.agent.get_self_reflective_rag_io_schema

.. py:function:: create_self_reflective_rag_agent(documents: list[langchain_core.documents.Document], llm_config: haive.core.models.llm.base.LLMConfig | None = None, reflection_mode: str = 'thorough', **kwargs) -> SelfReflectiveRAGAgent

   Create a Self-Reflective RAG agent.

   :param documents: Documents for retrieval
   :param llm_config: LLM configuration
   :param reflection_mode: Mode ("quick", "balanced", "thorough")
   :param \*\*kwargs: Additional arguments

   :returns: Configured Self-Reflective RAG agent


   .. autolink-examples:: create_self_reflective_rag_agent
      :collapse:

.. py:function:: get_self_reflective_rag_io_schema() -> dict[str, list[str]]

   Get I/O schema for Self-Reflective RAG agents.


   .. autolink-examples:: get_self_reflective_rag_io_schema
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.self_reflective.agent
   :collapse:
   
.. autolink-skip:: next
