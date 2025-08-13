
:py:mod:`agents.rag.utils.structured_output_enhancer`
=====================================================

.. py:module:: agents.rag.utils.structured_output_enhancer

Structured Output Enhancer for RAG Agents.

from typing import Any, Dict
This utility enables any agent to be enhanced with structured output by appending
a SimpleAgent with the appropriate prompt template and Pydantic model. This follows
the pattern of keeping prompts focused on generation while parsers handle structure.


.. autolink-examples:: agents.rag.utils.structured_output_enhancer
   :collapse:

Classes
-------

.. autoapisummary::

   agents.rag.utils.structured_output_enhancer.RAGEnhancementFactory
   agents.rag.utils.structured_output_enhancer.StructuredOutputEnhancer


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RAGEnhancementFactory:

   .. graphviz::
      :align: center

      digraph inheritance_RAGEnhancementFactory {
        node [shape=record];
        "RAGEnhancementFactory" [label="RAGEnhancementFactory"];
      }

.. autoclass:: agents.rag.utils.structured_output_enhancer.RAGEnhancementFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StructuredOutputEnhancer:

   .. graphviz::
      :align: center

      digraph inheritance_StructuredOutputEnhancer {
        node [shape=record];
        "StructuredOutputEnhancer" [label="StructuredOutputEnhancer"];
      }

.. autoclass:: agents.rag.utils.structured_output_enhancer.StructuredOutputEnhancer
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.rag.utils.structured_output_enhancer.create_fusion_enhancer
   agents.rag.utils.structured_output_enhancer.create_hyde_enhancer
   agents.rag.utils.structured_output_enhancer.create_memory_enhancer
   agents.rag.utils.structured_output_enhancer.create_speculative_enhancer
   agents.rag.utils.structured_output_enhancer.demonstrate_enhancement_patterns

.. py:function:: create_fusion_enhancer() -> StructuredOutputEnhancer

   Create an enhancer for Fusion RAG structured output.


   .. autolink-examples:: create_fusion_enhancer
      :collapse:

.. py:function:: create_hyde_enhancer() -> StructuredOutputEnhancer

   Create an enhancer for HyDE structured output.


   .. autolink-examples:: create_hyde_enhancer
      :collapse:

.. py:function:: create_memory_enhancer() -> StructuredOutputEnhancer

   Create an enhancer for Memory-aware RAG structured output.


   .. autolink-examples:: create_memory_enhancer
      :collapse:

.. py:function:: create_speculative_enhancer() -> StructuredOutputEnhancer

   Create an enhancer for Speculative RAG structured output.


   .. autolink-examples:: create_speculative_enhancer
      :collapse:

.. py:function:: demonstrate_enhancement_patterns() -> dict[str, Any]

   Demonstrate various enhancement patterns.


   .. autolink-examples:: demonstrate_enhancement_patterns
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.rag.utils.structured_output_enhancer
   :collapse:
   
.. autolink-skip:: next
