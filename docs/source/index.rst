Haive Agents Documentation
==========================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:

   getting_started
   agent_types
   memory_systems
   dynamic_supervisor
   conversation_orchestration
   quickstart
   user_guide
   examples
   api_reference
   advanced
   troubleshooting
   changelog

Welcome to Haive Agents
-----------------------

Haive Agents provides **truly dynamic, recompilable, and fully serializable agents** capable of real-time self-modification, dynamic replication, and autonomous coordination. This is not just another agent framework - it's a revolutionary system where agents can **dynamically modify their tools**, **hot-swap LLM providers**, **reconfigure retrieval systems**, **modify graph structures**, and **adapt their entire behavior stack** without restarts or predefined configuration.

🚀 **The Game Changer**: Your agents are **living, adaptable entities** that can **recompile themselves**, **serialize their entire state**, and **modify every component** - from tools to LLMs to retrievers to other agents and graphs - **at runtime**!

Runtime Recompilation & Serialization at its Core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Imagine agents that are **living, adaptable systems** capable of:

* **Dynamic Tool Modification** - Add, remove, or reconfigure tools without restarts
* **LLM Provider Hot-Swapping** - Switch between OpenAI, Anthropic, Azure in real-time
* **Retrieval System Reconfiguration** - Modify vector stores, graph schemas, embedding models live
* **Agent Network Restructuring** - Dynamically modify connections to other agents
* **Graph Structure Adaptation** - Recompile execution graphs and state flows at runtime
* **Complete State Serialization** - Serialize entire agent state for transfer/persistence
* **Memory System Live Migration** - Move memory systems between backends without data loss
* **Self-Modifying Behavior** - Agents modify their own code and configuration based on performance

**Revolutionary Example**: Start with a simple chatbot, ask it to "become a research team that analyzes market trends" - it will **dynamically spawn specialized agents**, **reconfigure its memory system for market data**, **modify its retrieval patterns**, and **serialize the entire configuration** for future use - all without stopping execution! See :doc:`dynamic_supervisor` for complete orchestration capabilities.

Key Innovations
~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🧠 Advanced Memory Systems
      :link: memory_systems
      :link-type: doc

      Graph-based memory with Neo4j integration, 11 cognitive memory types, and intelligent retrieval systems for context-aware interactions.

   .. grid-item-card:: 🔄 Self-Modifying Agents
      :link: advanced
      :link-type: doc

      Agents that can modify their own behavior, tools, and configurations based on performance and task requirements.

   .. grid-item-card:: 🌟 Dynamic Replication
      :link: advanced
      :link-type: doc

      Create specialized copies of agents with different configurations for parallel processing and task specialization.

   .. grid-item-card:: 🎭 Conversation Orchestration
      :link: conversation_orchestration
      :link-type: doc

      5 conversation types: Round Robin, Directed, Debate, Collaborative, and Social Media with viral dynamics and engagement mechanics.

Core Agent Types
~~~~~~~~~~~~~~~~

.. grid:: 2 2 3 3
   :gutter: 2

   .. grid-item-card:: SimpleAgent
      :img-top: _static/simple-agent-icon.png
      :link: agent_types
      :link-type: doc

      **Foundation Agent**
      
      Perfect for basic conversations, structured output, and role-playing scenarios.
      
      +++
      
      Features: Conversation memory, Pydantic models, Agent-as-tool pattern

   .. grid-item-card:: ReactAgent  
      :img-top: _static/react-agent-icon.png
      :link: agent_types
      :link-type: doc

      **Reasoning & Acting**
      
      Advanced agents with tool integration, reasoning loops, and planning capabilities.
      
      +++
      
      Features: Tool execution, Research workflows, Hierarchical reasoning

   .. grid-item-card:: MultiAgent
      :img-top: _static/multi-agent-icon.png
      :link: agent_types
      :link-type: doc

      **Coordination System**
      
      Orchestrate multiple agents in sequential, parallel, or conditional workflows. See :doc:`dynamic_supervisor` for advanced orchestration.
      
      +++
      
      Features: Workflow orchestration, State management, Dynamic routing

   .. grid-item-card:: ConversationAgents
      :img-top: _static/conversation-icon.png
      :link: conversation_orchestration
      :link-type: doc

      **Dialogue Orchestration**
      
      Multi-agent conversations with structured interactions and social dynamics. Advanced patterns in :doc:`conversation_orchestration`.
      
      +++
      
      Features: 5 conversation types, Turn management, Engagement metrics

   .. grid-item-card:: MemoryAgents
      :img-top: _static/memory-icon.png
      :link: memory_systems
      :link-type: doc

      **Intelligent Memory**
      
      Graph-based memory with classification, consolidation, and retrieval systems.
      
      +++
      
      Features: Neo4j integration, 11 memory types, Multi-modal retrieval

   .. grid-item-card:: DynamicSupervisor
      :img-top: _static/supervisor-icon.png
      :link: dynamic_supervisor
      :link-type: doc

      **Runtime-Recompilable Orchestration**
      
      Fully serializable supervisors with registry-based agent discovery and performance-driven evolution.
      
      +++
      
      Features: Agent registry, State serialization, Hot-swap coordination

Advanced Capabilities
~~~~~~~~~~~~~~~~~~~~~

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: 🔧 Self-Modification & Replication
      :link: advanced
      :link-type: doc

      Create agents that evolve their behavior based on performance feedback and replicate themselves with specialized configurations. See :doc:`dynamic_supervisor` for orchestration patterns.

   .. grid-item-card:: 🧠 Graph-Based Memory Systems
      :link: memory_systems
      :link-type: doc

      Comprehensive memory architecture with Neo4j graph database, 11 cognitive memory types, and intelligent consolidation mechanisms.

   .. grid-item-card:: 🎭 Conversation Orchestration
      :link: conversation_orchestration
      :link-type: doc

      5 sophisticated conversation types with turn management, social dynamics, viral mechanics, and engagement tracking. Extends :doc:`agent_types` MultiAgent patterns.

   .. grid-item-card:: 🔄 Provider Hot-Swapping
      :link: advanced
      :link-type: doc

      Dynamically switch between LLM providers (OpenAI, Anthropic, Azure) based on task complexity and performance requirements.

Quick Example: Dynamic Agent Evolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Watch as agents automatically adapt and coordinate::

    from haive.agents.simple import SimpleAgent
    from haive.agents.react import ReactAgent
    from haive.agents.multi import MultiAgent
    from haive.core.engine.aug_llm import AugLLMConfig

    # Create a self-organizing team with MultiAgent coordination
    coordinator = MultiAgent(
        name="adaptive_team",
        agents=[
            SimpleAgent(name="researcher", engine=AugLLMConfig()),
            ReactAgent(name="analyst", tools=[calculator, web_search]),
            SimpleAgent(name="writer", engine=AugLLMConfig(temperature=0.8))
        ],
        execution_mode="sequential"
    )

    # The team automatically adapts to complex requests
    result = await coordinator.arun(
        "Research AI trends, analyze market impact, and create a presentation"
    )

    # Each agent specialized automatically:
    # - Researcher: Gathered comprehensive data
    # - Analyst: Performed quantitative analysis  
    # - Writer: Created engaging presentation content
    
    # For dynamic agent creation and advanced orchestration, see DynamicSupervisor!

Memory-Enhanced Intelligence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Agents with persistent, intelligent memory::

    from haive.agents.memory_reorganized import SimpleMemoryAgent
    from haive.agents.memory_reorganized.coordination import IntegratedMemorySystem

    # Create memory-enhanced agent
    memory_agent = SimpleMemoryAgent(
        name="assistant",
        memory_config={
            "enable_classification": True,
            "store_type": "integrated",  # Graph + Vector + Time
            "consolidation_enabled": True
        }
    )

    # Store experiences with automatic processing
    await memory_agent.store_memory("I learned Python at university in 2020")
    # → Classified as EPISODIC + EDUCATION
    # → Entities: ["Python", "university", "2020"] 
    # → Graph relationships created

    # Intelligent retrieval with multi-factor scoring
    results = await memory_agent.retrieve_memories("programming experience")
    # → Combines similarity + graph + recency + importance

