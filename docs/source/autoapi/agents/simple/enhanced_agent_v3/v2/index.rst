
:py:mod:`agents.simple.enhanced_agent_v3.v2`
============================================

.. py:module:: agents.simple.enhanced_agent_v3.v2

Enhanced SimpleAgent V3 - Full feature implementation using enhanced base Agent.

This version leverages all advanced features from the enhanced base Agent class:
- Dynamic schema generation and composition
- Advanced engine management and routing
- Rich execution capabilities with debugging
- Sophisticated state management
- Comprehensive persistence and serialization


.. autolink-examples:: agents.simple.enhanced_agent_v3.v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.enhanced_agent_v3.v2.EnhancedSimpleAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EnhancedSimpleAgent:

   .. graphviz::
      :align: center

      digraph inheritance_EnhancedSimpleAgent {
        node [shape=record];
        "EnhancedSimpleAgent" [label="EnhancedSimpleAgent"];
        "haive.agents.base.agent.Agent" -> "EnhancedSimpleAgent";
      }

.. autoclass:: agents.simple.enhanced_agent_v3.v2.EnhancedSimpleAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.simple.enhanced_agent_v3.v2.has_tool_calls
   agents.simple.enhanced_agent_v3.v2.should_continue

.. py:function:: has_tool_calls(state: dict[str, Any]) -> Literal['true', 'false']

   Check if the last message has tool calls.


   .. autolink-examples:: has_tool_calls
      :collapse:

.. py:function:: should_continue(state: dict[str, Any]) -> bool

   Enhanced routing logic for tool calls and structured output.


   .. autolink-examples:: should_continue
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.simple.enhanced_agent_v3.v2
   :collapse:
   
.. autolink-skip:: next
