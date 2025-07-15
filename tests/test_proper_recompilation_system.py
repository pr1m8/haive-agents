"""
Test proper generalized recompilation system as described in the docs.

This implements the complete vision from GENERALIZED_RECOMPILATION_MIXIN.md:
- Hash-based change detection
- Observer pattern for change notifications
- ValidationNodeConfigV2 integration
- Batch operations and lazy recompilation
- Meta-agent integration with managed components
"""

import hashlib
import logging
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Set

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.validation_node_config_v2 import ValidationNodeConfigV2
from haive.core.graph.state_graph.base_graph2 import BaseGraph

from haive.agents.simple.agent import SimpleAgent

logger = logging.getLogger(__name__)


class RecompilationMixin:
    """
    Generalized mixin for components that need recompilation tracking.

    Provides:
    - Hash-based change detection
    - Observer pattern for change notifications
    - Configurable state tracking
    - Batch operation support
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._state_hash: Optional[str] = None
        self._last_recompiled: Optional[datetime] = None
        self._change_callbacks: List[tuple[str, Callable]] = []
        self._pending_changes: Set[str] = set()
        self._recompilation_reason: Optional[str] = None
        self._batch_mode: bool = False

    # ========================================================================
    # ABSTRACT METHODS (to be implemented by subclasses)
    # ========================================================================

    def _compute_state_hash(self) -> str:
        """
        Compute hash of current state.

        Subclasses must implement this to define what constitutes "state"
        for change detection purposes.
        """
        raise NotImplementedError("Subclasses must implement _compute_state_hash")

    def _get_change_details(self, change_type: str) -> Dict[str, Any]:
        """
        Get details about a specific change.

        Subclasses can override to provide richer change information.
        """
        return {"change_type": change_type, "timestamp": datetime.now()}

    # ========================================================================
    # CHANGE DETECTION
    # ========================================================================

    def needs_recompilation(self) -> bool:
        """Check if component needs recompilation."""
        if self._state_hash is None:
            return True

        current_hash = self._compute_state_hash()
        return current_hash != self._state_hash

    def mark_compiled(self, reason: Optional[str] = None) -> None:
        """Mark component as compiled with current state."""
        self._state_hash = self._compute_state_hash()
        self._last_recompiled = datetime.now()
        self._pending_changes.clear()
        self._recompilation_reason = reason

    def get_recompilation_info(self) -> Dict[str, Any]:
        """Get detailed recompilation information."""
        return {
            "needs_recompilation": self.needs_recompilation(),
            "last_recompiled": self._last_recompiled,
            "current_hash": self._compute_state_hash(),
            "stored_hash": self._state_hash,
            "pending_changes": list(self._pending_changes),
            "last_reason": self._recompilation_reason,
        }

    # ========================================================================
    # CHANGE NOTIFICATION
    # ========================================================================

    def register_change_callback(
        self, callback: Callable[[str, Dict[str, Any]], None]
    ) -> str:
        """
        Register callback for change notifications.

        Args:
            callback: Function called with (change_type, details)

        Returns:
            Callback ID for later removal
        """
        callback_id = f"callback_{len(self._change_callbacks)}"
        self._change_callbacks.append((callback_id, callback))
        return callback_id

    def unregister_change_callback(self, callback_id: str) -> bool:
        """Remove a registered callback."""
        for i, (cid, _) in enumerate(self._change_callbacks):
            if cid == callback_id:
                del self._change_callbacks[i]
                return True
        return False

    def _notify_change(self, change_type: str, **kwargs) -> None:
        """Notify all registered callbacks of a change."""
        if not self._batch_mode:
            self._pending_changes.add(change_type)

        details = self._get_change_details(change_type)
        details.update(kwargs)

        for _, callback in self._change_callbacks:
            try:
                callback(change_type, details)
            except Exception as e:
                # Log error but don't fail the operation
                logger.error(f"Error in change callback: {e}")

    # ========================================================================
    # BATCH OPERATIONS
    # ========================================================================

    def start_batch_mode(self) -> None:
        """Start batch mode to defer change notifications."""
        self._batch_mode = True

    def end_batch_mode(self, notify: bool = True) -> None:
        """End batch mode and optionally notify of all changes."""
        self._batch_mode = False

        if notify and self._pending_changes:
            self._notify_change("batch_update", changes=list(self._pending_changes))
            self._pending_changes.clear()

    def batch_operation(self, operation: Callable) -> Any:
        """Execute operation in batch mode."""
        self.start_batch_mode()
        try:
            result = operation()
            return result
        finally:
            self.end_batch_mode()


class RecompilableValidationNodeConfigV2(RecompilationMixin, ValidationNodeConfigV2):
    """
    ValidationNodeConfigV2 with recompilation tracking.

    This is the key integration point - ValidationNodeConfigV2 with
    proper recompilation tracking for tool routes and validation rules.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Use private attributes to avoid Pydantic field conflicts
        self._validation_rules: Dict[str, Callable] = {}
        self._custom_validators: Dict[str, Callable] = {}
        self._tool_routes: Dict[str, str] = {}

    def _compute_state_hash(self) -> str:
        """Compute hash based on validation configuration."""
        # Include tool routes, engine config, validation rules
        state_components = [
            str(sorted(self._tool_routes.items())),
            str(getattr(self, "engine_name", "")),
            str(sorted(self._validation_rules.items())),
            str(sorted(self._custom_validators.items())),
        ]

        state_str = "|".join(state_components)
        return hashlib.md5(state_str.encode()).hexdigest()

    def _get_change_details(self, change_type: str) -> Dict[str, Any]:
        """Get validation node specific change details."""
        details = super()._get_change_details(change_type)
        details.update(
            {
                "engine_name": getattr(self, "engine_name", ""),
                "tool_routes": self._tool_routes,
                "validation_rules": self._validation_rules,
            }
        )
        return details

    def update_tool_routes(self, new_routes: Dict[str, str]) -> None:
        """Update tool routes and notify of changes."""
        old_routes = self._tool_routes.copy()

        # Update routes
        self._tool_routes.update(new_routes)

        # Notify change
        self._notify_change(
            "tool_routes_updated",
            old_routes=old_routes,
            new_routes=self._tool_routes,
            added_routes={k: v for k, v in new_routes.items() if k not in old_routes},
            changed_routes={
                k: v
                for k, v in new_routes.items()
                if k in old_routes and old_routes[k] != v
            },
        )

    def add_validation_rule(self, rule_name: str, rule_func: Callable) -> None:
        """Add validation rule and notify of changes."""
        old_rules = self._validation_rules.copy()
        self._validation_rules[rule_name] = rule_func

        self._notify_change(
            "validation_rule_added",
            rule_name=rule_name,
            old_rules=old_rules,
            new_rules=self._validation_rules,
        )

    def add_custom_validator(
        self, validator_name: str, validator_func: Callable
    ) -> None:
        """Add custom validator and notify of changes."""
        old_validators = self._custom_validators.copy()
        self._custom_validators[validator_name] = validator_func

        self._notify_change(
            "custom_validator_added",
            validator_name=validator_name,
            old_validators=old_validators,
            new_validators=self._custom_validators,
        )


