"""Self-Discover Adapter Agent module."""

from .agent import AdapterAgent
from .models import AdaptedModule, AdaptedModules
from .prompts import ADAPTER_PROMPT, ADAPTER_SYSTEM_MESSAGE

__all__ = [
    "ADAPTER_PROMPT",
    "ADAPTER_SYSTEM_MESSAGE",
    "AdaptedModule",
    "AdaptedModules",
    "AdapterAgent",
]
