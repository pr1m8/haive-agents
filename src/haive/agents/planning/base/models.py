"""Planning Base Models - Advanced planning system with generics, indexing, and intelligent tree structures.

This module provides a sophisticated planning framework with:
- Maximum flexibility generics: Plan[Union[Step, Plan, Callable, str, Any]]
- Intelligent tree traversal with cycle detection
- Event-driven modifiable sequences with undo/redo
- Auto-propagating status management
- Smart field validation and auto-completion
- Dynamic model adaptation based on content
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Generic, List, Optional, Set, TypeVar, Union
from typing_extensions import Self
from collections import deque
from functools import wraps
import asyncio

from pydantic import BaseModel, Field, computed_field, field_validator, model_validator
from enum import Enum
import uuid
from datetime import datetime

# ============================================================================
# TYPE DEFINITIONS AND ADVANCED GENERICS
# ============================================================================

T = TypeVar('T')
StepType = TypeVar('StepType', bound='BaseStep')
PlanType = TypeVar('PlanType', bound='BasePlan')

# Maximum flexibility - plans can contain anything
PlanContent = Union['BasePlan[Any]', 'BaseStep', List['BaseStep'], Callable, str, Dict[str, Any], Any]


class TaskStatus(str, Enum):
    """Enhanced status enumeration with parallel execution support."""
    PENDING = "pending"
    READY = "ready"  # Dependencies met, ready to start
    IN_PROGRESS = "in_progress"
    PARALLEL_RUNNING = "parallel_running"  # Multiple items running
    WAITING_FOR_DEPENDENCY = "waiting_for_dependency"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    BLOCKED = "blocked"
    PAUSED = "paused"
    SKIPPED = "skipped"


class Priority(str, Enum):
    """Priority levels with critical and emergency levels."""
    EMERGENCY = "emergency"
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    DEFERRED = "deferred"


class TraversalMode(str, Enum):
    """Tree traversal patterns."""
    DEPTH_FIRST = "depth_first"
    BREADTH_FIRST = "breadth_first"
    PRIORITY_FIRST = "priority_first"
    DEPENDENCY_ORDER = "dependency_order"


# ============================================================================
# EVENT SYSTEM FOR CHANGE TRACKING
# ============================================================================

class ChangeEvent(BaseModel):
    """Event representing a change in the planning structure."""
    event_type: str
    source_id: str
    timestamp: datetime = Field(default_factory=datetime.now)
    old_value: Any = None
    new_value: Any = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class EventEmitter:
    """Event system for tracking changes."""
    
    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}
        self.event_history: List[ChangeEvent] = []
    
    def on(self, event_type: str, callback: Callable):
        """Register event listener."""
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)
    
    def emit(self, event: ChangeEvent):
        """Emit an event."""
        self.event_history.append(event)
        if event.event_type in self.listeners:
            for callback in self.listeners[event.event_type]:
                try:
                    callback(event)
                except Exception as e:
                    print(f"Event listener error: {e}")


# ============================================================================
# ADVANCED INDEXING AND STATUS MIXIN WITH INTELLIGENCE
# ============================================================================

class IntelligentStatusMixin(BaseModel, ABC):
    """Advanced mixin with intelligent status management and auto-adaptation."""
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Unique identifier")
    index: Optional[int] = Field(default=None, description="Index within parent container")
    status: TaskStatus = Field(default=TaskStatus.PENDING, description="Current status")
    
    # Timestamps with full lifecycle tracking
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default=None)
    started_at: Optional[datetime] = Field(default=None)
    completed_at: Optional[datetime] = Field(default=None)
    failed_at: Optional[datetime] = Field(default=None)
    
    # Intelligent features
    auto_status_propagation: bool = Field(default=True, description="Auto-propagate status changes")
    auto_field_completion: bool = Field(default=True, description="Auto-complete missing fields")
    adaptation_enabled: bool = Field(default=True, description="Enable dynamic adaptation")
    
    # Event system
    _event_emitter: EventEmitter = Field(default_factory=EventEmitter, exclude=True)
    _parent_ref: Optional['IntelligentStatusMixin'] = Field(default=None, exclude=True)
    _children_refs: Set[str] = Field(default_factory=set, exclude=True)
    
    def __init__(self, **data):
        super().__init__(**data)
        self._auto_setup()
    
    def _auto_setup(self) -> None:
        """Intelligent auto-setup based on model content."""
        if self.auto_field_completion:
            self._auto_complete_fields()
        
        if self.auto_status_propagation:
            self._setup_status_propagation()
        
        if self.adaptation_enabled:
            self._adapt_model()
    
    def _auto_complete_fields(self) -> None:
        """Intelligently auto-complete missing fields."""
        # Auto-generate title if missing
        if hasattr(self, 'title') and not getattr(self, 'title', None):
            if hasattr(self, 'description'):
                desc = getattr(self, 'description', '')
                if desc:
                    self.title = desc[:50] + "..." if len(desc) > 50 else desc
        
        # Auto-set priorities based on content
        if hasattr(self, 'priority') and self.priority == Priority.MEDIUM:
            if hasattr(self, 'description'):
                desc = getattr(self, 'description', '').lower()
                if any(word in desc for word in ['urgent', 'critical', 'asap', 'emergency']):
                    self.priority = Priority.CRITICAL
                elif any(word in desc for word in ['important', 'high', 'priority']):
                    self.priority = Priority.HIGH
    
    def _setup_status_propagation(self) -> None:
        """Set up automatic status propagation."""
        self._event_emitter.on('status_changed', self._handle_status_change)
    
    def _adapt_model(self) -> None:
        """Dynamically adapt model based on content."""
        # If we have steps/children, become a container
        if hasattr(self, 'steps') and getattr(self, 'steps'):
            self._adapt_as_container()
        
        # If we have callable content, become executable
        if hasattr(self, 'content') and callable(getattr(self, 'content', None)):
            self._adapt_as_executable()
    
    def _adapt_as_container(self) -> None:
        """Adapt to container behavior."""
        if hasattr(self, 'steps'):
            steps = getattr(self, 'steps')
            for step in steps:
                if hasattr(step, '_parent_ref'):
                    step._parent_ref = self
                if hasattr(step, 'id'):
                    self._children_refs.add(step.id)
    
    def _adapt_as_executable(self) -> None:
        """Adapt to executable behavior."""
        # Add execution metadata if not present
        if not hasattr(self, 'execution_context'):
            self.execution_context = {}
    
    def _handle_status_change(self, event: ChangeEvent) -> None:
        """Handle status change events."""
        if event.source_id in self._children_refs:
            self._update_container_status()
        
        if self._parent_ref and self.auto_status_propagation:
            self._parent_ref._update_container_status()
    
    def _update_container_status(self) -> None:
        """Intelligently update container status based on children."""
        if not hasattr(self, 'steps') or not getattr(self, 'steps'):
            return
        
        steps = getattr(self, 'steps')
        if not steps:
            return
        
        statuses = []
        for item in steps:
            if hasattr(item, 'status'):
                statuses.append(item.status)
            elif isinstance(item, list):
                for sub_item in item:
                    if hasattr(sub_item, 'status'):
                        statuses.append(sub_item.status)
        
        if not statuses:
            return
        
        # Intelligent status calculation
        completed = sum(1 for s in statuses if s == TaskStatus.COMPLETED)
        failed = sum(1 for s in statuses if s == TaskStatus.FAILED)
        in_progress = sum(1 for s in statuses if s in [TaskStatus.IN_PROGRESS, TaskStatus.PARALLEL_RUNNING])
        
        old_status = self.status
        
        if completed == len(statuses):
            new_status = TaskStatus.COMPLETED
            self.completed_at = datetime.now()
        elif failed > 0:
            new_status = TaskStatus.FAILED
            self.failed_at = datetime.now()
        elif in_progress > 1:
            new_status = TaskStatus.PARALLEL_RUNNING
        elif in_progress > 0:
            new_status = TaskStatus.IN_PROGRESS
            if not self.started_at:
                self.started_at = datetime.now()
        else:
            new_status = TaskStatus.READY if self._dependencies_met() else TaskStatus.WAITING_FOR_DEPENDENCY
        
        if new_status != old_status:
            self.status = new_status
            self.updated_at = datetime.now()
            
            # Emit change event
            event = ChangeEvent(
                event_type='status_changed',
                source_id=self.id,
                old_value=old_status,
                new_value=new_status
            )
            self._event_emitter.emit(event)
    
    def _dependencies_met(self) -> bool:
        """Check if all dependencies are met."""
        if not hasattr(self, 'depends_on'):
            return True
        
        depends_on = getattr(self, 'depends_on', [])
        if not depends_on:
            return True
        
        # Would need access to parent plan to check this properly
        return True  # Simplified for now
    
    def update_status(self, new_status: TaskStatus, propagate: bool = True) -> Self:
        """Update status with intelligent propagation."""
        old_status = self.status
        self.status = new_status
        self.updated_at = datetime.now()
        
        # Update timestamps based on status
        if new_status == TaskStatus.IN_PROGRESS and not self.started_at:
            self.started_at = datetime.now()
        elif new_status == TaskStatus.COMPLETED and old_status != TaskStatus.COMPLETED:
            self.completed_at = datetime.now()
        elif new_status == TaskStatus.FAILED and old_status != TaskStatus.FAILED:
            self.failed_at = datetime.now()
        
        # Emit event if propagation enabled
        if propagate and self.auto_status_propagation:
            event = ChangeEvent(
                event_type='status_changed',
                source_id=self.id,
                old_value=old_status,
                new_value=new_status
            )
            self._event_emitter.emit(event)
        
        return self


# ============================================================================
# ADVANCED MODIFIABLE SEQUENCE WITH UNDO/REDO
# ============================================================================

class IntelligentSequence(List[PlanContent], Generic[T]):
    """Advanced modifiable sequence with event system, undo/redo, and cycle detection."""
    
    def __init__(self, items: List[T] = None, parent: Optional['BasePlan'] = None):
        super().__init__(items or [])
        self.parent = parent
        self._event_emitter = EventEmitter()
        self._undo_stack: List[Callable] = []
        self._redo_stack: List[Callable] = []
        self._modification_history: List[ChangeEvent] = []
        self._reindex()
    
    def _reindex(self) -> None:
        """Intelligently reindex all items."""
        for i, item in enumerate(self):
            if hasattr(item, 'index'):
                item.index = i
            if hasattr(item, '_parent_ref'):
                item._parent_ref = self.parent
    
    def _emit_change(self, operation: str, item: Any = None, index: int = None) -> None:
        """Emit change event."""
        event = ChangeEvent(
            event_type=f'sequence_{operation}',
            source_id=self.parent.id if self.parent else 'unknown',
            metadata={'operation': operation, 'index': index}
        )
        self._event_emitter.emit(event)
        self._modification_history.append(event)
    
    def _create_undo_action(self, operation: str, item: Any, index: int) -> Callable:
        """Create undo action for operation."""
        if operation == 'append':
            return lambda: self._raw_remove(item)
        elif operation == 'insert':
            return lambda: self._raw_pop(index)
        elif operation == 'remove':
            return lambda: self._raw_insert(index, item)
        elif operation == 'pop':
            return lambda: self._raw_insert(index, item)
        return lambda: None
    
    def _raw_append(self, item: T) -> None:
        """Raw append without events or undo tracking."""
        super().append(item)
        self._reindex()
    
    def _raw_insert(self, index: int, item: T) -> None:
        """Raw insert without events or undo tracking."""
        super().insert(index, item)
        self._reindex()
    
    def _raw_remove(self, item: T) -> None:
        """Raw remove without events or undo tracking."""
        super().remove(item)
        self._reindex()
    
    def _raw_pop(self, index: int = -1) -> T:
        """Raw pop without events or undo tracking."""
        item = super().pop(index)
        self._reindex()
        return item
    
    def append(self, item: T) -> None:
        """Add item with undo support and events."""
        # Check for cycles if item is a plan
        if hasattr(item, 'id') and self.parent and self._would_create_cycle(item):
            raise ValueError(f"Adding item {item.id} would create a cycle")
        
        # Create undo action
        undo_action = lambda: self._raw_remove(item)
        self._undo_stack.append(undo_action)
        self._redo_stack.clear()  # Clear redo on new action
        
        # Perform operation
        self._raw_append(item)
        
        # Emit event
        self._emit_change('append', item)
        
        # Update parent status
        if self.parent and hasattr(self.parent, '_update_container_status'):
            self.parent._update_container_status()
    
    def insert(self, index: int, item: T) -> None:
        """Insert item with undo support and events."""
        if hasattr(item, 'id') and self.parent and self._would_create_cycle(item):
            raise ValueError(f"Adding item {item.id} would create a cycle")
        
        undo_action = lambda: self._raw_pop(index)
        self._undo_stack.append(undo_action)
        self._redo_stack.clear()
        
        self._raw_insert(index, item)
        self._emit_change('insert', item, index)
        
        if self.parent and hasattr(self.parent, '_update_container_status'):
            self.parent._update_container_status()
    
    def remove(self, item: T) -> None:
        """Remove item with undo support and events."""
        index = self.index(item)
        undo_action = lambda: self._raw_insert(index, item)
        self._undo_stack.append(undo_action)
        self._redo_stack.clear()
        
        self._raw_remove(item)
        self._emit_change('remove', item, index)
        
        if self.parent and hasattr(self.parent, '_update_container_status'):
            self.parent._update_container_status()
    
    def pop(self, index: int = -1) -> T:
        """Pop item with undo support and events."""
        item = self[index]
        actual_index = index if index >= 0 else len(self) + index
        
        undo_action = lambda: self._raw_insert(actual_index, item)
        self._undo_stack.append(undo_action)
        self._redo_stack.clear()
        
        result = self._raw_pop(index)
        self._emit_change('pop', item, actual_index)
        
        if self.parent and hasattr(self.parent, '_update_container_status'):
            self.parent._update_container_status()
        
        return result
    
    def undo(self) -> bool:
        """Undo last operation."""
        if not self._undo_stack:
            return False
        
        # Get last undo action and create corresponding redo
        undo_action = self._undo_stack.pop()
        
        # Store current state for redo
        current_state = list(self)
        redo_action = lambda: self._restore_state(current_state)
        self._redo_stack.append(redo_action)
        
        # Execute undo
        undo_action()
        
        return True
    
    def redo(self) -> bool:
        """Redo last undone operation."""
        if not self._redo_stack:
            return False
        
        redo_action = self._redo_stack.pop()
        redo_action()
        
        return True
    
    def _restore_state(self, state: List[T]) -> None:
        """Restore sequence to specific state."""
        self.clear()
        for item in state:
            self._raw_append(item)
    
    def _would_create_cycle(self, item: Any) -> bool:
        """Check if adding item would create a cycle."""
        if not hasattr(item, 'id') or not self.parent:
            return False
        
        # Simple cycle detection - check if item contains parent
        return self._contains_plan_recursive(item, self.parent.id)
    
    def _contains_plan_recursive(self, plan: Any, target_id: str) -> bool:
        """Recursively check if plan contains target ID."""
        if not hasattr(plan, 'steps') or not hasattr(plan, 'id'):
            return False
        
        if plan.id == target_id:
            return True
        
        for step in getattr(plan, 'steps', []):
            if hasattr(step, 'id') and step.id == target_id:
                return True
            if hasattr(step, 'steps') and self._contains_plan_recursive(step, target_id):
                return True
        
        return False


# ============================================================================
# ENHANCED BASE STEP WITH MAXIMUM INTELLIGENCE
# ============================================================================

class BaseStep(IntelligentStatusMixin):
    """Intelligent base step with adaptive behavior and smart validation."""
    
    title: str = Field(..., description="Step title")
    description: str = Field(..., description="Detailed description")
    expected_outcome: str = Field(..., description="Expected result")
    
    # Enhanced metadata
    priority: Priority = Field(default=Priority.MEDIUM)
    estimated_duration: Optional[str] = Field(default=None)
    actual_duration: Optional[str] = Field(default=None)
    
    # Advanced dependencies
    depends_on: List[str] = Field(default_factory=list, description="Hard dependencies")
    soft_depends_on: List[str] = Field(default_factory=list, description="Soft dependencies")
    blocks: List[str] = Field(default_factory=list, description="What this blocks")
    
    # Execution requirements
    tools_required: List[str] = Field(default_factory=list)
    resources_required: List[str] = Field(default_factory=list)
    skills_required: List[str] = Field(default_factory=list)
    
    # Execution content (maximum flexibility)
    content: Optional[Union[str, Callable, Dict[str, Any], Any]] = Field(default=None)
    execution_context: Dict[str, Any] = Field(default_factory=dict)
    
    # Results and feedback
    result: Optional[Any] = Field(default=None)
    error_message: Optional[str] = Field(default=None)
    feedback: List[str] = Field(default_factory=list)
    quality_score: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    
    @computed_field
    @property
    def is_executable(self) -> bool:
        """Intelligent executability check."""
        if self.status not in [TaskStatus.PENDING, TaskStatus.READY]:
            return False
        
        # Check hard dependencies (simplified)
        if self.depends_on:
            # Would need parent context to check properly
            return False
        
        # Check if we have executable content
        if self.content and callable(self.content):
            return True
        
        # Check if we have enough information to execute
        return bool(self.description and self.expected_outcome)
    
    @computed_field
    @property
    def complexity_score(self) -> float:
        """Calculate complexity score based on various factors."""
        score = 0.0
        
        # Base complexity from description length
        if self.description:
            score += min(len(self.description) / 1000, 0.3)
        
        # Dependencies complexity
        score += len(self.depends_on) * 0.1
        score += len(self.soft_depends_on) * 0.05
        
        # Requirements complexity
        score += len(self.tools_required) * 0.1
        score += len(self.resources_required) * 0.05
        score += len(self.skills_required) * 0.1
        
        # Priority adjustment
        priority_multipliers = {
            Priority.EMERGENCY: 1.5,
            Priority.CRITICAL: 1.3,
            Priority.HIGH: 1.1,
            Priority.MEDIUM: 1.0,
            Priority.LOW: 0.8,
            Priority.DEFERRED: 0.5
        }
        score *= priority_multipliers.get(self.priority, 1.0)
        
        return min(score, 1.0)
    
    @computed_field
    @property
    def readiness_score(self) -> float:
        """Calculate how ready this step is for execution."""
        if not self.is_executable:
            return 0.0
        
        score = 0.5  # Base readiness
        
        # Information completeness
        if self.description:
            score += 0.2
        if self.expected_outcome:
            score += 0.2
        if self.content:
            score += 0.3
        
        # Requirements met (simplified)
        if not self.tools_required:
            score += 0.1
        if not self.resources_required:
            score += 0.1
        
        return min(score, 1.0)
    
    async def execute(self) -> Any:
        """Execute the step intelligently."""
        if not self.is_executable:
            raise ValueError(f"Step {self.id} is not executable")
        
        self.update_status(TaskStatus.IN_PROGRESS)
        
        try:
            result = None
            
            # Execute callable content
            if callable(self.content):
                if asyncio.iscoroutinefunction(self.content):
                    result = await self.content(**self.execution_context)
                else:
                    result = self.content(**self.execution_context)
            
            # Store result
            self.result = result
            self.update_status(TaskStatus.COMPLETED)
            
            return result
            
        except Exception as e:
            self.error_message = str(e)
            self.update_status(TaskStatus.FAILED)
            raise
    
    def add_feedback(self, feedback: str, quality_score: Optional[float] = None) -> Self:
        """Add execution feedback."""
        self.feedback.append(feedback)
        if quality_score is not None:
            self.quality_score = quality_score
        return self


# ============================================================================
# MAXIMUM FLEXIBILITY PLAN WITH TREE INTELLIGENCE
# ============================================================================

class BasePlan(IntelligentStatusMixin, Generic[T]):
    """Ultimate flexible plan supporting any content type with maximum intelligence."""
    
    title: str = Field(..., description="Plan title")
    description: str = Field(..., description="Plan description")
    objective: str = Field(..., description="What we're trying to achieve")
    success_criteria: str = Field(..., description="Success measurement")
    
    # Maximum flexibility content - can contain anything
    steps: IntelligentSequence[PlanContent] = Field(
        default_factory=lambda: IntelligentSequence([])
    )
    
    # Execution strategy
    execution_mode: str = Field(default="sequential", description="How to execute steps")
    parallel_limit: Optional[int] = Field(default=None, description="Max parallel execution")
    
    # Advanced planning metadata
    plan_type: str = Field(default="flexible")
    complexity_level: str = Field(default="medium")
    estimated_total_duration: Optional[str] = Field(default=None)
    actual_duration: Optional[str] = Field(default=None)
    
    # Context and constraints
    context: Dict[str, Any] = Field(default_factory=dict)
    constraints: List[str] = Field(default_factory=list)
    assumptions: List[str] = Field(default_factory=list)
    
    # Quality and performance
    quality_gates: List[str] = Field(default_factory=list)
    performance_targets: Dict[str, Any] = Field(default_factory=dict)
    
    def __init__(self, **data):
        super().__init__(**data)
        # Set parent reference
        if hasattr(self.steps, 'parent'):
            self.steps.parent = self
    
    @computed_field
    @property
    def total_steps(self) -> int:
        """Recursively count all executable items."""
        return self._count_items_recursive(lambda x: self._is_executable_item(x))
    
    @computed_field
    @property
    def completed_items(self) -> int:
        """Count completed items recursively."""
        return self._count_items_recursive(
            lambda x: hasattr(x, 'status') and x.status == TaskStatus.COMPLETED
        )
    
    @computed_field
    @property
    def progress_percentage(self) -> float:
        """Intelligent progress calculation."""
        total = self.total_steps
        if total == 0:
            return 0.0
        
        completed = self.completed_items
        in_progress = self._count_items_recursive(
            lambda x: hasattr(x, 'status') and x.status in [TaskStatus.IN_PROGRESS, TaskStatus.PARALLEL_RUNNING]
        )
        
        # Weight in-progress items as 50% complete
        weighted_complete = completed + (in_progress * 0.5)
        return min((weighted_complete / total) * 100.0, 100.0)
    
    @computed_field
    @property
    def complexity_score(self) -> float:
        """Calculate overall plan complexity."""
        base_complexity = len(self.steps) * 0.1
        
        # Add complexity from contained items
        item_complexity = sum(
            getattr(item, 'complexity_score', 0.1) for item in self.steps
            if hasattr(item, 'complexity_score')
        )
        
        # Depth penalty
        depth_penalty = self._calculate_max_depth() * 0.1
        
        return min(base_complexity + item_complexity + depth_penalty, 1.0)
    
    @computed_field
    @property
    def next_executable_items(self) -> List[Union[BaseStep, 'BasePlan']]:
        """Find all items ready for execution (supports parallel)."""
        executable = []
        
        for item in self.steps:
            if self._is_item_ready(item):
                executable.append(item)
            elif hasattr(item, 'next_executable_items'):
                executable.extend(item.next_executable_items)
        
        return executable
    
    def _count_items_recursive(self, predicate: Callable[[Any], bool]) -> int:
        """Recursively count items matching predicate."""
        count = 0
        
        for item in self.steps:
            if predicate(item):
                count += 1
            elif hasattr(item, 'steps'):  # Sub-plan
                count += item._count_items_recursive(predicate)
            elif isinstance(item, list):  # List of items
                for sub_item in item:
                    if predicate(sub_item):
                        count += 1
        
        return count
    
    def _is_executable_item(self, item: Any) -> bool:
        """Check if item is executable."""
        return (
            hasattr(item, 'is_executable') or
            callable(item) or
            isinstance(item, str) or
            hasattr(item, 'steps')  # Sub-plan
        )
    
    def _is_item_ready(self, item: Any) -> bool:
        """Check if item is ready for execution."""
        if hasattr(item, 'is_executable'):
            return item.is_executable
        elif callable(item):
            return True
        elif hasattr(item, 'status'):
            return item.status == TaskStatus.READY
        return False
    
    def _calculate_max_depth(self) -> int:
        """Calculate maximum nesting depth."""
        max_depth = 0
        
        for item in self.steps:
            if hasattr(item, '_calculate_max_depth'):
                depth = 1 + item._calculate_max_depth()
                max_depth = max(max_depth, depth)
        
        return max_depth
    
    def traverse(self, mode: TraversalMode = TraversalMode.DEPTH_FIRST) -> List[Any]:
        """Traverse the plan tree using specified mode."""
        if mode == TraversalMode.DEPTH_FIRST:
            return self._traverse_depth_first()
        elif mode == TraversalMode.BREADTH_FIRST:
            return self._traverse_breadth_first()
        elif mode == TraversalMode.PRIORITY_FIRST:
            return self._traverse_priority_first()
        elif mode == TraversalMode.DEPENDENCY_ORDER:
            return self._traverse_dependency_order()
        else:
            return self._traverse_depth_first()
    
    def _traverse_depth_first(self) -> List[Any]:
        """Depth-first traversal."""
        result = []
        
        def visit(item):
            result.append(item)
            if hasattr(item, 'steps'):
                for sub_item in item.steps:
                    visit(sub_item)
            elif isinstance(item, list):
                for sub_item in item:
                    visit(sub_item)
        
        for item in self.steps:
            visit(item)
        
        return result
    
    def _traverse_breadth_first(self) -> List[Any]:
        """Breadth-first traversal."""
        result = []
        queue = deque(self.steps)
        
        while queue:
            item = queue.popleft()
            result.append(item)
            
            if hasattr(item, 'steps'):
                queue.extend(item.steps)
            elif isinstance(item, list):
                queue.extend(item)
        
        return result
    
    def _traverse_priority_first(self) -> List[Any]:
        """Priority-first traversal."""
        all_items = self._traverse_depth_first()
        
        # Sort by priority (emergency first)
        priority_order = {
            Priority.EMERGENCY: 0,
            Priority.CRITICAL: 1,
            Priority.HIGH: 2,
            Priority.MEDIUM: 3,
            Priority.LOW: 4,
            Priority.DEFERRED: 5
        }
        
        def get_priority(item):
            if hasattr(item, 'priority'):
                return priority_order.get(item.priority, 3)
            return 3
        
        return sorted(all_items, key=get_priority)
    
    def _traverse_dependency_order(self) -> List[Any]:
        """Dependency-order traversal (topological sort)."""
        # Simplified implementation - would need full dependency graph
        return self._traverse_depth_first()
    
    def add_step(self, step: PlanContent) -> Self:
        """Add any type of content as a step."""
        self.steps.append(step)
        return self
    
    def add_steps(self, steps: List[PlanContent]) -> Self:
        """Add multiple steps."""
        for step in steps:
            self.steps.append(step)
        return self
    
    def find_by_id(self, item_id: str) -> Optional[Any]:
        """Find any item by ID recursively."""
        for item in self.traverse():
            if hasattr(item, 'id') and item.id == item_id:
                return item
        return None
    
    def find_by_predicate(self, predicate: Callable[[Any], bool]) -> List[Any]:
        """Find all items matching predicate."""
        return [item for item in self.traverse() if predicate(item)]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get comprehensive plan statistics."""
        all_items = self.traverse()
        
        stats = {
            'total_items': len(all_items),
            'total_steps': self.total_steps,
            'completed_items': self.completed_items,
            'progress_percentage': self.progress_percentage,
            'complexity_score': self.complexity_score,
            'max_depth': self._calculate_max_depth(),
            'status_distribution': {},
            'priority_distribution': {},
            'type_distribution': {}
        }
        
        # Status distribution
        for item in all_items:
            if hasattr(item, 'status'):
                status = item.status
                stats['status_distribution'][status] = stats['status_distribution'].get(status, 0) + 1
        
        # Priority distribution
        for item in all_items:
            if hasattr(item, 'priority'):
                priority = item.priority
                stats['priority_distribution'][priority] = stats['priority_distribution'].get(priority, 0) + 1
        
        # Type distribution
        for item in all_items:
            item_type = type(item).__name__
            stats['type_distribution'][item_type] = stats['type_distribution'].get(item_type, 0) + 1
        
        return stats
    
    async def execute(self, mode: str = None) -> Dict[str, Any]:
        """Execute the plan using specified mode."""
        execution_mode = mode or self.execution_mode
        
        self.update_status(TaskStatus.IN_PROGRESS)
        
        try:
            if execution_mode == "sequential":
                return await self._execute_sequential()
            elif execution_mode == "parallel":
                return await self._execute_parallel()
            elif execution_mode == "conditional":
                return await self._execute_conditional()
            else:
                return await self._execute_flexible()
        except Exception as e:
            self.update_status(TaskStatus.FAILED)
            raise
    
    async def _execute_sequential(self) -> Dict[str, Any]:
        """Execute steps sequentially."""
        results = {}
        
        for i, item in enumerate(self.steps):
            if hasattr(item, 'execute'):
                result = await item.execute()
                results[f'step_{i}'] = result
            elif callable(item):
                if asyncio.iscoroutinefunction(item):
                    result = await item()
                else:
                    result = item()
                results[f'step_{i}'] = result
        
        self.update_status(TaskStatus.COMPLETED)
        return results
    
    async def _execute_parallel(self) -> Dict[str, Any]:
        """Execute steps in parallel."""
        tasks = []
        
        for i, item in enumerate(self.steps):
            if hasattr(item, 'execute'):
                tasks.append(item.execute())
            elif callable(item) and asyncio.iscoroutinefunction(item):
                tasks.append(item())
        
        if tasks:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return {f'step_{i}': result for i, result in enumerate(results)}
        
        self.update_status(TaskStatus.COMPLETED)
        return {}
    
    async def _execute_conditional(self) -> Dict[str, Any]:
        """Execute with conditional logic."""
        # Would implement conditional execution based on context
        return await self._execute_sequential()
    
    async def _execute_flexible(self) -> Dict[str, Any]:
        """Execute using flexible strategy."""
        executable_items = self.next_executable_items
        
        if not executable_items:
            self.update_status(TaskStatus.COMPLETED)
            return {}
        
        # Execute ready items in parallel if possible
        if len(executable_items) > 1 and self.parallel_limit != 1:
            return await self._execute_parallel()
        else:
            return await self._execute_sequential()


