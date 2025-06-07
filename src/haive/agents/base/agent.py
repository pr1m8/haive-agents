# haive/core/engine/agent/base.py

import logging
import re
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Literal, Optional, Tuple, Type, Union

from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.base import Engine, EngineType, InvokableEngine
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.schema.schema_composer import SchemaComposer
from haive.core.schema.state_schema import StateSchema
from langchain_core.messages import BaseMessage
from langgraph.graph.graph import CompiledGraph
from pydantic import BaseModel, Field, PrivateAttr, model_validator

logger = logging.getLogger(__name__)


class Agent(InvokableEngine[BaseModel, BaseModel], ABC):
    """
    Abstract base agent class that extends InvokableEngine.

    This class is now an Engine itself, providing consistent interface
    with the rest of the Haive framework.

    Initialization Order:
    1. Normalize engines and setup name
    2. Subclass field syncing (hook: setup_agent())
    3. Schema generation from engines
    4. Graph building
    """

    # Engine type for this agent
    engine_type: EngineType = Field(default=EngineType.AGENT)

    # Core identification
    name: str = Field(
        default="Agent",
        description="Name of the agent - auto-generated from class name if not provided",
    )

    # Engine management
    engines: Dict[str, Engine] = Field(
        default_factory=dict, description="Dictionary of engines this agent uses"
    )

    engine: Optional[Engine] = Field(
        default=None, description="Main/default engine for this agent"
    )

    # Graph state - will be built after setup
    graph: Optional[BaseGraph] = Field(default=None, exclude=True)

    # Schema definitions
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

    # Private state tracking
    _graph_built: bool = PrivateAttr(default=False)
    _compiled_graph: Optional[CompiledGraph] = PrivateAttr(default=None)
    _is_compiled: bool = PrivateAttr(default=False)
    _setup_complete: bool = PrivateAttr(default=False)

    # Schema control flag
    set_schema: Literal[True, False] = Field(default=False)

    @model_validator(mode="before")
    @classmethod
    def normalize_engines_and_name(cls, values):
        """STEP 1: Normalize engines dict and auto-generate name."""
        if not isinstance(values, dict):
            return values

        # Auto-generate name from class name if default or empty
        if "name" not in values or not values["name"] or values["name"] == "Agent":
            class_name = cls.__name__
            # Convert CamelCase to readable name
            name = re.sub("([a-z0-9])([A-Z])", r"\1 \2", class_name)
            values["name"] = name

        # Initialize engines dict if not present
        if "engines" not in values:
            values["engines"] = {}

        # Move single engine to engines dict
        if "engine" in values and values["engine"] is not None:
            engine = values["engine"]

            # Add to engines dict with appropriate key
            if hasattr(engine, "name") and engine.name:
                values["engines"][engine.name] = engine
            else:
                values["engines"]["main"] = engine

        # Normalize engines field to always be a dict
        if "engines" in values and values["engines"] is not None:
            engines = values["engines"]

            if isinstance(engines, (list, tuple)):
                # Convert list/tuple to dict
                engine_dict = {}
                for i, engine in enumerate(engines):
                    if hasattr(engine, "name") and engine.name:
                        engine_dict[engine.name] = engine
                    else:
                        engine_dict[f"engine_{i}"] = engine
                values["engines"] = engine_dict

            elif not isinstance(engines, dict):
                # Single engine not in dict form
                if hasattr(engines, "name") and engines.name:
                    values["engines"] = {engines.name: engines}
                else:
                    values["engines"] = {"main": engines}

        return values

    @model_validator(mode="after")
    def complete_agent_setup(self):
        """STEP 2-4: Complete agent setup in proper order."""
        try:
            # STEP 2: Call subclass setup hook for field syncing
            self.setup_agent()

            # STEP 3: Generate schemas from engines (only if set_schema is True)
            if self.set_schema:
                self._setup_schemas()

            # STEP 4: Build the graph
            self._build_initial_graph()

            self._setup_complete = True

        except Exception as e:
            logger.error(f"Failed to setup agent {self.__class__.__name__}: {e}")
            # Don't raise - allow partial setup

        return self

    @model_validator(mode="after")
    def ensure_basic_schema(self):
        """Ensure we always have at least a basic state schema."""
        if not self.state_schema:
            logger.debug(
                f"No state schema found for {self.name}, creating basic fallback"
            )
            try:
                from haive.core.schema.prebuilt.messages_state import MessagesState

                self.state_schema = SchemaComposer.from_components(
                    components=[self.engine], name=f"{self.__class__.__name__}State"
                )
            except ImportError:
                # Create a very basic state schema as last resort
                from typing import List

                from langchain_core.messages import BaseMessage
                from pydantic import BaseModel

                class InitialBasicMessagesState(BaseModel):
                    messages: List[BaseMessage] = []

                self.state_schema = InitialBasicMessagesState
                logger.debug(
                    f"Created InitialBasicMessagesState fallback for {self.name}"
                )

        return self

    def setup_agent(self):
        """
        Hook for subclasses to perform field syncing and custom setup.

        This is called BEFORE schema generation and graph building,
        allowing subclasses to sync fields to engines properly.

        Override this method in subclasses for custom setup logic.
        """
        pass  # Default implementation does nothing

    # ============================================================================
    # ENGINE INTERFACE IMPLEMENTATION
    # ============================================================================

    def get_input_fields(self) -> Dict[str, Tuple[Type, Any]]:
        """Return input field definitions as field_name -> (type, default) pairs."""
        # Only return from input schema if explicitly defined and it's a BaseModel
        if (
            self.input_schema
            and not isinstance(self.input_schema, dict)
            and hasattr(self.input_schema, "model_fields")
        ):
            result = {}
            for name, field_info in self.input_schema.model_fields.items():
                field_type = field_info.annotation or Any
                default_value = (
                    field_info.default if field_info.default is not ... else None
                )
                result[name] = (field_type, default_value)
            return result

        # If no explicit input schema, try to get from first engine
        if self.engines:
            # Get the first engine (in order of declaration)
            first_engine = next(iter(self.engines.values()), None)
            if first_engine and hasattr(first_engine, "get_input_fields"):
                try:
                    self.input_schema = first_engine.get_input_fields()
                    return first_engine.get_input_fields()
                except:
                    pass

        # Fallback - return empty to avoid exposing internal state
        return {}

    def get_output_fields(self) -> Dict[str, Tuple[Type, Any]]:
        """Return output field definitions as field_name -> (type, default) pairs."""
        # Only return from output schema if explicitly defined and it's a BaseModel
        if (
            self.output_schema
            and not isinstance(self.output_schema, dict)
            and hasattr(self.output_schema, "model_fields")
        ):
            result = {}
            for name, field_info in self.output_schema.model_fields.items():
                field_type = field_info.annotation or Any
                default_value = (
                    field_info.default if field_info.default is not ... else None
                )
                result[name] = (field_type, default_value)
            return result

        # If no explicit output schema, try to get from last engine
        if self.engines:
            # Get the last engine
            last_engine = list(self.engines.values())[-1] if self.engines else None
            if last_engine and hasattr(last_engine, "get_output_fields"):
                try:
                    self.output_schema = last_engine.get_output_fields()
                    return last_engine.get_output_fields()
                except:
                    pass

        # Fallback - return empty to avoid exposing internal state
        return {}

    def create_runnable(self, runnable_config=None) -> CompiledGraph:
        """Create and compile the runnable with proper schema kwargs."""
        if not self._setup_complete:
            raise RuntimeError("Agent setup not complete")

        if not self.graph:
            self._ensure_graph_built()

        if not self.graph:
            raise ValueError("Graph could not be built")

        # Ensure we have a state schema - regenerate if needed
        if not self.state_schema:
            logger.warning(f"No state schema found for {self.name}, regenerating...")
            self._setup_schemas()

        # If still no state schema, create a basic one
        if not self.state_schema:
            logger.warning(f"Creating fallback state schema for {self.name}")
            try:
                from haive.core.schema.prebuilt.messages_state import MessagesState

                self.state_schema = MessagesState
                logger.debug("Using MessagesState fallback")
            except ImportError:
                # Create basic state schema
                from typing import List

                from langchain_core.messages import BaseMessage
                from pydantic import BaseModel

                class BasicAgentState(BaseModel):
                    messages: List[BaseMessage] = []

                self.state_schema = BasicAgentState
                logger.debug(f"Created BasicAgentState fallback for {self.name}")

        # Build schema kwargs - only pass what StateGraph expects
        schema_kwargs = {}

        if self.state_schema:
            schema_kwargs["state_schema"] = self.state_schema

        if self.input_schema:
            schema_kwargs["input"] = self.input_schema

        if self.output_schema:
            schema_kwargs["output"] = self.output_schema

        if self.config_schema:
            schema_kwargs["config_schema"] = self.config_schema

        # Debug logging
        logger.debug(f"Schema kwargs for {self.name}: {list(schema_kwargs.keys())}")
        logger.debug(f"State schema: {self.state_schema}")

        # Convert to LangGraph with only schema kwargs
        langgraph = self.graph.to_langgraph(**schema_kwargs)

        # Apply runnable_config during compilation if provided
        compile_kwargs = {}
        if runnable_config:
            # Extract compilation-relevant parameters from runnable_config
            if "checkpointer" in runnable_config:
                compile_kwargs["checkpointer"] = runnable_config["checkpointer"]
            if "interrupt_before" in runnable_config:
                compile_kwargs["interrupt_before"] = runnable_config["interrupt_before"]
            if "interrupt_after" in runnable_config:
                compile_kwargs["interrupt_after"] = runnable_config["interrupt_after"]

        return langgraph.compile(**compile_kwargs)

    # ============================================================================
    # FIXED AGENT SCHEMA SETUP
    # ============================================================================
    def _setup_schemas(self):
        """Generate schemas from available engines and sub-agents."""

        # Collect all engines and agents
        engine_list = []
        agent_list = []

        if self.engine:
            engine_list.append(self.engine)

        for name, component in self.engines.items():
            if isinstance(component, str):  # Skip string references
                continue
            elif isinstance(component, Agent):
                # It's a sub-agent
                agent_list.append(component)
            else:
                # It's an engine
                engine_list.append(component)

        logger.debug(
            f"Setting up schemas for {self.name} with {len(engine_list)} engines and {len(agent_list)} sub-agents"
        )

        try:
            # Generate state schema
            if not self.state_schema:
                if agent_list:
                    # Use AgentSchemaComposer for agents
                    logger.debug(f"Creating schema from {len(agent_list)} sub-agents")
                    from haive.core.schema.agent_schema_composer import (
                        AgentSchemaComposer,
                    )

                    self.state_schema = AgentSchemaComposer.from_agents(
                        agents=agent_list,
                        name=f"{self.__class__.__name__}State",
                        include_meta=True,
                        separation="smart",
                    )
                elif engine_list:
                    # Use regular SchemaComposer for engines
                    logger.debug(f"Creating schema from {len(engine_list)} engines")
                    self.state_schema = SchemaComposer.from_components(
                        components=engine_list, name=f"{self.__class__.__name__}State"
                    )
                else:
                    logger.debug(
                        "No engines or agents found, creating basic message state"
                    )
                    # Create basic message state
                    try:
                        from haive.core.schema.prebuilt.messages_state import (
                            MessagesState,
                        )

                        self.state_schema = MessagesState
                    except ImportError:
                        # Create basic state schema
                        from typing import List

                        from langchain_core.messages import BaseMessage
                        from pydantic import BaseModel

                        class SchemaGenerationFallbackState(BaseModel):
                            messages: List[BaseMessage] = []

                        self.state_schema = SchemaGenerationFallbackState
                        logger.debug("Using SchemaGenerationFallbackState fallback")

            logger.debug(f"Schema setup complete. State schema: {self.state_schema}")

        except Exception as e:
            logger.warning(
                f"Schema generation failed for {self.__class__.__name__}: {e}"
            )
            # Fallback to basic message state
            if not self.state_schema:
                try:
                    from haive.core.schema.prebuilt.messages_state import MessagesState

                    self.state_schema = MessagesState
                    logger.debug("Using MessagesState fallback")
                except ImportError:
                    # Create basic state schema
                    from typing import List

                    from langchain_core.messages import BaseMessage
                    from pydantic import BaseModel

                    class SchemaGenerationFallbackState(BaseModel):
                        messages: List[BaseMessage] = []

                    self.state_schema = SchemaGenerationFallbackState
                    logger.debug("Using SchemaGenerationFallbackState fallback")

    def _build_initial_graph(self):
        """Build the initial graph."""
        try:
            self.graph = self.build_graph()
            self._graph_built = True
        except Exception as e:
            logger.warning(
                f"Initial graph build failed for {self.__class__.__name__}: {e}"
            )
            self.graph = None
            self._graph_built = False

    @property
    def main_engine(self) -> Optional[Engine]:
        """Get the main engine (prioritize engine field, then first in engines dict)."""
        if self.engine:
            return self.engine
        if self.engines:
            return next(iter(self.engines.values()), None)
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
        """
        Abstract method to build the agent's graph.

        This is called after field syncing and schema generation.
        """
        raise NotImplementedError(
            "build_graph method must be implemented by subclasses"
        )

    def rebuild_graph(self) -> BaseGraph:
        """Force rebuild the graph."""
        self._invalidate_graph()
        try:
            self.graph = self.build_graph()
            self._graph_built = True
        except Exception as e:
            logger.error(f"Failed to rebuild graph for {self.__class__.__name__}: {e}")
            raise
        return self.graph

    def regenerate_schemas(self):
        """Regenerate schemas from current engines."""
        # Clear existing schemas
        self.state_schema = None
        self.input_schema = None
        self.output_schema = None

        # Regenerate
        self._setup_schemas()

    def compile(self, **kwargs) -> CompiledGraph:
        """Compile the graph and cache the result."""
        if not self._is_compiled or kwargs:
            compiled_graph = self.create_runnable(**kwargs)
            self._compiled_graph = compiled_graph
            self._is_compiled = True

        if self._compiled_graph is None:
            raise RuntimeError("Failed to compile graph")

        return self._compiled_graph

    def invoke(self, *args, **kwargs):
        """Invoke the compiled graph."""
        if not self._is_compiled:
            self.compile()

        if self._compiled_graph is None:
            raise RuntimeError("Graph not compiled")

        return self._compiled_graph.invoke(*args, **kwargs)

    async def ainvoke(self, *args, **kwargs):
        """Asynchronously invoke the compiled graph."""
        if not self._is_compiled:
            self.compile()

        if self._compiled_graph is None:
            raise RuntimeError("Graph not compiled")

        return await self._compiled_graph.ainvoke(*args, **kwargs)

    def __repr__(self) -> str:
        engine_count = len(self.engines)
        main_engine = self.main_engine
        engine_type = type(main_engine).__name__ if main_engine else "None"
        return f"{self.__class__.__name__}(name='{self.name}', engines={engine_count}, main_engine={engine_type})"

    def get_all_tools(self) -> List[Any]:
        """
        Collect all tools from all engines.

        Returns:
            List of all tools available across all engines
        """
        tools = []

        # Get tools from main engine
        if self.engine and hasattr(self.engine, "tools"):
            engine_tools = getattr(self.engine, "tools", None)
            if engine_tools:
                tools.extend(engine_tools)

        # Get tools from all engines
        for engine in self.engines.values():
            if not isinstance(engine, str) and hasattr(engine, "tools"):
                engine_tools = getattr(engine, "tools", None)
                if engine_tools:
                    tools.extend(engine_tools)

        # Remove duplicates while preserving order
        seen = set()
        unique_tools = []
        for tool in tools:
            # Use tool name or id for deduplication
            tool_id = getattr(tool, "name", getattr(tool, "__name__", id(tool)))
            if tool_id not in seen:
                seen.add(tool_id)
                unique_tools.append(tool)

        logger.debug(f"Agent {self.name} collected {len(unique_tools)} unique tools")
        return unique_tools

    def get_all_tool_schemas(self) -> List[Any]:
        """
        Collect all tool schemas from engines for validation.

        Returns:
            List of tool schemas/classes for validation
        """
        schemas = []
        tools = self.get_all_tools()

        for tool in tools:
            # Add the tool class itself if it's a Pydantic model
            if isinstance(tool, type) and issubclass(tool, BaseModel):
                schemas.append(tool)
            # Check if tool has a schema attribute
            elif hasattr(tool, "args_schema") and tool.args_schema:
                schemas.append(tool.args_schema)
            # Check if tool has structured_output_model
            elif (
                hasattr(tool, "structured_output_model")
                and tool.structured_output_model
            ):
                schemas.append(tool.structured_output_model)

        logger.debug(f"Agent {self.name} collected {len(schemas)} tool schemas")
        return schemas
