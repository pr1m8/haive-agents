"""Test structured output reflection agents - NO MOCKS."""

import pytest

from haive.agents.reflection.models import Critique, ReflectionResult
from haive.agents.reflection.structured_output import (
    ReflectionLoop,
    StructuredImprovementAgent,
    StructuredReflectionAgent,
    create_improvement_agent,
    create_reflection_agent,
    create_reflection_loop,
)
from haive.core.engine.aug_llm import AugLLMConfig


class TestStructuredReflectionAgents:
    """Test structured reflection agents with real components."""

    @pytest.mark.asyncio
    async def test_structured_reflection_agent_basic(self):
        """Test basic structured reflection agent functionality."""
        # Create reflection agent
        reflector = create_reflection_agent(name="test_reflector")

        # Test reflection on a simple response
        query = "What is Python?"
        response = "Python is a programming language. It's easy to use."

        # Run reflection
        reflection = await reflector.reflect(query, response)

        # Verify structured output
        assert reflection is not None
        assert isinstance(reflection, ReflectionResult)
        assert isinstance(reflection.critique, Critique)

        # Check required fields
        assert reflection.summary
        assert len(reflection.critique.strengths) > 0
        assert len(reflection.critique.weaknesses) >= 0
        assert len(reflection.critique.suggestions) >= 0
        assert 0.0 <= reflection.critique.overall_quality <= 1.0
        assert isinstance(reflection.critique.needs_revision, bool)
        assert 0.0 <= reflection.confidence <= 1.0
        assert len(reflection.action_items) >= 0

    @pytest.mark.asyncio
    async def test_structured_improvement_agent(self):
        """Test improvement agent with real reflection feedback."""
        # Create agents
        reflector = create_reflection_agent(name="test_reflector")
        improver = create_improvement_agent(name="test_improver")

        # Original content that needs improvement
        query = "Explain photosynthesis"
        poor_response = "Plants use sunlight to make food."

        # Get reflection feedback
        reflection = await reflector.reflect(query, poor_response)
        assert reflection is not None

        # Apply improvements
        improved_response = await improver.improve(query, poor_response, reflection)

        # Verify improvement
        assert isinstance(improved_response, str)
        assert len(improved_response) > len(poor_response)
        assert improved_response != poor_response
        assert "photosynthesis" in improved_response.lower()

    @pytest.mark.asyncio
    async def test_reflection_loop_iterative_improvement(self):
        """Test iterative reflection loop."""
        # Create reflection loop
        loop = create_reflection_loop(max_iterations=2, quality_threshold=0.7)

        # Starting content
        query = "What is artificial intelligence?"
        initial_response = "AI is computer intelligence."

        # Run iterative improvement
        result = await loop.iterate(query, initial_response)

        # Verify results
        assert isinstance(result, dict)
        assert "final_response" in result
        assert "iterations" in result
        assert "quality_scores" in result
        assert "reflections" in result
        assert "improved" in result

        # Check progression
        assert result["iterations"] >= 1
        assert len(result["quality_scores"]) >= 1
        assert len(result["reflections"]) >= 1

        # Final response should be different
        assert result["final_response"] != initial_response
        assert len(result["final_response"]) > len(initial_response)

    @pytest.mark.asyncio
    async def test_quality_threshold_stopping(self):
        """Test that reflection loop stops when quality threshold is reached."""
        # Create loop with high threshold
        loop = create_reflection_loop(
            max_iterations=5, quality_threshold=0.95  # Very high threshold
        )

        # Good starting response
        query = "What is 2+2?"
        good_response = "2+2 equals 4. This is basic arithmetic addition."

        # Run loop
        result = await loop.iterate(query, good_response)

        # Should stop quickly due to good quality
        assert result["iterations"] <= 3
        if result["quality_scores"]:
            # If we got quality scores, final should be decent
            assert result["quality_scores"][-1] >= 0.6

    @pytest.mark.asyncio
    async def test_extract_structured_output_function(self):
        """Test the post-processing hook extraction function."""
        # Create agent with structured output
        reflector = create_reflection_agent()

        # Run agent to get raw result
        query = "Test query"
        response = "Test response"

        # This would normally use the agent's arun method
        # For testing the extraction, we'll call the agent directly
        reflection = await reflector.reflect(query, response)

        # Verify extraction worked
        assert reflection is not None
        assert isinstance(reflection, ReflectionResult)

    def test_agent_creation_parameters(self):
        """Test agent creation with different parameters."""
        # Test custom parameters
        reflector = StructuredReflectionAgent(
            name="custom_reflector",
            temperature=0.1,
            system_prompt="Custom reflection prompt",
        )

        assert reflector.name == "custom_reflector"
        assert reflector.agent.engine.temperature == 0.1

        improver = StructuredImprovementAgent(name="custom_improver", temperature=0.8)

        assert improver.name == "custom_improver"
        assert improver.agent.engine.temperature == 0.8

    def test_reflection_loop_parameters(self):
        """Test reflection loop with different parameters."""
        loop = ReflectionLoop(
            reflector=create_reflection_agent(),
            improver=create_improvement_agent(),
            max_iterations=5,
            quality_threshold=0.9,
        )

        assert loop.max_iterations == 5
        assert loop.quality_threshold == 0.9

    @pytest.mark.asyncio
    async def test_declining_quality_stopping(self):
        """Test that loop stops if quality declines."""
        # This is harder to test reliably with real LLMs
        # but we can verify the loop completes
        loop = create_reflection_loop(max_iterations=3)

        query = "Explain quantum physics"
        response = "Quantum physics is about very small particles."

        result = await loop.iterate(query, response)

        # Should complete without errors
        assert "iterations" in result
        assert result["iterations"] >= 1


