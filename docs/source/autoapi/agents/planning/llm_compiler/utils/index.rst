agents.planning.llm_compiler.utils
==================================

.. py:module:: agents.planning.llm_compiler.utils


Functions
---------

.. autoapisummary::

   agents.planning.llm_compiler.utils._execute_task
   agents.planning.llm_compiler.utils._get_observations
   agents.planning.llm_compiler.utils._resolve_arg
   agents.planning.llm_compiler.utils.schedule_pending_task
   agents.planning.llm_compiler.utils.schedule_pending_task
   agents.planning.llm_compiler.utils.schedule_task
   agents.planning.llm_compiler.utils.schedule_tasks


Module Contents
---------------

.. py:function:: _execute_task(task, observations, config)

.. py:function:: _get_observations(messages: list[langchain_core.messages.BaseMessage]) -> dict[int, Any]

.. py:function:: _resolve_arg(arg: str | Any, observations: dict[int, Any])

.. py:function:: schedule_pending_task(task: agents.planning.llm_compiler.models.Task, observations: dict[int, Any], retry_after: float = 0.2)

.. py:function:: schedule_pending_task(task: agents.planning.llm_compiler.models.Task, observations: dict[int, Any], retry_after: float = 0.2)

.. py:function:: schedule_task(task_inputs, config: dict[str, Any])

.. py:function:: schedule_tasks(scheduler_input: agents.planning.llm_compiler.models.SchedulerInput) -> list[langchain_core.messages.FunctionMessage]

   Group the tasks into a DAG schedule.


   .. autolink-examples:: schedule_tasks
      :collapse:

