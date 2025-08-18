Agent Types
===========

Haive Agents provides a comprehensive suite of **dynamically recompilable and fully serializable agent types**, each capable of runtime modification across their entire component stack. From simple conversational agents to sophisticated multi-agent orchestrators, our framework offers **living, adaptable building blocks** that can modify their tools, LLM configurations, retrieval systems, graph structures, and coordination patterns **at runtime without restarts**.

Foundation Agents
-----------------

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: SimpleAgent
      :img-top: _static/simple-agent-large.png
      :link: #simple-agent
      :link-type: ref
      :class-card: foundation-card

      **Dynamic Foundation Agent with Runtime Recompilation**
      
      Perfect for conversational AI, structured output generation, and role-playing scenarios. **Fully recompilable** - modify tools, LLM configs, and behavior patterns at runtime. **Completely serializable** for persistence and transfer between systems.

      +++

      **Dynamic Capabilities:**
      
      * Runtime conversation memory reconfiguration
      * Hot-swap Pydantic models and structured output
      * Dynamic persona and role modification
      * Live agent-as-tool composition changes
      * Real-time temperature and provider switching

   .. grid-item-card:: ReactAgent
      :img-top: _static/react-agent-large.png
      :link: #react-agent
      :link-type: ref
      :class-card: reasoning-card

      **Self-Modifying Reasoning & Acting Agent**
      
      Advanced agents with **dynamic tool integration**, **recompilable reasoning loops**, and **adaptive planning**. Tools, retrieval systems, and reasoning patterns can be **modified at runtime**. Perfect for research tasks that evolve their methodology dynamically.

      +++

      **Runtime Modification Features:**
      
      * Dynamic tool discovery and integration
      * Live reasoning loop reconfiguration
      * Adaptive workflow pattern switching
      * Real-time planning strategy modification
      * Self-optimizing error handling evolution

Coordination Agents
-------------------

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: MultiAgent
      :img-top: _static/multi-agent-large.png
      :link: #multi-agent
      :link-type: ref
      :class-card: coordination-card

      **Fully Serializable Multi-Agent Orchestration System**
      
      Coordinate multiple agents with **runtime reconfigurable workflows**, **dynamic agent addition/removal**, and **live routing adaptation**. Entire coordination graphs can be **serialized, modified, and recompiled** without stopping execution.

      +++

      **Dynamic Orchestration Features:**
      
      * Live workflow reconfiguration (sequential ↔ parallel)
      * Runtime agent spawning and termination
      * Dynamic routing rule modification
      * Real-time state sharing reconfiguration
      * Hot-swap coordination pattern switching

   .. grid-item-card:: DynamicSupervisor
      :img-top: _static/supervisor-large.png
      :link: #dynamic-supervisor
      :link-type: ref
      :class-card: meta-card

      **Self-Modifying Meta-Agent Supervision System**
      
      **Fully serializable supervisors** that can **spawn agents with custom configurations**, **live-modify team structures**, and **dynamically recompile coordination graphs**. Supervision hierarchies can be **serialized and transferred** between systems while maintaining state.

      +++

      **Meta-Level Dynamic Capabilities:**
      
      * Runtime agent architecture modification
      * Live team topology reconfiguration
      * Dynamic supervision hierarchy restructuring
      * Real-time resource allocation adjustment
      * Self-optimizing management pattern evolution

Specialized Agents
------------------

