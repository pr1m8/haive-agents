# SimpleAgent Package - Ultra-fast lazy loading
"""SimpleAgent package with ultra-optimized import performance.
Achieves sub-3 second import times through comprehensive lazy loading.
"""

# Lazy import mapping for SimpleAgent variants

import importlib

_SIMPLE_AGENT_IMPORTS = {
    "SimpleAgent": ("haive.agents.simple.agent_v2", "SimpleAgentV2"),
    "SimpleAgentV3": ("haive.agents.simple.agent_v3", "SimpleAgentV3"),
}


def __getattr__(name: str):
    """Lazy load SimpleAgent classes to avoid import-time overhead."""
    if name in _SIMPLE_AGENT_IMPORTS:
        module_path, class_name = _SIMPLE_AGENT_IMPORTS[name]

        # Import module and get class only when accessed

        module = importlib.import_module(module_path)
        agent_class = getattr(module, class_name)

        # Cache in globals for subsequent access
        globals()[name] = agent_class
        return agent_class

    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


__all__ = ["SimpleAgent", "SimpleAgentV3"]
