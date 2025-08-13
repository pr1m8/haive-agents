
:py:mod:`agents.simple.agent_with_validation`
=============================================

.. py:module:: agents.simple.agent_with_validation


Classes
-------

.. autoapisummary::

   agents.simple.agent_with_validation.SimpleAgentWithValidation


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleAgentWithValidation:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleAgentWithValidation {
        node [shape=record];
        "SimpleAgentWithValidation" [label="SimpleAgentWithValidation"];
        "haive.agents.base.agent.Agent" -> "SimpleAgentWithValidation";
      }

.. autoclass:: agents.simple.agent_with_validation.SimpleAgentWithValidation
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.simple.agent_with_validation.has_tool_calls
   agents.simple.agent_with_validation.upgrade_simple_agent_with_validation

.. py:function:: has_tool_calls(state: haive.core.graph.node.state_updating_validation_node.Dict[str, Any]) -> bool

   Check if the last AI message has tool calls.


   .. autolink-examples:: has_tool_calls
      :collapse:

.. py:function:: upgrade_simple_agent_with_validation(simple_agent: SimpleAgent) -> SimpleAgentWithValidation

   Upgrade a SimpleAgent to use StateUpdatingValidationNode.


   .. autolink-examples:: upgrade_simple_agent_with_validation
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.simple.agent_with_validation
   :collapse:
   
.. autolink-skip:: next
