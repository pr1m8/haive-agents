# Self-Discover Multi-Agent Reasoning Module

**Status**: ✅ **PRODUCTION READY**  
**Purpose**: Systematic multi-stage reasoning methodology using specialized agents  
**Framework**: Built on EnhancedMultiAgentV4 with SimpleAgentV3 agents

## 🧠 Overview

The Self-Discover module implements the Self-Discover reasoning methodology through a coordinated multi-agent system. It breaks complex problem-solving into four distinct stages, each handled by a specialized agent, resulting in systematic and traceable reasoning processes.

### Four-Stage Workflow

1. **🎯 Module Selection** - Analyze task and select optimal reasoning strategies
2. **🔧 Module Adaptation** - Adapt strategies for the specific task context
3. **📋 Plan Structuring** - Create step-by-step reasoning plan
4. **⚡ Plan Execution** - Execute the plan systematically to solve the task

## 🏗️ Architecture

### Agent Composition

```python
SelfDiscoverWorkflow:
├── selector_agent: SimpleAgentV3     # Select reasoning modules
├── adapter_agent: SimpleAgentV3      # Adapt modules for task
├── structurer_agent: SimpleAgentV3   # Create structured plan
└── executor_agent: SimpleAgentV3     # Execute plan systematically

Coordinated by: EnhancedMultiAgentV4 (sequential execution)
```

### Structured Outputs

Each agent produces typed, validated outputs:

- **ModuleSelection**: Selected reasoning modules with rationale
- **ModuleAdaptation**: Task-specific adaptation strategies
- **ReasoningStructure**: Step-by-step execution plan
- **TaskSolution**: Final answer with reasoning trace

## 🚀 Quick Start

### Basic Usage

```python
from haive.agents.reasoning_and_critique.self_discover import SelfDiscoverWorkflow

# Create workflow
workflow = SelfDiscoverWorkflow()

# Solve a complex task
result = await workflow.solve_task(
    "How should a startup enter a competitive market?"
)

# Analyze results
workflow.analyze_self_discover_result(result)
```

### Production Example

```python
import asyncio
from haive.agents.reasoning_and_critique.self_discover import SelfDiscoverWorkflow

async def solve_business_problem():
    """Example of using Self-Discover for business strategy."""

    workflow = SelfDiscoverWorkflow()

    task = """
    A small e-commerce startup is struggling with customer retention.
    They have a 15% monthly churn rate, limited marketing budget,
    and growing competition from larger players. What strategy should
    they implement to improve retention and grow sustainably?
    """

    # Execute Self-Discover reasoning
    result = await workflow.solve_task(task)

    # The result contains:
    # - Selected reasoning modules (e.g., Systems Thinking, Risk Assessment)
    # - Adapted strategies specific to e-commerce retention
    # - Structured step-by-step plan
    # - Comprehensive solution with reasoning trace

    return result

# Run the example
result = asyncio.run(solve_business_problem())
```

## 📋 Key Components

### Selector Agent

Analyzes tasks and selects 3-5 optimal reasoning modules from 15 available strategies.

### Adapter Agent

Takes selected modules and adapts them with task-specific strategies and concrete action steps.

### Structurer Agent

Creates ordered, step-by-step reasoning plans using the adapted modules.

### Executor Agent

Systematically executes the plan to generate comprehensive solutions with reasoning traces.

## 📊 Available Reasoning Modules

The Self-Discover system can select from 15 reasoning modules:

1. **Critical Thinking** - Analyze assumptions, evaluate evidence, identify biases
2. **Pattern Recognition** - Identify patterns, structures, and relationships
3. **Decomposition** - Break complex problems into manageable parts
4. **Systems Thinking** - Consider interactions, feedback loops, emergent properties
5. **Analogical Reasoning** - Draw parallels with similar known problems
6. **Causal Analysis** - Understand cause-and-effect relationships
7. **Mathematical Reasoning** - Apply quantitative analysis and logic
8. **Creative Problem Solving** - Generate innovative solutions and alternatives
9. **Risk Assessment** - Evaluate potential outcomes and uncertainties
10. **Optimization** - Find the best solution among alternatives
11. **Temporal Reasoning** - Consider sequence, timing, temporal relationships
12. **Spatial Reasoning** - Understand geometric and spatial relationships
13. **Logical Reasoning** - Apply formal logic and deductive reasoning
14. **Empirical Validation** - Test hypotheses with evidence and data
15. **Meta-cognitive Reflection** - Think about thinking and reasoning processes

## Installation

This module is part of the `haive-agents` package. Install it using:

```bash
poetry install haive-agents
```

## 🧪 Testing and Validation

All Self-Discover components are tested with **real LLM execution** (no mocks):

```bash
# Run the comprehensive demo suite
poetry run python packages/haive-agents/examples/self_discover_multi_agent_demo.py

# Includes 4 demo scenarios:
# 1. Problem Solving (startup market entry)
# 2. Analytical Reasoning (city traffic planning)
# 3. Creative Problem Solving (elderly connectivity)
# 4. Technical Analysis (software performance)
```

### Demo Results

Recent validation shows excellent performance:

- **Quality Scores**: 12/12 across all demos
- **Stage Completion**: All four stages successfully executed
- **Reasoning Quality**: Structured outputs and systematic progression
- **Real LLM**: Validated with Azure OpenAI (no mocks)

## API Reference

For detailed API documentation, see the individual agent documentation:

- [Selector Agent](./selector/agent.py) - Module selection
- [Adapter Agent](./adapter/agent.py) - Module adaptation
- [Structurer Agent](./structurer/agent.py) - Plan creation
- [Executor Agent](./executor/agent.py) - Plan execution

## See Also

- **[Reasoning & Critique README](../README.md)** - Overview of reasoning modules
- **[Multi-Agent Coordination Guide](../../docs/MULTI_AGENT_COORDINATION_GUIDE.md)** - Multi-agent patterns
- **[Reflection Module](../reflection/README.md)** - Complementary reasoning pattern
- **[EnhancedMultiAgentV4](../../multi/README.md)** - Multi-agent coordination framework
