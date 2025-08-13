
:py:mod:`agents.memory_v2.multi_memory_coordinator`
===================================================

.. py:module:: agents.memory_v2.multi_memory_coordinator

Multi-Memory Agent Coordinator - Orchestrates all memory systems.

This is the top-level coordinator that manages all memory agents:
- SimpleMemoryAgent (pre-hook system)
- ReactMemoryAgent (tool-based memory)
- LongTermMemoryAgent (persistent memory)
- GraphMemoryAgent (structured knowledge)
- AdvancedRAGMemoryAgent (multi-stage retrieval)

The coordinator intelligently routes operations to the most appropriate
memory system and can combine results from multiple systems.


.. autolink-examples:: agents.memory_v2.multi_memory_coordinator
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.multi_memory_coordinator.CoordinationMode
   agents.memory_v2.multi_memory_coordinator.MemorySystemType
   agents.memory_v2.multi_memory_coordinator.MultiMemoryConfig
   agents.memory_v2.multi_memory_coordinator.MultiMemoryCoordinator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CoordinationMode:

   .. graphviz::
      :align: center

      digraph inheritance_CoordinationMode {
        node [shape=record];
        "CoordinationMode" [label="CoordinationMode"];
        "str" -> "CoordinationMode";
        "enum.Enum" -> "CoordinationMode";
      }

.. autoclass:: agents.memory_v2.multi_memory_coordinator.CoordinationMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **CoordinationMode** is an Enum defined in ``agents.memory_v2.multi_memory_coordinator``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemorySystemType:

   .. graphviz::
      :align: center

      digraph inheritance_MemorySystemType {
        node [shape=record];
        "MemorySystemType" [label="MemorySystemType"];
        "str" -> "MemorySystemType";
        "enum.Enum" -> "MemorySystemType";
      }

.. autoclass:: agents.memory_v2.multi_memory_coordinator.MemorySystemType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemorySystemType** is an Enum defined in ``agents.memory_v2.multi_memory_coordinator``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiMemoryConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MultiMemoryConfig {
        node [shape=record];
        "MultiMemoryConfig" [label="MultiMemoryConfig"];
      }

.. autoclass:: agents.memory_v2.multi_memory_coordinator.MultiMemoryConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiMemoryCoordinator:

   .. graphviz::
      :align: center

      digraph inheritance_MultiMemoryCoordinator {
        node [shape=record];
        "MultiMemoryCoordinator" [label="MultiMemoryCoordinator"];
      }

.. autoclass:: agents.memory_v2.multi_memory_coordinator.MultiMemoryCoordinator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory_v2.multi_memory_coordinator.demo_multi_memory_coordinator

.. py:function:: demo_multi_memory_coordinator()
   :async:


   Demonstrate the multi-memory coordinator.


   .. autolink-examples:: demo_multi_memory_coordinator
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.multi_memory_coordinator
   :collapse:
   
.. autolink-skip:: next
