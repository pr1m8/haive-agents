agents.memory_v2.extraction_prompts
===================================

.. py:module:: agents.memory_v2.extraction_prompts

.. autoapi-nested-parse::

   Advanced extraction prompt templates for Memory V2 system.

   This module provides sophisticated, focused prompt templates for extracting
   different types of information from conversations and documents, specifically
   designed for memory-based agents with KG integration.


   .. autolink-examples:: agents.memory_v2.extraction_prompts
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.extraction_prompts.CONVERSATION_SUMMARY_EXTRACTOR
   agents.memory_v2.extraction_prompts.DECISION_MAKING_EXTRACTOR
   agents.memory_v2.extraction_prompts.ENGINEERING_CONTEXT_EXTRACTOR
   agents.memory_v2.extraction_prompts.ENTITY_RELATIONSHIP_EXTRACTOR
   agents.memory_v2.extraction_prompts.EXTRACTION_PROMPTS
   agents.memory_v2.extraction_prompts.PERSONAL_CONTEXT_EXTRACTOR
   agents.memory_v2.extraction_prompts.PRODUCT_MANAGEMENT_EXTRACTOR
   agents.memory_v2.extraction_prompts.PROFESSIONAL_INFORMATION_EXTRACTOR
   agents.memory_v2.extraction_prompts.PROJECT_AND_TASK_EXTRACTOR
   agents.memory_v2.extraction_prompts.SENTIMENT_AND_TONE_EXTRACTOR
   agents.memory_v2.extraction_prompts.TECHNICAL_KNOWLEDGE_EXTRACTOR


Classes
-------

.. autoapisummary::

   agents.memory_v2.extraction_prompts.ExtractionOrchestrator


Functions
---------

.. autoapisummary::

   agents.memory_v2.extraction_prompts.get_all_extraction_types
   agents.memory_v2.extraction_prompts.get_extraction_prompt


Module Contents
---------------

.. py:class:: ExtractionOrchestrator(llm_config=None)

   Orchestrates multiple extraction types on the same content.

   Initialize with LLM configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExtractionOrchestrator
      :collapse:

   .. py:method:: extract_all(conversation_text: str, extraction_types: list[str] | None = None) -> dict[str, Any]
      :async:


      Run multiple extractors on the same conversation.

      :param conversation_text: The conversation to analyze
      :param extraction_types: Which extractors to run (default: all)

      :returns: Dictionary with results from each extractor


      .. autolink-examples:: extract_all
         :collapse:


   .. py:method:: get_focused_extractors(domain: str) -> list[str]

      Get recommended extractors for a specific domain.

      :param domain: Domain type (e.g., 'product', 'engineering', 'general')

      :returns: List of recommended extraction types


      .. autolink-examples:: get_focused_extractors
         :collapse:


   .. py:attribute:: llm_config
      :value: None



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

.. py:data:: CONVERSATION_SUMMARY_EXTRACTOR

.. py:data:: DECISION_MAKING_EXTRACTOR

.. py:data:: ENGINEERING_CONTEXT_EXTRACTOR

.. py:data:: ENTITY_RELATIONSHIP_EXTRACTOR

.. py:data:: EXTRACTION_PROMPTS

.. py:data:: PERSONAL_CONTEXT_EXTRACTOR

.. py:data:: PRODUCT_MANAGEMENT_EXTRACTOR

.. py:data:: PROFESSIONAL_INFORMATION_EXTRACTOR

.. py:data:: PROJECT_AND_TASK_EXTRACTOR

.. py:data:: SENTIMENT_AND_TONE_EXTRACTOR

.. py:data:: TECHNICAL_KNOWLEDGE_EXTRACTOR

