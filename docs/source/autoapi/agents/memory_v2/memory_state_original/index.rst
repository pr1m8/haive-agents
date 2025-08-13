
:py:mod:`agents.memory_v2.memory_state_original`
================================================

.. py:module:: agents.memory_v2.memory_state_original

Memory state models for Memory V2 system using original Haive memory models.

This module integrates the proven memory models from haive.agents.memory.models
and haive.agents.ltm.memory_schemas with our V2 enhancements for token tracking,
graph integration, and advanced memory management.


.. autolink-examples:: agents.memory_v2.memory_state_original
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.memory_state_original.EnhancedKnowledgeTriple
   agents.memory_v2.memory_state_original.EnhancedMemoryItem
   agents.memory_v2.memory_state_original.ImportanceLevel
   agents.memory_v2.memory_state_original.KnowledgeTriple
   agents.memory_v2.memory_state_original.MemoryItem
   agents.memory_v2.memory_state_original.MemoryState
   agents.memory_v2.memory_state_original.MemoryStats
   agents.memory_v2.memory_state_original.MemoryType
   agents.memory_v2.memory_state_original.UnifiedMemoryEntry


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedKnowledgeTriple:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedKnowledgeTriple {
        node [shape=record];
        "EnhancedKnowledgeTriple" [label="EnhancedKnowledgeTriple"];
        "agents.memory_v2.memory_models_standalone.KnowledgeTriple" -> "EnhancedKnowledgeTriple";
      }

.. autoclass:: agents.memory_v2.memory_state_original.EnhancedKnowledgeTriple
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedMemoryItem:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedMemoryItem {
        node [shape=record];
        "EnhancedMemoryItem" [label="EnhancedMemoryItem"];
        "MemoryItem" -> "EnhancedMemoryItem";
      }

.. autoclass:: agents.memory_v2.memory_state_original.EnhancedMemoryItem
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ImportanceLevel:

   .. graphviz::
      :align: center

      digraph inheritance_ImportanceLevel {
        node [shape=record];
        "ImportanceLevel" [label="ImportanceLevel"];
        "str" -> "ImportanceLevel";
        "enum.Enum" -> "ImportanceLevel";
      }

.. autoclass:: agents.memory_v2.memory_state_original.ImportanceLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ImportanceLevel** is an Enum defined in ``agents.memory_v2.memory_state_original``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for KnowledgeTriple:

   .. graphviz::
      :align: center

      digraph inheritance_KnowledgeTriple {
        node [shape=record];
        "KnowledgeTriple" [label="KnowledgeTriple"];
        "pydantic.BaseModel" -> "KnowledgeTriple";
      }

.. autopydantic_model:: agents.memory_v2.memory_state_original.KnowledgeTriple
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

   Inheritance diagram for MemoryItem:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryItem {
        node [shape=record];
        "MemoryItem" [label="MemoryItem"];
        "pydantic.BaseModel" -> "MemoryItem";
      }

.. autopydantic_model:: agents.memory_v2.memory_state_original.MemoryItem
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
        "pydantic.BaseModel" -> "MemoryState";
      }

.. autopydantic_model:: agents.memory_v2.memory_state_original.MemoryState
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

   Inheritance diagram for MemoryStats:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryStats {
        node [shape=record];
        "MemoryStats" [label="MemoryStats"];
        "pydantic.BaseModel" -> "MemoryStats";
      }

.. autopydantic_model:: agents.memory_v2.memory_state_original.MemoryStats
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

   Inheritance diagram for MemoryType:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryType {
        node [shape=record];
        "MemoryType" [label="MemoryType"];
        "str" -> "MemoryType";
        "enum.Enum" -> "MemoryType";
      }

.. autoclass:: agents.memory_v2.memory_state_original.MemoryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryType** is an Enum defined in ``agents.memory_v2.memory_state_original``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for UnifiedMemoryEntry:

   .. graphviz::
      :align: center

      digraph inheritance_UnifiedMemoryEntry {
        node [shape=record];
        "UnifiedMemoryEntry" [label="UnifiedMemoryEntry"];
        "pydantic.BaseModel" -> "UnifiedMemoryEntry";
      }

.. autopydantic_model:: agents.memory_v2.memory_state_original.UnifiedMemoryEntry
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

.. autolink-examples:: agents.memory_v2.memory_state_original
   :collapse:
   
.. autolink-skip:: next
