# Reasoning And Critique

Advanced reasoning and critique systems for AI agents, featuring multiple reasoning paradigms and multi-agent coordination patterns. This module provides state-of-the-art reasoning capabilities including self-reflection, tree search, logical reasoning, and self-discovery mechanisms.

## Overview

The reasoning_and_critique module offers sophisticated agent architectures that can perform complex reasoning tasks, self-improvement through reflection, and coordinated multi-agent reasoning workflows. All agents support both individual execution and multi-agent coordination patterns.

**Key Features**:

- **Multi-Agent Coordination**: All reasoning agents support sequential and parallel coordination
- **Self-Improvement**: Reflection and self-correction capabilities
- **Advanced Search**: Tree-based and Monte Carlo search strategies
- **Logical Reasoning**: Formal logic and premise-based reasoning
- **Real Component Testing**: No mocks - all agents tested with real LLMs

## Key Components

### Core Reasoning Modules

- **reflection**: 🎯 **Production Ready** - Multi-agent reflection system with sequential workflows
- **self_discover**: ✅ **Production Ready** - Self-discovery reasoning with 4-stage multi-agent workflow (12/12 quality scores)
- **lats**: 🌳 **Experimental** - Language Agent Tree Search for complex problem solving
- **reflexion**: 🔄 **Self-Improving** - Self-reflexive agents that learn from mistakes
- **logic**: 🧠 **Formal** - Logic-based reasoning with premise extraction and synthesis
- **tot**: 🌲 **Tree Search** - Tree of Thought reasoning for step-by-step problem decomposition
- **mcts**: 🎲 **Monte Carlo** - Monte Carlo Tree Search for optimal decision making

## Installation

This module is part of the `haive-agents` package. Install it using:

```bash
poetry add haive-agents
# or
pip install haive-agents
```

## Multi-Agent Coordination Patterns

### Sequential Reasoning Workflow (Production Ready)

```python
from haive.agents.reasoning_and_critique.reflection import ReflectionAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.core.engine.aug_llm import AugLLMConfig

# Create reasoning and synthesis agents
reasoning_agent = ReflectionAgent(
    name="reasoner",
    engine=AugLLMConfig(temperature=0.3)
)

synthesis_agent = SimpleAgentV3(
    name="synthesizer",
    engine=AugLLMConfig(temperature=0.7)
)

# Coordinate in multi-agent workflow
multi_agent = EnhancedMultiAgentV4(
    name="reasoning_workflow",
    agents=[reasoning_agent, synthesis_agent],
    execution_mode="sequential"
)

# Execute coordinated reasoning
result = await multi_agent.arun({
    "messages": [HumanMessage(content="Analyze the ethical implications of AI in healthcare")]
})
```

### Self-Discovery Multi-Agent Pattern (Production Ready)

```python
# Use the complete Self-Discover workflow for production
from haive.agents.reasoning_and_critique.self_discover import SelfDiscoverWorkflow

# Create complete 4-stage workflow: Select → Adapt → Structure → Execute
workflow = SelfDiscoverWorkflow()

# Solve complex problems with systematic reasoning
result = await workflow.solve_task("""
A tech startup needs to decide between three growth strategies:
(A) Expanding to new markets, (B) Adding premium features, or
(C) Improving customer success. Limited budget of $500K. What approach?
""")

# Analyze reasoning quality (returns 12/12 quality scores)
workflow.analyze_self_discover_result(result)

# Alternative: Individual agent usage
from haive.agents.reasoning_and_critique.self_discover.selector.agent import SelectorAgent
from haive.agents.reasoning_and_critique.self_discover.adapter.agent import AdapterAgent
from haive.agents.reasoning_and_critique.self_discover.structurer.agent import StructurerAgent
from haive.agents.reasoning_and_critique.self_discover.executor.agent import ExecutorAgent

# 4-stage workflow with individual agents
selector = SelectorAgent(name="selector", engine=AugLLMConfig())
adapter = AdapterAgent(name="adapter", engine=AugLLMConfig())
structurer = StructurerAgent(name="structurer", engine=AugLLMConfig())
executor = ExecutorAgent(name="executor", engine=AugLLMConfig())

# Sequential 4-stage self-discovery workflow
self_discovery_workflow = EnhancedMultiAgentV4(
    name="self_discovery",
    agents=[selector, adapter, structurer, executor],
    execution_mode="sequential"
)
```

### Tree of Thought Multi-Agent Coordination

```python
from haive.agents.reasoning_and_critique.tot.agent import ToTAgent
from haive.agents.react.agent_v3 import ReactAgentV3

# Combine ToT reasoning with React execution
tot_planner = ToTAgent(
    name="planner",
    engine=AugLLMConfig(temperature=0.1)
)

react_executor = ReactAgentV3(
    name="executor",
    engine=AugLLMConfig(tools=[calculator, web_search]),
    max_iterations=5
)

# Plan with ToT, execute with React
planning_workflow = EnhancedMultiAgentV4(
    name="plan_and_execute",
    agents=[tot_planner, react_executor],
    execution_mode="sequential"
)
```

## Individual Agent Usage

### Reflection Agent (Production Ready)

```python
from haive.agents.reasoning_and_critique.reflection import ReflectionAgent

# Create reflection agent for self-improving reasoning
reflection_agent = ReflectionAgent(
    name="self_reflector",
    engine=AugLLMConfig(temperature=0.3)
)

# Execute with reflection capability
result = await reflection_agent.arun(
    "Analyze this complex problem and reflect on your reasoning process"
)
```

### Self-Discover Agent

```python
from haive.agents.reasoning_and_critique.self_discover import SelfDiscoverAgent

# Create self-discovery agent
self_discover_agent = SelfDiscoverAgent(
    name="discoverer",
    engine=AugLLMConfig()
)

# Self-discover reasoning patterns
result = await self_discover_agent.arun(
    "Find the best approach to solve this novel problem"
)
```

## Module Guide

### When to Use Each Reasoning Approach

| Module            | Best For                                      | Multi-Agent Support           | Complexity |
| ----------------- | --------------------------------------------- | ----------------------------- | ---------- |
| **reflection**    | Self-improving workflows, quality assurance   | ✅ Production Ready           | Medium     |
| **self_discover** | Novel problem solving, adaptive reasoning     | ✅ Production Ready (4-stage) | High       |
| **lats**          | Complex search problems, optimization         | 🔄 Experimental               | High       |
| **reflexion**     | Learning from failures, iterative improvement | ✅ Supported                  | Medium     |
| **logic**         | Formal reasoning, premise-based analysis      | ✅ Supported                  | Medium     |
| **tot**           | Step-by-step decomposition, planning          | ✅ Supported                  | High       |
| **mcts**          | Decision optimization, game-like problems     | 🔄 Experimental               | High       |

### Multi-Agent Integration Patterns

1. **Sequential Reasoning**: Chain different reasoning approaches
2. **Parallel Analysis**: Multiple reasoning approaches on same problem
3. **Hierarchical Reasoning**: High-level planning with detailed execution
4. **Reflection Loops**: Execute → Reflect → Improve → Execute

## Production Examples

See the [`examples/`](../../../examples/) directory for comprehensive working examples:

- **`reflection_multi_agent_demo.py`** - Production reflection workflows (Execute → Reflect → Improve)
- **`self_discover_multi_agent_demo.py`** - Self-discovery coordination (Select → Adapt → Structure → Execute)
- **`reasoning_chain_patterns.py`** - Complex reasoning chains
- **`advanced_multi_reasoning.py`** - Multiple reasoning approaches

### Recent Demo Results (Production Validated)

✅ **Self-Discover Demos**: 4/4 scenarios completed with 12/12 quality scores  
✅ **Reflection Demos**: Multi-agent reflection working with real Azure OpenAI  
✅ **No Mocks**: All tests use real LLM execution for production validation

## Testing

All reasoning agents follow the **NO MOCKS** philosophy:

```bash
poetry run pytest packages/haive-agents/tests/reasoning_and_critique/ -v
```

## API Reference

For detailed API documentation, see the [API Reference](../../../docs/source/api/reasoning_and_critique/index.rst).

## Module Deep Dive

- [`reasoning_and_critique.reflection`](./reflection/): 🎯 **Production Ready** - Multi-agent reflection system
- [`reasoning_and_critique.self_discover`](./self_discover/): ✅ **Production Ready** - Self-discovery with 4-stage multi-agent flows
- [`reasoning_and_critique.lats`](./lats/): 🌳 **Experimental** - Language Agent Tree Search
- [`reasoning_and_critique.reflexion`](./reflexion/): 🔄 **Self-Improving** - Learn from mistakes and failures
- [`reasoning_and_critique.logic`](./logic/): 🧠 **Formal** - Logic-based reasoning and synthesis
- [`reasoning_and_critique.tot`](./tot/): 🌲 **Tree Search** - Tree of Thought reasoning
- [`reasoning_and_critique.mcts`](./mcts/): 🎲 **Monte Carlo** - MCTS for optimal decisions

## Multi-Agent Coordination Success

✅ **Dict Compatibility Fix**: All reasoning agents now work with EnhancedMultiAgentV4  
✅ **Real LLM Testing**: Validated with Azure OpenAI integration  
✅ **Production Ready**: Sequential workflows tested and working  
✅ **State Management**: Full conversation history across reasoning agents
