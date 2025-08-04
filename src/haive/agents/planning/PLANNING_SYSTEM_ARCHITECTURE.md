# Planning System Architecture - Base Components and Multi-Agent Setup

**Status**: Work in Progress  
**Version**: 1.0  
**Last Updated**: 2025-01-29

## 🎯 Overview

We're building a sophisticated planning system from the ground up using modern Haive patterns. This document outlines our architecture, components, and the multi-agent coordination challenges we're solving.

## 🏗️ System Architecture

### Core Components

```
Planning System
├── base/
│   ├── models.py          # Advanced planning models with generics
│   ├── prompts.py         # Comprehensive system prompts  
│   └── agents/
│       ├── planner.py     # BasePlannerAgent (SimpleAgentV3)
│       └── executor.py    # BaseExecutorAgent (ReactAgent)
├── enhanced_plan_execute_v5.py  # Multi-agent orchestration
└── PLANNING_SYSTEM_ARCHITECTURE.md  # This document
```

### Agent Hierarchy

```
BasePlannerAgent (SimpleAgentV3)
    ↓ Creates BasePlan[PlanContent]
BaseExecutorAgent (ReactAgent + Tools)  
    ↓ Executes individual steps
Multi-Agent Coordinator (TBD)
    ↓ Orchestrates the workflow
```

## 🧠 Base Models - Maximum Flexibility Design

### Key Model Classes

**BasePlan[T]** - Generic plan supporting any content type:
```python
class BasePlan(IntelligentStatusMixin, Generic[T]):
    steps: IntelligentSequence[PlanContent]
    # PlanContent = Union[BasePlan[Any], BaseStep, List[BaseStep], Callable, str, Dict[str, Any], Any]
```

**BaseStep** - Individual actionable step:
```python
class BaseStep(IntelligentStatusMixin):
    step_id: str
    description: str
    # Note: Removing expected_outcome - too prescriptive
    tools_needed: List[str] 
    priority: Priority
    dependencies: List[str]
```

**IntelligentSequence** - Event-driven sequence with undo/redo:
- Auto-propagating status management
- Tree traversal with cycle detection
- Modifiable sequences with change tracking

## 🤖 Agent Design

### BasePlannerAgent (SimpleAgentV3)

**Configuration:**
```python
engine: AugLLMConfig(
    model="gpt-4o-mini",
    temperature=0.3,
    system_message=BASE_PLANNING_SYSTEM_MESSAGE  # Comprehensive strategic planning prompt
)

structured_output_model=BasePlan[PlanContent]
```

**Capabilities:**
- Deep objective analysis
- Strategic planning framework  
- Risk assessment and mitigation
- Resource optimization
- Comprehensive system prompts (2000+ words)

### BaseExecutorAgent (ReactAgent)

**Configuration:**
```python
engine: AugLLMConfig(
    model="gpt-4o-mini", 
    temperature=0.1,
    system_message=EXECUTOR_SYSTEM_MESSAGE  # Precision execution prompt
)

tools=[tavily_search_tool, tavily_qna, tavily_search_context]
```

**Capabilities:**
- Precise task execution
- Tool mastery (search-focused)
- Quality assurance and validation
- Detailed execution reporting

## 🚨 Current Challenge: Multi-Agent Setup

### The Problem

We need to properly coordinate these agents in a multi-agent system, but there are several architectural decisions to make:

**1. Step-by-Step Execution Flow:**
- How does the executor access the current step from the plan?
- How do we track which step is currently being executed?
- How do we pass context between steps?

**2. Prompt Template Integration:**
- The executor prompt needs access to plan model fields
- Current step details must be dynamically injected
- Previous results need to be accumulated and passed

**3. Multi-Agent State Management:**
- Shared state between planner and executor
- Progress tracking across the workflow
- Error handling and recovery

### Specific Technical Challenges

**A. ReactAgent in Multi-Agent Context:**
```python
# How should this work?
executor = BaseExecutorAgent(tools=[tavily_search_tool])

# In multi-agent workflow:
# 1. How does executor get current_step from plan?
# 2. How do we format the prompt with step details?
# 3. How do we track execution progress?
```

