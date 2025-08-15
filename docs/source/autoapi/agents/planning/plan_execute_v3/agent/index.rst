agents.planning.plan_execute_v3.agent
=====================================

.. py:module:: agents.planning.plan_execute_v3.agent

.. autoapi-nested-parse::

   Plan-and-Execute V3 Agent - Enhanced MultiAgent V3 Implementation.

   This agent implements the Plan-and-Execute methodology using Enhanced MultiAgent V3,
   separating planning, execution, evaluation, and replanning into distinct sub-agents.

   Key Features:
   - SimpleAgent for planning with structured output (ExecutionPlan)
   - ReactAgent for step execution with tools
   - SimpleAgent for evaluation and decision-making (PlanEvaluation)
   - SimpleAgent for replanning when needed (RevisedPlan)
   - Enhanced MultiAgent V3 for coordination
   - Real component testing (no mocks)


   .. autolink-examples:: agents.planning.plan_execute_v3.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.plan_execute_v3.agent.PlanExecuteV3Agent


Module Contents
---------------

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



