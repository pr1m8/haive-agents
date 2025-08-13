
:py:mod:`agents.memory_reorganized.core.types`
==============================================

.. py:module:: agents.memory_reorganized.core.types

Memory type definitions and core data structures.

This module defines the fundamental memory types, entry structures, and metadata schemas
used throughout the Haive memory system.


.. autolink-examples:: agents.memory_reorganized.core.types
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.core.types.MemoryClassificationResult
   agents.memory_reorganized.core.types.MemoryConsolidationResult
   agents.memory_reorganized.core.types.MemoryEntry
   agents.memory_reorganized.core.types.MemoryImportance
   agents.memory_reorganized.core.types.MemoryQueryIntent
   agents.memory_reorganized.core.types.MemoryType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryClassificationResult:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryClassificationResult {
        node [shape=record];
        "MemoryClassificationResult" [label="MemoryClassificationResult"];
        "pydantic.BaseModel" -> "MemoryClassificationResult";
      }

.. autopydantic_model:: agents.memory_reorganized.core.types.MemoryClassificationResult
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

   Inheritance diagram for MemoryConsolidationResult:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryConsolidationResult {
        node [shape=record];
        "MemoryConsolidationResult" [label="MemoryConsolidationResult"];
        "pydantic.BaseModel" -> "MemoryConsolidationResult";
      }

.. autopydantic_model:: agents.memory_reorganized.core.types.MemoryConsolidationResult
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

   Inheritance diagram for MemoryEntry:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryEntry {
        node [shape=record];
        "MemoryEntry" [label="MemoryEntry"];
        "pydantic.BaseModel" -> "MemoryEntry";
      }

.. autopydantic_model:: agents.memory_reorganized.core.types.MemoryEntry
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

   Inheritance diagram for MemoryImportance:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryImportance {
        node [shape=record];
        "MemoryImportance" [label="MemoryImportance"];
        "str" -> "MemoryImportance";
        "enum.Enum" -> "MemoryImportance";
      }

.. autoclass:: agents.memory_reorganized.core.types.MemoryImportance
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryImportance** is an Enum defined in ``agents.memory_reorganized.core.types``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryQueryIntent:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryQueryIntent {
        node [shape=record];
        "MemoryQueryIntent" [label="MemoryQueryIntent"];
        "pydantic.BaseModel" -> "MemoryQueryIntent";
      }

.. autopydantic_model:: agents.memory_reorganized.core.types.MemoryQueryIntent
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

.. autoclass:: agents.memory_reorganized.core.types.MemoryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryType** is an Enum defined in ``agents.memory_reorganized.core.types``.





.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.core.types
   :collapse:
   
.. autolink-skip:: next
