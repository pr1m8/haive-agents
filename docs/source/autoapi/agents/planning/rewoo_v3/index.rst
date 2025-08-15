agents.planning.rewoo_v3
========================

.. py:module:: agents.planning.rewoo_v3

.. autoapi-nested-parse::

   ReWOO V3 Agent - Reasoning WithOut Observation using Enhanced MultiAgent V3.

   This package implements the ReWOO (Reasoning WithOut Observation) methodology
   using our proven Enhanced MultiAgent V3 patterns from Plan-and-Execute V3 success.

   ReWOO separates planning, execution, and synthesis phases for improved efficiency:
   1. Planner creates complete reasoning plan upfront with evidence placeholders
   2. Worker executes all tool calls in batch to collect evidence
   3. Solver synthesizes all evidence into comprehensive final answer

   Key advantages over traditional iterative agents:
   - 5x token efficiency improvement
   - Parallel/batch tool execution capability
   - Robust handling of partial failures
   - Modular design for fine-tuning

   Usage:
       >>> from haive.agents.planning.rewoo_v3 import ReWOOV3Agent
       >>> from haive.core.engine.aug_llm import AugLLMConfig
       >>>
       >>> config = AugLLMConfig(temperature=0.7)
       >>> agent = ReWOOV3Agent(
       ...     name="research_agent",
       ...     config=config,
       ...     tools=[search_tool, calculator_tool]
       ... )
       >>>
       >>> result = await agent.arun("Research market trends and calculate growth rates")
       >>> print(f"Answer: {result.final_answer}")
       >>> print(f"Confidence: {result.confidence}")
       >>> print(f"Evidence collected: {result.evidence_collected}")

   Architecture:
       - ReWOOV3Agent: Main coordinator using Enhanced MultiAgent V3
       - ReWOOV3State: State schema with computed fields for dynamic prompts
       - ReWOOPlan/EvidenceCollection/ReWOOSolution: Structured output models
       - ChatPromptTemplates: Dynamic prompts with state field placeholders


   .. autolink-examples:: agents.planning.rewoo_v3
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/planning/rewoo_v3/agent/index
   /autoapi/agents/planning/rewoo_v3/models/index
   /autoapi/agents/planning/rewoo_v3/prompts/index
   /autoapi/agents/planning/rewoo_v3/state/index


Classes
-------

.. autoapisummary::

   agents.planning.rewoo_v3.EvidenceCollection
   agents.planning.rewoo_v3.EvidenceItem
   agents.planning.rewoo_v3.EvidenceStatus
   agents.planning.rewoo_v3.PlanStep
   agents.planning.rewoo_v3.ReWOOPlan
   agents.planning.rewoo_v3.ReWOOSolution
   agents.planning.rewoo_v3.ReWOOV3Agent
   agents.planning.rewoo_v3.ReWOOV3Input
   agents.planning.rewoo_v3.ReWOOV3Output
   agents.planning.rewoo_v3.ReWOOV3State


Package Contents
----------------

.. py:class:: EvidenceCollection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Worker agent structured output with all collected evidence.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EvidenceCollection
      :collapse:

   .. py:attribute:: collection_id
      :type:  str
      :value: None



   .. py:attribute:: completed_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: evidence_items
      :type:  list[EvidenceItem]
      :value: None



   .. py:attribute:: execution_notes
      :type:  list[str]
      :value: None



   .. py:attribute:: failure_count
      :type:  int
      :value: None



   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: success_count
      :type:  int
      :value: None



   .. py:attribute:: summary
      :type:  str
      :value: None



   .. py:attribute:: tools_used
      :type:  list[str]
      :value: None



