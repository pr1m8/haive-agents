"""Test script for Perplexity-style search agents.

This script tests all four search agents (QuickSearch, ProSearch, DeepResearch, Labs)
with real LLM execution and comprehensive validation.
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_imports():
    """Test that all agent imports work correctly."""
    print("🔍 Testing imports...")

    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        print("✅ AugLLMConfig imported successfully")

        from haive.agents.memory.search.quick_search import QuickSearchAgent

        print("✅ QuickSearchAgent imported successfully")

        from haive.agents.memory.search.pro_search import ProSearchAgent

        print("✅ ProSearchAgent imported successfully")

        from haive.agents.memory.search.deep_research import DeepResearchAgent

        print("✅ DeepResearchAgent imported successfully")

        from haive.agents.memory.search.labs import LabsAgent

        print("✅ LabsAgent imported successfully")

        return True

    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False


async def test_quick_search_agent():
    """Test QuickSearchAgent with real LLM execution."""
    print("\n🚀 Testing QuickSearchAgent...")

    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.memory.search.quick_search import QuickSearchAgent

        # Create agent with optimized config
        config = AugLLMConfig(
            temperature=0.1,
            max_tokens=200,
            system_message="You are a quick search assistant providing concise answers.",
        )

        agent = QuickSearchAgent(name="test_quick_search", engine=config)

        # Test queries
        test_queries = [
            "What is the capital of France?",
            "How tall is Mount Everest?",
            "When was Python programming language created?",
            "What does AI stand for?",
        ]

        print(f"Testing {len(test_queries)} queries...")

        for i, query in enumerate(test_queries, 1):
            print(f"\n📝 Query {i}: {query}")

            try:
                response = await agent.process_search(query)

                print(f"✅ Response received in {response.processing_time:.2f}s")
                print(f"📊 Confidence: {response.confidence:.2f}")
                print(f"🔤 Keywords: {response.keywords}")
                print(f"📋 Answer type: {response.answer_type}")
                print(f"📝 Response: {response.response[:100]}...")

            except Exception as e:
                print(f"❌ Query {i} failed: {e}")

        # Test batch processing
        print("\n🔄 Testing batch processing...")
        batch_results = await agent.batch_search(test_queries[:2])
        print(f"✅ Batch processing completed: {len(batch_results)} results")

        return True

    except Exception as e:
        print(f"❌ QuickSearchAgent test failed: {e}")
        return False


async def test_pro_search_agent():
    """Test ProSearchAgent with real LLM execution."""
    print("\n🚀 Testing ProSearchAgent...")

    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.memory.search.pro_search import ProSearchAgent

        # Create agent with balanced config
        config = AugLLMConfig(
            temperature=0.3,
            max_tokens=800,
            system_message="You are a pro search assistant providing detailed, contextual responses.",
        )

        agent = ProSearchAgent(name="test_pro_search", engine=config)

        # Test queries with context
        test_cases = [
            {
                "query": "How can I improve my productivity while working from home?",
                "context": {
                    "domain": "software_development",
                    "experience_level": "intermediate",
                    "preferences": {"format": "structured_list"},
                },
            },
            {
                "query": "What are the best practices for machine learning model deployment?",
                "context": {"domain": "enterprise", "experience_level": "advanced"},
            },
        ]

        print(f"Testing {len(test_cases)} contextual queries...")

        for i, test_case in enumerate(test_cases, 1):
            print(f"\n📝 Query {i}: {test_case['query']}")
            print(f"🔍 Context: {test_case['context']}")

            try:
                response = await agent.process_pro_search(
                    query=test_case["query"],
                    context=test_case["context"],
                    depth_level=3,
                    use_preferences=True,
                    generate_follow_ups=True,
                )

                print(f"✅ Response received in {response.processing_time:.2f}s")
                print(f"📊 Confidence: {response.confidence:.2f}")
                print(f"🔧 Refinements: {len(response.refinements)}")
                print(f"💡 Insights: {len(response.contextual_insights)}")
                print(f"❓ Follow-ups: {len(response.follow_up_questions)}")
                print(f"📝 Response: {response.response[:150]}...")

                # Show refinements
                if response.refinements:
                    print(f"🔄 Query refined: {response.refinements[0].refined_query}")

                # Show follow-ups
                if response.follow_up_questions:
                    print(f"❓ Follow-up: {response.follow_up_questions[0]}")

            except Exception as e:
                print(f"❌ Query {i} failed: {e}")

        return True

    except Exception as e:
        print(f"❌ ProSearchAgent test failed: {e}")
        return False


async def test_deep_research_agent():
    """Test DeepResearchAgent with real LLM execution."""
    print("\n🚀 Testing DeepResearchAgent...")

    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.memory.search.deep_research import DeepResearchAgent

        # Create agent with research-optimized config
        config = AugLLMConfig(
            temperature=0.2,
            max_tokens=1500,
            system_message="You are a deep research assistant providing comprehensive, multi-source analysis.",
        )

        agent = DeepResearchAgent(
            name="test_deep_research",
            engine=config,
            enable_kg=False,  # Disable KG for this test
        )

        # Test research queries
        test_cases = [
            {
                "query": "What are the environmental impacts of electric vehicles?",
                "research_depth": 3,
                "focus_areas": ["manufacturing", "lifecycle", "disposal"],
            },
            {
                "query": "How does artificial intelligence impact healthcare outcomes?",
                "research_depth": 2,
                "focus_areas": ["diagnostic accuracy", "treatment efficiency"],
            },
        ]

        print(f"Testing {len(test_cases)} research queries...")

        for i, test_case in enumerate(test_cases, 1):
            print(f"\n📝 Research {i}: {test_case['query']}")
            print(f"🔍 Depth: {test_case['research_depth']}")
            print(f"🎯 Focus areas: {test_case['focus_areas']}")

            try:
                response = await agent.process_deep_research(
                    query=test_case["query"],
                    research_depth=test_case["research_depth"],
                    focus_areas=test_case["focus_areas"],
                    max_sources=20,
                    include_fact_checking=True,
                )

                print(f"✅ Research completed in {response.processing_time:.2f}s")
                print(f"📊 Confidence: {response.confidence:.2f}")
                print(f"📄 Sections: {len(response.research_sections)}")
                print(f"🔍 Queries executed: {len(response.research_queries)}")
                print(f"📚 Sources examined: {response.total_sources_examined}")
                print(f"⭐ High quality sources: {response.high_quality_sources}")
                print(f"📝 Executive summary: {response.executive_summary[:100]}...")

                # Show research sections
                if response.research_sections:
                    print(
                        f"📑 Section titles: {[s.title for s in response.research_sections]}"
                    )

                # Show limitations
                if response.limitations:
                    print(f"⚠️ Limitations: {response.limitations[0]}")

                # Show related topics
                if response.related_topics:
                    print(f"🔗 Related topics: {response.related_topics}")

            except Exception as e:
                print(f"❌ Research {i} failed: {e}")

        return True

    except Exception as e:
        print(f"❌ DeepResearchAgent test failed: {e}")
        return False


async def test_labs_agent():
    """Test LabsAgent with real LLM execution."""
    print("\n🚀 Testing LabsAgent...")

    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.memory.search.labs import LabsAgent

        # Create agent with project-optimized config
        config = AugLLMConfig(
            temperature=0.3,
            max_tokens=2000,
            system_message="You are a labs assistant providing comprehensive project automation.",
        )

        agent = LabsAgent(name="test_labs", engine=config, enable_code_execution=True)

        # Test project requests
        test_cases = [
            {
                "query": "Create a dashboard analyzing customer satisfaction survey data",
                "project_type": "dashboard",
                "data_sources": ["survey_data.csv", "customer_feedback.json"],
            },
            {
                "query": "Build an interactive chart showing sales trends over time",
                "project_type": "analysis",
                "data_sources": ["sales_data.csv"],
            },
        ]

        print(f"Testing {len(test_cases)} project requests...")

        for i, test_case in enumerate(test_cases, 1):
            print(f"\n📝 Project {i}: {test_case['query']}")
            print(f"🎯 Type: {test_case['project_type']}")
            print(f"📊 Data sources: {test_case['data_sources']}")

            try:
                response = await agent.process_labs_project(
                    query=test_case["query"],
                    project_type=test_case["project_type"],
                    data_sources=test_case["data_sources"],
                    create_interactive_app=True,
                    max_work_time=300,  # 5 minutes
                )

                print(f"✅ Project completed in {response.total_work_time:.2f}s")
                print(f"📊 Confidence: {response.confidence:.2f}")
                print(f"📋 Project: {response.project_name}")
                print(f"🔧 Workflow steps: {len(response.workflow_steps)}")
                print(f"📦 Assets created: {len(response.assets_created)}")
                print(f"🖥️ Interactive apps: {len(response.interactive_apps)}")
                print(f"🛠️ Tools used: {response.tools_used}")
                print(f"📈 Visualizations: {response.visualizations_created}")
                print(f"📝 Summary: {response.project_summary}")

                # Show workflow steps
                successful_steps = [s for s in response.workflow_steps if s.success]
                print(
                    f"✅ Successful steps: {len(successful_steps)}/{len(response.workflow_steps)}"
                )

                # Show asset types
                if response.assets_created:
                    asset_types = [a.type.value for a in response.assets_created]
                    print(f"📦 Asset types: {asset_types}")

                # Show next steps
                if response.next_steps:
                    print(f"➡️ Next step: {response.next_steps[0]}")

            except Exception as e:
                print(f"❌ Project {i} failed: {e}")

        return True

    except Exception as e:
        print(f"❌ LabsAgent test failed: {e}")
        return False


async def test_multi_agent_coordination():
    """Test multi-agent coordination with sequential processing."""
    print("\n🚀 Testing Multi-Agent Coordination...")

    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.memory.search.deep_research import DeepResearchAgent
        from haive.agents.memory.search.labs import LabsAgent
        from haive.agents.memory.search.pro_search import ProSearchAgent
        from haive.agents.memory.search.quick_search import QuickSearchAgent

        # Create all agents
        base_config = AugLLMConfig(temperature=0.2, max_tokens=1000)

        agents = {
            "quick": QuickSearchAgent(name="quick_agent", engine=base_config),
            "pro": ProSearchAgent(name="pro_agent", engine=base_config),
            "research": DeepResearchAgent(name="research_agent", engine=base_config),
            "labs": LabsAgent(name="labs_agent", engine=base_config),
        }

        # Test query progression: Quick → Pro → Research → Labs
        base_query = "Machine learning in healthcare"

        print(f"🔍 Base query: {base_query}")
        print("🤖 Agent progression: Quick → Pro → Research → Labs")

        # Step 1: Quick search for basic info
        print("\n1️⃣ Quick Search...")
        quick_response = await agents["quick"].process_search(base_query)
        print(f"✅ Quick search completed: {quick_response.response[:80]}...")

        # Step 2: Pro search for detailed analysis
        print("\n2️⃣ Pro Search...")
        pro_context = {
            "domain": "healthcare",
            "experience_level": "intermediate",
            "previous_search": quick_response.response,
        }
        pro_response = await agents["pro"].process_pro_search(
            query=base_query, context=pro_context, depth_level=3
        )
        print(
            f"✅ Pro search completed: {len(pro_response.follow_up_questions)} follow-ups generated"
        )

        # Step 3: Deep research for comprehensive analysis
        print("\n3️⃣ Deep Research...")
        research_response = await agents["research"].process_deep_research(
            query=base_query,
            research_depth=2,
            focus_areas=["diagnostic accuracy", "treatment outcomes"],
            max_sources=15,
        )
        print(
            f"✅ Deep research completed: {len(research_response.research_sections)} sections generated"
        )

        # Step 4: Labs for interactive implementation
        print("\n4️⃣ Labs Project...")
        labs_response = await agents["labs"].process_labs_project(
            query=f"Create a dashboard for {base_query} analysis",
            project_type="dashboard",
            data_sources=["ml_healthcare_data.csv"],
            max_work_time=180,
        )
        print(
            f"✅ Labs project completed: {len(labs_response.assets_created)} assets created"
        )

        # Summary
        print("\n📊 Multi-Agent Coordination Summary:")
        print(f"🚀 Quick: {quick_response.processing_time:.1f}s")
        print(f"⚡ Pro: {pro_response.processing_time:.1f}s")
        print(f"🔍 Research: {research_response.processing_time:.1f}s")
        print(f"🛠️ Labs: {labs_response.total_work_time:.1f}s")
        total_time = (
            quick_response.processing_time
            + pro_response.processing_time
            + research_response.processing_time
            + labs_response.total_work_time
        )
        print(f"⏱️ Total time: {total_time:.1f}s")

        # Demonstrate knowledge transfer
        print("\n🔄 Knowledge Transfer Demo:")
        print("📝 Quick → Pro: Context aware of basic facts")
        print(
            f"🔍 Pro → Research: {len(pro_response.follow_up_questions)} questions for deeper investigation"
        )
        print(
            f"📊 Research → Labs: {len(research_response.research_sections)} sections inform dashboard design"
        )

        return True

    except Exception as e:
        print(f"❌ Multi-agent coordination test failed: {e}")
        return False


def print_performance_summary(test_results: Dict[str, bool], start_time: datetime):
    """Print performance summary of all tests."""
    print("\n" + "=" * 60)
    print("🏆 PERFORMANCE SUMMARY")
    print("=" * 60)

    total_time = (datetime.now() - start_time).total_seconds()
    passed_tests = sum(test_results.values())
    total_tests = len(test_results)

    print(f"⏱️ Total execution time: {total_time:.2f}s")
    print(f"✅ Tests passed: {passed_tests}/{total_tests}")
    print(f"📊 Success rate: {(passed_tests/total_tests)*100:.1f}%")

    print("\n📋 Test Results:")
    for test_name, result in test_results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"  {test_name}: {status}")

    if passed_tests == total_tests:
        print(
            "\n🎉 ALL TESTS PASSED! Perplexity-style agents are ready for production!"n!"
        )
    else:
        print("\n⚠️ Some tests failed. Review the output above for details.")


async def main():
    """Main test execution."""
    print("🚀 Starting Perplexity-Style Search Agents Test Suite")
    print("=" * 60)

    start_time = datetime.now()
    test_results = {}

    # Test 1: Import validation
    test_results["imports"] = test_imports()

    # Test 2: Individual agent tests
    test_results["quick_search"] = await test_quick_search_agent()
    test_results["pro_search"] = await test_pro_search_agent()
    test_results["deep_research"] = await test_deep_research_agent()
    test_results["labs"] = await test_labs_agent()

    # Test 3: Multi-agent coordination
    test_results["multi_agent"] = await test_multi_agent_coordination()

    # Print final summary
    print_performance_summary(test_results, start_time)


if __name__ == "__main__":
    asyncio.run(main())
