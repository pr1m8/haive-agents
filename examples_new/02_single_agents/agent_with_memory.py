#!/usr/bin/env python3
"""Agent with Memory Example - Intermediate Level

This example demonstrates how to use conversation memory with agents,
showing both in-memory and persistent memory patterns. Memory allows
agents to maintain context across multiple interactions.

Key concepts covered:
- ConversationBufferMemory for chat history
- ConversationSummaryMemory for long conversations
- Memory persistence to disk
- Memory window management
- Contextual responses based on history"""

import asyncio
import json
from datetime import datetime
from pathlib import Path

from haive.core.engine.aug_llm import AugLLMConfig
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

from haive.agents.simple.agent_v3 import SimpleAgentV3


class MemoryPersistenceManager:
    """Helper class to manage memory persistence."""

    def __init__(self, storage_dir: str = "./agent_memories"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(exist_ok=True)

    def save_memory(self, agent_name: str, messages: list[dict[str, str]]) -> str:
        """Save memory to disk."""
        filepath = self.storage_dir / f"{agent_name}_memory.json"

        memory_data = {
            "agent_name": agent_name,
            "saved_at": datetime.now().isoformat(),
            "messages": messages,
            "message_count": len(messages),
        }

        with open(filepath, "w") as f:
            json.dump(memory_data, f, indent=2)

        return str(filepath)

    def load_memory(self, agent_name: str) -> list[dict[str, str]]:
        """Load memory from disk."""
        filepath = self.storage_dir / f"{agent_name}_memory.json"

        if not filepath.exists():
            return []

        with open(filepath) as f:
            data = json.load(f)

        return data.get("messages", [])


async def main():
    """Demonstrate agents with different memory patterns."""
    print("=" * 60)
    print("Agent with Memory Example")
    print("=" * 60)

    # Initialize memory manager
    memory_manager = MemoryPersistenceManager()

    # Example 1: Basic conversation memory
    print("\n1. Agent with Conversation Memory")
    print("-" * 40)

    # Create memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Create agent with memory
    chat_agent = SimpleAgentV3(
        name="personal_assistant",
        engine=AugLLMConfig(
            temperature=0.7,
            system_message="You are a helpful personal assistant. Remember details about the user and refer back to previous conversations.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                ("placeholder", "{chat_history}"),
                ("human", "{query}"),
            ]
        ),
    )

    # Simulate conversation
    conversations = [
        "Hi! My name is Alice and I'm learning Python.",
        "What's my name?",
        "What am I learning?",
        "Can you give me a Python tip based on what you know about me?",
    ]

    for _i, query in enumerate(conversations, 1):
        print(f"\n🗣️  User: {query}")

        # Prepare input with memory
        inputs = {"query": query, "chat_history": memory.chat_memory.messages}

        # Get response
        response = await chat_agent.arun(inputs)
        print(f"🤖 Assistant: {response}")

        # Update memory
        memory.chat_memory.add_user_message(query)
        memory.chat_memory.add_ai_message(response)

    # Show memory contents
    print("\n📊 Memory Statistics:")
    print(f"   Total messages: {len(memory.chat_memory.messages)}")
    print(
        f"   User messages: {len([m for m in memory.chat_memory.messages if isinstance(m, HumanMessage)])}"
    )
    print(
        f"   AI messages: {len([m for m in memory.chat_memory.messages if isinstance(m, AIMessage)])}"
    )

    # Example 2: Memory with persistence
    print("\n\n2. Persistent Memory Across Sessions")
    print("-" * 40)

    # Save current memory
    messages_to_save = [
        {
            "role": "human" if isinstance(m, HumanMessage) else "assistant",
            "content": m.content,
        }
        for m in memory.chat_memory.messages
    ]

    saved_path = memory_manager.save_memory("personal_assistant", messages_to_save)
    print(f"💾 Memory saved to: {saved_path}")

    # Simulate new session - load memory
    print("\n🔄 Starting new session...")

    loaded_messages = memory_manager.load_memory("personal_assistant")
    print(f"📂 Loaded {len(loaded_messages)} messages from previous session")

    # Create new agent with loaded memory
    new_memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True
    )

    # Restore messages
    for msg in loaded_messages:
        if msg["role"] == "human":
            new_memory.chat_memory.add_user_message(msg["content"])
        else:
            new_memory.chat_memory.add_ai_message(msg["content"])

    # Continue conversation
    query = "Do you remember who I am and what I'm studying?"
    print(f"\n🗣️  User: {query}")

    response = await chat_agent.arun(
        {"query": query, "chat_history": new_memory.chat_memory.messages}
    )
    print(f"🤖 Assistant: {response}")

    # Example 3: Memory window management
    print("\n\n3. Memory Window Management")
    print("-" * 40)

    # Create agent with limited memory window
    windowed_agent = SimpleAgentV3(
        name="windowed_assistant",
        engine=AugLLMConfig(
            temperature=0.7,
            system_message="You are an assistant with limited memory. Focus on recent context.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                ("placeholder", "{recent_history}"),
                ("human", "{query}"),
            ]
        ),
    )

    # Simulate long conversation
    long_conversation = [
        "Let's talk about machine learning",
        "What are neural networks?",
        "How do transformers work?",
        "What about attention mechanisms?",
        "Can you explain BERT?",
        "Now let's switch topics to cooking",
        "What's a good pasta recipe?",
        "How do I make tomato sauce?",
    ]

    full_memory = ConversationBufferMemory(return_messages=True)
    window_size = 4  # Only keep last 4 messages (2 exchanges)

    for query in long_conversation:
        print(f"\n🗣️  User: {query}")

        # Get recent history (sliding window)
        all_messages = full_memory.chat_memory.messages
        recent_messages = (
            all_messages[-window_size:]
            if len(all_messages) > window_size
            else all_messages
        )

        response = await windowed_agent.arun(
            {"query": query, "recent_history": recent_messages}
        )
        print(f"🤖 Assistant: {response[:150]}...")  # Truncate for readability

        # Update full memory
        full_memory.chat_memory.add_user_message(query)
        full_memory.chat_memory.add_ai_message(response)

    print("\n📊 Memory Window Stats:")
    print(f"   Total messages: {len(full_memory.chat_memory.messages)}")
    print(f"   Window size: {window_size}")
    print(
        f"   Messages in context: {min(window_size, len(full_memory.chat_memory.messages))}"
    )

    # Example 4: Summary memory for long conversations
    print("\n\n4. Summary Memory for Long Conversations")
    print("-" * 40)

    # Create summarizing agent
    summary_agent = SimpleAgentV3(
        name="summarizer",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are a conversation summarizer. Create concise summaries.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    "Summarize this conversation in 2-3 sentences:\n\n{conversation}",
                ),
            ]
        ),
    )

    # Get conversation text
    conversation_text = "\n".join(
        [
            f"{'User' if isinstance(m, HumanMessage) else 'Assistant'}: {m.content}"
            for m in full_memory.chat_memory.messages[:6]  # First 6 messages
        ]
    )

    summary = await summary_agent.arun({"conversation": conversation_text})

    print(f"📝 Conversation Summary:\n{summary}")

    # Example 5: Contextual memory search
    print("\n\n5. Contextual Memory Search")
    print("-" * 40)

    def search_memory(memory: ConversationBufferMemory, keyword: str) -> list[str]:
        """Search memory for messages containing keyword."""
        results = []
        for msg in memory.chat_memory.messages:
            if keyword.lower() in msg.content.lower():
                role = "User" if isinstance(msg, HumanMessage) else "Assistant"
                results.append(f"{role}: {msg.content[:100]}...")
        return results

    # Search for specific topics
    search_terms = ["learning", "Python", "neural"]

    for term in search_terms:
        results = search_memory(new_memory, term)
        print(f"\n🔍 Search results for '{term}': {len(results)} found")
        for result in results[:2]:  # Show first 2 results
            print(f"   - {result}")

    # Clean up
    print("\n\n🧹 Cleanup")
    print("-" * 40)
    print(f"Memory files saved in: {memory_manager.storage_dir}")
    print("Memory demonstration complete!")


if __name__ == "__main__":
    asyncio.run(main())
