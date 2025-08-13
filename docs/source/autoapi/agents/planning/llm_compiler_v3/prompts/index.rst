
:py:mod:`agents.planning.llm_compiler_v3.prompts`
=================================================

.. py:module:: agents.planning.llm_compiler_v3.prompts

Prompt templates for LLM Compiler V3 Agent.


.. autolink-examples:: agents.planning.llm_compiler_v3.prompts
   :collapse:


Functions
---------

.. autoapisummary::

   agents.planning.llm_compiler_v3.prompts.get_executor_prompt
   agents.planning.llm_compiler_v3.prompts.get_joiner_prompt
   agents.planning.llm_compiler_v3.prompts.get_planner_prompt
   agents.planning.llm_compiler_v3.prompts.get_task_fetcher_prompt

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



.. rubric:: Related Links

.. autolink-examples:: agents.planning.llm_compiler_v3.prompts
   :collapse:
   
.. autolink-skip:: next
