clean_multi_agent
=================

.. py:module:: clean_multi_agent

.. autoapi-nested-parse::

   Clean Multi-Agent Implementation using AgentNodeV3.

   from typing import Any, Dict
   This module provides a clean multi-agent system that:
   - Uses AgentNodeV3 for proper state projection
   - Emulates the engines dict pattern from base Agent
   - Supports private state passing between agents
   - Maintains type safety without schema flattening


   .. autolink-examples:: clean_multi_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   clean_multi_agent.logger


Classes
-------

.. autoapisummary::

   clean_multi_agent.ConditionalAgent
   clean_multi_agent.ContainerMultiAgentState
   clean_multi_agent.MinimalMultiAgentState
   clean_multi_agent.MultiAgent
   clean_multi_agent.SequentialAgent


Module Contents
---------------

.. py:class:: ConditionalAgent(agents: dict[str, haive.agents.base.agent.Agent], routing_function: Any, **kwargs)

   Bases: :py:obj:`MultiAgent`


   Conditional routing multi-agent.

   .. rubric:: Example

   agent = ConditionalAgent(
       agents={"analyzer": analyzer, "synthesizer": synthesizer},
       routing_function=my_router
   )

   Initialize with agents dict and routing function.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ConditionalAgent
      :collapse:

   .. py:attribute:: mode
      :type:  Literal['conditional']
      :value: None



.. py:class:: ContainerMultiAgentState

   Bases: :py:obj:`haive.core.schema.state_schema.StateSchema`


   Container pattern with isolated agent states.


   .. autolink-examples:: ContainerMultiAgentState
      :collapse:

   .. py:attribute:: agent_states
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: agents
      :type:  dict[str, haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: completed_agents
      :type:  list[str]
      :value: None



   .. py:attribute:: current_agent
      :type:  str | None
      :value: None



   .. py:attribute:: error
      :type:  str | None
      :value: None



   .. py:attribute:: final_result
      :type:  Any | None
      :value: None



   .. py:attribute:: shared_context
      :type:  dict[str, Any]
      :value: None



.. py:class:: MinimalMultiAgentState

   Bases: :py:obj:`typing_extensions.TypedDict`


   Minimal state for multi-agent coordination.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MinimalMultiAgentState
      :collapse:

   .. py:attribute:: completed_agents
      :type:  list[str]


   .. py:attribute:: current_agent
      :type:  str | None


   .. py:attribute:: error
      :type:  str | None


   .. py:attribute:: final_result
      :type:  Any | None


.. py:class:: MultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Multi-agent coordinator using AgentNodeV3 for proper state management.

   This class provides a clean implementation that:
   - Emulates the engines dict pattern from base Agent
   - Uses AgentNodeV3 for each agent with state projection
   - Supports both list and dict agent specifications
   - Maintains type safety without schema flattening

   .. rubric:: Example

   Sequential execution::

       multi = MultiAgent(
           agents=[react_agent, simple_agent],
           mode="sequential"
       )

   With dict specification::

       multi = MultiAgent(
           agents={
               "reasoner": react_agent,
               "formatter": simple_agent
           }
       )


   .. autolink-examples:: MultiAgent
      :collapse:

   .. py:method:: __repr__() -> str


   .. py:method:: _build_conditional_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build conditional routing edges.


      .. autolink-examples:: _build_conditional_edges
         :collapse:


   .. py:method:: _build_parallel_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build parallel execution edges.


      .. autolink-examples:: _build_parallel_edges
         :collapse:


   .. py:method:: _build_sequential_edges(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build sequential execution edges.


      .. autolink-examples:: _build_sequential_edges
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph using AgentNodeV3 for each agent.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: normalize_agents() -> MultiAgent

      Normalize agents into registry dict, similar to engines normalization.


      .. autolink-examples:: normalize_agents
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup multi-agent specific configuration.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: _agent_order
      :type:  list[str]
      :value: None



   .. py:attribute:: _agent_registry
      :type:  dict[str, haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: agents
      :type:  list[haive.agents.base.agent.Agent] | dict[str, haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: mode
      :type:  Literal['sequential', 'conditional', 'parallel']
      :value: None



   .. py:attribute:: routing_function
      :type:  Any | None
      :value: None



   .. py:attribute:: shared_fields
      :type:  list[str]
      :value: None



   .. py:attribute:: state_strategy
      :type:  Literal['minimal', 'container', 'custom']
      :value: None



   .. py:attribute:: state_transfer_map
      :type:  dict[str, dict[str, str]]
      :value: None



.. py:class:: SequentialAgent(agents: list[haive.agents.base.agent.Agent], **kwargs)

   Bases: :py:obj:`MultiAgent`


   Sequential multi-agent execution.

   .. rubric:: Example

   agent = SequentialAgent([react_agent, simple_agent])

   Initialize with list of agents for sequential execution.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SequentialAgent
      :collapse:

   .. py:attribute:: mode
      :type:  Literal['sequential']
      :value: None



.. py:data:: logger

