agents.planning.rewoo_tree_agent_v3
===================================

.. py:module:: agents.planning.rewoo_tree_agent_v3

.. autoapi-nested-parse::

   ReWOO Tree Agent V3 - Pure Agent Composition for Evidence-Based Planning.

   This module provides the **recommended** implementation for research and evidence-based
   planning tasks. It represents the latest and most elegant approach to the ReWOO
   (Reasoning WithOut Observation) pattern using pure agent composition.

   ## Key Features

   - **Pure Agent Composition**: No manual nodes - agents are automatically wrapped
   - **Evidence-Based Planning**: Gather evidence before reasoning for better decisions
   - **Parallel Execution**: Evidence collection can happen in parallel
   - **Tool Aliasing**: Map abstract tool names to actual implementations
   - **Type Safety**: Full Pydantic validation and type checking
   - **Clean Architecture**: Leverages MultiAgent patterns for orchestration

   ## ReWOO Pattern

   ```
   Problem Analysis
       ↓
   Evidence Planning (what info needed?)
       ↓
   Parallel Evidence Collection
       ↓
   Reasoning with Evidence
       ↓
   Final Answer
   ```

   ## Usage

   ### Basic Research Task
   ```python
   from haive.agents.planning import create_rewoo_agent_with_tools_v3
   from haive.tools import web_search_tool, calculator_tool

   agent = create_rewoo_agent_with_tools_v3(
       name="researcher",
       tools=[web_search_tool, calculator_tool],
       model="gpt-4"
   )

   result = agent.run("What is the economic impact of renewable energy?")
   ```

   ### Advanced with Tool Aliases
   ```python
   agent = ReWOOTreeAgent(
       name="advanced_researcher",
       available_tools=[web_search, db_query, api_call],
       tool_aliases={
           "research": ToolAlias(
               alias="research",
               actual_tool="web_search",
               force_choice=True
           ),
           "data": ToolAlias(
               alias="data",
               actual_tool="db_query",
               parameters={"limit": 100}
           )
       },
       max_parallelism=4
   )
   ```

   ## When to Use

   ✅ **Use ReWOO V3 when**:
   - You need evidence-based decision making
   - Research tasks with multiple information sources
   - Tasks benefit from parallel evidence gathering
   - You want clean, maintainable code

   ❌ **Consider alternatives when**:
   - Simple sequential tasks (use clean_plan_execute)
   - No evidence gathering needed (use simple planning)
   - Very simple single-step tasks (use ReactAgent directly)

   ## Advantages over V2

   1. **Cleaner Code**: Pure agent composition, no manual node management
   2. **Better Type Safety**: Proper Pydantic field initialization
   3. **More Maintainable**: Follows framework patterns consistently
   4. **Easier Testing**: Standard agent testing patterns apply

   ## Status: Recommended for Research Tasks

   This is the preferred implementation for any task requiring evidence gathering
   and research before making decisions.


   .. autolink-examples:: agents.planning.rewoo_tree_agent_v3
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.rewoo_tree_agent_v3.ParallelReWOOAgent
   agents.planning.rewoo_tree_agent_v3.ReWOOPlan
   agents.planning.rewoo_tree_agent_v3.ReWOOTreeAgent
   agents.planning.rewoo_tree_agent_v3.ReWOOTreeState
   agents.planning.rewoo_tree_agent_v3.TaskType
   agents.planning.rewoo_tree_agent_v3.ToolAlias


Functions
---------

.. autoapisummary::

   agents.planning.rewoo_tree_agent_v3.create_rewoo_agent_with_tools


Module Contents
---------------

.. py:class:: ParallelReWOOAgent(name: str = 'parallel_rewoo', max_parallelism: int = 8, **kwargs)

   Bases: :py:obj:`ReWOOTreeAgent`


   Enhanced ReWOO agent with maximum parallelization.


   .. autolink-examples:: ParallelReWOOAgent
      :collapse:

   .. py:attribute:: execution_mode
      :value: 'parallel'



.. py:class:: ReWOOPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured plan output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOPlan
      :collapse:

   .. py:attribute:: approach_strategy
      :type:  str
      :value: None



   .. py:attribute:: dependencies
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: fallback_strategies
      :type:  list[str]
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



   .. py:attribute:: risk_factors
      :type:  list[str]
      :value: None



   .. py:attribute:: tasks
      :type:  list[str]
      :value: None



   .. py:attribute:: tool_assignments
      :type:  dict[str, str]
      :value: None



.. py:class:: ReWOOTreeAgent(name: str = 'rewoo_tree_agent', available_tools: list[langchain_core.tools.BaseTool] | None = None, tool_aliases: dict[str, ToolAlias] | None = None, max_planning_depth: int = 3, max_parallelism: int = 4, **kwargs)

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   ReWOO Tree Agent using pure MultiAgent composition.

   No manual nodes - everything is agents that get automatically wrapped.


   .. autolink-examples:: ReWOOTreeAgent
      :collapse:

   .. py:method:: _configure_execution_flow()

      Configure execution flow using MultiAgent branching.


      .. autolink-examples:: _configure_execution_flow
         :collapse:


   .. py:method:: add_tool_alias(alias: str, actual_tool: str, force_choice: bool = True, **params)

      Add a tool alias for forced tool choice.


      .. autolink-examples:: add_tool_alias
         :collapse:


   .. py:method:: create_and_execute_plan(problem: str) -> dict[str, Any]
      :async:


      Create and execute a plan using pure MultiAgent flow.


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

   .. py:attribute:: current_plan
      :type:  ReWOOPlan | None
      :value: None



   .. py:attribute:: planning_depth
      :type:  int
      :value: None



   .. py:attribute:: task_results
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: tool_aliases
      :type:  dict[str, ToolAlias]
      :value: None



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

   Factory function to create ReWOO agent with tools.


   .. autolink-examples:: create_rewoo_agent_with_tools
      :collapse:

