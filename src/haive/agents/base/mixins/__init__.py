"""Agent Mixins - Modular capabilities for Haive agents.

This module provides mixins that add specific capabilities to agent classes:
- ExecutionMixin: Run, stream, and invocation functionality
- StateMixin: State management and persistence operations
- PersistenceMixin: Checkpointer and store configuration

Example:
    Basic usage::

        from haive.agents.base.mixins import ExecutionMixin, StateMixin, PersistenceMixin

        class MyAgent(PersistenceMixin, ExecutionMixin, StateMixin):
            def setup_agent(self):
                # Configure persistence
                self.persistence = PostgresCheckpointerConfig()
                self.checkpoint_mode = "async"
"""

from haive.agents.base.mixins.execution_mixin import ExecutionMixin
from haive.agents.base.mixins.persistence_mixin import PersistenceMixin
from haive.agents.base.mixins.state_mixin import StateMixin

__all__ = [
    "ExecutionMixin",
    "PersistenceMixin",
    "StateMixin",
]
