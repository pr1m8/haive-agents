agents
======

.. py:module:: agents

.. autoapi-nested-parse::

   Haive Agents Module - Main exports.

   This module provides various agent implementations for the Haive framework,
   including base agents, multi-agents, reactive agents, and specialized agents
   for different use cases like RAG, planning, memory, and reasoning.

   Key Components:
       - Base: Core agent abstractions and foundational classes
       - Simple: Basic agent implementations for common use cases
       - React: Reactive agents with reasoning loops and tool usage
       - Multi: Multi-agent coordination and orchestration
       - RAG: Retrieval-Augmented Generation agents
       - Planning: Planning and execution agents
       - Memory: Memory-enabled agents with long-term context
       - Conversation: Conversational agent patterns
       - Supervisor: Agent supervision and coordination patterns

   The agents are designed to be modular, extensible, and optimized for
   various AI workflows and use cases within the Haive ecosystem.

   .. rubric:: Examples

   Basic agent usage::

       from haive.agents import SimpleAgent
       from haive.core.engine.aug_llm import AugLLMConfig

       agent = SimpleAgent(
           name="helper",
           engine=AugLLMConfig(model="gpt-4")
       )
       result = agent.run("Hello world")

   Multi-agent coordination::

       from haive.agents import MultiAgent, SimpleAgent, ReactAgent

       coordinator = MultiAgent([
           SimpleAgent(name="planner"),
           ReactAgent(name="executor", tools=[...])
       ], mode="sequential")

   RAG agent setup::

       from haive.agents.rag import BaseRAGAgent
       from haive.core.models import VectorStoreConfig

       rag_agent = BaseRAGAgent(
           vectorstore_config=VectorStoreConfig(...)
       )


   .. autolink-examples:: agents
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/agent/index
   /autoapi/agents/base/index
   /autoapi/agents/chain/index
   /autoapi/agents/chain_agent/index
   /autoapi/agents/config/index
   /autoapi/agents/conversation/index
   /autoapi/agents/discovery/index
   /autoapi/agents/document/index
   /autoapi/agents/document_loader/index
   /autoapi/agents/document_modifiers/index
   /autoapi/agents/document_processing/index
   /autoapi/agents/dynamic_supervisor/index
   /autoapi/agents/experiments/index
   /autoapi/agents/factory/index
   /autoapi/agents/long_term_memory/index
   /autoapi/agents/ltm/index
   /autoapi/agents/memory/index
   /autoapi/agents/memory_reorganized/index
   /autoapi/agents/memory_v2/index
   /autoapi/agents/models/index
   /autoapi/agents/multi/index
   /autoapi/agents/patterns/index
   /autoapi/agents/planning/index
   /autoapi/agents/planning_v2/index
   /autoapi/agents/qa_agent/index
   /autoapi/agents/rag/index
   /autoapi/agents/react/index
   /autoapi/agents/react_class/index
   /autoapi/agents/reasoning_and_critique/index
   /autoapi/agents/reflection/index
   /autoapi/agents/research/index
   /autoapi/agents/routing_agent/index
   /autoapi/agents/self_healing_code/index
   /autoapi/agents/sequential/index
   /autoapi/agents/simple/index
   /autoapi/agents/state/index
   /autoapi/agents/state_wrapper/index
   /autoapi/agents/structured/index
   /autoapi/agents/structured_output/index
   /autoapi/agents/supervisor/index
   /autoapi/agents/task_analysis/index
   /autoapi/agents/tool_utils/index
   /autoapi/agents/tools/index
   /autoapi/agents/utils/index
   /autoapi/agents/wiki_writer/index


