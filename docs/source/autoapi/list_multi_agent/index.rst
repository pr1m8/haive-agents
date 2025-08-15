list_multi_agent
================

.. py:module:: list_multi_agent

.. autoapi-nested-parse::

   List-based multi-agent implementation.

   from typing import Any
   A clean, simple multi-agent that acts like a Python list of agents.
   Focus on composition and orchestration, not complex state management.


   .. autolink-examples:: list_multi_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   list_multi_agent.logger


Classes
-------

.. autoapisummary::

   list_multi_agent.ListMultiAgent


Functions
---------

.. autoapisummary::

   list_multi_agent.pipeline
   list_multi_agent.sequential


Module Contents
---------------

.. py:class:: ListMultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`, :py:obj:`haive.core.common.mixins.recompile_mixin.RecompileMixin`, :py:obj:`collections.abc.Sequence`\ [\ :py:obj:`haive.agents.base.agent.Agent`\ ]


   Multi-agent system that works like a Python list.

   Simple, clean interface for composing agents:
   - Append, insert, remove agents like a list
   - Agents execute in sequence by default
   - Each agent manages its own tools/state
   - Message passing between agents

   .. rubric:: Example

   .. code-block:: python

       multi = ListMultiAgent("my_system")
       multi.append(PlannerAgent())
       multi.append(ResearchAgent())
       multi.append(WriterAgent())

       result = multi.invoke({"messages": [HumanMessage("Write about AI")]})


   .. autolink-examples:: ListMultiAgent
      :collapse:

   .. py:method:: __getitem__(index: int | slice) -> haive.agents.base.agent.Agent | list[haive.agents.base.agent.Agent]


   .. py:method:: __iter__() -> collections.abc.Iterator[haive.agents.base.agent.Agent]


   .. py:method:: __len__() -> int


   .. py:method:: __repr__() -> str

      Detailed representation.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: __rshift__(agent: haive.agents.base.agent.Agent) -> ListMultiAgent

      Support >> operator for chaining.


      .. autolink-examples:: __rshift__
         :collapse:


   .. py:method:: __str__() -> str

      String representation.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: _update_index() -> None

      Update agent name to index mapping.


      .. autolink-examples:: _update_index
         :collapse:


   .. py:method:: append(agent: haive.agents.base.agent.Agent) -> ListMultiAgent

      Add agent to end of list.


      .. autolink-examples:: append
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build simple sequential graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: clear() -> ListMultiAgent

      Remove all agents.


      .. autolink-examples:: clear
         :collapse:


   .. py:method:: get_agent_by_name(name: str) -> haive.agents.base.agent.Agent | None

      Get agent by name.


      .. autolink-examples:: get_agent_by_name
         :collapse:


   .. py:method:: get_agent_names() -> list[str]

      Get list of agent names in order.


      .. autolink-examples:: get_agent_names
         :collapse:


   .. py:method:: insert(index: int, agent: haive.agents.base.agent.Agent) -> ListMultiAgent

      Insert agent at specific position.


      .. autolink-examples:: insert
         :collapse:


   .. py:method:: pop(index: int = -1) -> haive.agents.base.agent.Agent

      Remove and return agent at index.


      .. autolink-examples:: pop
         :collapse:


   .. py:method:: remove(agent: haive.agents.base.agent.Agent | str) -> ListMultiAgent

      Remove agent by instance or name.


      .. autolink-examples:: remove
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup the multi-agent system.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: then(agent: haive.agents.base.agent.Agent) -> ListMultiAgent

      Add next agent in chain (alias for append).


      .. autolink-examples:: then
         :collapse:


   .. py:attribute:: _agent_index
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: agents
      :type:  list[haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: stop_on_error
      :type:  bool
      :value: None



.. py:function:: pipeline(*agents: haive.agents.base.agent.Agent, name: str = 'pipeline') -> ListMultiAgent

   Create a pipeline of agents (alias for sequential).


   .. autolink-examples:: pipeline
      :collapse:

.. py:function:: sequential(*agents: haive.agents.base.agent.Agent, name: str = 'sequential_multi') -> ListMultiAgent

   Create a sequential multi-agent from agents.


   .. autolink-examples:: sequential
      :collapse:

.. py:data:: logger

