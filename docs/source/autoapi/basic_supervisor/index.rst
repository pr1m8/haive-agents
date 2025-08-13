
:py:mod:`basic_supervisor`
==========================

.. py:module:: basic_supervisor

Haive Supervisor Agent - ReactAgent with Dynamic Routing and Agent Registry.

ReactAgent-based supervisor with:
1. Agent registry with add_agent tool
2. Dynamic routing tool that creates base model with agents in state
3. Prompt template showing available agents
4. Generic agent execution node for running selected agents


.. autolink-examples:: basic_supervisor
   :collapse:

Classes
-------

.. autoapisummary::

   basic_supervisor.SupervisorAgent
   basic_supervisor.SupervisorState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorAgent {
        node [shape=record];
        "SupervisorAgent" [label="SupervisorAgent"];
        "haive.agents.react.agent.ReactAgent" -> "SupervisorAgent";
      }

.. autoclass:: basic_supervisor.SupervisorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorState:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorState {
        node [shape=record];
        "SupervisorState" [label="SupervisorState"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "SupervisorState";
      }

.. autoclass:: basic_supervisor.SupervisorState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: basic_supervisor
   :collapse:
   
.. autolink-skip:: next
