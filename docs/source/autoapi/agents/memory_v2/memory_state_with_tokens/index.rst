
:py:mod:`agents.memory_v2.memory_state_with_tokens`
===================================================

.. py:module:: agents.memory_v2.memory_state_with_tokens

Memory state with integrated token tracking and summarization hooks.

This module extends MessagesStateWithTokenUsage to add memory-specific
functionality with pre-hooks for summarization and token management.


.. autolink-examples:: agents.memory_v2.memory_state_with_tokens
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens
   agents.memory_v2.memory_state_with_tokens.MemoryStats
   agents.memory_v2.memory_state_with_tokens.UnifiedMemoryEntry


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryStateWithTokens:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryStateWithTokens {
        node [shape=record];
        "MemoryStateWithTokens" [label="MemoryStateWithTokens"];
        "haive.core.schema.prebuilt.messages.messages_with_token_usage.MessagesStateWithTokenUsage" -> "MemoryStateWithTokens";
      }

.. autoclass:: agents.memory_v2.memory_state_with_tokens.MemoryStateWithTokens
   :members:
   :undoc-members:
   :show-inheritance:

:orphan:



.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryStats:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryStats {
        node [shape=record];
        "MemoryStats" [label="MemoryStats"];
        "pydantic.BaseModel" -> "MemoryStats";
      }

.. autopydantic_model:: agents.memory_v2.memory_state_with_tokens.MemoryStats
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

   Inheritance diagram for UnifiedMemoryEntry:

   .. graphviz::
      :align: center

      digraph inheritance_UnifiedMemoryEntry {
        node [shape=record];
        "UnifiedMemoryEntry" [label="UnifiedMemoryEntry"];
        "pydantic.BaseModel" -> "UnifiedMemoryEntry";
      }

.. autopydantic_model:: agents.memory_v2.memory_state_with_tokens.UnifiedMemoryEntry
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

.. autolink-examples:: agents.memory_v2.memory_state_with_tokens
   :collapse:
   
.. autolink-skip:: next
