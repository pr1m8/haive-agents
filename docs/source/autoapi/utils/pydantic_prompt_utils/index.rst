
:py:mod:`utils.pydantic_prompt_utils`
=====================================

.. py:module:: utils.pydantic_prompt_utils

Utilities for converting Pydantic models to prompt templates.

This module provides utilities to create prompt templates from Pydantic models,
supporting the structured output pattern where prompts focus on generation
and parsers handle the structured parsing separately.

Key features:
- Generate prompts that guide LLMs to create content parseable by Pydantic models
- Support for different prompt styles (descriptive, example-based, schema-based)
- Field-specific guidance and constraints
- Optional examples and formatting hints


.. autolink-examples:: utils.pydantic_prompt_utils
   :collapse:

Classes
-------

.. autoapisummary::

   utils.pydantic_prompt_utils.PromptStyle
   utils.pydantic_prompt_utils.PydanticPromptConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PromptStyle:

   .. graphviz::
      :align: center

      digraph inheritance_PromptStyle {
        node [shape=record];
        "PromptStyle" [label="PromptStyle"];
        "str" -> "PromptStyle";
        "enum.Enum" -> "PromptStyle";
      }

.. autoclass:: utils.pydantic_prompt_utils.PromptStyle
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PromptStyle** is an Enum defined in ``utils.pydantic_prompt_utils``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PydanticPromptConfig:

   .. graphviz::
      :align: center

      digraph inheritance_PydanticPromptConfig {
        node [shape=record];
        "PydanticPromptConfig" [label="PydanticPromptConfig"];
        "pydantic.BaseModel" -> "PydanticPromptConfig";
      }

.. autopydantic_model:: utils.pydantic_prompt_utils.PydanticPromptConfig
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



Functions
---------

.. autoapisummary::

   utils.pydantic_prompt_utils.analyze_pydantic_field
   utils.pydantic_prompt_utils.analyze_type_annotation
   utils.pydantic_prompt_utils.create_example_from_model
   utils.pydantic_prompt_utils.create_generation_and_parsing_prompts
   utils.pydantic_prompt_utils.create_parsing_prompt
   utils.pydantic_prompt_utils.create_pydantic_prompt
   utils.pydantic_prompt_utils.generate_field_description
   utils.pydantic_prompt_utils.quick_pydantic_prompt

.. py:function:: analyze_pydantic_field(field_info: Any, field_name: str) -> dict[str, Any]

   Analyze a Pydantic field to extract information for prompt generation.

   :param field_info: Pydantic FieldInfo object
   :param field_name: Name of the field

   :returns: Dictionary containing field analysis


   .. autolink-examples:: analyze_pydantic_field
      :collapse:

.. py:function:: analyze_type_annotation(annotation: type) -> dict[str, Any]

   Analyze a type annotation to extract useful information.

   :param annotation: Type annotation to analyze

   :returns: Dictionary containing type analysis


   .. autolink-examples:: analyze_type_annotation
      :collapse:

.. py:function:: create_example_from_model(model_class: type[pydantic.BaseModel]) -> str

   Create an example output from a Pydantic model.

   :param model_class: Pydantic model class

   :returns: Example string showing the expected format


   .. autolink-examples:: create_example_from_model
      :collapse:

.. py:function:: create_generation_and_parsing_prompts(model_class: type[pydantic.BaseModel], generation_instruction: str = 'Generate comprehensive content about the topic:', config: PydanticPromptConfig | None = None) -> tuple[langchain_core.prompts.ChatPromptTemplate, langchain_core.prompts.ChatPromptTemplate]

   Create both generation and parsing prompts for structured output pattern.

   This follows the best practice of separating content generation from
   structured parsing, allowing the LLM to focus on creating good content
   first, then extracting structure from that content.

   :param model_class: Pydantic model class
   :param generation_instruction: Instruction for content generation
   :param config: Configuration for prompt generation

   :returns: Tuple of (generation_prompt, parsing_prompt)


   .. autolink-examples:: create_generation_and_parsing_prompts
      :collapse:

.. py:function:: create_parsing_prompt(model_class: type[pydantic.BaseModel], content_field: str = 'content') -> langchain_core.prompts.ChatPromptTemplate

   Create a prompt for parsing content into a Pydantic model.

   This creates a separate parsing prompt that can be used after generation
   to extract structured information from unstructured content.

   :param model_class: Pydantic model class to parse into
   :param content_field: Name of the field containing the content to parse

   :returns: ChatPromptTemplate for parsing content


   .. autolink-examples:: create_parsing_prompt
      :collapse:

.. py:function:: create_pydantic_prompt(model_class: type[pydantic.BaseModel], config: PydanticPromptConfig, base_instruction: str = 'Generate content with the following structure:') -> langchain_core.prompts.ChatPromptTemplate

   Create a prompt template from a Pydantic model.

   :param model_class: Pydantic model class to create prompt for
   :param config: Configuration for prompt generation
   :param base_instruction: Base instruction for the prompt

   :returns: ChatPromptTemplate that guides LLM to generate parseable content


   .. autolink-examples:: create_pydantic_prompt
      :collapse:

.. py:function:: generate_field_description(field_analysis: dict[str, Any], style: PromptStyle) -> str

   Generate a description for a field based on analysis and style.

   :param field_analysis: Field analysis from analyze_pydantic_field
   :param style: Prompt style to use

   :returns: Description string for the field


   .. autolink-examples:: generate_field_description
      :collapse:

.. py:function:: quick_pydantic_prompt(model_class: type[pydantic.BaseModel], style: PromptStyle = PromptStyle.DESCRIPTIVE, use_json: bool = False) -> langchain_core.prompts.ChatPromptTemplate

   Quick way to create a basic prompt from a Pydantic model.

   :param model_class: Pydantic model class
   :param style: Prompt style to use
   :param use_json: Whether to request JSON format

   :returns: ChatPromptTemplate for the model


   .. autolink-examples:: quick_pydantic_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: utils.pydantic_prompt_utils
   :collapse:
   
.. autolink-skip:: next
