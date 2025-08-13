
:py:mod:`agents.reasoning_and_critique`
=======================================

.. py:module:: agents.reasoning_and_critique

Reasoning And Critique - Module for reasoning and self-critique agents.

This module provides agents that can reason about their outputs and perform
self-critique and reflection to improve their responses.

Available Agents:
    - MCTSAgent: Monte Carlo Tree Search based reasoning agent

.. rubric:: Example

Basic MCTS usage::

    from haive.agents.reasoning_and_critique.mcts import MCTSAgent, MCTSAgentConfig

    config = MCTSAgentConfig(
        name="mcts_reasoner",
        max_iterations=10
    )
    agent = MCTSAgent(config=config)

    result = await agent.ainvoke({"problem": "Solve this logic puzzle..."})


.. autolink-examples:: agents.reasoning_and_critique
   :collapse:




