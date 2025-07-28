"""Simple test script for search agents without memory dependencies."""

import asyncio
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_basic_imports():
    """Test that basic imports work."""
    print("🔍 Testing basic imports...")

    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        print("✅ AugLLMConfig imported successfully")

        from haive.agents.react.agent import ReactAgent

        print("✅ ReactAgent imported successfully")

        return True

    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False


def test_search_agent_imports():
    """Test that search agent imports work."""
    print("\n🔍 Testing search agent imports...")

    try:
        from haive.agents.memory.search.quick_search.agent import QuickSearchAgent

        print("✅ QuickSearchAgent imported successfully")

        from haive.agents.memory.search.pro_search.agent import ProSearchAgent

        print("✅ ProSearchAgent imported successfully")

        from haive.agents.memory.search.deep_research.agent import DeepResearchAgent

        print("✅ DeepResearchAgent imported successfully")

        from haive.agents.memory.search.labs.agent import LabsAgent

        print("✅ LabsAgent imported successfully")

        return True

    except ImportError as e:
        print(f"❌ Search agent import failed: {e}")
        return False


async def test_quick_search_basic():
    """Test basic QuickSearchAgent functionality."""
    print("\n🚀 Testing QuickSearchAgent basic functionality...")

    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.memory.search.quick_search.agent import QuickSearchAgent

        # Create simple configuration
        config = AugLLMConfig(temperature=0.1, max_tokens=150)

        # Create agent
        agent = QuickSearchAgent(name="test_quick_search", engine=config)

        print(f"✅ Agent created successfully: {agent.name}")

        # Test basic properties
        print(f"🔧 Agent engine: {type(agent.engine).__name__}")
        tools_count = (
            len(agent.tools)
            if hasattr(agent, "tools") and agent.tools is not None
            else 0
        )
        print(f"🛠️ Agent tools: {tools_count} tools")

        # Test response model
        response_model = agent.get_response_model()
        print(f"📝 Response model: {response_model.__name__}")

        # Test system prompt
        system_prompt = agent.get_system_prompt()
        print(f"💬 System prompt length: {len(system_prompt)} chars")

        # Test search instructions
        instructions = agent.get_search_instructions()
        print(f"📋 Instructions length: {len(instructions)} chars")

        # Test keyword extraction
        keywords = agent.extract_keywords("What is the capital of France?")
        print(f"🔤 Keywords extracted: {keywords}")

        # Test answer type determination
        answer_type = agent.determine_answer_type("What is machine learning?")
        print(f"❓ Answer type: {answer_type}")

        return True

    except Exception as e:
        print(f"❌ QuickSearchAgent test failed: {e}")
        return False


async def test_pro_search_basic():
    """Test basic ProSearchAgent functionality."""
    print("\n🚀 Testing ProSearchAgent basic functionality...")

    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.memory.search.pro_search.agent import ProSearchAgent

        # Create configuration
        config = AugLLMConfig(temperature=0.3, max_tokens=400)

        # Create agent
        agent = ProSearchAgent(name="test_pro_search", engine=config)

        print(f"✅ Agent created successfully: {agent.name}")

        # Test query refinement
        test_query = "How can I improve my productivity?"
        test_context = {
            "domain": "software_development",
            "experience_level": "intermediate",
        }

        refinement = agent.refine_query(test_query, test_context)
        print("🔄 Query refinement:")
        print(f"  Original: {refinement.original_query}")
        print(f"  Refined: {refinement.refined_query}")
        print(f"  Reason: {refinement.refinement_reason}")

        # Test contextual insights
        insights = agent.extract_contextual_insights(test_query, test_context)
        print(f"💡 Contextual insights: {len(insights)} insights")
        for insight in insights:
            print(f"  - {insight.insight} (score: {insight.relevance_score:.2f})")

        # Test reasoning steps
        reasoning_steps = agent.generate_reasoning_steps(test_query, test_context)
        print(f"🧠 Reasoning steps: {len(reasoning_steps)} steps")
        for i, step in enumerate(reasoning_steps, 1):
            print(f"  {i}. {step}")

        # Test follow-up questions
        follow_ups = agent.generate_follow_up_questions(
            test_query, "Sample response", test_context
        )
        print(f"❓ Follow-up questions: {len(follow_ups)} questions")
        for i, question in enumerate(follow_ups, 1):
            print(f"  {i}. {question}")

        return True

    except Exception as e:
        print(f"❌ ProSearchAgent test failed: {e}")
        return False


