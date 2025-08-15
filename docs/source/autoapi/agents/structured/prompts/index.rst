agents.structured.prompts
=========================

.. py:module:: agents.structured.prompts

.. autoapi-nested-parse::

   Prompt templates for structured output agents.

   This module provides prompt templates used by structured agents
   to guide the conversion of unstructured text into structured formats.


   .. autolink-examples:: agents.structured.prompts
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.structured.prompts.ANALYSIS_PROMPT
   agents.structured.prompts.DECISION_PROMPT
   agents.structured.prompts.PROMPT_MAPPING
   agents.structured.prompts.STRUCTURED_OUTPUT_PROMPT
   agents.structured.prompts.TASK_PROMPT


Functions
---------

.. autoapisummary::

   agents.structured.prompts.create_contextual_prompt
   agents.structured.prompts.get_prompt_for_model


Module Contents
---------------

.. py:function:: create_contextual_prompt(additional_context: str) -> langchain_core.prompts.ChatPromptTemplate

   Create a prompt with custom context for specific extraction needs.

   :param additional_context: Additional instructions for extraction

   :returns: ChatPromptTemplate with the custom context


   .. autolink-examples:: create_contextual_prompt
      :collapse:

.. py:function:: get_prompt_for_model(model_name: str, custom_context: str | None = None) -> langchain_core.prompts.ChatPromptTemplate

   Get the appropriate prompt for a given output model.

   :param model_name: Name of the output model class
   :param custom_context: Optional custom context to override default

   :returns: ChatPromptTemplate for the model


   .. autolink-examples:: get_prompt_for_model
      :collapse:

.. py:data:: ANALYSIS_PROMPT

.. py:data:: DECISION_PROMPT

.. py:data:: PROMPT_MAPPING

.. py:data:: STRUCTURED_OUTPUT_PROMPT

.. py:data:: TASK_PROMPT

