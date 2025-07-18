"""Enhanced Discovery System for Dynamic Agent and Tool Management.

This module provides advanced discovery capabilities for Haive agents, including:
- Semantic discovery using vector embeddings
- Dynamic tool selection based on query content
- Component capability matching and analysis
- Memory-aware discovery for persistent systems
- LangGraph-style tool management patterns

The system builds on the existing haive.core.utils.discovery infrastructure
while adding intelligent, context-aware discovery capabilities.
"""

# Re-export component registry items from core
from haive.core.registry import DynamicRegistry, RegistryItem, RegistryManager

from haive.agents.discovery.component_discovery_agent import ComponentDiscoveryAgent

__all__ = [
    # Component Registry (re-exported from core)
    "DynamicRegistry",
    "RegistryItem",
    "RegistryManager",
    # Component Discovery Agent
    "ComponentDiscoveryAgent",
]