async def test_deep_research_basic():
    """Test basic DeepResearchAgent functionality."""
    print("\n🚀 Testing DeepResearchAgent basic functionality...")

    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.memory.search.deep_research.agent import DeepResearchAgent

        # Create configuration
        config = AugLLMConfig(temperature=0.2, max_tokens=800)

        # Create agent
        agent = DeepResearchAgent(name="test_deep_research", engine=config)

        print(f"✅ Agent created successfully: {agent.name}")
        print(
            f"🔧 Knowledge graph enabled: {hasattr(agent, 'enable_kg') and agent.enable_kg}"
        )

        # Test query decomposition
        test_query = "What are the environmental impacts of electric vehicles?"
        focus_areas = ["manufacturing", "lifecycle", "disposal"]

        sub_queries = agent.decompose_research_query(test_query, focus_areas)
        print(f"🔍 Query decomposition: {len(sub_queries)} sub-queries")
        for i, sub_query in enumerate(sub_queries[:5], 1):  # Show first 5
            print(f"  {i}. {sub_query}")

        # Test source credibility evaluation
        test_source = {
            "domain": "nature.com",
            "type": "academic",
            "publication_date": "2023-01-01",
        }

        credibility = agent.evaluate_source_credibility(test_source)
        print(f"⭐ Source credibility: {credibility:.2f}")

        # Test research query execution
        research_query = await agent.execute_research_query(
            "electric vehicle environmental impact studies", "background"
        )
        print("📊 Research query result:")
        print(f"  Query: {research_query.query}")
        print(f"  Type: {research_query.query_type}")
        print(f"  Success: {research_query.success}")
        print(f"  Processing time: {research_query.processing_time:.2f}s")

        return True

    except Exception as e:
        print(f"❌ DeepResearchAgent test failed: {e}")
        return False


async def test_labs_basic():
    """Test basic LabsAgent functionality."""
    print("\n🚀 Testing LabsAgent basic functionality...")

    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.memory.search.labs.agent import LabsAgent

        # Create configuration
        config = AugLLMConfig(temperature=0.3, max_tokens=1000)

        # Create agent
        agent = LabsAgent(name="test_labs", engine=config, enable_code_execution=True)

        print(f"✅ Agent created successfully: {agent.name}")
        print(
            f"🔧 Code execution enabled: {hasattr(agent, 'enable_code_execution') and agent.enable_code_execution}"
        )
        tools_count = (
            len(agent.tools)
            if hasattr(agent, "tools") and agent.tools is not None
            else 0
        )
        print(f"🛠️ Total tools: {tools_count} tools")

        # Test workflow planning
        test_query = "Create a dashboard analyzing sales data"
        project_type = "dashboard"
        data_sources = ["sales_data.csv", "customer_info.json"]

        workflow_plan = agent.plan_project_workflow(
            test_query, project_type, data_sources
        )
        print(f"📋 Workflow plan: {len(workflow_plan)} steps")
        for i, step in enumerate(workflow_plan, 1):
            print(f"  {i}. {step['name']} ({step['estimated_time']}s)")

        # Test workflow step execution
        if workflow_plan:
            step_result = await agent.execute_workflow_step(workflow_plan[0], 0)
            print("✅ Workflow step executed:")
            print(f"  Step: {step_result.name}")
            print(f"  Success: {step_result.success}")
            print(f"  Duration: {step_result.duration_seconds:.2f}s")
            print(f"  Tool: {step_result.tool_used}")

        return True

    except Exception as e:
        print(f"❌ LabsAgent test failed: {e}")
        return False


def print_summary(results):
    """Print test summary."""
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)

    total_tests = len(results)
    passed_tests = sum(results.values())
    success_rate = (passed_tests / total_tests) * 100

    print(f"✅ Tests passed: {passed_tests}/{total_tests}")
    print(f"📈 Success rate: {success_rate:.1f}%")

    print("\n📋 Individual Results:")
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"  {test_name}: {status}")

    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED! Search agents are working correctly!")
    else:
        print("\n⚠️ Some tests failed. Check output above for details.")


async def main():
    """Main test execution."""
    print("🚀 Starting Search Agents Simple Test Suite")
    print("=" * 60)

    results = {}

    # Test imports
    results["basic_imports"] = test_basic_imports()
    results["search_agent_imports"] = test_search_agent_imports()

    # Test basic functionality
    results["quick_search_basic"] = await test_quick_search_basic()
    results["pro_search_basic"] = await test_pro_search_basic()
    results["deep_research_basic"] = await test_deep_research_basic()
    results["labs_basic"] = await test_labs_basic()

    # Print summary
    print_summary(results)


if __name__ == "__main__":
    asyncio.run(main())
