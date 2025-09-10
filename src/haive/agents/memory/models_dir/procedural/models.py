from datetime import datetime
from typing import Any
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, field_validator, model_validator
from haive.agents.memory.models_dir.base import BaseMemoryModel
from haive.agents.memory.models_dir.semantic.mixins import TemporalMixin


class InstructionComponent(BaseModel):
    """Individual instruction component with metadata."""

    component_id: UUID = Field(default_factory=uuid4)
    instruction_text: str = Field(..., min_length=10, max_length=2000)
    priority: int = Field(default=1, ge=1, le=10)
    effectiveness_score: float = Field(default=0.5, ge=0.0, le=1.0)
    usage_count: int = Field(default=0, ge=0)
    last_modified: datetime = Field(default_factory=datetime.now)

    @field_validator("instruction_text")
    @classmethod
    def validate_instruction_clarity(cls, v: str) -> str:
        """Validate instruction clarity and format."""
        v = v.strip()
        if not v.endswith(".") and (not v.endswith("!")) and (not v.endswith("?")):
            v += "."
        imperative_starters = ["use", "avoid", "ensure", "always", "never", "when", "if"]
        if not any((v.lower().startswith(starter) for starter in imperative_starters)):
            pass
        return v


class ReflectionCycle(BaseModel):
    """Reflection cycle for continuous improvement."""

    cycle_id: UUID = Field(default_factory=uuid4)
    trigger_event: str = Field(..., description="What triggered this reflection")
    current_performance: dict[str, float] = Field(default_factory=dict)
    identified_issues: list[str] = Field(default_factory=list)
    proposed_changes: list[str] = Field(default_factory=list)
    change_rationale: str = Field(..., description="Why these changes are needed")
    confidence_score: float = Field(default=0.5, ge=0.0, le=1.0)

    @model_validator(mode="after")
    def validate_reflection_logic(self) -> "ReflectionCycle":
        """Validate reflection cycle logic."""
        if len(self.proposed_changes) > 10:
            raise ValueError("Too many proposed changes in one cycle (max 10)")
        if self.confidence_score > 0.8 and len(self.identified_issues) == 0:
            raise ValueError("High confidence requires identified issues")
        return self


class ProceduralMemory(BaseMemoryModel, TemporalMixin):
    """Advanced procedural memory with self-modification capabilities."""

    __memory_type__ = "procedural"
    __validation_level__ = "enterprise"
    agent_id: str = Field(..., description="Agent identifier")
    instruction_set_name: str = Field(..., description="Instruction set identifier")
    core_instructions: list[InstructionComponent] = Field(default_factory=list)
    contextual_modifiers: dict[str, list[str]] = Field(default_factory=dict)
    overall_effectiveness: float = Field(default=0.5, ge=0.0, le=1.0)
    usage_statistics: dict[str, int] = Field(default_factory=dict)
    performance_trends: list[dict[str, Any]] = Field(default_factory=list)
    reflection_cycles: list[ReflectionCycle] = Field(default_factory=list)
    last_reflection: datetime | None = Field(None)
    adaptation_threshold: float = Field(default=0.3, ge=0.0, le=1.0)
    version: int = Field(default=1, ge=1)
    change_log: list[dict[str, Any]] = Field(default_factory=list)

    @field_validator("core_instructions")
    @classmethod
    def validate_instruction_set(cls, v: list[InstructionComponent]) -> list[InstructionComponent]:
        """Validate instruction set consistency."""
        if len(v) == 0:
            raise ValueError("At least one core instruction required")
        if len(v) > 50:
            raise ValueError("Too many core instructions (max 50)")
        texts = [instr.instruction_text.lower() for instr in v]
        for i, text1 in enumerate(texts):
            for _j, text2 in enumerate(texts[i + 1 :], i + 1):
                if "never" in text1 and "always" in text2:
                    words1 = set(text1.split())
                    words2 = set(text2.split())
                    if len(words1 & words2) > 3:
                        pass
        return v

    @model_validator(mode="after")
    def validate_procedural_integrity(self) -> "ProceduralMemory":
        """Validate overall procedural memory integrity."""
        if self.core_instructions:
            total_effectiveness = sum(
                (instr.effectiveness_score for instr in self.core_instructions)
            )
            self.overall_effectiveness = total_effectiveness / len(self.core_instructions)
        if self.should_trigger_reflection():
            self._add_reflection_trigger("Performance threshold reached")
        return self

    def should_trigger_reflection(self) -> bool:
        """Determine if reflection cycle should be triggered."""
        if self.overall_effectiveness < self.adaptation_threshold:
            return True
        if self.last_reflection is None:
            return True
        days_since_reflection = (datetime.now() - self.last_reflection).days
        return days_since_reflection > 30

    def _add_reflection_trigger(self, trigger: str) -> None:
        """Add a reflection trigger event."""

    def generate_instruction_text(self) -> str:
        """Generate formatted instruction text for agent use."""
        sections = []
        sorted_instructions = sorted(
            self.core_instructions, key=lambda x: (-x.priority, -x.effectiveness_score)
        )
        sections.append("=== CORE INSTRUCTIONS ===")
        for instr in sorted_instructions:
            sections.append(f"• {instr.instruction_text}")
        if self.contextual_modifiers:
            sections.append("\n=== CONTEXTUAL GUIDELINES ===")
            for context, modifiers in self.contextual_modifiers.items():
                sections.append(f"When {context}:")
                for modifier in modifiers:
                    sections.append(f"  - {modifier}")
        return "\n".join(sections)

    def adapt_from_reflection(self, reflection: ReflectionCycle) -> None:
        """Adapt instructions based on reflection cycle."""
        if reflection.confidence_score < 0.6:
            return
        for change in reflection.proposed_changes:
            if "add instruction" in change.lower():
                new_text = change.split(":")[-1].strip() if ":" in change else change
                new_instruction = InstructionComponent(instruction_text=new_text)
                self.core_instructions.append(new_instruction)
        self.version += 1
        self.change_log.append(
            {
                "version": self.version,
                "timestamp": datetime.now().isoformat(),
                "reflection_id": str(reflection.cycle_id),
                "changes": reflection.proposed_changes,
            }
        )
        self.last_reflection = datetime.now()
        self.reflection_cycles.append(reflection)


