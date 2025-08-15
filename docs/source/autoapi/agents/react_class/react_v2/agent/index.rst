agents.react_class.react_v2.agent
=================================

.. py:module:: agents.react_class.react_v2.agent

.. autoapi-nested-parse::

   ReactAgent implementation that extends SimpleAgent with tool usage capabilities.


   .. autolink-examples:: agents.react_class.react_v2.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.react_class.react_v2.agent.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_v2.agent.ReactAgent


Module Contents
---------------

.. py:class:: ReactAgent(config: haive.agents.react_class.react_v2.config.ReactAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.react_class.react_v2.config.ReactAgentConfig`\ ]


   A React agent that enhances SimpleAgent with tool-using capabilities.

   This agent implements the ReAct (Reasoning + Acting) pattern which allows
   multi-step reasoning and tool usage for complex tasks.


   .. autolink-examples:: ReactAgent
      :collapse:

   .. py:method:: _convert_tools_list(tools_list)

      Convert a list of mixed tool formats to LangChain tools.


      .. autolink-examples:: _convert_tools_list
         :collapse:


   .. py:method:: _create_tool_nodes()

      Create ToolNodes from the prepared tools map.


      .. autolink-examples:: _create_tool_nodes
         :collapse:


   .. py:method:: _prepare_tools(tools_input)

      Convert various tool formats to LangChain tools.


      .. autolink-examples:: _prepare_tools
         :collapse:


   .. py:method:: _route_agent_output(state: Any) -> str | list[langgraph.types.Send]

      Route output from agent to appropriate next node(s).

      This function implements complex routing, supporting:
      1. Single tool execution (returns the node name)
      2. Parallel tool execution (returns list of Send objects)
      3. End of reasoning (returns "end")
      4. Structured output (returns "structured_output")


      .. autolink-examples:: _route_agent_output
         :collapse:


   .. py:method:: run(input_data, thread_id: str | None = None, **kwargs)

      Override run to handle tool-based workflows and proper state preparation.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the React agent workflow with tool support.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: tool_nodes


   .. py:attribute:: tools_map


.. py:data:: logger

