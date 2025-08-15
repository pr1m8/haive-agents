agents.multi.enhanced.multi_agent_v3
====================================

.. py:module:: agents.multi.enhanced.multi_agent_v3

.. autoapi-nested-parse::

   Enhanced MultiAgent V3 - Full feature implementation with generic typing support.

   This version provides advanced multi-agent orchestration with generic typing support,
   performance tracking, and enhanced debugging capabilities. It follows the V3 pattern
   established by SimpleAgentV3 and ReactAgent.

   **Current Status**: This is the **V3 enhanced implementation** with advanced features.
   Use this when you need generic typing support, performance tracking, or complex routing
   patterns. For simpler use cases, use the default MultiAgent. For the latest features,
   use MultiAgent.

   Key Features:
   - **Generic typing**: MultiAgent[AgentsT] for type-safe agent collections
   - **Performance tracking**: Adaptive routing based on agent performance metrics
   - **Rich debugging**: Comprehensive observability and capabilities display
   - **Multi-engine coordination**: Support for multiple LLM engines
   - **Advanced routing**: Conditional, branching, and adaptive patterns
   - **V3 consistency**: Follows patterns from SimpleAgentV3 and ReactAgent

   This version combines the best features from clean.py and enhanced_multi_agent_standalone.py:
   - Production-ready coordination from clean.py
   - Generic typing and performance features from standalone
   - Full integration with enhanced base Agent class
   - V3 pattern consistency with SimpleAgent V3 and ReactAgent V3

   .. rubric:: Examples

   With generic typing for type safety::

       from typing import Dict, Any
       from haive.agents.multi.enhanced_multi_agent_v3 import EnhancedMultiAgent

       # Type-safe agent dictionary
       agents: Dict[str, SimpleAgent] = {
           "analyzer": SimpleAgent(name="analyzer"),
           "processor": SimpleAgent(name="processor")
       }

       # Generic typing ensures type safety
       multi: EnhancedMultiAgent[Dict[str, SimpleAgent]] = EnhancedMultiAgent(
           name="typed_workflow",
           agents=agents,
           performance_mode=True
       )

   With performance tracking::

       # Enable adaptive routing based on performance
       multi = EnhancedMultiAgent(
           name="adaptive_workflow",
           agents={"fast": fast_agent, "accurate": accurate_agent},
           execution_mode="branch",
           performance_mode=True,
           adaptation_rate=0.2
       )

       # System learns which agent performs best for different tasks
       result = await multi.arun("Process this data")

   .. seealso::

      - :class:`haive.agents.multi.enhanced_multi_agent_v4.MultiAgent`: Latest V4
      - :class:`haive.agents.multi.clean.MultiAgent`: Current default
      - :class:`haive.agents.simple.agent_v3.SimpleAgentV3`: V3 pattern reference


   .. autolink-examples:: agents.multi.enhanced.multi_agent_v3
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.multi.enhanced.multi_agent_v3.AgentsT
   agents.multi.enhanced.multi_agent_v3.console
   agents.multi.enhanced.multi_agent_v3.logger


Classes
-------

.. autoapisummary::

   agents.multi.enhanced.multi_agent_v3.EnhancedMultiAgent


Module Contents
---------------

