
:py:mod:`agent_original`
========================

.. py:module:: agent_original


Classes
-------

.. autoapisummary::

   agent_original.SimpleAgent
   agent_original.SimpleAgentConfig


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

.. autoclass:: agent_original.SimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAgentConfig {
        node [shape=record];
        "SimpleAgentConfig" [label="SimpleAgentConfig"];
        "haive.core.engine.agent.AgentConfig" -> "SimpleAgentConfig";
      }

.. autoclass:: agent_original.SimpleAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agent_original.check_if_should_use_tool
   agent_original.has_tool_calls
   agent_original.placeholder_node

.. py:function:: check_if_should_use_tool(state: dict[str, Any]) -> bool

   Check if the last message has tool calls.


   .. autolink-examples:: check_if_should_use_tool
      :collapse:

.. py:function:: has_tool_calls(state: dict[str, Any]) -> Literal['true', 'false']

   Check if the last message has tool calls.


   .. autolink-examples:: has_tool_calls
      :collapse:

.. py:function:: placeholder_node(_state: dict[str, Any])

   Placeholder node that does nothing.


   .. autolink-examples:: placeholder_node
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agent_original
   :collapse:
   
.. autolink-skip:: next
