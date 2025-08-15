agents.planning.plan_execute_v3
===============================

.. py:module:: agents.planning.plan_execute_v3

.. autoapi-nested-parse::

   Plan-and-Execute V3 Agent Package.

   This package implements the Plan-and-Execute methodology using Enhanced MultiAgent V3,
   providing a comprehensive solution for complex task planning and execution.

   Key Components:
   - PlanExecuteV3Agent: Main agent coordinator
   - ExecutionPlan, StepExecution, PlanEvaluation: Structured output models
   - PlanExecuteV3State: State management with computed fields
   - System prompts for each sub-agent

   Usage:
       from haive.agents.planning.plan_execute_v3 import PlanExecuteV3Agent

       agent = PlanExecuteV3Agent(tools=[search_tool, calculator])
       result = await agent.arun("Analyze market trends for renewable energy")


   .. autolink-examples:: agents.planning.plan_execute_v3
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/planning/plan_execute_v3/agent/index
   /autoapi/agents/planning/plan_execute_v3/config/index
   /autoapi/agents/planning/plan_execute_v3/engines/index
   /autoapi/agents/planning/plan_execute_v3/models/index
   /autoapi/agents/planning/plan_execute_v3/prompts/index
   /autoapi/agents/planning/plan_execute_v3/state/index


Attributes
----------

.. autoapisummary::

   agents.planning.plan_execute_v3.EVALUATOR_SYSTEM_MESSAGE
   agents.planning.plan_execute_v3.EXECUTOR_SYSTEM_MESSAGE
   agents.planning.plan_execute_v3.PLANNER_SYSTEM_MESSAGE
   agents.planning.plan_execute_v3.REPLANNER_SYSTEM_MESSAGE
   agents.planning.plan_execute_v3.evaluator_prompt
   agents.planning.plan_execute_v3.executor_prompt
   agents.planning.plan_execute_v3.planner_prompt
   agents.planning.plan_execute_v3.replanner_prompt


Classes
-------

.. autoapisummary::

   agents.planning.plan_execute_v3.ExecutionPlan
   agents.planning.plan_execute_v3.PlanEvaluation
   agents.planning.plan_execute_v3.PlanExecuteInput
   agents.planning.plan_execute_v3.PlanExecuteOutput
   agents.planning.plan_execute_v3.PlanExecuteV3Agent
   agents.planning.plan_execute_v3.PlanExecuteV3State
   agents.planning.plan_execute_v3.PlanStep
   agents.planning.plan_execute_v3.RevisedPlan
   agents.planning.plan_execute_v3.StepExecution
   agents.planning.plan_execute_v3.StepStatus


Package Contents
----------------

.. py:class:: ExecutionPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Complete execution plan with metadata.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ExecutionPlan
      :collapse:

   .. py:method:: get_next_step() -> PlanStep | None

      Get the next step ready for execution.


      .. autolink-examples:: get_next_step
         :collapse:


   .. py:method:: get_progress_percentage() -> float

      Calculate completion percentage.


      .. autolink-examples:: get_progress_percentage
         :collapse:


   .. py:method:: has_failures() -> bool

      Check if any steps have failed.


      .. autolink-examples:: has_failures
         :collapse:


   .. py:method:: is_complete() -> bool

      Check if all steps are completed.


      .. autolink-examples:: is_complete
         :collapse:


   .. py:method:: update_total_steps()

      Ensure total_steps matches actual step count.


      .. autolink-examples:: update_total_steps
         :collapse:


   .. py:method:: validate_step_ids(v)
      :classmethod:


      Ensure step IDs are sequential starting from 1.


      .. autolink-examples:: validate_step_ids
         :collapse:


   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: estimated_duration
      :type:  str | None
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: steps
      :type:  list[PlanStep]
      :value: None



   .. py:attribute:: total_steps
      :type:  int
      :value: None



