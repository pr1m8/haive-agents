"""LLM Compiler V3 - Enhanced MultiAgent V3 Implementation.

This module provides a modernized implementation of the LLM Compiler pattern
using Enhanced MultiAgent V3 architecture for simplified, maintainable code.
"""

from haive.agents.planning.llm_compiler_v3.agent import LLMCompilerV3Agent
from haive.agents.planning.llm_compiler_v3.config import LLMCompilerV3Config
from haive.agents.planning.llm_compiler_v3.models import (
    CompilerInput,
    CompilerOutput,
    CompilerPlan,
    CompilerTask,
    ParallelExecutionResult,
    TaskDependency,
)
from haive.agents.planning.llm_compiler_v3.state import LLMCompilerStateSchema

__all__ = [
    "LLMCompilerV3Agent",
    "CompilerTask",
    "CompilerPlan",
    "TaskDependency",
    "ParallelExecutionResult",
    "CompilerInput",
    "CompilerOutput",
    "LLMCompilerStateSchema",
    "LLMCompilerV3Config",
]
