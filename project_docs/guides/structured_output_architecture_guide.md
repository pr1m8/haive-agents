# Structured Output Architecture Guide for Haive Agents

**Created**: 2025-01-30
**Purpose**: Document how structured output models work across the agent hierarchy
**Status**: Analysis complete

## Overview

This guide explains how structured output models are handled across the different agent classes in Haive, and how to properly implement multi-agent systems with structured output transfer.

## Architecture Hierarchy

```
Agent (base class in haive-core)
├── SimpleAgent (in haive-agents)
│   └── ReactAgent (extends SimpleAgent)
└── MultiAgent (in haive-agents)
```

## Where Structured Output is Defined

### 1. **Engine Level (AugLLMConfig)**

The structured output model is primarily configured at the **engine level** in `AugLLMConfig`:

```python
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel

class MyOutput(BaseModel):
    result: str
    confidence: float

# Structured output is set on the engine
engine = AugLLMConfig(
    structured_output_model=MyOutput,
    temperature=0.7
)
```

Key points:

- `AugLLMConfig.structured_output_model` is where the Pydantic model is specified
- The engine handles tool route synchronization (`'my_output'` → `'parse_output'` route)
- This is inherited by ALL agent types through their engine

### 2. **Agent Convenience Fields**

Both SimpleAgent and ReactAgent provide **convenience fields** that sync to the engine:

```python
# SimpleAgent fields (inherited by ReactAgent)
class SimpleAgent(Agent[AugLLMConfig]):
    structured_output_model: type[BaseModel] | None = Field(
        default=None,
        description="Structured output model (syncs to engine, triggers recompile + hooks)"
    )
```

This allows two patterns:

```python
# Pattern 1: Set on engine directly
agent = SimpleAgent(
    name="agent1",
    engine=AugLLMConfig(structured_output_model=MyOutput)
)

# Pattern 2: Set via convenience field (syncs to engine)
agent = SimpleAgent(
    name="agent2",
    structured_output_model=MyOutput  # This syncs to engine.structured_output_model
)
```

### 3. **MultiAgent Considerations**

MultiAgent does NOT have its own structured output model. Instead:

- Each sub-agent has its own engine with its own structured output model
- MultiAgent coordinates the execution flow between agents
- State transfer happens through `MultiAgentState`

## Structured Output Flow

### 1. Single Agent Flow

```
User Input → Agent → Engine (with structured_output_model) → Pydantic Validation → Structured Output
```

### 2. Multi-Agent Sequential Flow

```
Input → Agent1 → Output1 (structured) → Agent2 → Output2 (structured) → Final Result
         ↑                                ↑
         Engine1                          Engine2
         (Model1)                        (Model2)
```

## Correct Multi-Agent Implementation

### Problem with Current Approach

The test examples were creating separate agents and calling them independently:

```python
# ❌ WRONG - Just sequential calls, not true multi-agent
agent1 = SimpleAgent(...)
result1 = agent1.run(input)

agent2 = SimpleAgent(...)
result2 = agent2.run(result1)  # Manual transfer
```

### Correct Approach - True MultiAgent

```python
# ✅ CORRECT - MultiAgent orchestrates sub-agents
from haive.agents.multi.agent import MultiAgent

# Define structured outputs for each agent
class AnalysisResult(BaseModel):
    findings: List[str]
    confidence: float

class FinalReport(BaseModel):
    summary: str
    recommendations: List[str]

# Create agents with their own structured outputs
analyzer = SimpleAgent(
    name="analyzer",
    engine=AugLLMConfig(
        structured_output_model=AnalysisResult,
        temperature=0.7
    )
)

reporter = SimpleAgent(
    name="reporter",
    engine=AugLLMConfig(
        structured_output_model=FinalReport,
        temperature=0.5
    )
)

# Create MultiAgent to orchestrate them
workflow = MultiAgent(
    name="analysis_workflow",
    agents=[analyzer, reporter],
    execution_mode="sequential"
)

# Execute as a single unit
result = workflow.run("Analyze this data")
```

## Key Implementation Details

### 1. State Management

MultiAgent uses `MultiAgentState` which provides:

- Shared state across agents
- Private state per agent
- Message passing between agents

### 2. AgentNodeV3 Integration

Each agent in MultiAgent is wrapped in `AgentNodeV3` which:

- Projects the full MultiAgentState to agent-specific state
- Handles structured output updates
- Manages recompilation tracking

### 3. Execution Modes

MultiAgent supports different execution patterns:

- **Sequential**: Agent1 → Agent2 → Agent3
- **Parallel**: All agents run simultaneously
- **Conditional**: Routing based on conditions
- **Manual**: Custom edge configuration

## Example: Complete Multi-Agent with Structured Output

```python
from haive.agents.simple.agent import SimpleAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.multi.agent import MultiAgent
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field
from typing import List

# Step 1: Define structured outputs
class ResearchPlan(BaseModel):
    """Output from planning agent"""
    objectives: List[str]
    methodology: str
    priority: str

class ResearchData(BaseModel):
    """Output from research agent"""
    findings: List[str]
    sources: List[str]
    confidence: float

class FinalReport(BaseModel):
    """Output from reporting agent"""
    executive_summary: str
    detailed_findings: List[str]
    recommendations: List[str]
    next_steps: List[str]

# Step 2: Create agents with structured outputs
planner = SimpleAgent(
    name="planner",
    engine=AugLLMConfig(
        structured_output_model=ResearchPlan,
        temperature=0.7,
        system_message="You are a research planning expert."
    )
)

researcher = ReactAgent(
    name="researcher",
    engine=AugLLMConfig(
        structured_output_model=ResearchData,
        temperature=0.6,
        tools=[web_search, data_analyzer],
        system_message="You are a thorough researcher."
    )
)

reporter = SimpleAgent(
    name="reporter",
    engine=AugLLMConfig(
        structured_output_model=FinalReport,
        temperature=0.5,
        system_message="You are a professional report writer."
    )
)

# Step 3: Create MultiAgent workflow
research_workflow = MultiAgent(
    name="complete_research_workflow",
    agents=[planner, researcher, reporter],
    execution_mode="sequential"
)

# Step 4: Execute the workflow
result = research_workflow.run("Research the impact of AI on healthcare")

# The result will be the FinalReport from the last agent
```

## Important Notes

1. **Structured output is defined at the ENGINE level**, not the agent level
2. **SimpleAgent and ReactAgent** have convenience fields that sync to the engine
3. **MultiAgent** does not have its own structured output - each sub-agent has its own
4. **State transfer** between agents happens through MultiAgentState
5. **AgentNodeV3** handles the projection from MultiAgentState to agent-specific state

## Common Pitfalls

1. **Setting structured_output_model on MultiAgent** - It doesn't have this field
2. **Manual agent chaining** - Use MultiAgent for proper orchestration
3. **Forgetting engine configuration** - Each agent needs its own properly configured engine
4. **State isolation** - Each agent only sees its projected state, not the full MultiAgentState

## Next Steps

To implement proper multi-agent workflows:

1. Define clear structured output models for each agent
2. Create agents with appropriate engines and structured outputs
3. Use MultiAgent to orchestrate them (not manual chaining)
4. Configure execution mode (sequential, parallel, conditional)
5. Let MultiAgent handle state transfer and coordination

This architecture ensures clean separation of concerns, proper state management, and type-safe data flow between agents.
