agents.planning.rewoo_v3.agent
==============================

.. py:module:: agents.planning.rewoo_v3.agent

.. autoapi-nested-parse::

   ReWOO V3 Agent using Enhanced MultiAgent V3 coordination.

   This module implements the ReWOO (Reasoning WithOut Observation) methodology
   using our proven patterns from Plan-and-Execute V3 success.

   ReWOO Architecture:
   1. Planner: Creates complete reasoning plan with evidence placeholders
   2. Worker: Executes all tool calls to collect evidence
   3. Solver: Synthesizes all evidence into final answer

   Key advantages:
   - Token efficiency (5x improvement over iterative methods)
   - Parallel tool execution capability
   - Robust to partial failures
   - Fine-tuning friendly modular design


   .. autolink-examples:: agents.planning.rewoo_v3.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.rewoo_v3.agent.ReWOOV3Agent


Module Contents
---------------

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



