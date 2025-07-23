# Plan-and-Execute V3: Prompt Template to State Mapping

This document explains how the ChatPromptTemplate variables correspond to computed fields in PlanExecuteV3State.

## State Computed Fields → Prompt Variables

### Core State Fields

```python
# From PlanExecuteV3State computed fields:
@computed_field
@property
def objective(self) -> str:
    """Extract objective from plan or messages"""
    # Used in: {objective} in all prompts

@computed_field
@property
def current_step(self) -> Optional[str]:
    """Get formatted current step for executor"""
    # Used in: {current_step} in executor_prompt

@computed_field
@property
def plan_status(self) -> str:
    """Get formatted plan status for agents"""
    # Used in: {plan_status} in executor_prompt, evaluator_prompt

@computed_field
@property
def previous_results(self) -> str:
    """Get formatted previous step execution results"""
    # Used in: {previous_results} in executor_prompt

@computed_field
@property
def execution_summary(self) -> str:
    """Get summary of entire execution"""
    # Used in: {execution_summary} in evaluator_prompt, replanner_prompt

@computed_field
@property
def key_findings(self) -> List[str]:
    """Extract key findings from executions"""
    # Used in: {key_findings} in evaluator_prompt, replanner_prompt
```

## Prompt Template Usage

### 1. Planner Prompt

```python
planner_prompt = ChatPromptTemplate.from_messages([
    ("system", PLANNER_SYSTEM_MESSAGE),
    MessagesPlaceholder(variable_name="messages", optional=True),
    ("human", """Objective: {objective}
Please create a detailed execution plan...""")
])
```

**State mapping:** `{objective}` → `state.objective`

### 2. Executor Prompt

```python
executor_prompt = ChatPromptTemplate.from_messages([
    ("system", EXECUTOR_SYSTEM_MESSAGE),
    MessagesPlaceholder(variable_name="messages", optional=True),
    ("human", """Current Plan Status: {plan_status}
Current Step to Execute: {current_step}
Previous Steps Results: {previous_results}
Execute the current step...""")
])
```

**State mapping:**

- `{plan_status}` → `state.plan_status`
- `{current_step}` → `state.current_step`
- `{previous_results}` → `state.previous_results`

### 3. Evaluator Prompt

```python
evaluator_prompt = ChatPromptTemplate.from_messages([
    ("system", EVALUATOR_SYSTEM_MESSAGE),
    MessagesPlaceholder(variable_name="messages", optional=True),
    ("human", """Original Objective: {objective}
Execution Summary: {execution_summary}
Key Findings: {key_findings}
Plan Status: {plan_status}
Based on current state, evaluate progress...""")
])
```

**State mapping:**

- `{objective}` → `state.objective`
- `{execution_summary}` → `state.execution_summary`
- `{key_findings}` → `state.key_findings` (joined as string)
- `{plan_status}` → `state.plan_status`

### 4. Replanner Prompt

```python
replanner_prompt = ChatPromptTemplate.from_messages([
    ("system", REPLANNER_SYSTEM_MESSAGE),
    MessagesPlaceholder(variable_name="messages", optional=True),
    ("human", """Original Objective: {objective}
Previous Execution Summary: {execution_summary}
Key Findings from Previous Attempt: {key_findings}
Revision Notes: {revision_notes}
Create a revised plan...""")
])
```

**State mapping:**

- `{objective}` → `state.objective`
- `{execution_summary}` → `state.execution_summary`
- `{key_findings}` → `state.key_findings` (joined as string)
- `{revision_notes}` → from last evaluation's `revision_notes` field

## How State Fields Are Populated

### Automatic (Computed Fields)

- `objective`: Extracted from plan.objective or first human message
- `current_step`: Formatted from current_step_id + plan.steps
- `plan_status`: Generated from plan progress, step counts, next step
- `previous_results`: Formatted from last 5 step_executions
- `execution_summary`: Generated from plan progress, timing, errors
- `key_findings`: Extracted from step_executions.observations + evaluations

### Manual Updates

- `step_executions`: Added via `add_step_execution()`
- `evaluations`: Added via `add_evaluation()`
- `plan`: Updated via `revise_plan()`
- `current_step_id`: Set during execution flow

## Agent Integration Pattern

```python
# In Enhanced MultiAgent V3, agents receive state and extract needed fields:

# For planner:
planner_input = planner_prompt.format_messages(
    messages=state.messages,
    objective=state.objective
)

# For executor:
executor_input = executor_prompt.format_messages(
    messages=state.messages,
    plan_status=state.plan_status,
    current_step=state.current_step,
    previous_results=state.previous_results
)

# For evaluator:
evaluator_input = evaluator_prompt.format_messages(
    messages=state.messages,
    objective=state.objective,
    execution_summary=state.execution_summary,
    key_findings="\n".join(state.key_findings),
    plan_status=state.plan_status
)

# For replanner:
revision_notes = state.evaluations[-1].revision_notes if state.evaluations else ""
replanner_input = replanner_prompt.format_messages(
    messages=state.messages,
    objective=state.objective,
    execution_summary=state.execution_summary,
    key_findings="\n".join(state.key_findings),
    revision_notes=revision_notes
)
```

## Benefits of This Pattern

1. **Automatic State Formatting**: Computed fields auto-format complex state for prompts
2. **Consistent Data**: Same data formatting used across all agents
3. **Real-time Updates**: Computed fields always reflect current state
4. **Template Flexibility**: Easy to modify prompts without changing state logic
5. **Type Safety**: State schema ensures all required fields are available

## Key Implementation Notes

### 1. Use ChatPromptTemplate in Engine Configuration

**CRITICAL**: Use `engine.prompt_template` instead of `system_message`:

```python
# ✅ CORRECT - Use ChatPromptTemplate in engine config
planner_config = AugLLMConfig.model_copy(self.config)
planner_config.prompt_template = planner_prompt  # ChatPromptTemplate from prompts.py
self.planner = SimpleAgent(
    name=f"{name}_planner",
    engine=planner_config,
    structured_output_model=ExecutionPlan
)

# ❌ WRONG - Don't use system_message string
self.planner = SimpleAgent(
    name=f"{name}_planner",
    engine=self.config,
    system_message=PLANNER_SYSTEM_MESSAGE,  # This bypasses state field mapping
    structured_output_model=ExecutionPlan
)
```

### 2. State Field Auto-Population

The Enhanced MultiAgent V3 coordinator automatically calls `prompt.format_messages()` with the state fields, so individual agents don't need to handle this manually. The computed fields ensure the prompt variables are always populated with current, properly-formatted data.