.. grid:: 2 2 3 3
   :gutter: 2

   .. grid-item-card:: 🎭 Conversation Agents
      :link: conversation_orchestration
      :link-type: doc
      :class-card: conversation-card

      **Multi-Agent Dialogue Orchestration**
      
      5 conversation types with sophisticated turn management and social dynamics.

      +++
      
      Round Robin • Directed • Debate • Collaborative • Social Media

   .. grid-item-card:: 🧠 Memory Agents
      :link: memory_systems
      :link-type: doc
      :class-card: memory-card

      **Intelligent Memory Systems**
      
      Graph-based memory with 11 cognitive types and advanced retrieval.

      +++
      
      Neo4j Integration • Vector Search • Temporal Memory

   .. grid-item-card:: 🔄 Self-Modifying Agents
      :link: advanced
      :link-type: doc
      :class-card: adaptive-card

      **Runtime Behavior Adaptation**
      
      Agents that modify their own behavior based on performance feedback.

      +++
      
      Performance Monitoring • Behavior Evolution • Tool Adaptation

   .. grid-item-card:: 🌟 Self-Replicating Agents
      :link: advanced
      :link-type: doc
      :class-card: replication-card

      **Dynamic Agent Cloning**
      
      Create specialized copies with different configurations for parallel tasks.

      +++
      
      Configuration Cloning • Task Specialization • Parallel Processing

   .. grid-item-card:: 🔌 Provider-Switching Agents
      :link: advanced
      :link-type: doc
      :class-card: provider-card

      **Dynamic Provider Management**
      
      Hot-swap between LLM providers based on task complexity and cost.

      +++
      
      OpenAI • Anthropic • Azure • Automatic Optimization

   .. grid-item-card:: 🛠️ Tool Transfer Agents
      :link: advanced
      :link-type: doc
      :class-card: tool-card

      **Capability Sharing System**
      
      Share tools and capabilities between agents for efficient resource use.

      +++
      
      Tool Discovery • Capability Transfer • Resource Optimization

.. _simple-agent:

SimpleAgent
-----------

The foundation agent perfect for basic conversational AI, structured output, and role-playing scenarios.

Core Capabilities
~~~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 💬 Conversation Management
      :class-card: feature-card

      **Persistent Context & Memory**
      
      * Automatic conversation history tracking
      * Context window management
      * Message formatting and templating
      * Multi-turn conversation support

   .. grid-item-card:: 📊 Structured Output
      :class-card: feature-card

      **Pydantic Model Integration**
      
      * Type-safe response generation
      * Automatic validation and parsing
      * Complex data structure support
      * JSON schema compatibility

   .. grid-item-card:: 🎭 Role-Playing & Personas
      :class-card: feature-card

      **Dynamic Character Simulation**
      
      * Character consistency maintenance
      * Personality trait modeling
      * Scenario-based adaptations
      * Emotional state tracking

   .. grid-item-card:: 🔧 Agent-as-Tool Pattern
      :class-card: feature-card

      **Composable Agent Architecture**
      
      * Convert any agent to a tool
      * Nested agent workflows
      * Capability encapsulation
      * Modular design patterns

Usage Examples
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Basic Conversation

      Simple conversational agent with memory::

          from haive.agents.simple import SimpleAgent
          from haive.core.engine.aug_llm import AugLLMConfig

          # Create conversational agent
          agent = SimpleAgent(
              name="assistant",
              engine=AugLLMConfig(
                  temperature=0.7,
                  system_message="You are a helpful AI assistant."
              )
          )

          # Multi-turn conversation
          response1 = await agent.arun("My name is Alice")
          response2 = await agent.arun("What's my name?")
          # Agent remembers: "Your name is Alice"

   .. tab-item:: Structured Output

      Generate structured data with Pydantic models::

          from pydantic import BaseModel, Field
          from typing import List

          class AnalysisResult(BaseModel):
              sentiment: str = Field(description="positive/negative/neutral")
              confidence: float = Field(ge=0.0, le=1.0)
              key_themes: List[str] = Field(description="Main themes")

          # Agent with structured output
          structured_agent = SimpleAgent(
              name="analyzer",
              engine=AugLLMConfig(
                  structured_output_model=AnalysisResult,
                  temperature=0.3
              )
          )

          result = await structured_agent.arun("This product is amazing!")
          print(f"Sentiment: {result.sentiment}")
          print(f"Confidence: {result.confidence}")

   .. tab-item:: Role-Playing

      Create character-based agents::

          # Character agent with consistent personality
          character = SimpleAgent(
              name="detective",
              engine=AugLLMConfig(
                  temperature=0.8,
                  system_message="""
                  You are Detective Sarah Chen, a seasoned investigator with 15 years 
                  experience. You're analytical, methodical, and have a dry sense of humor. 
                  You always look for evidence and ask probing questions.
                  """
              )
          )

          response = await character.arun("There's been a robbery at the bank")
          # Detective persona maintained throughout interaction

.. _react-agent:

ReactAgent
----------

Advanced reasoning agent that follows the ReAct (Reasoning and Acting) pattern for complex problem-solving.

Core Capabilities
~~~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🧠 Iterative Reasoning
      :class-card: feature-card

      **Think-Act-Observe Loop**
      
      * Step-by-step problem breakdown
      * Hypothesis formation and testing
      * Evidence gathering and analysis
      * Conclusion synthesis

   .. grid-item-card:: 🛠️ Tool Integration
      :class-card: feature-card

      **Dynamic Tool Execution**
      
      * Automatic tool selection
      * Parameter inference
      * Error handling and recovery
      * Tool composition patterns

   .. grid-item-card:: 🔍 Research Workflows
      :class-card: feature-card

      **Information Gathering**
      
      * Web search and analysis
      * Document processing
      * Data extraction and synthesis
      * Fact verification

   .. grid-item-card:: 📋 Planning & Decision Making
      :class-card: feature-card

      **Strategic Problem Solving**
      
      * Goal decomposition
      * Action planning
      * Progress monitoring
      * Adaptive strategy adjustment

Usage Examples
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Research Assistant

      Agent with web search and analysis tools::

          from haive.agents.react import ReactAgent
          from langchain_core.tools import tool

          @tool
          def web_search(query: str) -> str:
              """Search the web for information."""
              # Implementation here
              return f"Search results for: {query}"

          @tool
          def calculator(expression: str) -> str:
              """Calculate mathematical expressions."""
              return str(eval(expression))

          # Research agent with tools
          researcher = ReactAgent(
              name="research_assistant",
              engine=AugLLMConfig(tools=[web_search, calculator]),
              max_iterations=5
          )

          result = await researcher.arun(
              "Research the latest AI developments and calculate market growth"
          )

   .. tab-item:: Data Analysis

      Agent for complex data analysis tasks::

          @tool
          def analyze_data(data_path: str) -> str:
              """Analyze data from CSV file."""
              # Implementation here
              return "Analysis complete"

          @tool
          def create_visualization(data: str, chart_type: str) -> str:
              """Create data visualization."""
              # Implementation here
              return f"Created {chart_type} visualization"

          # Data analysis agent
          analyst = ReactAgent(
              name="data_analyst",
              engine=AugLLMConfig(tools=[analyze_data, create_visualization]),
              max_iterations=10
          )

          result = await analyst.arun(
              "Analyze sales data and create trend visualizations"
          )

   .. tab-item:: Problem Solver

      Multi-step problem solving with reasoning::

          @tool
          def get_weather(location: str) -> str:
              """Get current weather for location."""
              return f"Weather in {location}: Sunny, 72°F"

          @tool
          def book_flight(origin: str, destination: str, date: str) -> str:
              """Book a flight."""
              return f"Flight booked from {origin} to {destination} on {date}"

          # Problem solving agent
          planner = ReactAgent(
              name="travel_planner",
              engine=AugLLMConfig(tools=[get_weather, book_flight]),
              max_iterations=7
          )

          result = await planner.arun(
              "Plan a trip to Hawaii next week, considering weather"
          )

.. _multi-agent:

MultiAgent
----------

Sophisticated orchestration system for coordinating multiple agents in complex workflows.

