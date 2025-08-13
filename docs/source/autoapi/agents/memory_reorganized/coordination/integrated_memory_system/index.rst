
:py:mod:`agents.memory_reorganized.coordination.integrated_memory_system`
=========================================================================

.. py:module:: agents.memory_reorganized.coordination.integrated_memory_system

Integrated Memory System combining Graph, Vector, and Time-based memory.

This system shows how to use multiple memory strategies together:
1. GraphMemoryAgent for structured knowledge and relationships
2. ReactMemoryAgent for flexible tool-based memory management
3. LongTermMemoryAgent for persistent cross-conversation memory


.. autolink-examples:: agents.memory_reorganized.coordination.integrated_memory_system
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.coordination.integrated_memory_system.IntegratedMemorySystem
   agents.memory_reorganized.coordination.integrated_memory_system.MemorySystemMode


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for IntegratedMemorySystem:

   .. graphviz::
      :align: center

      digraph inheritance_IntegratedMemorySystem {
        node [shape=record];
        "IntegratedMemorySystem" [label="IntegratedMemorySystem"];
      }

.. autoclass:: agents.memory_reorganized.coordination.integrated_memory_system.IntegratedMemorySystem
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemorySystemMode:

   .. graphviz::
      :align: center

      digraph inheritance_MemorySystemMode {
        node [shape=record];
        "MemorySystemMode" [label="MemorySystemMode"];
        "str" -> "MemorySystemMode";
        "enum.Enum" -> "MemorySystemMode";
      }

.. autoclass:: agents.memory_reorganized.coordination.integrated_memory_system.MemorySystemMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MemorySystemMode** is an Enum defined in ``agents.memory_reorganized.coordination.integrated_memory_system``.



Functions
---------

.. autoapisummary::

   agents.memory_reorganized.coordination.integrated_memory_system.create_research_assistant
   agents.memory_reorganized.coordination.integrated_memory_system.demo_integrated_memory

.. py:function:: create_research_assistant()
   :async:


   Create a research assistant with integrated memory.


   .. autolink-examples:: create_research_assistant
      :collapse:

.. py:function:: demo_integrated_memory()
   :async:


   Demonstrate the integrated memory system.


   .. autolink-examples:: demo_integrated_memory
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.coordination.integrated_memory_system
   :collapse:
   
.. autolink-skip:: next
