import re
from datetime import datetime
from typing import Literal
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, field_validator, model_validator
from haive.agents.memory.models_dir.meta import MemoryValidationMeta

class BaseMemoryModel(BaseModel):
    """Enhanced base memory model with sophisticated validation patterns
    and automatic metadata management.
    """
    memory_id: UUID = Field(default_factory=uuid4, description='Unique memory identifier')
    created_at: datetime = Field(default_factory=datetime.now, description='Creation timestamp')
    last_accessed: datetime = Field(default_factory=datetime.now, description='Last access timestamp')
    access_count: int = Field(default=0, ge=0, description='Number of times accessed')
    expires_at: datetime | None = Field(None, description='Expiration timestamp')
    is_archived: bool = Field(default=False, description='Archive status')
    priority_level: int = Field(default=1, ge=1, le=10, description='Memory priority (1-10)')
    checksum: str | None = Field(None, description='Data integrity checksum')
    validation_status: Literal['pending', 'validated', 'invalid', 'expired'] = Field(default='pending')
    tags: list[str] = Field(default_factory=list, description='Memory classification tags')
    relationships: dict[str, list[UUID]] = Field(default_factory=dict, description='Related memory IDs')

    class Config:
        """Enhanced model configuration."""
        validate_assignment = True
        arbitrary_types_allowed = True
        json_encoders = {datetime: lambda v: v.isoformat(), UUID: lambda v: str(v)}

    @field_validator('tags')
    @classmethod
    def validate_tags(cls, v: list[str]) -> list[str]:
        """Advanced tag validation with business rules."""
        if len(v) > 20:
            raise ValueError('Maximum 20 tags allowed')
        normalized_tags = []
        for tag in v:
            if not re.match('^[a-zA-Z0-9_-]+$', tag):
                raise ValueError(f'Invalid tag format: {tag}')
            normalized_tags.append(tag.lower().strip())
        return list(set(normalized_tags))

    @field_validator('priority_level')
    @classmethod
    def validate_priority(cls, v: int, info) -> int:
        """Dynamic priority validation based on memory type."""
        memory_type = getattr(cls, '__memory_type__', None)
        if memory_type == 'procedural' and v < 5:
            raise ValueError('Procedural memories must have priority >= 5')
        if memory_type == 'working' and v < 7:
            raise ValueError('Working memories must have priority >= 7')
        return v

    @model_validator(mode='after')
    def validate_lifecycle_consistency(self) -> 'BaseMemoryModel':
        """Cross-field lifecycle validation."""
        now = datetime.now()
        if self.expires_at and self.expires_at <= self.created_at:
            raise ValueError('Expiration time must be after creation time')
        if self.expires_at and now > self.expires_at:
            self.validation_status = 'expired'
            self.is_archived = True
        if hasattr(self, '_being_accessed'):
            self.last_accessed = now
            self.access_count += 1
        return self

    def mark_accessed(self) -> None:
        """Mark memory as being accessed for validation."""
        self._being_accessed = True
        self.__class__.model_validate(self.model_dump())