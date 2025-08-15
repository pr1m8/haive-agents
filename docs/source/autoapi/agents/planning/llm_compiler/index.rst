agents.planning.llm_compiler
============================

.. py:module:: agents.planning.llm_compiler

.. autoapi-nested-parse::

   Module exports.


   .. autolink-examples:: agents.planning.llm_compiler
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/planning/llm_compiler/agent/index
   /autoapi/agents/planning/llm_compiler/aug_llms/index
   /autoapi/agents/planning/llm_compiler/config/index
   /autoapi/agents/planning/llm_compiler/models/index
   /autoapi/agents/planning/llm_compiler/output_parser/index
   /autoapi/agents/planning/llm_compiler/state/index
   /autoapi/agents/planning/llm_compiler/tools/index
   /autoapi/agents/planning/llm_compiler/utils/index


Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler.CompilerPlan
   agents.planning.llm_compiler.CompilerState
   agents.planning.llm_compiler.CompilerStep
   agents.planning.llm_compiler.CompilerTask
   agents.planning.llm_compiler.FinalResponse
   agents.planning.llm_compiler.JoinerOutput
   agents.planning.llm_compiler.LLMCompilerAgent
   agents.planning.llm_compiler.LLMCompilerAgentConfig
   agents.planning.llm_compiler.Replan
   agents.planning.llm_compiler.TaskDependency


Functions
---------

.. autoapisummary::

   agents.planning.llm_compiler.main
   agents.planning.llm_compiler.schedule_pending_task
   agents.planning.llm_compiler.schedule_task
   agents.planning.llm_compiler.schedule_tasks


Package Contents
----------------

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



.. py:class:: CompilerState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State model for the LLM Compiler agent.

   Tracks:
   - The user's query
   - The current plan
   - Results from executed steps
   - Conversation history

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CompilerState
      :collapse:

   .. py:method:: all_steps_complete() -> bool

      Check if all steps in the plan are complete.


      .. autolink-examples:: all_steps_complete
         :collapse:


   .. py:method:: get_executable_steps() -> list[agents.planning.llm_compiler.models.CompilerStep]

      Get steps that can be executed right now.


      .. autolink-examples:: get_executable_steps
         :collapse:


   .. py:method:: get_highest_step_id() -> int

      Get the highest step ID in the current plan.


      .. autolink-examples:: get_highest_step_id
         :collapse:


   .. py:method:: has_join_result() -> bool

      Check if the join step has been executed.


      .. autolink-examples:: has_join_result
         :collapse:


   .. py:attribute:: messages
      :type:  list[langchain_core.messages.BaseMessage]
      :value: None



   .. py:attribute:: plan
      :type:  agents.planning.llm_compiler.models.CompilerPlan | None
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: replan_count
      :type:  int
      :value: None



   .. py:attribute:: results
      :type:  dict[int, Any]
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



