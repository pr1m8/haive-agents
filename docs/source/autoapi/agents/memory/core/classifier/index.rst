
:py:mod:`agents.memory.core.classifier`
=======================================

.. py:module:: agents.memory.core.classifier

Memory classification system using LLM-based analysis.

This module provides intelligent classification of memories into types,
importance scoring, and metadata extraction using language models.


.. autolink-examples:: agents.memory.core.classifier
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory.core.classifier.MemoryClassifier
   agents.memory.core.classifier.MemoryClassifierConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryClassifier:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryClassifier {
        node [shape=record];
        "MemoryClassifier" [label="MemoryClassifier"];
      }

.. autoclass:: agents.memory.core.classifier.MemoryClassifier
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryClassifierConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryClassifierConfig {
        node [shape=record];
        "MemoryClassifierConfig" [label="MemoryClassifierConfig"];
        "pydantic.BaseModel" -> "MemoryClassifierConfig";
      }

.. autopydantic_model:: agents.memory.core.classifier.MemoryClassifierConfig
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

.. autolink-examples:: agents.memory.core.classifier
   :collapse:
   
.. autolink-skip:: next
