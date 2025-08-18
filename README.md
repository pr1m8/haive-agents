# haive-agents

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/dependency-poetry-blue.svg)](https://python-poetry.org/)
[![Haive Framework](https://img.shields.io/badge/haive-framework-green.svg)](https://github.com/haive-agents/haive-agents)

Dynamic AI agent framework with self-replication, self-modification, dynamic supervision, and real-time schema composition. Build agents that adapt, evolve, and coordinate automatically.

## What is haive-agents?

haive-agents is a sophisticated multi-agent framework that enables the creation of **truly dynamic agents** capable of self-modification, self-replication, runtime adaptation, and autonomous coordination. Unlike static agent frameworks, haive-agents provides agents that can **modify their own behavior**, **spawn new agents**, and **coordinate complex workflows** in real-time.

### Revolutionary Capabilities

- 🧬 **Self-Replication** - Agents can spawn copies of themselves with modified capabilities
- 🔄 **Self-Modification** - Runtime behavior modification and capability enhancement
- 🎯 **Dynamic Supervision** - Adaptive coordination with agent creation/management
- ⚙️ **Provider Switching** - Hot-swap between different LLM providers and models
- 📐 **Schema Composition** - Dynamic state and I/O schema generation
- 🔗 **Multi-Agent Coordination** - Advanced orchestration patterns (sequential, parallel, conditional)
- 🧠 **Advanced Reasoning** - Tree search, reflection, self-discovery, and logical reasoning
- 🗄️ **Graph-Based Memory** - Neo4j knowledge graphs with entity relationships and semantic traversal
- 🧩 **Memory Reorganization** - Intelligent memory consolidation, importance scoring, and lifecycle management
- 🔍 **Multi-Modal Retrieval** - Graph + vector + temporal + importance-based memory retrieval
- 🏗️ **Clean Architecture** - 4 core packages: simple, react, multi, agent + comprehensive memory system

## Quick Start

### Installation

```bash
# Install with poetry (recommended)
poetry add haive-agents

# Or install from source
cd packages/haive-agents
poetry install
```

### Basic Agent Usage

```python
from haive.agents.simple import SimpleAgent
from haive.agents.react import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

# Simple conversational agent
simple_agent = SimpleAgent(
    name="assistant",
    engine=AugLLMConfig(temperature=0.7)
)

result = await simple_agent.arun("Hello, how can you help me?")

# ReAct agent with tools
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression))

react_agent = ReactAgent(
    name="math_assistant",
    engine=AugLLMConfig(tools=[calculator])
)

result = await react_agent.arun("What is 15 * 23?")
```

### Multi-Agent Coordination

```python
from haive.agents.multi import MultiAgent

# Create specialized agents
researcher = ReactAgent(name="researcher", tools=[web_search])
writer = SimpleAgent(name="writer", engine=AugLLMConfig(temperature=0.8))
reviewer = SimpleAgent(name="reviewer", engine=AugLLMConfig(temperature=0.3))

# Coordinate them in a workflow
workflow = MultiAgent(
    name="content_pipeline",
    agents=[researcher, writer, reviewer],
    execution_mode="sequential"
)

result = await workflow.arun("Create a blog post about AI trends")
```

### Dynamic Supervision

```python
from haive.agents.agent import DynamicSupervisorAgent

# Create a supervisor that can spawn and manage agents
supervisor = DynamicSupervisorAgent(
    name="adaptive_coordinator",
    engine=AugLLMConfig(),
    enable_agent_builder=True
)

# Supervisor automatically creates specialized agents based on tasks
result = await supervisor.arun(
    "Analyze this dataset, create visualizations, and write a report"
)
# Supervisor creates: DataAnalyst → Visualizer → ReportWriter agents automatically
```

## Core Architecture

### 1. Package Structure

The framework is organized into 4 clean, focused packages:

```
haive-agents/
├── 🎯 simple/      # Foundation agents - conversation, structured output
├── ⚡ react/       # ReAct pattern - tools, reasoning, planning
├── 🔀 multi/       # Multi-agent coordination - orchestration patterns
└── 🤖 agent/       # Advanced agents - supervision, self-modification
```

### 2. Agent Hierarchy

```
Agent (base class)
├── SimpleAgent (conversation, structured output)
├── ReactAgent (tools + reasoning)
├── MultiAgent (agent coordination)
├── DynamicSupervisorAgent (dynamic agent management)
└── Memory System
    ├── SimpleMemoryAgent (basic memory with classification)
    ├── ReactMemoryAgent (reasoning with memory context)
    ├── MultiMemoryAgent (coordinated memory management)
    ├── LongTermMemoryAgent (persistent memory with consolidation)
    └── IntegratedMemorySystem (unified memory coordination)
```

### 3. Self-Modification System

```python
from haive.agents.agent import SelfModifyingAgent

class AdaptiveAgent(SelfModifyingAgent):
    """Agent that can modify its own behavior based on performance."""
    
    async def arun(self, input_data):
        # Execute task
        result = await super().arun(input_data)
        
        # Analyze performance and self-modify if needed
        if self.performance_below_threshold():
            await self.modify_behavior({
                "temperature": 0.1,  # Become more deterministic
                "system_message": "You are an expert analyst. Be precise.",
                "tools": self.tools + [additional_tool]
            })
        
        return result
```

### 4. Provider Switching

```python
from haive.agents.agent import ProviderSwitchingAgent

class AdaptiveAgent(ProviderSwitchingAgent):
    async def optimize_for_task(self, task_complexity: float):
        if task_complexity > 0.8:
            # Switch to powerful model for complex tasks
            await self.switch_provider({
                "provider": "azure",
                "model": "gpt-4",
                "temperature": 0.1
            })
        else:
            # Use efficient model for simple tasks
            await self.switch_provider({
                "provider": "openai", 
                "model": "gpt-3.5-turbo",
                "temperature": 0.7
            })
```

## Available Agent Types

### Simple Agents

#### SimpleAgent
Foundation agent for conversation and structured output:

```python
from haive.agents.simple import SimpleAgent
from pydantic import BaseModel, Field

class AnalysisResult(BaseModel):
    sentiment: str = Field(description="positive/negative/neutral")
    confidence: float = Field(ge=0.0, le=1.0)

# Basic conversation
agent = SimpleAgent(name="chatbot", engine=AugLLMConfig())

# With structured output
structured_agent = SimpleAgent(
    name="analyzer",
    engine=AugLLMConfig(structured_output_model=AnalysisResult)
)
```

### React Agents

#### ReactAgent
Advanced reasoning with tools and planning:

```python
from haive.agents.react import ReactAgent
from langchain_core.tools import tool

@tool
def web_search(query: str) -> str:
    """Search the web for information."""
    return f"Search results for: {query}"

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    return str(eval(expression))

agent = ReactAgent(
    name="research_assistant",
    engine=AugLLMConfig(tools=[web_search, calculator]),
    max_iterations=5
)
```

### Multi Agents

#### MultiAgent
Coordinate multiple agents in sophisticated workflows:

```python
from haive.agents.multi import MultiAgent

# Sequential workflow
workflow = MultiAgent(
    name="pipeline",
    agents=[planner, executor, reviewer],
    execution_mode="sequential"
)

# Parallel execution
parallel_workflow = MultiAgent(
    name="parallel_analysis",
    agents=[analyzer1, analyzer2, analyzer3],
    execution_mode="parallel"
)

# Conditional routing
conditional_workflow = MultiAgent(
    name="smart_router",
    agents=[classifier, simple_processor, complex_processor],
    execution_mode="conditional"
)

# Add routing logic
conditional_workflow.add_conditional_edge(
    from_agent="classifier",
    condition=lambda state: state.get("complexity") > 0.7,
    true_agent="complex_processor",
    false_agent="simple_processor"
)
```

### Advanced Agents

#### DynamicSupervisorAgent
Intelligent supervisor that can create agents on-demand:

```python
from haive.agents.agent import DynamicSupervisorAgent

supervisor = DynamicSupervisorAgent(
    name="meta_coordinator",
    engine=AugLLMConfig(),
    enable_agent_builder=True
)

# Supervisor analyzes task and creates appropriate agents
await supervisor.arun(
    "I need to: research quantum computing, analyze market data, "
    "create visualizations, and write a technical report"
)

# Supervisor automatically creates and coordinates:
# 1. ResearchAgent(tools=[web_search, paper_search])
# 2. DataAnalyst(tools=[pandas, statistical_analysis])  
# 3. VisualizationAgent(tools=[matplotlib, plotly])
# 4. TechnicalWriter(structured_output=ReportModel)
```

#### SelfReplicatingAgent
Agent that can spawn copies of itself with modifications:

```python
from haive.agents.agent import SelfReplicatingAgent

class ReplicatingAgent(SelfReplicatingAgent):
    async def replicate_for_task(self, task_type: str):
        """Create a specialized copy for specific tasks."""
        
        if task_type == "analysis":
            return await self.replicate({
                "name": f"{self.name}_analyst",
                "temperature": 0.1,
                "system_message": "You are a data analysis expert.",
                "tools": self.tools + [analysis_tool]
            })
        elif task_type == "creative":
            return await self.replicate({
                "name": f"{self.name}_creative",
                "temperature": 0.9,
                "system_message": "You are a creative writing expert.",
                "tools": [writing_tool, inspiration_tool]
            })

# Original agent creates specialized versions
agent = ReplicatingAgent(name="base", engine=config)
analyst = await agent.replicate_for_task("analysis")
writer = await agent.replicate_for_task("creative")
```

### Memory System

#### Graph-Based Memory with Knowledge Graphs
Sophisticated memory system combining Neo4j graphs, vector search, and intelligent reorganization:

```python
from haive.agents.memory_reorganized import SimpleMemoryAgent
from haive.agents.memory_reorganized.coordination import IntegratedMemorySystem

# Basic memory agent with automatic classification
memory_agent = SimpleMemoryAgent(
    name="assistant",
    memory_config={
        "enable_classification": True,
        "store_type": "integrated"  # Graph + Vector + Time
    }
)

# Store memory with automatic type detection and entity extraction
await memory_agent.store_memory("I learned Python at university in 2020")
# -> Automatically classified as EPISODIC + EDUCATION
# -> Entities extracted: ["Python", "university", "2020"] 
# -> Knowledge graph relationships created

# Retrieve with memory-aware context
results = await memory_agent.retrieve_memories("programming experience")
# -> Returns memories with relevance, importance, and recency scores
```

#### Advanced Graph RAG Retrieval
Combine knowledge graph traversal with vector similarity for comprehensive memory retrieval:

```python
from haive.agents.memory_reorganized.retrieval import GraphRAGRetriever
from haive.agents.memory_reorganized.knowledge import KGGeneratorAgent

# Setup Graph RAG with knowledge graph
kg_agent = KGGeneratorAgent(neo4j_config=neo4j_config)
retriever = GraphRAGRetriever(
    kg_agent=kg_agent,
    vector_store=chroma_store,
    enable_graph_traversal=True
)

# Retrieve with graph context and relationship awareness
result = await retriever.retrieve_memories(
    "What's the relationship between Python and machine learning?"
)

print(f"Found {len(result.memories)} memories")
print(f"Explored {result.graph_nodes_explored} entities")
print(f"Relationship paths: {len(result.relationship_paths)}")
print(f"Graph traversal time: {result.graph_traversal_time_ms:.1f}ms")
```

#### Integrated Memory System with Multi-Modal Retrieval
Unified memory system combining graph, vector, and temporal-based retrieval:

```python
from haive.agents.memory_reorganized.coordination import IntegratedMemorySystem

# Configure multi-modal memory system
memory_system = IntegratedMemorySystem(
    mode="INTEGRATED",  # Graph + Vector + Time-based
    graph_config=graph_config,
    vector_config=vector_config,
    enable_consolidation=True,
    enable_importance_scoring=True
)

# Store with automatic processing
await memory_system.store_memory(
    "I prefer morning meetings because I'm most productive then",
    user_context={"user_id": "alice", "timezone": "EST"}
)
# -> Classified as PREFERENCE + TEMPORAL
# -> Entities extracted: ["meetings", "morning", "productivity"]
# -> Graph relationships: alice -> prefers -> morning_meetings
# -> Importance scoring based on personal preference patterns

# Query with intelligent routing
results = await memory_system.query_memory(
    "scheduling preferences", 
    max_results=10,
    include_graph_context=True
)
# -> Routes to optimal retrieval strategy (graph + vector + temporal)
# -> Returns results with multi-factor scoring
```

#### Memory Types Supported
11 cognitive memory types with automatic classification:

- **SEMANTIC**: Facts, concepts, definitions ("Python is a programming language")
- **EPISODIC**: Personal experiences, events ("Yesterday I met John at the coffee shop")  
- **PROCEDURAL**: How-to knowledge, processes ("To make coffee, first heat water")
- **CONTEXTUAL**: Entity relationships ("John works at Microsoft and knows Sarah")
- **PREFERENCE**: Likes, dislikes, patterns ("I prefer tea over coffee in the morning")
- **META**: Self-awareness, learning patterns ("I learn better with examples")
- **EMOTIONAL**: Feelings, sentiments ("I felt frustrated when the meeting was cancelled")
- **TEMPORAL**: Time-based patterns ("I usually exercise at 6 AM")
- **ERROR**: Mistakes, corrections ("I was wrong about the meeting time")
- **FEEDBACK**: User corrections, evaluations ("That summary was too long")
- **SYSTEM**: Configuration, settings ("Set notification frequency to daily")

## Advanced Features

### 1. Real-Time Recompilation

Agents automatically recompile when their configuration changes:

```python
agent = SimpleAgent(name="adaptive", engine=config)

# Add tool dynamically - triggers recompilation
agent.add_tool(new_calculator_tool)
# Agent's graph is automatically rebuilt

# Change system message - triggers recompilation  
agent.engine.system_message = "You are now a math expert."
# Agent adapts immediately
```

### 2. Hierarchical State Management

Multi-agent workflows maintain isolated yet connected state:

```python
from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState

# Each agent gets its own state view
class WorkflowState(MultiAgentState):
    # Shared across all agents
    task_description: str
    shared_context: Dict[str, Any]
    
    # Agent-specific private state
    planner_state: PlannerState  # Only planner sees this
    executor_state: ExecutorState  # Only executor sees this
```

### 3. Dynamic Schema Composition

```python
from haive.core.schema.composer import DynamicSchemaComposer

# Compose schemas based on agent requirements
composer = DynamicSchemaComposer()

# Automatically generate state schema for workflow
workflow_schema = composer.compose_for_agents([
    ReactAgent(name="analyzer"),
    SimpleAgent(name="formatter", structured_output=ReportModel),
    ReactAgent(name="reviewer")
])
```

### 4. Tool Transfer and Sharing

```python
from haive.agents.agent import ToolTransferMixin

class CollaborativeAgent(SimpleAgent, ToolTransferMixin):
    async def share_tools_with(self, other_agent, tool_names: List[str]):
        """Transfer specific tools to another agent."""
        await self.transfer_tools(other_agent, tool_names)
        
agent1 = CollaborativeAgent(name="specialist", tools=[expert_tool])
agent2 = CollaborativeAgent(name="generalist", tools=[basic_tools])

# Share expertise
await agent1.share_tools_with(agent2, ["expert_tool"])
```

## Common Workflows

### 1. Self-Organizing Agent Team

```python
# Create a supervisor that builds its own team
supervisor = DynamicSupervisorAgent(
    name="team_builder",
    enable_agent_builder=True,
    auto_team_optimization=True
)

# Supervisor analyzes task and builds optimal team
result = await supervisor.arun({
    "task": "Build a web application with user authentication",
    "requirements": ["security", "scalability", "user experience"]
})

# Supervisor creates:
# - BackendAgent(tools=[python, fastapi, database])
# - SecurityAgent(tools=[auth, encryption, validation])  
# - FrontendAgent(tools=[react, css, testing])
# - DevOpsAgent(tools=[docker, kubernetes, monitoring])
```

### 2. Adaptive Multi-Agent Pipeline

```python
# Multi-stage processing that adapts based on complexity
planner = ReactAgent(name="planner", tools=[analysis_tools])
simple_executor = SimpleAgent(name="simple_executor")
complex_executor = ReactAgent(name="complex_executor", tools=[advanced_tools])
reviewer = SimpleAgent(name="reviewer")

# Adaptive pipeline
adaptive_pipeline = MultiAgent(
    name="adaptive_workflow",
    agents=[planner, simple_executor, complex_executor, reviewer],
    execution_mode="conditional"
)

# Route based on task complexity
adaptive_pipeline.add_conditional_edge(
    from_agent="planner",
    condition=lambda state: state.get("complexity") > 0.7,
    true_agent="complex_executor",  # Complex tasks
    false_agent="simple_executor"   # Simple tasks
)

adaptive_pipeline.add_edge("simple_executor", "reviewer")
adaptive_pipeline.add_edge("complex_executor", "reviewer")
```

### 3. Self-Improving Agent Colony

```python
# Agents that improve through interaction and feedback
class EvolvingAgent(SimpleAgent, SelfModifyingAgent, SelfReplicatingAgent):
    async def evolve_from_feedback(self, feedback: Dict[str, Any]):
        """Evolve based on performance feedback."""
        if feedback["accuracy"] < 0.7:
            # Create improved version
            improved = await self.replicate({
                "temperature": self.engine.temperature * 0.8,
                "system_message": f"{self.engine.system_message}\nFocus on accuracy.",
            })
            return improved
        return self

# Create evolving colony
colony = [
    EvolvingAgent(name=f"agent_{i}", engine=base_config)
    for i in range(5)
]

# Agents evolve based on performance
for agent in colony:
    feedback = await evaluate_agent_performance(agent)
    improved_agent = await agent.evolve_from_feedback(feedback)
    if improved_agent != agent:
        colony[colony.index(agent)] = improved_agent
```

### 4. Hierarchical Supervision

```python
class HierarchicalSupervisor(DynamicSupervisorAgent):
    """Multi-level supervision with sub-supervisors."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sub_supervisors: Dict[str, DynamicSupervisorAgent] = {}
    
    async def create_sub_supervisor(self, domain: str, agents: List[Agent]):
        """Create domain-specific sub-supervisor."""
        sub_supervisor = DynamicSupervisorAgent(
            name=f"{domain}_supervisor",
            engine=self.engine,
            enable_agent_builder=False  # Managed by parent
        )
        
        # Initialize with domain agents
        for agent in agents:
            sub_supervisor.add_agent(agent)
        
        self.sub_supervisors[domain] = sub_supervisor
        return sub_supervisor

# Create hierarchical system
main_supervisor = HierarchicalSupervisor(name="main")

# Create domain supervisors
research_supervisor = await main_supervisor.create_sub_supervisor(
    "research", [web_search_agent, paper_analysis_agent]
)

development_supervisor = await main_supervisor.create_sub_supervisor(
    "development", [code_agent, test_agent, deploy_agent]
)
```

## Agent Architecture Patterns

### Pattern 1: Self-Modifying Specialist

```python
from haive.agents.agent import SelfModifyingAgent

class ExpertAgent(SimpleAgent, SelfModifyingAgent):
    """Agent that becomes more specialized over time."""
    
    def __init__(self, domain: str, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.expertise_level = 1.0
    
    async def enhance_expertise(self, new_knowledge: Dict[str, Any]):
        """Enhance domain expertise based on new knowledge."""
        self.expertise_level += 0.1
        
        # Modify system message to be more specialized
        enhanced_message = f"""You are a level {self.expertise_level:.1f} expert in {self.domain}.
        New knowledge: {new_knowledge}
        Apply this expertise to all responses."""
        
        await self.modify_behavior({
            "system_message": enhanced_message,
            "temperature": max(0.1, self.engine.temperature - 0.05)
        })
```

### Pattern 2: Adaptive Multi-Agent System

```python
from haive.agents.multi import MultiAgent

class AdaptiveWorkflow(MultiAgent):
    """Workflow that adapts its structure based on task requirements."""
    
    async def adapt_to_task(self, task_description: str):
        """Restructure workflow based on task complexity."""
        complexity = await self.analyze_task_complexity(task_description)
        
        if complexity > 0.8:
            # Complex task: add more specialized agents
            self.add_agent(DeepAnalysisAgent(name="deep_analyzer"))
            self.add_agent(QualityAssuranceAgent(name="qa_specialist"))
            
            # Change to sequential for thorough processing
            self.execution_mode = "sequential"
        else:
            # Simple task: streamline workflow
            self.execution_mode = "parallel"
        
        # Rebuild graph with new structure
        await self.rebuild_graph()
```

### Pattern 3: Multi-Model Orchestration

```python
from haive.agents.multi import MultiAgent

class MultiModelWorkflow(MultiAgent):
    """Use different models for different tasks."""
    
    def __init__(self, **kwargs):
        # Creative agent with high-temperature model
        creative = SimpleAgent(
            name="creative",
            engine=AugLLMConfig(model="gpt-4", temperature=0.9)
        )
        
        # Analytical agent with low-temperature model
        analytical = SimpleAgent(
            name="analytical", 
            engine=AugLLMConfig(model="gpt-4", temperature=0.1)
        )
        
        # Efficient agent with smaller model
        efficient = SimpleAgent(
            name="efficient",
            engine=AugLLMConfig(model="gpt-3.5-turbo", temperature=0.5)
        )
        
        super().__init__(
            agents=[creative, analytical, efficient],
            **kwargs
        )
```

## Performance and Optimization

### Real-Time Compilation

All agents support hot-recompilation when their configuration changes:

- **Tool Changes**: Adding/removing tools triggers graph rebuild
- **Schema Updates**: State schema modifications trigger recompilation
- **Config Changes**: Engine configuration changes trigger rebuild
- **Agent Addition**: Multi-agent workflows recompile when agents added

### Memory Management

Agents include sophisticated memory patterns:

- **Conversation Memory**: Persistent conversation history
- **Vector Memory**: Semantic memory for relevant context
- **Hierarchical Memory**: Multi-level memory systems
- **Shared Memory**: Memory sharing between agents

### Concurrent Execution

Multi-agent workflows support true concurrency:

- **Parallel Execution**: Multiple agents run simultaneously
- **Async Coordination**: Full async/await support
- **State Synchronization**: Thread-safe state management
- **Resource Pooling**: Efficient resource sharing

## Testing Philosophy

haive-agents follows a **NO MOCKS** testing philosophy:

```bash
# All tests use real LLMs and components
poetry run pytest packages/haive-agents/tests/ -v

# Integration tests with real providers
poetry run pytest packages/haive-agents/tests/integration/ -v

# Performance benchmarks
poetry run pytest packages/haive-agents/tests/benchmarks/ -v
```

**Why No Mocks?**
- Tests validate real LLM behavior
- Ensures production readiness
- Catches integration issues early
- Validates complex multi-agent interactions

## Package Structure

```
haive-agents/
├── 📚 project_docs/              # Comprehensive documentation
│   ├── guides/                   # Usage guides and patterns
│   ├── architecture/             # System design documents
│   ├── patterns/                 # Common implementation patterns
│   └── examples/                 # Working code examples
├── 🧹 src/haive/agents/          # Clean source code
│   ├── simple/                   # Foundation agents
│   ├── react/                    # ReAct pattern agents
│   ├── multi/                    # Multi-agent coordination
│   ├── agent/                    # Advanced agent capabilities
│   └── base/                     # Base classes and mixins
├── 🎯 examples/                  # Organized examples
│   ├── basic/                    # Getting started examples
│   ├── advanced/                 # Complex multi-agent scenarios
│   ├── self_modification/        # Self-modifying agent examples
│   └── dynamic_supervision/      # Supervisor pattern examples
├── ✅ tests/                     # Comprehensive tests (NO MOCKS)
│   ├── simple/                   # SimpleAgent tests
│   ├── react/                    # ReactAgent tests
│   ├── multi/                    # Multi-agent tests
│   ├── agent/                    # Advanced agent tests
│   └── integration/              # End-to-end integration tests
└── 🔧 scripts/                   # Development utilities
```

## Advanced Usage

### Custom Agent Development

```python
from haive.agents.base.agent import Agent

class MyAdvancedAgent(Agent):
    """Custom agent with specialized behavior."""
    
    def build_graph(self) -> BaseGraph:
        """Implement required abstract method."""
        graph = BaseGraph(name=f"{self.name}_graph")
        # Custom graph building logic
        return graph
    
    async def adaptive_execution(self, input_data):
        """Custom execution with adaptation."""
        # Analyze input and adapt if needed
        complexity = self.analyze_complexity(input_data)
        
        if complexity > self.capability_threshold:
            # Enhance capabilities for complex tasks
            await self.enhance_capabilities(complexity)
        
        return await self.arun(input_data)
```

### Real-Time Agent Evolution

```python
from haive.agents.agent import EvolutionarySystem

class EvolutionarySystem:
    """System that evolves agents based on performance."""
    
    def __init__(self):
        self.agents: List[Agent] = []
        self.performance_history: Dict[str, List[float]] = {}
    
    async def evolve_population(self):
        """Evolve agent population based on performance."""
        # Evaluate all agents
        performances = await self.evaluate_all_agents()
        
        # Select top performers
        top_agents = self.select_top_performers(performances, top_k=3)
        
        # Create variations of top performers
        new_agents = []
        for agent in top_agents:
            if hasattr(agent, 'replicate'):
                # Create mutations
                variation1 = await agent.replicate({
                    "temperature": agent.engine.temperature * 0.9,
                    "system_message": f"Enhanced: {agent.engine.system_message}"
                })
                variation2 = await agent.replicate({
                    "temperature": agent.engine.temperature * 1.1,
                    "tools": agent.tools + [self.get_random_tool()]
                })
                new_agents.extend([variation1, variation2])
        
        # Replace bottom performers with new variants
        self.agents = top_agents + new_agents
```

## Troubleshooting

### Common Issues

1. **Graph Compilation Errors**
   ```python
   # Check agent configuration
   agent.validate_configuration()
   
   # Manually trigger recompilation
   await agent.rebuild_graph()
   ```

2. **State Schema Conflicts**
   ```python
   # Use schema composition for complex workflows
   from haive.core.schema.composer import DynamicSchemaComposer
   composer = DynamicSchemaComposer()
   resolved_schema = composer.resolve_conflicts(agent_schemas)
   ```

3. **Provider Connection Issues**
   ```python
   # Test provider connectivity
   await agent.test_provider_connection()
   
   # Switch to backup provider
   await agent.switch_provider(backup_config)
   ```

### Debug Mode

```python
# Enable comprehensive debugging
import logging
logging.getLogger("haive.agents").setLevel(logging.DEBUG)

# Check agent internal state
agent.display_debug_info()

# Monitor multi-agent coordination
workflow.enable_execution_monitoring()
```

## Examples & Documentation

### 🚀 Quick Start

```bash
# 5-minute setup guide
see project_docs/guides/quick-start.md

# Run basic example
poetry run python examples/basic_agent.py
```

### 📚 Comprehensive Documentation

- **[Project Documentation](project_docs/README.md)** - Complete documentation hub
- **[Architecture Guide](project_docs/architecture/README.md)** - System design
- **[Usage Patterns](project_docs/guides/usage-patterns.md)** - Common scenarios
- **[Examples](project_docs/examples/README.md)** - Working code examples

### 🎯 Key Examples

```bash
# Basic agent usage
poetry run python examples/simple_agent_example.py

# ReAct agents with tools
poetry run python examples/react_agent_example.py

# Multi-agent coordination
poetry run python examples/multi_agent_workflow.py

# Dynamic supervision
poetry run python examples/dynamic_supervisor.py

# Self-modifying agents
poetry run python examples/self_modification.py
```

## Testing

```bash
# Run all tests
poetry run pytest

# Run specific package tests
poetry run pytest tests/simple/ -v
poetry run pytest tests/react/ -v
poetry run pytest tests/multi/ -v
poetry run pytest tests/agent/ -v

# Run with coverage
poetry run pytest --cov=haive.agents
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Follow the NO MOCKS testing philosophy
4. Add comprehensive tests with real LLMs
5. Ensure all agents support dynamic patterns
6. Submit a pull request

## License

MIT License - see LICENSE file for details.

## References

- [Haive Agents Repository](https://github.com/haive-agents/haive-agents)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [Self-Discover Paper](https://arxiv.org/abs/2402.03620)
- [Tree of Thoughts Paper](https://arxiv.org/abs/2305.10601)

## Support

For issues and questions:

- GitHub Issues: [haive-agents/issues](https://github.com/haive-agents/haive-agents/issues)
- Documentation: [haive-agents.readthedocs.io](https://haive-agents.readthedocs.io)