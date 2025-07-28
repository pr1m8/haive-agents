# Haive Agents

**AI Agent Framework for Complex Workflows**

**Last Updated**: January 28, 2025  
**Status**: ✅ **PRODUCTION READY** - Individual Agents & Multi-Agent Coordination Working

## 🎯 Quick Start - What Works Right Now

### ✅ **Production Ready Agents**

| Agent                      | Status                 | Use Case                 | Features                      |
| -------------------------- | ---------------------- | ------------------------ | ----------------------------- |
| **SimpleAgentV3**          | ✅ Production          | Conversation, formatting | Structured output, async      |
| **ReactAgentV3**           | ✅ Production          | Tool use, reasoning      | Tools, planning, async        |
| **EnhancedMultiAgentV4**   | ✅ **FIXED & Working** | Multi-agent coordination | Sequential/parallel execution |
| **Reflection Patterns**    | ✅ Production          | Self-improving workflows | Multi-agent reflection chains |
| **Self-Discover Patterns** | ✅ Production          | Complex problem solving  | 4-stage reasoning methodology |

### 🆕 **Multi-Agent Coordination (NEW!)**

✅ **Dict Compatibility Fixed**: StateSchema now works seamlessly with LangGraph  
✅ **Production Ready**: All multi-agent patterns tested with real LLMs  
✅ **Comprehensive Guides**: [Multi-Agent Coordination Guide](docs/MULTI_AGENT_COORDINATION_GUIDE.md)

### **Working Import Patterns**

```python
# ✅ INDIVIDUAL AGENTS - Production ready
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.agents.react.agent_v3 import ReactAgentV3
from haive.core.engine.aug_llm import AugLLMConfig

# ✅ MULTI-AGENT COORDINATION - Now working!
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4

# ✅ REASONING & CRITIQUE - Production ready
from haive.agents.reasoning_and_critique.reflection import ReflectionAgent
from haive.agents.reasoning_and_critique.self_discover import SelfDiscoverWorkflow
# See reasoning_and_critique README for more modules

# ❌ STILL BROKEN - Avoid these
# from haive.agents.multi import MultiAgent (old version)
```

## 🚀 Quick Examples

### **SimpleAgentV3** - Basic Conversation & Structured Output

```python
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

# Basic conversational agent
agent = SimpleAgentV3(
    name="assistant",
    engine=AugLLMConfig(temperature=0.7)
)

result = await agent.arun("Hello, how can you help me?")

# With structured output
class TaskAnalysis(BaseModel):
    difficulty: str = Field(description="easy/medium/hard")
    time_estimate: str = Field(description="Estimated time")

structured_agent = SimpleAgentV3(
    name="analyzer",
    engine=AugLLMConfig(structured_output_model=TaskAnalysis)
)

analysis = await structured_agent.arun("Analyze building a web app")
```

### **ReactAgentV3** - Tools & Reasoning

```python
from haive.agents.react.agent_v3 import ReactAgentV3
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression))

@tool
def web_search(query: str) -> str:
    """Search for information."""
    return f"Search results for: {query}"

# Agent with tools and reasoning
agent = ReactAgentV3(
    name="research_assistant",
    engine=AugLLMConfig(
        temperature=0.3,
        tools=[calculator, web_search]
    ),
    max_iterations=3,
    debug=True  # Shows reasoning steps
)

result = await agent.arun("What is 15 * 23 and find info about that number?")
```

### **🆕 Multi-Agent Coordination** - Production Ready!

```python
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from langchain_core.messages import HumanMessage

# ReactAgent → SimpleAgent coordination workflow
react_agent = ReactAgentV3(
    name="researcher",
    engine=AugLLMConfig(
        temperature=0.3,
        tools=[calculator, web_search]
    ),
    max_iterations=3
)

simple_agent = SimpleAgentV3(
    name="formatter",
    engine=AugLLMConfig(temperature=0.7)
)

# Create coordinated multi-agent workflow
multi_agent = EnhancedMultiAgentV4(
    name="research_workflow",
    agents=[react_agent, simple_agent],
    execution_mode="sequential"  # or "parallel"
)

# Execute with full coordination
result = await multi_agent.arun({
    "messages": [HumanMessage(content="Research AI trends and format findings")]
})
```

### **🔄 Reflection Multi-Agent Pattern**

```python
from haive.agents.reasoning_and_critique.reflection import ReflectionAgent

# Multi-agent reflection: Execute → Reflect → Improve
executor = SimpleAgentV3(name="executor", engine=AugLLMConfig(temperature=0.7))
reflector = SimpleAgentV3(name="reflector", engine=AugLLMConfig(temperature=0.3))
improver = SimpleAgentV3(name="improver", engine=AugLLMConfig(temperature=0.5))

reflection_workflow = EnhancedMultiAgentV4(
    name="reflection_system",
    agents=[executor, reflector, improver],
    execution_mode="sequential"
)

# Self-improving workflow execution
result = await reflection_workflow.arun({
    "messages": [HumanMessage(content="Write and improve a technical proposal")]
})
```

### **🧠 Self-Discover Multi-Agent Pattern** (NEW!)

```python
from haive.agents.reasoning_and_critique.self_discover import SelfDiscoverWorkflow

# Complete 4-stage reasoning: Select → Adapt → Structure → Execute
workflow = SelfDiscoverWorkflow()

# Solve complex problems with systematic reasoning
result = await workflow.solve_task("""
A tech startup needs to decide between three growth strategies:
(A) Expanding to new markets, (B) Adding premium features, or
(C) Improving customer success. Limited budget of $500K. What approach?
""")

# Analyze reasoning quality (returns 12/12 quality scores)
workflow.analyze_self_discover_result(result)

# Individual agents for custom workflows
from haive.agents.reasoning_and_critique.self_discover.selector.agent import SelectorAgent
from haive.agents.reasoning_and_critique.self_discover.adapter.agent import AdapterAgent
from haive.agents.reasoning_and_critique.self_discover.structurer.agent import StructurerAgent
from haive.agents.reasoning_and_critique.self_discover.executor.agent import ExecutorAgent

# Custom 4-stage workflow
self_discover_agents = [
    SelectorAgent(name="selector", engine=AugLLMConfig(temperature=0.3)),
    AdapterAgent(name="adapter", engine=AugLLMConfig(temperature=0.4)),
    StructurerAgent(name="structurer", engine=AugLLMConfig(temperature=0.2)),
    ExecutorAgent(name="executor", engine=AugLLMConfig(temperature=0.6))
]

custom_workflow = EnhancedMultiAgentV4(
    name="custom_self_discover",
    agents=self_discover_agents,
    execution_mode="sequential"
)
```

### **Simple Branching Pattern** (Working Alternative)

```python
class SimpleBranchingAgent:
    """Route between agents based on custom logic."""

    def __init__(self, agents: dict, branch_function):
        self.agents = agents
        self.branch_function = branch_function

    async def arun(self, input_text: str):
        # Execute first agent
        initial = list(self.agents.keys())[0]
        result = await self.agents[initial].arun(input_text)

        # Use branch function to route
        state = {"agent_outputs": {initial: result}}
        next_agent = self.branch_function(state)

        if next_agent != initial and next_agent in self.agents:
            context = f"Previous: {result}\nOriginal: {input_text}"
            result = await self.agents[next_agent].arun(context)

        return result

# Usage
def complexity_router(state):
    output = str(list(state["agent_outputs"].values())[0]).lower()
    return "detailed" if "complex" in output else "simple"

workflow = SimpleBranchingAgent(
    agents={
        "analyzer": ReactAgentV3(...),
        "simple": SimpleAgentV3(...),
        "detailed": SimpleAgentV3(...)
    },
    branch_function=complexity_router
)

result = await workflow.arun("Analyze this problem")
```

## 🎉 **Recent Achievements (January 2025)**

### **✅ Multi-Agent Coordination FIXED & Working!**

**StateSchema Dict Compatibility**: Fixed the critical "object is not subscriptable" error that prevented EnhancedMultiAgentV4 from working with LangGraph.

```python
# ✅ NOW WORKING - Multi-agent coordination
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4

multi_agent = EnhancedMultiAgentV4(
    name="workflow",
    agents=[react_agent, simple_agent],
    execution_mode="sequential"
)

result = await multi_agent.arun({"messages": [HumanMessage(content="...")]})
```

### **✅ What's Production Ready**

- ✅ **SimpleAgentV3** - Conversation, structured output
- ✅ **ReactAgentV3** - Tools, reasoning, planning
- ✅ **EnhancedMultiAgentV4** - Multi-agent coordination (FIXED!)
- ✅ **Reflection Patterns** - Self-improving workflows
- ✅ **Self-Discover Patterns** - 4-stage systematic reasoning (12/12 quality scores)
- ✅ **Reasoning & Critique** - Advanced reasoning modules
- ✅ **Real LLM Testing** - All patterns validated with Azure OpenAI

### **📚 Comprehensive Documentation**

- 🔗 **[Multi-Agent Coordination Guide](docs/MULTI_AGENT_COORDINATION_GUIDE.md)** - Complete patterns & examples
- 🔗 **[Reasoning & Critique README](src/haive/agents/reasoning_and_critique/README.md)** - Advanced reasoning modules
- 🔗 **[Reflection Demo](examples/reflection_multi_agent_demo.py)** - Working reflection patterns
- 🔗 **[Self-Discover Demo](examples/self_discover_multi_agent_demo.py)** - 4-stage reasoning workflows (12/12 scores)
- 🔗 **[Success Summary](../../../MULTI_AGENT_COORDINATION_SUCCESS_SUMMARY.md)** - Technical achievement details

## 📋 **Agent Selection Guide**

### **Use SimpleAgentV3 When:**

- Basic conversation or Q&A
- Text formatting and generation
- Structured output needed (Pydantic models)
- No external tools required

### **Use ReactAgentV3 When:**

- Need to use tools (APIs, calculators, search)
- Require reasoning and planning
- Multi-step problem solving
- Research and analysis tasks

### **Use EnhancedMultiAgentV4 When:**

- Need multiple specialized agents working together
- Want sequential or parallel agent coordination
- Complex workflows with different agent roles
- Production multi-agent systems (now working!)

### **Use Reflection Patterns When:**

- Need self-improving responses
- Want quality assurance workflows
- Require critique and improvement cycles
- Building sophisticated reasoning systems

### **Use Reasoning & Critique Modules When:**

- Advanced reasoning required (self-discover, ToT, MCTS)
- Need formal logic and premise analysis
- Want tree-based or Monte Carlo search
- Building cutting-edge AI reasoning systems

### **Use Self-Discover Pattern When:**

- Need systematic problem-solving methodology
- Want traceable reasoning steps
- Require module selection and adaptation
- Complex problems need structured approach (12/12 quality validated)

## 🧪 **Testing**

**Philosophy**: NO MOCKS - Test with real LLMs and tools.

```python
import pytest
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig

@pytest.mark.asyncio
async def test_simple_agent_real():
    """Test with real LLM execution."""
    agent = SimpleAgentV3(
        name="test",
        engine=AugLLMConfig(temperature=0.1)  # Low for consistency
    )

    result = await agent.arun("Hello")
    assert isinstance(result, str)
    assert len(result) > 0

# Run tests
poetry run pytest packages/haive-agents/tests/ -v
```

## 📚 **Documentation**

- **[Current Status](CURRENT_STATUS_2025.md)** - Detailed status report
- **[Architecture](../../../project_docs/active/architecture/)** - System design
- **[Testing Philosophy](../../../project_docs/active/standards/testing/philosophy.md)** - No-mocks approach

## 🔮 **Roadmap**

### **Q1 2025**

- Fix MultiAgent import issues
- Restore EnhancedMultiAgentV4 functionality
- Complete branching and conditional routing

### **Q2 2025**

- Advanced orchestration patterns
- Production-ready MultiAgent classes
- Performance optimizations

---

**Current Recommendation**: Use SimpleAgentV3 and ReactAgentV3 with manual coordination. MultiAgent functionality will be restored in Q1 2025.

# Use it

response = agent.run("Explain quantum computing")

````

### Agent with Tools

