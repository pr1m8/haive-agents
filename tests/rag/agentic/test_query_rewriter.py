"""Tests for QueryRewriterAgent - real component testing, no mocks."""

import pytest

from haive.agents.rag.agentic import QueryRewriterAgent
from haive.agents.rag.common.query_refinement.models import QueryRefinementResponse
from haive.core.engine.aug_llm import AugLLMConfig


class TestQueryRewriterAgent:
    """Test QueryRewriterAgent with real LLM calls."""

    @pytest.mark.asyncio
    async def test_query_rewriter_creation(self):
        """Test creating a query rewriter agent."""
        rewriter = QueryRewriterAgent.create_default(name="test_rewriter", temperature=0.7)

        assert rewriter.name == "test_rewriter"
        assert rewriter.structured_output_model == QueryRefinementResponse
        assert isinstance(rewriter.engine, AugLLMConfig)
        assert rewriter.engine.temperature == 0.7

    @pytest.mark.asyncio
    async def test_rewrite_vague_query(self):
        """Test rewriting a vague query with real LLM."""
        rewriter = QueryRewriterAgent.create_default(temperature=0.7)

        # Test with a vague query
        vague_query = "ML stuff"

        result = await rewriter.rewrite_query(vague_query)

        # Verify result structure
        assert isinstance(result, QueryRefinementResponse)
        assert result.original_query == vague_query
        assert result.query_analysis  # Should analyze the query
        assert result.query_type  # Should classify query type
        assert result.complexity_level in ["simple", "moderate", "complex"]

        # Should have refinement suggestions
        assert len(result.refinement_suggestions) > 0
        assert result.best_refined_query
        assert result.search_strategy_recommendations

        # Best query should be more specific than original
        assert len(result.best_refined_query) > len(vague_query)
        assert result.best_refined_query != vague_query

    @pytest.mark.asyncio
    async def test_rewrite_with_context(self):
        """Test rewriting with additional context."""
        rewriter = QueryRewriterAgent.create_default(temperature=0.7)

        query = "latest developments"
        context = "User is researching quantum computing for a technical paper"

        result = await rewriter.rewrite_query(query, context)

        # Refined query should incorporate quantum computing context
        assert (
            "quantum" in result.best_refined_query.lower()
            or "computing" in result.best_refined_query.lower()
        )

        # Should have multiple suggestions
        assert len(result.refinement_suggestions) >= 2

        # Each suggestion should have required fields
        for suggestion in result.refinement_suggestions:
            assert suggestion.refined_query
            assert suggestion.improvement_type
            assert suggestion.rationale
            assert suggestion.expected_benefit

    @pytest.mark.asyncio
    async def test_rewrite_already_good_query(self):
        """Test rewriting an already well-formed query."""
        rewriter = QueryRewriterAgent.create_default(temperature=0.7)

        good_query = "What are the key differences between supervised and unsupervised machine learning algorithms?"

        result = await rewriter.rewrite_query(good_query)

        # Should still provide suggestions
        assert len(result.refinement_suggestions) > 0

        # Analysis should recognize it's already good
        assert (
            "clear" in result.query_analysis.lower() or "specific" in result.query_analysis.lower()
        )

        # Complexity should be moderate or complex
        assert result.complexity_level in ["moderate", "complex"]

    @pytest.mark.asyncio
    async def test_multiple_refinement_types(self):
        """Test that different improvement types are suggested."""
        rewriter = QueryRewriterAgent.create_default(temperature=0.7)

        query = "AI applications"

        result = await rewriter.rewrite_query(query)

        # Collect improvement types
        improvement_types = {s.improvement_type for s in result.refinement_suggestions}

        # Should have variety in improvement types
        assert len(improvement_types) >= 2

        # Common improvement types to expect
        possible_types = {"clarity", "specificity", "scope", "context", "terminology"}
        assert len(improvement_types.intersection(possible_types)) > 0

    @pytest.mark.asyncio
    async def test_direct_agent_invocation(self):
        """Test invoking the agent directly."""
        rewriter = QueryRewriterAgent.create_default(temperature=0.7)

        input_data = {
            "query": "blockchain uses",
            "context": "Research for a fintech startup",
        }

        result = await rewriter.arun(input_data)

        assert isinstance(result, QueryRefinementResponse)
        assert result.original_query == "blockchain uses"

        # Should incorporate fintech context
        assert any(
            "fintech" in s.refined_query.lower() or "financial" in s.refined_query.lower()
            for s in result.refinement_suggestions
        )

    @pytest.mark.asyncio
    async def test_custom_engine_configuration(self):
        """Test creating rewriter with custom engine configuration."""
        custom_engine = AugLLMConfig(
            temperature=0.3,
            max_tokens=800,
            system_message="You are an expert at query optimization for technical searches.",
        )

        rewriter = QueryRewriterAgent.create_default(name="custom_rewriter", engine=custom_engine)

        assert rewriter.engine == custom_engine
        assert rewriter.engine.temperature == 0.3
        assert rewriter.engine.max_tokens == 800

    @pytest.mark.asyncio
    async def test_search_strategy_recommendations(self):
        """Test that search strategies are recommended."""
        rewriter = QueryRewriterAgent.create_default(temperature=0.7)

        query = "how to implement neural networks"

        result = await rewriter.rewrite_query(query)

        # Should have search strategy recommendations
        assert len(result.search_strategy_recommendations) > 0

        # Strategies should be actionable
        for strategy in result.search_strategy_recommendations:
            assert len(strategy) > 10  # Not just short phrases

    @pytest.mark.asyncio
    async def test_query_type_classification(self):
        """Test that queries are properly classified."""
        rewriter = QueryRewriterAgent.create_default(temperature=0.7)

        test_queries = {
            "What is the capital of France?": ["factual", "simple"],
            "Compare REST and GraphQL APIs": ["analytical", "comparison"],
            "How to build a web scraper": ["procedural", "how-to"],
            "Understanding consciousness": ["conceptual", "abstract"],
        }

        for query, expected_types in test_queries.items():
            result = await rewriter.rewrite_query(query)

            # Query type should match expected categories
            assert any(exp_type in result.query_type.lower() for exp_type in expected_types)