**B. Prompt Variable Mapping:**
```python
# Current executor prompt template:
"""Execute this specific step from our plan:

**Step to Execute:** {step_description}    # From BaseStep.description?
**Available Tools:** {available_tools}     # From executor.tools?
**Context from Previous Steps:** {previous_results}  # From where?
"""

# Questions:
# - How do we populate step_description from current BaseStep?
# - How do we accumulate previous_results?
# - How do we determine what tools are available?
```

**C. State Schema Design:**
```python
# What should our multi-agent state look like?
class PlanExecuteState(StateSchema):
    current_plan: BasePlan[PlanContent]
    current_step_id: str
    execution_results: List[???]  # What structure?
    completed_steps: List[str]
    # How do we track progress and pass data between agents?
```

## 🎯 Next Steps - Decision Points

### 1. State Schema Design
We need to design the state schema that will coordinate between planner and executor:

```python
class PlanExecuteState(StateSchema):
    # Plan data
    original_objective: str
    current_plan: Optional[BasePlan[PlanContent]]
    
    # Execution tracking  
    current_step_id: Optional[str]
    completed_steps: List[str]
    execution_results: List[???]  # What structure for results?
    
    # Progress and control
    iteration_count: int
    final_answer: Optional[str]
```

### 2. Step Execution Interface
How should the executor receive and process step information?

**Option A: Direct Step Object**
```python
# Pass the BaseStep object directly
current_step: BaseStep = plan.get_step(current_step_id)
executor_input = {
    "step": current_step,
    "previous_results": accumulated_results
}
```

**Option B: Flattened Step Data**
```python
# Extract step fields into flat structure
executor_input = {
    "step_description": current_step.description,
    "tools_needed": current_step.tools_needed,
    "step_priority": current_step.priority,
    "previous_results": accumulated_results
}
```

### 3. Multi-Agent Orchestration Pattern
Should we use:

**A. EnhancedMultiAgentV4** (existing pattern)
**B. Custom workflow with LangGraph**  
**C. Sequential agent calling**

### 4. Execution Result Structure
What should execution results look like?

```python
class ExecutionResult(BaseModel):
    step_id: str
    success: bool
    output: str  # The actual result content
    tools_used: List[str]
    execution_time: Optional[str]
    # What other fields do we need?
```

## 🔬 Prototyping Approach

### Phase 1: Simple Sequential Test
1. Create minimal state schema
2. Test planner → executor flow manually
3. Verify prompt template integration
4. Validate step execution and result capture

### Phase 2: Multi-Agent Integration  
1. Choose orchestration pattern
2. Implement state management
3. Add proper routing logic
4. Test end-to-end workflow

### Phase 3: Enhancement and Polish
1. Add error handling and recovery
2. Implement replanning logic  
3. Add comprehensive monitoring
4. Performance optimization

## 🤔 Open Questions

1. **Step Model Simplification**: Should `BaseStep` be simpler? Just `step_id` and `description`?

2. **Tool Integration**: How should `tools_needed` in `BaseStep` relate to actual executor tools?

3. **Result Accumulation**: How do we build context from previous step results?

4. **Error Handling**: What happens when a step fails? Replan? Retry? Skip?

5. **Parallel Execution**: Should we support parallel step execution in the future?

## 💡 Proposed Next Actions

1. **Simplify BaseStep model** - Remove complex fields, focus on core functionality
2. **Design minimal state schema** - Just what we need for basic coordination
3. **Create simple test workflow** - Planner → Executor → Results
4. **Iterate on prompt integration** - Make sure ReactAgent gets the right data
5. **Choose multi-agent pattern** - Pick one and implement it fully

## 📝 Notes and Considerations

- **Keep it simple first** - We can add complexity later
- **Focus on the core workflow** - Plan → Execute → Results  
- **Real component testing** - No mocks, test with actual LLMs
- **Document decisions** - Capture why we chose specific approaches

---

**Status**: Currently brainstorming the multi-agent coordination approach. Need to make decisions on state schema, prompt integration, and orchestration pattern before proceeding with implementation.