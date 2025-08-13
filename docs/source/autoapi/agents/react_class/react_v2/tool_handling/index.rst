
:py:mod:`agents.react_class.react_v2.tool_handling`
===================================================

.. py:module:: agents.react_class.react_v2.tool_handling


Classes
-------

.. autoapisummary::

   agents.react_class.react_v2.tool_handling.GeneralizedToolNode


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GeneralizedToolNode:

   .. graphviz::
      :align: center

      digraph inheritance_GeneralizedToolNode {
        node [shape=record];
        "GeneralizedToolNode" [label="GeneralizedToolNode"];
      }

.. autoclass:: agents.react_class.react_v2.tool_handling.GeneralizedToolNode
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.react_class.react_v2.tool_handling.create_human_assistance_tool
   agents.react_class.react_v2.tool_handling.human_input_node

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



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_v2.tool_handling
   :collapse:
   
.. autolink-skip:: next
