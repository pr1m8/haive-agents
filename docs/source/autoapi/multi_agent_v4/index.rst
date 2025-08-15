multi_agent_v4
==============

.. py:module:: multi_agent_v4

.. autoapi-nested-parse::

   MultiAgent V4 - Clean implementation using enhanced base agent.

   This implementation follows the V4 pattern with:
   - Enhanced base agent integration
   - MultiAgentState usage
   - AgentNodeV3 execution
   - Simple list initialization
   - Incremental build-up approach

   Start small, test incrementally, build up features.


   .. autolink-examples:: multi_agent_v4
      :collapse:


Attributes
----------

.. autoapisummary::

   multi_agent_v4.logger


Classes
-------

.. autoapisummary::

   multi_agent_v4.MultiAgentV4


Module Contents
---------------

.. py:class:: MultiAgentV4

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   V4 Multi-agent coordinator using enhanced base agent.

   Simple, clean implementation that starts small and builds incrementally.
   Uses MultiAgentState and AgentNodeV3 for proper integration.

   .. rubric:: Example

   >>> from haive.agents.simple.agent import SimpleAgent
   >>> from haive.agents.react.agent import ReactAgent
   >>>
   >>> # Create agents
   >>> planner = ReactAgent(name="planner", engine=config, tools=[...])
   >>> writer = SimpleAgent(name="writer", engine=config)
   >>>
   >>> # Create multi-agent (simple list initialization)
   >>> workflow = MultiAgentV4(
   ...     name="content_workflow",
   ...     agents=[planner, writer],
   ...     execution_mode="sequential"
   ... )
   >>>
   >>> # Execute
   >>> result = await workflow.arun({"task": "Write an article"})


   .. autolink-examples:: MultiAgentV4
      :collapse:

   .. py:method:: _add_parallel_edges(graph: langgraph.graph.StateGraph)

      Add parallel edges: START -> all agents -> END.


      .. autolink-examples:: _add_parallel_edges
         :collapse:


   .. py:method:: _add_sequential_edges(graph: langgraph.graph.StateGraph)

      Add sequential edges: START -> agent1 -> agent2 -> ... -> END.


      .. autolink-examples:: _add_sequential_edges
         :collapse:


   .. py:method:: _build_execution_graph() -> langgraph.graph.graph.CompiledGraph

      Build LangGraph for agent execution.


      .. autolink-examples:: _build_execution_graph
         :collapse:


   .. py:method:: _convert_agents_to_dict(agents: list[haive.agents.base.agent.Agent]) -> dict[str, haive.agents.base.agent.Agent]

      Convert agent list to dictionary keyed by name.


      .. autolink-examples:: _convert_agents_to_dict
         :collapse:


   .. py:method:: _create_initial_state(input_data: Any) -> haive.core.schema.prebuilt.multi_agent_state.MultiAgentState

      Create initial MultiAgentState from input.


      .. autolink-examples:: _create_initial_state
         :collapse:


   .. py:method:: _extract_result(final_state: haive.core.schema.prebuilt.multi_agent_state.MultiAgentState) -> Any

      Extract final result from state.


      .. autolink-examples:: _extract_result
         :collapse:


   .. py:method:: add_agent(agent: haive.agents.base.agent.Agent) -> None

      Add an agent to the workflow.


      .. autolink-examples:: add_agent
         :collapse:


   .. py:method:: arun(input_data: Any, **kwargs) -> Any
      :async:


      Execute the multi-agent workflow.


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: build() -> langgraph.graph.graph.CompiledGraph

      Manually build the execution graph.


      .. autolink-examples:: build
         :collapse:


   .. py:method:: display_workflow_info() -> None

      Display workflow information.


      .. autolink-examples:: display_workflow_info
         :collapse:


   .. py:method:: get_agent(name: str) -> haive.agents.base.agent.Agent | None

      Get agent by name.


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: get_agent_names() -> list[str]

      Get list of agent names.


      .. autolink-examples:: get_agent_names
         :collapse:


   .. py:method:: setup_multi_agent()

      Set up multi-agent system after initialization.


      .. autolink-examples:: setup_multi_agent
         :collapse:


   .. py:attribute:: agent_dict
      :type:  dict[str, haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: agents
      :type:  list[haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: build_mode
      :type:  Literal['auto', 'manual', 'lazy']
      :value: None



   .. py:attribute:: execution_graph
      :type:  langgraph.graph.graph.CompiledGraph | None
      :value: None



   .. py:attribute:: execution_mode
      :type:  Literal['sequential', 'parallel']
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.core.schema.prebuilt.multi_agent_state.MultiAgentState]
      :value: None



.. py:data:: logger

