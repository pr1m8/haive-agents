
:py:mod:`hyde.enhanced_prompts`
===============================

.. py:module:: hyde.enhanced_prompts

Enhanced HyDE prompts based on LangChain best practices.

This module provides improved HyDE prompt templates that follow the principle
of separating document generation from structured output parsing.

Key improvements:
- Simplified generation prompts focused on content creation
- Domain-specific prompt templates
- Separate analysis/parsing prompts for structured output
- Multi-perspective generation support
- Controlled document length


.. autolink-examples:: hyde.enhanced_prompts
   :collapse:

Classes
-------

.. autoapisummary::

   hyde.enhanced_prompts.HyDEPerspective
   hyde.enhanced_prompts.HyDEPromptConfig
   hyde.enhanced_prompts.HyDEPromptType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HyDEPerspective:

   .. graphviz::
      :align: center

      digraph inheritance_HyDEPerspective {
        node [shape=record];
        "HyDEPerspective" [label="HyDEPerspective"];
        "str" -> "HyDEPerspective";
        "enum.Enum" -> "HyDEPerspective";
      }

.. autoclass:: hyde.enhanced_prompts.HyDEPerspective
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **HyDEPerspective** is an Enum defined in ``hyde.enhanced_prompts``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HyDEPromptConfig:

   .. graphviz::
      :align: center

      digraph inheritance_HyDEPromptConfig {
        node [shape=record];
        "HyDEPromptConfig" [label="HyDEPromptConfig"];
        "pydantic.BaseModel" -> "HyDEPromptConfig";
      }

.. autopydantic_model:: hyde.enhanced_prompts.HyDEPromptConfig
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

   Inheritance diagram for HyDEPromptType:

   .. graphviz::
      :align: center

      digraph inheritance_HyDEPromptType {
        node [shape=record];
        "HyDEPromptType" [label="HyDEPromptType"];
        "str" -> "HyDEPromptType";
        "enum.Enum" -> "HyDEPromptType";
      }

.. autoclass:: hyde.enhanced_prompts.HyDEPromptType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **HyDEPromptType** is an Enum defined in ``hyde.enhanced_prompts``.



Functions
---------

.. autoapisummary::

   hyde.enhanced_prompts.create_hyde_prompt
   hyde.enhanced_prompts.get_ensemble_prompt
   hyde.enhanced_prompts.get_generation_prompt
   hyde.enhanced_prompts.get_perspective_prompt
   hyde.enhanced_prompts.select_prompt_automatically

.. py:function:: create_hyde_prompt(config: HyDEPromptConfig, query: str) -> langchain_core.prompts.ChatPromptTemplate

   Create a HyDE prompt based on configuration.

   :param config: Prompt configuration
   :param query: User query

   :returns: Configured ChatPromptTemplate ready for use


   .. autolink-examples:: create_hyde_prompt
      :collapse:

.. py:function:: get_ensemble_prompt(num_documents: int = 3, target_length: int = 1000) -> langchain_core.prompts.ChatPromptTemplate

   Get an ensemble generation prompt for multiple documents.

   :param num_documents: Number of documents to generate
   :param target_length: Target character length per document

   :returns: Configured ChatPromptTemplate


   .. autolink-examples:: get_ensemble_prompt
      :collapse:

.. py:function:: get_generation_prompt(prompt_type: HyDEPromptType = HyDEPromptType.GENERAL, target_length: int = 1000) -> langchain_core.prompts.ChatPromptTemplate

   Get a generation prompt for the specified type and length.

   :param prompt_type: Type of prompt to use
   :param target_length: Target character length for generated document

   :returns: Configured ChatPromptTemplate


   .. autolink-examples:: get_generation_prompt
      :collapse:

.. py:function:: get_perspective_prompt(perspective: HyDEPerspective, target_length: int = 1000) -> langchain_core.prompts.ChatPromptTemplate

   Get a perspective-based generation prompt.

   :param perspective: Perspective to use for generation
   :param target_length: Target character length for generated document

   :returns: Configured ChatPromptTemplate


   .. autolink-examples:: get_perspective_prompt
      :collapse:

.. py:function:: select_prompt_automatically(query: str) -> HyDEPromptType

   Automatically select appropriate prompt type based on query analysis.

   :param query: User query to analyze

   :returns: Recommended prompt type


   .. autolink-examples:: select_prompt_automatically
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: hyde.enhanced_prompts
   :collapse:
   
.. autolink-skip:: next
