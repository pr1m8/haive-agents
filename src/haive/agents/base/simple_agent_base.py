"""Simple Agent base class based on GraphNode architecture.

This module provides a simplified Agent class that inherits from GraphNode
while maintaining clear separation between LLM reasoning agents and
deterministic processing components.
"""

from __future__ import annotations

import logging
from abc import abstractmethod
from typing import Any

from haive.core.engine.base import Engine, EngineType
from haive.core.graph.state_graph.graph_node import GraphNode
from haive.core.schema.schema_composer import SchemaComposer
from langchain_core.tools import BaseTool
from pydantic import Field, model_validator

logger = logging.getLogger(__name__)


class Agent(GraphNode):
    """Base class for LLM-based reasoning agents.

    Agents are distinguished from Components by their ability to:
    - Reason about problems using LLM engines
    - Use tools to interact with external systems
    - Make dynamic decisions based on context
    - Maintain conversation memory and state

    All true "Agents" should have LLM reasoning capabilities.
    Deterministic processing should use Component classes instead.

    Attributes:
        engine: Primary LLM engine for reasoning (required)
        engines: Dictionary of additional engines
        tools: List of tools available to this agent
        conversation_memory: Whether to maintain conversation history
        max_iterations: Maximum reasoning iterations
    """

    # Core engine requirements (LLM for reasoning)
    engine: Engine | None = Field(
        default=None,
        description="Primary LLM engine for reasoning (required for agents)",
    )

    engines: dict[str, Engine] = Field(
        default_factory=dict,
        description="Dictionary of additional engines used by this agent",
    )

    # Tool capabilities
    tools: list[BaseTool] = Field(
        default_factory=list, description="List of tools available to this agent"
    )

    # Agent-specific behavior
    conversation_memory: bool = Field(
        default=True, description="Whether to maintain conversation history"
    )

    max_iterations: int = Field(
        default=10, description="Maximum reasoning iterations before stopping"
    )

    # Schema generation control
    set_schema: bool = Field(
        default=True, description="Whether to auto-generate schemas from engines"
    )

    @model_validator(mode="after")
    def validate_agent_requirements(self) -> Agent:
        """Validate that agent has required LLM capabilities."""
        if not self.engine:
            if not self.engines:
                raise ValueError(
                    "Agents must have at least one engine. "
                    "Provide either 'engine' or 'engines' parameter."
                )
            # Try to find an LLM engine in engines dict
            llm_engines = [
                eng
                for eng in self.engines.values()
                if hasattr(eng, "engine_type") and eng.engine_type == EngineType.LLM
            ]
            if llm_engines:
                self.engine = llm_engines[0]
            else:
                logger.warning(
                    f"Agent {self.name} has no LLM engine. "
                    "Consider using Component for deterministic processing."
                )

        # Set up schemas if requested
        if self.set_schema:
            self._setup_schemas()

        return self

    def _setup_schemas(self) -> None:
        """Generate schemas from available engines."""
        if not self.state_schema:
            engine_list = []
            if self.engine:
                engine_list.append(self.engine)
            engine_list.extend(self.engines.values())

            if engine_list:
                logger.debug(f"Creating schema from {len(engine_list)} engines")
                self.state_schema = SchemaComposer.from_components(
                    components=engine_list, name=f"{self.__class__.__name__}State"
                )
            else:
                logger.debug("No engines found, using basic message state")
                from haive.core.schema.prebuilt.messages_state import MessagesState

                self.state_schema = MessagesState

    @abstractmethod
    def reason(self, problem: Any, context: dict[str, Any] | None = None) -> Any:
        """Reason about a problem and provide a solution.

        This method must be implemented by all agent subclasses to define
        their reasoning capabilities.

        Args:
            problem: The problem or input to reason about
            context: Optional context information for reasoning

        Returns:
            Any: The reasoning result or solution
        """
        pass

    async def areason(self, problem: Any, context: dict[str, Any] | None = None) -> Any:
        """Asynchronous version of reason method."""
        return self.reason(problem, context)

    def use_tool(self, tool_name: str, **kwargs) -> Any:
        """Use a specific tool by name.

        Args:
            tool_name: Name of the tool to use
            **kwargs: Arguments to pass to the tool

        Returns:
            Any: Tool execution result

        Raises:
            ValueError: If tool is not found
        """
        for tool in self.tools:
            if tool.name == tool_name:
                return tool.invoke(kwargs)
        raise ValueError(f"Tool '{tool_name}' not found in agent tools")

    def get_available_tools(self) -> list[str]:
        """Get list of available tool names."""
        return [tool.name for tool in self.tools]

    def add_tool(self, tool: BaseTool) -> None:
        """Add a tool to this agent."""
        if tool not in self.tools:
            self.tools.append(tool)

    def can_reason(self) -> bool:
        """Check if this agent has reasoning capabilities."""
        return self.engine is not None

    def get_agent_capabilities(self) -> dict[str, Any]:
        """Get information about agent capabilities."""
        return {
            "has_reasoning": self.can_reason(),
            "tool_count": len(self.tools),
            "available_tools": self.get_available_tools(),
            "conversation_memory": self.conversation_memory,
            "max_iterations": self.max_iterations,
            "engine_count": len(self.engines) + (1 if self.engine else 0),
        }

    def get_node_type(self) -> str:
        """Get the node type identifier."""
        return "agent"

    # Backward compatibility hook
    def setup_agent(self) -> None:
        """Hook for subclass-specific setup logic.

        Maintained for backward compatibility with existing Agent interface.
        """
        pass
