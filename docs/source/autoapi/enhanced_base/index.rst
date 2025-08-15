enhanced_base
=============

.. py:module:: enhanced_base

.. autoapi-nested-parse::

   Enhanced Multi-Agent Base for flexible agent orchestration.

   from typing import Any, Dict
   This module provides an improved multi-agent base that leverages the advanced
   conditional edges functionality from base_graph2.py while keeping the API simple
   and similar to how it works in simple agents.

   The MultiAgentBase class enables sophisticated agent orchestration patterns including:

   - **Sequential Execution**: Simple chain of agents in order
   - **Conditional Branching**: Dynamic routing based on state conditions
   - **Plan-Execute-Replan**: Complex workflows with feedback loops
   - **Parallel Schema Composition**: Isolated namespaces for agent fields

   The system uses Pydantic fields for configuration and supports both simple
   edge definitions and complex conditional routing with proper error handling
   and state management.

   .. rubric:: Example

   Sequential multi-agent system::

       agents = [planner, executor, validator]
       multi_agent = MultiAgentBase(
           agents=agents,
           name="sequential_pipeline"
       )

   Conditional branching system::

       def route_condition(state) -> str:
           return "success" if state.validation_passed else "retry"

       multi_agent = MultiAgentBase(
           agents=[processor, validator, retrier],
           branches=[
               (validator, route_condition, {
                   "success": "END",
                   "retry": retrier
               })
           ]
       )

   .. seealso::

      :class:`haive.agents.planning.plan_and_execute.PlanAndExecuteAgent`: Complete Plan and Execute implementation
      :class:`haive.core.graph.state_graph.base_graph2.BaseGraph`: Underlying graph implementation


   .. autolink-examples:: enhanced_base
      :collapse:


Attributes
----------

.. autoapisummary::

   enhanced_base.logger


Classes
-------

.. autoapisummary::

   enhanced_base.AgentList
   enhanced_base.MultiAgentBase


Functions
---------

.. autoapisummary::

   enhanced_base.create_branching_multi_agent
   enhanced_base.create_plan_execute_multi_agent
   enhanced_base.create_sequential_multi_agent


Module Contents
---------------

.. py:class:: AgentList

   Bases: :py:obj:`list`


   List of agents with dict-like access by name.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentList
      :collapse:

   .. py:method:: __contains__(key)

      Check if agent exists by name (str) or object (Agent).


      .. autolink-examples:: __contains__
         :collapse:


   .. py:method:: __getitem__(key)

      Get agent by index (int) or name (str).


      .. autolink-examples:: __getitem__
         :collapse:


   .. py:method:: get(key: str, default=None)

      Get agent by name with optional default.


      .. autolink-examples:: get
         :collapse:


.. py:class:: MultiAgentBase

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Multi-agent base with simple API for advanced orchestration.

   This class provides a flexible foundation for building complex multi-agent systems
   with conditional routing, parallel schema composition, and sophisticated workflow
   management. It extends the base Agent class while orchestrating multiple sub-agents.

   The system supports various orchestration patterns:

   - **Sequential**: Agents execute in order (default behavior)
   - **Conditional**: Dynamic routing based on state conditions
   - **Parallel Schema**: Isolated field namespaces for complex state management
   - **Custom Workflows**: User-defined workflow nodes for state processing

   .. attribute:: agents

      List of agents to orchestrate

      :type: List[Agent]

   .. attribute:: branches

      Conditional routing branches

      :type: Optional[List[tuple]]

   .. attribute:: state_schema_override

      Override for state schema

      :type: Optional[Type[StateSchema]]

   .. attribute:: schema_build_mode

      Schema composition mode (SEQUENCE/PARALLEL)

      :type: BuildMode

   .. attribute:: schema_separation

      Field separation strategy for schemas

      :type: str

   .. attribute:: include_meta

      Include meta state for coordination

      :type: bool

   .. attribute:: entry_points

      Entry points for execution

      :type: Optional[List[Union[str, Agent]]]

   .. attribute:: finish_points

      Finish points for execution

      :type: Optional[List[Union[str, Agent]]]

   .. attribute:: workflow_nodes

      Custom workflow nodes

      :type: Optional[Dict[str, Callable]]

   .. attribute:: create_missing_nodes

      Auto-create missing destination nodes

      :type: bool

   .. rubric:: Example

   Sequential execution (default)::

       multi_agent = MultiAgentBase(
           agents=[agent1, agent2, agent3],
           name="sequential_pipeline"
       )

   Conditional branching::

       def route_condition(state) -> str:
           return "success" if state.is_valid else "retry"

       multi_agent = MultiAgentBase(
           agents=[processor, validator, retrier],
           branches=[
               (validator, route_condition, {
                   "success": "END",
                   "retry": retrier
               })
           ]
       )

   Parallel schema composition::

       multi_agent = MultiAgentBase(
           agents=[planner, executor, replanner],
           schema_build_mode=BuildMode.PARALLEL,
           branches=[
               (executor, route_after_execution, {
                   "continue": executor,
                   "replan": replanner
               })
           ]
       )

   .. note::

      The class automatically handles schema composition, node creation, and edge
      routing based on the provided configuration. Custom workflow nodes can be
      added for complex state processing between agent executions.


   .. autolink-examples:: MultiAgentBase
      :collapse:

   .. py:method:: _auto_detect_agents() -> AgentList

      Auto-detect agents from individual agent fields.


      .. autolink-examples:: _auto_detect_agents
         :collapse:


   .. py:method:: _get_agent_node_name(agent: str | haive.agents.base.agent.Agent) -> str

      Get the node name for an agent.


      .. autolink-examples:: _get_agent_node_name
         :collapse:


   .. py:method:: _get_unique_node_name(base_name: str) -> str

      Ensure unique node names.


      .. autolink-examples:: _get_unique_node_name
         :collapse:


   .. py:method:: _normalize_destination(dest: str | haive.agents.base.agent.Agent) -> str

      Normalize destination to node name.


      .. autolink-examples:: _normalize_destination
         :collapse:


   .. py:method:: _prepare_input(input_data: Any) -> Any

      Prepare input data for the multi-agent system.

      For PARALLEL mode, we don't pass engines through state to avoid
      serialization issues. Each agent will use its own engines.


      .. autolink-examples:: _prepare_input
         :collapse:


   .. py:method:: _serialize_engine_for_state(engine: Any) -> dict[str, Any]

      Serialize an engine to a dict that can be stored in state and serialized by msgpack.

      The agent node can model validate this dict back to an engine if needed.


      .. autolink-examples:: _serialize_engine_for_state
         :collapse:


   .. py:method:: add_conditional_edges(source_agent: str | haive.agents.base.agent.Agent, condition: collections.abc.Callable[[Any], Any], destinations: str | list[str] | dict[Any, str | haive.agents.base.agent.Agent], default: str | haive.agents.base.agent.Agent | None = END) -> None

      Add conditional edges between agents with simple API.

      This method provides a simple interface for adding conditional routing between
      agents, similar to the API used in simple agents. The conditional edges are
      stored and processed during graph building to create the actual routing logic.

      :param source_agent: Source agent (name or Agent object) from which to route
      :param condition: Function that takes state and returns routing key for destinations
      :param destinations: Target destinations based on condition result. Can be:
                           - str: Single destination
                           - List[str]: Multiple destinations (condition returns index)
                           - Dict[Any, Union[str, Agent]]: Mapping of condition results to destinations
      :param default: Default destination if no condition matches (defaults to END)

      .. rubric:: Example

      Simple conditional routing::

          def route_condition(state):
              return "success" if state.is_valid else "retry"

          multi_agent.add_conditional_edges(
              source_agent=validator,
              condition=route_condition,
              destinations={
                  "success": "END",
                  "retry": processor
              }
          )

      .. note::

         The conditional edges are stored and processed during graph building.
         The actual routing logic is implemented using the underlying BaseGraph
         conditional edges functionality.


      .. autolink-examples:: add_conditional_edges
         :collapse:


   .. py:method:: add_edge(source_agent: str | haive.agents.base.agent.Agent, target_agent: str | haive.agents.base.agent.Agent) -> None

      Add a simple edge between agents.

      :param source_agent: Source agent
      :param target_agent: Target agent


      .. autolink-examples:: add_edge
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the execution graph using the configured agents and routing logic.

      This method creates the complete execution graph by:

      1. Adding all agents as nodes with proper configuration
      2. Adding custom workflow nodes for state processing
      3. Setting up entry points for execution flow
      4. Processing conditional edges for dynamic routing
      5. Creating sequential flow if no explicit routing is defined
      6. Configuring finish points for completion

      The graph building process handles both simple sequential execution and
      complex conditional routing patterns, automatically normalizing destinations
      and creating the appropriate edge types.

      :returns:

                Compiled graph ready for execution with all nodes, edges,
                    and routing logic properly configured
      :rtype: BaseGraph

      .. note::

         This method is called automatically during agent execution setup.
         The resulting graph uses the advanced BaseGraph functionality for
         conditional edges and state management.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: convert_to_agent_list(v) -> Any
      :classmethod:


      Convert regular list to AgentList.


      .. autolink-examples:: convert_to_agent_list
         :collapse:


   .. py:method:: model_post_init(__context: Any) -> None


   .. py:attribute:: agent_node_mapping
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: agents
      :type:  AgentList
      :value: None



   .. py:attribute:: branches
      :type:  list[tuple] | None
      :value: None



   .. py:attribute:: conditional_edges
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: create_missing_nodes
      :type:  bool
      :value: None



   .. py:attribute:: entry_points
      :type:  list[str | haive.agents.base.agent.Agent] | None
      :value: None



   .. py:attribute:: finish_points
      :type:  list[str | haive.agents.base.agent.Agent] | None
      :value: None



   .. py:attribute:: include_meta
      :type:  bool
      :value: None



   .. py:attribute:: schema_build_mode
      :type:  haive.core.schema.agent_schema_composer.BuildMode
      :value: None



   .. py:attribute:: schema_separation
      :type:  str
      :value: None



   .. py:attribute:: state_schema_override
      :type:  type[haive.core.schema.state_schema.StateSchema] | None
      :value: None



   .. py:attribute:: workflow_nodes
      :type:  dict[str, collections.abc.Callable] | None
      :value: None



