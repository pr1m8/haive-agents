agents.planning.enhanced_plan_execute_v5
========================================

.. py:module:: agents.planning.enhanced_plan_execute_v5

.. autoapi-nested-parse::

   Enhanced Plan & Execute V5 - Modern Haive Implementation with Custom Models and Agents.

   This module provides a completely redesigned Plan & Execute implementation using the latest
   Haive architecture patterns, enhanced agents, and modern multi-agent orchestration.

   ## Key Features

   - **MultiAgent**: Latest multi-agent orchestration with state management
   - **SimpleAgentV3**: Enhanced planning and replanning with hooks system
   - **ReactAgent**: Advanced tool-based execution with real-time feedback
   - **Custom Pydantic Models**: Structured output designed for planning workflows
   - **Modern Prompt Engineering**: Context-aware prompts with structured templates
   - **Comprehensive Monitoring**: Full hooks system for execution tracking
   - **Dynamic Recompilation**: Real-time agent updates and tool management

   ## Architecture

   ```
   PlannerAgentV3 (SimpleAgentV3)
       ↓ (structured Plan model)
   ExecutorAgentV3 (ReactAgent) ←─┐
       ↓ (execution results)       │
   Routing Logic ──→ Continue ────┘
       ↓
   ReplannerAgentV3 (SimpleAgentV3)
       ↓ (structured Decision model)
   Final Response or Loop Back
   ```

   ## Usage

   ### Basic Usage
   ```python
   from haive.agents.planning.enhanced_plan_execute_v5 import create_enhanced_plan_execute_v5

   # Create with default tools
   agent = create_enhanced_plan_execute_v5()
   result = await agent.arun("Calculate compound interest on $1000 at 5% for 10 years")

   # Create with custom tools
   from haive.tools import web_search_tool, calculator_tool
   agent = create_enhanced_plan_execute_v5(
       name="research_planner",
       tools=[web_search_tool, calculator_tool]
   )
   result = await agent.arun("Research Tesla stock performance and calculate ROI")
   ```

   ### Advanced Configuration
   ```python
   agent = create_enhanced_plan_execute_v5(
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
       tools=[custom_tool1, custom_tool2],
       max_iterations=10,
       enable_hooks=True
   )

   # Add custom hooks
   @agent.before_run
   def track_execution(context):
       print(f"Starting planning workflow: {context.agent_name}")

   result = await agent.arun("Complex multi-step research task")
   ```

   ## Custom Models

   The implementation uses custom Pydantic models designed specifically for planning:

   - **TaskPlan**: Structured plan with steps, priorities, and dependencies
   - **ExecutionStatus**: Rich execution tracking with success/failure states
   - **PlanningDecision**: Intelligent routing decisions with reasoning
   - **PlanExecuteState**: Enhanced state management for multi-agent coordination

   ## When to Use

   ✅ **Use this implementation when**:
   - You need modern Haive architecture patterns
   - Enhanced monitoring and debugging is important
   - You want structured output and type safety
   - Dynamic agent recompilation is needed
   - Production-ready error handling is required

   ❌ **Consider alternatives when**:
   - Simple tasks that don't need planning (use ReactAgent directly)
   - Legacy compatibility is required (use clean_plan_execute)
   - Minimal complexity is preferred (use SimpleAgent)

   ## Status: Next-Generation Planning

   This is the future of planning agents in Haive, showcasing the full power
   of the enhanced base agent pattern and modern multi-agent orchestration.


   .. autolink-examples:: agents.planning.enhanced_plan_execute_v5
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.planning.enhanced_plan_execute_v5.EXECUTOR_PROMPT_TEMPLATE
   agents.planning.enhanced_plan_execute_v5.EXECUTOR_SYSTEM_MESSAGE
   agents.planning.enhanced_plan_execute_v5.PLANNER_PROMPT_TEMPLATE
   agents.planning.enhanced_plan_execute_v5.PLANNER_SYSTEM_MESSAGE
   agents.planning.enhanced_plan_execute_v5.REPLANNER_PROMPT_TEMPLATE
   agents.planning.enhanced_plan_execute_v5.REPLANNER_SYSTEM_MESSAGE
   agents.planning.enhanced_plan_execute_v5.logger


Classes
-------

