"""Test message transformer reflection patterns - NO MOCKS.

This tests reflection patterns using Message Transformer V2 instead of
just structured output extraction. Tests the integration with the
message transformation system from haive-core.
"""

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
import pytest

from haive.agents.reflection.message_transformer import (
    ConversationalReflectionAgent,
    MessageTransformerReflectionAgent,
    create_conversational_reflection_agent,
    create_message_transformer_reflection_agent,
    create_reflection_context_transformer,
    create_reflection_message_flow,
)
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


class TestMessageTransformerReflection:
    """Test message transformer reflection patterns."""

    @pytest.mark.asyncio
    async def test_message_transformer_reflection_agent_basic(self):
        """Test basic message transformer reflection functionality."""
        # Create reflection agent
        mt_reflector = create_message_transformer_reflection_agent(
            name="test_mt_reflector"
        )

        # Create sample conversation
        conversation = [
            HumanMessage(content="What is Python?"),
            AIMessage(content="Python is a programming language."),
            HumanMessage(content="What are its main features?"),
            AIMessage(content="Python is easy to read and has many libraries."),
        ]

        # Run reflection analysis
        result = await mt_reflector.reflect_on_conversation(
            conversation, original_query="What is Python?"
        )

        # Verify reflection result structure
        assert isinstance(result, dict)
        assert "analysis" in result
        assert "transformed_messages" in result
        assert "original_messages" in result
        assert "transformation_applied" in result
        assert "message_count_before" in result
        assert "message_count_after" in result

        # Check transformation was applied
        assert result["transformation_applied"] == "reflection"
        assert result["message_count_before"] == len(conversation)
        assert isinstance(result["transformed_messages"], list)
        assert isinstance(result["analysis"], str)
        assert len(result["analysis"]) > 0

    @pytest.mark.asyncio
    async def test_conversational_reflection_agent(self):
        """Test conversational reflection with context injection."""
        # Create base agent
        base_agent = SimpleAgent(
            name="test_base",
            engine=AugLLMConfig(
                system_message="You are a helpful assistant.", temperature=0.5
            ),
        )

        # Create conversational reflection agent
        conv_reflector = create_conversational_reflection_agent(
            base_agent=base_agent, reflection_frequency=2  # Reflect every 2 messages
        )

        # Test first message (no reflection)
        result1 = await conv_reflector.run_with_reflection("Hello, how are you?")
        assert isinstance(result1, dict)
        assert not result1.get("reflection_applied", False)

        # Test second message (should trigger reflection)
        result2 = await conv_reflector.run_with_reflection("Tell me about AI")
        assert isinstance(result2, dict)
        assert result2.get("reflection_applied", False)
        assert result2.get("transformation_type") == "reflection_context"

        # Verify messages structure
        if "messages" in result2:
            assert isinstance(result2["messages"], list)
            assert len(result2["messages"]) > 0

    @pytest.mark.asyncio
    async def test_reflection_message_flow(self):
        """Test complete reflection message flow system."""
        # Create primary agent
        primary_agent = SimpleAgent(
            name="test_primary",
            engine=AugLLMConfig(
                system_message="You are an informative assistant.", temperature=0.6
            ),
        )

        # Create reflection flow
        reflection_flow = create_reflection_message_flow(
            primary_agent=primary_agent, name="test_flow"
        )

        # Test query
        query = "Explain quantum computing"

        # Run with reflection
        flow_result = await reflection_flow.run_primary_with_reflection(
            query=query, include_reflection=True
        )

        # Verify flow result structure
        assert isinstance(flow_result, dict)
        assert "primary_response" in flow_result
        assert "reflection_included" in flow_result
        assert flow_result["reflection_included"]

        # Check for reflection components
        if "reflection_response" in flow_result:
            assert isinstance(flow_result["reflection_response"], dict)

        if "enhanced_messages" in flow_result:
            assert isinstance(flow_result["enhanced_messages"], list)

        if "transformation_steps" in flow_result:
            assert isinstance(flow_result["transformation_steps"], list)
            assert len(flow_result["transformation_steps"]) > 0

    @pytest.mark.asyncio
    async def test_reflection_message_flow_without_reflection(self):
        """Test message flow with reflection disabled."""
        # Create primary agent
        primary_agent = SimpleAgent(
            name="test_primary_no_ref", engine=AugLLMConfig(temperature=0.5)
        )

        # Create reflection flow
        reflection_flow = create_reflection_message_flow(primary_agent)

        # Run without reflection
        result = await reflection_flow.run_primary_with_reflection(
            query="Simple test query", include_reflection=False
        )

        # Verify no reflection was applied
        assert not result["reflection_included"]
        assert "reflection_response" not in result
        assert "enhanced_messages" not in result
        assert "transformation_steps" not in result

    def test_reflection_context_transformer_function(self):
        """Test the reflection context transformer function."""
        # Create test messages with tool message containing reflection data
        messages = [
            HumanMessage(content="Test query"),
            AIMessage(content="Test response"),
            ToolMessage(
                name="ReflectionResult",
                content='{"critique": {"overall_quality": 0.7, "weaknesses": ["too brief"]}, "summary": "Response needs more detail"}',
                tool_call_id="test_call",
            ),
        ]

        # Apply transformer
        transformed = create_reflection_context_transformer(messages)

        # Should have original messages plus reflection context
        assert len(transformed) >= len(messages)

        # Find the added reflection context
        reflection_added = False
        for msg in transformed:
            if (
                isinstance(msg, HumanMessage)
                and "Previous response reflection" in msg.content
            ):
                reflection_added = True
                assert "Quality assessment: 0.7" in msg.content
                assert "too brief" in msg.content
                break

        assert reflection_added, "Reflection context should have been added"

    def test_agent_initialization_parameters(self):
        """Test agent initialization with different parameters."""
        # Test MessageTransformerReflectionAgent
        mt_agent = MessageTransformerReflectionAgent(
            name="custom_mt_agent", temperature=0.1, preserve_first_message=False
        )

        assert mt_agent.name == "custom_mt_agent"
        assert not mt_agent.preserve_first_message
        assert mt_agent.analyzer.engine.temperature == 0.1

        # Test ConversationalReflectionAgent
        base_agent = SimpleAgent(name="base", engine=AugLLMConfig())
        conv_agent = ConversationalReflectionAgent(
            base_agent=base_agent, name="custom_conv_agent", reflection_frequency=5
        )

        assert conv_agent.name == "custom_conv_agent"
        assert conv_agent.reflection_frequency == 5
        assert conv_agent.base_agent == base_agent

    @pytest.mark.asyncio
    async def test_empty_conversation_handling(self):
        """Test handling of empty conversations."""
        mt_reflector = create_message_transformer_reflection_agent()

        # Test with empty conversation
        empty_result = await mt_reflector.reflect_on_conversation([])

        # Should handle gracefully
        assert isinstance(empty_result, dict)
        assert empty_result["message_count_before"] == 0
        assert empty_result["message_count_after"] == 0

    @pytest.mark.asyncio
    async def test_single_message_conversation(self):
        """Test reflection on single message conversations."""
        mt_reflector = create_message_transformer_reflection_agent()

        # Single message conversation
        single_msg = [HumanMessage(content="Hello world")]

        result = await mt_reflector.reflect_on_conversation(single_msg)

        # Should process single message
        assert result["message_count_before"] == 1
        assert isinstance(result["analysis"], str)
        assert len(result["transformed_messages"]) >= 1