.. py:class:: EvidenceItem(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual piece of evidence collected by Worker.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EvidenceItem
      :collapse:

   .. py:attribute:: content
      :type:  str
      :value: None



   .. py:attribute:: evidence_id
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: source
      :type:  str
      :value: None



   .. py:attribute:: status
      :type:  EvidenceStatus
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



   .. py:attribute:: timestamp
      :type:  datetime.datetime
      :value: None



.. py:class:: EvidenceStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status of evidence collection.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: EvidenceStatus
      :collapse:

   .. py:attribute:: FAILED
      :value: 'failed'



   .. py:attribute:: PARTIAL
      :value: 'partial'



   .. py:attribute:: PENDING
      :value: 'pending'



   .. py:attribute:: SUCCESS
      :value: 'success'



.. py:class:: PlanStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual step in the ReWOO plan.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlanStep
      :collapse:

   .. py:attribute:: depends_on
      :type:  list[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: evidence_id
      :type:  str
      :value: None



   .. py:attribute:: step_id
      :type:  str
      :value: None



   .. py:attribute:: tool_call
      :type:  str | None
      :value: None



.. py:class:: ReWOOPlan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Structured planning output from Planner agent.

   The plan contains all steps upfront without seeing any tool results.
   Each step has an evidence placeholder that will be filled by the Worker.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOPlan
      :collapse:

   .. py:attribute:: approach
      :type:  str
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: expected_evidence
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: objective
      :type:  str
      :value: None



   .. py:attribute:: plan_id
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



.. py:class:: ReWOOSolution(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final synthesized solution from Solver agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOSolution
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: created_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: evidence_used
      :type:  list[str]
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



   .. py:attribute:: limitations
      :type:  list[str]
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: solution_id
      :type:  str
      :value: None



   .. py:attribute:: synthesis_process
      :type:  str
      :value: None



.. py:class:: ReWOOV3Agent(name: str, config: haive.core.engine.aug_llm.AugLLMConfig, tools: list | None = None, max_steps: int = 10, **kwargs)

   ReWOO V3 Agent using Enhanced MultiAgent V3 coordination.

   Implements ReWOO (Reasoning WithOut Observation) methodology:
   - Separates planning, execution, and synthesis phases
   - Plans complete solution upfront without tool observation
   - Executes all tool calls in batch/parallel
   - Synthesizes all evidence together for final answer

   This provides significant efficiency gains over traditional iterative
   agent approaches while maintaining high solution quality.

   Initialize ReWOO V3 Agent.

   :param name: Agent identifier
   :param config: Base LLM configuration for all sub-agents
   :param tools: Available tools for worker agent execution
   :param max_steps: Maximum planning steps allowed
   :param \*\*kwargs: Additional configuration for Enhanced MultiAgent V3


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOV3Agent
      :collapse:

   .. py:method:: _format_output(result: agents.planning.rewoo_v3.state.ReWOOV3State, query: str, total_time: float, planning_time: float, execution_time: float, solving_time: float) -> agents.planning.rewoo_v3.models.ReWOOV3Output

      Format Enhanced MultiAgent V3 result into structured output.

      :param result: Final state from Enhanced MultiAgent V3 execution
      :param query: Original query
      :param total_time: Total execution time
      :param planning_time: Time spent in planning phase
      :param execution_time: Time spent in execution phase
      :param solving_time: Time spent in solving phase

      :returns: Structured ReWOO V3 output with all results and metadata


      .. autolink-examples:: _format_output
         :collapse:


   .. py:method:: _setup_sub_agents()

      Create ReWOO sub-agents with proper prompt templates.

      CRITICAL: Uses prompt_template (NOT system_message) following
      proven Plan-and-Execute V3 pattern.


      .. autolink-examples:: _setup_sub_agents
         :collapse:


   .. py:method:: arun(query: str, context: str | None = None, max_steps: int | None = None, tools_preference: list[str] | None = None, **kwargs) -> agents.planning.rewoo_v3.models.ReWOOV3Output
      :async:


      Execute ReWOO V3 workflow asynchronously.

      :param query: User query to solve using ReWOO methodology
      :param context: Optional additional context
      :param max_steps: Override default max steps
      :param tools_preference: Preferred tools to use
      :param \*\*kwargs: Additional arguments for Enhanced MultiAgent V3

      :returns: Structured output with complete ReWOO results and metadata


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: run(query: str, context: str | None = None, max_steps: int | None = None, tools_preference: list[str] | None = None, **kwargs) -> agents.planning.rewoo_v3.models.ReWOOV3Output

      Synchronous wrapper for ReWOO V3 execution.

      :param query: User query to solve
      :param context: Optional additional context
      :param max_steps: Override default max steps
      :param tools_preference: Preferred tools to use
      :param \*\*kwargs: Additional arguments

      :returns: Structured output with ReWOO results


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: execution_stats


   .. py:attribute:: max_steps
      :value: 10



   .. py:attribute:: multi_agent


   .. py:attribute:: name


   .. py:attribute:: tools
      :value: []



.. py:class:: ReWOOV3Input(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Input model for ReWOO V3 agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOV3Input
      :collapse:

   .. py:attribute:: context
      :type:  str | None
      :value: None



   .. py:attribute:: max_steps
      :type:  int | None
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: tools_preference
      :type:  list[str] | None
      :value: None



.. py:class:: ReWOOV3Output(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Output model for ReWOO V3 agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReWOOV3Output
      :collapse:

   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: evidence_collected
      :type:  int
      :value: None



   .. py:attribute:: evidence_summary
      :type:  str
      :value: None



   .. py:attribute:: execution_time
      :type:  float
      :value: None



   .. py:attribute:: final_answer
      :type:  str
      :value: None



   .. py:attribute:: limitations
      :type:  list[str]
      :value: None



   .. py:attribute:: plan_id
      :type:  str
      :value: None



   .. py:attribute:: planning_time
      :type:  float
      :value: None



   .. py:attribute:: query
      :type:  str
      :value: None



   .. py:attribute:: reasoning_process
      :type:  str
      :value: None



   .. py:attribute:: solution_id
      :type:  str
      :value: None



   .. py:attribute:: solving_time
      :type:  float
      :value: None



   .. py:attribute:: steps_planned
      :type:  int
      :value: None



   .. py:attribute:: tools_used
      :type:  list[str]
      :value: None



   .. py:attribute:: total_execution_time
      :type:  float
      :value: None



.. py:class:: ReWOOV3State

   Bases: :py:obj:`haive.core.schema.prebuilt.messages_state.MessagesState`


   State schema for ReWOO V3 with computed fields for prompt templates.

   ReWOO (Reasoning WithOut Observation) separates planning, execution, and synthesis:
   1. Planner creates complete plan upfront with evidence placeholders
   2. Worker executes all tool calls to collect evidence
   3. Solver synthesizes all evidence into final answer

   This state tracks the complete ReWOO workflow with dynamic computed fields
   for prompt template variable substitution.


   .. autolink-examples:: ReWOOV3State
      :collapse:

   .. py:method:: update_execution_result(execution_result: dict[str, Any]) -> None

      Update with worker agent result.


      .. autolink-examples:: update_execution_result
         :collapse:


   .. py:method:: update_planning_result(plan_result: dict[str, Any]) -> None

      Update with planner agent result.


      .. autolink-examples:: update_planning_result
         :collapse:


   .. py:method:: update_solution_result(solution_result: dict[str, Any]) -> None

      Update with solver agent result.


      .. autolink-examples:: update_solution_result
         :collapse:


   .. py:property:: available_tools
      :type: str


      Formatted list of available tools for planner prompt.

      .. autolink-examples:: available_tools
         :collapse:


   .. py:attribute:: current_phase
      :type:  str
      :value: None



   .. py:attribute:: evidence_collection
      :type:  dict[str, Any] | None
      :value: None



   .. py:property:: evidence_summary
      :type: str


      Formatted evidence for solver agent prompt.

      .. autolink-examples:: evidence_summary
         :collapse:


   .. py:attribute:: execution_completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: execution_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:property:: execution_status
      :type: str


      Current ReWOO workflow status for prompts.

      .. autolink-examples:: execution_status
         :collapse:


   .. py:attribute:: final_solution
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: original_query
      :type:  str
      :value: None



   .. py:property:: phase_progress
      :type: str


      Progress through ReWOO phases for prompts.

      .. autolink-examples:: phase_progress
         :collapse:


   .. py:property:: plan_summary
      :type: str


      Formatted plan for worker agent prompt.

      .. autolink-examples:: plan_summary
         :collapse:


   .. py:attribute:: planning_completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: reasoning_plan
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: solving_completed_at
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: started_at
      :type:  datetime.datetime
      :value: None



   .. py:attribute:: tools_available
      :type:  list[str]
      :value: None



   .. py:property:: workflow_context
      :type: str


      Complete workflow context for solver synthesis.

      .. autolink-examples:: workflow_context
         :collapse:


