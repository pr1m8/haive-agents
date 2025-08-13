
:py:mod:`agents.rag.multi_agent_rag.specialized_workflows_v2`
=============================================================

.. py:module:: agents.rag.multi_agent_rag.specialized_workflows_v2

Specialized Workflows V2 - Using Enhanced State Schemas.

Updated versions of FLARE, Dynamic RAG, Debate RAG, etc. using
state schemas with built-in configuration support.


.. autolink-examples:: agents.rag.multi_agent_rag.specialized_workflows_v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.specialized_workflows_v2.AdaptiveThresholdRAGAgentV2
   agents.rag.multi_agent_rag.specialized_workflows_v2.DebateRAGAgentV2
   agents.rag.multi_agent_rag.specialized_workflows_v2.DynamicRAGAgentV2
   agents.rag.multi_agent_rag.specialized_workflows_v2.FLAREAgentV2


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveThresholdRAGAgentV2:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveThresholdRAGAgentV2 {
        node [shape=record];
        "AdaptiveThresholdRAGAgentV2" [label="AdaptiveThresholdRAGAgentV2"];
        "haive.agents.multi.base.MultiAgent" -> "AdaptiveThresholdRAGAgentV2";
        "haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin" -> "AdaptiveThresholdRAGAgentV2";
      }

.. autoclass:: agents.rag.multi_agent_rag.specialized_workflows_v2.AdaptiveThresholdRAGAgentV2
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebateRAGAgentV2:

   .. graphviz::
      :align: center

      digraph inheritance_DebateRAGAgentV2 {
        node [shape=record];
        "DebateRAGAgentV2" [label="DebateRAGAgentV2"];
        "haive.agents.multi.base.MultiAgent" -> "DebateRAGAgentV2";
        "haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin" -> "DebateRAGAgentV2";
      }

.. autoclass:: agents.rag.multi_agent_rag.specialized_workflows_v2.DebateRAGAgentV2
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicRAGAgentV2:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicRAGAgentV2 {
        node [shape=record];
        "DynamicRAGAgentV2" [label="DynamicRAGAgentV2"];
        "haive.agents.multi.base.MultiAgent" -> "DynamicRAGAgentV2";
        "haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin" -> "DynamicRAGAgentV2";
      }

.. autoclass:: agents.rag.multi_agent_rag.specialized_workflows_v2.DynamicRAGAgentV2
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FLAREAgentV2:

   .. graphviz::
      :align: center

      digraph inheritance_FLAREAgentV2 {
        node [shape=record];
        "FLAREAgentV2" [label="FLAREAgentV2"];
        "haive.agents.multi.base.MultiAgent" -> "FLAREAgentV2";
        "haive.agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin" -> "FLAREAgentV2";
      }

.. autoclass:: agents.rag.multi_agent_rag.specialized_workflows_v2.FLAREAgentV2
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.specialized_workflows_v2.build_custom_graph

.. py:function:: build_custom_graph() -> Any

   Build custom graph for specialized workflows v2.

   :returns: Graph configuration or None for default behavior


   .. autolink-examples:: build_custom_graph
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.specialized_workflows_v2
   :collapse:
   
.. autolink-skip:: next