.. py:class:: LLMCompilerAgent(config: agents.planning.llm_compiler.config.LLMCompilerAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentArchitecture`


   LLM Compiler Agent implementation.

   This agent architecture has three main components:
   1. Planner: Creates a task DAG
   2. Task Executor: Executes tasks as their dependencies are satisfied
   3. Joiner: Processes results and decides whether to output an answer or replan

   Initialize the LLM Compiler agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LLMCompilerAgent
      :collapse:

   .. py:method:: _create_fallback_plan(query: str) -> agents.planning.llm_compiler.models.CompilerPlan

      Create a fallback plan when planning fails.

      :param query: The user's query

      :returns: A simple fallback plan


      .. autolink-examples:: _create_fallback_plan
         :collapse:


   .. py:method:: _execute_step(step: agents.planning.llm_compiler.models.CompilerStep, results: dict[int, Any], tool_map: dict[str, langchain_core.tools.BaseTool]) -> Any
      :staticmethod:


      Execute a single step.

      :param step: The step to execute
      :param results: Results from previous steps
      :param tool_map: Dictionary mapping tool names to tools

      :returns: Result of the step execution


      .. autolink-examples:: _execute_step
         :collapse:


   .. py:method:: _format_results_for_replanning(state: agents.planning.llm_compiler.state.CompilerState) -> str

      Format previous results for replanning.

      :param state: Current agent state

      :returns: Formatted results as a string


      .. autolink-examples:: _format_results_for_replanning
         :collapse:


   .. py:method:: _format_tool_descriptions() -> str

      Format tool descriptions for the planner prompt.

      :returns: Formatted tool descriptions


      .. autolink-examples:: _format_tool_descriptions
         :collapse:


   .. py:method:: _generate_fallback_response(state)

      Generates a fallback response when execution fails.

      :param state: The final state after execution.
      :type state: CompilerState | Dict

      :returns: The fallback response.
      :rtype: str


      .. autolink-examples:: _generate_fallback_response
         :collapse:


   .. py:method:: arun(query: str)
      :async:


      Run the agent asynchronously.

      :param query: The user's query

      :returns: Response from the agent


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: execute_tasks(state: agents.planning.llm_compiler.state.CompilerState) -> dict[str, Any]

      Execute tasks in parallel as their dependencies are satisfied.

      :param state: Current agent state

      :returns: Updated state with executed task results


      .. autolink-examples:: execute_tasks
         :collapse:


   .. py:method:: join(state: agents.planning.llm_compiler.state.CompilerState) -> dict[str, Any]

      Process the results and decide whether to provide a final answer or replan.

      :param state: Current agent state

      :returns: Decision to end or replan


      .. autolink-examples:: join
         :collapse:


   .. py:method:: plan(state: agents.planning.llm_compiler.state.CompilerState) -> dict[str, Any]

      Generate a plan based on the user's query.

      :param state: Current agent state

      :returns: Updated state with a new plan


      .. autolink-examples:: plan
         :collapse:


   .. py:method:: run(query: str)

      Run the agent on a query.

      :param query: The user's query

      :returns: Response from the agent


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> Any

      Set up the agent workflow as a state graph.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: should_execute_more(state: agents.planning.llm_compiler.state.CompilerState, config: dict[str, Any] | None = None) -> str

      Determine the next execution step.

      :param state: The current agent state.
      :type state: CompilerState
      :param config: Execution configuration (not used but required).
      :type config: Optional[Any]

      :returns: The next node to execute in the state graph.
      :rtype: str


      .. autolink-examples:: should_execute_more
         :collapse:


   .. py:method:: stream(query: str)

      Stream the agent's execution.

      :param query: The user's query

      :Yields: Execution steps


      .. autolink-examples:: stream
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: graph
      :value: None



   .. py:attribute:: joiner_llm


   .. py:attribute:: parser


   .. py:attribute:: planner_llm


   .. py:attribute:: replanner_llm


   .. py:attribute:: tool_map


   .. py:attribute:: tools


.. py:class:: LLMCompilerAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


   Configuration for the LLM Compiler Agent using AugLLMConfig system.

   The LLM Compiler agent creates a directed acyclic graph (DAG) of tasks
   and executes them in parallel when dependencies are satisfied.


   .. autolink-examples:: LLMCompilerAgentConfig
      :collapse:

   .. py:method:: validate_configs(values) -> Any

      Ensure that the configurations are valid.


      .. autolink-examples:: validate_configs
         :collapse:


   .. py:attribute:: joiner_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: max_execution_time
      :type:  float
      :value: None



   .. py:attribute:: max_replanning_attempts
      :type:  int
      :value: None



   .. py:attribute:: planner_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: replanner_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: runnable_config
      :type:  langchain_core.runnables.RunnableConfig
      :value: None



   .. py:attribute:: should_visualize_graph
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: tool_configs
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: tool_instances
      :type:  list[langchain_core.tools.BaseTool | langchain_core.tools.StructuredTool]
      :value: None



   .. py:attribute:: visualize_graph_output_name
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



.. py:function:: main() -> None

.. py:function:: schedule_pending_task(task: agents.planning.llm_compiler.models.Task, observations: dict[int, Any], retry_after: float = 0.2)

.. py:function:: schedule_task(task_inputs, config: dict[str, Any])

.. py:function:: schedule_tasks(scheduler_input: agents.planning.llm_compiler.models.SchedulerInput) -> list[langchain_core.messages.FunctionMessage]

   Group the tasks into a DAG schedule.


   .. autolink-examples:: schedule_tasks
      :collapse:

