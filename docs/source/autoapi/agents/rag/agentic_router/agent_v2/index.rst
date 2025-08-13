
:py:mod:`agents.rag.agentic_router.agent_v2`
============================================

.. py:module:: agents.rag.agentic_router.agent_v2

Agentic RAG Router with Proper Conditional Routing.

Implementation using conditional edges for routing between strategies.


.. autolink-examples:: agents.rag.agentic_router.agent_v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.agentic_router.agent_v2.AgenticRAGRouterV2
   agents.rag.agentic_router.agent_v2.RAGStrategy
   agents.rag.agentic_router.agent_v2.StrategyDecision


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgenticRAGRouterV2:

   .. graphviz::
      :align: center

      digraph inheritance_AgenticRAGRouterV2 {
        node [shape=record];
        "AgenticRAGRouterV2" [label="AgenticRAGRouterV2"];
        "haive.agents.base.agent.Agent" -> "AgenticRAGRouterV2";
      }

.. autoclass:: agents.rag.agentic_router.agent_v2.AgenticRAGRouterV2
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_RAGStrategy {
        node [shape=record];
        "RAGStrategy" [label="RAGStrategy"];
        "str" -> "RAGStrategy";
        "enum.Enum" -> "RAGStrategy";
      }

.. autoclass:: agents.rag.agentic_router.agent_v2.RAGStrategy
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **RAGStrategy** is an Enum defined in ``agents.rag.agentic_router.agent_v2``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StrategyDecision:

   .. graphviz::
      :align: center

      digraph inheritance_StrategyDecision {
        node [shape=record];
        "StrategyDecision" [label="StrategyDecision"];
        "pydantic.BaseModel" -> "StrategyDecision";
      }

.. autopydantic_model:: agents.rag.agentic_router.agent_v2.StrategyDecision
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

.. autolink-examples:: agents.rag.agentic_router.agent_v2
   :collapse:
   
.. autolink-skip:: next
