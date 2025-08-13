
:py:mod:`agents.memory.core.stores`
===================================

.. py:module:: agents.memory.core.stores

Memory store management system integrating with existing Haive store tools.

This module provides enhanced memory storage and retrieval capabilities
that build on the existing store tools with intelligent classification,
self-query retrieval, and memory lifecycle management.


.. autolink-examples:: agents.memory.core.stores
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.core.stores.MemoryStoreConfig
   agents.memory.core.stores.MemoryStoreManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryStoreConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryStoreConfig {
        node [shape=record];
        "MemoryStoreConfig" [label="MemoryStoreConfig"];
        "pydantic.BaseModel" -> "MemoryStoreConfig";
      }

.. autopydantic_model:: agents.memory.core.stores.MemoryStoreConfig
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

   Inheritance diagram for MemoryStoreManager:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryStoreManager {
        node [shape=record];
        "MemoryStoreManager" [label="MemoryStoreManager"];
      }

.. autoclass:: agents.memory.core.stores.MemoryStoreManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.memory.core.stores
   :collapse:
   
.. autolink-skip:: next
