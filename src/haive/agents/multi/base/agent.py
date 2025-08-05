"""Base MultiAgent implementation.

This module provides the base multi-agent class that other multi-agent
implementations can inherit from or use directly.
"""

# Re-export the clean MultiAgent implementation as the base
from haive.agents.multi.clean import MultiAgent

__all__ = ["MultiAgent"]