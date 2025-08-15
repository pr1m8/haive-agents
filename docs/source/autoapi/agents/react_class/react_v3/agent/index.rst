agents.react_class.react_v3.agent
=================================

.. py:module:: agents.react_class.react_v3.agent

.. autoapi-nested-parse::

   ReactAgent implementation with tool usage and ReAct pattern.

   from typing import Any, Dict
   This module implements a tool-using agent that follows the ReAct pattern
   (Reasoning, Acting, and Observing) for solving tasks.


   .. autolink-examples:: agents.react_class.react_v3.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.react_class.react_v3.agent.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_v3.agent.ReactAgent


Module Contents
---------------

.. py:class:: ReactAgent

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.react_class.react_v3.config.ReactAgentConfig`\ ]


   A tool-using agent implementing the ReAct pattern.

   Features:
   - Integration with LangChain tools
   - Automatic schema composition from tools and engine
   - Reasoning → Tool Use → Observation cycle
   - Retry policies for resilience
   - Configurable termination conditions


   .. autolink-examples:: ReactAgent
      :collapse:

   .. py:method:: _create_tool_node()

      Create a function that handles tool execution.

      :returns: Function that executes the appropriate tool based on state


      .. autolink-examples:: _create_tool_node
         :collapse:


   .. py:method:: _prepare_input(input_data: Any) -> dict[str, Any]

      Prepare input for the agent.

      :param input_data: Raw input in various formats

      :returns: Properly formatted input dictionary


      .. autolink-examples:: _prepare_input
         :collapse:


   .. py:method:: _should_use_tool(state) -> bool

      Determine if we should use a tool based on the last message.

      :param state: Current state with messages

      :returns: True if we should use a tool, False otherwise


      .. autolink-examples:: _should_use_tool
         :collapse:


   .. py:method:: from_langgraph(react_state_graph: langgraph.graph.StateGraph, **kwargs) -> ReactAgent
      :classmethod:


      Create a ReactAgent from an existing LangGraph StateGraph.

      This allows using LangGraph's `create_react_agent` directly and then
      wrapping it with our ReactAgent class.

      :param react_state_graph: Existing React agent StateGraph
      :param \*\*kwargs: Additional configuration parameters

      :returns: ReactAgent instance wrapping the provided StateGraph


      .. autolink-examples:: from_langgraph
         :collapse:


   .. py:method:: from_tools(tools: list[Any], llm: haive.core.engine.aug_llm.AugLLMConfig | None = None, system_prompt: str | None = None, **kwargs) -> ReactAgent
      :classmethod:


      Create a ReactAgent from a list of tools.

      :param tools: List of tools to use
      :param llm: Optional LLM configuration (auto-created if not provided)
      :param system_prompt: Optional system prompt
      :param \*\*kwargs: Additional configuration parameters

      :returns: Configured ReactAgent instance


      .. autolink-examples:: from_tools
         :collapse:


   .. py:method:: run(input_data: Any) -> Any

      Run the agent on the provided input.

      :param input_data: Input in various formats

      :returns: Agent result


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the ReAct workflow with reasoning and tool execution nodes.

      This creates a graph with:
      1. A reasoning node that decides what to do
      2. A tool execution node that carries out actions
      3. Conditional branching based on message types


      .. autolink-examples:: setup_workflow
         :collapse:


.. py:data:: logger