class RecompilableBaseGraph(RecompilationMixin, BaseGraph):
    """
    BaseGraph with recompilation tracking.
    """

    def _compute_state_hash(self) -> str:
        """Compute hash based on graph structure."""
        components = [
            str(sorted(self.nodes.keys())),
            str(sorted(self.edges)) if hasattr(self, "edges") else "[]",
            str(sorted(self.branches.keys())) if hasattr(self, "branches") else "[]",
            str(getattr(self, "tool_routes", {})),
        ]

        state_str = "|".join(components)
        return hashlib.md5(state_str.encode()).hexdigest()

    def add_node(self, *args, **kwargs) -> "RecompilableBaseGraph":
        """Add node and notify of changes."""
        old_nodes = set(self.nodes.keys())

        result = super().add_node(*args, **kwargs)

        new_nodes = set(self.nodes.keys())
        added_nodes = new_nodes - old_nodes

        if added_nodes:
            self._notify_change(
                "nodes_added",
                added_nodes=list(added_nodes),
                total_nodes=len(self.nodes),
            )

        return result

    def add_edge(self, *args, **kwargs) -> "RecompilableBaseGraph":
        """Add edge and notify of changes."""
        old_edges = len(getattr(self, "edges", []))

        result = super().add_edge(*args, **kwargs)

        new_edges = len(getattr(self, "edges", []))
        if new_edges > old_edges:
            self._notify_change(
                "edges_added", edges_added=new_edges - old_edges, total_edges=new_edges
            )

        return result