.. autoapisummary::

   agents.planning.enhanced_plan_execute_v5.EnhancedPlanExecuteState
   agents.planning.enhanced_plan_execute_v5.ExecutionResult
   agents.planning.enhanced_plan_execute_v5.PlanningDecision
   agents.planning.enhanced_plan_execute_v5.TaskPlan
   agents.planning.enhanced_plan_execute_v5.TaskStep


Functions
---------

.. autoapisummary::

   agents.planning.enhanced_plan_execute_v5._add_monitoring_hooks
   agents.planning.enhanced_plan_execute_v5.create_enhanced_plan_execute_v5
   agents.planning.enhanced_plan_execute_v5.create_research_plan_execute
   agents.planning.enhanced_plan_execute_v5.create_simple_enhanced_plan_execute
   agents.planning.enhanced_plan_execute_v5.get_next_step_id
   agents.planning.enhanced_plan_execute_v5.should_continue_enhanced
   agents.planning.enhanced_plan_execute_v5.test_enhanced_plan_execute


Module Contents
---------------

.. py:class:: EnhancedPlanExecuteState

   Bases: :py:obj:`haive.core.schema.prebuilt.multi_agent_state.MultiAgentState`


   Enhanced state for plan and execute workflow with rich tracking.


   .. autolink-examples:: EnhancedPlanExecuteState
      :collapse:

   .. py:attribute:: completed_steps
      :type:  list[str]
      :value: None



   .. py:attribute:: current_plan
      :type:  TaskPlan | None
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



   .. py:attribute:: planning_start_time
      :type:  str | None
      :value: None



   .. py:attribute:: replan_count
      :type:  int
      :value: None



   .. py:attribute:: total_execution_time
      :type:  str | None
      :value: None



.. py:class:: ExecutionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Rich execution result with detailed feedback.

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



.. py:class:: PlanningDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Intelligent decision model for routing and replanning.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanningDecision
      :collapse:

   .. py:attribute:: action
      :type:  Literal['continue', 'replan', 'complete']
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:attribute:: new_plan
      :type:  TaskPlan | None
      :value: None



   .. py:attribute:: next_step_id
      :type:  str | None
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:class:: TaskPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive task plan with metadata and tracking.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskPlan
      :collapse:

   .. py:attribute:: estimated_total_time
      :type:  str | None
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: steps
      :type:  list[TaskStep]
      :value: None



   .. py:attribute:: success_criteria
      :type:  str
      :value: None



