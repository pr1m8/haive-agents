"""Multi-Agent System for the Haive Framework.

This module provides a clean, simple multi-agent system for coordinating
multiple agents with intelligent routing and execution patterns.

Example:
    >>> from haive.agents.multi import MultiAgent
    >>> from haive.agents.simple.agent import SimpleAgent
    >>> from haive.agents.react.agent import ReactAgent
    >>>
    >>> # Create agents
    >>> writer = SimpleAgent(name="writer", engine=writer_config)
    >>> editor = ReactAgent(name="editor", engine=editor_config)
    >>>
    >>> # Create multi-agent system
    >>> system = MultiAgent.create(
    ...     agents=[writer, editor],
    ...     name="content_pipeline",
    ...     execution_mode="sequential"
    ... )
    >>>
    >>> # Run the system
    >>> result = await system.arun("Write a story about AI")
"""

# Import clean multi-agent implementation

from haive.agents.multi.clean import MultiAgent

__all__ = [
    "MultiAgent",
]