class TestMessageTransformerIntegration:
    """Test integration with message transformation system."""

    @pytest.mark.asyncio
    async def test_transformation_type_integration(self):
        """Test integration with TransformationType.REFLECTION."""
        from haive.core.graph.node.message_transformation_v2 import (
            TransformationType,
            create_reflection_transformer,
        )

        # Create reflection transformer
        transformer = create_reflection_transformer(
            name="test_reflection_transformer", preserve_first_message=True
        )

        # Verify it's properly configured
        assert transformer.transformation_type == TransformationType.REFLECTION
        assert transformer.preserve_first_message

        # Test with sample messages
        messages = [
            HumanMessage(content="Original query"),
            AIMessage(content="AI response"),
            HumanMessage(content="Follow up"),
        ]

        # Apply transformation
        transformed = transformer._apply_transformation(messages)

        # Should preserve first message and transform the rest
        assert len(transformed) == len(messages)
        assert isinstance(transformed[0], HumanMessage)  # First preserved
        assert transformed[0].content == "Original query"

    @pytest.mark.asyncio
    async def test_ai_to_human_transformation_integration(self):
        """Test integration with AI->Human message transformation."""
        from haive.core.graph.node.message_transformation_v2 import (
            MessageTransformationNodeConfig,
            TransformationType,
        )

        # Create AI->Human transformer
        transformer = MessageTransformationNodeConfig(
            name="test_ai_to_human",
            transformation_type=TransformationType.AI_TO_HUMAN,
            preserve_metadata=True,
        )

        # Test messages with AI message
        messages = [
            HumanMessage(content="Question"),
            AIMessage(
                content="AI answer with metadata", additional_kwargs={"test": "value"}
            ),
        ]

        # Apply transformation
        transformed = transformer._apply_transformation(messages)

        # AI message should become Human message
        assert len(transformed) == 2
        assert isinstance(transformed[0], HumanMessage)  # Original human
        assert isinstance(transformed[1], HumanMessage)  # Transformed AI->Human
        assert transformed[1].content == "AI answer with metadata"

        # Metadata should be preserved
        if hasattr(transformed[1], "additional_kwargs"):
            assert transformed[1].additional_kwargs.get("test") == "value"


