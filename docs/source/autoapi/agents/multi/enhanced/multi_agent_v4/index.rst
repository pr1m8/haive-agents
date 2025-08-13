
:py:mod:`agents.multi.enhanced.multi_agent_v4`
==============================================

.. py:module:: agents.multi.enhanced.multi_agent_v4

Enhanced MultiAgent V4 - Advanced multi-agent orchestration with enhanced base agent pattern.

This module provides the MultiAgent class, which represents the **recommended**
multi-agent coordination implementation in the Haive framework. It leverages the enhanced
base agent pattern to provide sophisticated agent orchestration with clean, intuitive APIs.

**Current Status**: This is the **most advanced and recommended** MultiAgent implementation
for new projects. It provides the cleanest API, best performance, and most complete feature
set for multi-agent coordination.

The MultiAgent extends the base Agent class and implements the required
build_graph() abstract method, enabling it to participate fully in the Haive ecosystem
while providing advanced multi-agent capabilities.

Key Features:
    - **Enhanced Base Agent Pattern**: Properly extends Agent and implements build_graph()
    - **Direct List Initialization**: Simple API with agents=[agent1, agent2, ...]
    - **Multiple Execution Modes**: Sequential, parallel, conditional, and manual orchestration
    - **AgentNodeV3 Integration**: Advanced state projection for clean agent isolation
    - **MultiAgentState Management**: Type-safe state handling across agents
    - **Dynamic Graph Building**: Auto, manual, and lazy build modes
    - **Conditional Routing**: Rich conditional edge support via BaseGraph2
    - **Hot Agent Addition**: Add agents dynamically with automatic recompilation

Architecture:
    The MultiAgent follows a hierarchical architecture:

    1. **Agent Layer**: Individual agents with their own state and logic
    2. **Orchestration Layer**: Coordination logic and routing decisions
    3. **State Layer**: MultiAgentState for shared and private state management
    4. **Execution Layer**: AgentNodeV3 for proper state projection

.. rubric:: Example

Basic sequential workflow::

    >>> from haive.agents.multi.agent import MultiAgent
    >>> from haive.agents.simple import SimpleAgent
    >>> from haive.agents.react import ReactAgent
    >>>
    >>> # Create individual agents
    >>> analyzer = ReactAgent(name="analyzer", tools=[...])
    >>> formatter = SimpleAgent(name="formatter")
    >>>
    >>> # Create multi-agent workflow
    >>> workflow = MultiAgent(
    ...     name="analysis_pipeline",
    ...     agents=[analyzer, formatter],
    ...     execution_mode="sequential"
    ... )
    >>>
    >>> # Execute workflow
    >>> result = await workflow.arun({"task": "Analyze this data"})

Advanced conditional routing::

    >>> # Create workflow with conditional execution
    >>> workflow = MultiAgent(
    ...     name="smart_processor",
    ...     agents=[classifier, simple_processor, complex_processor],
    ...     execution_mode="conditional"
    ... )
    >>>
    >>> # Add routing logic
    >>> workflow.add_conditional_edge(
    ...     from_agent="classifier",
    ...     condition=lambda state: state.get("complexity") > 0.7,
    ...     true_agent="complex_processor",
    ...     false_agent="simple_processor"
    ... )

Parallel execution with convergence::

    >>> # Create parallel workflow
    >>> workflow = MultiAgent(
    ...     name="parallel_analysis",
    ...     agents=[analyzer1, analyzer2, analyzer3, aggregator],
    ...     execution_mode="manual"
    ... )
    >>>
    >>> # Configure parallel execution
    >>> workflow.add_edge(START, "analyzer1")
    >>> workflow.add_edge(START, "analyzer2")
    >>> workflow.add_edge(START, "analyzer3")
    >>> workflow.add_edge("analyzer1", "aggregator")
    >>> workflow.add_edge("analyzer2", "aggregator")
    >>> workflow.add_edge("analyzer3", "aggregator")
    >>> workflow.add_edge("aggregator", END)

.. seealso::

   - :class:`haive.agents.base.agent.Agent`: Base agent class
   - :class:`haive.core.schema.prebuilt.multi_agent_state.MultiAgentState`: State management
   - :mod:`haive.core.graph.node.agent_node_v3`: AgentNodeV3 for state projection
   - :class:`haive.core.graph.state_graph.base_graph2.BaseGraph`: Graph building
   - :class:`haive.agents.multi.enhanced_multi_agent_v3.EnhancedMultiAgent`: V3 with generics
   - :class:`haive.agents.multi.clean.MultiAgent`: Current default (being replaced)

.. note::

   This implementation is planned to become the default MultiAgent in a future release.
   It offers significant improvements over the current clean.py implementation including
   better type safety, cleaner API, and more powerful routing capabilities.


.. autolink-examples:: agents.multi.enhanced.multi_agent_v4
   :collapse:

Classes
-------

.. autoapisummary::

   agents.multi.enhanced.multi_agent_v4.MultiAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgent {
        node [shape=record];
        "MultiAgent" [label="MultiAgent"];
        "haive.agents.base.agent.Agent" -> "MultiAgent";
      }

.. autoclass:: agents.multi.enhanced.multi_agent_v4.MultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.multi.enhanced.multi_agent_v4
   :collapse:
   
.. autolink-skip:: next