Execution Modes
~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: ➡️ Sequential Execution
      :class-card: mode-card

      **Pipeline Workflows**
      
      * Agent A → Agent B → Agent C
      * State passing between agents
      * Error handling and recovery
      * Progress tracking

   .. grid-item-card:: ⚡ Parallel Execution
      :class-card: mode-card

      **Concurrent Processing**
      
      * Multiple agents run simultaneously
      * Result aggregation
      * Load balancing
      * Timeout management

   .. grid-item-card:: 🌳 Conditional Routing
      :class-card: mode-card

      **Decision Trees**
      
      * Dynamic agent selection
      * State-based routing
      * Conditional logic
      * Fallback strategies

   .. grid-item-card:: 🏗️ Hierarchical Coordination
      :class-card: mode-card

      **Nested Workflows**
      
      * Supervisor-worker patterns
      * Multi-level coordination
      * Resource allocation
      * Priority management

Usage Examples
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Sequential Pipeline

      Content creation pipeline::

          from haive.agents.multi import MultiAgent

          # Create specialized agents
          researcher = ReactAgent(name="researcher", tools=[web_search])
          writer = SimpleAgent(name="writer", engine=AugLLMConfig(temperature=0.8))
          editor = SimpleAgent(name="editor", engine=AugLLMConfig(temperature=0.3))

          # Sequential workflow
          content_pipeline = MultiAgent(
              name="content_creation",
              agents=[researcher, writer, editor],
              execution_mode="sequential"
          )

          result = await content_pipeline.arun(
              "Create a blog post about sustainable energy"
          )

   .. tab-item:: Parallel Processing

      Data analysis with multiple perspectives::

          # Create analysis agents
          technical_analyst = ReactAgent(name="tech_analyst", tools=[data_tools])
          business_analyst = SimpleAgent(name="biz_analyst")
          market_analyst = ReactAgent(name="market_analyst", tools=[market_tools])

          # Parallel analysis
          analysis_team = MultiAgent(
              name="analysis_team",
              agents=[technical_analyst, business_analyst, market_analyst],
              execution_mode="parallel"
          )

          result = await analysis_team.arun(
              "Analyze Q4 performance from multiple perspectives"
          )

   .. tab-item:: Conditional Routing

      Smart routing based on task complexity::

          # Route based on task complexity
          simple_processor = SimpleAgent(name="simple")
          complex_processor = ReactAgent(name="complex", tools=[advanced_tools])

          # Conditional workflow
          smart_router = MultiAgent(
              name="smart_processor",
              agents=[simple_processor, complex_processor],
              execution_mode="conditional"
          )

          # Add routing logic
          smart_router.add_conditional_edge(
              condition=lambda state: state.get("complexity", 0) > 0.7,
              true_agent="complex",
              false_agent="simple"
          )

.. _dynamic-supervisor:

DynamicSupervisor
-----------------

Meta-agent system that can spawn, coordinate, and optimize agent teams dynamically.

Core Capabilities
~~~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🏗️ Dynamic Agent Creation
      :class-card: supervisor-card

      **Runtime Agent Generation**
      
      * Task-based agent creation
      * Automatic configuration
      * Capability matching
      * Resource optimization

   .. grid-item-card:: ⚖️ Team Optimization
      :class-card: supervisor-card

      **Performance Management**
      
      * Load balancing
      * Resource allocation
      * Performance monitoring
      * Bottleneck identification

   .. grid-item-card:: 📊 Monitoring & Analytics
      :class-card: supervisor-card

      **System Insights**
      
      * Real-time metrics
      * Performance tracking
      * Resource utilization
      * Failure analysis

   .. grid-item-card:: 🎯 Hierarchical Control
      :class-card: supervisor-card

      **Multi-Level Management**
      
      * Supervisor hierarchies
      * Delegation strategies
      * Escalation handling
      * Authority management

Usage Examples
~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Auto Team Building

      Supervisor that builds teams for complex tasks::

          from haive.agents.agent import DynamicSupervisorAgent

          # Create adaptive supervisor
          supervisor = DynamicSupervisorAgent(
              name="project_manager",
              engine=AugLLMConfig(),
              enable_agent_builder=True
          )

          # Supervisor analyzes task and creates appropriate team
          result = await supervisor.arun(
              "Develop a mobile app with user authentication and data visualization"
          )
          # Creates: BackendAgent, FrontendAgent, SecurityAgent, UIAgent

   .. tab-item:: Performance Optimization

      Supervisor that optimizes team performance::

          class OptimizingSupervisor(DynamicSupervisorAgent):
              async def optimize_team(self):
                  # Monitor performance
                  metrics = await self.get_team_metrics()
                  
                  # Identify bottlenecks
                  if metrics.response_time > threshold:
                      await self.add_parallel_agents()
                  
                  # Balance workload
                  if metrics.load_imbalance > 0.3:
                      await self.redistribute_tasks()

   .. tab-item:: Hierarchical System

      Multi-level supervision with delegation::

          # Create hierarchical system
          cto = DynamicSupervisorAgent(name="CTO")
          
          # Create department supervisors
          backend_lead = DynamicSupervisorAgent(name="backend_lead")
          frontend_lead = DynamicSupervisorAgent(name="frontend_lead")
          
          # Delegate to department leads
          cto.add_subordinate(backend_lead)
          cto.add_subordinate(frontend_lead)
          
          # Complex project delegation
          result = await cto.arun("Build enterprise SaaS platform")

Runtime Reconfiguration Examples
----------------------------------

**🔄 Dynamic Agent Evolution in Action:**

Watch agents transform themselves at runtime:

.. code-block:: python

   # 🚀 START WITH SIMPLE AGENT
   agent = SimpleAgent(name="basic_bot", engine=AugLLMConfig())
   
   # 📈 DYNAMICALLY EVOLVE TO RESEARCH AGENT
   await agent.live_reconfigure({
       "agent_type": "ReactAgent",           # Change agent class
       "tools": [web_search, calculator],    # Add tools
       "max_iterations": 5,                  # Add reasoning capability
       "preserve_conversation_history": True  # Keep existing context
   })
   
   # 🧠 ADD MEMORY SYSTEM WITHOUT RESTART
   await agent.add_memory_system({
       "type": "integrated",  # Graph + Vector + Temporal
       "neo4j_config": neo4j_config,
       "migrate_conversation_to_memory": True
   })
   
   # 🎯 SERIALIZE ENTIRE AGENT STATE
   agent_snapshot = await agent.serialize_complete_state()
   
   # 🔄 SPAWN SPECIALIZED COPIES
   analyst = await agent.replicate_as({
       "name": "market_analyst",
       "tools": [market_data_tool, analysis_tool],
       "system_message": "You are a market analysis expert",
       "memory_focus": ["ANALYTICAL", "PROFESSIONAL"]
   })

**⚡ Hot-Swap LLM Providers:**

Switch providers based on task complexity:

.. code-block:: python

   # 💰 START WITH COST-EFFECTIVE PROVIDER
   agent = ReactAgent(
       name="adaptive_agent",
       engine=AugLLMConfig(provider="openai", model="gpt-3.5-turbo")
   )
   
   # 🧠 DYNAMICALLY UPGRADE FOR COMPLEX TASK
   if task_complexity > 0.8:
       await agent.hot_swap_provider({
           "provider": "anthropic",
           "model": "claude-3-opus",
           "preserve_conversation": True,
           "migrate_tools": True
       })
   
   # 📊 AUTO-OPTIMIZE BASED ON PERFORMANCE
   await agent.enable_auto_provider_optimization({
       "performance_threshold": 0.85,
       "cost_efficiency_weight": 0.3,
       "response_quality_weight": 0.7
   })

**🌐 Live Multi-Agent Network Reconfiguration:**

