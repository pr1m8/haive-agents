# haive/core/engine/agent/base.py

"""
Base Agent class for the Haive framework.

This module provides the abstract base agent class that all agents inherit from,
including execution, state management, and persistence functionality through mixins.
"""

import logging
import re
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Literal, Optional, Tuple, Type, Union

from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.base import Engine, EngineType, InvokableEngine
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.persistence.handlers import setup_checkpointer
from haive.core.schema.schema_composer import SchemaComposer
from haive.core.schema.state_schema import StateSchema
from langchain_core.messages import BaseMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph.graph import CompiledGraph
from pydantic import BaseModel, Field, PrivateAttr, model_validator

# Import mixins
from haive.agents.base.mixins.execution_mixin import ExecutionMixin
from haive.agents.base.mixins.state_mixin import StateMixin

logger = logging.getLogger(__name__)


class Agent(InvokableEngine[BaseModel, BaseModel], ExecutionMixin, StateMixin, ABC):
    """
    Abstract base agent class that extends InvokableEngine with execution and state management.

    This class provides the foundation for all agent implementations in the Haive framework,
    combining the Engine interface with execution and state management capabilities through mixins.

    The agent lifecycle follows this initialization order:
    1. Normalize engines and setup name
    2. Subclass field syncing (hook: setup_agent())
    3. Schema generation from engines
    4. Persistence setup
    5. Graph building and compilation

    Attributes:
        engine_type: Always EngineType.AGENT for agents
        name: Agent name, auto-generated from class name if not provided
        engines: Dictionary of named engines used by this agent
        engine: Primary/main engine for the agent
        graph: The workflow graph (excluded from serialization)
        state_schema: Schema for agent state
        input_schema: Schema for agent input
        output_schema: Schema for agent output
        config_schema: Schema for agent configuration
        checkpointer: Persistence checkpointer (excluded from serialization)
        store: Optional state store (excluded from serialization)
        config: Reference to AgentConfig (excluded from serialization)
        set_schema: Whether to auto-generate schemas from engines
    """

    # Engine type for this agent
    engine_type: Literal[EngineType.AGENT] = Field(
        default=EngineType.AGENT, description="Engine type, always AGENT for agents"
    )

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
    graph: Optional[BaseGraph] = Field(
        default=None,
        exclude=True,
        description="The workflow graph (excluded from serialization)",
    )

    # Schema definitions
    state_schema: Optional[
        Union[Type[StateSchema], Type[BaseModel], Dict[str, Any]]
    ] = Field(default=None, description="Schema for agent state")
    input_schema: Optional[Union[Type[BaseModel], Dict[str, Any]]] = Field(
        default=None, description="Schema for agent input"
    )
    output_schema: Optional[Union[Type[BaseModel], Dict[str, Any]]] = Field(
        default=None, description="Schema for agent output"
    )
    config_schema: Optional[Union[Type[BaseModel], Dict[str, Any]]] = Field(
        default=None, description="Schema for agent configuration"
    )

    # Persistence fields (non-serialized)
    checkpointer: Any = Field(
        default=None,
        exclude=True,
        description="Persistence checkpointer (excluded from serialization)",
    )
    store: Optional[Any] = Field(
        default=None,
        exclude=True,
        description="Optional state store (excluded from serialization)",
    )

    # Configuration reference (non-serialized)
    config: Optional[AgentConfig] = Field(
        default=None,
        exclude=True,
        description="Reference to AgentConfig (excluded from serialization)",
    )

    # Runtime configuration
    runnable_config: Optional[RunnableConfig] = Field(
        default=None, description="Default runtime configuration"
    )

    # Verbosity for debugging
    verbose: bool = Field(default=False, description="Enable verbose logging")

    # Private state tracking
    _graph_built: bool = PrivateAttr(default=False)
    _compiled_graph: Optional[CompiledGraph] = PrivateAttr(default=None)
    _is_compiled: bool = PrivateAttr(default=False)
    _setup_complete: bool = PrivateAttr(default=False)
    _checkpoint_mode: str = PrivateAttr(default="sync")
    _app: Optional[Any] = PrivateAttr(default=None)

    # Schema control flag
    set_schema: Literal[True, False] = Field(
        default=False, description="Whether to auto-generate schemas from engines"
    )

    @model_validator(mode="before")
    @classmethod
    def normalize_engines_and_name(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """
        STEP 1: Normalize engines dict and auto-generate name.

        This validator:
        - Auto-generates agent name from class name if not provided
        - Normalizes engines into a dictionary format
        - Moves single engine to engines dict if needed
        """
        if not isinstance(values, dict):
            return values

        # Auto-generate name from class name if default or empty
        if "name" not in values or not values["name"] or values["name"] == "Agent":
            class_name = cls.__name__
            # Convert CamelCase to readable name (e.g., "SimpleAgent" -> "Simple Agent")
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
    def complete_agent_setup(self) -> "Agent":
        """
        STEP 2-5: Complete agent setup in proper order.

        This validator handles the main initialization sequence:
        2. Call subclass setup hook for field syncing
        3. Generate schemas from engines (if set_schema is True)
        4. Setup persistence (checkpointer and store)
        5. Build the initial graph
        """
        try:
            # STEP 2: Call subclass setup hook for field syncing
            self.setup_agent()

            # STEP 3: Generate schemas from engines (only if set_schema is True)
            if self.set_schema:
                self._setup_schemas()

            # STEP 4: Setup persistence
            self._setup_persistence()

            # STEP 5: Build the initial graph
            self._build_initial_graph()

            self._setup_complete = True

        except Exception as e:
            logger.error(f"Failed to setup agent {self.__class__.__name__}: {e}")
            # Don't raise - allow partial setup for better debugging

        return self

    @model_validator(mode="after")
    def ensure_basic_schema(self) -> "Agent":
        """
        Ensure we always have at least a basic state schema.

        This provides a fallback schema with messages field if no schema is defined.
        """
        if not self.state_schema:
            logger.debug(
                f"No state schema found for {self.name}, creating basic fallback"
            )
            try:
                # Try to import prebuilt MessagesState
                from haive.core.schema.prebuilt.messages_state import MessagesState

                self.state_schema = MessagesState
            except ImportError:
                # Create a very basic state schema as last resort
                from typing import List

                from langchain_core.messages import BaseMessage
                from pydantic import BaseModel

                class BasicMessagesState(BaseModel):
                    """Fallback state schema with messages field."""

                    messages: List[BaseMessage] = []

                self.state_schema = BasicMessagesState
                logger.debug(f"Created BasicMessagesState fallback for {self.name}")

        return self

    def setup_agent(self) -> None:
        """
        Hook for subclasses to perform field syncing and custom setup.

        This method is called BEFORE schema generation and graph building,
        allowing subclasses to sync fields to engines properly.

        Override this method in subclasses for custom setup logic.

        Example:
            def setup_agent(self):
                # Sync fields to engine
                if self.temperature is not None:
                    self.engine.temperature = self.temperature
                # Add engines to registry
                self.engines["main"] = self.engine
        """
        pass  # Default implementation does nothing

    def _setup_persistence(self) -> None:
        """
        Set up persistence with checkpointer and store.

        This method:
        - Sets up the checkpointer based on config
        - Configures checkpoint mode (sync/async)
        - Optionally adds a state store
        """
        # Setup checkpointer based on config
        if hasattr(self, "config") and self.config:
            # Get checkpoint mode from config
            self._checkpoint_mode = getattr(self.config, "checkpoint_mode", "sync")

            # Setup checkpointer using the handler
            self.checkpointer = setup_checkpointer(self.config)
            logger.debug(
                f"Checkpointer set up for {self.name}: {type(self.checkpointer).__name__}"
            )

            # Set default runnable config from config if not already set
            if not self.runnable_config and hasattr(self.config, "runnable_config"):
                self.runnable_config = self.config.runnable_config

            # Add store if configured
            self.store = None
            if getattr(self.config, "add_store", False):
                try:
                    from langgraph.store.base import BaseStore

                    self.store = BaseStore()
                    logger.debug("BaseStore added to agent")
                except ImportError:
                    logger.warning(
                        "Could not import BaseStore, store functionality disabled"
                    )
        else:
            # No config - use memory checkpointer as fallback
            try:
                from langgraph.checkpoint.memory import MemorySaver

                self.checkpointer = MemorySaver()
                self.store = None
                logger.debug(f"Using fallback MemorySaver for {self.name}")
            except ImportError:
                logger.error("Could not import MemorySaver, persistence disabled")
                self.checkpointer = None
                self.store = None

    def _setup_schemas(self) -> None:
        """
        Generate schemas from available engines and sub-agents with enhanced tool synchronization.

        This method creates state, input, and output schemas by analyzing
        the engines and sub-agents configured for this agent. It uses the enhanced
        SchemaComposer functionality to ensure proper tool routing and engine
        synchronization based on the tool route mixin system.
        """
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
            f"Setting up schemas for {self.name} with {len(engine_list)} engines "
            f"and {len(agent_list)} sub-agents"
        )

        try:
            # Generate state schema using enhanced SchemaComposer
            if not self.state_schema:
                if agent_list:
                    # Use AgentSchemaComposer for agents
                    logger.debug(f"Creating schema from {len(agent_list)} sub-agents")
                    try:
                        from haive.core.schema.agent_schema_composer import (
                            AgentSchemaComposer,
                        )

                        self.state_schema = AgentSchemaComposer.from_agents(
                            agents=agent_list,
                            name=f"{self.__class__.__name__}State",
                            include_meta=True,
                            separation="smart",
                        )
                    except ImportError:
                        logger.warning(
                            "AgentSchemaComposer not available, using regular composer"
                        )
                        # Use the classmethod from_components for proper schema creation
                        self.state_schema = SchemaComposer.from_components(
                            components=engine_list,
                            name=f"{self.__class__.__name__}State",
                        )
                elif engine_list:
                    # Use enhanced SchemaComposer for engines with tool routing
                    logger.debug(f"Creating schema from {len(engine_list)} engines")

                    # Use the classmethod from_components for proper schema creation
                    self.state_schema = SchemaComposer.from_components(
                        components=engine_list, name=f"{self.__class__.__name__}State"
                    )

                    logger.debug(
                        f"Built schema with enhanced tool synchronization: "
                        f"{getattr(self.state_schema, '__name__', 'Unknown')}"
                    )

                    # Log engines stored on schema class
                    if hasattr(self.state_schema, "engines"):
                        schema_engines = getattr(self.state_schema, "engines", {})
                        logger.debug(
                            f"Schema has {len(schema_engines)} class-level engines: "
                            f"{list(schema_engines.keys())}"
                        )
                else:
                    logger.debug(
                        "No engines or agents found, creating basic message state"
                    )
                    # Create basic message state
                    self._create_basic_message_state()

            # Optionally auto-derive input and output schemas
            if self.set_schema:
                self.auto_derive_schemas()

            logger.debug(f"Schema setup complete. State schema: {self.state_schema}")

        except Exception as e:
            logger.warning(
                f"Schema generation failed for {self.__class__.__name__}: {e}"
            )
            # Fallback to basic message state
            if not self.state_schema:
                self._create_basic_message_state()

    def _create_basic_message_state(self) -> None:
        """Create a basic message state schema as fallback."""
        try:
            from haive.core.schema.prebuilt.messages_state import MessagesState

            self.state_schema = MessagesState
            logger.debug("Using MessagesState fallback")
        except ImportError:
            # Create basic state schema
            from typing import List

            from langchain_core.messages import BaseMessage
            from pydantic import BaseModel

            class FallbackMessagesState(BaseModel):
                """Fallback state schema with messages field."""

                messages: List[BaseMessage] = []

            self.state_schema = FallbackMessagesState
            logger.debug("Using FallbackMessagesState")

    def _build_initial_graph(self) -> None:
        """
        Build the initial graph.

        This calls the abstract build_graph method that must be implemented by subclasses.
        """
        try:
            self.graph = self.build_graph()
            self._graph_built = True
        except Exception as e:
            logger.warning(
                f"Initial graph build failed for {self.__class__.__name__}: {e}"
            )
            self.graph = None
            self._graph_built = False

    # ============================================================================
    # ENGINE INTERFACE IMPLEMENTATION
    # ============================================================================

    def get_input_fields(self) -> Dict[str, Tuple[Type, Any]]:
        """
        Return input field definitions as field_name -> (type, default) pairs.

        This implements the abstract method from Engine base class.
        """
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
                    return first_engine.get_input_fields()
                except:
                    pass

        # Fallback - return empty to avoid exposing internal state
        return {}

    def get_output_fields(self) -> Dict[str, Tuple[Type, Any]]:
        """
        Return output field definitions as field_name -> (type, default) pairs.

        This implements the abstract method from Engine base class.
        """
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
                    return last_engine.get_output_fields()
                except:
                    pass

        # Fallback - return empty to avoid exposing internal state
        return {}

    def create_runnable(
        self, runnable_config: Optional[Dict[str, Any]] = None
    ) -> CompiledGraph:
        """
        Create and compile the runnable with proper schema kwargs.

        This implements the abstract method from Engine base class.
        """
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
            self._create_basic_message_state()

        # Build schema kwargs - only pass what StateGraph expects
        schema_kwargs = {}

        # CRITICAL FIX: Ensure state_schema is always passed
        if self.state_schema:
            schema_kwargs["state_schema"] = self.state_schema
        else:
            # This should never happen due to fallbacks above, but just in case
            raise ValueError(f"No state schema available for {self.name}")

        # Only add input/output if they exist (they're optional if state_schema is provided)
        if self.input_schema:
            schema_kwargs["input"] = self.input_schema

        if self.output_schema:
            schema_kwargs["output"] = self.output_schema

        if self.config_schema:
            schema_kwargs["config_schema"] = self.config_schema

        # Debug logging
        logger.debug(f"Schema kwargs for {self.name}: {list(schema_kwargs.keys())}")
        logger.debug(f"State schema: {self.state_schema}")

        # Convert BaseGraph to LangGraph with schemas
        try:
            langgraph = self.graph.to_langgraph(**schema_kwargs)
        except Exception as e:
            logger.error(f"Failed to convert graph to langgraph: {e}")
            logger.error(f"Schema kwargs were: {list(schema_kwargs.keys())}")
            logger.error(f"State schema type: {type(self.state_schema)}")
            raise

        # Now compile the LangGraph StateGraph with checkpointer and runtime config
        compile_kwargs = {}

        # Always add our checkpointer
        if self.checkpointer:
            compile_kwargs["checkpointer"] = self.checkpointer

        # Add store if available
        if self.store:
            compile_kwargs["store"] = self.store

        # Extract compilation-relevant parameters from runnable_config if provided
        if runnable_config:
            if "interrupt_before" in runnable_config:
                compile_kwargs["interrupt_before"] = runnable_config["interrupt_before"]
            if "interrupt_after" in runnable_config:
                compile_kwargs["interrupt_after"] = runnable_config["interrupt_after"]

        # Compile the LangGraph StateGraph
        return langgraph.compile(**compile_kwargs)

    # ============================================================================
    # GRAPH MANAGEMENT
    # ============================================================================

    @property
    def main_engine(self) -> Optional[Engine]:
        """Get the main engine (prioritize engine field, then first in engines dict)."""
        if self.engine:
            return self.engine
        if self.engines:
            return next(iter(self.engines.values()), None)
        return None

    def _invalidate_graph(self) -> None:
        """Mark graph as needing rebuild."""
        self._graph_built = False
        self._is_compiled = False
        self.graph = None
        self._compiled_graph = None

    def _ensure_graph_built(self) -> None:
        """Ensure the graph is built. Rebuild if needed."""
        if not self._graph_built or self.graph is None:
            self.graph = self.build_graph()
            self._graph_built = True

    @abstractmethod
    def build_graph(self) -> BaseGraph:
        """
        Abstract method to build the agent's graph.

        This is called after field syncing and schema generation.
        Must be implemented by all concrete agent classes.

        Returns:
            The constructed BaseGraph for this agent
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

    def regenerate_schemas(self) -> None:
        """Regenerate schemas from current engines."""
        # Clear existing schemas
        self.state_schema = None
        self.input_schema = None
        self.output_schema = None

        # Regenerate
        self._setup_schemas()

    def compile(self, **kwargs) -> CompiledGraph:
        """
        Compile the graph and cache the result.

        Args:
            **kwargs: Additional compilation arguments

        Returns:
            The compiled graph
        """
        if not self._is_compiled or kwargs:
            # Build graph if not already built
            if not hasattr(self, "graph") or self.graph is None:
                logger.debug("Building graph before compilation")
                self._ensure_graph_built()

            if not self.graph:
                raise RuntimeError("Graph not built")

            # Make sure checkpointer tables are set up if needed
            if self.checkpointer and hasattr(self.checkpointer, "setup"):
                try:
                    from haive.core.persistence.handlers import ensure_pool_open

                    ensure_pool_open(self.checkpointer)
                    self.checkpointer.setup()
                    logger.debug("Checkpointer tables set up successfully")
                except Exception as e:
                    logger.error(f"Error setting up checkpointer tables: {e}")

            # First, we need to convert BaseGraph to LangGraph StateGraph
            # Build schema kwargs for conversion
            schema_kwargs = {}

            # Ensure we have a state schema
            if not self.state_schema:
                logger.warning(
                    f"No state schema found for {self.name}, regenerating..."
                )
                self._setup_schemas()

            if not self.state_schema:
                logger.warning(f"Creating fallback state schema for {self.name}")
                self._create_basic_message_state()

            # Add schemas to kwargs
            if self.state_schema:
                schema_kwargs["state_schema"] = self.state_schema
            else:
                raise ValueError(f"No state schema available for {self.name}")

            if self.input_schema:
                schema_kwargs["input"] = self.input_schema

            if self.output_schema:
                schema_kwargs["output"] = self.output_schema

            if self.config_schema:
                schema_kwargs["config_schema"] = self.config_schema

            # Convert BaseGraph to LangGraph StateGraph
            try:
                langgraph_graph = self.graph.to_langgraph(**schema_kwargs)
                logger.debug(
                    f"Successfully converted BaseGraph to LangGraph StateGraph"
                )
            except Exception as e:
                logger.error(f"Failed to convert BaseGraph to LangGraph: {e}")
                raise

            # Now compile the LangGraph StateGraph with checkpointer and store
            compile_kwargs = kwargs.copy()

            # Add checkpointer if we have one and it's not already specified
            if self.checkpointer and "checkpointer" not in compile_kwargs:
                compile_kwargs["checkpointer"] = self.checkpointer

            # Add store if available and not already specified
            if self.store and "store" not in compile_kwargs:
                compile_kwargs["store"] = self.store

            logger.debug(
                f"Compiling LangGraph with kwargs: {list(compile_kwargs.keys())}"
            )

            # The LangGraph StateGraph.compile() method accepts checkpointer and store
            self._app = langgraph_graph.compile(**compile_kwargs)
            self._compiled_graph = self._app
            self._is_compiled = True

        if self._compiled_graph is None:
            raise RuntimeError("Failed to compile graph")

        return self._compiled_graph

    # ============================================================================
    # ENGINE INVOCATION INTERFACE
    # ============================================================================

    def invoke(self, input_data: Any, config: Optional[RunnableConfig] = None) -> Any:
        """
        Invoke the agent using ExecutionMixin's run method.

        This implements the Engine interface's invoke method.

        Args:
            input_data: Input data for the agent
            runnable_config: Optional runtime configuration

        Returns:
            Output from the agent
        """
        return self.run(input_data, config=config)

    async def ainvoke(
        self, input_data: Any, config: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Async invoke the agent using ExecutionMixin's arun method.

        This implements the Engine interface's ainvoke method.

        Args:
            input_data: Input data for the agent
            runnable_config: Optional runtime configuration

        Returns:
            Output from the agent
        """
        return await self.arun(input_data, config=config)

    # ============================================================================
    # UTILITY METHODS
    # ============================================================================

    def __repr__(self) -> str:
        """String representation of the agent."""
        engine_count = len(self.engines)
        main_engine = self.main_engine
        engine_type = type(main_engine).__name__ if main_engine else "None"
        return f"{self.__class__.__name__}(name='{self.name}', engines={engine_count}, main_engine={engine_type})"

    def get_all_tools(self) -> List[Any]:
        """
        Collect all tools from all engines and state schema.

        Returns:
            List of all tools available across all engines and state schema
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

        # Get tools from state schema if available
        state_tools = self.get_state_tools()
        if state_tools:
            tools.extend(state_tools)

        # Get tools from class-level engines in state schema
        class_engines = self.get_all_class_engines()
        for engine in class_engines.values():
            if hasattr(engine, "tools"):
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

        logger.debug(
            f"Agent {self.name} collected {len(unique_tools)} unique tools from all sources"
        )
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

    def visualize_graph(self, output_path: Optional[str] = None) -> None:
        """
        Generate and save a visualization of the agent's graph.

        Args:
            output_path: Optional custom path for visualization output
        """
        if not self._app:
            logger.warning("Cannot visualize graph: Not compiled yet")
            return

        try:
            import os
            from datetime import datetime

            if not output_path:
                # Use default path
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_dir = "resources/graph_images"
                os.makedirs(output_dir, exist_ok=True)
                output_path = os.path.join(output_dir, f"{self.name}_{timestamp}.png")

            # Generate the visualization
            png_data = self._app.get_graph(xray=True).draw_mermaid_png()

            # Save the PNG data
            with open(output_path, "wb") as f:
                f.write(png_data)

            logger.info(f"Graph visualization saved to: {output_path}")

        except Exception as e:
            logger.error(f"Error visualizing graph: {e}")

    # ============================================================================
    # ENGINE ACCESS METHODS (StateSchema-compatible interface)
    # ============================================================================

    def get_class_engine(self, name: str) -> Optional[Engine]:
        """
        Get a class-level engine by name from the state schema.

        Args:
            name: Name of the engine to retrieve

        Returns:
            Engine instance if found, None otherwise
        """
        if self.state_schema and hasattr(self.state_schema, "get_class_engine"):
            return self.state_schema.get_class_engine(name)
        return None

    def get_all_class_engines(self) -> Dict[str, Engine]:
        """
        Get all class-level engines from the state schema.

        Returns:
            Dictionary of all engines
        """
        if self.state_schema and hasattr(self.state_schema, "get_all_class_engines"):
            return self.state_schema.get_all_class_engines()
        return {}

    def get_instance_engine(self, name: str) -> Optional[Engine]:
        """
        Get an engine from instance or class level (via state schema).

        Args:
            name: Name of the engine to retrieve

        Returns:
            Engine instance if found, None otherwise
        """
        # First check agent's own engines
        if name in self.engines:
            return self.engines[name]

        # Check main engine
        if self.engine and getattr(self.engine, "name", None) == name:
            return self.engine

        # Then check state schema engines
        if self.state_schema and hasattr(self.state_schema, "get_instance_engine"):
            return self.state_schema.get_instance_engine(name)

        return None

    def get_all_instance_engines(self) -> Dict[str, Engine]:
        """
        Get all engines from both instance and class level.

        Returns:
            Dictionary mapping engine names to engine instances
        """
        engines = {}

        # Get engines from state schema first
        if self.state_schema and hasattr(self.state_schema, "get_all_instance_engines"):
            engines.update(self.state_schema.get_all_instance_engines())

        # Add agent's own engines (may override schema engines)
        engines.update(self.engines)

        # Add main engine if it has a name
        if self.engine and hasattr(self.engine, "name") and self.engine.name:
            engines[self.engine.name] = self.engine

        return engines

    def has_engine(self, name: str) -> bool:
        """
        Check if an engine exists in this agent.

        Args:
            name: Name of the engine to check

        Returns:
            True if engine exists, False otherwise
        """
        return self.get_instance_engine(name) is not None

    def add_tool_to_state(
        self,
        tool: Any,
        route: Optional[str] = None,
        target_engine: Optional[str] = None,
    ) -> None:
        """
        Add a tool to the agent's state schema if it supports tools.

        Args:
            tool: Tool to add
            route: Optional explicit route/type
            target_engine: Optional specific engine name to add tool to
        """
        # Create a state instance to add the tool
        if self.state_schema:
            try:
                # Create a temporary state instance
                state_instance = self.state_schema()

                # Check if state supports tools
                if hasattr(state_instance, "add_tool"):
                    if target_engine:
                        state_instance.add_tool_to_engine(tool, target_engine, route)
                    else:
                        state_instance.add_tool(tool, route, target_engine)
                    logger.debug(
                        f"Added tool to state schema: {getattr(tool, 'name', str(tool))}"
                    )
                else:
                    logger.warning(
                        f"State schema {self.state_schema.__name__} does not support tools"
                    )
            except Exception as e:
                logger.error(f"Failed to add tool to state: {e}")

    def configure_engine_routes(self, engine_type: str, routes: List[str]) -> None:
        """
        Configure which tool routes an engine type should accept in the state schema.

        Args:
            engine_type: The engine type (e.g., 'llm', 'retriever', etc.)
            routes: List of tool routes this engine type should accept
        """
        if self.state_schema:
            try:
                # Create a temporary state instance
                state_instance = self.state_schema()

                # Check if state supports route configuration
                if hasattr(state_instance, "configure_engine_routes"):
                    state_instance.configure_engine_routes(engine_type, routes)
                    logger.debug(
                        f"Configured routes for engine type '{engine_type}': {routes}"
                    )
                else:
                    logger.warning(
                        f"State schema {self.state_schema.__name__} does not support route configuration"
                    )
            except Exception as e:
                logger.error(f"Failed to configure engine routes: {e}")

    def get_state_tools(self) -> List[Any]:
        """
        Get all tools from the state schema if it supports tools.

        Returns:
            List of tools from the state schema, empty list if not supported
        """
        if self.state_schema:
            try:
                # Create a temporary state instance
                state_instance = self.state_schema()

                # Check if state has tools
                if hasattr(state_instance, "tools"):
                    return getattr(state_instance, "tools", [])
            except Exception as e:
                logger.error(f"Failed to get state tools: {e}")

        return []

    def sync_tools_to_engines(self) -> None:
        """
        Manually trigger tool synchronization to engines in the state schema.
        """
        if self.state_schema:
            try:
                # Create a temporary state instance
                state_instance = self.state_schema()

                # Check if state supports tool syncing
                if hasattr(state_instance, "_sync_tools_to_engines_by_route"):
                    state_instance._sync_tools_to_engines_by_route()
                    logger.debug("Manually triggered tool synchronization to engines")
                else:
                    logger.warning(
                        f"State schema {self.state_schema.__name__} does not support tool syncing"
                    )
            except Exception as e:
                logger.error(f"Failed to sync tools to engines: {e}")

    def get_schema_info(self) -> Dict[str, Any]:
        """
        Get comprehensive information about the agent's schema system.

        Returns:
            Dictionary containing schema information including engines, tools, and capabilities
        """
        info = {
            "agent_name": self.name,
            "agent_engines": list(self.engines.keys()),
            "main_engine": getattr(self.engine, "name", None) if self.engine else None,
            "state_schema": {
                "name": (
                    getattr(self.state_schema, "__name__", None)
                    if self.state_schema
                    else None
                ),
                "class_engines": [],
                "supports_tools": False,
                "supports_routing": False,
                "tools_count": 0,
            },
            "total_engines": 0,
            "total_tools": 0,
        }

        # Get class-level engines from state schema
        class_engines = self.get_all_class_engines()
        info["state_schema"]["class_engines"] = list(class_engines.keys())

        # Check if state schema supports tools and routing
        if self.state_schema:
            try:
                state_instance = self.state_schema()
                info["state_schema"]["supports_tools"] = hasattr(
                    state_instance, "tools"
                )
                info["state_schema"]["supports_routing"] = hasattr(
                    state_instance, "tool_routes"
                )

                if hasattr(state_instance, "tools"):
                    info["state_schema"]["tools_count"] = len(
                        getattr(state_instance, "tools", [])
                    )
            except Exception as e:
                logger.debug(f"Could not analyze state schema: {e}")

        # Count total engines and tools
        all_engines = self.get_all_instance_engines()
        info["total_engines"] = len(all_engines)
        info["total_tools"] = len(self.get_all_tools())

        return info

    def display_schema_info(self) -> None:
        """
        Display comprehensive information about the agent's schema system.
        """
        info = self.get_schema_info()

        print(f"\n=== Agent Schema Information: {info['agent_name']} ===")
        print(f"Agent Engines: {info['agent_engines']}")
        print(f"Main Engine: {info['main_engine']}")

        print(f"\nState Schema: {info['state_schema']['name']}")
        print(f"  Class-level Engines: {info['state_schema']['class_engines']}")
        print(f"  Supports Tools: {info['state_schema']['supports_tools']}")
        print(f"  Supports Routing: {info['state_schema']['supports_routing']}")
        print(f"  Tools Count: {info['state_schema']['tools_count']}")

        print(f"\nTotals:")
        print(f"  Total Engines: {info['total_engines']}")
        print(f"  Total Tools: {info['total_tools']}")

        # Show schema information
        print(f"\nSchema Information:")
        print(
            f"  Input Schema: {getattr(self.input_schema, '__name__', 'None') if self.input_schema else 'None'}"
        )
        print(
            f"  Output Schema: {getattr(self.output_schema, '__name__', 'None') if self.output_schema else 'None'}"
        )
        print(
            f"  Config Schema: {getattr(self.config_schema, '__name__', 'None') if self.config_schema else 'None'}"
        )

        # Show derived schema capabilities
        if self.state_schema and hasattr(self.state_schema, "derive_input_schema"):
            print(f"  Can derive input schema: ✅")
        else:
            print(f"  Can derive input schema: ❌")

        if self.state_schema and hasattr(self.state_schema, "derive_output_schema"):
            print(f"  Can derive output schema: ✅")
        else:
            print(f"  Can derive output schema: ❌")

        # Show engine details
        all_engines = self.get_all_instance_engines()
        if all_engines:
            print(f"\nAll Available Engines:")
            for name, engine in all_engines.items():
                engine_type = getattr(engine, "engine_type", "unknown")
                tool_count = len(getattr(engine, "tools", []))
                print(f"  - {name}: {engine_type} ({tool_count} tools)")

    def derive_input_schema(
        self, engine_name: Optional[str] = None, name: Optional[str] = None
    ) -> Optional[Type[BaseModel]]:
        """
        Derive input schema from the agent's state schema.

        Args:
            engine_name: Optional name of the engine to target (default: all inputs)
            name: Optional name for the schema class

        Returns:
            A BaseModel subclass for input validation, or None if state schema doesn't support it
        """
        if not self.state_schema:
            logger.warning("No state schema available to derive input schema from")
            return None

        # Check if state schema has derive_input_schema method
        if hasattr(self.state_schema, "derive_input_schema"):
            try:
                schema_name = name or f"{self.name}InputSchema"
                return self.state_schema.derive_input_schema(
                    engine_name=engine_name, name=schema_name
                )
            except Exception as e:
                logger.error(f"Failed to derive input schema: {e}")
                return None
        else:
            logger.warning(
                f"State schema {getattr(self.state_schema, '__name__', 'Unknown')} does not support input schema derivation"
            )
            return None

    def derive_output_schema(
        self, engine_name: Optional[str] = None, name: Optional[str] = None
    ) -> Optional[Type[BaseModel]]:
        """
        Derive output schema from the agent's state schema.

        Args:
            engine_name: Optional name of the engine to target (default: all outputs)
            name: Optional name for the schema class

        Returns:
            A BaseModel subclass for output validation, or None if state schema doesn't support it
        """
        if not self.state_schema:
            logger.warning("No state schema available to derive output schema from")
            return None

        # Check if state schema has derive_output_schema method
        if hasattr(self.state_schema, "derive_output_schema"):
            try:
                schema_name = name or f"{self.name}OutputSchema"
                return self.state_schema.derive_output_schema(
                    engine_name=engine_name, name=schema_name
                )
            except Exception as e:
                logger.error(f"Failed to derive output schema: {e}")
                return None
        else:
            logger.warning(
                f"State schema {getattr(self.state_schema, '__name__', 'Unknown')} does not support output schema derivation"
            )
            return None

    def auto_derive_schemas(self) -> None:
        """
        Automatically derive and set input and output schemas from the state schema.

        This convenience method will derive input and output schemas from the state schema
        and set them on the agent if they haven't been explicitly set.
        """
        # Only derive if not already set
        if not self.input_schema:
            derived_input = self.derive_input_schema()
            if derived_input:
                self.input_schema = derived_input
                logger.debug(f"Auto-derived input schema: {derived_input.__name__}")

        if not self.output_schema:
            derived_output = self.derive_output_schema()
            if derived_output:
                self.output_schema = derived_output
                logger.debug(f"Auto-derived output schema: {derived_output.__name__}")

    def get_derived_schemas(self) -> Dict[str, Optional[Type[BaseModel]]]:
        """
        Get all derived schemas (input and output) from the state schema.

        Returns:
            Dictionary containing derived input and output schemas
        """
        return {
            "input_schema": self.derive_input_schema(),
            "output_schema": self.derive_output_schema(),
            "state_schema": self.state_schema,
        }
