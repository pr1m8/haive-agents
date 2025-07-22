"""Module exports for reflection agents."""

# Multi-agent reflection patterns (NEW - working implementation)
# Message transformer post-hook patterns (CORRECT implementation)
from .message_transformer_posthook import (
    AgentWithPostHook,
    MessageTransformerPostHook,
    ReflectionWithGradePostHook,
    create_agent_with_reflection,
    create_graded_reflection_post_hook,
    create_reflection_post_hook,
)
from .multi_agent_reflection import (
    MultiAgentReflection,
    ReflectionGrade,
    ReflectionResult,
    create_full_reflection_system,
    create_simple_reflection_system,
)

__all__ = [
    # Multi-agent reflection patterns (NEW)
    "MultiAgentReflection",
    "ReflectionGrade",
    "ReflectionResult",
    "create_simple_reflection_system",
    "create_full_reflection_system",
    # Message transformer post-hook patterns
    "MessageTransformerPostHook",
    "ReflectionWithGradePostHook",
    "AgentWithPostHook",
    "create_reflection_post_hook",
    "create_graded_reflection_post_hook",
    "create_agent_with_reflection",
]