Orchestration Capabilities Progression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**From Basic to Advanced Agent Coordination:**

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: 1. MultiAgent Coordination
      :link: agent_types
      :link-type: doc
      :text-align: center

      **Sequential, Parallel & Conditional**
      
      Orchestrate predefined agents in structured workflows with state management and dynamic routing.

   .. grid-item-card:: 2. Conversation Orchestration  
      :link: conversation_orchestration
      :link-type: doc
      :text-align: center

      **Interactive Dialogues**
      
      5 conversation types with turn management, social dynamics, and engagement tracking for multi-agent interactions.

   .. grid-item-card:: 3. Dynamic Supervision
      :link: dynamic_supervisor
      :link-type: doc
      :text-align: center

      **Runtime Agent Creation**
      
      Fully serializable supervisors that discover, create, and optimize agent teams dynamically with registry management.

**When to Use Each:**

* **MultiAgent**: Known agents, structured workflows, predictable patterns
* **ConversationAgents**: Interactive dialogues, social dynamics, turn-based coordination  
* **DynamicSupervisor**: Unknown requirements, adaptive teams, performance optimization

Getting Started Paths
~~~~~~~~~~~~~~~~~~~~~

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: 🚀 Quick Start
      :link: quickstart
      :link-type: doc
      :text-align: center

      Jump right in with working examples and common patterns. Perfect for getting your first agent running in minutes.

   .. grid-item-card:: 📚 Comprehensive Guide  
      :link: user_guide
      :link-type: doc
      :text-align: center

      Deep dive into all capabilities, patterns, and advanced features. Complete learning path from basics to mastery.

   .. grid-item-card:: 💡 Example Gallery
      :link: examples
      :link-type: doc
      :text-align: center

      Explore real-world implementations including self-organizing teams, memory systems, and conversation orchestration.

   .. grid-item-card:: 🔧 API Reference
      :link: api_reference
      :link-type: doc
      :text-align: center

      Complete technical documentation with class references, method signatures, and implementation details.

Dynamic Memory Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: 📊 Graph Memory
      :text-align: center

      Neo4j-powered knowledge graphs with entity relationships and semantic connections.

   .. grid-item-card:: 🔍 Vector Memory  
      :text-align: center

      High-performance semantic search with Chroma and FAISS vector stores.

   .. grid-item-card:: ⏰ Temporal Memory
      :text-align: center

      Time-aware memory with recency weighting and consolidation mechanisms.

Performance Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Startup Time**: <100ms for basic agents, <500ms for memory-enhanced agents
* **Memory Retrieval**: <10ms for quick search, 100-500ms for deep graph traversal  
* **Conversation Flow**: <1s response time for multi-agent orchestration
* **Scalability**: 10+ concurrent conversations, 100+ agents per supervisor

Next Steps
~~~~~~~~~~

- :doc:`getting_started` - Understand core concepts and architecture
- :doc:`quickstart` - Create your first dynamic agent  
- :doc:`agent_types` - Explore different agent capabilities including MultiAgent coordination
- :doc:`conversation_orchestration` - Master multi-agent dialogues and social dynamics
- :doc:`dynamic_supervisor` - Advanced orchestration with registry-based agent creation
- :doc:`memory_systems` - Learn about intelligent memory systems
- :doc:`examples` - See real-world implementations

Getting Help
~~~~~~~~~~~~

* **Documentation**: You're reading it!
* **GitHub Issues**: https://github.com/haive-ai/haive/issues
* **Examples**: See the ``examples/`` directory in each agent type
* **Community**: Join our Discord server

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`