# Haive Agents - Current Status & Recommendations

**Last Updated**: January 27, 2025  
**Status**: Working Individual Agents, MultiAgent Under Development

## 🎯 Quick Start - What Works Right Now

### ✅ **Fully Working Individual Agents**

#### **SimpleAgentV3** - Recommended for Basic Tasks

```python
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig

# Basic conversational agent
agent = SimpleAgentV3(
    name="assistant",
    engine=AugLLMConfig(temperature=0.7)
)

result = await agent.arun("Hello, how can you help me?")
```

#### **ReactAgentV3** - Recommended for Tool Usage & Reasoning

```python
from haive.agents.react.agent_v3 import ReactAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression))

# Agent with tools and reasoning
agent = ReactAgentV3(
    name="reasoner",
    engine=AugLLMConfig(
        temperature=0.3,
        tools=[calculator]
    ),
    max_iterations=3
)

result = await agent.arun("What is 15 * 23?")
```

### ✅ **Working Patterns**

#### **Sequential Coordination** (Manual)

```python
# Proven working pattern: ReactAgent → SimpleAgent
from pydantic import BaseModel, Field

class AnalysisReport(BaseModel):
    findings: list[str] = Field(description="Key findings")
    confidence: float = Field(ge=0.0, le=1.0)

# Step 1: Analysis with tools
analyzer = ReactAgentV3(
    name="analyzer",
    engine=AugLLMConfig(tools=[research_tool]),
    max_iterations=3
)

# Step 2: Structured output
formatter = SimpleAgentV3(
    name="formatter",
    engine=AugLLMConfig(structured_output_model=AnalysisReport)
)

# Execute sequentially
analysis = await analyzer.arun("Research AI trends")
report = await formatter.arun(f"Format this analysis: {analysis}")
```

#### **Simple Branching Pattern** (Working)

```python
class SimpleBranchingMultiAgent:
    """Simple branching coordinator - pass agents & branch function."""

    def __init__(self, name: str, agents: dict, branch_function):
        self.name = name
        self.agents = agents
        self.branch_function = branch_function

    async def arun(self, input_text: str):
        # Execute initial agent
        result = await self.agents[self.initial_agent].arun(input_text)

        # Use branch function to route
        next_agent = self.branch_function({"agent_outputs": {self.initial_agent: result}})

        # Execute next agent if different
        if next_agent != self.initial_agent:
            context = f"Previous: {result}\nOriginal: {input_text}"
            result = await self.agents[next_agent].arun(context)

        return result

# Usage
workflow = SimpleBranchingMultiAgent(
    name="smart_router",
    agents={
        "analyzer": ReactAgentV3(...),
        "simple_processor": SimpleAgentV3(...),
        "detailed_processor": SimpleAgentV3(...)
    },
    branch_function=lambda state: "detailed_processor" if "complex" in str(state["agent_outputs"]) else "simple_processor"
)
```

## ❌ **What's Currently Broken**

### **All MultiAgent Classes**

- `MultiAgent` (from multi_agent.py) - Missing `build_graph()` method
- `MultiAgentV4` - Missing `build_graph()` method
- `EnhancedMultiAgentV3` - Import issues
- `EnhancedMultiAgentV4` - Import issues
- All enhanced versions - `Tool_Type` import error

**Root Cause**: Import error in `haive.core.types` blocking all agent imports

### **Common Error**

```
UserWarning: Failed to import agent submodules:
cannot import name 'Tool_Type' from 'haive.core.types'
```

## 🛠️ **Development Recommendations**

### **For Production Use** (January 2025)

1. **Use Individual Agents**: SimpleAgentV3 and ReactAgentV3 are stable
2. **Manual Coordination**: Coordinate agents manually for reliability
3. **Custom Branching**: Use simple branching patterns as shown above
4. **Structured Output**: Use Pydantic models with SimpleAgentV3

### **Avoid Until Fixed**

- Any MultiAgent class import
- Enhanced MultiAgent implementations
- Complex multi-agent orchestration classes

### **Testing Approach**

- ✅ **NO MOCKS**: All tests use real LLMs (Azure OpenAI)
- ✅ **Real Tools**: Test with actual tool implementations
- ✅ **Real State**: Test with actual state management

## 📊 **Agent Comparison Matrix**

