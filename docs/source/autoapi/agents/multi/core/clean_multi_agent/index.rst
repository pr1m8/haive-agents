
:py:mod:`agents.multi.core.clean_multi_agent`
=============================================

.. py:module:: agents.multi.core.clean_multi_agent

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




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiAgent {
        node [shape=record];
        "MultiAgent" [label="MultiAgent"];
        "haive.agents.base.agent.Agent" -> "MultiAgent";
      }

.. autoclass:: agents.multi.core.clean_multi_agent.MultiAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.multi.core.clean_multi_agent
   :collapse:
   
.. autolink-skip:: next
