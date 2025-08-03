# 🗂️ Haive Examples Master Index

**Your Complete Guide to Every Example in Haive**

## 🎯 Quick Navigation

| 🎓 **Learning Path**                         | 📁 **Location**           | 📊 **Count** | ⏱️ **Time** | 🎯 **Purpose**                 |
| -------------------------------------------- | ------------------------- | ------------ | ----------- | ------------------------------ |
| [🌱 **Beginner**](#beginner-gallery)         | `galleries/beginner/`     | 5 examples   | 30 min      | First steps, basic concepts    |
| [🌿 **Intermediate**](#intermediate-gallery) | `galleries/intermediate/` | 4 examples   | 1-2 hours   | Multi-agent, workflows         |
| [🌲 **Advanced**](#advanced-gallery)         | `galleries/advanced/`     | 3 examples   | 2-4 hours   | Complex patterns, optimization |
| [🎮 **Games**](#games-gallery)               | `galleries/games/`        | 6 examples   | 1-2 hours   | AI gaming, strategy            |
| [📚 **Reference**](#reference-patterns)      | `reference/`              | 15 patterns  | As needed   | Technical implementation       |
| [🎯 **Showcase**](#production-showcase)      | `showcase/`               | 8 examples   | As needed   | Production-ready apps          |
| [📖 **Tutorials**](#step-by-step-tutorials)  | `tutorials/`              | 5 guides     | 3-5 hours   | Complete projects              |
| [🏛️ **Legacy**](#legacy-examples)            | `examples/`               | 12 examples  | Various     | Original examples              |
| [📦 **Source**](#source-examples)            | `src/.../example.py`      | 39 examples  | Various     | Module-specific demos          |

---

## 🌱 Beginner Gallery

**Perfect for newcomers to Haive**

### 📍 Location: `galleries/beginner/`

| 📋 **Example**               | 🎯 **What You'll Learn**            | ⏱️ **Time** | 🔗 **Next Step**    |
| ---------------------------- | ----------------------------------- | ----------- | ------------------- |
| **simple_agent_tutorial.py** | Basic agent creation, conversations | 5 min       | ReactAgent tutorial |
| **react_agent_tutorial.py**  | Tool integration, reasoning loops   | 10 min      | Structured output   |
| **simple_agent_example.py**  | Original simple agent demo          | 5 min       | Multi-agent basics  |
| **react_agent_example.py**   | Original ReactAgent demo            | 10 min      | Planning workflows  |
| **basic_tools_tutorial.py**  | Custom tool creation                | 10 min      | Advanced patterns   |

### 🚀 **Quick Start**

```bash
cd galleries/beginner
poetry run python simple_agent_tutorial.py
```

---

## 🌿 Intermediate Gallery

**Multi-agent coordination and workflows**

### 📍 Location: `galleries/intermediate/`

| 📋 **Example**                | 🎯 **What You'll Learn**                 | ⏱️ **Time** | 🔗 **Next Step**    |
| ----------------------------- | ---------------------------------------- | ----------- | ------------------- |
| **plan_and_execute_guide.py** | Strategic planning, multi-step workflows | 15 min      | Advanced workflows  |
| **multi_agent_example.py**    | Agent coordination, communication        | 20 min      | Supervisor patterns |
| **structured_output_demo.py** | Data extraction, Pydantic models         | 15 min      | Production apps     |
| **supervisor_patterns.py**    | Agent orchestration, delegation          | 25 min      | Advanced patterns   |

### 🚀 **Quick Start**

```bash
cd galleries/intermediate
poetry run python plan_and_execute_guide.py
```

---

## 🌲 Advanced Gallery

**Complex patterns and optimization**

### 📍 Location: `galleries/advanced/`

| 📋 **Example**                             | 🎯 **What You'll Learn** | ⏱️ **Time** | 🔗 **Next Step**         |
| ------------------------------------------ | ------------------------ | ----------- | ------------------------ |
| **dynamic_activation_advanced_example.py** | Dynamic agent networks   | 30 min      | Production deployment    |
| **custom_workflow_patterns.py**            | Custom graph patterns    | 45 min      | Performance optimization |
| **performance_optimization.py**            | Speed and efficiency     | 30 min      | Production monitoring    |

### 🚀 **Quick Start**

```bash
cd galleries/advanced
poetry run python dynamic_activation_advanced_example.py
```

---

## 🎮 Games Gallery

**AI agents playing games**

### 📍 Location: `galleries/games/`

| 📋 **Example**             | 🎯 **What You'll Learn**       | ⏱️ **Time** | 🔗 **Next Step**      |
| -------------------------- | ------------------------------ | ----------- | --------------------- |
| **tic_tac_toe_ai.py**      | Game strategy, decision making | 15 min      | Chess strategy        |
| **chess_strategy.py**      | Complex strategy, evaluation   | 25 min      | Multi-player games    |
| **connect4_tournament.py** | AI vs AI competitions          | 20 min      | Game tournaments      |
| **multi_game_agent.py**    | Versatile game playing         | 30 min      | Advanced strategies   |
| **strategy_evaluation.py** | Performance analysis           | 20 min      | Custom games          |
| **game_learning.py**       | Adaptive strategy learning     | 35 min      | Research applications |

### 🚀 **Quick Start**

```bash
cd galleries/games
poetry run python tic_tac_toe_ai.py
```

---

## 📚 Reference Patterns

**Technical implementation patterns**

### 📍 Location: `reference/`

#### 🤖 **Agent Types** (`reference/agent_types/`)

| 📋 **Pattern**               | 🎯 **Purpose**              | 🔗 **Use When**                  |
| ---------------------------- | --------------------------- | -------------------------------- |
| **simple_agent_patterns.py** | Basic agent implementations | Building conversational agents   |
| **react_agent_patterns.py**  | Tool-enabled reasoning      | Need problem-solving with tools  |
| **multi_agent_patterns.py**  | Agent coordination          | Multiple agents working together |
| **supervisor_patterns.py**   | Agent orchestration         | Complex workflow management      |
| **custom_agent_patterns.py** | Custom implementations      | Specialized use cases            |

#### 🛠️ **Tools** (`reference/tools/`)

| 📋 **Pattern**         | 🎯 **Purpose**             | 🔗 **Use When**                |
| ---------------------- | -------------------------- | ------------------------------ |
| **custom_tools.py**    | Tool creation patterns     | Building domain-specific tools |
| **tool_routing.py**    | Dynamic tool selection     | Conditional tool usage         |
| **tool_management.py** | Tool lifecycle management  | Complex tool orchestration     |
| **tool_validation.py** | Input/output validation    | Robust tool implementations    |
| **async_tools.py**     | Asynchronous tool patterns | High-performance applications  |

#### 🗃️ **State Management** (`reference/state/`)

| 📋 **Pattern**              | 🎯 **Purpose**            | 🔗 **Use When**             |
| --------------------------- | ------------------------- | --------------------------- |
| **state_schemas.py**        | State modeling patterns   | Complex state requirements  |
| **state_management.py**     | State lifecycle patterns  | Multi-step workflows        |
| **persistence_patterns.py** | State persistence         | Long-running applications   |
| **state_validation.py**     | State validation patterns | Data integrity requirements |
| **state_composition.py**    | Composite state patterns  | Complex agent hierarchies   |

#### 🔌 **Integration** (`reference/integration/`)

| 📋 **Pattern**              | 🎯 **Purpose**            | 🔗 **Use When**                 |
| --------------------------- | ------------------------- | ------------------------------- |
| **api_integration.py**      | External API patterns     | Third-party service integration |
| **database_integration.py** | Database connectivity     | Data persistence needs          |
| **external_services.py**    | Service integration       | Microservice architectures      |
| **webhook_patterns.py**     | Event-driven patterns     | Real-time integrations          |
| **streaming_patterns.py**   | Real-time data processing | Live data applications          |

---

## 🎯 Production Showcase

**Real-world applications**

### 📍 Location: `showcase/`

| 📋 **Application**         | 🎯 **Use Case**             | 🏗️ **Architecture**      | 🔗 **Industry**         |
| -------------------------- | --------------------------- | ------------------------ | ----------------------- |
| **chat_assistant.py**      | Customer support            | ReactAgent + RAG         | Customer Service        |
| **research_assistant.py**  | Research automation         | Multi-agent workflow     | Research & Academia     |
| **code_analyst.py**        | Code review automation      | Planning + Analysis      | Software Development    |
| **game_coordinator.py**    | Tournament management       | Multi-agent coordination | Gaming & Entertainment  |
| **workflow_automation.py** | Business process automation | Supervisor patterns      | Business Operations     |
| **data_processor.py**      | Data analysis pipeline      | Sequential agents        | Data Science            |
| **content_creator.py**     | Content generation          | Multi-modal agents       | Marketing & Media       |
| **monitoring_system.py**   | System monitoring           | Event-driven agents      | DevOps & Infrastructure |

### 🚀 **Quick Start**

```bash
cd showcase
poetry run python chat_assistant.py
```

---

## 📖 Step-by-Step Tutorials

**Complete project guides**

### 📍 Location: `tutorials/`

| 📋 **Tutorial**               | 🎯 **Project**               | ⏱️ **Time** | 🎓 **Level** |
| ----------------------------- | ---------------------------- | ----------- | ------------ |
| **getting_started.py**        | Your first agent application | 30 min      | Beginner     |
| **building_chatbot.py**       | Complete chatbot with memory | 1 hour      | Intermediate |
| **multi_agent_system.py**     | Coordinated agent team       | 2 hours     | Advanced     |
| **production_deployment.py**  | Deploy to production         | 1 hour      | Advanced     |
| **custom_agent_framework.py** | Build custom patterns        | 3 hours     | Expert       |

### 🚀 **Quick Start**

```bash
cd tutorials
poetry run python getting_started.py
```

---

## 🏛️ Legacy Examples

**Original examples (maintained for compatibility)**

### 📍 Location: `examples/`

| 📋 **Example**                          | 🎯 **Purpose**       | ⚠️ **Status** | 🔗 **Alternative**                                          |
| --------------------------------------- | -------------------- | ------------- | ----------------------------------------------------------- |
| **plan_and_execute_example.py**         | Planning workflows   | Legacy        | `galleries/intermediate/plan_and_execute_guide.py`          |
| **dynamic_activation_basic_example.py** | Dynamic agents       | Legacy        | `galleries/advanced/dynamic_activation_advanced_example.py` |
| **dynamic_react_agent_example.py**      | Dynamic ReactAgent   | Legacy        | `galleries/beginner/react_agent_tutorial.py`                |
| **dynamic_supervisor_demo.py**          | Supervisor patterns  | Legacy        | `galleries/intermediate/supervisor_patterns.py`             |
| **dynamic_supervisor_example.py**       | Supervisor workflows | Legacy        | `galleries/intermediate/supervisor_patterns.py`             |
| **enhanced_memory_retriever_demo.py**   | Memory systems       | Legacy        | `reference/state/persistence_patterns.py`                   |
| **full_supervisor_demo.py**             | Complete supervisor  | Legacy        | `showcase/workflow_automation.py`                           |
| **output_adapter_demo.py**              | Output formatting    | Legacy        | `reference/tools/tool_validation.py`                        |
| **token_tracking_example.py**           | Token management     | Legacy        | `reference/integration/api_integration.py`                  |
| **validation_integration_example.py**   | Validation patterns  | Legacy        | `reference/state/state_validation.py`                       |
| **supervisor/**                         | Supervisor examples  | Legacy        | `galleries/intermediate/`                                   |

---

## 📦 Source Examples

**Module-specific demonstrations**

### 📍 Location: `src/haive/agents/*/example.py`

#### 🔧 **Core Agents**

| 📋 **Module**             | 📍 **Location**                          | 🎯 **Purpose**    |
| ------------------------- | ---------------------------------------- | ----------------- |
| **SimpleAgent**           | `src/haive/agents/simple/example.py`     | Basic agent usage |
| **ReactAgent**            | `src/haive/agents/react/example.py`      | Tool integration  |
| **StructuredOutputAgent** | `src/haive/agents/structured/example.py` | Data extraction   |

#### 🧠 **RAG Agents**

| 📋 **Module**             | 📍 **Location**                            | 🎯 **Purpose**         |
| ------------------------- | ------------------------------------------ | ---------------------- |
| **BaseRAGAgent**          | `src/haive/agents/rag/base/example.py`     | Basic RAG patterns     |
| **AdaptiveRAGAgent**      | `src/haive/agents/rag/adaptive/example.py` | Adaptive retrieval     |
| **HyDERAGAgent**          | `src/haive/agents/rag/hyde/example.py`     | Hypothetical documents |
| **SelfRAGAgent**          | `src/haive/agents/rag/self/example.py`     | Self-reflective RAG    |
| **MultiStrategyRAGAgent** | `src/haive/agents/rag/multi/example.py`    | Multiple strategies    |

#### 💬 **Conversation Agents**

| 📋 **Module**          | 📍 **Location**                                          | 🎯 **Purpose**        |
| ---------------------- | -------------------------------------------------------- | --------------------- |
| **DebateAgent**        | `src/haive/agents/conversation/debate/example.py`        | Debate simulations    |
| **CollaborativeAgent** | `src/haive/agents/conversation/collaborative/example.py` | Team collaboration    |
| **RoundRobinAgent**    | `src/haive/agents/conversation/round_robin/example.py`   | Turn-based discussion |
| **SocialMediaAgent**   | `src/haive/agents/conversation/social_media/example.py`  | Social interactions   |

#### 🎯 **Planning Agents**

| 📋 **Module**           | 📍 **Location**                                         | 🎯 **Purpose**       |
| ----------------------- | ------------------------------------------------------- | -------------------- |
| **PlanAndExecuteAgent** | `src/haive/agents/planning/plan_and_execute/example.py` | Strategic planning   |
| **TreeOfThoughtsAgent** | `src/haive/agents/planning/tot/example.py`              | Reasoning trees      |
| **MCTSAgent**           | `src/haive/agents/planning/mcts/example.py`             | Monte Carlo planning |
| **ReWOOAgent**          | `src/haive/agents/planning/rewoo/example.py`            | Reasoning workflows  |

#### 🔬 **Research Agents**

| 📋 **Module**               | 📍 **Location**                                  | 🎯 **Purpose**      |
| --------------------------- | ------------------------------------------------ | ------------------- |
| **PersonResearchAgent**     | `src/haive/agents/research/person/example.py`    | Person research     |
| **STORMAgent**              | `src/haive/agents/research/storm/example.py`     | Research synthesis  |
| **ComponentDiscoveryAgent** | `src/haive/agents/research/discovery/example.py` | Component discovery |

#### 📄 **Document Agents**

| 📋 **Module**           | 📍 **Location**                                   | 🎯 **Purpose**           |
| ----------------------- | ------------------------------------------------- | ------------------------ |
| **SummarizerAgent**     | `src/haive/agents/document/summarizer/example.py` | Document summarization   |
| **KGGeneratorAgent**    | `src/haive/agents/document/kg/example.py`         | Knowledge graph creation |
| **DocumentLoaderAgent** | `src/haive/agents/document/loader/example.py`     | Document processing      |

---

## 🎮 Games Examples

**AI game-playing agents**

### 📍 Location: `../haive-games/examples/` & `../haive-games/src/`

| 🎲 **Game**     | 📍 **Location**                        | 🎯 **AI Strategy**   | 🏆 **Difficulty** |
| --------------- | -------------------------------------- | -------------------- | ----------------- |
| **Tic-Tac-Toe** | `examples/tic_tac_toe_example.py`      | Minimax algorithm    | Beginner          |
| **Chess**       | `examples/chess_api_example.py`        | Strategic evaluation | Advanced          |
| **Connect4**    | `examples/connect4_working_example.py` | Pattern recognition  | Intermediate      |
| **Poker**       | `src/haive/games/poker/example.py`     | Probability analysis | Advanced          |
| **Blackjack**   | `src/haive/games/blackjack/example.py` | Card counting        | Intermediate      |
| **Among Us**    | `examples/run_among_us.py`             | Deduction logic      | Advanced          |

---

## 🔍 Search & Filter

### 🏷️ **By Difficulty**

- **🌱 Beginner**: `galleries/beginner/`, basic source examples
- **🌿 Intermediate**: `galleries/intermediate/`, workflow examples
- **🌲 Advanced**: `galleries/advanced/`, complex patterns
- **🎓 Expert**: `tutorials/`, custom implementations

### 🕐 **By Time Investment**

- **⚡ Quick (5-15 min)**: Beginner gallery, basic source examples
- **🚀 Medium (15-60 min)**: Intermediate gallery, single concepts
- **🔥 Long (1-4 hours)**: Advanced gallery, complete projects
- **💫 Marathon (4+ hours)**: Tutorial series, custom frameworks

### 🎯 **By Purpose**

- **📚 Learning**: `galleries/`, `tutorials/`
- **🔍 Reference**: `reference/`, `src/*/example.py`
- **🚀 Production**: `showcase/`, production-ready examples
- **🎮 Fun**: `galleries/games/`, game examples

### 🏗️ **By Architecture**

- **Single Agent**: `galleries/beginner/`, simple examples
- **Multi-Agent**: `galleries/intermediate/`, coordination examples
- **Complex Workflows**: `galleries/advanced/`, enterprise patterns
- **Game AI**: `galleries/games/`, strategic thinking

---

## 🚀 Quick Commands

```bash
# Navigate to any gallery
cd packages/haive-agents/galleries/beginner
cd packages/haive-agents/galleries/intermediate
cd packages/haive-agents/galleries/advanced
cd packages/haive-agents/galleries/games

# Run examples
poetry run python simple_agent_tutorial.py
poetry run python react_agent_tutorial.py
poetry run python plan_and_execute_guide.py
poetry run python tic_tac_toe_ai.py

# Browse reference patterns
ls reference/agent_types/
ls reference/tools/
ls reference/state/
ls reference/integration/

# Check production examples
ls showcase/

# Follow tutorials
ls tutorials/
```

---

## 📊 Statistics

- **Total Examples**: 92 across all categories
- **Galleries**: 18 curated examples
- **Reference Patterns**: 20 implementation patterns
- **Production Examples**: 8 real-world applications
- **Tutorial Projects**: 5 complete guides
- **Legacy Examples**: 12 maintained for compatibility
- **Source Examples**: 39 module-specific demos
- **Game Examples**: 6 AI game implementations

---

## 🗺️ Your Learning Journey

### 🎯 **Recommended Path**

1. **Start Here**: `galleries/beginner/simple_agent_tutorial.py`
2. **Add Tools**: `galleries/beginner/react_agent_tutorial.py`
3. **Multi-Agent**: `galleries/intermediate/multi_agent_example.py`
4. **Planning**: `galleries/intermediate/plan_and_execute_guide.py`
5. **Advanced**: `galleries/advanced/dynamic_activation_advanced_example.py`
6. **Games**: `galleries/games/tic_tac_toe_ai.py`
7. **Production**: `showcase/chat_assistant.py`
8. **Custom**: `tutorials/custom_agent_framework.py`

### 🎓 **Mastery Checkpoints**

- **✅ Beginner**: Can create and run basic agents
- **✅ Intermediate**: Can coordinate multiple agents
- **✅ Advanced**: Can build complex workflows
- **✅ Expert**: Can create custom patterns and deploy to production

---

**🎯 Pick your starting point and dive in!** Every example is designed to teach you something new while building on previous knowledge.
