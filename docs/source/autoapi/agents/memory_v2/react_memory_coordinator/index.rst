
:py:mod:`agents.memory_v2.react_memory_coordinator`
===================================================

.. py:module:: agents.memory_v2.react_memory_coordinator

ReactAgent Memory Coordinator with Tool Integration.

This implements the ReactAgent version with memory tools as requested:
- Uses ReactAgent for reasoning and planning
- Integrates LongTermMemoryAgent as a tool
- Provides memory search, storage, and analysis capabilities
- Follows the "get into the react version with the tools" directive

Architecture:
- ReactAgent with memory tools for reasoning about memory operations
- LongTermMemoryAgent tool for persistent memory operations
- ConversationMemoryAgent tool for conversation context
- Memory analysis and coordination through ReactAgent reasoning


.. autolink-examples:: agents.memory_v2.react_memory_coordinator
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.react_memory_coordinator.MemoryCoordinatorConfig
   agents.memory_v2.react_memory_coordinator.ReactMemoryCoordinator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryCoordinatorConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryCoordinatorConfig {
        node [shape=record];
        "MemoryCoordinatorConfig" [label="MemoryCoordinatorConfig"];
        "pydantic.BaseModel" -> "MemoryCoordinatorConfig";
      }

.. autopydantic_model:: agents.memory_v2.react_memory_coordinator.MemoryCoordinatorConfig
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

   Inheritance diagram for ReactMemoryCoordinator:

   .. graphviz::
      :align: center

      digraph inheritance_ReactMemoryCoordinator {
        node [shape=record];
        "ReactMemoryCoordinator" [label="ReactMemoryCoordinator"];
      }

.. autoclass:: agents.memory_v2.react_memory_coordinator.ReactMemoryCoordinator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory_v2.react_memory_coordinator.demo_react_memory_coordinator

.. py:function:: demo_react_memory_coordinator()
   :async:


   Demo ReactAgent memory coordinator functionality.


   .. autolink-examples:: demo_react_memory_coordinator
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.react_memory_coordinator
   :collapse:
   
.. autolink-skip:: next
