
:py:mod:`agents.memory.agentic_rag_coordinator`
===============================================

.. py:module:: agents.memory.agentic_rag_coordinator

Agentic RAG Coordinator for Memory System.

This module provides an intelligent coordinator that selects and combines
multiple retrieval strategies based on query analysis and context.


.. autolink-examples:: agents.memory.agentic_rag_coordinator
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.agentic_rag_coordinator.AgenticRAGCoordinator
   agents.memory.agentic_rag_coordinator.AgenticRAGCoordinatorConfig
   agents.memory.agentic_rag_coordinator.AgenticRAGResult
   agents.memory.agentic_rag_coordinator.RetrievalStrategy


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticRAGCoordinator:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRAGCoordinator {
        node [shape=record];
        "AgenticRAGCoordinator" [label="AgenticRAGCoordinator"];
        "haive.agents.simple.agent.SimpleAgent" -> "AgenticRAGCoordinator";
      }

.. autoclass:: agents.memory.agentic_rag_coordinator.AgenticRAGCoordinator
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticRAGCoordinatorConfig:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRAGCoordinatorConfig {
        node [shape=record];
        "AgenticRAGCoordinatorConfig" [label="AgenticRAGCoordinatorConfig"];
        "pydantic.BaseModel" -> "AgenticRAGCoordinatorConfig";
      }

.. autopydantic_model:: agents.memory.agentic_rag_coordinator.AgenticRAGCoordinatorConfig
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

   Inheritance diagram for AgenticRAGResult:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRAGResult {
        node [shape=record];
        "AgenticRAGResult" [label="AgenticRAGResult"];
        "pydantic.BaseModel" -> "AgenticRAGResult";
      }

.. autopydantic_model:: agents.memory.agentic_rag_coordinator.AgenticRAGResult
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

   Inheritance diagram for RetrievalStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_RetrievalStrategy {
        node [shape=record];
        "RetrievalStrategy" [label="RetrievalStrategy"];
        "pydantic.BaseModel" -> "RetrievalStrategy";
      }

.. autopydantic_model:: agents.memory.agentic_rag_coordinator.RetrievalStrategy
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

.. autolink-examples:: agents.memory.agentic_rag_coordinator
   :collapse:
   
.. autolink-skip:: next
