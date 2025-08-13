
:py:mod:`agents.multi.agent`
============================

.. py:module:: agents.multi.agent

Enhanced MultiAgent V4 - Advanced multi-agent orchestration with enhanced base agent pattern.

This module provides the MultiAgent class, which represents the next generation
of multi-agent coordination in the Haive framework. It leverages the enhanced base agent
pattern to provide sophisticated agent orchestration with clean, intuitive APIs.

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

    >>> from haive.agents.multi.enhanced_multi_agent_v4 import MultiAgent
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

.. seealso::

   - :class:`haive.agents.base.agent.Agent`: Base agent class
   - :class:`haive.core.schema.prebuilt.multi_agent_state.MultiAgentState`: State management
   - :mod:`haive.core.graph.node.agent_node_v3`: AgentNodeV3 for state projection
   - :class:`haive.core.graph.state_graph.base_graph2.BaseGraph`: Graph building


.. autolink-examples:: agents.multi.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.multi.agent.MultiAgent


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

.. autoclass:: agents.multi.agent.MultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.multi.agent
   :collapse:
   
.. autolink-skip:: next