class TestReflectionEdgeCases:
    """Test edge cases for message transformer reflection."""

    @pytest.mark.asyncio
    async def test_malformed_tool_messages(self):
        """Test handling of malformed tool messages in context transformer."""
        messages = [
            HumanMessage(content="Test"),
            AIMessage(content="Response"),
            ToolMessage(
                name="ReflectionResult",
                content="invalid json {",  # Malformed JSON
                tool_call_id="test",
            ),
        ]

        # Should handle gracefully without crashing
        transformed = create_reflection_context_transformer(messages)

        # Should return at least the original messages
        assert len(transformed) >= len(messages)

    @pytest.mark.asyncio
    async def test_very_long_conversation(self):
        """Test handling of very long conversations."""
        mt_reflector = create_message_transformer_reflection_agent()

        # Create long conversation
        long_conversation = []
        for i in range(50):
            long_conversation.extend(
                [
                    HumanMessage(content=f"Question {i}"),
                    AIMessage(content=f"Answer {i}"),
                ]
            )

        # Should handle long conversations
        result = await mt_reflector.reflect_on_conversation(long_conversation)

        assert result["message_count_before"] == 100
        assert isinstance(result["analysis"], str)
        assert len(result["analysis"]) > 0

    @pytest.mark.asyncio
    async def test_mixed_message_types(self):
        """Test handling of conversations with mixed message types."""
        from langchain_core.messages import SystemMessage, ToolMessage

        mt_reflector = create_message_transformer_reflection_agent()

        # Mixed message types
        mixed_conversation = [
            SystemMessage(content="System prompt"),
            HumanMessage(content="User question"),
            AIMessage(content="AI response"),
            ToolMessage(content="Tool result", tool_call_id="123", name="test_tool"),
            HumanMessage(content="Follow up"),
        ]

        # Should handle mixed types
        result = await mt_reflector.reflect_on_conversation(mixed_conversation)

        assert result["message_count_before"] == 5
        assert isinstance(result["transformed_messages"], list)


if __name__ == "__main__":
    # Run tests manually
    import asyncio

    async def run_tests():
        test_basic = TestMessageTransformerReflection()
        await test_basic.test_message_transformer_reflection_agent_basic()
        await test_basic.test_conversational_reflection_agent()
        await test_basic.test_reflection_message_flow()

        test_integration = TestMessageTransformerIntegration()
        await test_integration.test_transformation_type_integration()
        await test_integration.test_ai_to_human_transformation_integration()

        test_edge = TestReflectionEdgeCases()
        await test_edge.test_malformed_tool_messages()
        await test_edge.test_very_long_conversation()
        await test_edge.test_mixed_message_types()

    asyncio.run(run_tests())
