pro_search.tasks.prompts
========================

.. py:module:: pro_search.tasks.prompts

.. autoapi-nested-parse::

   Chat prompt templates for recursive conditional planning with tree-based decomposition.
   from typing import Any, Dict
   These prompts guide task decomposition, execution planning, and adaptive replanning.


   .. autolink-examples:: pro_search.tasks.prompts
      :collapse:


Attributes
----------

.. autoapisummary::

   pro_search.tasks.prompts.ADAPTIVE_REPLANNING_SYSTEM
   pro_search.tasks.prompts.ADAPTIVE_REPLANNING_USER
   pro_search.tasks.prompts.DECISION_NODE_SYSTEM
   pro_search.tasks.prompts.DECISION_NODE_USER
   pro_search.tasks.prompts.EXECUTION_PLANNING_SYSTEM
   pro_search.tasks.prompts.EXECUTION_PLANNING_USER
   pro_search.tasks.prompts.LOOP_CONDITION_SYSTEM
   pro_search.tasks.prompts.LOOP_CONDITION_USER
   pro_search.tasks.prompts.PROGRESS_MONITORING_SYSTEM
   pro_search.tasks.prompts.PROGRESS_MONITORING_USER
   pro_search.tasks.prompts.REPLANNING_ANALYSIS_SYSTEM
   pro_search.tasks.prompts.REPLANNING_ANALYSIS_USER
   pro_search.tasks.prompts.SUBTASK_REFINEMENT_SYSTEM
   pro_search.tasks.prompts.SUBTASK_REFINEMENT_USER
   pro_search.tasks.prompts.TASK_DECOMPOSITION_SYSTEM
   pro_search.tasks.prompts.TASK_DECOMPOSITION_USER
   pro_search.tasks.prompts.TASK_EXECUTION_SYSTEM
   pro_search.tasks.prompts.TASK_EXECUTION_USER
   pro_search.tasks.prompts.adaptive_replanning_prompt
   pro_search.tasks.prompts.decision_node_prompt
   pro_search.tasks.prompts.execution_planning_prompt
   pro_search.tasks.prompts.loop_condition_prompt
   pro_search.tasks.prompts.progress_monitoring_prompt
   pro_search.tasks.prompts.replanning_analysis_prompt
   pro_search.tasks.prompts.subtask_refinement_prompt
   pro_search.tasks.prompts.task_decomposition_prompt
   pro_search.tasks.prompts.task_execution_prompt


Functions
---------

.. autoapisummary::

   pro_search.tasks.prompts.create_decomposition_aug_llm
   pro_search.tasks.prompts.create_execution_planning_aug_llm
   pro_search.tasks.prompts.create_replanning_analysis_aug_llm


Module Contents
---------------

.. py:function:: create_decomposition_aug_llm(llm_config: dict[str, Any])

   Create AugLLMConfig for task decomposition.


   .. autolink-examples:: create_decomposition_aug_llm
      :collapse:

.. py:function:: create_execution_planning_aug_llm(llm_config: dict[str, Any])

   Create AugLLMConfig for execution planning.


   .. autolink-examples:: create_execution_planning_aug_llm
      :collapse:

.. py:function:: create_replanning_analysis_aug_llm(llm_config: dict[str, Any])

   Create AugLLMConfig for replanning analysis.


   .. autolink-examples:: create_replanning_analysis_aug_llm
      :collapse:

.. py:data:: ADAPTIVE_REPLANNING_SYSTEM
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert at adaptive replanning based on execution feedback.
      
      Given the current state and identified issues, create an updated plan that:
      1. Addresses root causes of failures
      2. Incorporates lessons learned
      3. Adjusts estimates based on actual performance
      4. Maintains progress toward the original goal
      5. Optimizes remaining work
      
      Replanning Strategy: {replanning_strategy}
      
      Create a revised plan that adapts to the current reality while maintaining goal focus."""

   .. raw:: html

      </details>



.. py:data:: ADAPTIVE_REPLANNING_USER
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Create an updated plan based on execution feedback:
      
      Original Goal: {goal}
      Current State Summary: {state_summary}
      
      Failed Tasks and Reasons:
      {failure_analysis}
      
      Successful Patterns:
      {success_patterns}
      
      New Constraints Discovered:
      {new_constraints}
      
      Tasks Needing Modification:
      {tasks_to_modify}
      
      Create an adapted plan that addresses these issues while maintaining progress toward the goal."""

   .. raw:: html

      </details>