```python
from haive.agents.react import ReactAgent
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression))

# Create agent with tools
agent = ReactAgent(
    name="math_assistant",
    engine=AugLLMConfig(),
    tools=[calculator]
)

# Use it
response = agent.run("What is 25 * 37?")
````

### Multi-Agent Workflow

```python
from haive.agents.multi import MultiAgent
from haive.agents.simple import SimpleAgent

# Create specialized agents
researcher = SimpleAgent(name="researcher")
writer = SimpleAgent(name="writer")

# Coordinate them
team = MultiAgent(
    name="content_team",
    agents={"research": researcher, "write": writer},
    mode="sequential"
)

# Execute workflow
result = team.run("Write a blog post about AI")

## 📖 Detailed Documentation

Each agent family has comprehensive documentation:

1. **[SimpleAgent Documentation](src/haive/agents/simple/README.md)**
   - Version comparison (V1, V2, V3)
   - Prompt engineering patterns
   - Structured output examples

2. **[ReactAgent Documentation](src/haive/agents/react/README.md)**
   - Tool integration guide
   - Reasoning patterns
   - Error handling

3. **[MultiAgent Documentation](src/haive/agents/multi/README.md)**
   - Version comparison (V1-V4)
   - Execution modes
   - State management patterns

## 🏗️ Architecture Patterns

### Agent Hierarchy
```

Agent (base class)
├── SimpleAgent (basic LLM agent)
│ ├── SimpleAgentV2 (+ typed state)
│ └── SimpleAgentV3 (+ enhanced features)
├── ReactAgent (reasoning + tools)
└── MultiAgent (orchestration)
├── SimpleMultiAgent (basic)
├── MultiAgentV2 (+ state management)
├── MultiAgentV3 (+ async)
└── EnhancedMultiAgentV4 (+ all features)

````

### Key Concepts

1. **Engine (AugLLMConfig)**: LLM configuration for all agents
2. **Tools**: Functions that agents can call
3. **State**: Agent memory and context
4. **Orchestration**: Coordinating multiple agents

## 🛠️ Advanced Features

### Structured Output
```python
from pydantic import BaseModel

class AnalysisResult(BaseModel):
    sentiment: str
    confidence: float
    themes: list[str]

agent = SimpleAgent(
    name="analyzer",
    engine=AugLLMConfig(structured_output_model=AnalysisResult)
)
````

### Async Execution

```python
# All agents support async
result = await agent.arun("Process this asynchronously")

# Multi-agent parallel execution
results = await team.arun("Process in parallel", mode="parallel")
```

### State Persistence

```python
# Agents can save/load state
agent.save_state("agent_state.json")
restored_agent = SimpleAgent.load_state("agent_state.json")
```

## 🧪 Testing Agents

```python
# All agents use real LLMs in tests (no mocks)
def test_agent_with_real_llm():
    agent = SimpleAgent(
        name="test",
        engine=AugLLMConfig(temperature=0.1)  # Low for consistency
    )

    result = agent.run("Hello")
    assert isinstance(result, str)
    assert len(result) > 0
```

## 📋 Migration Guide

### Upgrading SimpleAgent

```python
# From default to V3
# Before:
agent = SimpleAgent(name="old")

# After:
from haive.agents.simple.agent_v3 import SimpleAgentV3
agent = SimpleAgentV3(name="new")  # Drop-in replacement
```

### Upgrading MultiAgent

```python
# From default to V4
# Before:
multi = MultiAgent(agents=[agent1, agent2])

# After:
from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
multi = EnhancedMultiAgentV4(
    agents=[agent1, agent2],
    execution_mode="sequential"  # Explicit mode
)
```

## 🧪 Testing Philosophy

### No-Mocks Testing

All tests use real components:

- **Real LLM integrations** - Actual API calls
- **Real agent implementations** - Full agent stack
- **Real state management** - Actual persistence
- **Real tool execution** - Complete workflow

### Test Categories

```bash
# Run all tests
poetry run pytest tests/ -v

# Run specific categories
poetry run pytest tests/supervisor/ -v          # Supervisor tests
poetry run pytest tests/react/ -v              # React agent tests
poetry run pytest tests/supervisor/components/ -v  # Component tests
poetry run pytest tests/supervisor/experiments/ -v # Experimental tests
```

