agents.planning.llm_compiler_v3.agent
=====================================

.. py:module:: agents.planning.llm_compiler_v3.agent

.. autoapi-nested-parse::

   LLM Compiler V3 Agent using Enhanced MultiAgent V3 Architecture.

   This implementation modernizes the LLM Compiler pattern by using Enhanced MultiAgent V3
   for simplified architecture, better maintainability, and consistent patterns.


   .. autolink-examples:: agents.planning.llm_compiler_v3.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler_v3.agent.LLMCompilerV3Agent


Module Contents
---------------

.. py:class:: LLMCompilerV3Agent(name: str = 'llm_compiler_v3', config: haive.agents.planning.llm_compiler_v3.config.LLMCompilerV3Config | None = None, tools: list | None = None, **kwargs)

   LLM Compiler V3 Agent using Enhanced MultiAgent V3.

   This agent implements the LLM Compiler pattern with three specialized sub-agents:
   1. Planner - Decomposes tasks into parallelizable DAG
   2. Task Fetcher - Manages task coordination and dependency resolution
   3. Parallel Executor - Executes individual tasks with tools
   4. Joiner - Synthesizes results into final answer

   Initialize LLM Compiler V3 Agent.

   :param name: Agent name
   :param config: Configuration for the compiler
   :param tools: List of tools available for task execution
   :param \*\*kwargs: Additional arguments for Enhanced MultiAgent V3


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LLMCompilerV3Agent
      :collapse:

   .. py:method:: _create_error_output(error_message: str, state: haive.agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema) -> haive.agents.planning.llm_compiler_v3.models.CompilerOutput

      Create error output when execution fails.


      .. autolink-examples:: _create_error_output
         :collapse:


   .. py:method:: _create_fallback_output(state: haive.agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema, error_message: str) -> haive.agents.planning.llm_compiler_v3.models.CompilerOutput

      Create fallback output when synthesis fails.


      .. autolink-examples:: _create_fallback_output
         :collapse:


   .. py:method:: _execute_parallel_tasks(state: haive.agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema, tasks: list[haive.agents.planning.llm_compiler_v3.models.CompilerTask]) -> None
      :async:


      Execute multiple tasks in parallel.


      .. autolink-examples:: _execute_parallel_tasks
         :collapse:


   .. py:method:: _execute_single_task(state: haive.agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema, task: haive.agents.planning.llm_compiler_v3.models.CompilerTask) -> haive.agents.planning.llm_compiler_v3.models.ParallelExecutionResult
      :async:


      Execute a single task with timing and error handling.


      .. autolink-examples:: _execute_single_task
         :collapse:


   .. py:method:: _execute_tool(tool, arguments: dict[str, Any]) -> Any
      :async:


      Execute a tool with given arguments.


      .. autolink-examples:: _execute_tool
         :collapse:


   .. py:method:: _execution_phase(state: haive.agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema) -> haive.agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema
      :async:


      Execute tasks with parallel coordination.


      .. autolink-examples:: _execution_phase
         :collapse:


   .. py:method:: _parse_plan_from_result(result: Any) -> haive.agents.planning.llm_compiler_v3.models.CompilerPlan

      Fallback parsing of plan from agent result.


      .. autolink-examples:: _parse_plan_from_result
         :collapse:


   .. py:method:: _planning_phase(state: haive.agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema, compiler_input: haive.agents.planning.llm_compiler_v3.models.CompilerInput) -> haive.agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema
      :async:


      Execute planning phase to create task DAG.


      .. autolink-examples:: _planning_phase
         :collapse:


   .. py:method:: _replan_phase(state: haive.agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema) -> haive.agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema
      :async:


      Execute replanning when execution encounters issues.


      .. autolink-examples:: _replan_phase
         :collapse:


   .. py:method:: _setup_agents()

      Setup specialized sub-agents for the LLM Compiler pattern.


      .. autolink-examples:: _setup_agents
         :collapse:


   .. py:method:: _synthesis_phase(state: haive.agents.planning.llm_compiler_v3.state.LLMCompilerStateSchema) -> haive.agents.planning.llm_compiler_v3.models.CompilerOutput
      :async:


      Synthesize final results using joiner agent.


      .. autolink-examples:: _synthesis_phase
         :collapse:


   .. py:method:: arun(query: str, context: dict[str, Any] | None = None, **kwargs) -> haive.agents.planning.llm_compiler_v3.models.CompilerOutput
      :async:


      Execute LLM Compiler pattern asynchronously.

      :param query: User query to process
      :param context: Additional context
      :param \*\*kwargs: Additional execution parameters

      :returns: CompilerOutput with final results and execution details


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: run(query: str, context: dict[str, Any] | None = None, **kwargs) -> haive.agents.planning.llm_compiler_v3.models.CompilerOutput

      Execute LLM Compiler pattern synchronously.


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: multi_agent


   .. py:attribute:: name
      :value: 'llm_compiler_v3'



   .. py:attribute:: tool_map


   .. py:attribute:: tools
      :value: []