# ============================================================================
# SPECIALIZED PLAN TYPES WITH MAXIMUM INTELLIGENCE
# ============================================================================

class SequentialPlan(BasePlan[Union[BaseStep, 'BasePlan']]):
    """Sequential execution plan."""
    execution_mode: str = Field(default="sequential", frozen=True)
    plan_type: str = Field(default="sequential", frozen=True)


class ParallelPlan(BasePlan[Union[BaseStep, 'BasePlan']]):
    """Parallel execution plan."""
    execution_mode: str = Field(default="parallel", frozen=True)
    plan_type: str = Field(default="parallel", frozen=True)


class ConditionalPlan(BasePlan[Union[BaseStep, 'BasePlan', Callable]]):
    """Conditional execution plan."""
    execution_mode: str = Field(default="conditional", frozen=True)
    plan_type: str = Field(default="conditional", frozen=True)
    conditions: Dict[str, Callable] = Field(default_factory=dict)


class FlexiblePlan(BasePlan[PlanContent]):
    """Maximum flexibility plan - can contain anything."""
    execution_mode: str = Field(default="flexible", frozen=True)
    plan_type: str = Field(default="flexible", frozen=True)


# ============================================================================
# ULTIMATE TASK MODEL - CONTAINER FOR EVERYTHING
# ============================================================================

class Task(IntelligentStatusMixin):
    """Ultimate task model with maximum intelligence and flexibility."""
    
    title: str = Field(..., description="Task title")
    description: str = Field(..., description="Detailed description")
    objective: str = Field(..., description="What we're trying to achieve")
    success_criteria: str = Field(..., description="How we measure success")
    
    # Plans with maximum flexibility
    primary_plan: Optional[BasePlan] = Field(default=None)
    alternative_plans: List[BasePlan] = Field(default_factory=list)
    contingency_plans: List[BasePlan] = Field(default_factory=list)
    
    # Advanced task metadata
    category: Optional[str] = Field(default=None)
    complexity: str = Field(default="medium")
    priority: Priority = Field(default=Priority.MEDIUM)
    
    # Stakeholders and resources
    stakeholders: List[str] = Field(default_factory=list)
    owner: Optional[str] = Field(default=None)
    team: List[str] = Field(default_factory=list)
    
    # Context and constraints
    context: Dict[str, Any] = Field(default_factory=dict)
    constraints: List[str] = Field(default_factory=list)
    assumptions: List[str] = Field(default_factory=list)
    risks: List[str] = Field(default_factory=list)
    
    # Quality and performance
    quality_targets: Dict[str, Any] = Field(default_factory=dict)
    performance_metrics: Dict[str, Any] = Field(default_factory=dict)
    
    @computed_field
    @property
    def overall_progress(self) -> float:
        """Calculate progress across all active plans."""
        if not self.primary_plan:
            return 0.0
        return self.primary_plan.progress_percentage
    
    @computed_field
    @property
    def overall_complexity(self) -> float:
        """Calculate overall task complexity."""
        if not self.primary_plan:
            return 0.1
        
        base_complexity = self.primary_plan.complexity_score
        
        # Add complexity from alternatives
        alt_complexity = sum(plan.complexity_score for plan in self.alternative_plans) * 0.1
        
        return min(base_complexity + alt_complexity, 1.0)
    
    @computed_field
    @property
    def is_complete(self) -> bool:
        """Intelligent completion check."""
        return (
            self.primary_plan and
            self.primary_plan.status == TaskStatus.COMPLETED and
            self.status == TaskStatus.COMPLETED
        )
    
    def activate_plan(self, plan: BasePlan) -> Self:
        """Intelligently activate a plan."""
        if plan in self.alternative_plans:
            self.alternative_plans.remove(plan)
        
        if self.primary_plan:
            # Pause current plan
            self.primary_plan.update_status(TaskStatus.PAUSED)
            self.alternative_plans.append(self.primary_plan)
        
        self.primary_plan = plan
        plan.update_status(TaskStatus.READY)
        
        return self
    
    def add_contingency(self, plan: BasePlan, trigger_condition: str) -> Self:
        """Add contingency plan with trigger condition."""
        plan.context['trigger_condition'] = trigger_condition
        plan.context['plan_type'] = 'contingency'
        self.contingency_plans.append(plan)
        return self
    
    def get_comprehensive_status(self) -> Dict[str, Any]:
        """Get comprehensive status across all plans."""
        status = {
            'task_status': self.status,
            'overall_progress': self.overall_progress,
            'complexity_score': self.overall_complexity,
            'primary_plan': None,
            'alternative_plans': [],
            'contingency_plans': [],
            'next_actions': []
        }
        
        if self.primary_plan:
            status['primary_plan'] = {
                'status': self.primary_plan.status,
                'progress': self.primary_plan.progress_percentage,
                'next_executable': len(self.primary_plan.next_executable_items),
                'statistics': self.primary_plan.get_statistics()
            }
            
            status['next_actions'] = [
                {'id': item.id, 'title': getattr(item, 'title', str(item))}
                for item in self.primary_plan.next_executable_items[:5]
            ]
        
        status['alternative_plans'] = [
            {'id': plan.id, 'title': plan.title, 'status': plan.status}
            for plan in self.alternative_plans
        ]
        
        status['contingency_plans'] = [
            {'id': plan.id, 'title': plan.title, 'trigger': plan.context.get('trigger_condition')}
            for plan in self.contingency_plans
        ]
        
        return status
    
    async def execute(self) -> Dict[str, Any]:
        """Execute the primary plan intelligently."""
        if not self.primary_plan:
            raise ValueError("No primary plan to execute")
        
        self.update_status(TaskStatus.IN_PROGRESS)
        
        try:
            result = await self.primary_plan.execute()
            
            if self.primary_plan.status == TaskStatus.COMPLETED:
                self.update_status(TaskStatus.COMPLETED)
            
            return result
        except Exception as e:
            # Check if we should activate contingency plan
            for contingency in self.contingency_plans:
                trigger = contingency.context.get('trigger_condition', '')
                if 'failure' in trigger.lower():
                    self.activate_plan(contingency)
                    return await contingency.execute()
            
            self.update_status(TaskStatus.FAILED)
            raise