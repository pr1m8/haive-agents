agents.planning.llm_compiler.agent
==================================

.. py:module:: agents.planning.llm_compiler.agent

.. autoapi-nested-parse::

   LLM Compiler Agent Implementation.

   from typing import Any, Dict
   This implementation follows the LLM Compiler architecture from the paper by Kim et al.,
   focusing on parallelizable task execution through a DAG structure.


   .. autolink-examples:: agents.planning.llm_compiler.agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.llm_compiler.agent.LLMCompilerAgent


Functions
---------

.. autoapisummary::

   agents.planning.llm_compiler.agent.main


Module Contents
---------------

.. py:class:: LLMCompilerAgent(config: agents.planning.llm_compiler.config.LLMCompilerAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentArchitecture`


   LLM Compiler Agent implementation.

   This agent architecture has three main components:
   1. Planner: Creates a task DAG
   2. Task Executor: Executes tasks as their dependencies are satisfied
   3. Joiner: Processes results and decides whether to output an answer or replan

   Initialize the LLM Compiler agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LLMCompilerAgent
      :collapse:

   .. py:method:: _create_fallback_plan(query: str) -> agents.planning.llm_compiler.models.CompilerPlan

      Create a fallback plan when planning fails.

      :param query: The user's query

      :returns: A simple fallback plan


      .. autolink-examples:: _create_fallback_plan
         :collapse:


   .. py:method:: _execute_step(step: agents.planning.llm_compiler.models.CompilerStep, results: dict[int, Any], tool_map: dict[str, langchain_core.tools.BaseTool]) -> Any
      :staticmethod:


      Execute a single step.

      :param step: The step to execute
      :param results: Results from previous steps
      :param tool_map: Dictionary mapping tool names to tools

      :returns: Result of the step execution


      .. autolink-examples:: _execute_step
         :collapse:


   .. py:method:: _format_results_for_replanning(state: agents.planning.llm_compiler.state.CompilerState) -> str

      Format previous results for replanning.

      :param state: Current agent state

      :returns: Formatted results as a string


      .. autolink-examples:: _format_results_for_replanning
         :collapse:


   .. py:method:: _format_tool_descriptions() -> str

      Format tool descriptions for the planner prompt.

      :returns: Formatted tool descriptions


      .. autolink-examples:: _format_tool_descriptions
         :collapse:


   .. py:method:: _generate_fallback_response(state)

      Generates a fallback response when execution fails.

      :param state: The final state after execution.
      :type state: CompilerState | Dict

      :returns: The fallback response.
      :rtype: str


      .. autolink-examples:: _generate_fallback_response
         :collapse:


   .. py:method:: arun(query: str)
      :async:


      Run the agent asynchronously.

      :param query: The user's query

      :returns: Response from the agent


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: execute_tasks(state: agents.planning.llm_compiler.state.CompilerState) -> dict[str, Any]

      Execute tasks in parallel as their dependencies are satisfied.

      :param state: Current agent state

      :returns: Updated state with executed task results


      .. autolink-examples:: execute_tasks
         :collapse:


   .. py:method:: join(state: agents.planning.llm_compiler.state.CompilerState) -> dict[str, Any]

      Process the results and decide whether to provide a final answer or replan.

      :param state: Current agent state

      :returns: Decision to end or replan


      .. autolink-examples:: join
         :collapse:


   .. py:method:: plan(state: agents.planning.llm_compiler.state.CompilerState) -> dict[str, Any]

      Generate a plan based on the user's query.

      :param state: Current agent state

      :returns: Updated state with a new plan


      .. autolink-examples:: plan
         :collapse:


   .. py:method:: run(query: str)

      Run the agent on a query.

      :param query: The user's query

      :returns: Response from the agent


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> Any

      Set up the agent workflow as a state graph.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: should_execute_more(state: agents.planning.llm_compiler.state.CompilerState, config: dict[str, Any] | None = None) -> str

      Determine the next execution step.

      :param state: The current agent state.
      :type state: CompilerState
      :param config: Execution configuration (not used but required).
      :type config: Optional[Any]

      :returns: The next node to execute in the state graph.
      :rtype: str


      .. autolink-examples:: should_execute_more
         :collapse:


   .. py:method:: stream(query: str)

      Stream the agent's execution.

      :param query: The user's query

      :Yields: Execution steps


      .. autolink-examples:: stream
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: graph
      :value: None



   .. py:attribute:: joiner_llm


   .. py:attribute:: parser


   .. py:attribute:: planner_llm


   .. py:attribute:: replanner_llm


   .. py:attribute:: tool_map


   .. py:attribute:: tools


.. py:function:: main() -> None

