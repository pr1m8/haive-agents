
:py:mod:`agents.rag.multi_agent_rag.enhanced_state_schemas`
===========================================================

.. py:module:: agents.rag.multi_agent_rag.enhanced_state_schemas

Enhanced State Schemas with Configuration Support.

This module provides state schemas that include configuration fields,
solving the issue of storing agent-specific configuration in a clean way.


.. autolink-examples:: agents.rag.multi_agent_rag.enhanced_state_schemas
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_state_schemas.AdaptiveThresholdRAGState
   agents.rag.multi_agent_rag.enhanced_state_schemas.ConfigurableRAGState
   agents.rag.multi_agent_rag.enhanced_state_schemas.DebateRAGState
   agents.rag.multi_agent_rag.enhanced_state_schemas.DynamicRAGState
   agents.rag.multi_agent_rag.enhanced_state_schemas.FLAREState
   agents.rag.multi_agent_rag.enhanced_state_schemas.GradedRAGState
   agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AdaptiveThresholdRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_AdaptiveThresholdRAGState {
        node [shape=record];
        "AdaptiveThresholdRAGState" [label="AdaptiveThresholdRAGState"];
        "DynamicRAGState" -> "AdaptiveThresholdRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_state_schemas.AdaptiveThresholdRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableRAGState {
        node [shape=record];
        "ConfigurableRAGState" [label="ConfigurableRAGState"];
        "haive.core.schema.prebuilt.rag_state.RAGState" -> "ConfigurableRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_state_schemas.ConfigurableRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebateRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_DebateRAGState {
        node [shape=record];
        "DebateRAGState" [label="DebateRAGState"];
        "ConfigurableRAGState" -> "DebateRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_state_schemas.DebateRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicRAGState {
        node [shape=record];
        "DynamicRAGState" [label="DynamicRAGState"];
        "ConfigurableRAGState" -> "DynamicRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_state_schemas.DynamicRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FLAREState:

   .. graphviz::
      :align: center

      digraph inheritance_FLAREState {
        node [shape=record];
        "FLAREState" [label="FLAREState"];
        "ConfigurableRAGState" -> "FLAREState";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_state_schemas.FLAREState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GradedRAGState:

   .. graphviz::
      :align: center

      digraph inheritance_GradedRAGState {
        node [shape=record];
        "GradedRAGState" [label="GradedRAGState"];
        "ConfigurableRAGState" -> "GradedRAGState";
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_state_schemas.GradedRAGState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StateConfigMixin:

   .. graphviz::
      :align: center

      digraph inheritance_StateConfigMixin {
        node [shape=record];
        "StateConfigMixin" [label="StateConfigMixin"];
      }

.. autoclass:: agents.rag.multi_agent_rag.enhanced_state_schemas.StateConfigMixin
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.multi_agent_rag.enhanced_state_schemas.create_configured_state

.. py:function:: create_configured_state(state_class: type[ConfigurableRAGState], agent_name: str, workflow_type: str, **config_kwargs) -> ConfigurableRAGState

   Create a state instance with configuration.


   .. autolink-examples:: create_configured_state
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.multi_agent_rag.enhanced_state_schemas
   :collapse:
   
.. autolink-skip:: next
