agents.memory_v2
================

.. py:module:: agents.memory_v2

.. autoapi-nested-parse::

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


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/memory_v2/advanced_rag_memory_agent/index
   /autoapi/agents/memory_v2/conversation_memory_agent/index
   /autoapi/agents/memory_v2/extraction_prompts/index
   /autoapi/agents/memory_v2/graph_memory_agent/index
   /autoapi/agents/memory_v2/integrated_memory_system/index
   /autoapi/agents/memory_v2/kg_memory_agent/index
   /autoapi/agents/memory_v2/long_term_memory_agent/index
   /autoapi/agents/memory_v2/memory_models_standalone/index
   /autoapi/agents/memory_v2/memory_state/index
   /autoapi/agents/memory_v2/memory_state_original/index
   /autoapi/agents/memory_v2/memory_state_with_tokens/index
   /autoapi/agents/memory_v2/memory_tools/index
   /autoapi/agents/memory_v2/message_document_converter/index
   /autoapi/agents/memory_v2/multi_memory_agent/index
   /autoapi/agents/memory_v2/multi_memory_coordinator/index
   /autoapi/agents/memory_v2/multi_react_memory_system/index
   /autoapi/agents/memory_v2/rag_memory_agent/index
   /autoapi/agents/memory_v2/react_memory_agent/index
   /autoapi/agents/memory_v2/react_memory_coordinator/index
   /autoapi/agents/memory_v2/simple_memory_agent/index
   /autoapi/agents/memory_v2/simple_memory_agent_deepseek/index
   /autoapi/agents/memory_v2/standalone_memory_agent_free/index
   /autoapi/agents/memory_v2/standalone_rag_memory/index
   /autoapi/agents/memory_v2/time_weighted_retriever/index
   /autoapi/agents/memory_v2/token_tracker/index


