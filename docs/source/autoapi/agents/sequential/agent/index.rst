agents.sequential.agent
=======================

.. py:module:: agents.sequential.agent


Classes
-------

.. autoapisummary::

   agents.sequential.agent.SequentialAgent


Functions
---------

.. autoapisummary::

   agents.sequential.agent.build_graph
   agents.sequential.agent.set_state_schema
   agents.sequential.agent.validate_agents
   agents.sequential.agent.validate_non_empty_agents


Module Contents
---------------

.. py:class:: SequentialAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Sequential agent that executes multiple agents in sequence.


   .. autolink-examples:: SequentialAgent
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the sequential graph connecting agents in order.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: set_state_schema() -> SequentialAgent


   .. py:method:: validate_agents(values) -> Any
      :classmethod:


      Validate that agents are Agent instances or convertible.


      .. autolink-examples:: validate_agents
         :collapse:


   .. py:method:: validate_non_empty_agents() -> SequentialAgent

      Ensure we have at least one agent.


      .. autolink-examples:: validate_non_empty_agents
         :collapse:


   .. py:attribute:: agents
      :type:  collections.abc.Sequence[Agent | Any]
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: smart_compose
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel] | None
      :value: None



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