.. py:class:: PlanEvaluation(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Evaluation of current plan progress and decision on next action.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanEvaluation
      :collapse:

   .. py:method:: validate_decision_fields()

      Ensure required fields are present based on decision.


      .. autolink-examples:: validate_decision_fields
         :collapse:


   .. py:attribute:: current_progress
      :type:  str
      :value: None



   .. py:attribute:: decision
      :type:  str
      :value: None



   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:attribute:: plan_status
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: revision_notes
      :type:  str | None
      :value: None



.. py:class:: PlanExecuteInput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input format for the Plan-and-Execute agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanExecuteInput
      :collapse:

   .. py:attribute:: context
      :type:  str | None
      :value: None



   .. py:attribute:: max_steps
      :type:  int
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: time_limit
      :type:  int | None
      :value: None



.. py:class:: PlanExecuteOutput(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final output from the Plan-and-Execute agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanExecuteOutput
      :collapse:

   .. py:attribute:: confidence_score
      :type:  float
      :value: None



   .. py:attribute:: execution_summary
      :type:  str
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



   .. py:attribute:: key_findings
      :type:  list[str]
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: revisions_made
      :type:  int
      :value: None



   .. py:attribute:: steps_completed
      :type:  int
      :value: None



   .. py:attribute:: total_execution_time
      :type:  float
      :value: None



   .. py:attribute:: total_steps
      :type:  int
      :value: None



.. py:class:: PlanExecuteV3Agent(name: str = 'plan_execute_v3', config: haive.core.engine.aug_llm.AugLLMConfig | None = None, tools: list[langchain_core.tools.Tool] | None = None, max_iterations: int = 5, max_steps_per_plan: int = 10)

   Plan-and-Execute V3 Agent using Enhanced MultiAgent V3.

   This agent separates planning and execution into distinct phases:
   1. Planner: Creates detailed execution plans (SimpleAgent -> ExecutionPlan)
   2. Executor: Executes individual steps with tools (ReactAgent -> StepExecution)
   3. Evaluator: Evaluates progress and decides next action (SimpleAgent -> PlanEvaluation)
   4. Replanner: Creates revised plans when needed (SimpleAgent -> RevisedPlan)

   The Enhanced MultiAgent V3 coordinates these sub-agents using conditional routing
   based on plan progress and evaluation decisions.

   .. attribute:: name

      Agent name

   .. attribute:: config

      LLM configuration

   .. attribute:: tools

      Available tools for execution

   .. attribute:: max_iterations

      Maximum planning iterations

   .. attribute:: max_steps_per_plan

      Maximum steps per plan

   Initialize Plan-and-Execute V3 agent.

   :param name: Agent name
   :param config: LLM configuration (uses default if None)
   :param tools: Available tools for execution
   :param max_iterations: Maximum planning iterations
   :param max_steps_per_plan: Maximum steps per plan


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanExecuteV3Agent
      :collapse:

   .. py:method:: _setup_routing() -> None

      Set up conditional routing between sub-agents.


      .. autolink-examples:: _setup_routing
         :collapse:


   .. py:method:: arun(input_data: str | dict[str, Any] | agents.planning.plan_execute_v3.models.PlanExecuteInput, state: agents.planning.plan_execute_v3.state.PlanExecuteV3State | None = None) -> agents.planning.plan_execute_v3.models.PlanExecuteOutput
      :async:


      Execute the Plan-and-Execute agent asynchronously.

      :param input_data: Input objective/request
      :param state: Optional existing state (creates new if None)

      :returns: PlanExecuteOutput with final results


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: get_capabilities() -> dict[str, Any]

      Get agent capabilities description.


      .. autolink-examples:: get_capabilities
         :collapse:


   .. py:method:: run(input_data: str | dict[str, Any] | agents.planning.plan_execute_v3.models.PlanExecuteInput, state: agents.planning.plan_execute_v3.state.PlanExecuteV3State | None = None) -> agents.planning.plan_execute_v3.models.PlanExecuteOutput

      Execute the Plan-and-Execute agent synchronously.

      :param input_data: Input objective/request
      :param state: Optional existing state

      :returns: PlanExecuteOutput with final results


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: evaluator


   .. py:attribute:: executor


   .. py:attribute:: max_iterations
      :value: 5



   .. py:attribute:: max_steps_per_plan
      :value: 10



   .. py:attribute:: multi_agent


   .. py:attribute:: name
      :value: 'plan_execute_v3'



   .. py:attribute:: planner


   .. py:attribute:: replanner


   .. py:attribute:: tools
      :value: []



.. py:class:: PlanExecuteV3State

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State schema for Plan-and-Execute V3 agent.

   This state is shared across the planner, executor, evaluator, and replanner
   sub-agents to maintain full context throughout the execution.


   .. autolink-examples:: PlanExecuteV3State
      :collapse:

   .. py:method:: add_evaluation(evaluation: agents.planning.plan_execute_v3.models.PlanEvaluation) -> None

      Add an evaluation result.


      .. autolink-examples:: add_evaluation
         :collapse:


   .. py:method:: add_step_execution(execution: agents.planning.plan_execute_v3.models.StepExecution) -> None

      Add a step execution result and update plan.


      .. autolink-examples:: add_step_execution
         :collapse:


   .. py:method:: revise_plan(new_plan: agents.planning.plan_execute_v3.models.ExecutionPlan) -> None

      Replace current plan with a revised version.


      .. autolink-examples:: revise_plan
         :collapse:


   .. py:attribute:: completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: context
      :type:  dict[str, Any]
      :value: None



   .. py:property:: current_step
      :type: str | None


      Get the current step description for the executor.

      .. autolink-examples:: current_step
         :collapse:


   .. py:attribute:: current_step_id
      :type:  int | None
      :value: None



   .. py:attribute:: errors
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: evaluations
      :type:  list[agents.planning.plan_execute_v3.models.PlanEvaluation]
      :value: None



   .. py:property:: execution_summary
      :type: str


      Get a summary of the entire execution.

      .. autolink-examples:: execution_summary
         :collapse:


   .. py:property:: execution_time
      :type: float | None


      Total execution time in seconds.

      .. autolink-examples:: execution_time
         :collapse:


   .. py:attribute:: final_answer
      :type:  str | None
      :value: None



   .. py:property:: key_findings
      :type: list[str]


      Extract key findings from executions.

      .. autolink-examples:: key_findings
         :collapse:


   .. py:property:: objective
      :type: str


      Extract the objective from the plan or messages.

      .. autolink-examples:: objective
         :collapse:


   .. py:attribute:: plan
      :type:  agents.planning.plan_execute_v3.models.ExecutionPlan | None
      :value: None



   .. py:attribute:: plan_history
      :type:  list[agents.planning.plan_execute_v3.models.ExecutionPlan]
      :value: None



   .. py:property:: plan_status
      :type: str


      Get formatted plan status for agents.

      .. autolink-examples:: plan_status
         :collapse:


   .. py:property:: previous_results
      :type: str


      Get formatted previous step execution results.

      .. autolink-examples:: previous_results
         :collapse:


   .. py:attribute:: revision_count
      :type:  int
      :value: None



   .. py:property:: should_evaluate
      :type: bool


      Determine if we should run evaluation.

      .. autolink-examples:: should_evaluate
         :collapse:


   .. py:attribute:: started_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: step_executions
      :type:  list[agents.planning.plan_execute_v3.models.StepExecution]
      :value: None



.. py:class:: PlanStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual step in an execution plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanStep
      :collapse:

   .. py:method:: validate_dependencies(v, info)
      :classmethod:


      Ensure dependencies are valid step IDs.


      .. autolink-examples:: validate_dependencies
         :collapse:


   .. py:attribute:: dependencies
      :type:  list[int]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: execution_time
      :type:  float | None
      :value: None



   .. py:attribute:: expected_output
      :type:  str
      :value: None



   .. py:attribute:: result
      :type:  str | None
      :value: None



   .. py:attribute:: status
      :type:  StepStatus
      :value: None



   .. py:attribute:: step_id
      :type:  int
      :value: None



   .. py:attribute:: tools_required
      :type:  list[str]
      :value: None



.. py:class:: RevisedPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Revised execution plan based on evaluation.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RevisedPlan
      :collapse:

   .. py:attribute:: changes_made
      :type:  str
      :value: None



   .. py:attribute:: new_plan
      :type:  ExecutionPlan
      :value: None



   .. py:attribute:: original_objective
      :type:  str
      :value: None



   .. py:attribute:: retained_results
      :type:  list[str]
      :value: None



   .. py:attribute:: revision_reason
      :type:  str
      :value: None



.. py:class:: StepExecution(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result from executing a single step.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepExecution
      :collapse:

   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: execution_time
      :type:  float
      :value: None



   .. py:attribute:: observations
      :type:  str
      :value: None



   .. py:attribute:: result
      :type:  str
      :value: None



   .. py:attribute:: step_description
      :type:  str
      :value: None



   .. py:attribute:: step_id
      :type:  int
      :value: None



   .. py:attribute:: success
      :type:  bool
      :value: None



   .. py:attribute:: tools_used
      :type:  list[str]
      :value: None



.. py:class:: StepStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status of a plan step.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StepStatus
      :collapse:

   .. py:attribute:: COMPLETED
      :value: 'completed'



   .. py:attribute:: FAILED
      :value: 'failed'



   .. py:attribute:: IN_PROGRESS
      :value: 'in_progress'



   .. py:attribute:: PENDING
      :value: 'pending'



   .. py:attribute:: SKIPPED
      :value: 'skipped'



.. py:data:: EVALUATOR_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert evaluation agent responsible for assessing plan progress and determining next actions.
      
      Your role is to analyze the current state of execution and decide whether to continue, replan, or provide a final answer.
      
      ## Evaluation Criteria:
      
      1. **Progress Assessment**: How much has been accomplished toward the objective?
      2. **Quality Check**: Are the results sufficient and accurate?
      3. **Completion Test**: Can we provide a comprehensive final answer now?
      4. **Failure Analysis**: Are there critical errors that require replanning?
      5. **Efficiency Review**: Is the current approach optimal?
      
      ## Decision Framework:
      
      **CONTINUE**: When:
      - Plan is proceeding well with good results
      - Next steps are clear and feasible
      - No major issues or failures detected
      - More execution is needed to complete the objective
      
      **REPLAN**: When:
      - Current approach has fundamental issues
      - Step failures suggest a different strategy is needed
      - New information requires significant plan changes
      - Original plan was insufficient or incorrect
      
      **FINALIZE**: When:
      - Sufficient information has been gathered
      - Objective can be comprehensively answered
      - Further execution would not add significant value
      - Quality threshold has been met
      
      ## Output Requirements:
      
      - Summarize current progress clearly
      - Explain reasoning for the decision
      - If finalizing, provide complete answer
      - If replanning, specify what needs to change
      
      Remember: Focus on achieving the best outcome for the user's objective."""

   .. raw:: html

      </details>



.. py:data:: EXECUTOR_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert execution agent responsible for carrying out individual steps in a plan.
      
      Your role is to execute the current step using available tools and knowledge, then provide detailed results for the next steps to build upon.
      
      ## Execution Principles:
      
      1. **Focus**: Execute only the current assigned step
      2. **Tools**: Use appropriate tools when needed (search, calculation, analysis, etc.)
      3. **Thoroughness**: Provide comprehensive results that future steps can use
      4. **Adaptability**: If the step can't be completed as written, explain why and what you did instead
      5. **Documentation**: Record what tools were used and key observations
      
      ## Available Capabilities:
      
      - Web search for current information
      - Mathematical calculations
      - Data analysis and processing
      - File operations
      - API integrations
      - Reasoning and synthesis
      
      ## Output Requirements:
      
      - Clearly state what was accomplished
      - Include relevant details and findings
      - Note any tools that were used
      - Highlight key observations or insights
      - Flag any issues or limitations encountered
      
      Remember: Your results will be used by subsequent steps and final evaluation, so be thorough and accurate."""

   .. raw:: html

      </details>



.. py:data:: PLANNER_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert planning agent responsible for creating detailed, actionable execution plans.
      
      Your role is to analyze the user's objective and break it down into clear, sequential steps that can be executed by a separate executor agent.
      
      ## Planning Principles:
      
      1. **Clarity**: Each step must be self-contained and actionable
      2. **Dependencies**: Identify which steps depend on others
      3. **Tools**: Specify which tools might be needed for each step
      4. **Output Focus**: Define what each step should produce
      5. **Feasibility**: Ensure steps are realistic and achievable
      
      ## Step Guidelines:
      
      - Number steps sequentially starting from 1
      - Keep each step focused on a single task or outcome
      - Include expected output for each step
      - Identify tool requirements where applicable
      - Set up dependencies to ensure proper order
      - Balance thoroughness with efficiency
      
      ## Important Considerations:
      
      - The executor agent will have access to tools like search, calculation, analysis, etc.
      - Each step should build on previous results
      - Consider potential failure points and make steps resilient
      - Aim for 3-10 steps depending on complexity
      - Be specific about what constitutes success for each step
      
      Remember: You are creating a plan for another agent to execute, so be explicit about requirements and expected outcomes."""

   .. raw:: html

      </details>



.. py:data:: REPLANNER_SYSTEM_MESSAGE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """You are an expert replanning agent responsible for creating revised execution plans.
      
      Your role is to analyze what has been accomplished, identify what went wrong or what changed, and create an improved plan moving forward.
      
      ## Replanning Principles:
      
      1. **Learn from Results**: Incorporate findings from completed steps
      2. **Retain Value**: Keep useful results from previous execution
      3. **Address Issues**: Fix problems that caused the need for replanning
      4. **Optimize**: Improve efficiency and approach based on experience
      5. **Focus**: Maintain focus on the original objective
      
      ## Revision Strategies:
      
      - **Strategy Change**: Fundamentally different approach to the problem
      - **Step Refinement**: Improve specific steps that were problematic
      - **Sequence Adjustment**: Reorder steps for better flow
      - **Tool Optimization**: Better tool selection for remaining tasks
      - **Scope Adjustment**: Expand or narrow focus based on findings
      
      ## Key Considerations:
      
      - What worked well in the previous plan?
      - What specific issues need to be addressed?
      - What new information do we have?
      - How can we build on existing results?
      - What's the most efficient path forward?
      
      ## Output Requirements:
      
      - Explain why replanning was necessary
      - Identify what results to retain from previous execution
      - Present clear, improved plan with better steps
      - Justify changes made to the original approach
      
      Remember: The goal is to create a better plan that learns from experience while staying focused on the original objective."""

   .. raw:: html

      </details>



.. py:data:: evaluator_prompt

.. py:data:: executor_prompt

.. py:data:: planner_prompt

.. py:data:: replanner_prompt

