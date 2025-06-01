from abc import ABC, abstractmethod
from typing import Any, Dict, List, Literal, Optional, Sequence, Type, Union

from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.base import Engine
from haive.core.graph.node.engine_node import EngineNodeConfig
from haive.core.graph.node.tool_node_config import ToolNodeConfig
from haive.core.graph.node.validation_node_config import ValidationNodeConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.schema_composer import SchemaComposer
from haive.core.schema.state_schema import StateSchema
from langgraph.graph import END, START
from langgraph.graph.graph import CompiledGraph
from pydantic import BaseModel, Field, PrivateAttr, model_validator

# ============================================================================
# ABSTRACT BASE AGENT
# ============================================================================


class Agent(AgentConfig, ABC):
    """Abstract base agent class with automatic graph building and proper inheritance."""

    # Core fields that ALL agents have
    name: str = Field(
        default_factory=lambda: "Agent",
        description="Name of the agent - auto-generated from class name if not provided",
    )

    # Engine management - every agent has engines (could be empty dict)
    engines: Dict[str, Engine] = Field(
        default_factory=dict, description="Dictionary of engines this agent uses"
    )

    # Default main engine - can be None if agent uses only engines dict
    engine: Optional[Engine] = Field(
        default=None, description="Main/default engine for this agent"
    )

    # Graph - will be automatically built
    graph: Optional[BaseGraph] = Field(default=None, exclude=True)

    # Private state tracking
    _graph_built: bool = PrivateAttr(default=False)
    _compiled_graph: Optional[CompiledGraph] = PrivateAttr(default=None)
    _is_compiled: bool = PrivateAttr(default=False)

    # Schema definitions - at least one required
    state_schema: Optional[
        Union[Type[StateSchema], Type[BaseModel], Dict[str, Any]]
    ] = Field(default=None)
    input_schema: Optional[Union[Type[BaseModel], Dict[str, Any]]] = Field(default=None)
    output_schema: Optional[Union[Type[BaseModel], Dict[str, Any]]] = Field(
        default=None
    )
    config_schema: Optional[Union[Type[BaseModel], Dict[str, Any]]] = Field(
        default=None
    )

    @model_validator(mode="before")
    @classmethod
    def setup_name_and_engines(cls, values):
        """STEP 1: Set up name from class and normalize engines."""
        if not isinstance(values, dict):
            return values

        # Auto-generate name from class name if not provided
        if "name" not in values or not values["name"] or values["name"] == "Agent":
            class_name = cls.__name__
            # Convert CamelCase to readable name
            import re

            name = re.sub("([a-z0-9])([A-Z])", r"\1 \2", class_name)
            values["name"] = name

        # Handle single engine field - move to engines dict
        if "engine" in values and values["engine"] is not None:
            engine = values["engine"]

            # Initialize engines if not present
            if "engines" not in values:
                values["engines"] = {}

            # Add engine to engines dict
            if hasattr(engine, "name"):
                values["engines"][engine.name] = engine
            else:
                values["engines"]["main_engine"] = engine

        # Normalize engines field
        if "engines" in values and values["engines"] is not None:
            engines = values["engines"]

            if isinstance(engines, str):
                values["engines"] = {"main_engine": engines}
            elif isinstance(engines, list):
                engine_dict = {}
                for i, engine in enumerate(engines):
                    if hasattr(engine, "name"):
                        engine_dict[engine.name] = engine
                    else:
                        engine_dict[f"engine_{i}"] = engine
                values["engines"] = engine_dict
            elif not isinstance(engines, dict):
                if hasattr(engines, "name"):
                    values["engines"] = {engines.name: engines}
                else:
                    values["engines"] = {"main_engine": engines}

        # Ensure engines is always a dict
        if "engines" not in values:
            values["engines"] = {}

        return values

    @model_validator(mode="after")
    def setup_schemas_and_build_graph(self):
        """STEP 2: Setup schemas and build graph automatically."""
        # First, setup schemas
        if not any([self.state_schema, self.input_schema, self.output_schema]):
            if self.engines or self.engine:
                self._generate_schemas_from_engines()
            else:
                self.state_schema = SchemaComposer.create_message_state().build()

        if not self.state_schema and (self.engines or self.engine):
            self._generate_state_schema_from_engines()

        # Now build the graph automatically
        try:
            self.graph = self.build_graph()
            self._graph_built = True
        except Exception as e:
            # If graph building fails, log but don't crash
            import logging

            logging.warning(f"Failed to build graph for {self.__class__.__name__}: {e}")
            self.graph = None
            self._graph_built = False

        return self

    def _generate_schemas_from_engines(self):
        """Generate schemas from available engines using SchemaComposer."""
        engine_list = []

        if self.engine:
            engine_list.append(self.engine)

        for _engine_name, engine in self.engines.items():
            if isinstance(engine, str):
                continue
            engine_list.append(engine)

        if not engine_list:
            self.state_schema = SchemaComposer.create_message_state().build()
            return

        try:
            composer = SchemaComposer.from_components(
                engine_list, name=f"{self.__class__.__name__}State"
            )
            self.state_schema = composer.build()

            if not self.input_schema:
                input_composer = SchemaComposer.compose_input_schema(engine_list)
                if input_composer:
                    self.input_schema = input_composer.build()

            if not self.output_schema:
                output_composer = SchemaComposer.compose_output_schema(engine_list)
                if output_composer:
                    self.output_schema = output_composer.build()

        except Exception:
            self.state_schema = SchemaComposer.create_message_state().build()

    def _generate_state_schema_from_engines(self):
        """Generate only state schema from engines."""
        engine_list = []

        if self.engine:
            engine_list.append(self.engine)

        for engine in self.engines.values():
            if not isinstance(engine, str):
                engine_list.append(engine)

        if engine_list:
            try:
                composer = SchemaComposer.from_components(
                    engine_list, name=f"{self.__class__.__name__}State"
                )
                self.state_schema = composer.build()
            except Exception:
                self.state_schema = SchemaComposer.create_message_state().build()

    @property
    def main_engine(self) -> Optional[Engine]:
        """Get the main engine (prioritize engine field, then first in engines dict)."""
        if self.engine:
            return self.engine
        if self.engines:
            return next(iter(self.engines.values()))
        return None

    def _invalidate_graph(self):
        """Mark graph as needing rebuild."""
        self._graph_built = False
        self._is_compiled = False
        self.graph = None
        self._compiled_graph = None

    def _ensure_graph_built(self):
        """Ensure the graph is built. Rebuild if needed."""
        if not self._graph_built or self.graph is None:
            self.graph = self.build_graph()
            self._graph_built = True

    @abstractmethod
    def build_graph(self) -> BaseGraph:
        """Abstract method to build the agent's graph."""
        raise NotImplementedError(
            "build_graph method must be implemented by subclasses"
        )

    def rebuild_graph(self):
        """Force rebuild the graph."""
        self._invalidate_graph()
        try:
            self.graph = self.build_graph()
            self._graph_built = True
        except Exception as e:
            import logging

            logging.error(f"Failed to rebuild graph for {self.__class__.__name__}: {e}")
            raise
        return self.graph

    def create_runnable(self, **kwargs) -> CompiledGraph:
        """Create and compile the runnable with proper schema kwargs."""
        if not self.graph:
            self._ensure_graph_built()

        if not self.graph:
            raise ValueError("Graph could not be built")

        schema_kwargs = {}

        if self.input_schema:
            schema_kwargs["input"] = self.input_schema

        if self.state_schema:
            schema_kwargs["state_schema"] = self.state_schema

        if self.output_schema:
            schema_kwargs["output"] = self.output_schema

        if self.config_schema:
            schema_kwargs["config_schema"] = self.config_schema

        final_kwargs = {**schema_kwargs, **kwargs}

        langgraph = self.graph.to_langgraph(**final_kwargs)
        return langgraph.compile(**kwargs)

    def compile(self, **kwargs) -> CompiledGraph:
        """Compile the graph and cache the result."""
        if not self._is_compiled or kwargs:
            self._compiled_graph = self.create_runnable(**kwargs)
            self._is_compiled = True

        return self._compiled_graph

    def invoke(self, *args, **kwargs):
        """Invoke the compiled graph."""
        if not self._is_compiled:
            self.compile()
        return self._compiled_graph.invoke(*args, **kwargs)

    async def ainvoke(self, *args, **kwargs):
        """Asynchronously invoke the compiled graph."""
        if not self._is_compiled:
            self.compile()
        return await self._compiled_graph.ainvoke(*args, **kwargs)
