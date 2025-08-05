"""Test proper generalized recompilation system as designed in docs."""

from collections.abc import Callable
from datetime import datetime
from typing import Any

from pydantic import Field

from haive.agents.simple import SimpleAgent
from haive.agents.simple.state import SimpleAgentState
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.validation import ValidationNodeConfigV2


class RecompilationMixin:
    """Generalized mixin for components that need recompilation tracking."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._state_hash: str | None = None
        self._last_recompiled: datetime | None = None
        self._change_callbacks: list[tuple[str, Callable]] = []
        self._pending_changes: set[str] = set()
        self._recompilation_reason: str | None = None
        self._batch_mode: bool = False

    def needs_recompilation(self) -> bool:
        """Check if component needs recompilation."""
        if self._state_hash is None:
            return True
        current_hash = self._compute_state_hash()
        return current_hash != self._state_hash

    def _compute_state_hash(self) -> str:
        """Compute hash of current state."""
        # Simplified for demo - real implementation would use proper hashing
        import hashlib

        state_str = str(self.__dict__)
        return hashlib.sha256(state_str.encode()).hexdigest()[:8]

    def mark_compiled(self, reason: str = "Manual compilation") -> None:
        """Mark component as compiled and update hash."""
        self._state_hash = self._compute_state_hash()
        self._last_recompiled = datetime.now()
        self._recompilation_reason = reason
        self._pending_changes.clear()

        # Notify observers
        self._notify_change("compiled", reason=reason, timestamp=self._last_recompiled)

    def register_change_callback(self, callback: Callable[[str, dict[str, Any]], None]) -> str:
        """Register callback for change notifications."""
        callback_id = f"callback_{len(self._change_callbacks)}"
        self._change_callbacks.append((callback_id, callback))
        return callback_id

    def _notify_change(self, change_type: str, **kwargs) -> None:
        """Notify all registered callbacks of a change."""
        if self._batch_mode:
            self._pending_changes.add(change_type)
            return

        change_data = {
            "change_type": change_type,
            "timestamp": datetime.now(),
            **kwargs,
        }

        for _, callback in self._change_callbacks:
            callback(change_type, change_data)

    def start_batch_mode(self) -> None:
        """Start batch mode for multiple changes."""
        self._batch_mode = True
        self._pending_changes.clear()

    def end_batch_mode(self) -> None:
        """End batch mode and notify all pending changes."""
        self._batch_mode = False
        if self._pending_changes:
            self._notify_change("batch_changes", changes=list(self._pending_changes))


class RecompilableValidationNodeConfigV2(RecompilationMixin, ValidationNodeConfigV2):
    """ValidationNodeConfigV2 with recompilation tracking."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._tool_routes: dict[str, str] = {}
        self._validation_rules: dict[str, Callable] = {}

    def update_tool_routes(self, new_routes: dict[str, str]) -> None:
        """Update tool routes and notify of changes."""
        old_routes = self._tool_routes.copy()
        self._tool_routes.update(new_routes)

        self._notify_change(
            "tool_routes_updated",
            old_routes=old_routes,
            new_routes=self._tool_routes,
            added_routes={k: v for k, v in new_routes.items() if k not in old_routes},
        )

    def add_validation_rule(self, name: str, rule: Callable) -> None:
        """Add validation rule and notify of changes."""
        self._validation_rules[name] = rule
        self._notify_change("validation_rule_added", rule_name=name)

    def update_validation_rules(self, **rules) -> None:
        """Update multiple validation rules."""
        for name, rule in rules.items():
            self.add_validation_rule(name, rule)


class RecompilableSimpleAgentState(SimpleAgentState):
    """Agent state with recompilation tracking."""

    recompilation_count: int = Field(default=0, description="Number of recompilations")
    last_recompilation_reason: str = Field(default="", description="Last recompilation reason")


