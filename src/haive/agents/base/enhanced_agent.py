# haive/agents/base/enhanced_agent.py

"""Enhanced Agent hierarchy with engine-focused generics and backward compatibility.

This module provides the enhanced agent architecture:
- Workflow: Pure orchestration without LLM
- Agent: Workflow + Engine (generic on engine type)
- MultiAgent: Agent + multi-agent coordination

Key features:
- Engine-centric generics: Agent[EngineT]
- Full backward compatibility with existing code
- Clear separation of concerns: orchestration vs LLM vs coordination
- Type safety when needed, flexibility when desired
"""

import logging
import re
from abc import ABC, abstractmethod
from typing import Any, Generic, Literal, TypeVar

from haive.core.engine.base import Engine, EngineType, InvokableEngine
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from langchain_core.runnables import RunnableConfig
from langgraph.graph.graph import CompiledGraph
from pydantic import BaseModel, Field, PrivateAttr, model_validator

from haive.agents.base.agent_structured_output_mixin import StructuredOutputMixin

# Import mixins from existing agent
from haive.agents.base.mixins.execution_mixin import ExecutionMixin
from haive.agents.base.mixins.persistence_mixin import PersistenceMixin
from haive.agents.base.mixins.state_mixin import StateMixin
from haive.agents.base.serialization_mixin import SerializationMixin

logger = logging.getLogger(__name__)

# Generic type variables with defaults (PEP 696)
try:
    from typing_extensions import TypeVar
except ImportError:
    from typing import TypeVar

# ENGINE FOCUSED with defaults
EngineT = TypeVar("EngineT", bound=InvokableEngine)


# Create a custom InvokableEngine that accepts our EngineT
class TypedInvokableEngine(InvokableEngine[BaseModel, BaseModel], Generic[EngineT]):
    """InvokableEngine that's parameterized by the engine type."""


# ========================================================================
# 1. WORKFLOW - Pure orchestration, no engine
# ========================================================================