.. py:class:: EnhancedMultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`, :py:obj:`Generic`\ [\ :py:obj:`AgentsT`\ ]


   Enhanced MultiAgent V3 with full advanced features.

   This agent combines the production stability of clean.py with advanced features
   from enhanced_multi_agent_standalone.py, following the V3 pattern established
   by SimpleAgent V3 and ReactAgent V3.

   Core Features:
   - Generic typing for contained agents: MultiAgent[AgentsT]
   - Production-ready coordination patterns (sequential, parallel, conditional, custom)
   - Intelligent routing detection and BaseGraph integration
   - Rich API for flexible routing configuration
   - Real component testing (no mocks)

   Enhanced V3 Features:
   - Performance tracking and adaptive routing
   - Rich debugging and observability
   - Multi-engine coordination capabilities
   - Advanced persistence configuration
   - Comprehensive capabilities display and analysis

   Multi-Agent Specific Features:
   - Flexible agent management (dict or list)
   - Entry point configuration for workflow control
   - Branch configurations for complex routing
   - Custom routing methods: add_conditional_routing, add_parallel_group, add_edge
   - Intelligent vs custom routing detection

   Performance Features:
   - Agent performance metrics tracking
   - Adaptive routing based on success rates and timing
   - Execution optimization and caching
   - Load balancing across agents

   .. attribute:: agents

      Generic collection of agents to coordinate (AgentsT)

   .. attribute:: execution_mode

      How to execute agents (infer/sequential/parallel/conditional/branch)

   .. attribute:: entry_point

      Starting agent for execution

   .. attribute:: branches

      Branch configurations for routing

   .. attribute:: infer_sequence

      Whether to auto-infer execution sequence

   Enhanced Attributes:
       multi_engine_mode: Enable multiple engines for coordination
       advanced_routing: Enable sophisticated routing algorithms
       performance_mode: Enable performance tracking and optimization
       debug_mode: Enable rich debugging and observability
       agent_performance: Performance metrics for each agent
       adaptation_rate: Rate of performance adaptation
       max_iterations: Maximum iterations for conditional flows

   .. rubric:: Examples

   Basic sequential execution (backwards compatible)::

       from haive.agents.simple import SimpleAgent

       agent1 = SimpleAgent(name="analyzer")
       agent2 = SimpleAgent(name="summarizer")

       multi_agent = EnhancedMultiAgent(agents=[agent1, agent2])
       result = await multi_agent.arun("Process this data")

   Enhanced features with performance tracking::

       multi_agent = EnhancedMultiAgent(
           name="adaptive_coordinator",
           agents={"fast": fast_agent, "accurate": accurate_agent},
           execution_mode="branch",
           performance_mode=True,
           debug_mode=True,
           adaptation_rate=0.2
       )

   Conditional routing with entry point::

       multi_agent = EnhancedMultiAgent(
           agents=[classifier, billing_agent, technical_agent],
           entry_point="classifier",
           advanced_routing=True
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

       multi_agent = EnhancedMultiAgent(
           agents=[processor1, processor2, processor3, aggregator],
           performance_mode=True
       )

       multi_agent.add_parallel_group(
           ["processor1", "processor2", "processor3"],
           next_agent="aggregator"
       )

   Generic typing with specialized agents::

       from typing import Dict, Any

       agents: Dict[str, SimpleAgent] = {
           "researcher": research_agent,
           "analyzer": analysis_agent,
           "writer": writing_agent
       }

       multi: EnhancedMultiAgent[Dict[str, SimpleAgent]] = EnhancedMultiAgent(
           name="content_team",
           agents=agents,
           multi_engine_mode=True,
           debug_mode=True
       )


   .. autolink-examples:: EnhancedMultiAgent
      :collapse:

   .. py:method:: __repr__() -> str

      Enhanced string representation.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: _build_custom_routing(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build custom routing based on enhanced branch configurations.


      .. autolink-examples:: _build_custom_routing
         :collapse:


   .. py:method:: _initialize_performance_tracking() -> None

      Initialize performance tracking for all agents.


      .. autolink-examples:: _initialize_performance_tracking
         :collapse:


   .. py:method:: _setup_advanced_routing() -> None

      Configure advanced routing capabilities.


      .. autolink-examples:: _setup_advanced_routing
         :collapse:


   .. py:method:: _setup_multi_engine_mode() -> None

      Configure multi-engine support.


      .. autolink-examples:: _setup_multi_engine_mode
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

      .. rubric:: Examples

      Basic conditional routing::

          def route_by_priority(state):
              return "high" if state.get("priority", 0) > 5 else "normal"

          multi_agent.add_conditional_routing(
              "classifier",
              route_by_priority,
              {"high": "urgent_processor", "normal": "standard_processor"}
          )


      .. autolink-examples:: add_conditional_routing
         :collapse:


   .. py:method:: add_edge(source_agent: str, target_agent: str) -> None

      Add a direct edge between two agents.

      This method creates a direct connection from one agent to another,
      ensuring the target agent runs after the source agent completes.

      :param source_agent: Source agent name. Must exist in the agents dictionary.
      :param target_agent: Target agent name. Must exist in the agents dictionary.

      .. rubric:: Examples

      Sequential flow::

          multi_agent.add_edge("preprocessor", "analyzer")
          multi_agent.add_edge("analyzer", "postprocessor")


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

      .. rubric:: Examples

      Parallel processing with convergence::

          multi_agent.add_parallel_group(
              ["data_processor", "image_processor", "text_processor"],
              next_agent="aggregator"
          )


      .. autolink-examples:: add_parallel_group
         :collapse:


   .. py:method:: analyze_agent_performance() -> dict[str, Any]

      Analyze agent performance metrics.


      .. autolink-examples:: analyze_agent_performance
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the BaseGraph for this multi-agent.

      Uses intelligent routing from BaseGraph for sequence inference and branching.
      Enhanced with V3 debugging and performance features.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create(agents: list[haive.agents.base.agent.Agent] | dict[str, haive.agents.base.agent.Agent], name: str = 'multi_agent', execution_mode: str = 'infer', **kwargs) -> EnhancedMultiAgent
      :classmethod:


      Create an enhanced multi-agent from a collection of agents.

      This factory method provides a convenient way to create an EnhancedMultiAgent
      from a collection of agents with optional configuration.

      :param agents: Collection of Agent instances to coordinate.
      :param name: Name for the multi-agent instance.
      :param execution_mode: Execution pattern - "infer", "sequential", "parallel",
                             "conditional", or "branch".
      :param \*\*kwargs: Additional keyword arguments passed to the constructor.

      :returns: Configured enhanced multi-agent instance.
      :rtype: EnhancedMultiAgent

      .. rubric:: Examples

      Basic creation::

          agents = [SimpleAgent(name="a"), SimpleAgent(name="b")]
          multi_agent = EnhancedMultiAgent.create(agents, name="my_workflow")

      With enhanced features::

          multi_agent = EnhancedMultiAgent.create(
              agents,
              name="adaptive_workflow",
              execution_mode="branch",
              performance_mode=True,
              debug_mode=True
          )


      .. autolink-examples:: create
         :collapse:


   .. py:method:: display_capabilities() -> None

      Display comprehensive multi-agent capabilities.


      .. autolink-examples:: display_capabilities
         :collapse:


   .. py:method:: get_agent(name: str) -> haive.agents.base.agent.Agent | None

      Get agent by name.


      .. autolink-examples:: get_agent
         :collapse:


   .. py:method:: get_agent_names() -> list[str]

      Get list of agent names.


      .. autolink-examples:: get_agent_names
         :collapse:


   .. py:method:: get_best_agent_for_task(task_type: str = 'general') -> str

      Get best performing agent based on metrics.


      .. autolink-examples:: get_best_agent_for_task
         :collapse:


   .. py:method:: get_capabilities_summary() -> dict[str, Any]

      Get comprehensive capabilities summary.


      .. autolink-examples:: get_capabilities_summary
         :collapse:


   .. py:method:: normalize_agents_and_name(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Normalize agents dict and auto-generate name - follows engines pattern.


      .. autolink-examples:: normalize_agents_and_name
         :collapse:


   .. py:method:: setup_agent() -> None

      Enhanced multi-agent setup with V3 features.

      This setup method:
      1. Sets up MultiAgentState as default state schema
      2. Initializes performance tracking for all agents
      3. Configures multi-engine mode if enabled
      4. Sets up advanced routing if enabled
      5. Configures debug mode if enabled
      6. Sets up performance optimization if enabled
      7. Enables automatic schema generation


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: update_performance(agent_name: str, success: bool, duration: float) -> None

      Update agent performance metrics.


      .. autolink-examples:: update_performance
         :collapse:


   .. py:method:: validate_adaptation_rate(v)
      :classmethod:


      Validate adaptation rate range.


      .. autolink-examples:: validate_adaptation_rate
         :collapse:


   .. py:method:: validate_agents(v: AgentsT) -> AgentsT
      :classmethod:


      Validate agents collection.


      .. autolink-examples:: validate_agents
         :collapse:


   .. py:attribute:: adaptation_rate
      :type:  float
      :value: None



   .. py:attribute:: advanced_routing
      :type:  bool
      :value: None



   .. py:attribute:: agent
      :type:  haive.agents.base.agent.Agent | None
      :value: None



   .. py:attribute:: agent_performance
      :type:  dict[str, dict[str, float]]
      :value: None



   .. py:attribute:: agents
      :type:  AgentsT
      :value: None



   .. py:attribute:: branches
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: debug_mode
      :type:  bool
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



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: multi_engine_mode
      :type:  bool
      :value: None



   .. py:attribute:: performance_mode
      :type:  bool
      :value: None



   .. py:attribute:: persistence_config
      :type:  dict[str, Any] | None
      :value: None



.. py:data:: AgentsT

.. py:data:: console

.. py:data:: logger

