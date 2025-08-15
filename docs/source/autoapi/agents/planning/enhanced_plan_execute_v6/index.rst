agents.planning.enhanced_plan_execute_v6
========================================

.. py:module:: agents.planning.enhanced_plan_execute_v6

.. autoapi-nested-parse::

   Enhanced Plan & Execute V6 - Using MultiAgent with Universal Structured Output.

   This module provides the next-generation Plan & Execute implementation using:
   - MultiAgent for multi-agent orchestration
   - Universal structured output pattern (Agent.with_structured_output)
   - BasePlannerAgent and BaseExecutorAgent from base planning components
   - Modern Haive architecture with hooks, recompilation, and state management

   ## Key Features

   - **Universal Structured Output**: Any agent can have structured output via mixins
   - **MultiAgent**: Modern multi-agent coordination with conditional routing
   - **Base Planning Components**: Uses BasePlannerAgent and BaseExecutorAgent
   - **Real Component Testing**: No mocks, actual LLM execution and tool usage
   - **Modern Architecture**: Hooks, recompilation, state management, type safety

   ## Architecture

   ```
   BasePlannerAgent.with_structured_output(BasePlan)
       ↓ (structured BasePlan output)
   BaseExecutorAgent.with_structured_output(ExecutionResult)
       ↓ (structured ExecutionResult output)
   Conditional Routing (should_continue)
       ↓
   MultiAgent orchestration
   ```

   ## Usage

   ### Basic Usage
   ```python
   from haive.agents.planning.enhanced_plan_execute_v6 import create_enhanced_plan_execute_v6

   # Create with default configuration
   agent = create_enhanced_plan_execute_v6()
   result = await agent.arun("Calculate compound interest on $1000 at 5% for 10 years")

   # Create with custom tools
   from haive.tools.tools.search_tools import tavily_search_tool
   agent = create_enhanced_plan_execute_v6(
       name="research_planner",
       executor_tools=[tavily_search_tool]
   )
   result = await agent.arun("Research Tesla stock performance and calculate ROI")
   ```

   ### Advanced Configuration
   ```python
   agent = create_enhanced_plan_execute_v6(
       name="advanced_planner",
       planner_config=AugLLMConfig(
           model="gpt-4",
           temperature=0.2,
           system_message="You are an expert strategic planner."
       ),
       executor_config=AugLLMConfig(
           model="gpt-4-turbo",
           temperature=0.1
       ),
       executor_tools=[tavily_search_tool, calculator_tool],
       max_iterations=15,
       enable_hooks=True
   )

   # Add custom hooks
   @agent.before_run
   def track_execution(context):
       print(f"Starting planning workflow: {context.agent_name}")

   result = await agent.arun("Complex multi-step research task")
   ```

   ## Status: Production Ready

   This implementation showcases the full power of modern Haive architecture:
   - MultiAgent coordination
   - Universal structured output patterns
   - Base planning components
   - Real component integration


   .. autolink-examples:: agents.planning.enhanced_plan_execute_v6
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.enhanced_plan_execute_v6.logger


Classes
-------

.. autoapisummary::

   agents.planning.enhanced_plan_execute_v6.ExecutionResult
   agents.planning.enhanced_plan_execute_v6.PlanExecuteState
   agents.planning.enhanced_plan_execute_v6.PlanningDecision


Functions
---------

.. autoapisummary::

   agents.planning.enhanced_plan_execute_v6._add_monitoring_hooks_v6
   agents.planning.enhanced_plan_execute_v6.create_enhanced_plan_execute_v6
   agents.planning.enhanced_plan_execute_v6.create_research_plan_execute_v6
   agents.planning.enhanced_plan_execute_v6.create_simple_plan_execute_v6
   agents.planning.enhanced_plan_execute_v6.get_next_step_v6
   agents.planning.enhanced_plan_execute_v6.process_executor_output_v6
   agents.planning.enhanced_plan_execute_v6.process_planner_output_v6
   agents.planning.enhanced_plan_execute_v6.should_continue_v6
   agents.planning.enhanced_plan_execute_v6.test_enhanced_plan_execute_v6


Module Contents
---------------

.. py:class:: ExecutionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured execution result from executor agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionResult
      :collapse:

   .. py:attribute:: execution_time
      :type:  str | None
      :value: None



   .. py:attribute:: issues_encountered
      :type:  list[str]
      :value: None



   .. py:attribute:: next_step_ready
      :type:  bool
      :value: None



   .. py:attribute:: output
      :type:  str
      :value: None



   .. py:attribute:: recommendations
      :type:  list[str]
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



   .. py:attribute:: success
      :type:  bool
      :value: None



   .. py:attribute:: tools_used
      :type:  list[str]
      :value: None



