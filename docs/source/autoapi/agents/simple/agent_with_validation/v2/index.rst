
:py:mod:`agents.simple.agent_with_validation.v2`
================================================

.. py:module:: agents.simple.agent_with_validation.v2


Classes
-------

.. autoapisummary::

   agents.simple.agent_with_validation.v2.SimpleAgentWithValidation


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

.. autoclass:: agents.simple.agent_with_validation.v2.SimpleAgentWithValidation
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.simple.agent_with_validation.v2.has_tool_calls
   agents.simple.agent_with_validation.v2.upgrade_simple_agent_with_validation

.. py:function:: has_tool_calls(state: haive.core.graph.node.state_updating_validation_node.Dict[str, Any]) -> bool

   Check if the last AI message has tool calls.


   .. autolink-examples:: has_tool_calls
      :collapse:

.. py:function:: upgrade_simple_agent_with_validation(simple_agent: SimpleAgent) -> SimpleAgentWithValidation

   Upgrade a SimpleAgent to use StateUpdatingValidationNode.


   .. autolink-examples:: upgrade_simple_agent_with_validation
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.simple.agent_with_validation.v2
   :collapse:
   
.. autolink-skip:: next
