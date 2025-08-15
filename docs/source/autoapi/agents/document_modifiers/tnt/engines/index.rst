agents.document_modifiers.tnt.engines
=====================================

.. py:module:: agents.document_modifiers.tnt.engines

.. autoapi-nested-parse::

   Augmented LLM configurations for taxonomy generation.

   This module defines the prompt templates and configurations for various LLM-based
   tasks in the taxonomy generation process. It includes configurations for:
   - Document summarization
   - Taxonomy generation
   - Taxonomy updating
   - Taxonomy review
   - Document classification

   Each configuration combines specific prompt templates with output parsing and
   post-processing logic.

   .. rubric:: Example

   Basic usage of augmented LLM configs::

       summary_config = summary_aug_llm_config
       llm = summary_config.create_runnable()
       result = llm.invoke({"content": "text to summarize"})


   .. autolink-examples:: agents.document_modifiers.tnt.engines
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.document_modifiers.tnt.engines.SUMMARY_HUMAN_MESSAGE
   agents.document_modifiers.tnt.engines.SUMMARY_PROMPT_TEMPLATE
   agents.document_modifiers.tnt.engines.SUMMARY_SYSTEM_MESSAGE
   agents.document_modifiers.tnt.engines.TAXONOMY_CLASSIFICATION_HUMAN_MESSAGE
   agents.document_modifiers.tnt.engines.TAXONOMY_CLASSIFICATION_PROMPT
   agents.document_modifiers.tnt.engines.TAXONOMY_CLASSIFICATION_SYSTEM_MESSAGE
   agents.document_modifiers.tnt.engines.TAXONOMY_GENERATION_HUMAN_MESSAGE
   agents.document_modifiers.tnt.engines.TAXONOMY_GENERATION_PROMPT_TEMPLATE
   agents.document_modifiers.tnt.engines.TAXONOMY_GENERATION_SYSTEM_MESSAGE
   agents.document_modifiers.tnt.engines.TAXONOMY_REVIEW_HUMAN_MESSAGE
   agents.document_modifiers.tnt.engines.TAXONOMY_REVIEW_PROMPT_TEMPLATE
   agents.document_modifiers.tnt.engines.TAXONOMY_REVIEW_SYSTEM_MESSAGE
   agents.document_modifiers.tnt.engines.TAXONOMY_UPDATE_HUMAN_MESSAGE
   agents.document_modifiers.tnt.engines.TAXONOMY_UPDATE_PROMPT_TEMPLATE
   agents.document_modifiers.tnt.engines.TAXONOMY_UPDATE_SYSTEM_MESSAGE
   agents.document_modifiers.tnt.engines.summary_aug_llm_config
   agents.document_modifiers.tnt.engines.taxonomy_classification_aug_llm_config
   agents.document_modifiers.tnt.engines.taxonomy_generation_aug_llm_config
   agents.document_modifiers.tnt.engines.taxonomy_review_aug_llm_config
   agents.document_modifiers.tnt.engines.taxonomy_update_aug_llm_config


Module Contents
---------------

.. py:data:: SUMMARY_HUMAN_MESSAGE

.. py:data:: SUMMARY_PROMPT_TEMPLATE

.. py:data:: SUMMARY_SYSTEM_MESSAGE

.. py:data:: TAXONOMY_CLASSIFICATION_HUMAN_MESSAGE

.. py:data:: TAXONOMY_CLASSIFICATION_PROMPT

.. py:data:: TAXONOMY_CLASSIFICATION_SYSTEM_MESSAGE

.. py:data:: TAXONOMY_GENERATION_HUMAN_MESSAGE

.. py:data:: TAXONOMY_GENERATION_PROMPT_TEMPLATE

.. py:data:: TAXONOMY_GENERATION_SYSTEM_MESSAGE

.. py:data:: TAXONOMY_REVIEW_HUMAN_MESSAGE

.. py:data:: TAXONOMY_REVIEW_PROMPT_TEMPLATE

.. py:data:: TAXONOMY_REVIEW_SYSTEM_MESSAGE

.. py:data:: TAXONOMY_UPDATE_HUMAN_MESSAGE

.. py:data:: TAXONOMY_UPDATE_PROMPT_TEMPLATE

.. py:data:: TAXONOMY_UPDATE_SYSTEM_MESSAGE

.. py:data:: summary_aug_llm_config

.. py:data:: taxonomy_classification_aug_llm_config

.. py:data:: taxonomy_generation_aug_llm_config

.. py:data:: taxonomy_review_aug_llm_config

.. py:data:: taxonomy_update_aug_llm_config

