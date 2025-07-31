"""Simple test script for search agents without memory dependencies."""

import asyncio
import logging


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_basic_imports():
    """Test that basic imports work."""
    try:
        from haive.agents.react.agent import ReactAgent
        from haive.core.engine.aug_llm import AugLLMConfig

        return True

    except ImportError:
        return False


def test_search_agent_imports():
    """Test that search agent imports work."""
    try:
        from haive.agents.memory.search.deep_research.agent import DeepResearchAgent
        from haive.agents.memory.search.labs.agent import LabsAgent
        from haive.agents.memory.search.pro_search.agent import ProSearchAgent
        from haive.agents.memory.search.quick_search.agent import QuickSearchAgent

        return True

    except ImportError:
        return False


async def test_quick_search_basic():
    """Test basic QuickSearchAgent functionality."""
    try:
        from haive.agents.memory.search.quick_search.agent import QuickSearchAgent
        from haive.core.engine.aug_llm import AugLLMConfig

        # Create simple configuration
        config = AugLLMConfig(temperature=0.1, max_tokens=150)

        # Create agent
        agent = QuickSearchAgent(name="test_quick_search", engine=config)

        # Test basic properties
        (len(agent.tools) if hasattr(agent, "tools") and agent.tools is not None else 0)

        # Test response model
        agent.get_response_model()

        # Test system prompt
        agent.get_system_prompt()

        # Test search instructions
        agent.get_search_instructions()

        # Test keyword extraction
        agent.extract_keywords("What is the capital of France?")

        # Test answer type determination
        agent.determine_answer_type("What is machine learning?")

        return True

    except Exception:
        return False


async def test_pro_search_basic():
    """Test basic ProSearchAgent functionality."""
    try:
        from haive.agents.memory.search.pro_search.agent import ProSearchAgent
        from haive.core.engine.aug_llm import AugLLMConfig

        # Create configuration
        config = AugLLMConfig(temperature=0.3, max_tokens=400)

        # Create agent
        agent = ProSearchAgent(name="test_pro_search", engine=config)

        # Test query refinement
        test_query = "How can I improve my productivity?"
        test_context = {
            "domain": "software_development",
            "experience_level": "intermediate",
        }

        agent.refine_query(test_query, test_context)

        # Test contextual insights
        insights = agent.extract_contextual_insights(test_query, test_context)
        for _insight in insights:
            pass

        # Test reasoning steps
        reasoning_steps = agent.generate_reasoning_steps(test_query, test_context)
        for _i, _step in enumerate(reasoning_steps, 1):
            pass

        # Test follow-up questions
        follow_ups = agent.generate_follow_up_questions(
            test_query, "Sample response", test_context
        )
        for _i, _question in enumerate(follow_ups, 1):
            pass

        return True

    except Exception:
        return False


async def test_deep_research_basic():
    """Test basic DeepResearchAgent functionality."""
    try:
        from haive.agents.memory.search.deep_research.agent import DeepResearchAgent
        from haive.core.engine.aug_llm import AugLLMConfig

        # Create configuration
        config = AugLLMConfig(temperature=0.2, max_tokens=800)

        # Create agent
        agent = DeepResearchAgent(name="test_deep_research", engine=config)

        # Test query decomposition
        test_query = "What are the environmental impacts of electric vehicles?"
        focus_areas = ["manufacturing", "lifecycle", "disposal"]

        sub_queries = agent.decompose_research_query(test_query, focus_areas)
        for _i, _sub_query in enumerate(sub_queries[:5], 1):  # Show first 5
            pass

        # Test source credibility evaluation
        test_source = {
            "domain": "nature.com",
            "type": "academic",
            "publication_date": "2023-01-01",
        }

        agent.evaluate_source_credibility(test_source)

        # Test research query execution
        await agent.execute_research_query(
            "electric vehicle environmental impact studies", "background"
        )

        return True

    except Exception:
        return False


async def test_labs_basic():
    """Test basic LabsAgent functionality."""
    try:
        from haive.agents.memory.search.labs.agent import LabsAgent
        from haive.core.engine.aug_llm import AugLLMConfig

        # Create configuration
        config = AugLLMConfig(temperature=0.3, max_tokens=1000)

        # Create agent
        agent = LabsAgent(name="test_labs", engine=config, enable_code_execution=True)

        (len(agent.tools) if hasattr(agent, "tools") and agent.tools is not None else 0)

        # Test workflow planning
        test_query = "Create a dashboard analyzing sales data"
        project_type = "dashboard"
        data_sources = ["sales_data.csv", "customer_info.json"]

        workflow_plan = agent.plan_project_workflow(
            test_query, project_type, data_sources
        )
        for _i, _step in enumerate(workflow_plan, 1):
            pass

        # Test workflow step execution
        if workflow_plan:
            await agent.execute_workflow_step(workflow_plan[0], 0)

        return True

    except Exception:
        return False


def print_summary(results):
    """Print test summary."""
    total_tests = len(results)
    passed_tests = sum(results.values())
    (passed_tests / total_tests) * 100

    for _test_name, _result in results.items():
        pass

    if passed_tests == total_tests:
        pass
    else:
        pass


async def main():
    """Main test execution."""
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
