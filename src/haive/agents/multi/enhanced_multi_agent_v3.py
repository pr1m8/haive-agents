"""Compatibility shim - EnhancedMultiAgent redirects to MultiAgent."""

from haive.agents.multi.agent import MultiAgent as EnhancedMultiAgent

__all__ = ["EnhancedMultiAgent"]
