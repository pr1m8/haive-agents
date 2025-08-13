
:py:mod:`agents.memory_v2`
==========================

.. py:module:: agents.memory_v2

Memory V2 System - BaseRAGAgent-based Memory Architecture.

This package provides memory-capable agents built on BaseRAGAgent as requested:

**Working Components (BaseRAGAgent-based):**
- UnifiedMemoryRAGAgent: Complete memory system using BaseRAGAgent
- ConversationMemoryAgent: Conversation history with BaseRAGAgent
- FactualMemoryAgent: Factual storage with BaseRAGAgent
- PreferencesMemoryAgent: User preferences with SimpleRAGAgent
- StandaloneMemoryItem: Memory model without broken dependencies

**Key Features:**
- Real BaseRAGAgent integration with vector stores
- Time-weighted retrieval for temporal queries
- Multi-modal memory storage (conversation, facts, preferences)
- Agent-as-tool pattern support
- No mocks - all real components

**Quick Start:**

    from haive.agents.memory_v2 import create_unified_memory_agent
    from langchain_core.messages import HumanMessage

    # Create unified memory agent using BaseRAGAgent
    agent = create_unified_memory_agent(user_id="user123")
    await agent.initialize()

    # Process conversation and extract memories
    messages = [HumanMessage("I work at Google as a software engineer")]
    result = await agent.process_conversation(messages)

    # Retrieve context
    context = await agent.retrieve_context("Where do I work?")

**Agent-as-Tool Pattern:**

    # Use memory as a tool in other agents
    memory_tool = UnifiedMemoryRAGAgent.as_tool(
        name="user_memory",
        description="Search user memory"
    )

    # Use in ReactAgent or other agents
    coordinator = ReactAgent(tools=[memory_tool])


.. autolink-examples:: agents.memory_v2
   :collapse:




