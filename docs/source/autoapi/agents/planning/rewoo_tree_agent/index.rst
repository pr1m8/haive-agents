agents.planning.rewoo_tree_agent
================================

.. py:module:: agents.planning.rewoo_tree_agent

.. autoapi-nested-parse::

   ReWOO Tree-based Planning Agent with Parallelizable Execution.

   This agent implements the ReWOO (Reasoning without Observation) methodology
   with tree-based planning for parallelizable execution. It features:

   - Hierarchical tree planning with recursive decomposition
   - Parallelizable node execution with proper dependencies
   - Tool aliasing and forced tool choice
   - Structured output models with field validators
   - Plan-and-execute pattern with dynamic recompilation
   - LLM Compiler inspired parallelization

   Reference:
   - ReWOO: https://langchain-ai.github.io/langgraph/tutorials/rewoo/rewoo/#solver
   - LLM Compiler: https://langchain-ai.github.io/langgraph/tutorials/llm-compiler/LLMCompiler/


   .. autolink-examples:: agents.planning.rewoo_tree_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.rewoo_tree_agent.logger


Classes
-------

.. autoapisummary::

   agents.planning.rewoo_tree_agent.PlanNode
   agents.planning.rewoo_tree_agent.PlanTree
   agents.planning.rewoo_tree_agent.ReWOOTreeAgent
   agents.planning.rewoo_tree_agent.ReWOOTreeAgentState
   agents.planning.rewoo_tree_agent.ReWOOTreeExecutorOutput
   agents.planning.rewoo_tree_agent.ReWOOTreePlannerOutput
   agents.planning.rewoo_tree_agent.TaskPriority
   agents.planning.rewoo_tree_agent.TaskStatus
   agents.planning.rewoo_tree_agent.TaskType
   agents.planning.rewoo_tree_agent.ToolAlias


Module Contents
---------------

