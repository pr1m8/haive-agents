
:py:mod:`agents.memory_v2.token_tracker`
========================================

.. py:module:: agents.memory_v2.token_tracker

Token tracking component for memory operations.

Monitors token usage across memory operations and triggers
summarization or rewriting when approaching context limits.


.. autolink-examples:: agents.memory_v2.token_tracker
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.token_tracker.TokenThresholds
   agents.memory_v2.token_tracker.TokenTracker
   agents.memory_v2.token_tracker.TokenUsageEntry


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TokenThresholds:

   .. graphviz::
      :align: center

      digraph inheritance_TokenThresholds {
        node [shape=record];
        "TokenThresholds" [label="TokenThresholds"];
        "pydantic.BaseModel" -> "TokenThresholds";
      }

.. autopydantic_model:: agents.memory_v2.token_tracker.TokenThresholds
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

   Inheritance diagram for TokenTracker:

   .. graphviz::
      :align: center

      digraph inheritance_TokenTracker {
        node [shape=record];
        "TokenTracker" [label="TokenTracker"];
        "pydantic.BaseModel" -> "TokenTracker";
      }

.. autopydantic_model:: agents.memory_v2.token_tracker.TokenTracker
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

   Inheritance diagram for TokenUsageEntry:

   .. graphviz::
      :align: center

      digraph inheritance_TokenUsageEntry {
        node [shape=record];
        "TokenUsageEntry" [label="TokenUsageEntry"];
        "pydantic.BaseModel" -> "TokenUsageEntry";
      }

.. autopydantic_model:: agents.memory_v2.token_tracker.TokenUsageEntry
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

.. autolink-examples:: agents.memory_v2.token_tracker
   :collapse:
   
.. autolink-skip:: next
