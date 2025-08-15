agents.react_class.react_v2.tool_handling
=========================================

.. py:module:: agents.react_class.react_v2.tool_handling


Attributes
----------

.. autoapisummary::

   agents.react_class.react_v2.tool_handling.logger


Classes
-------

.. autoapisummary::

   agents.react_class.react_v2.tool_handling.GeneralizedToolNode


Functions
---------

.. autoapisummary::

   agents.react_class.react_v2.tool_handling.create_human_assistance_tool
   agents.react_class.react_v2.tool_handling.human_input_node


Module Contents
---------------

.. py:class:: GeneralizedToolNode(tools: list[langchain_core.tools.BaseTool], parallel: bool = True)

   A generalized tool node that supports both standard tools and human interaction.

   This node processes tool calls from the LLM and either:
   1. Executes standard tools using LangGraph's ToolNode
   2. Flags the state for human input when the "request_human_assistance" tool is called

   Initialize the generalized tool node.

   :param tools: List of tools that can be executed
   :param parallel: Whether to run tools in parallel


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GeneralizedToolNode
      :collapse:

   .. py:method:: __call__(state: dict[str, Any]) -> dict[str, Any]

      Process tool calls and update state with results or flag for human input.

      :param state: Current agent state

      :returns: Updated state with tool results or human input flag


      .. autolink-examples:: __call__
         :collapse:


   .. py:attribute:: human_tool_names


   .. py:attribute:: parallel
      :value: True



   .. py:attribute:: tool_node


   .. py:attribute:: tools_by_name


.. py:function:: create_human_assistance_tool(name: str = 'request_human_assistance') -> langchain_core.tools.BaseTool

   Create a tool for requesting human assistance.

   :param name: Name for the tool

   :returns: A BaseTool that can be added to the agent's toolkit


   .. autolink-examples:: create_human_assistance_tool
      :collapse:

.. py:function:: human_input_node(state: dict[str, Any]) -> langgraph.types.Command

   Node that handles human input requests.

   This node generates a command to interrupt the graph execution
   and wait for human input. It's triggered when a tool requests human assistance.

   :param state: Current agent state

   :returns: Command to interrupt the graph and wait for human input


   .. autolink-examples:: human_input_node
      :collapse:

.. py:data:: logger

