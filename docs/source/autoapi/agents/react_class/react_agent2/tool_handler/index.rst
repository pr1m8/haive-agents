
:py:mod:`agents.react_class.react_agent2.tool_handler`
======================================================

.. py:module:: agents.react_class.react_agent2.tool_handler



Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.tool_handler.normalize_tool_message
   agents.react_class.react_agent2.tool_handler.process_messages

.. py:function:: normalize_tool_message(message: dict[str, Any]) -> dict[str, Any]

   Normalize a tool message to ensure it has the required attributes.

   :param message: The tool message dictionary

   :returns: Normalized tool message dictionary


   .. autolink-examples:: normalize_tool_message
      :collapse:

.. py:function:: process_messages(messages: list[dict[str, Any]]) -> list[dict[str, Any]]

   Process a list of messages to ensure all tool messages are properly formatted.

   :param messages: List of message dictionaries

   :returns: Processed message list


   .. autolink-examples:: process_messages
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent2.tool_handler
   :collapse:
   
.. autolink-skip:: next
