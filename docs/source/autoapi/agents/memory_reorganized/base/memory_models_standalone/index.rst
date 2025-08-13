
:py:mod:`agents.memory_reorganized.base.memory_models_standalone`
=================================================================

.. py:module:: agents.memory_reorganized.base.memory_models_standalone

Standalone memory models for the reorganized memory system.

This module provides core memory models that are used throughout the memory system,
designed to be standalone without heavy dependencies to avoid circular imports.


.. autolink-examples:: agents.memory_reorganized.base.memory_models_standalone
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.base.memory_models_standalone.EnhancedMemoryItem
   agents.memory_reorganized.base.memory_models_standalone.ImportanceLevel
   agents.memory_reorganized.base.memory_models_standalone.KnowledgeTriple
   agents.memory_reorganized.base.memory_models_standalone.MemoryItem
   agents.memory_reorganized.base.memory_models_standalone.MemoryType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedMemoryItem:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedMemoryItem {
        node [shape=record];
        "EnhancedMemoryItem" [label="EnhancedMemoryItem"];
        "MemoryItem" -> "EnhancedMemoryItem";
      }

.. autoclass:: agents.memory_reorganized.base.memory_models_standalone.EnhancedMemoryItem
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

.. autoclass:: agents.memory_reorganized.base.memory_models_standalone.ImportanceLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ImportanceLevel** is an Enum defined in ``agents.memory_reorganized.base.memory_models_standalone``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for KnowledgeTriple:

   .. graphviz::
      :align: center

      digraph inheritance_KnowledgeTriple {
        node [shape=record];
        "KnowledgeTriple" [label="KnowledgeTriple"];
        "pydantic.BaseModel" -> "KnowledgeTriple";
      }

.. autopydantic_model:: agents.memory_reorganized.base.memory_models_standalone.KnowledgeTriple
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

.. autopydantic_model:: agents.memory_reorganized.base.memory_models_standalone.MemoryItem
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

.. autoclass:: agents.memory_reorganized.base.memory_models_standalone.MemoryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryType** is an Enum defined in ``agents.memory_reorganized.base.memory_models_standalone``.



Functions
---------

.. autoapisummary::

   agents.memory_reorganized.base.memory_models_standalone.create_knowledge_triple
   agents.memory_reorganized.base.memory_models_standalone.create_memory_item
   agents.memory_reorganized.base.memory_models_standalone.merge_memory_items

.. py:function:: create_knowledge_triple(subject: str, predicate: str, object: str, confidence: float = 1.0, source: str | None = None) -> KnowledgeTriple

   Create a knowledge triple.


   .. autolink-examples:: create_knowledge_triple
      :collapse:

.. py:function:: create_memory_item(content: str, memory_type: MemoryType = MemoryType.SEMANTIC, importance: ImportanceLevel = ImportanceLevel.MEDIUM, tags: list[str] | None = None, context_id: str | None = None, user_id: str | None = None, source: str | None = None, enhanced: bool = False) -> MemoryItem | EnhancedMemoryItem

   Create a memory item with the specified parameters.


   .. autolink-examples:: create_memory_item
      :collapse:

.. py:function:: merge_memory_items(items: list[MemoryItem]) -> EnhancedMemoryItem

   Merge multiple memory items into one enhanced memory item.


   .. autolink-examples:: merge_memory_items
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.base.memory_models_standalone
   :collapse:
   
.. autolink-skip:: next