Modify agent networks and coordination patterns:

.. code-block:: python

   # 🏗️ DYNAMIC TEAM RESTRUCTURING
   team = MultiAgent(
       name="adaptive_team",
       agents=[researcher, analyst, writer],
       execution_mode="sequential"
   )
   
   # ⚡ LIVE WORKFLOW RECONFIGURATION
   await team.reconfigure_workflow({
       "execution_mode": "parallel",          # Change from sequential
       "add_agents": [reviewer, validator],   # Add new team members
       "routing_strategy": "conditional",     # Add smart routing
       "preserve_agent_states": True         # Keep individual progress
   })
   
   # 📡 SERIALIZE ENTIRE TEAM CONFIGURATION
   team_blueprint = await team.serialize_team_structure()
   
   # 🔄 REPLICATE TEAM WITH MODIFICATIONS
   specialized_team = await MultiAgent.from_blueprint(
       team_blueprint,
       modifications={
           "domain_focus": "financial_analysis",
           "agent_specializations": {
               "researcher": "financial_data_specialist",
               "analyst": "quantitative_analyst"
           }
       }
   )

Agent Composition Patterns
---------------------------

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🔧 Agent-as-Tool
      :class-card: pattern-card

      **Tool Encapsulation**
      
      Convert any agent into a tool for use by other agents, enabling modular composition and reusability.

   .. grid-item-card:: 🎭 Role Specialization
      :class-card: pattern-card

      **Expert Systems**
      
      Create specialized agents for specific domains, then coordinate them for comprehensive solutions.

   .. grid-item-card:: 🔄 State Sharing
      :class-card: pattern-card

      **Context Preservation**
      
      Share state and context between agents for consistent, coherent multi-agent interactions.

   .. grid-item-card:: 🌊 Workflow Orchestration
      :class-card: pattern-card

      **Process Automation**
      
      Design complex workflows with conditional logic, error handling, and adaptive routing.

Best Practices
--------------

Agent Selection Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :class: agent-selection-table

   * - Use Case
     - Recommended Agent
     - Key Features
     - Example Scenarios

   * - Simple Q&A
     - SimpleAgent
     - Conversation memory, structured output
     - Chatbots, customer service, role-playing

   * - Research & Analysis  
     - ReactAgent
     - Tool integration, reasoning loops
     - Data analysis, web research, planning

   * - Multi-step Workflows
     - MultiAgent
     - Agent coordination, state management
     - Content pipelines, analysis workflows

   * - Dynamic Teams
     - DynamicSupervisor
     - Agent creation, team optimization
     - Complex projects, adaptive systems

   * - Conversations
     - ConversationAgents
     - Turn management, social dynamics
     - Debates, brainstorming, collaboration

   * - Memory & Context
     - MemoryAgents
     - Graph-based memory, classification
     - Learning systems, context-aware AI

Performance Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: ⚡ Startup Time
      :text-align: center
      :class-card: performance-card

      **SimpleAgent**: <100ms
      **ReactAgent**: <200ms  
      **MultiAgent**: <300ms
      **DynamicSupervisor**: <500ms

   .. grid-item-card:: 🔄 Response Time
      :text-align: center
      :class-card: performance-card

      **Simple queries**: <2s
      **Tool execution**: <5s
      **Multi-agent**: <10s
      **Complex workflows**: <30s

   .. grid-item-card:: 📊 Scalability
      :text-align: center
      :class-card: performance-card

      **Concurrent agents**: 50+
      **Conversations**: 10+
      **Supervisors**: 5 levels
      **Memory agents**: 1000+ memories

Next Steps
----------

- :doc:`quickstart` - Get started with your first agent
- :doc:`memory_systems` - Add intelligent memory to your agents  
- :doc:`conversation_orchestration` - Create multi-agent conversations
- :doc:`advanced` - Explore self-modification and replication
- :doc:`examples` - See complete working examples