agents.multi.core.clean_multi_agent
===================================

.. py:module:: agents.multi.core.clean_multi_agent

.. autoapi-nested-parse::

   Clean MultiAgent implementation - unified multi-agent coordination system.

   This module provides the current default multi-agent coordination system for
   the Haive framework. It supports simple sequential execution, complex routing patterns,
   parallel execution, and conditional workflows - all in one unified implementation.

   **Current Status**: This is the **default MultiAgent** exported by the multi module.
   It provides stable, production-ready multi-agent coordination. For new projects requiring
   advanced features, consider using MultiAgent.

   The MultiAgent class extends the base Agent class to coordinate multiple agents
   using various execution patterns. It automatically detects whether to use intelligent
   routing (via BaseGraph) or custom routing based on the configuration.

   Key Features:
       - List initialization: Natural `MultiAgent([agent1, agent2])` syntax
       - Flexible routing: Sequential, parallel, conditional, and custom patterns
       - Intelligent detection: Automatically uses appropriate routing mode
       - Enhanced methods: add_conditional_routing, add_parallel_group, add_edge
       - Backward compatible: Works with existing examples and patterns
       - No mocks testing: 100% real component validation

   .. rubric:: Examples

   Simple sequential execution::

       from haive.agents.multi.agent import MultiAgent
       from haive.agents.simple import SimpleAgent

       agent1 = SimpleAgent(name="analyzer")
       agent2 = SimpleAgent(name="summarizer")

       multi_agent = MultiAgent(agents=[agent1, agent2])
       result = await multi_agent.arun("Process this data")

   Conditional routing with entry point::

       multi_agent = MultiAgent(
           agents=[classifier, billing_agent, technical_agent],
           entry_point="classifier"
       )

       multi_agent.add_conditional_routing(
           "classifier",
           lambda state: state.get("category", "general"),
           {
               "billing": "billing_agent",
               "technical": "technical_agent",
               "general": "billing_agent"
           }
       )

   Parallel execution with convergence::

       multi_agent = MultiAgent(
           agents=[processor1, processor2, processor3, aggregator]
       )

       # Run processors in parallel, then aggregate
       multi_agent.add_parallel_group(
           ["processor1", "processor2", "processor3"],
           next_agent="aggregator"
       )

   Direct edge routing::

       multi_agent = MultiAgent(
           agents=[validator, processor, formatter],
           entry_point="validator"
       )

       # Create explicit flow
       multi_agent.add_edge("validator", "processor")
       multi_agent.add_edge("processor", "formatter")

   .. note::

      This is the unified implementation that replaces all previous multi-agent
      implementations. Use this for all new development. The system automatically
      detects whether to use intelligent routing or custom routing based on the
      branch configurations provided.

   .. seealso::

      BaseGraph: For intelligent routing capabilities
      MultiAgentState: For state management across agents
      Agent: Base class for all agent implementations
      README.md: Comprehensive documentation and examples


   .. autolink-examples:: agents.multi.core.clean_multi_agent
      :collapse:


Classes
-------

.. autoapisummary::

   agents.multi.core.clean_multi_agent.MultiAgent


Module Contents
---------------