.. py:class:: PlanExecuteState

   Bases: :py:obj:`haive.core.schema.prebuilt.multi_agent_state.MultiAgentState`


   Enhanced state for plan and execute workflow coordination.


   .. autolink-examples:: PlanExecuteState
      :collapse:

   .. py:attribute:: completed_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: current_plan
      :type:  haive.agents.planning.base.models.BasePlan[haive.agents.planning.base.models.PlanContent] | None
      :value: None



   .. py:attribute:: current_step_id
      :type:  str | None
      :value: None



   .. py:attribute:: execution_results
      :type:  list[ExecutionResult]
      :value: None



   .. py:attribute:: failed_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:attribute:: iteration_count
      :type:  int
      :value: None



   .. py:attribute:: last_decision
      :type:  PlanningDecision | None
      :value: None



   .. py:attribute:: original_objective
      :type:  str
      :value: None



   .. py:attribute:: replan_count
      :type:  int
      :value: None



.. py:class:: PlanningDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Decision model for routing and coordination.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanningDecision
      :collapse:

   .. py:attribute:: action
      :type:  str
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:attribute:: next_step_id
      :type:  str | None
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:function:: _add_monitoring_hooks_v6(workflow: haive.agents.multi.agent.MultiAgent) -> None

   Add comprehensive monitoring hooks to the V6 workflow.


   .. autolink-examples:: _add_monitoring_hooks_v6
      :collapse:

.. py:function:: create_enhanced_plan_execute_v6(name: str = 'EnhancedPlanExecuteV6', planner_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, executor_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, executor_tools: list | None = None, max_iterations: int = 20, enable_hooks: bool = True) -> haive.agents.multi.agent.MultiAgent

   Create enhanced Plan & Execute V6 using modern Haive patterns.

   :param name: Name for the multi-agent system
   :param planner_config: Configuration for the planning agent
   :param executor_config: Configuration for the execution agent
   :param executor_tools: Tools available to the executor
   :param max_iterations: Maximum planning iterations
   :param enable_hooks: Whether to enable the hooks system

   :returns: Complete planning workflow system
   :rtype: MultiAgent

   .. rubric:: Examples

   Basic usage::

       agent = create_enhanced_plan_execute_v6()
       result = await agent.arun("Calculate compound interest")

   With custom configuration::

       agent = create_enhanced_plan_execute_v6(
           name="research_planner",
           planner_config=AugLLMConfig(model="gpt-4", temperature=0.2),
           executor_tools=[tavily_search_tool],
           max_iterations=15
       )
       result = await agent.arun("Research and analyze market trends")


   .. autolink-examples:: create_enhanced_plan_execute_v6
      :collapse:

.. py:function:: create_research_plan_execute_v6(executor_tools: list | None = None) -> haive.agents.multi.agent.MultiAgent

   Create a plan and execute agent optimized for research tasks.


   .. autolink-examples:: create_research_plan_execute_v6
      :collapse:

.. py:function:: create_simple_plan_execute_v6(executor_tools: list | None = None) -> haive.agents.multi.agent.MultiAgent

   Create a simple plan and execute agent with default settings.


   .. autolink-examples:: create_simple_plan_execute_v6
      :collapse:

.. py:function:: get_next_step_v6(plan: haive.agents.planning.base.models.BasePlan[haive.agents.planning.base.models.PlanContent], completed_steps: list[str]) -> str | None

   Get the next step ID to execute based on plan and completed steps.


   .. autolink-examples:: get_next_step_v6
      :collapse:

.. py:function:: process_executor_output_v6(state: PlanExecuteState, executor_result: ExecutionResult) -> dict

   Process executor output and update state.


   .. autolink-examples:: process_executor_output_v6
      :collapse:

.. py:function:: process_planner_output_v6(state: PlanExecuteState, planner_result: haive.agents.planning.base.models.BasePlan[haive.agents.planning.base.models.PlanContent]) -> dict

   Process planner output and update state.


   .. autolink-examples:: process_planner_output_v6
      :collapse:

.. py:function:: should_continue_v6(state: PlanExecuteState) -> str

   Enhanced routing logic for V6 workflow.


   .. autolink-examples:: should_continue_v6
      :collapse:

.. py:function:: test_enhanced_plan_execute_v6()
   :async:


   Test the enhanced plan and execute V6 system.


   .. autolink-examples:: test_enhanced_plan_execute_v6
      :collapse:

.. py:data:: logger

