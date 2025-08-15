agents.react_class.react.agent
==============================

.. py:module:: agents.react_class.react.agent


Attributes
----------

.. autoapisummary::

   agents.react_class.react.agent.a
   agents.react_class.react.agent.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react.agent.ReactAgent


Module Contents
---------------

.. py:class:: ReactAgent(config: haive.agents.react_class.react.config.ReactAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.react_class.react.config.ReactAgentConfig`\ ]


   React Agent implementation that extends SimpleAgent.

   Enables multi-step reasoning and tool usage by routing between
   an LLM and tool execution nodes.

   Initialize the React Agent with its configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReactAgent
      :collapse:

   .. py:method:: _add_structured_output_node(gb: haive.core.graph.dynamic_graph_builder.DynamicGraph) -> None

      Add a node for generating structured output.


      .. autolink-examples:: _add_structured_output_node
         :collapse:


   .. py:method:: _add_system_message_node(gb: haive.core.graph.dynamic_graph_builder.DynamicGraph) -> None

      Add a node for adding a system message to the state.


      .. autolink-examples:: _add_system_message_node
         :collapse:


   .. py:method:: _setup_llm_node(gb: haive.core.graph.dynamic_graph_builder.DynamicGraph) -> None

      Set up the LLM node with tool binding.


      .. autolink-examples:: _setup_llm_node
         :collapse:


   .. py:method:: _setup_tools_v1(gb: haive.core.graph.dynamic_graph_builder.DynamicGraph) -> None

      Set up tools for v1 architecture (all tool calls in one node).


      .. autolink-examples:: _setup_tools_v1
         :collapse:


   .. py:method:: _setup_tools_v2(gb: haive.core.graph.dynamic_graph_builder.DynamicGraph) -> None

      Set up tools for v2 architecture (each tool call in separate node).


      .. autolink-examples:: _setup_tools_v2
         :collapse:


   .. py:method:: filter_tools_for_query(query: str) -> list[langchain_core.tools.BaseTool]

      Filter tools based on the user query.


      .. autolink-examples:: filter_tools_for_query
         :collapse:


   .. py:method:: run_with_filtered_tools(input_data: str | dict[str, Any], filter_tools: bool = True, **kwargs) -> dict[str, Any]

      Run agent with dynamically filtered tools based on the query.

      :param input_data: Input query or state
      :param filter_tools: Whether to filter tools based on query
      :param \*\*kwargs: Additional parameters for running

      :returns: Result from agent execution


      .. autolink-examples:: run_with_filtered_tools
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the React Agent workflow graph.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: config


   .. py:attribute:: tools


   .. py:attribute:: version


.. py:data:: a

.. py:data:: logger

