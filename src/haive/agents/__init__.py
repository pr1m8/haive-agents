"""Haive Agents Module - Main exports.

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

Examples:
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
"""

import lazy_loader as lazy

# Define submodules to lazy load
submodules = [
    "base",
    "simple",
    "react",
    "multi",
    "rag",
    "planning",
    "memory",
    "conversation",
    "supervisor",
    "discovery",
    "reflection",
    "structured_output",
    "sequential",
    "patterns",
    "utils",
]

# Define specific attributes from submodules to expose
submod_attrs = {
    "base": ["Agent"],
    "simple": ["SimpleAgent"],
    "react": ["ReactAgent"],
    "multi": ["MultiAgent", "MultiAgent"],
    "rag": ["BaseRAGAgent", "SimpleRAGAgent"],
    "planning": ["PlanAndExecuteAgent"],
    "memory": ["BaseMemoryAgent"],
    "conversation": ["ConversationAgent"],
    "supervisor": ["SupervisorAgent", "DynamicSupervisor"],
    "discovery": ["DynamicToolSelector"],
    "reflection": ["ReflectionAgent"],
    "structured_output": ["StructuredOutputAgent"],
    "sequential": ["SequentialAgent"],
    "patterns": [],  # TODO: Add specific pattern exports
    "utils": ["AgentUtils"],
}

# Attach lazy loading - this creates __getattr__, __dir__, and __all__
__getattr__, __dir__, __all__ = lazy.attach(
    __name__, submodules=submodules, submod_attrs=submod_attrs
)

# Eagerly load the most commonly used base agents for immediate access
from .base import Agent
from .multi import MultiAgent
from .react import ReactAgent
from .simple import SimpleAgent

# Add eager imports to __all__
__all__ += ["Agent", "MultiAgent", "ReactAgent", "SimpleAgent"]

# Note: Heavy agent implementations and specialized modules are lazy loaded
# to improve import performance and reduce memory usage
