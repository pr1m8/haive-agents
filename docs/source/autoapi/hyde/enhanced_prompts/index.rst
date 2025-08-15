hyde.enhanced_prompts
=====================

.. py:module:: hyde.enhanced_prompts

.. autoapi-nested-parse::

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


Attributes
----------

.. autoapisummary::

   hyde.enhanced_prompts.HYDE_ANALYSIS_PROMPT
   hyde.enhanced_prompts.HYDE_ENSEMBLE_PROMPT
   hyde.enhanced_prompts.HYDE_EXTRACTION_PROMPT
   hyde.enhanced_prompts.HYDE_GENERATION_PROMPTS
   hyde.enhanced_prompts.HYDE_LENGTH_CONTROLLED_PROMPT
   hyde.enhanced_prompts.HYDE_PERSPECTIVE_PROMPT


Classes
-------

.. autoapisummary::

   hyde.enhanced_prompts.HyDEPerspective
   hyde.enhanced_prompts.HyDEPromptConfig
   hyde.enhanced_prompts.HyDEPromptType


Functions
---------

.. autoapisummary::

   hyde.enhanced_prompts.create_hyde_prompt
   hyde.enhanced_prompts.get_ensemble_prompt
   hyde.enhanced_prompts.get_generation_prompt
   hyde.enhanced_prompts.get_perspective_prompt
   hyde.enhanced_prompts.select_prompt_automatically


Module Contents
---------------

.. py:class:: HyDEPerspective

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Different perspectives for multi-angle document generation.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HyDEPerspective
      :collapse:

   .. py:attribute:: BEGINNER
      :value: 'beginner'



   .. py:attribute:: CRITIC
      :value: 'critic'



   .. py:attribute:: EXPERT
      :value: 'expert'



   .. py:attribute:: PRACTITIONER
      :value: 'practitioner'



   .. py:attribute:: RESEARCHER
      :value: 'researcher'



.. py:class:: HyDEPromptConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for HyDE prompt selection.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HyDEPromptConfig
      :collapse:

   .. py:attribute:: num_documents
      :type:  int
      :value: None



   .. py:attribute:: perspective
      :type:  HyDEPerspective | None
      :value: None



   .. py:attribute:: prompt_type
      :type:  HyDEPromptType
      :value: None



   .. py:attribute:: target_length
      :type:  int
      :value: None



   .. py:attribute:: use_ensemble
      :type:  bool
      :value: None



.. py:class:: HyDEPromptType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of HyDE prompts for different domains.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HyDEPromptType
      :collapse:

   .. py:attribute:: ACADEMIC
      :value: 'academic'



   .. py:attribute:: BUSINESS
      :value: 'business'



   .. py:attribute:: GENERAL
      :value: 'general'



   .. py:attribute:: NEWS
      :value: 'news'



   .. py:attribute:: REFERENCE
      :value: 'reference'



   .. py:attribute:: TECHNICAL
      :value: 'technical'



   .. py:attribute:: TUTORIAL
      :value: 'tutorial'



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

.. py:data:: HYDE_ANALYSIS_PROMPT

.. py:data:: HYDE_ENSEMBLE_PROMPT

.. py:data:: HYDE_EXTRACTION_PROMPT

.. py:data:: HYDE_GENERATION_PROMPTS
   :type:  dict[HyDEPromptType, langchain_core.prompts.ChatPromptTemplate]

.. py:data:: HYDE_LENGTH_CONTROLLED_PROMPT

.. py:data:: HYDE_PERSPECTIVE_PROMPT

