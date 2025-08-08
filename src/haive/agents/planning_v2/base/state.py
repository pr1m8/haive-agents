"""State management for planning agents.

This module uses the prebuilt MessagesState from haive.core.
"""

from haive.core.schema.prebuilt.messages_state import MessagesState

# We use MessagesState directly, no custom state needed
__all__ = ["MessagesState"]