class RecompilableSimpleAgent(SimpleAgent):
    """SimpleAgent with recompilation capabilities."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._validation_node: RecompilableValidationNodeConfigV2 | None = None
        self._custom_nodes = []
        self._output_parser = None
        self._recompilation_count = 0

    def create_validation_node(self) -> RecompilableValidationNodeConfigV2:
        """Create a validation node for this agent."""
        if not self._validation_node:
            self._validation_node = RecompilableValidationNodeConfigV2(
                name=f"{self.name}_validation", engine_name=self.name
            )
        return self._validation_node

    def add_custom_node(self, node_name: str, node_function: Callable) -> None:
        """Add custom node to agent graph."""
        self._custom_nodes.append((node_name, node_function))
        # In real implementation, would rebuild graph

    def set_output_parser(self, parser: Callable) -> None:
        """Set custom output parser."""
        self._output_parser = parser

    def recompile_if_needed(self) -> dict[str, Any]:
        """Recompile agent if any components need it."""
        needs_recompile = False
        reasons = []

        # Check validation node
        if self._validation_node and self._validation_node.needs_recompilation():
            needs_recompile = True
            reasons.append("validation_node_changed")

        # Check custom nodes
        if self._custom_nodes:
            needs_recompile = True
            reasons.append(f"custom_nodes_added: {len(self._custom_nodes)}")

        if needs_recompile:
            self._recompilation_count += 1
            # In real implementation, would rebuild graph
            if self._validation_node:
                self._validation_node.mark_compiled("Agent recompilation")

        return {
            "recompiled": needs_recompile,
            "reasons": reasons,
            "recompilation_count": self._recompilation_count,
        }

    def needs_recompilation(self) -> bool:
        """Check if agent needs recompilation."""
        if self._validation_node and self._validation_node.needs_recompilation():
            return True
        return bool(self._custom_nodes)


class MetaAgentWithRecompilation:
    """Meta-agent that manages recompilable agents."""

    def __init__(self, name: str):
        self.name = name
        self.managed_components: dict[str, RecompilationMixin] = {}
        self.recompilation_callbacks: dict[str, str] = {}

    def add_managed_component(self, name: str, component: RecompilationMixin) -> None:
        """Add a component to manage."""
        self.managed_components[name] = component

        # Register for recompilation notifications
        callback_id = component.register_change_callback(
            lambda change_type, details: self._handle_component_change(name, change_type, details)
        )
        self.recompilation_callbacks[name] = callback_id

    def _handle_component_change(self, component_name: str, change_type: str, details: dict):
        """Handle changes from managed components."""
        # Could trigger meta-agent recompilation logic here
        if self._should_recompile_meta_agent(change_type):
            self._schedule_meta_agent_recompilation()

    def _should_recompile_meta_agent(self, change_type: str) -> bool:
        """Determine if meta-agent should recompile based on change type."""
        recompile_triggers = [
            "tool_routes_updated",
            "validation_rule_added",
            "nodes_added",
            "edges_added",
            "managed_component_changed",
        ]
        return change_type in recompile_triggers

    def _schedule_meta_agent_recompilation(self) -> None:
        """Schedule meta-agent recompilation."""

    def recompile_all_if_needed(self) -> dict[str, Any]:
        """Check and recompile all managed components."""
        result = {
            "components_checked": len(self.managed_components),
            "components_recompiled": [],
            "recompilation_details": {},
        }

        for name, component in self.managed_components.items():
            if component.needs_recompilation():
                # Perform recompilation
                if hasattr(component, "recompile_if_needed"):
                    recompile_result = component.recompile_if_needed()
                    result["recompilation_details"][name] = recompile_result
                else:
                    component.mark_compiled(f"Component {name} recompiled by meta-agent")

                result["components_recompiled"].append(name)

        return result


def test_validation_node_recompilation():
    """Test ValidationNodeConfigV2 with recompilation tracking."""
    # Create recompilable validation node
    node = RecompilableValidationNodeConfigV2(name="dynamic_validation", engine_name="main_engine")

    # Initial state
    assert not node.needs_recompilation()

    # Register callback to track changes
    changes = []
    node.register_change_callback(lambda reason, data: changes.append((reason, data)))

    # Update tool routes
    node.update_tool_routes({"calculator": "math_engine", "search": "search_engine"})

    # Should need recompilation
    assert node.needs_recompilation()
    assert len(changes) == 1
    assert changes[0][0] == "tool_routes_updated"

    # Mark as compiled
    node.mark_compiled("Test compilation")
    assert not node.needs_recompilation()

    # Update validation rules
    node.update_validation_rules(
        input_validation=lambda x: x.get("required_field") is not None,
        output_validation=lambda x: len(x) > 0,
    )

    assert node.needs_recompilation()
    assert len(changes) == 4  # tool_routes, compiled, 2 validation rules


def test_recompilable_agent():
    """Test agent with recompilation capabilities."""
    # Create agent with real engine
    engine = AugLLMConfig()
    agent = RecompilableSimpleAgent(name="meta_agent", engine=engine)

    # Create validation node
    val_node = agent.create_validation_node()

    # Initially doesn't need recompilation
    assert not agent.needs_recompilation()

    # Modify validation node
    val_node.update_tool_routes({"calc": "calc_route"})

    # Now needs recompilation
    assert agent.needs_recompilation()

    # Recompile
    result = agent.recompile_if_needed()
    assert result["recompiled"]
    assert "validation_node_changed" in result["reasons"]

    # After recompilation, shouldn't need it again
    assert not agent.needs_recompilation()

    # Add custom node
    agent.add_custom_node("custom_processor", lambda x: x)
    assert agent.needs_recompilation()


def test_meta_agent_system():
    """Test complete meta-agent system."""
    # Create meta-agent
    meta_agent = MetaAgentWithRecompilation(name="coordinator")

    # Create managed agents
    engine = AugLLMConfig()
    agent1 = RecompilableSimpleAgent(name="agent1", engine=engine)
    agent2 = RecompilableSimpleAgent(name="agent2", engine=engine)

    # Add to meta-agent
    meta_agent.add_managed_component("agent1", agent1)
    meta_agent.add_managed_component("agent2", agent2)

    # Create validation nodes
    val_node1 = agent1.create_validation_node()
    val_node2 = agent2.create_validation_node()

    # Modify components
    val_node1.update_tool_routes({"tool1": "route1"})
    val_node2.add_validation_rule("rule1", lambda x: True)

    # Both agents should need recompilation
    assert agent1.needs_recompilation()
    assert agent2.needs_recompilation()

    # Recompile through meta-agent
    result = meta_agent.recompile_all_if_needed()

    assert result["components_checked"] == 2
    assert len(result["components_recompiled"]) == 2
    assert "agent1" in result["components_recompiled"]
    assert "agent2" in result["components_recompiled"]

    # After meta-agent recompilation, nothing should need recompilation
    assert not agent1.needs_recompilation()
    assert not agent2.needs_recompilation()
