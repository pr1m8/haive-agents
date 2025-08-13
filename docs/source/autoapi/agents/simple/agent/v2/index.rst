
:py:mod:`agents.simple.agent.v2`
================================

.. py:module:: agents.simple.agent.v2

Agent core module.

This module provides agent functionality for the Haive framework.

Classes:
    SimpleAgent: SimpleAgent implementation.
    Story: Story implementation.

Functions:
    has_tool_calls: Has Tool Calls functionality.
    check_if_should_use_tool: Check If Should Use Tool functionality.
    placeholder_node: Placeholder Node functionality.


.. autolink-examples:: agents.simple.agent.v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.agent.v2.SimpleAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAgent {
        node [shape=record];
        "SimpleAgent" [label="SimpleAgent"];
        "haive.agents.base.Agent" -> "SimpleAgent";
      }

.. autoclass:: agents.simple.agent.v2.SimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.simple.agent.v2.check_if_should_use_tool
   agents.simple.agent.v2.has_tool_calls
   agents.simple.agent.v2.placeholder_node

.. py:function:: check_if_should_use_tool(state: dict[str, Any]) -> bool

   Check if the last message has tool calls.


   .. autolink-examples:: check_if_should_use_tool
      :collapse:

.. py:function:: has_tool_calls(state: dict[str, Any]) -> Literal['true', 'false']

   Check if the last message has tool calls.


   .. autolink-examples:: has_tool_calls
      :collapse:

.. py:function:: placeholder_node(state: dict[str, Any])

   Placeholder node that does nothing.


   .. autolink-examples:: placeholder_node
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.simple.agent.v2
   :collapse:
   
.. autolink-skip:: next
