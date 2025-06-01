# ============================================================================
# SIMPLE AGENT
# ============================================================================

from typing import Any, Optional, Type, Union

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.base import Engine
from haive.core.graph.node.engine_node import EngineNodeConfig
from haive.core.graph.node.tool_node_config import ToolNodeConfig
from haive.core.graph.node.validation_node_config import ValidationNodeConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from langgraph.graph import END, START
from pydantic import BaseModel, Field, PrivateAttr, Type, Union

from haive.agents.base.agent import Agent


class SimpleAgent(Agent):
    """Simple agent with generalized tool and parser node handling."""

    engine: AugLLMConfig = Field(
        default_factory=AugLLMConfig, description="The main LLM engine"
    )

    engine_node: Optional[EngineNodeConfig] = Field(default=None, exclude=True)
    structured_output_model: Optional[Type[BaseModel]] = Field(default=None)
    structured_output_version: Optional[Union[int, str]] = Field(default="v2")

    tool_node_config: Optional[ToolNodeConfig] = Field(default=None)
    parser_node_config: Optional[Any] = Field(default=None)
    validation_node_config: Optional[ValidationNodeConfig] = Field(default=None)

    # Computed capabilities - these will be set during build_graph()
    _has_tool_node: bool = PrivateAttr(default=False)
    _has_parser_node: bool = PrivateAttr(default=False)
    _has_structured_output_model: bool = PrivateAttr(default=False)
    _capabilities_computed: bool = PrivateAttr(default=False)

    @property
    def has_tool_node(self) -> bool:
        """Get tool node flag."""
        if not self._capabilities_computed:
            self._compute_capabilities()
        return self._has_tool_node

    @property
    def has_parser_node(self) -> bool:
        """Get parser node flag."""
        if not self._capabilities_computed:
            self._compute_capabilities()
        return self._has_parser_node

    @property
    def has_structured_output_model(self) -> bool:
        """Get structured output model flag."""
        if not self._capabilities_computed:
            self._compute_capabilities()
        return self._has_structured_output_model

    def _compute_capabilities(self):
        """Compute what nodes this agent needs."""
        main_engine = self.main_engine
        if not main_engine:
            return

        # Reset flags
        self._has_tool_node = False
        self._has_parser_node = False
        self._has_structured_output_model = False

        # Check structured output model
        if (
            hasattr(main_engine, "structured_output_model")
            and main_engine.structured_output_model
        ) or self.structured_output_model:
            self._has_structured_output_model = True

        # Check tool capabilities
        if hasattr(main_engine, "tools") and main_engine.tools:
            if (
                self._has_structured_output_model
                and str(self.structured_output_version) == "v2"
            ):
                # v2 structured output means parse_output only
                self._has_parser_node = True
            elif hasattr(main_engine, "tool_routes"):
                for tool, tool_type in main_engine.tool_routes.items():
                    if tool_type == "langchain_tool":
                        self._has_tool_node = True
                    elif tool_type == "pydantic_model":
                        self._has_parser_node = True
            else:
                # Default to tool node
                self._has_tool_node = True

        # Check parser node via pydantic_tools
        if hasattr(main_engine, "pydantic_tools") and main_engine.pydantic_tools:
            self._has_parser_node = True

        # Override with explicit configs
        if self.tool_node_config is not None:
            self._has_tool_node = True
        if self.parser_node_config is not None:
            self._has_parser_node = True

        self._capabilities_computed = True

    def build_graph(self) -> BaseGraph:
        """Build the simple agent graph."""

        # Get main engine
        main_engine = self.main_engine
        if not main_engine:
            raise ValueError("No engine available for SimpleAgent")

        # FIRST: Compute capabilities before building anything
        self._compute_capabilities()

        # Create base graph with agent name
        graph = BaseGraph(name=self.name)

        # Add agent node
        self.engine_node = EngineNodeConfig(name="agent_node", engine=main_engine)
        graph.add_node("agent_node", self.engine_node)
        graph.add_edge(START, "agent_node")

        # Determine if we need processing
        needs_processing = (
            self._has_tool_node
            or self._has_parser_node
            or (hasattr(main_engine, "tools") and main_engine.tools)
            or (hasattr(main_engine, "pydantic_tools") and main_engine.pydantic_tools)
        )

        if not needs_processing:
            # Simple case - no processing needed
            graph.add_edge("agent_node", END)
            return graph

        # SECOND: Add all processing nodes that we determined we need
        if self._has_tool_node:
            tool_config = self._get_or_create_tool_node_config(main_engine)
            graph.add_node("tool_node", tool_config)
            graph.add_edge("tool_node", END)  # Default end destination

        if self._has_parser_node:
            parser_config = self._get_or_create_parser_node_config(main_engine)
            graph.add_node("parse_output", parser_config)
            graph.add_edge("parse_output", END)  # Default end destination

        # THIRD: Add validation node and routing AFTER all target nodes exist
        validation_config = self._get_or_create_validation_node_config(main_engine)
        graph.add_node("validation", validation_config)

        # Connect agent to validation
        graph.add_edge("agent_node", "validation")

        # FOURTH: Set up routing map based on nodes that actually exist
        routing_map = {"has_errors": "agent_node"}

        if self._has_tool_node and "tool_node" in graph.nodes:
            routing_map["tool_node"] = "tool_node"

        if self._has_parser_node and "parse_output" in graph.nodes:
            routing_map["parse_output"] = "parse_output"

        # If no processing nodes exist, route to END
        if not (self._has_tool_node or self._has_parser_node):
            routing_map["no_tools"] = END

        # FINALLY: Add conditional edges with verified routing map
        graph.add_conditional_edges("validation", validation_config, routing_map)

        return graph

    def _get_or_create_tool_node_config(self, main_engine: Engine) -> ToolNodeConfig:
        """Get custom tool node config or create default one."""
        if self.tool_node_config:
            return self.tool_node_config

        return ToolNodeConfig(name="tool_node", tools=getattr(main_engine, "tools", []))

    def _get_or_create_parser_node_config(self, main_engine: Engine) -> Any:
        """Get custom parser node config or create default one."""
        if self.parser_node_config:
            return self.parser_node_config

        # TODO: Replace with actual ParseOutputNodeConfig creation
        return "parse_output_placeholder"

    def _get_or_create_validation_node_config(
        self, main_engine: Engine
    ) -> ValidationNodeConfig:
        """Get custom validation node config or create default one."""
        if self.validation_node_config:
            return self.validation_node_config

        schemas = []
        if self.structured_output_model:
            schemas = [self.structured_output_model]
        elif hasattr(main_engine, "pydantic_tools") and main_engine.pydantic_tools:
            schemas = main_engine.pydantic_tools
        elif hasattr(main_engine, "tools") and main_engine.tools:
            schemas = main_engine.tools

        return ValidationNodeConfig(
            name="validation_node",
            schemas=schemas,
            tools=getattr(main_engine, "tools", []),
            tool_routes=getattr(main_engine, "tool_routes", {}),
        )