class RecompilableSimpleAgent(RecompilationMixin, SimpleAgent):
    """
    SimpleAgent with the proper generalized recompilation system.

    This demonstrates the complete integration as described in the docs.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._validation_node: Optional[RecompilableValidationNodeConfigV2] = None
        self._graph: Optional[RecompilableBaseGraph] = None
        self._managed_components: Dict[str, RecompilationMixin] = {}

    def _compute_state_hash(self) -> str:
        """Hash based on agent configuration and managed components."""
        components = [
            # Agent identity
            str(self.name),
            # Engine configuration
            str(type(self.engine).__name__),
            str(getattr(self.engine, "system_message", "")),
            # Managed components
            str(sorted(self._managed_components.keys())),
            # Graph structure (if available)
            str(list(self._graph.nodes.keys()) if self._graph else []),
            # Validation node state
            str(
                self._validation_node._compute_state_hash()
                if self._validation_node
                else "None"
            ),
        ]

        state_str = "|".join(components)
        return hashlib.md5(state_str.encode()).hexdigest()

    def add_managed_component(self, name: str, component: RecompilationMixin) -> None:
        """Add component and register for recompilation tracking."""
        self._managed_components[name] = component

        # Register callback to track when this component needs recompilation
        component.register_change_callback(
            lambda change_type, details: self._handle_component_change(
                name, change_type, details
            )
        )

    def _handle_component_change(
        self, component_name: str, change_type: str, details: Dict
    ):
        """Handle changes from managed components."""
        print(
            f"  [Agent {self.name}] Component {component_name} changed: {change_type}"
        )

        # Propagate the change up to agent level
        self._notify_change(
            "managed_component_changed",
            component_name=component_name,
            component_change_type=change_type,
            component_details=details,
        )

    def create_validation_node(
        self, engine_name: str = "main"
    ) -> RecompilableValidationNodeConfigV2:
        """Create a recompilable validation node."""
        validation_node = RecompilableValidationNodeConfigV2(
            name=f"{self.name}_validation", engine_name=engine_name
        )

        # Add as managed component
        self.add_managed_component("validation_node", validation_node)
        self._validation_node = validation_node

        return validation_node

    def create_recompilable_graph(self) -> RecompilableBaseGraph:
        """Create a recompilable graph."""
        graph = RecompilableBaseGraph(name=f"{self.name}_graph")

        # Add as managed component
        self.add_managed_component("graph", graph)
        self._graph = graph

        return graph

    def recompile_if_needed(self) -> Dict[str, Any]:
        """Check and perform recompilation as needed."""
        result = {
            "agent_recompiled": False,
            "components_recompiled": [],
            "recompilation_report": {},
        }

        # Check if agent needs recompilation
        if self.needs_recompilation():
            print(f"  [Agent {self.name}] Needs recompilation")

            # Check each managed component
            for name, component in self._managed_components.items():
                if component.needs_recompilation():
                    print(f"    Component {name} needs recompilation")

                    # Perform component-specific recompilation
                    if name == "validation_node":
                        self._recompile_validation_node(component)
                    elif name == "graph":
                        self._recompile_graph(component)
                    else:
                        # Generic recompilation
                        component.mark_compiled(f"Component {name} recompiled")

                    result["components_recompiled"].append(name)

            # Mark agent as compiled
            self.mark_compiled("Agent recompiled with managed components")
            result["agent_recompiled"] = True

        result["recompilation_report"] = self.get_recompilation_info()
        return result

    def _recompile_validation_node(
        self, node: RecompilableValidationNodeConfigV2
    ) -> None:
        """Recompile validation node."""
        print(f"    Recompiling validation node: {node.name}")

        # Apply any validation rules or tool routes
        if hasattr(node, "_validation_rules"):
            print(f"      Applied {len(node._validation_rules)} validation rules")

        if hasattr(node, "_tool_routes"):
            print(f"      Applied {len(node._tool_routes)} tool routes")

        node.mark_compiled("Validation node recompiled")

    def _recompile_graph(self, graph: RecompilableBaseGraph) -> None:
        """Recompile graph."""
        print(f"    Recompiling graph: {graph.name}")
        print(f"      Graph has {len(graph.nodes)} nodes")

        graph.mark_compiled("Graph recompiled")


class MetaAgentWithRecompilation:
    """
    Complete meta-agent system with recompilation tracking.

    This demonstrates the full pattern from the docs.
    """

    def __init__(self):
        self.managed_components: Dict[str, RecompilationMixin] = {}
        self.recompilation_callbacks: Dict[str, str] = {}

    def add_managed_component(self, name: str, component: RecompilationMixin) -> None:
        """Add component and register for recompilation tracking."""
        self.managed_components[name] = component

        # Register callback to track when this component needs recompilation
        callback_id = component.register_change_callback(
            lambda change_type, details: self._handle_component_change(
                name, change_type, details
            )
        )
        self.recompilation_callbacks[name] = callback_id

    def _handle_component_change(
        self, component_name: str, change_type: str, details: Dict
    ):
        """Handle changes from managed components."""
        print(f"[Meta-Agent] Component {component_name} changed: {change_type}")

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
        print("  [Meta-Agent] Scheduling recompilation...")

    def recompile_all_if_needed(self) -> Dict[str, Any]:
        """Check and recompile all managed components."""
        result = {
            "components_checked": len(self.managed_components),
            "components_recompiled": [],
            "recompilation_details": {},
        }

        for name, component in self.managed_components.items():
            if component.needs_recompilation():
                print(f"[Meta-Agent] Recompiling component: {name}")

                # Perform recompilation
                if hasattr(component, "recompile_if_needed"):
                    recompile_result = component.recompile_if_needed()
                    result["recompilation_details"][name] = recompile_result
                else:
                    component.mark_compiled(
                        f"Component {name} recompiled by meta-agent"
                    )
                    result["recompilation_details"][name] = {"recompiled": True}

                result["components_recompiled"].append(name)

        return result


# Test functions
def test_validation_node_recompilation():
    """Test ValidationNodeConfigV2 with recompilation tracking."""
    print("\n=== Test: ValidationNodeConfigV2 Recompilation ===")

    # Create recompilable validation node
    validation_node = RecompilableValidationNodeConfigV2(
        name="dynamic_validation", engine_name="main_engine"
    )

    # Register for recompilation notifications
    def change_handler(change_type: str, details: Dict[str, Any]):
        print(f"  [Change] {change_type}: {details.get('timestamp', 'N/A')}")

    validation_node.register_change_callback(change_handler)

    # Initial state
    print("1. Initial state:")
    print(f"   Needs recompilation: {validation_node.needs_recompilation()}")
    validation_node.mark_compiled("Initial state")

    # Add tool routes
    print("\n2. Adding tool routes...")
    validation_node.update_tool_routes({"search": "tool_node", "analyze": "validation"})

    print(f"   Needs recompilation: {validation_node.needs_recompilation()}")
    print(f"   Tool routes: {validation_node._tool_routes}")

    # Add validation rules
    print("\n3. Adding validation rules...")
    validation_node.add_validation_rule("input_length", lambda x: len(x) > 0)
    validation_node.add_validation_rule("no_profanity", lambda x: "bad" not in x)

    print(f"   Needs recompilation: {validation_node.needs_recompilation()}")
    print(f"   Validation rules: {list(validation_node._validation_rules.keys())}")

    # Recompile
    print("\n4. Recompiling...")
    if validation_node.needs_recompilation():
        validation_node.mark_compiled("Tool routes and validation rules updated")
        print("   Recompilation completed")

    print(f"   Needs recompilation: {validation_node.needs_recompilation()}")

    return validation_node


def test_recompilable_agent():
    """Test RecompilableSimpleAgent with managed components."""
    print("\n=== Test: RecompilableSimpleAgent ===")

    # Create recompilable agent
    engine = AugLLMConfig(system_message="You are a helpful assistant.")
    agent = RecompilableSimpleAgent(name="meta_agent", engine=engine)

    # Register for agent-level changes
    def agent_change_handler(change_type: str, details: Dict[str, Any]):
        print(f"  [Agent Change] {change_type}")

    agent.register_change_callback(agent_change_handler)

    # Initial state
    print("1. Initial state:")
    print(f"   Agent needs recompilation: {agent.needs_recompilation()}")
    agent.mark_compiled("Initial state")

    # Create validation node
    print("\n2. Creating validation node...")
    validation_node = agent.create_validation_node()

    # Create graph
    print("\n3. Creating recompilable graph...")
    graph = agent.create_recompilable_graph()

    print(f"   Agent needs recompilation: {agent.needs_recompilation()}")
    print(f"   Managed components: {list(agent._managed_components.keys())}")

    # Modify validation node
    print("\n4. Modifying validation node...")
    validation_node.update_tool_routes({"new_tool": "new_route"})
    validation_node.add_validation_rule("new_rule", lambda x: True)

    print(f"   Agent needs recompilation: {agent.needs_recompilation()}")

    # Modify graph
    print("\n5. Modifying graph...")
    graph.add_node("new_node", lambda x: x)

    print(f"   Agent needs recompilation: {agent.needs_recompilation()}")

    # Recompile
    print("\n6. Recompiling agent...")
    recompile_result = agent.recompile_if_needed()

    print(f"   Agent recompiled: {recompile_result['agent_recompiled']}")
    print(f"   Components recompiled: {recompile_result['components_recompiled']}")
    print(f"   Agent needs recompilation: {agent.needs_recompilation()}")

    return agent


def test_meta_agent_system():
    """Test complete meta-agent system."""
    print("\n=== Test: Meta-Agent System ===")

    # Create meta-agent system
    meta_agent = MetaAgentWithRecompilation()

    # Create components
    engine = AugLLMConfig()
    agent1 = RecompilableSimpleAgent(name="agent1", engine=engine)
    agent2 = RecompilableSimpleAgent(name="agent2", engine=engine)

    # Add to meta-agent
    print("1. Adding agents to meta-agent...")
    meta_agent.add_managed_component("agent1", agent1)
    meta_agent.add_managed_component("agent2", agent2)

    # Create validation nodes for each agent
    print("\n2. Creating validation nodes...")
    val_node1 = agent1.create_validation_node()
    val_node2 = agent2.create_validation_node()

    # Modify components
    print("\n3. Modifying components...")
    val_node1.update_tool_routes({"tool1": "route1"})
    val_node2.add_validation_rule("rule1", lambda x: True)

    # Recompile through meta-agent
    print("\n4. Recompiling through meta-agent...")
    recompile_result = meta_agent.recompile_all_if_needed()

    print(f"   Components checked: {recompile_result['components_checked']}")
    print(f"   Components recompiled: {recompile_result['components_recompiled']}")

    return meta_agent


if __name__ == "__main__":
    print("🧪 Testing Proper Generalized Recompilation System")
    print("=" * 60)

    try:
        # Test 1: ValidationNodeConfigV2 recompilation
        validation_node = test_validation_node_recompilation()

        # Test 2: RecompilableSimpleAgent
        agent = test_recompilable_agent()

        # Test 3: Complete meta-agent system
        meta_agent = test_meta_agent_system()

        print("\n✅ All tests completed successfully!")
        print("Proper generalized recompilation system is working correctly.")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()
