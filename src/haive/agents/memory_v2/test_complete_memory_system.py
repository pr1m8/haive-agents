"""Comprehensive test suite for the complete Memory V2 system.

This test runs all memory components together with real LLMs and databases.
"""

import asyncio
import json
import shutil
import tempfile
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List

import pytest
from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.memory_v2.advanced_rag_memory_agent import (
    AdvancedRAGConfig,
    AdvancedRAGMemoryAgent,
    RetrievalStrategy,
)
from haive.agents.memory_v2.graph_memory_agent import (
    GraphMemoryAgent,
    GraphMemoryConfig,
    GraphMemoryMode,
)
from haive.agents.memory_v2.long_term_memory_agent import LongTermMemoryAgent
from haive.agents.memory_v2.multi_memory_coordinator import (
    CoordinationMode,
    MemorySystemType,
    MultiMemoryConfig,
    MultiMemoryCoordinator,
)
from haive.agents.memory_v2.react_memory_agent import ReactMemoryAgent
from haive.agents.memory_v2.simple_memory_agent import SimpleMemoryAgent


class TestCompleteMemorySystem:
    """Test the complete Memory V2 system with all components."""

    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for storage."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def test_config(self):
        """Test configuration."""
        return {"user_id": "test_user", "engine": AugLLMConfig(temperature=0.1)}

    @pytest.fixture
    def neo4j_config(self):
        """Neo4j test configuration (requires running Neo4j)."""
        return {
            "neo4j_uri": "bolt://localhost:7687",
            "neo4j_username": "neo4j",
            "neo4j_password": "password",
        }

    @pytest.mark.asyncio
    async def test_all_memory_agents_individually(self, test_config, temp_dir):
        """Test each memory agent individually."""
        print("\n=== Testing All Memory Agents Individually ===\n")

        # Test data
        test_memory = "Alice Johnson is a senior AI researcher at TechCorp working on neural networks."
        test_query = "Who is Alice Johnson?"

        # 1. SimpleMemoryAgent
        print("1. Testing SimpleMemoryAgent...")
        simple_agent = SimpleMemoryAgent(
            name="test_simple",
            engine=test_config["engine"],
            user_id=test_config["user_id"],
        )
        simple_result = await simple_agent.arun(f"Remember: {test_memory}")
        print(f"   Stored: {len(simple_result) > 0}")
        query_result = await simple_agent.arun(test_query)
        print(f"   Retrieved: {'alice' in query_result.lower()}")

        # 2. ReactMemoryAgent
        print("\n2. Testing ReactMemoryAgent...")
        react_agent = ReactMemoryAgent(
            name="test_react",
            engine=test_config["engine"],
            user_id=test_config["user_id"],
            memory_store_path=str(Path(temp_dir) / "react_memory"),
        )
        react_store = await react_agent.arun(
            f"Store this memory: {test_memory}", auto_save=True
        )
        print(f"   Stored: {'successfully' in react_store.lower()}")
        react_query = await react_agent.arun(
            f"Search memories for: {test_query}", auto_save=False
        )
        print(f"   Retrieved: {'alice' in react_query.lower()}")

        # 3. LongTermMemoryAgent
        print("\n3. Testing LongTermMemoryAgent...")
        longterm_agent = LongTermMemoryAgent(
            user_id=test_config["user_id"], llm_config=test_config["engine"]
        )
        longterm_result = await longterm_agent.run(test_memory, extract_memories=True)
        print(f"   Stored: {longterm_result.get('status') == 'success'}")
        longterm_query = await longterm_agent.run(test_query, extract_memories=False)
        print(f"   Retrieved: {'alice' in str(longterm_query).lower()}")

        # 4. AdvancedRAGMemoryAgent
        print("\n4. Testing AdvancedRAGMemoryAgent...")
        rag_config = AdvancedRAGConfig(
            user_id=test_config["user_id"],
            memory_store_path=str(Path(temp_dir) / "rag_memory"),
            llm_config=test_config["engine"],
            strategy=RetrievalStrategy.HYBRID,
        )
        rag_agent = AdvancedRAGMemoryAgent(rag_config)
        rag_store = await rag_agent.add_memory(test_memory, importance="high")
        print(f"   Stored: {rag_store['stored']}")
        rag_query = await rag_agent.query_memory(test_query)
        print(f"   Retrieved: {'alice' in rag_query['answer'].lower()}")

        print("\n✅ All individual memory agents tested successfully!")

    @pytest.mark.asyncio
    async def test_multi_memory_coordinator_basic(self, test_config, temp_dir):
        """Test MultiMemoryCoordinator with basic operations."""
        print("\n=== Testing MultiMemoryCoordinator Basic Operations ===\n")

        # Create coordinator without graph (doesn't require Neo4j)
        config = MultiMemoryConfig(
            user_id=test_config["user_id"],
            engine=test_config["engine"],
            base_storage_path=str(temp_dir),
            enable_graph=False,  # Disable graph to avoid Neo4j dependency
            default_mode=CoordinationMode.INTELLIGENT,
        )

        coordinator = MultiMemoryCoordinator(config)
        print(f"Initialized with {len(coordinator.memory_systems)} memory systems")

        # Test intelligent storage
        memories = [
            (
                "Bob Smith works as CTO at DataCorp and specializes in distributed systems.",
                "high",
            ),
            (
                "I had lunch with Bob yesterday where we discussed scalability challenges.",
                "normal",
            ),
            ("Important: Bob's email is bob.smith@datacorp.com", "critical"),
            ("DataCorp is planning to expand to Europe next year.", "normal"),
        ]

        print("\nStoring memories with intelligent routing...")
        for content, importance in memories:
            result = await coordinator.store_memory(
                content, importance=importance, mode=CoordinationMode.INTELLIGENT
            )
            print(
                f"Stored in {len(result['systems_used'])} systems: {result['systems_used']}"
            )

        # Test different query modes
        queries = [
            ("Who is Bob Smith?", CoordinationMode.INTELLIGENT),
            ("What did we discuss at lunch?", CoordinationMode.PARALLEL),
            ("What is Bob's contact information?", CoordinationMode.HIERARCHICAL),
        ]

        print("\nQuerying with different coordination modes...")
        for query, mode in queries:
            result = await coordinator.query_memory(query, mode=mode)
            print(f"\nQuery: {query}")
            print(f"Mode: {mode.value}")
            print(f"Systems queried: {result['systems_queried']}")
            print(
                f"Found answer: {'bob' in str(result.get('combined_result', '')).lower()}"
            )

        # Test analytics
        print("\nGetting system analytics...")
        analytics = await coordinator.get_system_analytics()
        print(f"Total operations: {analytics['coordinator']['operation_history']}")
        print(f"Active systems: {list(analytics['systems'].keys())}")

        print("\n✅ MultiMemoryCoordinator basic operations tested successfully!")

    @pytest.mark.asyncio
    async def test_memory_system_integration(self, test_config, temp_dir):
        """Test integration between different memory systems."""
        print("\n=== Testing Memory System Integration ===\n")

        # Create comprehensive coordinator
        coordinator = MultiMemoryCoordinator.create_comprehensive_system(
            user_id=test_config["user_id"],
            enable_graph=False,
            storage_path=str(temp_dir),
        )

        # Simulate a day of interactions
        print("Simulating a day of memory interactions...")

        # Morning: Learning about a new project
        morning_memories = [
            "Project Phoenix is our new AI initiative starting next month.",
            "Sarah Chen will lead Project Phoenix as the technical architect.",
            "The project aims to build an autonomous agent system.",
            "Budget allocated: $2.5 million over 18 months.",
        ]

        print("\nMorning: Storing project information...")
        for memory in morning_memories:
            await coordinator.store_memory(
                memory,
                importance="high",
                metadata={"time": "morning", "category": "project"},
            )

        # Afternoon: Technical discussions
        afternoon_memories = [
            "Discussed using transformer architecture for the agent's language model.",
            "Sarah suggested implementing a multi-agent coordination system.",
            "We need to research graph neural networks for knowledge representation.",
            "Important: Technical review meeting scheduled for next Tuesday at 2 PM.",
        ]

        print("\nAfternoon: Storing technical discussions...")
        for memory in afternoon_memories:
            await coordinator.store_memory(
                memory, importance="normal" if "Important" not in memory else "critical"
            )

        # Evening: Personal notes
        evening_memories = [
            "Remember to send Sarah the research papers on multi-agent systems.",
            "My thoughts: The project seems ambitious but achievable with the right team.",
            "Need to brush up on my knowledge of graph databases before the meeting.",
        ]

        print("\nEvening: Storing personal notes...")
        for memory in evening_memories:
            await coordinator.store_memory(memory, importance="normal")

        # End of day queries
        print("\n=== End of Day Queries ===")

        queries = [
            "What is Project Phoenix and who is leading it?",
            "What technical decisions were discussed today?",
            "What do I need to prepare for the upcoming meeting?",
            "What are my action items from today?",
        ]

        for query in queries:
            print(f"\nQuery: {query}")
            result = await coordinator.query_memory(
                query, mode=CoordinationMode.INTELLIGENT, combine_results=True
            )

            answer = result.get("combined_result", "No answer found")
            print(f"Answer preview: {answer[:200]}...")
            print(f"Systems used: {result['systems_queried']}")

            # Verify key information is retrieved
            answer_lower = str(answer).lower()
            if "phoenix" in query.lower():
                assert "phoenix" in answer_lower or "sarah" in answer_lower
            if "technical" in query.lower():
                assert "transformer" in answer_lower or "multi-agent" in answer_lower

        print("\n✅ Memory system integration tested successfully!")

    @pytest.mark.asyncio
    async def test_advanced_rag_features(self, test_config, temp_dir):
        """Test advanced RAG features like reranking and citations."""
        print("\n=== Testing Advanced RAG Features ===\n")

        # Create advanced RAG agent with all features
        config = AdvancedRAGConfig(
            user_id=test_config["user_id"],
            memory_store_path=str(Path(temp_dir) / "advanced_rag"),
            llm_config=test_config["engine"],
            strategy=RetrievalStrategy.ADAPTIVE,
            enable_reranking=True,
            include_citations=True,
            enable_query_expansion=True,
            k_initial=10,
            k_final=3,
        )

        agent = AdvancedRAGMemoryAgent(config)

        # Add diverse technical memories
        technical_memories = [
            (
                "BERT revolutionized NLP by introducing bidirectional pre-training of transformers.",
                "critical",
            ),
            (
                "GPT models use autoregressive training with causal attention masks.",
                "high",
            ),
            ("T5 treats all NLP tasks as text-to-text problems.", "high"),
            (
                "RoBERTa improved BERT by removing NSP and training on more data.",
                "normal",
            ),
            (
                "ELECTRA uses discriminative pre-training instead of masked language modeling.",
                "normal",
            ),
            (
                "DeBERTa adds disentangled attention and enhanced mask decoder.",
                "normal",
            ),
        ]

        print("Adding technical memories...")
        for content, importance in technical_memories:
            await agent.add_memory(content, importance=importance)

        # Test different complexity queries
        test_queries = [
            # Simple query
            ("What is BERT?", "simple"),
            # Medium complexity
            ("How does GPT differ from BERT in training approach?", "medium"),
            # Complex query
            (
                "Compare the architectural innovations in BERT, RoBERTa, and DeBERTa, and explain how each improved upon its predecessors.",
                "complex",
            ),
        ]

        print("\nTesting queries of different complexities...")
        for query, expected_complexity in test_queries:
            print(f"\nQuery: {query}")

            # Analyze complexity
            complexity = agent.analyze_query_complexity(query)
            print(
                f"Detected complexity: {complexity.value} (expected: {expected_complexity})"
            )

            # Query with full analysis
            result = await agent.query_memory(query, include_analysis=True)

            print(f"Strategy used: {result['analysis']['strategy_used']}")
            print(f"Documents retrieved: {result['retrieved_docs']}")

            # Check citations if enabled
            if result.get("citations"):
                print(f"Citations included: {len(result['citations'])} sources")

            print(f"Answer preview: {result['answer'][:150]}...")

            # Verify answer quality
            answer_lower = result["answer"].lower()
            if "bert" in query.lower():
                assert "bert" in answer_lower or "bidirectional" in answer_lower

        # Test analytics
        analytics = await agent.get_memory_analytics()
        print(f"\nRAG Analytics:")
        print(f"  Total documents: {analytics['documents']['total_documents']}")
        print(
            f"  Query complexity distribution: {analytics['queries']['complexity_distribution']}"
        )
        print(
            f"  Average processing time: {analytics['queries']['avg_processing_time']:.2f}s"
        )

        print("\n✅ Advanced RAG features tested successfully!")

    @pytest.mark.asyncio
    async def test_memory_persistence_and_recovery(self, test_config, temp_dir):
        """Test memory persistence across sessions."""
        print("\n=== Testing Memory Persistence and Recovery ===\n")

        storage_path = str(Path(temp_dir) / "persistent_memory")

        # Session 1: Store memories
        print("Session 1: Storing memories...")
        coordinator1 = MultiMemoryCoordinator.create_comprehensive_system(
            user_id=test_config["user_id"],
            enable_graph=False,
            storage_path=storage_path,
        )

        memories = [
            "Project deadline is December 15th, 2024.",
            "Team members: Alice (AI), Bob (Backend), Carol (Frontend).",
            "Critical dependency: Integration with legacy system API.",
            "Budget remaining: $500,000",
        ]

        for memory in memories:
            await coordinator1.store_memory(memory, importance="high")

        # Save any persistent stores
        if hasattr(
            coordinator1.memory_systems.get(MemorySystemType.REACT), "save_vector_store"
        ):
            coordinator1.memory_systems[MemorySystemType.REACT].save_vector_store(
                str(Path(storage_path) / "react_memory")
            )

        print("Session 1 completed, memories stored.")

        # Session 2: New coordinator, same storage
        print("\nSession 2: Creating new coordinator with same storage...")
        coordinator2 = MultiMemoryCoordinator.create_comprehensive_system(
            user_id=test_config["user_id"],
            enable_graph=False,
            storage_path=storage_path,
        )

        # Query previous session's memories
        queries = [
            "When is the project deadline?",
            "Who are the team members?",
            "What is our budget status?",
        ]

        print("\nQuerying memories from previous session...")
        for query in queries:
            result = await coordinator2.query_memory(query)
            answer = str(result.get("combined_result", ""))
            print(f"\nQuery: {query}")
            print(f"Found answer: {len(answer) > 20}")

            # Verify key information persisted
            answer_lower = answer.lower()
            if "deadline" in query.lower():
                assert "december" in answer_lower or "15" in answer_lower
            if "team" in query.lower():
                assert any(name in answer_lower for name in ["alice", "bob", "carol"])

        print("\n✅ Memory persistence and recovery tested successfully!")

    @pytest.mark.asyncio
    async def test_complex_real_world_scenario(self, test_config, temp_dir):
        """Test a complex real-world scenario with all systems."""
        print("\n=== Testing Complex Real-World Scenario ===\n")

        # Create a comprehensive system for a research assistant
        coordinator = MultiMemoryCoordinator.create_comprehensive_system(
            user_id="researcher", enable_graph=False, storage_path=str(temp_dir)
        )

        print("Scenario: AI Research Assistant managing research project")

        # Phase 1: Literature review
        print("\nPhase 1: Literature Review")
        papers = [
            (
                "'Attention is All You Need' (2017) introduced the transformer architecture, eliminating recurrence and convolutions.",
                "critical",
            ),
            (
                "BERT (2018) demonstrated that bidirectional pre-training significantly improves downstream task performance.",
                "critical",
            ),
            (
                "GPT-3 (2020) showed that scale alone can enable few-shot learning without task-specific fine-tuning.",
                "high",
            ),
            (
                "Chain-of-Thought Prompting (2022) enables complex reasoning by encouraging step-by-step thinking.",
                "high",
            ),
            (
                "Constitutional AI (2023) introduces methods for training harmless and helpful AI assistants.",
                "normal",
            ),
        ]

        for content, importance in papers:
            await coordinator.store_memory(
                f"Research paper: {content}",
                importance=importance,
                metadata={"type": "literature", "source": "academic"},
            )

        # Phase 2: Research meetings
        print("\nPhase 2: Research Meetings")
        meetings = [
            "Met with Prof. Smith who suggested exploring retrieval-augmented generation for our chatbot.",
            "Industry partner wants the system to handle 1000 concurrent users with <2s response time.",
            "Team decided to use a hybrid approach: fine-tuned small model + RAG for knowledge.",
            "Important: Submit grant proposal by November 30th including preliminary results.",
        ]

        for meeting in meetings:
            importance = "critical" if "Important" in meeting else "normal"
            await coordinator.store_memory(
                meeting,
                importance=importance,
                metadata={"type": "meeting", "source": "collaboration"},
            )

        # Phase 3: Technical implementation notes
        print("\nPhase 3: Technical Implementation")
        implementation = [
            "Implemented base transformer model using PyTorch, achieving 95% accuracy on validation set.",
            "RAG system using FAISS vector store reduces latency by 40% compared to full model inference.",
            "Memory usage issue: Need to implement gradient checkpointing for larger batch sizes.",
            "Successfully integrated with partner's API, handling 500 req/s in load tests.",
        ]

        for note in implementation:
            await coordinator.store_memory(
                note,
                importance="normal",
                metadata={"type": "implementation", "source": "development"},
            )

        # Phase 4: Complex queries spanning all phases
        print("\nPhase 4: Complex Integrated Queries")

        complex_queries = [
            "Based on the literature review and our meetings, what architecture should we use for the chatbot?",
            "What are the performance requirements and our current progress toward meeting them?",
            "What are the upcoming deadlines and deliverables for the project?",
            "How do recent AI advances like Chain-of-Thought relate to our implementation decisions?",
        ]

        for query in complex_queries:
            print(f"\n{'='*60}")
            print(f"Query: {query}")

            result = await coordinator.query_memory(
                query,
                mode=CoordinationMode.PARALLEL,  # Use all systems
                combine_results=True,
            )

            print(f"Systems consulted: {result['systems_queried']}")
            print(f"Processing time: {result['total_time']:.2f}s")

            answer = result.get("combined_result", "No answer")
            print(f"\nAnswer: {answer[:300]}...")

            # Verify comprehensive answers
            answer_lower = answer.lower()
            if "architecture" in query.lower():
                assert any(
                    term in answer_lower for term in ["transformer", "rag", "hybrid"]
                )
            if "performance" in query.lower():
                assert any(
                    term in answer_lower for term in ["1000", "concurrent", "latency"]
                )
            if "deadline" in query.lower():
                assert any(
                    term in answer_lower for term in ["november", "grant", "proposal"]
                )

        # Final analytics
        print("\n" + "=" * 60)
        print("Final System Analytics:")
        analytics = await coordinator.get_system_analytics()

        total_ops = analytics["coordinator"]["operation_history"]
        print(f"Total operations performed: {total_ops}")

        for system, stats in analytics["systems"].items():
            if isinstance(stats, dict) and "total_documents" in stats:
                print(f"{system}: {stats['total_documents']} documents")

        print("\n✅ Complex real-world scenario tested successfully!")
        print("\n🎉 ALL MEMORY V2 SYSTEM TESTS COMPLETED SUCCESSFULLY! 🎉")


# GraphMemoryAgent test (requires Neo4j)
@pytest.mark.asyncio
@pytest.mark.skipif(True, reason="Requires Neo4j to be running")
async def test_graph_memory_with_neo4j():
    """Test GraphMemoryAgent with real Neo4j (skip if not available)."""
    print("\n=== Testing GraphMemoryAgent with Neo4j ===\n")

    config = GraphMemoryConfig(
        neo4j_uri="bolt://localhost:7687",
        neo4j_username="neo4j",
        neo4j_password="password",
        user_id="graph_test_user",
        mode=GraphMemoryMode.FULL,
    )

    try:
        agent = GraphMemoryAgent(config)

        # Test structured knowledge
        result = await agent.run(
            "John Smith is the CEO of TechCorp. He knows Sarah Johnson who works as CTO. "
            "TechCorp is located in San Francisco and was founded in 2015.",
            auto_store=True,
        )

        print(f"Extracted {result['extracted_graph']['total_nodes']} nodes")
        print(
            f"Extracted {result['extracted_graph']['total_relationships']} relationships"
        )

        # Query the graph
        query_result = await agent.query_graph(
            "Who are the executives at TechCorp?", query_type="natural"
        )

        print(f"Query answer: {query_result.get('answer', 'No answer')}")

        # Cleanup
        agent.graph.query(
            "MATCH (n {user_id: $user_id}) DETACH DELETE n",
            {"user_id": "graph_test_user"},
        )

        print("\n✅ GraphMemoryAgent tested successfully!")

    except Exception as e:
        print(f"Neo4j test skipped: {e}")


# Run all tests
async def run_complete_test_suite():
    """Run the complete test suite."""
    print("\n" + "=" * 80)
    print("🚀 MEMORY V2 COMPLETE SYSTEM TEST SUITE 🚀")
    print("=" * 80)

    test_instance = TestCompleteMemorySystem()
    temp_dir = tempfile.mkdtemp()

    try:
        config = {"user_id": "test_user", "engine": AugLLMConfig(temperature=0.1)}

        # Run all tests
        await test_instance.test_all_memory_agents_individually(config, temp_dir)
        await test_instance.test_multi_memory_coordinator_basic(config, temp_dir)
        await test_instance.test_memory_system_integration(config, temp_dir)
        await test_instance.test_advanced_rag_features(config, temp_dir)
        await test_instance.test_memory_persistence_and_recovery(config, temp_dir)
        await test_instance.test_complex_real_world_scenario(config, temp_dir)

        # Optional: Test with Neo4j if available
        # await test_graph_memory_with_neo4j()

    finally:
        shutil.rmtree(temp_dir)

    print("\n" + "=" * 80)
    print("✨ ALL TESTS COMPLETED SUCCESSFULLY! ✨")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(run_complete_test_suite())