| Agent             | Status     | Use Case                 | Tools  | Structured Output | Async  |
| ----------------- | ---------- | ------------------------ | ------ | ----------------- | ------ |
| **SimpleAgentV3** | ✅ Working | Conversation, formatting | ❌ No  | ✅ Yes            | ✅ Yes |
| **ReactAgentV3**  | ✅ Working | Reasoning, tool use      | ✅ Yes | ✅ Yes            | ✅ Yes |
| SimpleAgent (old) | ⚠️ Legacy  | -                        | -      | -                 | -      |
| ReactAgent (old)  | ⚠️ Legacy  | -                        | -      | -                 | -      |
| MultiAgent\*      | ❌ Broken  | Multi-agent              | -      | -                 | -      |
| Enhanced\*        | ❌ Broken  | Advanced patterns        | -      | -                 | -      |

## 🎯 **Recommended Agent Selection**

### **Choose SimpleAgentV3 When:**

- Basic conversation or Q&A
- Text formatting and generation
- Structured output needed
- No external tools required

### **Choose ReactAgentV3 When:**

- Need to use tools (APIs, calculators, search)
- Require reasoning and planning
- Multi-step problem solving
- Research and analysis tasks

### **Manual Coordination When:**

- Need multiple specialized agents
- Want reliable execution
- Complex workflow requirements
- Production-critical applications

## 📝 **Working Code Examples**

### **Basic SimpleAgent with Structured Output**

```python
from pydantic import BaseModel, Field

class TaskResult(BaseModel):
    summary: str = Field(description="Task summary")
    status: str = Field(description="Completion status")
    next_steps: list[str] = Field(description="Recommended next steps")

agent = SimpleAgentV3(
    name="task_manager",
    engine=AugLLMConfig(
        temperature=0.5,
        structured_output_model=TaskResult
    )
)

result = await agent.arun("Plan a marketing campaign")
# Returns TaskResult object with typed fields
```

### **ReactAgent with Multiple Tools**

```python
@tool
def web_search(query: str) -> str:
    """Search the web for information."""
    return f"Search results for: {query}"

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression))

agent = ReactAgentV3(
    name="research_assistant",
    engine=AugLLMConfig(
        temperature=0.3,
        tools=[web_search, calculator]
    ),
    max_iterations=5,
    debug=True  # Shows reasoning steps
)

result = await agent.arun("Research the population of Tokyo and calculate its density")
```

### **Sequential Multi-Agent Pattern**

```python
# Research → Analysis → Report pipeline
async def research_pipeline(query: str):
    # Step 1: Research with tools
    researcher = ReactAgentV3(
        name="researcher",
        engine=AugLLMConfig(tools=[web_search, calculator])
    )
    research_data = await researcher.arun(f"Research: {query}")

    # Step 2: Analysis
    analyzer = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(
            system_message="Analyze data and extract key insights."
        )
    )
    analysis = await analyzer.arun(f"Analyze this research: {research_data}")

    # Step 3: Structured report
    class Report(BaseModel):
        title: str
        key_findings: list[str]
        recommendations: list[str]
        confidence_score: float = Field(ge=0.0, le=1.0)

    reporter = SimpleAgentV3(
        name="reporter",
        engine=AugLLMConfig(structured_output_model=Report)
    )

    report = await reporter.arun(f"Create report from: {analysis}")
    return report

# Usage
report = await research_pipeline("Impact of AI on job market")
```

## 🚨 **Known Issues & Workarounds**

### **Issue 1: Tool_Type Import Error**

**Problem**: `cannot import name 'Tool_Type' from 'haive.core.types'`  
**Workaround**: Use individual agents directly, avoid MultiAgent imports

### **Issue 2: MultiAgent Classes Broken**

**Problem**: All MultiAgent implementations have import or implementation issues  
**Workaround**: Use manual coordination patterns shown above

### **Issue 3: Enhanced Agent Import Paths**

**Problem**: `from haive.agents.base.enhanced_agent import Agent` may not exist  
**Workaround**: Use standard individual agents

## 🔮 **Future Development Priorities**

1. **Fix Tool_Type Import** - Restore MultiAgent functionality
2. **Complete EnhancedMultiAgentV4** - Target implementation
3. **Standardize Import Paths** - Clean up enhanced agent imports
4. **Documentation Update** - Comprehensive examples and patterns
5. **Test Coverage** - Full integration testing

## 📚 **Additional Resources**

- **Individual Agent Examples**: `packages/haive-agents/tests/simple/`, `packages/haive-agents/tests/react/`
- **Working Test Patterns**: `test_simple_v3_tools.py`, `test_react_v3_tools.py`
- **Architecture Documentation**: `project_docs/active/architecture/`
- **Testing Philosophy**: `project_docs/active/standards/testing/philosophy.md`

---

**Summary**: Use SimpleAgentV3 and ReactAgentV3 for all current development. MultiAgent classes are under active development but not ready for production use. Manual coordination patterns provide reliable multi-agent functionality.
