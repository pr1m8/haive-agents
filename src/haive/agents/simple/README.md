# SimpleAgent - Haive Framework

**Simple conversational agents for basic AI interactions**

## 🎯 Quick Start - Which Version to Use?

### ✅ **Default (Recommended)**: SimpleAgent → SimpleAgentV2

```python
from haive.agents.simple import SimpleAgent  # Gets SimpleAgentV2 automatically
from haive.core.engine.aug_llm import AugLLMConfig

# Create simple conversational agent
agent = SimpleAgent(
    name="assistant",
    engine=AugLLMConfig(
        system_message="You are a helpful assistant.",
        temperature=0.7
    )
)

# Use agent
result = await agent.arun("Hello! How can you help me today?")
print(result)
```

### 🚀 **Enhanced (Newer)**: SimpleAgentV3

```python
from haive.agents.simple import SimpleAgentV3  # Enhanced with hooks system
from haive.core.engine.aug_llm import AugLLMConfig

# Create enhanced agent with hooks and pre/post processing
agent = SimpleAgentV3(
    name="enhanced_assistant",
    engine=AugLLMConfig(
        system_message="You are an enhanced assistant.",
        temperature=0.7,
        structured_output_model=MyOutputModel  # Optional structured output
    )
)

# Add hooks for monitoring
@agent.before_run
def log_start(context):
    print(f"🚀 Starting {context.agent_name}")

@agent.after_run
def log_completion(context):
    print(f"✅ Completed {context.agent_name}")

# Execute with hooks
result = await agent.arun("Analyze this topic for me")
```

## 📋 Version Comparison

| Feature                 | SimpleAgent<br/>(Default V2)                  | SimpleAgentV3<br/>(Enhanced)                    | Original SimpleAgent<br/>(Legacy) |
| ----------------------- | --------------------------------------------- | ----------------------------------------------- | --------------------------------- |
| **Import**              | `from haive.agents.simple import SimpleAgent` | `from haive.agents.simple import SimpleAgentV3` | Manual import from agent.py       |
| **Base Class**          | Enhanced Agent ✅                             | Enhanced Agent ✅                               | Enhanced Agent ✅                 |
| **Structured Output**   | ✅ Built-in                                   | ✅ Advanced                                     | ✅ Basic                          |
| **Hooks System**        | ✅ Basic                                      | ✅ **Full System**                              | ❌ None                           |
| **Pre/Post Processing** | ❌ None                                       | ✅ **With Agents**                              | ❌ None                           |
| **Validation**          | ✅ ValidationNodeV2                           | ✅ Advanced                                     | ✅ Basic                          |
| **Recompilation**       | ✅ Auto                                       | ✅ **Hash-based**                               | ✅ Auto                           |
| **Agent-as-Tool**       | ✅ Ready                                      | ✅ **Enhanced**                                 | ✅ Ready                          |
| **Status**              | **Current Default**                           | **Latest Features**                             | Clean Legacy                      |

## Overview

SimpleAgent is designed to be the minimal functional agent that:

- Uses AugLLMConfig as its engine
- Provides convenience fields for common LLM parameters
- Builds a simple graph for LLM + tools + parsing
- Serves as the foundation for other agent types
- **Default import gets you V2** (current stable)
- **V3 available for enhanced features** (hooks, pre/post processing)

## 🔧 Installation & Setup

```bash
# Install Haive framework
poetry install

# SimpleAgent is included in haive-agents package
from haive.agents.simple import SimpleAgent, SimpleAgentV3
```

## 🎯 Use Cases

### SimpleAgent (Default V2) - For Most Users

- **General conversations**: Customer service, Q&A, chat
- **Structured output**: Form filling, data extraction
- **Basic workflows**: Simple task execution
- **Production ready**: Stable, tested, well-documented

### SimpleAgentV3 (Enhanced) - For Advanced Users

- **Complex workflows**: Multi-stage processing with hooks
- **Agent composition**: Agents calling other agents
- **Monitoring & debugging**: Full lifecycle tracking
- **Research & experimentation**: Latest features and patterns

## Features

### Convenience Fields

All these fields sync to the engine during setup:

- `temperature` - LLM temperature (0.0-2.0)
- `max_tokens` - Maximum response tokens
- `model_name` - Model selection
- `force_tool_use` - Force tool usage
- `structured_output_model` - Pydantic model for structured output
- `system_message` - System prompt
- `llm_config` - Full LLM configuration
- `output_parser` - Custom output parser
- `prompt_template` - Custom prompt template

### Structured Output

```python
from pydantic import BaseModel, Field

class Story(BaseModel):
    title: str = Field(description="Story title")
    content: str = Field(description="Story content")
    genre: str = Field(description="Story genre")

agent = SimpleAgent(
    name="story_writer",
    structured_output_model=Story
)
story = agent.run("Write a short sci-fi story")
# story will be a Story instance
```

### Tool Integration

```python
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression))

config = AugLLMConfig(tools=[calculator])
agent = SimpleAgent(name="math_assistant", engine=config)
result = agent.run("What is 15 * 23?")
```

## Graph Structure

The SimpleAgent builds different graphs based on configuration:

1. **Basic** (no tools/parsing): `START → agent_node → END`
2. **With tools**: `START → agent_node → validation → tool_node → agent_node`
3. **With parsing**: `START → agent_node → validation → parse_output → END`
4. **With both**: Combines tool and parsing flows

## API Reference

### Constructor

```python
SimpleAgent(
    name: str = "SimpleAgent",
    engine: AugLLMConfig | None = None,
    temperature: float | None = None,
    max_tokens: int | None = None,
    model_name: str | None = None,
    force_tool_use: bool | None = None,
    structured_output_model: type[BaseModel] | None = None,
    system_message: str | None = None,
    llm_config: LLMConfig | dict | None = None,
    output_parser: BaseOutputParser | None = None,
    prompt_template: ChatPromptTemplate | PromptTemplate | None = None,
    **kwargs
)
```

### Methods

All methods inherited from base Agent:

- `run(input: str) -> Any` - Synchronous execution
- `arun(input: str) -> Any` - Asynchronous execution
- `stream(input: str) -> Iterator` - Streaming execution
- `astream(input: str) -> AsyncIterator` - Async streaming

## Examples

### Basic Conversation

```python
agent = SimpleAgent(name="assistant")
response = agent.run("Tell me about Python")
print(response)
```

### Creative Writing

```python
agent = SimpleAgent(
    name="writer",
    temperature=0.9,
    system_message="You are a creative writer who writes engaging stories."
)
story = agent.run("Write a story about a robot learning to paint")
```

### Data Analysis with Tools

```python
from langchain_core.tools import tool

@tool
def analyze_data(data: str) -> str:
    """Analyze data and return insights."""
    # Analysis logic here
    return "Analysis results..."

config = AugLLMConfig(tools=[analyze_data])
agent = SimpleAgent(
    name="analyst",
    engine=config,
    system_message="You are a data analyst."
)
result = agent.run("Analyze the sales data")
```

## Testing

```bash
poetry run pytest packages/haive-agents/tests/test_simple_agent.py
```

## See Also

- [ReactAgent](../react/README.md) - For agents needing reasoning loops
- [MultiAgent](../multi/README.md) - For coordinating multiple agents
- [BaseRAGAgent](../rag/base/README.md) - For retrieval-augmented generation

## Version History

- v1.0.0: Initial clean implementation as minimal Agent[AugLLMConfig]
