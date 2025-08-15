agents.planning.llm_compiler.models
===================================

.. py:module:: agents.planning.llm_compiler.models

.. autoapi-nested-parse::

   Models for the LLM Compiler agent.

   This module defines the pydantic models specific to the LLM Compiler agent,
   integrating with the base Step and Plan models from the plan_and_execute agent.


   .. autolink-examples:: agents.planning.llm_compiler.models
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler.models.CompilerPlan
   agents.planning.llm_compiler.models.CompilerStep
   agents.planning.llm_compiler.models.CompilerTask
   agents.planning.llm_compiler.models.FinalResponse
   agents.planning.llm_compiler.models.JoinerOutput
   agents.planning.llm_compiler.models.Replan
   agents.planning.llm_compiler.models.TaskDependency


Module Contents
---------------

.. py:class:: CompilerPlan

   Bases: :py:obj:`haive.agents.planning.plan_and_execute.models.Plan`


   Extends the base Plan model for the LLM Compiler agent.

   Handles DAG execution and dependency tracking.


   .. autolink-examples:: CompilerPlan
      :collapse:

   .. py:method:: add_compiler_step(step_id: int, description: str, tool_name: str, arguments: dict[str, Any], dependencies: list[int | TaskDependency] | None = None) -> CompilerStep

      Add a new compiler step to the plan.

      :param step_id: Unique ID for the step
      :param description: Description of the step
      :param tool_name: Name of the tool to execute
      :param arguments: Arguments for the tool
      :param dependencies: List of step IDs or TaskDependency objects

      :returns: The newly created step


      .. autolink-examples:: add_compiler_step
         :collapse:


   .. py:method:: get_executable_steps(results: dict[int, Any]) -> list[CompilerStep]

      Get steps that can be executed (all dependencies satisfied).

      :param results: Dictionary mapping step IDs to their results

      :returns: List of executable steps


      .. autolink-examples:: get_executable_steps
         :collapse:


   .. py:method:: get_join_step() -> CompilerStep | None

      Get the join step (final step) if present.


      .. autolink-examples:: get_join_step
         :collapse:


   .. py:method:: get_step_by_id(step_id: int) -> CompilerStep | None

      Find a step by its ID.


      .. autolink-examples:: get_step_by_id
         :collapse:


   .. py:attribute:: steps
      :type:  list[CompilerStep]
      :value: None



.. py:class:: CompilerStep

   Bases: :py:obj:`haive.agents.planning.plan_and_execute.models.Step`


   Extends the base Step model with LLM Compiler-specific fields.

   Each step contains a task to execute and tracks dependencies.


   .. autolink-examples:: CompilerStep
      :collapse:

   .. py:method:: can_execute(results: dict[int, Any]) -> bool

      Check if all dependencies are satisfied.

      :param results: Dictionary mapping step IDs to their results

      :returns: True if all dependencies are satisfied, False otherwise


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: execute(tool_map: dict[str, langchain_core.tools.BaseTool], results: dict[int, Any]) -> Any

      Execute this step's task with the given tools.

      :param tool_map: Dictionary mapping tool names to tool objects
      :param results: Dictionary mapping step IDs to their results

      :returns: Result of executing the task


      .. autolink-examples:: execute
         :collapse:


   .. py:property:: dependencies
      :type: list[int]


      Get IDs of steps this step depends on.

      .. autolink-examples:: dependencies
         :collapse:


   .. py:attribute:: task
      :type:  CompilerTask
      :value: None



.. py:class:: CompilerTask(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a task in the LLM Compiler framework's DAG.

   Tasks define what tools to run and their dependencies on other tasks.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CompilerTask
      :collapse:

   .. py:method:: resolve_arguments(results: dict[int, Any]) -> dict[str, Any]

      Resolve dependencies in arguments to actual values.

      :param results: Dictionary mapping step IDs to their results

      :returns: Dictionary with resolved argument values


      .. autolink-examples:: resolve_arguments
         :collapse:


   .. py:attribute:: arguments
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: dependencies
      :type:  list[TaskDependency]
      :value: None



   .. py:property:: is_join
      :type: bool


      Check if this is a join (final) task.

      .. autolink-examples:: is_join
         :collapse:


   .. py:attribute:: tool_name
      :type:  str
      :value: None



.. py:class:: FinalResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   The final response/answer to return to the user.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FinalResponse
      :collapse:

   .. py:attribute:: response
      :type:  str


.. py:class:: JoinerOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   The joiner's decision: either provide a final response or request replanning.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: JoinerOutput
      :collapse:

   .. py:attribute:: action
      :type:  FinalResponse | Replan
      :value: None



   .. py:attribute:: thought
      :type:  str
      :value: None



.. py:class:: Replan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Feedback for replanning when the current plan wasn't sufficient.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Replan
      :collapse:

   .. py:attribute:: feedback
      :type:  str
      :value: None



.. py:class:: TaskDependency(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a dependency reference to another task's output.

   This allows for tracking references between steps in the plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskDependency
      :collapse:

   .. py:method:: resolve(results: dict[int, Any]) -> Any

      Resolve the dependency to the actual value.


      .. autolink-examples:: resolve
         :collapse:


   .. py:attribute:: output_key
      :type:  str | None
      :value: None



   .. py:attribute:: step_id
      :type:  int
      :value: None



