proper_list_multi_agent
=======================

.. py:module:: proper_list_multi_agent

.. autoapi-nested-parse::

   Proper list multi-agent that uses MultiAgentState and AgentNodeV3.

   from typing import Any
   This implementation properly leverages the existing infrastructure:
   - MultiAgentState for proper state management
   - AgentNodeV3 for agent execution with state projection
   - create_agent_node_v3 for creating agent nodes
   - Proper engine syncing and recompilation tracking


   .. autolink-examples:: proper_list_multi_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   proper_list_multi_agent.logger


Classes
-------

.. autoapisummary::

   proper_list_multi_agent.MetaListMultiAgent
   proper_list_multi_agent.ProperListMultiAgent


Functions
---------

.. autoapisummary::

   proper_list_multi_agent.meta_multi
   proper_list_multi_agent.sequential_multi


Module Contents
---------------

.. py:class:: MetaListMultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`, :py:obj:`haive.core.common.mixins.recompile_mixin.RecompileMixin`, :py:obj:`collections.abc.Sequence`\ [\ :py:obj:`haive.agents.base.agent.Agent`\ ]


   List multi-agent that uses MetaStateSchema for single agent embedding.

   This is useful when you want to embed a sequence of agents as a single
   unit within another agent's state using the MetaStateSchema pattern.

   .. rubric:: Example

   .. code-block:: python

       # Create a meta multi-agent
       meta = MetaListMultiAgent("research_pipeline")
       meta.append(PlannerAgent())
       meta.append(ResearchAgent())
       meta.append(WriterAgent())

       # This can be embedded in another agent's state
       parent_state = MetaStateSchema(agent=meta)


   .. autolink-examples:: MetaListMultiAgent
      :collapse:

   .. py:method:: __getitem__(index: int | slice) -> haive.agents.base.agent.Agent | list[haive.agents.base.agent.Agent]


   .. py:method:: __iter__() -> collections.abc.Iterator[haive.agents.base.agent.Agent]


   .. py:method:: __len__() -> int


   .. py:method:: _setup_schemas() -> None

      Setup using MetaStateSchema as the base.


      .. autolink-examples:: _setup_schemas
         :collapse:


   .. py:method:: _update_agent_index() -> None

      Update agent name to index mapping.


      .. autolink-examples:: _update_agent_index
         :collapse:


   .. py:method:: append(agent: haive.agents.base.agent.Agent) -> MetaListMultiAgent

      Add agent to the list.


      .. autolink-examples:: append
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph that executes agents sequentially.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup the meta multi-agent.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: _agent_index
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: agent_results
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: agents
      :type:  list[haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: current_index
      :type:  int
      :value: None



.. py:class:: ProperListMultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`, :py:obj:`haive.core.common.mixins.recompile_mixin.RecompileMixin`, :py:obj:`collections.abc.Sequence`\ [\ :py:obj:`haive.agents.base.agent.Agent`\ ]


   List-based multi-agent that properly uses MultiAgentState and AgentNodeV3.

   This implementation:
   - Uses MultiAgentState as the state schema
   - Uses AgentNodeV3 for proper agent execution
   - Handles state projection and hierarchical management
   - Supports recompilation tracking
   - Maintains the natural list interface

   .. rubric:: Example

   .. code-block:: python

       multi = ProperListMultiAgent("research_team")
       multi.append(PlannerAgent("planner"))
       multi.append(ResearchAgent("researcher"))
       multi.append(WriterAgent("writer"))

       # Agents are stored in MultiAgentState.agents
       # Each agent gets its own state in MultiAgentState.agent_states
       # Output tracked in MultiAgentState.agent_outputs

       result = multi.invoke({"messages": [HumanMessage("Research AI")]})


   .. autolink-examples:: ProperListMultiAgent
      :collapse:

   .. py:method:: __getitem__(index: int | slice) -> haive.agents.base.agent.Agent | list[haive.agents.base.agent.Agent]


   .. py:method:: __iter__() -> collections.abc.Iterator[haive.agents.base.agent.Agent]


   .. py:method:: __len__() -> int


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: _build_conditional_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Build graph with conditional routing.


      .. autolink-examples:: _build_conditional_graph
         :collapse:


   .. py:method:: _build_sequential_graph(graph: haive.core.graph.state_graph.base_graph2.BaseGraph) -> None

      Build sequential execution using AgentNodeV3.


      .. autolink-examples:: _build_sequential_graph
         :collapse:


   .. py:method:: _init_multi_agent_state(state: dict[str, Any]) -> dict[str, Any]

      Initialize MultiAgentState with our agents.


      .. autolink-examples:: _init_multi_agent_state
         :collapse:


   .. py:method:: _passthrough_node(state: dict[str, Any]) -> dict[str, Any]

      Passthrough for empty multi-agent.


      .. autolink-examples:: _passthrough_node
         :collapse:


   .. py:method:: _setup_schemas() -> None

      Setup using MultiAgentState as the base schema.


      .. autolink-examples:: _setup_schemas
         :collapse:


   .. py:method:: _update_agent_index() -> None

      Update agent name to index mapping.


      .. autolink-examples:: _update_agent_index
         :collapse:


   .. py:method:: append(agent: haive.agents.base.agent.Agent) -> ProperListMultiAgent

      Add agent to the list.


      .. autolink-examples:: append
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build graph using AgentNodeV3 for proper state handling.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_agent_by_name(name: str) -> haive.agents.base.agent.Agent | None

      Get agent by name.


      .. autolink-examples:: get_agent_by_name
         :collapse:


   .. py:method:: get_agent_names() -> list[str]

      Get ordered list of agent names.


      .. autolink-examples:: get_agent_names
         :collapse:


   .. py:method:: get_execution_summary() -> dict[str, Any]

      Get execution summary.


      .. autolink-examples:: get_execution_summary
         :collapse:


   .. py:method:: insert(index: int, agent: haive.agents.base.agent.Agent) -> ProperListMultiAgent

      Insert agent at position.


      .. autolink-examples:: insert
         :collapse:


   .. py:method:: model_post_init(__context) -> None

      Initialize after model creation.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:method:: pop(index: int = -1) -> haive.agents.base.agent.Agent

      Remove and return agent.


      .. autolink-examples:: pop
         :collapse:


   .. py:method:: remove(agent: haive.agents.base.agent.Agent | str) -> ProperListMultiAgent

      Remove agent.


      .. autolink-examples:: remove
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup the multi-agent system.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: then(agent: haive.agents.base.agent.Agent) -> ProperListMultiAgent

      Add next agent in sequence.


      .. autolink-examples:: then
         :collapse:


   .. py:method:: when(condition: collections.abc.Callable[[Any], str | bool], routes: dict[str | bool, Union[str, haive.agents.base.agent.Agent, langgraph.graph.END]]) -> ProperListMultiAgent

      Add conditional routing for the last agent.


      .. autolink-examples:: when
         :collapse:


   .. py:attribute:: _agent_index
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: agents
      :type:  list[haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: routing_rules
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: sequential
      :type:  bool
      :value: None



   .. py:attribute:: stop_on_error
      :type:  bool
      :value: None



   .. py:attribute:: use_prebuilt_base
      :type:  bool
      :value: None



.. py:function:: meta_multi(*agents: haive.agents.base.agent.Agent, name: str = 'meta_multi') -> MetaListMultiAgent

   Create a meta multi-agent.


   .. autolink-examples:: meta_multi
      :collapse:

.. py:function:: sequential_multi(*agents: haive.agents.base.agent.Agent, name: str = 'sequential_multi') -> ProperListMultiAgent

   Create a sequential multi-agent.


   .. autolink-examples:: sequential_multi
      :collapse:

.. py:data:: logger

