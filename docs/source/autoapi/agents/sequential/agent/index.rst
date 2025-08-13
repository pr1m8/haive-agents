
:py:mod:`agents.sequential.agent`
=================================

.. py:module:: agents.sequential.agent


Classes
-------

.. autoapisummary::

   agents.sequential.agent.SequentialAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialAgent {
        node [shape=record];
        "SequentialAgent" [label="SequentialAgent"];
        "haive.agents.base.agent.Agent" -> "SequentialAgent";
      }

.. autoclass:: agents.sequential.agent.SequentialAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.sequential.agent.build_graph
   agents.sequential.agent.set_state_schema
   agents.sequential.agent.validate_agents
   agents.sequential.agent.validate_non_empty_agents

.. py:function:: build_graph(agents: collections.abc.Sequence[haive.agents.base.agent.Agent]) -> haive.core.graph.state_graph.base_graph2.BaseGraph

   Build a sequential graph from a list of agents.


   .. autolink-examples:: build_graph
      :collapse:

.. py:function:: set_state_schema(agents: collections.abc.Sequence[haive.agents.base.agent.Agent]) -> type[pydantic.BaseModel] | None

   Set state schema for a list of agents.


   .. autolink-examples:: set_state_schema
      :collapse:

.. py:function:: validate_agents(agents: collections.abc.Sequence[haive.agents.base.agent.Agent]) -> bool

   Validate that all items are valid agents.


   .. autolink-examples:: validate_agents
      :collapse:

.. py:function:: validate_non_empty_agents(agents: collections.abc.Sequence[haive.agents.base.agent.Agent]) -> bool

   Validate that agents list is not empty.


   .. autolink-examples:: validate_non_empty_agents
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.sequential.agent
   :collapse:
   
.. autolink-skip:: next
