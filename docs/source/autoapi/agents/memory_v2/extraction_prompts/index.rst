
:py:mod:`agents.memory_v2.extraction_prompts`
=============================================

.. py:module:: agents.memory_v2.extraction_prompts

Advanced extraction prompt templates for Memory V2 system.

This module provides sophisticated, focused prompt templates for extracting
different types of information from conversations and documents, specifically
designed for memory-based agents with KG integration.


.. autolink-examples:: agents.memory_v2.extraction_prompts
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_v2.extraction_prompts.ExtractionOrchestrator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ExtractionOrchestrator:

   .. graphviz::
      :align: center

      digraph inheritance_ExtractionOrchestrator {
        node [shape=record];
        "ExtractionOrchestrator" [label="ExtractionOrchestrator"];
      }

.. autoclass:: agents.memory_v2.extraction_prompts.ExtractionOrchestrator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.memory_v2.extraction_prompts.get_all_extraction_types
   agents.memory_v2.extraction_prompts.get_extraction_prompt

.. py:function:: get_all_extraction_types() -> list[str]

   Get list of all available extraction types.


   .. autolink-examples:: get_all_extraction_types
      :collapse:

.. py:function:: get_extraction_prompt(prompt_type: str) -> langchain_core.prompts.ChatPromptTemplate

   Get extraction prompt by type.

   :param prompt_type: One of the available prompt types

   :returns: ChatPromptTemplate for the specified extraction type

   :raises ValueError: If prompt_type is not available


   .. autolink-examples:: get_extraction_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.memory_v2.extraction_prompts
   :collapse:
   
.. autolink-skip:: next