.. py:class:: TaskStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual step in a task plan with rich metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskStep
      :collapse:

   .. py:attribute:: dependencies
      :type:  list[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: estimated_time
      :type:  str | None
      :value: None



   .. py:attribute:: expected_outcome
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  Literal['high', 'medium', 'low']
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



   .. py:attribute:: tools_needed
      :type:  list[str]
      :value: None



.. py:function:: _add_monitoring_hooks(workflow: haive.agents.multi.enhanced.multi_agent_v4.MultiAgent) -> None

   Add comprehensive monitoring hooks to the workflow.


   .. autolink-examples:: _add_monitoring_hooks
      :collapse:

.. py:function:: create_enhanced_plan_execute_v5(name: str = 'EnhancedPlanExecuteV5', planner_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, executor_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, replanner_config: haive.core.engine.aug_llm.AugLLMConfig | None = None, tools: list | None = None, max_iterations: int = 20, enable_hooks: bool = True) -> haive.agents.multi.enhanced.multi_agent_v4.MultiAgent

   Create enhanced Plan & Execute agent using modern Haive patterns.

   :param name: Name for the multi-agent system
   :param planner_config: Configuration for the planning agent
   :param executor_config: Configuration for the execution agent
   :param replanner_config: Configuration for the replanning agent
   :param tools: Tools available to the executor
   :param max_iterations: Maximum planning iterations
   :param enable_hooks: Whether to enable the hooks system

   :returns: Complete planning workflow system
   :rtype: MultiAgent

   .. rubric:: Examples

   Basic usage::

       agent = create_enhanced_plan_execute_v5()
       result = await agent.arun("Calculate compound interest")

   With custom configuration::

       agent = create_enhanced_plan_execute_v5(
           name="research_planner",
           planner_config=AugLLMConfig(model="gpt-4", temperature=0.2),
           tools=[web_search_tool, calculator_tool],
           max_iterations=15
       )
       result = await agent.arun("Research and analyze market trends")


   .. autolink-examples:: create_enhanced_plan_execute_v5
      :collapse:

.. py:function:: create_research_plan_execute(tools: list | None = None) -> haive.agents.multi.enhanced.multi_agent_v4.MultiAgent

   Create a plan and execute agent optimized for research tasks.


   .. autolink-examples:: create_research_plan_execute
      :collapse:

.. py:function:: create_simple_enhanced_plan_execute(tools: list | None = None) -> haive.agents.multi.enhanced.multi_agent_v4.MultiAgent

   Create a simple enhanced plan and execute agent with default settings.


   .. autolink-examples:: create_simple_enhanced_plan_execute
      :collapse:

.. py:function:: get_next_step_id(plan: TaskPlan, completed_steps: list[str]) -> str | None

   Get the next step ID to execute based on plan and completed steps.


   .. autolink-examples:: get_next_step_id
      :collapse:

.. py:function:: should_continue_enhanced(state: EnhancedPlanExecuteState) -> str

   Enhanced routing logic based on current state and decisions.


   .. autolink-examples:: should_continue_enhanced
      :collapse:

.. py:function:: test_enhanced_plan_execute()
   :async:


   Test the enhanced plan and execute system.


   .. autolink-examples:: test_enhanced_plan_execute
      :collapse:

.. py:data:: EXECUTOR_PROMPT_TEMPLATE

.. py:data:: EXECUTOR_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a skilled task executor who specializes in carrying out specific steps in a larger plan with precision and attention to detail.
      
      Your role is to:
      1. Execute the given step exactly as described
      2. Use available tools effectively and appropriately
      3. Provide clear, detailed output about what was accomplished
      4. Note any issues or recommendations for future steps
      5. Be thorough in documenting the execution process
      
      Key Principles:
      - Focus on the specific step - don't try to do more than asked
      - Use tools when they can help achieve better results
      - Provide detailed output that others can build upon
      - Note any problems or unexpected results
      - Make recommendations for improving the process
      
      When using tools:
      - Choose the most appropriate tool for the task
      - Use tools efficiently and effectively
      - Document what tools were used and why
      - Report on the quality and usefulness of tool outputs
      """

   .. raw:: html

      </details>



.. py:data:: PLANNER_PROMPT_TEMPLATE

.. py:data:: PLANNER_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert strategic planner specializing in breaking down complex objectives into actionable, well-structured plans.
      
      Your role is to:
      1. Analyze the given objective thoroughly
      2. Create a comprehensive, step-by-step plan
      3. Ensure each step is specific, actionable, and measurable
      4. Consider dependencies between steps
      5. Estimate effort and identify required tools
      
      Key Principles:
      - Be specific and actionable in step descriptions
      - Consider what tools or resources each step needs
      - Think about the logical order and dependencies
      - Provide clear success criteria for the overall objective
      - Include your reasoning for the planning approach
      
      Focus on creating plans that are:
      - CLEAR: Each step is unambiguous
      - COMPLETE: Nothing important is missed
      - ACTIONABLE: Each step can be executed immediately
      - MEASURABLE: Success can be determined objectively
      """

   .. raw:: html

      </details>



.. py:data:: REPLANNER_PROMPT_TEMPLATE

.. py:data:: REPLANNER_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert planning analyst who specializes in evaluating progress and making intelligent decisions about next steps.
      
      Your role is to:
      1. Analyze the current progress against the original plan
      2. Determine if the objective has been achieved
      3. Decide whether to continue, replan, or complete the task
      4. Provide clear reasoning for your decisions
      5. Create revised plans when necessary
      
      Key Principles:
      - Consider the original objective - has it been achieved?
      - Evaluate the quality and completeness of results so far
      - Be realistic about what still needs to be done
      - Don't continue unnecessarily if the objective is met
      - Create better plans based on what you've learned
      
      Decision Guidelines:
      - COMPLETE: The objective has been fully achieved
      - CONTINUE: The plan is working, proceed with next step
      - REPLAN: The current approach needs adjustment or improvement
      """

   .. raw:: html

      </details>



.. py:data:: logger

