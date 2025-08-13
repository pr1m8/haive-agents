
:py:mod:`agents.planning.rewoo_v3.state`
========================================

.. py:module:: agents.planning.rewoo_v3.state

ReWOO V3 State Schema with computed fields for dynamic prompts.

This module defines the state schema for ReWOO V3 Agent using our proven
MessagesState + computed fields pattern from Plan-and-Execute V3 success.


.. autolink-examples:: agents.planning.rewoo_v3.state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.planning.rewoo_v3.state.EvidenceCollection
   agents.planning.rewoo_v3.state.ReWOOPlan
   agents.planning.rewoo_v3.state.ReWOOV3State


Module Contents
---------------

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EvidenceCollection:

   .. graphviz::
      :align: center

      digraph inheritance_EvidenceCollection {
        node [shape=record];
        "EvidenceCollection" [label="EvidenceCollection"];
        "pydantic.BaseModel" -> "EvidenceCollection";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.state.EvidenceCollection
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


:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReWOOPlan:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOPlan {
        node [shape=record];
        "ReWOOPlan" [label="ReWOOPlan"];
        "pydantic.BaseModel" -> "ReWOOPlan";
      }

.. autopydantic_model:: agents.planning.rewoo_v3.state.ReWOOPlan
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

   Inheritance diagram for ReWOOV3State:

   .. graphviz::
      :align: center

      digraph inheritance_ReWOOV3State {
        node [shape=record];
        "ReWOOV3State" [label="ReWOOV3State"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "ReWOOV3State";
      }

.. autoclass:: agents.planning.rewoo_v3.state.ReWOOV3State
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.planning.rewoo_v3.state
   :collapse:
   
.. autolink-skip:: next
