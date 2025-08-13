
:py:mod:`agents.memory_v2.memory_models_standalone`
===================================================

.. py:module:: agents.memory_v2.memory_models_standalone

Standalone memory models to avoid broken imports.


.. autolink-examples:: agents.memory_v2.memory_models_standalone
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.memory_models_standalone.EnhancedMemoryItem
   agents.memory_v2.memory_models_standalone.ImportanceLevel
   agents.memory_v2.memory_models_standalone.KnowledgeTriple
   agents.memory_v2.memory_models_standalone.MemoryItem
   agents.memory_v2.memory_models_standalone.MemoryType


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

.. autoclass:: agents.memory_v2.memory_models_standalone.EnhancedMemoryItem
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

.. autoclass:: agents.memory_v2.memory_models_standalone.ImportanceLevel
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ImportanceLevel** is an Enum defined in ``agents.memory_v2.memory_models_standalone``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for KnowledgeTriple:

   .. graphviz::
      :align: center

      digraph inheritance_KnowledgeTriple {
        node [shape=record];
        "KnowledgeTriple" [label="KnowledgeTriple"];
        "pydantic.BaseModel" -> "KnowledgeTriple";
      }

.. autopydantic_model:: agents.memory_v2.memory_models_standalone.KnowledgeTriple
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

.. autopydantic_model:: agents.memory_v2.memory_models_standalone.MemoryItem
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

.. autoclass:: agents.memory_v2.memory_models_standalone.MemoryType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemoryType** is an Enum defined in ``agents.memory_v2.memory_models_standalone``.





.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.memory_models_standalone
   :collapse:
   
.. autolink-skip:: next
