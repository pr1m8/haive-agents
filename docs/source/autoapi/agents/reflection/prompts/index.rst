
:py:mod:`agents.reflection.prompts`
===================================

.. py:module:: agents.reflection.prompts

Prompts for reflection agents.


.. autolink-examples:: agents.reflection.prompts
   :collapse:


Functions
---------

.. autoapisummary::

   agents.reflection.prompts.create_expert_prompt
   agents.reflection.prompts.create_grading_prompt
   agents.reflection.prompts.create_improvement_prompt
   agents.reflection.prompts.create_reflection_prompt

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



.. rubric:: Related Links

.. autolink-examples:: agents.reflection.prompts
   :collapse:
   
.. autolink-skip:: next
