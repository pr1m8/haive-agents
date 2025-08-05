import re
from typing import Any
from pydantic import Field, field_validator, model_validator
from haive.agents.memory.models_dir.base import BaseMemoryModel
from haive.agents.memory.models_dir.semantic.mixins import TemporalMixin, UserContextMixin

class SemanticMemory(BaseMemoryModel, UserContextMixin, TemporalMixin):
    """Advanced semantic memory with comprehensive user modeling."""
    __memory_type__ = 'semantic'
    __validation_level__ = 'enterprise'
    user_id: str = Field(..., min_length=1, max_length=100, description='User identifier')
    personality_profile: PersonalityTraits = Field(default_factory=PersonalityTraits)
    preferences: UserPreferences = Field(default_factory=UserPreferences)
    factual_knowledge: dict[str, Any] = Field(default_factory=dict, description='Structured factual data')
    concept_graph: dict[str, list[str]] = Field(default_factory=dict, description='Concept relationships')
    belief_system: dict[str, float] = Field(default_factory=dict, description='Belief strengths (0-1)')
    temporal_weight: float = Field(default=1.0, ge=0.0, le=1.0, description='Temporal relevance weight')
    embedding_vector: list[float] | None = Field(None, description='Semantic embedding')
    semantic_keywords: list[str] = Field(default_factory=list, description='Optimized keywords')

    @field_validator('user_id')
    @classmethod
    def validate_user_id(cls, v: str) -> str:
        """Enhanced user ID validation."""
        if not re.match('^[a-zA-Z0-9_-]+$', v):
            raise ValueError('User ID must contain only alphanumeric characters, hyphens, and underscores')
        return v.lower()

    @field_validator('concept_graph')
    @classmethod
    def validate_concept_graph(cls, v: dict[str, list[str]]) -> dict[str, list[str]]:
        """Validate concept graph structure."""
        for concept, related in v.items():
            if len(related) > 50:
                raise ValueError(f"Concept '{concept}' has too many relations (max 50)")
            if concept in related:
                related.remove(concept)
        return v

    @model_validator(mode='after')
    def validate_semantic_consistency(self) -> 'SemanticMemory':
        """Advanced semantic consistency validation."""
        for belief, strength in self.belief_system.items():
            if not 0.0 <= strength <= 1.0:
                raise ValueError(f"Belief strength for '{belief}' must be between 0.0 and 1.0")
        if not self.semantic_keywords and self.factual_knowledge:
            self.semantic_keywords = self._extract_keywords(self.factual_knowledge)
        return self

    def _extract_keywords(self, data: dict[str, Any]) -> list[str]:
        """Extract semantic keywords from factual knowledge."""
        keywords = []
        for key, value in data.items():
            keywords.append(key.lower())
            if isinstance(value, str):
                words = re.findall('\\b[a-zA-Z]+\\b', value.lower())
                keywords.extend([w for w in words if len(w) > 3])
        return list(set(keywords))[:20]

    def get_context_summary(self) -> str:
        """Generate comprehensive context summary."""
        return f'\n        User: {self.user_id}\n        Communication Style: {self.personality_profile.communication_style}\n        Expertise: {', '.join(self.personality_profile.expertise_areas[:3])}\n        Recent Activity: {self.access_count} interactions\n        Temporal Relevance: {self.calculate_temporal_relevance():.2f}\n        Key Interests: {', '.join(self.preferences.topics_of_interest[:3])}\n        '

    def update_context(self, new_data: dict[str, Any]) -> None:
        """Intelligently update contextual information."""
        for key, value in new_data.items():
            if key in ['personality_traits', 'communication_style']:
                if hasattr(self.personality_profile, key):
                    setattr(self.personality_profile, key, value)
            elif key in ['preferences', 'privacy_level']:
                if hasattr(self.preferences, key):
                    setattr(self.preferences, key, value)
            else:
                self.factual_knowledge[key] = value
        self.semantic_keywords = self._extract_keywords(self.factual_knowledge)

# Standalone functions for export
def get_context_summary(memory: SemanticMemory) -> str:
    """Generate comprehensive context summary."""
    return memory.get_context_summary()

def update_context(memory: SemanticMemory, new_data: dict[str, Any]) -> None:
    """Intelligently update contextual information."""
    memory.update_context(new_data)

def validate_concept_graph(graph: dict[str, list[str]]) -> dict[str, list[str]]:
    """Validate conceptual relationship graph."""
    if len(graph) > 100:
        raise ValueError('Concept graph too large (max 100 nodes)')
    for concept, relations in graph.items():
        if len(relations) > 20:
            raise ValueError(f'Too many relations for concept {concept} (max 20)')
    return graph

def validate_semantic_consistency(memory: SemanticMemory) -> SemanticMemory:
    """Validate semantic memory consistency."""
    # Basic validation - can be extended
    if not memory.user_id:
        raise ValueError('User ID is required')
    return memory

def validate_user_id(user_id: str) -> str:
    """Validate user ID format."""
    if not user_id or not user_id.strip():
        raise ValueError('User ID cannot be empty')
    return user_id.strip()
