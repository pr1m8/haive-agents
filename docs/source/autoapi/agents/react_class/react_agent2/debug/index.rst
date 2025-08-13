
:py:mod:`agents.react_class.react_agent2.debug`
===============================================

.. py:module:: agents.react_class.react_agent2.debug



Functions
---------

.. autoapisummary::

   agents.react_class.react_agent2.debug.create_debug_tool_node
   agents.react_class.react_agent2.debug.debug_print_state
   agents.react_class.react_agent2.debug.fix_tool_messages

.. py:function:: create_debug_tool_node(tools: list[Any])

   Create a thoroughly debugged tool node that prevents tool_call_id issues.


   .. autolink-examples:: create_debug_tool_node
      :collapse:

.. py:function:: debug_print_state(state: dict[str, Any], label: str = 'State') -> None

   Print state in a readable format for debugging.


   .. autolink-examples:: debug_print_state
      :collapse:

.. py:function:: fix_tool_messages(messages: list[Any]) -> list[Any]

   Fix tool messages by ensuring each tool message has a valid tool_call_id.

   :param messages: List of messages to fix

   :returns: Fixed list of messages


   .. autolink-examples:: fix_tool_messages
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.react_class.react_agent2.debug
   :collapse:
   
.. autolink-skip:: next
