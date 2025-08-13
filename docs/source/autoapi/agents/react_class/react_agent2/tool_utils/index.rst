
:py:mod:`agents.react_class.react_agent2.tool_utils`
====================================================

.. py:module:: agents.react_class.react_agent2.tool_utils



Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.tool_utils.create_custom_tool_node
   agents.react_class.react_agent2.tool_utils.fix_tool_messages

.. py:function:: create_custom_tool_node(tools: list[langchain_core.tools.BaseTool]) -> collections.abc.Callable

   Create a custom tool node function that properly handles AIMessage tool calls.

   This function specifically addresses edge cases in tool_call ID handling between
   different message formats.

   :param tools: List of tools to use

   :returns: A function that can be used as a node in the graph


   .. autolink-examples:: create_custom_tool_node
      :collapse:

.. py:function:: fix_tool_messages(messages: list[Any]) -> list[Any]

   Fix tool messages by ensuring they have proper tool_call_ids.

   This function ensures all ToolMessages have a valid tool_call_id
   by matching them with their corresponding AIMessage tool calls.

   :param messages: List of messages to fix

   :returns: Fixed list of messages


   .. autolink-examples:: fix_tool_messages
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent2.tool_utils
   :collapse:
   
.. autolink-skip:: next