class Workflow(BaseModel, ABC):
    """Pure workflow orchestration without engine dependencies.

    Workflow handles pure orchestration - routing, transformation,
    coordination - without requiring engines. This is the foundation.

    Examples:
        class DataProcessor(Workflow):
            async def execute(self, data):
                # Pure processing, no LLM
                return processed_data

        class Router(Workflow):
            async def execute(self, request):
                # Route to appropriate handler
                return route_decision
    """

    # Core identification
    name: str = Field(default="Workflow", description="Name of the workflow")

    # Runtime config
    verbose: bool = Field(default=False, description="Enable verbose logging")
    debug: bool = Field(default=False, description="Enable debug mode")

    @model_validator(mode="before")
    @classmethod
    def auto_generate_name(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Auto-generate workflow name from class name if not provided."""
        if not isinstance(values, dict):
            return values

        if "name" not in values or not values["name"] or values["name"] == "Workflow":
            class_name = cls.__name__
            # Convert CamelCase to readable name
            name = re.sub("([a-z0-9])([A-Z])", r"\1 \2", class_name)
            values["name"] = name

        return values

    @abstractmethod
    async def execute(self, input_data: Any) -> Any:
        """Execute the workflow logic."""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"


# ========================================================================
# 2. AGENT - Workflow + Engine (GENERIC ON ENGINE)
# ========================================================================


class Agent(
    TypedInvokableEngine[EngineT],  # Engine interface with our generic parameter
    ExecutionMixin,  # Execution capabilities
    StateMixin,  # State management
    PersistenceMixin,  # Persistence capabilities
    SerializationMixin,  # Serialization support
    StructuredOutputMixin,  # Structured output support
    ABC,  # Abstract base class (must be last)
):
    """Enhanced Agent with engine-focused generics and full backward compatibility.

    Agent = Workflow + Engine. The engine type is the primary generic parameter,
    enabling type-safe engine-specific functionality while maintaining full
    backward compatibility.

    Generic Parameters:
        EngineT: Type of engine (defaults to InvokableEngine for backward compatibility)

    Key Benefits:
        - Engine-specific type safety: Agent[AugLLMConfig] vs Agent[ReactEngine]
        - Backward compatible: existing Agent() calls work unchanged
        - Engine-specific methods: BaseRAGAgent[RetrieverEngine] gets retriever methods
        - Flexible composition: Any engine type can be used

    Examples:
        # Backward compatible - works unchanged
        agent = SimpleAgent(name="test")

        # Engine-specific typing
        aug_agent: SimpleAgent[AugLLMConfig] = SimpleAgent(engine=aug_config)
        rag_agent: BaseRAGAgent[RetrieverEngine] = BaseRAGAgent(engine=retriever_engine)

        # Mixed usage - all compatible
        agents = [agent, aug_agent, rag_agent]
    """

    # Engine type marker
    engine_type: Literal[EngineType.AGENT] = Field(
        default=EngineType.AGENT, description="Engine type, always AGENT"
    )

    # Engine management - CORE GENERIC FIELD
    engines: dict[str, Engine] = Field(
        default_factory=dict, description="Dictionary of engines this agent uses"
    )

    engine: EngineT | None = Field(
        default=None, description="Main engine (determines agent type)"
    )

    # Graph and state management
    graph: BaseGraph | None = Field(
        default=None,
        exclude=True,
        description="The workflow graph (excluded from serialization)",
    )

    # Schema definitions (enhanced for type safety)
    state_schema: type[BaseModel] | dict[str, Any] | None = Field(
        default=None, exclude=True, description="Schema for agent state"
    )
    input_schema: type[BaseModel] | dict[str, Any] | None = Field(
        default=None, exclude=True, description="Schema for agent input"
    )
    output_schema: type[BaseModel] | dict[str, Any] | None = Field(
        default=None, exclude=True, description="Schema for agent output"
    )
    use_prebuilt_base: bool = Field(
        default=False,
        description="Whether to use the state_schema as a base for composition",
    )

    # Persistence fields (same as original for compatibility)
    checkpointer: Any = Field(
        default=None,
        exclude=True,
        description="Persistence checkpointer (excluded from serialization)",
    )
    store: Any | None = Field(
        default=None,
        exclude=True,
        description="Optional state store (excluded from serialization)",
    )

    persistence: Any | None = Field(
        default=True,
        description="Persistence configuration for state checkpointing",
    )

    checkpoint_mode: Literal["sync", "async"] = Field(
        default="sync", description="Checkpoint mode for persistence"
    )

    add_store: bool = Field(
        default=True,
        description="Whether to add a state store for cross-thread persistence",
    )

    # Runtime configuration
    runnable_config: RunnableConfig | None = Field(
        default=None, description="Default runtime configuration"
    )

    # Debug and history flags
    save_history: bool = Field(default=True, description="Save state history")
    visualize: bool = Field(default=True, description="Enable visualization")

    # Private state tracking (same as original)
    _graph_built: bool = PrivateAttr(default=False)
    _compiled_graph: CompiledGraph | None = PrivateAttr(default=None)
    _is_compiled: bool = PrivateAttr(default=False)
    _setup_complete: bool = PrivateAttr(default=False)
    _checkpoint_mode: str = PrivateAttr(default="sync")
    _app: Any | None = PrivateAttr(default=None)
    _async_checkpointer: Any | None = PrivateAttr(default=None)
    _async_setup_pending: bool = PrivateAttr(default=False)

    # Schema control flag
    set_schema: Literal[True, False] = Field(
        default=False, description="Whether to auto-generate schemas from engines"
    )

    @model_validator(mode="before")
    @classmethod
    def normalize_engines_and_name(cls, values: dict[str, Any]) -> dict[str, Any]:
        """STEP 1: Normalize engines dict and auto-generate name."""
        if not isinstance(values, dict):
            return values

        # Auto-generate name from class name if default or empty
        if (
            "name" not in values
            or not values["name"]
            or values["name"] in ["Agent", "Workflow"]
        ):
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

            if isinstance(engines, list | tuple):
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
    @classmethod
    def complete_agent_setup(cls) -> "Agent":
        """STEP 2-5: Complete agent setup in proper order."""
        try:
            # STEP 2: Call subclass setup hook for field syncing
            self.setup_agent()

            # STEP 3: Generate schemas from engines
            self._setup_schemas()

            # STEP 4: Setup persistence using the mixin
            self._setup_persistence_from_config()

            # STEP 5: Build the initial graph
            self._build_initial_graph()

            self._setup_complete = True

            if self.verbose:
                logger.info(f"Enhanced Agent setup complete: {self.name}")

        except Exception as e:
            logger.exception(f"Failed to setup agent {self.__class__.__name__}: {e}")

        return self

    def setup_agent(self) -> None:
        """Hook for subclasses to perform field syncing and custom setup.

        This method is called BEFORE schema generation and graph building,
        allowing subclasses to sync fields to engines properly.

        Override this method in subclasses for custom setup logic.
        """
        # Default implementation does nothing - subclasses override

    def _setup_schemas(self) -> None:
        """Enhanced schema setup with engine type support.

        This could be enhanced to use engine-specific schema generation
        based on the EngineT generic parameter.
        """
        # For now, delegate to existing schema setup logic
        # TODO: Enhance with engine-specific schema generation

    def _setup_persistence_from_config(self) -> None:
        """Setup persistence using the PersistenceMixin."""
        # Delegate to mixin - TODO: implement

    def _build_initial_graph(self) -> None:
        """Build the initial graph."""
        if not self._graph_built:
            self.graph = self.build_graph()
            self._graph_built = True

    @abstractmethod
    def build_graph(self) -> BaseGraph:
        """Abstract method to build the agent's graph."""

    # Bridge Workflow.execute and Agent.arun APIs
    async def execute(self, input_data: Any) -> Any:
        """Execute the agent (bridges Workflow API with Agent API)."""
        result = await self.arun(input_data)
        return result

    # Engine-specific convenience methods
    def get_engine(self) -> EngineT | None:
        """Get the main engine with proper typing."""
        return self.engine

    def set_engine(self, engine: EngineT) -> None:
        """Set the main engine with proper typing."""
        self.engine = engine
        # Add to engines dict
        if hasattr(engine, "name") and engine.name:
            self.engines[engine.name] = engine
        else:
            self.engines["main"] = engine

    def __repr__(self) -> str:
        engine_type = (
            getattr(type(self.engine), "__name__", "None") if self.engine else "None"
        )
        return f"{self.__class__.__name__}[{engine_type}](name='{self.name}')"
