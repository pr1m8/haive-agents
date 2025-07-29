"""ReWOO V3 Agent - Reasoning WithOut Observation using Enhanced MultiAgent V3.

This package implements the ReWOO (Reasoning WithOut Observation) methodology
using our proven Enhanced MultiAgent V3 patterns from Plan-and-Execute V3 success.

ReWOO separates planning, execution, and synthesis phases for improved efficiency:
1. Planner creates complete reasoning plan upfront with evidence placeholders
2. Worker executes all tool calls in batch to collect evidence
3. Solver synthesizes all evidence into comprehensive final answer

Key advantages over traditional iterative agents:
- 5x token efficiency improvement
- Parallel/batch tool execution capability
- Robust handling of partial failures
- Modular design for fine-tuning

Usage:
    >>> from haive.agents.planning.rewoo_v3 import ReWOOV3Agent
    >>> from haive.core.engine.aug_llm import AugLLMConfig
    >>>
    >>> config = AugLLMConfig(temperature=0.7)
    >>> agent = ReWOOV3Agent(
    ...     name="research_agent",
    ...     config=config,
    ...     tools=[search_tool, calculator_tool]
    ... )
    >>>
    >>> result = await agent.arun("Research market trends and calculate growth rates")
    >>> print(f"Answer: {result.final_answer}")
    >>> print(f"Confidence: {result.confidence}")
    >>> print(f"Evidence collected: {result.evidence_collected}")

Architecture:
    - ReWOOV3Agent: Main coordinator using Enhanced MultiAgent V3
    - ReWOOV3State: State schema with computed fields for dynamic prompts
    - ReWOOPlan/EvidenceCollection/ReWOOSolution: Structured output models
    - ChatPromptTemplates: Dynamic prompts with state field placeholders
"""

from haive.agents.planning.rewoo_v3.agent import ReWOOV3Agent
from haive.agents.planning.rewoo_v3.models import (
    EvidenceCollection,
    EvidenceItem,
    EvidenceStatus,
    PlanStep,
    ReWOOPlan,
    ReWOOSolution,
    ReWOOV3Input,
    ReWOOV3Output,
)
from haive.agents.planning.rewoo_v3.state import ReWOOV3State

__all__ = [
    # Main agent
    "ReWOOV3Agent",
    # State management
    "ReWOOV3State",
    # Structured models
    "ReWOOPlan",
    "PlanStep",
    "EvidenceCollection",
    "EvidenceItem",
    "EvidenceStatus",
    "ReWOOSolution",
    # I/O models
    "ReWOOV3Input",
    "ReWOOV3Output",
]