.. py:class:: MultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Unified multi-agent coordination system for the Haive framework.

   MultiAgent extends the base Agent class to coordinate multiple agents using
   various execution patterns. It supports both simple sequential execution
   and complex routing patterns including conditional routing, parallel execution,
   and custom branching logic.

   The implementation automatically detects whether to use intelligent routing
   (via BaseGraph) or custom routing based on the configuration provided.

   .. attribute:: agents

      Dictionary of agents this multi-agent coordinates, keyed by agent name.

   .. attribute:: agent

      Optional main/default agent for this multi-agent (legacy support).

   .. attribute:: execution_mode

      Execution pattern - "infer", "sequential", "parallel", "conditional", or "branch".

   .. attribute:: infer_sequence

      Whether to automatically infer execution sequence from dependencies.

   .. attribute:: branches

      Branch configurations for conditional and custom routing.

   .. attribute:: entry_point

      Starting agent for execution (optional).

   .. rubric:: Examples

   Basic sequential execution::

       multi_agent = MultiAgent(agents=[agent1, agent2, agent3])
       result = await multi_agent.arun("Process this task")

   Conditional routing with entry point::

       multi_agent = MultiAgent(
           agents=[classifier, processor1, processor2],
           entry_point="classifier"
       )

       multi_agent.add_conditional_routing(
           "classifier",
           lambda state: state.get("category"),
           {"type1": "processor1", "type2": "processor2"}
       )

   Parallel execution with convergence::

       multi_agent = MultiAgent(agents=[agent1, agent2, agent3])
       multi_agent.add_parallel_group(["agent1", "agent2"], next_agent="agent3")

   .. note::

      This class automatically uses MultiAgentState for state management
      if no custom state schema is provided. The state schema handles
      message passing and context sharing between agents.

   .. seealso::

      BaseGraph.add_intelligent_agent_routing: For automatic routing inference
      MultiAgentState: Default state schema for multi-agent coordination
      Agent: Base class with core agent functionality


   .. autolink-examples:: MultiAgent
      :collapse:

   .. py:method:: _build_custom_routing(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build custom routing based on enhanced branch configurations.


      .. autolink-examples:: _build_custom_routing
         :collapse:


   .. py:method:: add_branch(source_agent: str, condition: str, target_agents: list[str])

      Add a branch condition for routing between agents.

      :param source_agent: The agent to branch from
      :param condition: The condition logic (e.g., 'if error' or 'if success')
      :param target_agents: List of possible target agents


      .. autolink-examples:: add_branch
         :collapse:


   .. py:method:: add_conditional_edges(source: str, path: collections.abc.Callable[[dict[str, Any]], str]) -> None

      Add conditional edges for backward compatibility with examples.

      This method provides compatibility with existing examples that use
      add_conditional_edges directly. It wraps the add_conditional_routing
      method with automatic route mapping.

      :param source: Source agent name to route from.
      :param path: Function that takes state and returns target agent name.

      .. rubric:: Examples

      Basic routing function::

          def route_by_category(state):
              category = state.get("category", "default")
              if category == "billing":
                  return "billing_agent"
              elif category == "technical":
                  return "technical_agent"
              else:
                  return "general_agent"

          multi_agent.add_conditional_edges("classifier", route_by_category)


      .. autolink-examples:: add_conditional_edges
         :collapse:


   .. py:method:: add_conditional_routing(source_agent: str, condition_fn: collections.abc.Callable[[dict[str, Any]], str], routes: dict[str, str]) -> None

      Add conditional routing with a function that returns route keys.

      This method enables dynamic routing based on state conditions. The condition
      function receives the current state and returns a key that maps to a target
      agent in the routes dictionary.

      :param source_agent: The agent to route from. Must exist in the agents dictionary.
      :param condition_fn: Function that takes state dict and returns a route key.
                           Should return a string that exists as a key in the routes dictionary.
      :param routes: Dictionary mapping route keys to target agent names.
                     Keys are the possible return values from condition_fn.
                     Values are agent names that must exist in the agents dictionary.

      :raises ValueError: If source_agent doesn't exist in agents dictionary.
      :raises KeyError: If routes contain agent names that don't exist in agents.

      .. rubric:: Examples

      Basic conditional routing::

          def route_by_priority(state):
              return "high" if state.get("priority", 0) > 5 else "normal"

          multi_agent.add_conditional_routing(
              "classifier",
              route_by_priority,
              {"high": "urgent_processor", "normal": "standard_processor"}
          )

      Category-based routing::

          multi_agent.add_conditional_routing(
              "categorizer",
              lambda state: state.get("category", "default"),
              {
                  "billing": "billing_agent",
                  "technical": "tech_support_agent",
                  "default": "general_agent"
              }
          )

      .. note::

         This method marks the MultiAgent for custom routing mode, bypassing
         the intelligent routing system in favor of explicit routing logic.


      .. autolink-examples:: add_conditional_routing
         :collapse:


   .. py:method:: add_edge(source_agent: str, target_agent: str) -> None

      Add a direct edge between two agents.

      This method creates a direct connection from one agent to another,
      ensuring the target agent runs after the source agent completes.

      :param source_agent: Source agent name. Must exist in the agents dictionary.
      :param target_agent: Target agent name. Must exist in the agents dictionary.

      :raises ValueError: If source_agent doesn't exist in agents dictionary.
      :raises ValueError: If target_agent doesn't exist in agents dictionary.

      .. rubric:: Examples

      Sequential flow::

          multi_agent.add_edge("preprocessor", "analyzer")
          multi_agent.add_edge("analyzer", "postprocessor")

      Branching flow::

          multi_agent.add_edge("classifier", "processor_a")
          multi_agent.add_edge("classifier", "processor_b")

      .. note::

         This method marks the MultiAgent for custom routing mode, bypassing
         the intelligent routing system in favor of explicit connections.


      .. autolink-examples:: add_edge
         :collapse:


   .. py:method:: add_parallel_group(agent_names: list[str], next_agent: str | None = None) -> None

      Add a group of agents that run in parallel.

      This method configures a set of agents to execute in parallel, with
      optional convergence to a single agent after parallel execution completes.

      :param agent_names: List of agent names to run in parallel.
                          All names must exist in the agents dictionary.
      :param next_agent: Optional next agent to run after the parallel group completes.
                         If provided, must exist in the agents dictionary.

      :raises ValueError: If any agent name in agent_names doesn't exist in agents.
      :raises ValueError: If next_agent is provided but doesn't exist in agents.

      .. rubric:: Examples

      Parallel processing with convergence::

          multi_agent.add_parallel_group(
              ["data_processor", "image_processor", "text_processor"],
              next_agent="aggregator"
          )

      Parallel processing without convergence::

          multi_agent.add_parallel_group(
              ["notification_sender", "logger", "metrics_collector"]
          )

      .. note::

         This method marks the MultiAgent for custom routing mode. The parallel
         execution is managed by the underlying graph execution system.


      .. autolink-examples:: add_parallel_group
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the BaseGraph for this multi-agent.

      Uses intelligent routing from BaseGraph for sequence inference and branching.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create(agents: list[haive.agents.base.agent.Agent], name: str = 'multi_agent', execution_mode: str = 'infer', **kwargs) -> MultiAgent
      :classmethod:


      Create a multi-agent from a list of agents.

      This factory method provides a convenient way to create a MultiAgent
      from a list of agents with optional configuration.

      :param agents: List of Agent instances to coordinate.
      :param name: Name for the multi-agent instance.
      :param execution_mode: Execution pattern - "infer", "sequential", "parallel",
                             "conditional", or "branch".
      :param \*\*kwargs: Additional keyword arguments passed to the MultiAgent constructor.

      :returns: Configured multi-agent instance.
      :rtype: MultiAgent

      .. rubric:: Examples

      Basic creation::

          agents = [SimpleAgent(name="a"), SimpleAgent(name="b")]
          multi_agent = MultiAgent.create(agents, name="my_workflow")

      With custom execution mode::

          multi_agent = MultiAgent.create(
              agents,
              name="parallel_workflow",
              execution_mode="parallel"
          )


      .. autolink-examples:: create
         :collapse:


   .. py:method:: normalize_agents_and_name(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Normalize agents dict and auto-generate name - follows engines pattern.


      .. autolink-examples:: normalize_agents_and_name
         :collapse:


   .. py:method:: set_sequence(sequence: list[str])

      Manually set the execution sequence of agents.

      :param sequence: List of agent names in execution order


      .. autolink-examples:: set_sequence
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup multi-agent - use MultiAgentState by default.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: agent
      :type:  haive.agents.base.agent.Agent | None
      :value: None



   .. py:attribute:: agents
      :type:  dict[str, haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: branches
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: entry_point
      :type:  str | None
      :value: None



   .. py:attribute:: execution_mode
      :type:  str
      :value: None



   .. py:attribute:: infer_sequence
      :type:  bool
      :value: None



