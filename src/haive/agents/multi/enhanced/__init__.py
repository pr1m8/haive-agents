"""Enhanced multi-agent implementations with advanced features."""

# V3 has Pydantic generics issues; use base MultiAgent via shim
from haive.agents.multi.agent import MultiAgent as EnhancedMultiAgent

__all__ = ["EnhancedMultiAgent"]