## 📚 Examples and Patterns

### Basic Examples

- **[Basic Supervisor](examples/supervisor/basic/basic_supervisor_example.py)** - Simple multi-agent coordination
- **[React Agent](examples/react/)** - ReAct pattern usage

### Advanced Examples

- **[Dynamic Activation](examples/supervisor/advanced/dynamic_activation_example.py)** - Capability-based agent activation
- **[Multi-Step Workflows](examples/supervisor/advanced/)** - Complex task coordination

### Pattern Examples

- **[Agent Execution Node](examples/supervisor/patterns/agent_execution_node_pattern.py)** - Clean execution pattern
- **[Dynamic Tool Generation](examples/supervisor/patterns/dynamic_tool_generation_pattern.py)** - Tool creation patterns
- **[State Synchronized Tools](examples/supervisor/patterns/state_synchronized_tools_pattern.py)** - State-tool coordination

## 🔧 Development

### Installation

```bash
# Install with poetry
poetry install

# Install with pip
pip install haive-agents
```

### Running Examples

```bash
# Basic examples
poetry run python examples/simple_agent_example.py
poetry run python examples/react_agent_example.py
poetry run python examples/multi_agent_example.py

# Advanced patterns
poetry run python examples/structured_output_example.py
poetry run python examples/parallel_execution_example.py
```

### Development Setup

```bash
# Install dependencies
poetry install --all-extras

# Run tests
poetry run pytest tests/ -v

# Run specific tests
poetry run pytest tests/simple/ -v
```

## 🎯 Common Use Cases

### 1. Task Routing

Route different types of tasks to specialized agents:

```python
# Question answering → General agent
# Calculations → Math agent
# Research → Search agent
# Code generation → Code agent
```

### 2. Multi-Step Workflows

Coordinate complex processes:

```python
# Research → Analysis → Presentation
# Data Collection → Processing → Reporting
# Problem Analysis → Solution Design → Implementation
```

### 3. Resource Management

Optimize resource usage:

```python
# Dynamic activation - Activate agents on demand
# Load balancing - Distribute work across agents
# Cost optimization - Use appropriate models
```

## 🛡️ Best Practices

### 1. Agent Design

- **Specialized agents** for specific tasks
- **Clear descriptions** for routing decisions
- **Robust error handling** in implementations
- **Appropriate tool selection**

### 2. Configuration

- **Clear system messages** for agent behavior
- **Appropriate model selection** for task complexity
- **Proper state management** for conversations
- **Resource optimization** for cost efficiency

### 3. Testing

- **Real LLM testing** - No mocks
- **Integration tests** - Full workflows
- **Error scenarios** - Edge cases
- **Performance testing** - Response times

## 🔗 Related Documentation

- [Haive Core Documentation](../haive-core/README.md)
- [Tool Integration Guide](../haive-tools/README.md)
- [Agent Patterns](../../project_docs/active/architecture/multi_agent_meta_agent_memory_hub.md)
- [CLAUDE.md](../../CLAUDE.md) - Main development hub

## 🤝 Contributing

When contributing new agents:

1. Follow the version naming convention
2. Maintain backward compatibility
3. Add comprehensive tests (no mocks)
4. Update relevant documentation
5. Add migration notes if needed

## 📈 Version History

### Latest Updates

- **SimpleAgentV3**: Enhanced base agent with hooks, recompilation
- **EnhancedMultiAgentV4**: Full async support, parallel execution
- **ReactAgent**: Stable, no version changes needed

### Version Policy

- Default imports remain stable for backward compatibility
- New features added in versioned classes (V2, V3, etc.)
- Migration guides provided for version upgrades

## 📝 License

MIT License - see [LICENSE](../../../LICENSE) for details.

## 🔗 Resources

- **[API Reference](https://haive.readthedocs.io)**
- **[GitHub Repository](https://github.com/haive/haive)**
- **[Discord Community](https://discord.gg/haive)**
- **[Blog & Tutorials](https://haive.ai/blog)**

For questions, issues, or contributions, please refer to the main project repository or create an issue.
