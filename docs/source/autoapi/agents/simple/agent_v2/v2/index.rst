
:py:mod:`agents.simple.agent_v2.v2`
===================================

.. py:module:: agents.simple.agent_v2.v2

SimpleAgent V2 - Uses V2 validation node + router system.

This version uses the V2 validation system that can properly:
1. Add ToolMessages to state for Pydantic model validation
2. Use separate validation node + router for proper state management
3. Handle both regular tools and Pydantic models correctly

Key improvements over V1:
- Uses ValidationNodeV2 for state updates
- Uses validation_router_v2 for routing decisions
- Proper ToolMessage creation for Pydantic models
- Better error handling and routing


.. autolink-examples:: agents.simple.agent_v2.v2
   :collapse:

Classes
-------

.. autoapisummary::

   agents.simple.agent_v2.v2.SimpleAgentV2


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAgentV2:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAgentV2 {
        node [shape=record];
        "SimpleAgentV2" [label="SimpleAgentV2"];
        "haive.agents.base.agent.Agent" -> "SimpleAgentV2";
      }

.. autoclass:: agents.simple.agent_v2.v2.SimpleAgentV2
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.simple.agent_v2.v2.has_tool_calls_v2

.. py:function:: has_tool_calls_v2(state: dict[str, Any]) -> bool

   Check if the last AI message has tool calls - V2 version.


   .. autolink-examples:: has_tool_calls_v2
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.simple.agent_v2.v2
   :collapse:
   
.. autolink-skip:: next