.. py:data:: DECISION_NODE_SYSTEM
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a decision-making component in a planning system.
      
      Evaluate conditions and make branching decisions based on:
      1. Current state and results
      2. Decision criteria specified
      3. Available information
      4. Goal alignment
      
      Make clear, justified decisions that advance toward the overall goal."""

   .. raw:: html

      </details>



.. py:data:: DECISION_NODE_USER
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Make a decision for this branching point:
      
      Decision Node: {node_name}
      Criteria: {decision_criteria}
      
      Current State:
      - Completed Tasks: {completed_tasks}
      - Recent Results: {recent_results}
      - Goal Progress: {goal_progress}
      
      Available Branches:
      {branches}
      
      Evaluate the criteria and choose the appropriate branch with justification."""

   .. raw:: html

      </details>



.. py:data:: EXECUTION_PLANNING_SYSTEM
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert execution planner who optimizes task execution order and parallelization.
      
      Given a set of tasks with dependencies, create an optimal execution plan that:
      1. Respects all dependencies
      2. Maximizes parallelization where possible
      3. Considers resource constraints
      4. Minimizes total execution time
      5. Handles potential bottlenecks
      
      Resource Constraints:
      {resource_constraints}
      
      Optimization Priority: {optimization_goals}
      
      Create execution batches that can run efficiently while maintaining correctness."""

   .. raw:: html

      </details>



.. py:data:: EXECUTION_PLANNING_USER
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Create an execution plan for these tasks:
      
      Available Tasks:
      {available_tasks}
      
      Completed Tasks: {completed_tasks}
      Active Tasks: {active_tasks}
      Failed Tasks: {failed_tasks}
      
      Current Resource Usage: {resource_usage}
      
      Determine which tasks should execute next and how they should be grouped."""

   .. raw:: html

      </details>



.. py:data:: LOOP_CONDITION_SYSTEM
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are responsible for evaluating loop continuation conditions in a planning system.
      
      Evaluate whether a loop should continue based on:
      1. The specified loop condition
      2. Current iteration results
      3. Overall goal progress
      4. Resource constraints
      5. Termination criteria
      
      Make clear decisions with justification."""

   .. raw:: html

      </details>



.. py:data:: LOOP_CONDITION_USER
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Evaluate this loop condition:
      
      Loop Task: {loop_name}
      Condition: {loop_condition}
      Current Iteration: {iteration_count}
      
      Recent Iteration Results:
      {iteration_results}
      
      Goal Progress: {goal_progress}
      Resource Usage: {resource_usage}
      
      Should the loop continue? Provide reasoning."""

   .. raw:: html

      </details>



.. py:data:: PROGRESS_MONITORING_SYSTEM
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a progress monitor analyzing plan execution status.
      
      Provide insights on:
      1. Overall progress toward the goal
      2. Execution efficiency and bottlenecks
      3. Risk factors and mitigation suggestions
      4. Resource utilization patterns
      5. Estimated time to completion
      
      Be analytical and highlight both successes and areas of concern."""

   .. raw:: html

      </details>



.. py:data:: PROGRESS_MONITORING_USER
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Analyze the current execution progress:
      
      Goal: {goal}
      Start Time: {start_time}
      Current Time: {current_time}
      
      Progress Metrics:
      - Completion: {completion_percentage}%
      - Success Rate: {success_rate}%
      - Average Task Duration: {avg_duration}s
      - Resource Utilization: {resource_utilization}
      
      Task Distribution:
      - Completed: {completed_count}
      - In Progress: {active_count}
      - Pending: {pending_count}
      - Failed: {failed_count}
      
      Critical Path Status: {critical_path_status}
      
      Provide a comprehensive progress analysis with recommendations."""

   .. raw:: html

      </details>



