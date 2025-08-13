
:py:mod:`agents.document_modifiers.tnt.engines`
===============================================

.. py:module:: agents.document_modifiers.tnt.engines

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




