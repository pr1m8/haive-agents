agents.planning.llm_compiler_v3.state
=====================================

.. py:module:: agents.planning.llm_compiler_v3.state

.. autoapi-nested-parse::

   State schema for LLM Compiler V3 Agent.


   .. autolink-examples:: agents.planning.llm_compiler_v3.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema


Module Contents
---------------

.. py:class:: LLMCompilerStateSchema

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State schema for LLM Compiler V3 Agent using Enhanced MultiAgent V3.


   .. autolink-examples:: LLMCompilerStateSchema
      :collapse:

   .. py:method:: add_execution_result(result: haive.agents.planning.llm_compiler_v3.models.ParallelExecutionResult) -> None

      Add a task execution result to state.


      .. autolink-examples:: add_execution_result
         :collapse:


   .. py:method:: can_execute_more_tasks() -> bool

      Check if more tasks can be executed in parallel.


      .. autolink-examples:: can_execute_more_tasks
         :collapse:


   .. py:method:: get_execution_summary() -> dict[str, Any]

      Get comprehensive execution summary.


      .. autolink-examples:: get_execution_summary
         :collapse:


   .. py:method:: get_failed_results() -> list[haive.agents.planning.llm_compiler_v3.models.ParallelExecutionResult]

      Get all failed execution results.


      .. autolink-examples:: get_failed_results
         :collapse:


   .. py:method:: get_next_executable_tasks(count: int | None = None) -> list[haive.agents.planning.llm_compiler_v3.models.CompilerTask]

      Get the next tasks to execute, respecting parallel limits.


      .. autolink-examples:: get_next_executable_tasks
         :collapse:


   .. py:method:: get_successful_results() -> list[haive.agents.planning.llm_compiler_v3.models.ParallelExecutionResult]

      Get all successful execution results.


      .. autolink-examples:: get_successful_results
         :collapse:


   .. py:method:: is_execution_complete() -> bool

      Check if all tasks in the plan have been executed or failed.


      .. autolink-examples:: is_execution_complete
         :collapse:


   .. py:method:: mark_task_executing(task_id: str) -> None

      Mark a task as currently executing.


      .. autolink-examples:: mark_task_executing
         :collapse:


   .. py:method:: resolve_task_arguments(task: haive.agents.planning.llm_compiler_v3.models.CompilerTask) -> dict[str, Any]

      Resolve task arguments by substituting dependency references.


      .. autolink-examples:: resolve_task_arguments
         :collapse:


   .. py:method:: should_replan() -> bool

      Determine if replanning is needed based on execution state.


      .. autolink-examples:: should_replan
         :collapse:


   .. py:method:: update_ready_tasks() -> None

      Update lists of ready and blocked tasks based on current state.


      .. autolink-examples:: update_ready_tasks
         :collapse:


   .. py:attribute:: blocked_tasks
      :type:  list[haive.agents.planning.llm_compiler_v3.models.CompilerTask]
      :value: None



   .. py:attribute:: compiler_context
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: completed_task_ids
      :type:  list[str]
      :value: None



   .. py:attribute:: current_agent
      :type:  str
      :value: None



   .. py:attribute:: current_plan
      :type:  haive.agents.planning.llm_compiler_v3.models.CompilerPlan | None
      :value: None



   .. py:attribute:: currently_executing
      :type:  list[str]
      :value: None



   .. py:attribute:: execution_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: execution_results
      :type:  list[haive.agents.planning.llm_compiler_v3.models.ParallelExecutionResult]
      :value: None



   .. py:attribute:: execution_start_time
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: failed_task_ids
      :type:  list[str]
      :value: None



   .. py:attribute:: max_parallel_tasks
      :type:  int
      :value: None



   .. py:attribute:: next_agent
      :type:  str | None
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: parallel_efficiency_score
      :type:  float | None
      :value: None



   .. py:attribute:: ready_tasks
      :type:  list[haive.agents.planning.llm_compiler_v3.models.CompilerTask]
      :value: None



   .. py:attribute:: replan_count
      :type:  int
      :value: None



   .. py:attribute:: replan_requests
      :type:  list[haive.agents.planning.llm_compiler_v3.models.ReplanRequest]
      :value: None



   .. py:attribute:: task_results
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: total_execution_time
      :type:  float
      :value: None