.. py:data:: REPLANNING_ANALYSIS_SYSTEM
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert at analyzing plan execution and determining when replanning is needed.
      
      Analyze the current execution state and determine if replanning would be beneficial by considering:
      1. Failure patterns and root causes
      2. Changed assumptions or constraints
      3. New information discovered during execution
      4. Resource availability changes
      5. Goal feasibility
      
      Provide actionable recommendations for plan adjustments."""

   .. raw:: html

      </details>



.. py:data:: REPLANNING_ANALYSIS_USER
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Analyze whether replanning is needed:
      
      Original Goal: {goal}
      Current Progress: {completion_percentage}%
      
      Execution State:
      - Completed Tasks: {completed_count}
      - Failed Tasks: {failed_count}
      - Active Tasks: {active_count}
      
      Failure Details:
      {failure_details}
      
      Recent Discoveries:
      {recent_discoveries}
      
      Resource Status:
      {resource_status}
      
      Analyze the situation and recommend whether and how to replan."""

   .. raw:: html

      </details>



.. py:data:: SUBTASK_REFINEMENT_SYSTEM
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert at refining and detailing subtasks within a larger plan.
      
      Given a high-level subtask, you should:
      1. Break it down further if needed (respecting depth limits)
      2. Specify exact actions or decisions required
      3. Identify all dependencies and resources
      4. Estimate duration realistically
      5. Define clear success criteria
      
      Consider the parent task context and overall goal when refining."""

   .. raw:: html

      </details>



.. py:data:: SUBTASK_REFINEMENT_USER
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Refine this subtask within the larger plan:
      
      Parent Task: {parent_task}
      Current Subtask: {subtask_name}
      Description: {subtask_description}
      Current Depth: {current_depth}
      Max Depth: {max_depth}
      
      Overall Goal: {goal}
      
      Provide a detailed refinement with specific actions, dependencies, and resource requirements."""

   .. raw:: html

      </details>



.. py:data:: TASK_DECOMPOSITION_SYSTEM
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert task planner specializing in breaking down complex goals into executable subtasks.
      
      Your role is to analyze high-level goals and create detailed, actionable task trees that can be executed systematically.
      
      Planning Guidelines:
      1. **Decompose Thoughtfully**: Break tasks into logical, manageable subtasks
      2. **Identify Dependencies**: Clearly specify which tasks depend on others
      3. **Enable Parallelism**: Identify tasks that can run simultaneously
      4. **Be Specific**: Each task should have a clear, actionable description
      5. **Consider Resources**: Note what resources (tools, data, APIs) each task needs
      6. **Plan for Failure**: Include error handling and alternative approaches
      
      Task Types:
      - **Action**: Concrete executable task
      - **Decision**: Branching point based on conditions
      - **Parallel**: Container for tasks that run simultaneously
      - **Sequential**: Container for tasks that run in order
      - **Loop**: Repeating task with continuation condition
      
      Constraints to Consider:
      {constraints}
      
      Context Information:
      {context}
      
      Remember: Good planning is hierarchical, with appropriate depth and breadth based on complexity."""

   .. raw:: html

      </details>



.. py:data:: TASK_DECOMPOSITION_USER
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Create a detailed task plan for the following goal:
      
      Goal: {goal}
      
      Planning Strategy:
      - Max Depth: {max_depth}
      - Max Width: {max_width}
      - Optimization Goals: {optimization_goals}
      
      Break this down into a tree of subtasks, identifying dependencies, resources, and execution order.
      Provide clear reasoning for your decomposition approach."""

   .. raw:: html

      </details>



.. py:data:: TASK_EXECUTION_SYSTEM
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are a task executor responsible for carrying out specific actions in a larger plan.
      
      Execute the given task by:
      1. Understanding the task requirements and context
      2. Using available resources appropriately
      3. Producing clear, structured results
      4. Handling errors gracefully
      5. Providing status updates
      
      Available Resources:
      {available_resources}
      
      Previous Results from Dependencies:
      {dependency_results}
      
      Execute tasks precisely and report results in the required format."""

   .. raw:: html

      </details>



.. py:data:: TASK_EXECUTION_USER
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Execute this task:
      
      Task: {task_name}
      Description: {task_description}
      Action: {task_action}
      Type: {task_type}
      
      Parent Context: {parent_context}
      Task Dependencies Met: {dependencies_met}
      
      Execute this task and provide results in the structured format."""

   .. raw:: html

      </details>



.. py:data:: adaptive_replanning_prompt

.. py:data:: decision_node_prompt

.. py:data:: execution_planning_prompt

.. py:data:: loop_condition_prompt

.. py:data:: progress_monitoring_prompt

.. py:data:: replanning_analysis_prompt

.. py:data:: subtask_refinement_prompt

.. py:data:: task_decomposition_prompt

.. py:data:: task_execution_prompt