.. py:function:: create_branching_multi_agent(agents: list[haive.agents.base.agent.Agent], branches: list[tuple], name: str = 'Branching Multi-Agent', state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> MultiAgentBase

   Create a multi-agent system with conditional branching.

   This convenience function creates a MultiAgentBase configured for conditional
   execution with branching logic. The system uses SEQUENCE schema build mode
   by default for unified state management.

   :param agents: List of agents involved in the branching system
   :param branches: List of branch tuples defining conditional routing
   :param name: Name for the multi-agent system
   :param state_schema: Optional state schema override
   :param \*\*kwargs: Additional configuration options for MultiAgentBase

   :returns: Configured branching multi-agent system
   :rtype: MultiAgentBase

   .. rubric:: Example

   Create a system with conditional routing::

       def route_condition(state):
           return "success" if state.is_valid else "retry"

       branches = [
           (validator, route_condition, {
               "success": "END",
               "retry": processor
           })
       ]

       system = create_branching_multi_agent(
           agents=[processor, validator],
           branches=branches,
           name="validation_system"
       )


   .. autolink-examples:: create_branching_multi_agent
      :collapse:

.. py:function:: create_plan_execute_multi_agent(planner_agent: haive.agents.base.agent.Agent, executor_agent: haive.agents.base.agent.Agent, replanner_agent: haive.agents.base.agent.Agent, name: str = 'Plan and Execute System', state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, schema_build_mode: haive.core.schema.agent_schema_composer.BuildMode = BuildMode.PARALLEL, **kwargs) -> MultiAgentBase

   Create a Plan and Execute multi-agent system with proper routing.


   .. autolink-examples:: create_plan_execute_multi_agent
      :collapse:

.. py:function:: create_sequential_multi_agent(agents: list[haive.agents.base.agent.Agent], name: str = 'Sequential Multi-Agent', state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> MultiAgentBase

   Create a simple sequential multi-agent system.

   This convenience function creates a MultiAgentBase configured for sequential
   execution where agents run in the order provided. The system uses SEQUENCE
   schema build mode for unified state management.

   :param agents: List of agents to execute in sequence
   :param name: Name for the multi-agent system
   :param state_schema: Optional state schema override
   :param \*\*kwargs: Additional configuration options for MultiAgentBase

   :returns: Configured sequential multi-agent system
   :rtype: MultiAgentBase

   .. rubric:: Example

   Create a simple pipeline::

       agents = [preprocessor, analyzer, summarizer]
       pipeline = create_sequential_multi_agent(
           agents=agents,
           name="analysis_pipeline"
       )


   .. autolink-examples:: create_sequential_multi_agent
      :collapse:

.. py:data:: logger

