
:py:mod:`agents.memory_reorganized.base.memory_state`
=====================================================

.. py:module:: agents.memory_reorganized.base.memory_state

Memory state models for Memory V2 system using original Haive memory models.

This module integrates the proven memory models from haive.agents.memory.models and
haive.agents.ltm.memory_schemas with our V2 enhancements for token tracking, graph
integration, and advanced memory management.


.. autolink-examples:: agents.memory_reorganized.base.memory_state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.base.memory_state.MemoryEntry
   agents.memory_reorganized.base.memory_state.MemoryMetadata
   agents.memory_reorganized.base.memory_state.MemoryState
   agents.memory_reorganized.base.memory_state.MemoryStats


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryEntry:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryEntry {
        node [shape=record];
        "MemoryEntry" [label="MemoryEntry"];
        "pydantic.BaseModel" -> "MemoryEntry";
      }

.. autopydantic_model:: agents.memory_reorganized.base.memory_state.MemoryEntry
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

   Inheritance diagram for MemoryMetadata:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryMetadata {
        node [shape=record];
        "MemoryMetadata" [label="MemoryMetadata"];
        "pydantic.BaseModel" -> "MemoryMetadata";
      }

.. autopydantic_model:: agents.memory_reorganized.base.memory_state.MemoryMetadata
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

   Inheritance diagram for MemoryState:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryState {
        node [shape=record];
        "MemoryState" [label="MemoryState"];
        "MessagesState" -> "MemoryState";
      }

.. autoclass:: agents.memory_reorganized.base.memory_state.MemoryState
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryStats:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryStats {
        node [shape=record];
        "MemoryStats" [label="MemoryStats"];
        "pydantic.BaseModel" -> "MemoryStats";
      }

.. autopydantic_model:: agents.memory_reorganized.base.memory_state.MemoryStats
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

.. autolink-examples:: agents.memory_reorganized.base.memory_state
   :collapse:
   
.. autolink-skip:: next