.. py:class:: PlanNode(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A node in the planning tree representing a task.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanNode
      :collapse:

   .. py:method:: add_child(child_id: str) -> None

      Add a child node.


      .. autolink-examples:: add_child
         :collapse:


   .. py:method:: add_dependency(dependency_id: str) -> None

      Add a dependency.


      .. autolink-examples:: add_dependency
         :collapse:


   .. py:method:: can_execute(completed_nodes: set[str]) -> bool

      Check if this node can be executed given completed nodes.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: mark_completed(result: Any = None) -> None

      Mark the task as completed.


      .. autolink-examples:: mark_completed
         :collapse:


   .. py:method:: mark_failed(error: str) -> None

      Mark the task as failed.


      .. autolink-examples:: mark_failed
         :collapse:


   .. py:method:: mark_started() -> None

      Mark the task as started.


      .. autolink-examples:: mark_started
         :collapse:


   .. py:method:: validate_dependencies() -> PlanNode

      Validate dependency relationships.


      .. autolink-examples:: validate_dependencies
         :collapse:


   .. py:method:: validate_id(v: str) -> str
      :classmethod:


      Validate node ID format.


      .. autolink-examples:: validate_id
         :collapse:


   .. py:attribute:: agent_name
      :type:  str | None
      :value: None



   .. py:attribute:: children_ids
      :type:  list[str]
      :value: None



   .. py:attribute:: completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: dependencies
      :type:  list[str]
      :value: None



   .. py:attribute:: dependent_nodes
      :type:  list[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: estimated_duration
      :type:  float | None
      :value: None



   .. py:attribute:: expected_output
      :type:  str | None
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



   .. py:attribute:: parallelizable
      :type:  bool
      :value: None



   .. py:attribute:: parent_id
      :type:  str | None
      :value: None



   .. py:attribute:: priority
      :type:  TaskPriority
      :value: None



   .. py:attribute:: result
      :type:  Any | None
      :value: None



   .. py:attribute:: started_at
      :type:  datetime.datetime | None
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



.. py:class:: PlanTree(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A tree structure representing the complete execution plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanTree
      :collapse:

   .. py:method:: add_node(node: PlanNode) -> None

      Add a node to the tree.


      .. autolink-examples:: add_node
         :collapse:


   .. py:method:: get_completion_percentage() -> float

      Get the completion percentage of the plan.


      .. autolink-examples:: get_completion_percentage
         :collapse:


   .. py:method:: get_node(node_id: str) -> PlanNode | None

      Get a node by ID.


      .. autolink-examples:: get_node
         :collapse:


   .. py:method:: get_parallelizable_nodes() -> list[list[PlanNode]]

      Get nodes organized by parallelizable execution levels.


      .. autolink-examples:: get_parallelizable_nodes
         :collapse:


   .. py:method:: get_ready_nodes() -> list[PlanNode]

      Get nodes that are ready for execution.


      .. autolink-examples:: get_ready_nodes
         :collapse:


   .. py:method:: has_failures() -> bool

      Check if there are any failed nodes.


      .. autolink-examples:: has_failures
         :collapse:


   .. py:method:: is_complete() -> bool

      Check if the entire plan is complete.


      .. autolink-examples:: is_complete
         :collapse:


   .. py:method:: mark_node_completed(node_id: str, result: Any = None) -> None

      Mark a node as completed.


      .. autolink-examples:: mark_node_completed
         :collapse:


   .. py:method:: mark_node_failed(node_id: str, error: str) -> None

      Mark a node as failed.


      .. autolink-examples:: mark_node_failed
         :collapse:


   .. py:method:: validate_id(v: str) -> str
      :classmethod:


      Validate plan tree ID format.


      .. autolink-examples:: validate_id
         :collapse:


   .. py:attribute:: completed_nodes
      :type:  int
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: execution_levels
      :type:  list[list[str]]
      :value: None



   .. py:attribute:: failed_nodes
      :type:  int
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: max_parallelism
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: nodes
      :type:  dict[str, PlanNode]
      :value: None



   .. py:attribute:: root_id
      :type:  str | None
      :value: None



   .. py:attribute:: total_nodes
      :type:  int
      :value: None



.. py:class:: ReWOOTreeAgent(**kwargs)

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   ReWOO Tree-based Planning Agent with Parallelizable Execution.

   This agent implements the ReWOO methodology with enhancements:
   - Hierarchical tree planning with recursive decomposition
   - Parallelizable execution with dependency management
   - Tool aliasing for forced tool choice
   - Structured output models with validation
   - LLM Compiler inspired optimizations

   Initialize ReWOO Tree Agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOTreeAgent
      :collapse:

   .. py:method:: _create_executor_agent() -> haive.agents.base.agent.Agent

      Create specialized execution agent.


      .. autolink-examples:: _create_executor_agent
         :collapse:


   .. py:method:: _create_fallback_plan(error_or_result: str, user_input: str) -> ReWOOTreePlannerOutput

      Create a fallback plan when planning fails.


      .. autolink-examples:: _create_fallback_plan
         :collapse:


   .. py:method:: _create_planner_agent() -> haive.agents.base.agent.Agent

      Create specialized planning agent.


      .. autolink-examples:: _create_planner_agent
         :collapse:


   .. py:method:: _execute_nodes_sync(nodes: list[PlanNode], state: ReWOOTreeAgentState) -> dict[str, Any]

      Execute nodes synchronously (simplified version).


      .. autolink-examples:: _execute_nodes_sync
         :collapse:


   .. py:method:: _execute_parallel_nodes(nodes: list[PlanNode], state: ReWOOTreeAgentState) -> dict[str, Any]
      :async:


      Execute nodes in parallel with proper coordination.


      .. autolink-examples:: _execute_parallel_nodes
         :collapse:


   .. py:method:: _execute_single_node(node: PlanNode, state: ReWOOTreeAgentState) -> Any
      :async:


      Execute a single node with proper tool aliasing.


      .. autolink-examples:: _execute_single_node
         :collapse:


   .. py:method:: _execute_with_tool_alias(alias_config: ToolAlias, context: dict[str, Any]) -> Any
      :async:


      Execute a task using a specific tool alias.


      .. autolink-examples:: _execute_with_tool_alias
         :collapse:


   .. py:method:: _execute_with_tool_alias_sync(alias_config: ToolAlias, description: str) -> str

      Execute a task using a specific tool alias (sync version).


      .. autolink-examples:: _execute_with_tool_alias_sync
         :collapse:


   .. py:method:: _execution_coordinator_node(state: ReWOOTreeAgentState) -> langgraph.types.Command

      Coordinate the execution of the plan tree.


      .. autolink-examples:: _execution_coordinator_node
         :collapse:


   .. py:method:: _format_final_response(result: dict[str, Any], state: ReWOOTreeAgentState) -> str

      Format the final response for the user.


      .. autolink-examples:: _format_final_response
         :collapse:


   .. py:method:: _format_node_results(node_results: dict[str, Any]) -> str

      Format node results for display.


      .. autolink-examples:: _format_node_results
         :collapse:


   .. py:method:: _planning_node(state: ReWOOTreeAgentState) -> langgraph.types.Command

      Execute the planning phase.


      .. autolink-examples:: _planning_node
         :collapse:


   .. py:method:: _recursive_planning_check_node(state: ReWOOTreeAgentState) -> langgraph.types.Command

      Check if recursive planning is needed.


      .. autolink-examples:: _recursive_planning_check_node
         :collapse:


   .. py:method:: _result_aggregator_node(state: ReWOOTreeAgentState) -> langgraph.types.Command

      Aggregate results from all executions.


      .. autolink-examples:: _result_aggregator_node
         :collapse:


   .. py:method:: add_tool_alias(alias: str, actual_tool: str, force_choice: bool = True, **params) -> None

      Add a tool alias for forced tool choice.


      .. autolink-examples:: add_tool_alias
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the execution graph for ReWOO tree agent.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:attribute:: available_tools
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



   .. py:attribute:: executor_agent
      :type:  haive.agents.base.agent.Agent | None
      :value: None



   .. py:attribute:: max_parallelism
      :type:  int
      :value: None



   .. py:attribute:: max_planning_depth
      :type:  int
      :value: None



   .. py:attribute:: planner_agent
      :type:  haive.agents.base.agent.Agent | None
      :value: None



   .. py:attribute:: tool_aliases
      :type:  dict[str, ToolAlias]
      :value: None



.. py:class:: ReWOOTreeAgentState

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   Enhanced state for ReWOO tree agent.


   .. autolink-examples:: ReWOOTreeAgentState
      :collapse:

   .. py:attribute:: active_executions
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: available_tools
      :type:  list[str]
      :value: None



   .. py:attribute:: current_execution
      :type:  ReWOOTreeExecutorOutput | None
      :value: None



   .. py:attribute:: current_plan
      :type:  ReWOOTreePlannerOutput | None
      :value: None



   .. py:attribute:: execution_queue
      :type:  list[str]
      :value: None



   .. py:attribute:: final_output
      :type:  Any | None
      :value: None



   .. py:attribute:: node_results
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: planning_depth
      :type:  int
      :value: None



   .. py:attribute:: subplan_stack
      :type:  list[str]
      :value: None



   .. py:attribute:: tool_aliases
      :type:  dict[str, ToolAlias]
      :value: None



.. py:class:: ReWOOTreeExecutorOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for the ReWOO tree executor.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOTreeExecutorOutput
      :collapse:

   .. py:attribute:: completed_nodes
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: completion_percentage
      :type:  float
      :value: None



   .. py:attribute:: execution_id
      :type:  str
      :value: None



   .. py:attribute:: failed_nodes
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: final_result
      :type:  Any | None
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: nodes_executed
      :type:  int
      :value: None



   .. py:attribute:: nodes_failed
      :type:  int
      :value: None



   .. py:attribute:: parallel_efficiency
      :type:  float
      :value: None



   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: success
      :type:  bool
      :value: None



   .. py:attribute:: total_execution_time
      :type:  float
      :value: None



.. py:class:: ReWOOTreePlannerOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured output for the ReWOO tree planner.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOTreePlannerOutput
      :collapse:

   .. py:method:: validate_consistency() -> ReWOOTreePlannerOutput

      Validate consistency between plan components.


      .. autolink-examples:: validate_consistency
         :collapse:


   .. py:method:: validate_plan_id(v: str) -> str
      :classmethod:


      Validate plan ID format.


      .. autolink-examples:: validate_plan_id
         :collapse:


   .. py:attribute:: approach_strategy
      :type:  str
      :value: None



   .. py:attribute:: estimated_duration
      :type:  float
      :value: None



   .. py:attribute:: fallback_strategies
      :type:  list[str]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: parallelization_factor
      :type:  float
      :value: None



   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: plan_name
      :type:  str
      :value: None



   .. py:attribute:: plan_tree
      :type:  PlanTree
      :value: None



   .. py:attribute:: problem_analysis
      :type:  str
      :value: None



   .. py:attribute:: required_tools
      :type:  list[str]
      :value: None



   .. py:attribute:: risk_factors
      :type:  list[str]
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



.. py:data:: logger