# Standalone functions for export
def validate_instruction_clarity(instruction_text: str) -> str:
    """Validate instruction clarity and format."""
    text = instruction_text.strip()
    if not text.endswith(".") and (not text.endswith("!")) and (not text.endswith("?")):
        text += "."
    return text


def validate_instruction_set(
    instructions: list[InstructionComponent],
) -> list[InstructionComponent]:
    """Validate instruction set consistency."""
    if len(instructions) == 0:
        raise ValueError("At least one core instruction required")
    if len(instructions) > 50:
        raise ValueError("Too many core instructions (max 50)")
    return instructions


def validate_procedural_integrity(memory: ProceduralMemory) -> ProceduralMemory:
    """Validate overall procedural memory integrity."""
    if memory.core_instructions:
        total_effectiveness = sum((instr.effectiveness_score for instr in memory.core_instructions))
        memory.overall_effectiveness = total_effectiveness / len(memory.core_instructions)
    return memory


def validate_reflection_logic(reflection: ReflectionCycle) -> ReflectionCycle:
    """Validate reflection cycle logic."""
    if len(reflection.proposed_changes) > 10:
        raise ValueError("Too many proposed changes in one cycle (max 10)")
    if reflection.confidence_score > 0.8 and len(reflection.identified_issues) == 0:
        raise ValueError("High confidence requires identified issues")
    return reflection


def should_trigger_reflection(memory: ProceduralMemory) -> bool:
    """Determine if reflection cycle should be triggered."""
    if memory.overall_effectiveness < memory.adaptation_threshold:
        return True
    if memory.last_reflection is None:
        return True
    days_since_reflection = (datetime.now() - memory.last_reflection).days
    return days_since_reflection > 30


def generate_instruction_text(memory: ProceduralMemory) -> str:
    """Generate formatted instruction text for agent use."""
    sections = []
    sorted_instructions = sorted(
        memory.core_instructions, key=lambda x: (-x.priority, -x.effectiveness_score)
    )
    sections.append("=== CORE INSTRUCTIONS ===")
    for instr in sorted_instructions:
        sections.append(f"• {instr.instruction_text}")
    if memory.contextual_modifiers:
        sections.append("\n=== CONTEXTUAL GUIDELINES ===")
        for context, modifiers in memory.contextual_modifiers.items():
            sections.append(f"When {context}:")
            for modifier in modifiers:
                sections.append(f"  - {modifier}")
    return "\n".join(sections)


def adapt_from_reflection(memory: ProceduralMemory, reflection: ReflectionCycle) -> None:
    """Adapt instructions based on reflection cycle."""
    if reflection.confidence_score < 0.6:
        return
    for change in reflection.proposed_changes:
        if "add instruction" in change.lower():
            new_text = change.split(":")[-1].strip() if ":" in change else change
            new_instruction = InstructionComponent(instruction_text=new_text)
            memory.core_instructions.append(new_instruction)
    memory.version += 1
    memory.change_log.append(
        {
            "version": memory.version,
            "timestamp": datetime.now().isoformat(),
            "reflection_id": str(reflection.cycle_id),
            "changes": reflection.proposed_changes,
        }
    )
    memory.last_reflection = datetime.now()
    memory.reflection_cycles.append(reflection)