class TestReflectionEdgeCases:
    """Test edge cases and error handling."""

    @pytest.mark.asyncio
    async def test_empty_response_reflection(self):
        """Test reflection on empty response."""
        reflector = create_reflection_agent()

        query = "What is machine learning?"
        empty_response = ""

        # Should still work, just critique the emptiness
        reflection = await reflector.reflect(query, empty_response)

        # Should get a reflection even for empty response
        assert reflection is not None
        assert isinstance(reflection, ReflectionResult)

    @pytest.mark.asyncio
    async def test_very_long_response(self):
        """Test reflection on very long response."""
        reflector = create_reflection_agent()

        query = "Explain everything about computers"
        long_response = "Computers are electronic devices. " * 100

        reflection = await reflector.reflect(query, long_response)

        # Should handle long responses
        assert reflection is not None
        assert isinstance(reflection, ReflectionResult)

    @pytest.mark.asyncio
    async def test_special_characters_response(self):
        """Test reflection on response with special characters."""
        reflector = create_reflection_agent()

        query = "What is coding?"
        special_response = "Coding involves symbols like: {}, [], (), <>, @, #, $, %, &, *, +, =, |, \\, /, ?, ~"

        reflection = await reflector.reflect(query, special_response)

        # Should handle special characters
        assert reflection is not None
        assert isinstance(reflection, ReflectionResult)


class TestReflectionIntegration:
    """Test integration with other patterns."""

    @pytest.mark.asyncio
    async def test_sequential_agent_pattern(self):
        """Test reflection in sequential agent pattern."""
        from haive.agents.simple.agent import SimpleAgent

        # Create main agent
        main_agent = SimpleAgent(
            name="writer",
            engine=AugLLMConfig(system_message="You are a concise writer."),
        )

        # Create reflection agent
        reflector = create_reflection_agent()

        # Sequential pattern: main -> reflect
        query = "Write about renewable energy"

        # Step 1: Main agent writes
        main_result = await main_agent.arun(query)

        # Extract response from main agent
        if isinstance(main_result, dict) and "messages" in main_result:
            messages = main_result["messages"]
            for msg in reversed(messages):
                if hasattr(msg, "content") and msg.content:
                    main_response = msg.content
                    break
            else:
                main_response = str(main_result)
        else:
            main_response = str(main_result)

        # Step 2: Reflect on main agent output
        reflection = await reflector.reflect(query, main_response)

        # Verify sequential pattern works
        assert reflection is not None
        assert isinstance(reflection, ReflectionResult)

    @pytest.mark.asyncio
    async def test_multi_perspective_reflection(self):
        """Test multiple reflection perspectives."""
        # Create specialized reflection agents
        technical_reflector = StructuredReflectionAgent(
            name="technical_reflector",
            system_prompt="""You are a technical expert who focuses on accuracy,
            precision, and technical correctness in responses.""",
        )

        communication_reflector = StructuredReflectionAgent(
            name="communication_reflector",
            system_prompt="""You are a communication expert who focuses on clarity,
            readability, and accessibility of responses.""",
        )

        query = "How does machine learning work?"
        response = "ML uses algorithms to find patterns in data and make predictions."

        # Get multiple perspectives
        technical_reflection = await technical_reflector.reflect(query, response)
        communication_reflection = await communication_reflector.reflect(
            query, response
        )

        # Both should work
        assert technical_reflection is not None
        assert communication_reflection is not None

        # Reflections may focus on different aspects
        assert isinstance(technical_reflection, ReflectionResult)
        assert isinstance(communication_reflection, ReflectionResult)


if __name__ == "__main__":
    # Run tests manually
    import asyncio

    async def run_tests():
        test_basic = TestStructuredReflectionAgents()
        await test_basic.test_structured_reflection_agent_basic()
        await test_basic.test_structured_improvement_agent()
        await test_basic.test_reflection_loop_iterative_improvement()

        test_edge = TestReflectionEdgeCases()
        await test_edge.test_empty_response_reflection()
        await test_edge.test_very_long_response()

        test_integration = TestReflectionIntegration()
        await test_integration.test_sequential_agent_pattern()
        await test_integration.test_multi_perspective_reflection()

    asyncio.run(run_tests())
