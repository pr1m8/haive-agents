agents.reflection.prompts
=========================

.. py:module:: agents.reflection.prompts

.. autoapi-nested-parse::

   Prompts for reflection agents.


   .. autolink-examples:: agents.reflection.prompts
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reflection.prompts.EXPERT_SYSTEM_TEMPLATE
   agents.reflection.prompts.GRADING_SYSTEM_PROMPT
   agents.reflection.prompts.IMPROVEMENT_PROMPT_TEMPLATE
   agents.reflection.prompts.REFLECTION_SYSTEM_PROMPT


Functions
---------

.. autoapisummary::

   agents.reflection.prompts.create_expert_prompt
   agents.reflection.prompts.create_grading_prompt
   agents.reflection.prompts.create_improvement_prompt
   agents.reflection.prompts.create_reflection_prompt


Module Contents
---------------

.. py:function:: create_expert_prompt(expertise_config: dict) -> langchain_core.prompts.ChatPromptTemplate

   Create an expert prompt template.


   .. autolink-examples:: create_expert_prompt
      :collapse:

.. py:function:: create_grading_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Create a grading prompt template.


   .. autolink-examples:: create_grading_prompt
      :collapse:

.. py:function:: create_improvement_prompt(include_grading: bool = True, improvement_focus: str = 'all identified areas') -> langchain_core.prompts.ChatPromptTemplate

   Create an improvement prompt template.


   .. autolink-examples:: create_improvement_prompt
      :collapse:

.. py:function:: create_reflection_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Create a reflection prompt template.


   .. autolink-examples:: create_reflection_prompt
      :collapse:

.. py:data:: EXPERT_SYSTEM_TEMPLATE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a {expertise_level} expert in {domain}.
      
      {additional_context}
      
      Your role is to provide expert-level insights and analysis in your domain.
      Leverage your deep knowledge to:
      - Provide accurate, nuanced information
      - Identify subtleties others might miss
      - Offer expert perspectives and recommendations
      - Explain complex concepts clearly
      
      {style_instruction}"""

   .. raw:: html

      </details>



.. py:data:: GRADING_SYSTEM_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert evaluator that grades responses based on quality criteria.
      
      Evaluate responses on these dimensions:
      - Accuracy (0-100): Is the information correct and reliable?
      - Completeness (0-100): Does it fully address the question?
      - Clarity (0-100): Is it well-organized and easy to understand?
      - Relevance (0-100): Does it stay on topic and address what was asked?
      
      Provide:
      1. Numerical scores for each dimension
      2. An overall score and letter grade
      3. Specific strengths and weaknesses
      4. Actionable improvement suggestions
      5. Optionally, an improved version of the response
      
      Be fair but thorough in your evaluation."""

   .. raw:: html

      </details>



.. py:data:: IMPROVEMENT_PROMPT_TEMPLATE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Given this response to improve:
      
      {original_response}
      
      {grading_context}
      
      Please provide an improved version that addresses the identified weaknesses while maintaining the strengths.
      
      Focus on:
      {improvement_focus}
      
      Improved response:"""

   .. raw:: html

      </details>



.. py:data:: REFLECTION_SYSTEM_PROMPT
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a helpful assistant that reflects on responses to improve them.
      
      When given a response, you should:
      1. Consider what works well
      2. Identify areas for improvement
      3. Provide an enhanced version that addresses those improvements
      
      Focus on:
      - Accuracy and correctness
      - Completeness of the answer
      - Clarity and organization
      - Helpfulness to the user
      
      Maintain the core message while improving the delivery."""

   .. raw:: html

      </details>



