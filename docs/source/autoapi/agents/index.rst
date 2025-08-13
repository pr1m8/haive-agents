
:py:mod:`agents`
================

.. py:module:: agents

Haive Agents Module - Main exports.

This module provides various agent implementations for the Haive framework,
including base agents, multi-agents, reactive agents, and specialized agents
for different use cases like RAG, planning, memory, and reasoning.

Key Components:
    - Base: Core agent abstractions and foundational classes
    - Simple: Basic agent implementations for common use cases
    - React: Reactive agents with reasoning loops and tool usage
    - Multi: Multi-agent coordination and orchestration
    - RAG: Retrieval-Augmented Generation agents
    - Planning: Planning and execution agents
    - Memory: Memory-enabled agents with long-term context
    - Conversation: Conversational agent patterns
    - Supervisor: Agent supervision and coordination patterns

The agents are designed to be modular, extensible, and optimized for
various AI workflows and use cases within the Haive ecosystem.

.. rubric:: Examples

Basic agent usage::

    from haive.agents import SimpleAgent
    from haive.core.engine.aug_llm import AugLLMConfig

    agent = SimpleAgent(
        name="helper",
        engine=AugLLMConfig(model="gpt-4")
    )
    result = agent.run("Hello world")

Multi-agent coordination::

    from haive.agents import MultiAgent, SimpleAgent, ReactAgent

    coordinator = MultiAgent([
        SimpleAgent(name="planner"),
        ReactAgent(name="executor", tools=[...])
    ], mode="sequential")

RAG agent setup::

    from haive.agents.rag import BaseRAGAgent
    from haive.core.models import VectorStoreConfig

    rag_agent = BaseRAGAgent(
        vectorstore_config=VectorStoreConfig(...)
    )


.. autolink-examples:: agents
   :collapse:




