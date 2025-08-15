agents.planning.rewoo_tree_agent_v2
===================================

.. py:module:: agents.planning.rewoo_tree_agent_v2

.. autoapi-nested-parse::

   ReWOO Tree-based Planning Agent V2 - Using MultiAgent Pattern.

   This agent implements the ReWOO (Reasoning without Observation) methodology
   using proper agent composition without manual node creation. All nodes are
   created automatically by wrapping agents.

   Key improvements:
   - No manual node functions - everything is agents
   - Uses MultiAgent pattern for composition
   - Automatic parallelization through agent dependencies
   - Tool aliasing and forced tool choice
   - Structured output models with field validators
   - Recursive planning through agent composition

   Reference:
   - ReWOO: https://langchain-ai.github.io/langgraph/tutorials/rewoo/rewoo/#solver
   - LLM Compiler: https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/


   .. autolink-examples:: agents.planning.rewoo_tree_agent_v2
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.rewoo_tree_agent_v2.logger


Classes
-------

.. autoapisummary::

   agents.planning.rewoo_tree_agent_v2.ParallelReWOOAgent
   agents.planning.rewoo_tree_agent_v2.PlanTask
   agents.planning.rewoo_tree_agent_v2.ReWOOExecutorAgent
   agents.planning.rewoo_tree_agent_v2.ReWOOPlan
   agents.planning.rewoo_tree_agent_v2.ReWOOPlannerAgent
   agents.planning.rewoo_tree_agent_v2.ReWOOTreeAgent
   agents.planning.rewoo_tree_agent_v2.ReWOOTreeState
   agents.planning.rewoo_tree_agent_v2.TaskPriority
   agents.planning.rewoo_tree_agent_v2.TaskStatus
   agents.planning.rewoo_tree_agent_v2.TaskType
   agents.planning.rewoo_tree_agent_v2.ToolAlias


Functions
---------

.. autoapisummary::

   agents.planning.rewoo_tree_agent_v2.create_rewoo_agent_with_tools


Module Contents
---------------

.. py:class:: ParallelReWOOAgent(name: str = 'parallel_rewoo', max_parallelism: int = 8, **kwargs)

   Bases: :py:obj:`ReWOOTreeAgent`


   Enhanced ReWOO agent with advanced parallel execution capabilities.

   This version focuses on maximizing parallelization by:
   - Creating multiple executor instances dynamically
   - Using Send objects for true parallel execution
   - Optimizing task distribution
   - Real-time performance tracking


   .. autolink-examples:: ParallelReWOOAgent
      :collapse:

   .. py:method:: _configure_execution_flow()

      Configure for maximum parallelization.


      .. autolink-examples:: _configure_execution_flow
         :collapse:


   .. py:attribute:: performance_metrics


.. py:class:: PlanTask(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A task in the planning tree - simplified for agent-based execution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanTask
      :collapse:

   .. py:method:: validate_id(v: str) -> str
      :classmethod:


      Validate task ID format.


      .. autolink-examples:: validate_id
         :collapse:


   .. py:attribute:: agent_name
      :type:  str
      :value: None



   .. py:attribute:: dependencies
      :type:  list[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: result
      :type:  Any | None
      :value: None



   .. py:attribute:: status
      :type:  TaskStatus
      :value: None



   .. py:attribute:: task_type
      :type:  TaskType
      :value: None



   .. py:attribute:: tool_alias
      :type:  str | None
      :value: None



.. py:class:: ReWOOExecutorAgent(name: str = 'rewoo_executor', tools: list[langchain_core.tools.BaseTool] | None = None, tool_aliases: dict[str, ToolAlias] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Agent that executes individual tasks with tool support.


   .. autolink-examples:: ReWOOExecutorAgent
      :collapse:

   .. py:method:: execute_task(task: PlanTask, context: dict[str, Any] | None = None) -> Any

      Execute a single task.


      .. autolink-examples:: execute_task
         :collapse:


   .. py:attribute:: tool_aliases
      :type:  dict[str, ToolAlias]
      :value: None



.. py:class:: ReWOOPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete execution plan with tasks and dependencies.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOPlan
      :collapse:

   .. py:method:: _update_execution_levels() -> None

      Update execution levels based on dependencies.


      .. autolink-examples:: _update_execution_levels
         :collapse:


   .. py:method:: add_task(task: PlanTask) -> None

      Add a task to the plan.


      .. autolink-examples:: add_task
         :collapse:


   .. py:method:: get_ready_tasks(completed_tasks: set[str]) -> list[PlanTask]

      Get tasks that are ready for execution.


      .. autolink-examples:: get_ready_tasks
         :collapse:


   .. py:attribute:: execution_levels
      :type:  list[list[str]]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: problem_analysis
      :type:  str
      :value: None



   .. py:attribute:: required_tools
      :type:  list[str]
      :value: None



   .. py:attribute:: tasks
      :type:  list[PlanTask]
      :value: None



   .. py:attribute:: tool_aliases
      :type:  dict[str, ToolAlias]
      :value: None



.. py:class:: ReWOOPlannerAgent(name: str = 'rewoo_planner', available_tools: list[langchain_core.tools.BaseTool] | None = None, **kwargs)

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Specialized agent for creating ReWOO plans.


   .. autolink-examples:: ReWOOPlannerAgent
      :collapse:

   .. py:method:: _create_fallback_plan(problem: str) -> ReWOOPlan

      Create a simple fallback plan.


      .. autolink-examples:: _create_fallback_plan
         :collapse:


   .. py:method:: create_plan(problem: str, context: dict[str, Any] | None = None) -> ReWOOPlan

      Create a ReWOO plan for the given problem.


      .. autolink-examples:: create_plan
         :collapse:


   .. py:attribute:: available_tools
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



.. py:class:: ReWOOTreeAgent(name: str = 'rewoo_tree_agent', available_tools: list[langchain_core.tools.BaseTool] | None = None, tool_aliases: dict[str, ToolAlias] | None = None, max_planning_depth: int = 3, max_parallelism: int = 4, **kwargs)

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   ReWOO Tree Agent using proper MultiAgent composition.

   This agent creates and executes tree-based plans using multiple specialized agents:
   - Planner: Creates structured execution plans
   - Executor: Executes individual tasks with tools
   - Coordinator: Manages parallel execution
   - Validator: Validates results


   .. autolink-examples:: ReWOOTreeAgent
      :collapse:

   .. py:method:: _configure_execution_flow()

      Configure the execution flow with proper branching.


      .. autolink-examples:: _configure_execution_flow
         :collapse:


   .. py:method:: _format_result(raw_result: Any) -> dict[str, Any]

      Format the execution result.


      .. autolink-examples:: _format_result
         :collapse:


   .. py:method:: add_tool_alias(alias: str, actual_tool: str, force_choice: bool = True, **params)

      Add a tool alias for forced tool choice.


      .. autolink-examples:: add_tool_alias
         :collapse:


   .. py:method:: create_and_execute_plan(problem: str) -> dict[str, Any]
      :async:


      Create and execute a plan for the given problem.


      .. autolink-examples:: create_and_execute_plan
         :collapse:


   .. py:attribute:: available_tools
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



   .. py:attribute:: max_parallelism
      :type:  int
      :value: None



   .. py:attribute:: max_planning_depth
      :type:  int
      :value: None



   .. py:attribute:: tool_aliases
      :type:  dict[str, ToolAlias]
      :value: None



.. py:class:: ReWOOTreeState

   Bases: :py:obj:`haive.core.schema.prebuilt.multi_agent_state.MultiAgentState`


   State for ReWOO tree execution.


   .. autolink-examples:: ReWOOTreeState
      :collapse:

   .. py:attribute:: completed_tasks
      :type:  set[str]
      :value: None



   .. py:attribute:: current_plan
      :type:  ReWOOPlan | None
      :value: None



   .. py:attribute:: end_time
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: planning_depth
      :type:  int
      :value: None



   .. py:attribute:: start_time
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: task_results
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: tool_aliases
      :type:  dict[str, ToolAlias]
      :value: None



.. py:class:: TaskPriority

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Priority levels for tasks.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskPriority
      :collapse:

   .. py:attribute:: CRITICAL
      :value: 'critical'



   .. py:attribute:: HIGH
      :value: 'high'



   .. py:attribute:: LOW
      :value: 'low'



   .. py:attribute:: MEDIUM
      :value: 'medium'



.. py:class:: TaskStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status of tasks in the planning tree.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskStatus
      :collapse:

   .. py:attribute:: BLOCKED
      :value: 'blocked'



   .. py:attribute:: COMPLETED
      :value: 'completed'



   .. py:attribute:: FAILED
      :value: 'failed'



   .. py:attribute:: IN_PROGRESS
      :value: 'in_progress'



   .. py:attribute:: PENDING
      :value: 'pending'



.. py:class:: TaskType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of tasks in the planning tree.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskType
      :collapse:

   .. py:attribute:: ANALYSIS
      :value: 'analysis'



   .. py:attribute:: EXECUTION
      :value: 'execution'



   .. py:attribute:: PLANNING
      :value: 'planning'



   .. py:attribute:: RESEARCH
      :value: 'research'



   .. py:attribute:: SYNTHESIS
      :value: 'synthesis'



   .. py:attribute:: VALIDATION
      :value: 'validation'



.. py:class:: ToolAlias(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Tool alias configuration for forced tool choice.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ToolAlias
      :collapse:

   .. py:method:: validate_alias(v: str) -> str
      :classmethod:


      Validate alias format.


      .. autolink-examples:: validate_alias
         :collapse:


   .. py:attribute:: actual_tool
      :type:  str
      :value: None



   .. py:attribute:: alias
      :type:  str
      :value: None



   .. py:attribute:: force_choice
      :type:  bool
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: parameters
      :type:  dict[str, Any]
      :value: None



.. py:function:: create_rewoo_agent_with_tools(tools: list[langchain_core.tools.BaseTool], tool_aliases: dict[str, str] | None = None, max_parallelism: int = 4) -> ReWOOTreeAgent

   Factory function to create a ReWOO agent with tools.

   :param tools: List of tools available to the agent
   :param tool_aliases: Mapping of alias names to actual tool names
   :param max_parallelism: Maximum parallel executions

   :returns: Configured ReWOOTreeAgent


   .. autolink-examples:: create_rewoo_agent_with_tools
      :collapse:

.. py:data:: logger

