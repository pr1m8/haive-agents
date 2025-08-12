"""Test reflection agents with real LLMs - NO MOCKS."""

from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.reflection import (
    GradedReflectionMultiAgent,
    GradingAgent,
    GradingResult,
    ReflectionMultiAgent,
    StructuredOutputMultiAgent,
    create_expert_agent,
    create_reflection_agent,
    create_tool_based_reflection_agent,
)
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class TestReflectionAgents:
    """Test reflection agents with real components."""
    def test_simple_reflection_agent(self):
        """Test basic reflection agent improving a response."""
        # Create reflection agent
        reflector = create_reflection_agent(name="test_reflector")

        # Original response to improve
        original = """
        Python is a programming language. It's used for many things.
        It has simple syntax.
        """

        # Run reflection
        improved = reflector.run(f"Please reflect on and improve this response:\n\n{original}")

        # Verify improvement
        assert isinstance(improved, str)
        assert len(improved) > len(original)  # Should be more detailed
        assert improved != original  # Should be different

    def test_grading_agent_with_structured_output(self):
        """Test grading agent produces structured GradingResult."""
        # Create grading agent
        grader = GradingAgent(name="test_grader", engine=AugLLMConfig(temperature=0.1))

        # Response to grade
        query = "What is machine learning?"
        response = """
        Machine learning is a subset of artificial intelligence that enables
        computers to learn from data without being explicitly programmed.
        It uses algorithms to identify patterns and make decisions.
        """

        # Grade the response
        result = grader.run(f"Original query: {query}\n\nResponse to grade:\n{response}")

        # Verify structured output
        assert isinstance(result, GradingResult)
        assert 0 <= result.overall_score.score <= 100
        assert result.letter_grade.startswith(("A", "B", "C", "D", "F"))
        assert len(result.strengths) > 0
        assert 0 <= result.accuracy_score <= 100
        assert 0 <= result.completeness_score <= 100

    def test_expert_agent_with_domain(self):
        """Test expert agent with specific domain expertise."""
        # Create expert in quantum physics
        expert = create_expert_agent(
            name="quantum_expert",
            domain="quantum physics",
            expertise_level="world-class",
            style="academic but accessible",
        )

        # Ask expert question
        response = expert.run("Explain quantum entanglement in simple terms")

        # Verify expert response
        assert isinstance(response, str)
        assert len(response) > 100  # Should be detailed
        # Should mention quantum concepts
        assert any(
            term in response.lower() for term in ["quantum", "entangle", "particle", "state"]
        )

    def test_tool_based_reflection_agent(self):
        """Test reflection agent that uses tools."""
        # Create a simple calculation tool
        @tool
        def calculator(expression: str) -> str:
            """Calculate mathematical expressions."""
            try:
                result = eval(expression)
                return f"The result of {expression} is {result}"
            except:
                return "Invalid expression"

        # Create tool-based reflector
        reflector = create_tool_based_reflection_agent(name="tool_reflector", tools=[calculator])

        # Original response with calculation error
        original = """
        To calculate the area of a circle with radius 5, we use the formula
        A = πr². So the area would be approximately 3.14 × 5 × 5 = 75.
        """

        # Run reflection with tool
        improved = reflector.run(
            f"Please improve this response, using tools to verify calculations:\n\n{original}"
        )

        # Should correct the calculation
        assert isinstance(improved, str)
        assert "78.5" in improved or "78.54" in improved  # Correct answer


class TestPrePostHookPatterns:
    """Test the generic pre/post hook multi-agent patterns."""
    def test_reflection_multi_agent(self):
        """Test main agent with reflection post-processing."""
        # Create main agent
        main_agent = SimpleAgent(
            name="writer",
            engine=AugLLMConfig(system_message="You are a helpful writing assistant."),
        )

        # Create reflection multi-agent
        reflective_writer = ReflectionMultiAgent.create(
            main_agent=main_agent, name="reflective_writer"
        )

        # Test writing with reflection
        query = "Write a short paragraph about the importance of testing"

        # This would normally run through the full graph with message transformation
        # For unit test, we'll simulate the flow

        # Step 1: Main agent writes
        initial_response = main_agent.run(query)

        # Step 2: Reflection (would have message transform in between)
        reflector = reflective_writer.post_agent
        reflected = reflector.run(
            f"Please reflect on and improve this response:\n\n{initial_response}"
        )

        # Verify improvement
        assert len(reflected) >= len(initial_response)
        assert reflected != initial_response

    def test_structured_output_multi_agent(self):
        """Test main agent with structured output extraction."""
        # Define output model
        class Summary(BaseModel):
            main_topic: str = Field(description="Main topic discussed")
            key_points: list[str] = Field(description="Key points made")
            word_count: int = Field(description="Approximate word count")

        # Create main agent
        main_agent = SimpleAgent(name="analyzer", engine=AugLLMConfig())

        # Create structured output multi-agent
        structured_analyzer = StructuredOutputMultiAgent.create(
            main_agent=main_agent, output_model=Summary, name="structured_analyzer"
        )

        # Test analysis
        text = """
        Artificial intelligence is transforming how we work and live.
        Key benefits include automation of repetitive tasks, enhanced
        decision-making through data analysis, and new creative possibilities.
        However, we must also consider ethical implications and job displacement.
        """

        # Run main agent
        analysis = main_agent.run(f"Analyze this text:\n{text}")

        # Extract structure
        structurer = structured_analyzer.post_agent
        structured = structurer.run(analysis)

        # Verify structured output
        assert isinstance(structured, Summary)
        assert structured.main_topic
        assert len(structured.key_points) > 0
        assert structured.word_count > 0

    def test_graded_reflection_multi_agent(self):
        """Test full graded reflection pattern."""
        # Create main agent
        main_agent = SimpleAgent(
            name="explainer",
            engine=AugLLMConfig(system_message="You explain complex topics clearly."),
        )

        # Create graded reflection system
        graded_system = GradedReflectionMultiAgent.create(
            main_agent=main_agent, name="graded_explainer"
        )

        # Test explanation with grading and reflection
        query = "Explain recursion in programming"

        # Step 1: Main agent explains
        explanation = main_agent.run(query)

        # Step 2: Grade the explanation
        grader = graded_system.pre_agent
        grade = grader.run(f"Original query: {query}\n\nResponse to grade:\n{explanation}")

        assert isinstance(grade, GradingResult)

        # Step 3: Reflect and improve based on grade
        reflector = graded_system.post_agent

        # Format grade feedback for reflection
        grade_context = f"""
        The response received a grade of {grade.letter_grade} ({grade.overall_score.score}/100).

        Strengths: {", ".join(grade.strengths)}
        Weaknesses: {", ".join(grade.weaknesses)}

        Suggested improvements:
        {chr(10).join(f"- {imp.suggestion}" for imp in grade.improvements[:3])}
        """

        improved = reflector.run(
            f"Original response:\n{explanation}\n\n"
            f"Feedback:\n{grade_context}\n\n"
            f"Please provide an improved version addressing the feedback."
        )

        # Verify improvement addresses feedback
        assert len(improved) > 50
        assert improved != explanation


class TestReflectionWithMessageTransform:
    """Test reflection patterns that use message transformation."""
    def test_reflection_preserves_context(self):
        """Test that reflection preserves original query context."""
        # This tests the pattern where:
        # 1. User asks question
        # 2. Agent responds
        # 3. Response is transformed to human message
        # 4. Reflection agent sees it and improves

        from langchain_core.messages import AIMessage, HumanMessage

        from haive.core.schema.prebuilt.messages_state import MessagesState

        # Create state with conversation
        state = MessagesState()

        # Original query
        state.add_message(HumanMessage(content="Explain cloud computing"))

        # Agent response
        state.add_message(
            AIMessage(
                content="Cloud computing is when you use computers over the internet.",
                additional_kwargs={"engine_name": "main_agent"},
            )
        )

        # After reflection transform, the AI message becomes human
        # But first message (original query) is preserved

        # Reflection agent would see:
        # - Original query (preserved)
        # - Previous response as human input

        reflector = create_reflection_agent()

        # Simulate post-transform state
        reflection_input = (
            "Original query: Explain cloud computing\n\n"
            "Response to improve: Cloud computing is when you use computers over the internet."
        )

        improved = reflector.run(reflection_input)

        # Should maintain context and improve
        assert "cloud computing" in improved.lower()
        assert len(improved) > 100  # More detailed


if __name__ == "__main__":
    # Run tests
    test_basic = TestReflectionAgents()
    test_basic.test_simple_reflection_agent()
    test_basic.test_grading_agent_with_structured_output()
    test_basic.test_expert_agent_with_domain()
    test_basic.test_tool_based_reflection_agent()

    test_patterns = TestPrePostHookPatterns()
    test_patterns.test_reflection_multi_agent()
    test_patterns.test_structured_output_multi_agent()
    test_patterns.test_graded_reflection_multi_agent()

    test_transform = TestReflectionWithMessageTransform()
    test_transform.test_reflection_preserves_context()
