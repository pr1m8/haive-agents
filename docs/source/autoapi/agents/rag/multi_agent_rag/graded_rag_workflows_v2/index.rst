
:py:mod:`agents.rag.multi_agent_rag.graded_rag_workflows_v2`
============================================================

.. py:module:: agents.rag.multi_agent_rag.graded_rag_workflows_v2

Graded RAG Workflows V2 - Using Enhanced State Schemas.

This version uses state schemas with built-in configuration support,
providing a cleaner approach to managing agent-specific parameters.


.. autolink-examples:: agents.rag.multi_agent_rag.graded_rag_workflows_v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.graded_rag_workflows_v2.FLAREAgentV2Example
   agents.rag.multi_agent_rag.graded_rag_workflows_v2.FullyGradedRAGAgentV2
   agents.rag.multi_agent_rag.graded_rag_workflows_v2.MultiCriteriaGradedRAGAgentV2


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FLAREAgentV2Example:

   .. graphviz::
      :align: center

      digraph inheritance_FLAREAgentV2Example {
        node [shape=record];
        "FLAREAgentV2Example" [label="FLAREAgentV2Example"];
        "haive.agents.multi.base.MultiAgent" -> "FLAREAgentV2Example";
        "haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin" -> "FLAREAgentV2Example";
      }

.. autoclass:: agents.rag.multi_agent_rag.graded_rag_workflows_v2.FLAREAgentV2Example
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FullyGradedRAGAgentV2:

   .. graphviz::
      :align: center

      digraph inheritance_FullyGradedRAGAgentV2 {
        node [shape=record];
        "FullyGradedRAGAgentV2" [label="FullyGradedRAGAgentV2"];
        "haive.agents.multi.base.MultiAgent" -> "FullyGradedRAGAgentV2";
        "haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin" -> "FullyGradedRAGAgentV2";
      }

.. autoclass:: agents.rag.multi_agent_rag.graded_rag_workflows_v2.FullyGradedRAGAgentV2
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiCriteriaGradedRAGAgentV2:

   .. graphviz::
      :align: center

      digraph inheritance_MultiCriteriaGradedRAGAgentV2 {
        node [shape=record];
        "MultiCriteriaGradedRAGAgentV2" [label="MultiCriteriaGradedRAGAgentV2"];
        "haive.agents.multi.base.MultiAgent" -> "MultiCriteriaGradedRAGAgentV2";
        "haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin" -> "MultiCriteriaGradedRAGAgentV2";
      }

.. autoclass:: agents.rag.multi_agent_rag.graded_rag_workflows_v2.MultiCriteriaGradedRAGAgentV2
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.graded_rag_workflows_v2.build_custom_graph
   agents.rag.multi_agent_rag.graded_rag_workflows_v2.create_graded_rag_agent

.. py:function:: build_custom_graph() -> Any

   Build custom graph for graded RAG workflows v2.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:

.. py:function:: create_graded_rag_agent(workflow_type: str = 'fully_graded', relevance_threshold: float = 0.5, grading_criteria: list[str] | None = None, **kwargs) -> haive.agents.multi.base.MultiAgent

   Factory function to create graded RAG agents with proper configuration.


   .. autolink-examples:: create_graded_rag_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.graded_rag_workflows_v2
   :collapse:
   
.. autolink-skip:: next
