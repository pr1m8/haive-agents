agents.planning.llm_compiler_v3.prompts
=======================================

.. py:module:: agents.planning.llm_compiler_v3.prompts

.. autoapi-nested-parse::

   Prompt templates for LLM Compiler V3 Agent.


   .. autolink-examples:: agents.planning.llm_compiler_v3.prompts
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.llm_compiler_v3.prompts.EXECUTION_SCENARIO_PROMPTS
   agents.planning.llm_compiler_v3.prompts.LLM_COMPILER_V3_PROMPTS


Functions
---------

.. autoapisummary::

   agents.planning.llm_compiler_v3.prompts.get_executor_prompt
   agents.planning.llm_compiler_v3.prompts.get_joiner_prompt
   agents.planning.llm_compiler_v3.prompts.get_planner_prompt
   agents.planning.llm_compiler_v3.prompts.get_task_fetcher_prompt


Module Contents
---------------

.. py:function:: get_executor_prompt(current_task: dict, tool_name: str, resolved_arguments: dict, available_tools: list) -> str

   Generate contextual executor prompt.


   .. autolink-examples:: get_executor_prompt
      :collapse:

.. py:function:: get_joiner_prompt(original_query: str, execution_results: list, successful_tasks: list, failed_tasks: list) -> str

   Generate contextual joiner prompt.


   .. autolink-examples:: get_joiner_prompt
      :collapse:

.. py:function:: get_planner_prompt(query: str, available_tools: list, scenario: str = 'default') -> str

   Generate contextual planner prompt based on scenario.


   .. autolink-examples:: get_planner_prompt
      :collapse:

.. py:function:: get_task_fetcher_prompt(completed_tasks: list, available_tasks: list, max_parallel: int, failed_tasks: list | None = None) -> str

   Generate contextual task fetcher prompt.


   .. autolink-examples:: get_task_fetcher_prompt
      :collapse:

.. py:data:: EXECUTION_SCENARIO_PROMPTS

.. py:data:: LLM_COMPILER_V3_PROMPTS

