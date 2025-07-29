"""Comprehensive test suite for ValidationNodeV2 with edge cases and bad tool calls.

This test validates the correct ValidationNodeV2 pattern discovered from the user's .v2 branch:

KEY VALIDATION NODE V2 PATTERN:
===============================
The ValidationNodeV2 correctly implements conditional tool injection:

1. **Pydantic Models** → Create ToolMessage for validation
   - Extracts tool calls with route "pydantic_model"
   - Validates using Pydantic model.model_validate()
   - Creates ToolMessage with validation results
   - Adds ToolMessage to state for downstream processing

2. **LangChain Tools** → Let tool_node handle (NO ToolMessage)
   - Extracts tool calls with route "langchain_tool"
   - Does NOT create ToolMessage
   - Lets tool_node execute the actual tool
   - Preserves original message flow

3. **Dynamic Engine Attribution**
   - Extracts engine_name from AIMessage.additional_kwargs
   - Uses engine.tool_routes to determine routing
   - Supports multiple engines in same workflow

This test suite validates:
1. Correct routing of pydantic_model vs langchain_tool
2. Proper ToolMessage creation for Pydantic models ONLY
3. No ToolMessage creation for langchain tools (correct behavior)
4. Error handling for bad tool calls
5. Unknown tool handling
6. Dynamic engine attribution
7. Multiple tool calls with mixed types
8. Malformed tool call handling
"""

import json
import logging
import pytest
from typing import List, Optional

from langchain_core.messages import AIMessage, ToolMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.types import Command
from pydantic import BaseModel, Field, ValidationError

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.node.validation_node_v2 import ValidationNodeV2
from haive.core.schema.prebuilt.messages_state import MessagesState

logger = logging.getLogger(__name__)


# Test Pydantic models
class TaskAnalysis(BaseModel):
    """Structured task analysis model."""
    task_type: str = Field(description="Type of task")
    complexity: int = Field(ge=1, le=10, description="Complexity score")
    requirements: List[str] = Field(description="Task requirements")


class InvalidModel(BaseModel):
    """Model that will fail validation."""
    required_field: str = Field(description="This is required")
    must_be_positive: int = Field(gt=0, description="Must be positive")


# Test tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def search_tool(query: str, max_results: int = 5) -> str:
    """Search for information."""
    return f"Found {max_results} results for '{query}'"


class TestValidationNodeV2Comprehensive:
    """Comprehensive test suite for ValidationNodeV2."""

    @pytest.fixture
    def real_engine(self):
        """Create a real AugLLMConfig engine with tools and structured output."""
        engine = AugLLMConfig(
            model="gpt-4",
            temperature=0.7,
            structured_output_model=TaskAnalysis,
            tools=[calculator, search_tool]
        )
        
        # Set up tool routes - AugLLMConfig should do this automatically
        # but we'll ensure they're set correctly
        engine.tool_routes = {
            "TaskAnalysis": "pydantic_model",
            "InvalidModel": "pydantic_model",
            "calculator": "langchain_tool",
            "search_tool": "langchain_tool",
            "unknown_tool": "unknown"
        }
        
        # Add schemas for validation
        engine.schemas = [TaskAnalysis, InvalidModel]
        
        return engine

    @pytest.fixture
    def validation_node(self):
        """Create ValidationNodeV2 instance."""
        return ValidationNodeV2(
            name="test_validation",
            router_node="validation_router"
        )

    @pytest.fixture
    def base_state(self, real_engine):
        """Create base state with real engine."""
        return MessagesState(
            messages=[
                HumanMessage(content="Test the validation")
            ],
            engines={"test_engine": real_engine},
            tool_routes=real_engine.tool_routes,
            engine_name="test_engine"
        )

    def test_pydantic_model_validation_success(self, validation_node, base_state):
        """Test successful Pydantic model validation creates proper ToolMessage."""
        # Create AIMessage with tool call for TaskAnalysis
        ai_message = AIMessage(
            content="I'll analyze this task",
            tool_calls=[{
                "id": "call_123",
                "name": "TaskAnalysis",
                "args": {
                    "task_type": "coding",
                    "complexity": 7,
                    "requirements": ["Python", "Testing", "Documentation"]
                }
            }],
            additional_kwargs={"engine_name": "test_engine"}
        )
        base_state.messages.append(ai_message)

        # Execute validation node
        result = validation_node(base_state)

        # Verify Command structure
        assert isinstance(result, Command)
        assert result.goto == "validation_router"
        assert "messages" in result.update

        # Check the ToolMessage was created
        updated_messages = result.update["messages"]
        assert len(updated_messages) > len(base_state.messages)
        
        tool_message = updated_messages[-1]
        
        assert isinstance(tool_message, ToolMessage)
        assert tool_message.tool_call_id == "call_123"
        assert tool_message.name == "TaskAnalysis"
        
        # Parse content
        content = json.loads(tool_message.content)
        assert content["success"] is True
        assert content["model"] == "TaskAnalysis"
        assert content["validated"] is True
        assert content["data"]["task_type"] == "coding"
        assert content["data"]["complexity"] == 7
        
        # Check additional kwargs
        assert tool_message.additional_kwargs["is_error"] is False
        assert tool_message.additional_kwargs["validation_passed"] is True
        assert tool_message.additional_kwargs["model_type"] == "pydantic"

    def test_pydantic_model_validation_failure(self, validation_node, base_state):
        """Test Pydantic model validation failure creates error ToolMessage."""
        # Create AIMessage with invalid data
        ai_message = AIMessage(
            content="Testing invalid data",
            tool_calls=[{
                "id": "call_456",
                "name": "TaskAnalysis",
                "args": {
                    "task_type": "coding",
                    "complexity": 15,  # Invalid: > 10
                    "requirements": []  # This is ok, empty list is valid
                }
            }]
        )
        base_state.messages.append(ai_message)

        # Execute validation node
        result = validation_node(base_state)

        # Check error ToolMessage
        tool_message = result.update["messages"][-1]
        assert isinstance(tool_message, ToolMessage)
        assert tool_message.tool_call_id == "call_456"
        
        content = json.loads(tool_message.content)
        assert content["success"] is False
        assert content["error"] == "ValidationError"
        assert "complexity" in content["details"]
        
        # Check error flags
        assert tool_message.additional_kwargs["is_error"] is True
        assert tool_message.additional_kwargs["validation_passed"] is False

    def test_langchain_tool_routing_no_toolmessage(self, validation_node, base_state):
        """Test that langchain tools don't get ToolMessages, just route to tool_node."""
        # Create AIMessage with calculator tool call
        ai_message = AIMessage(
            content="Let me calculate that",
            tool_calls=[{
                "id": "call_789",
                "name": "calculator",
                "args": {"expression": "15 * 23"}
            }],
            additional_kwargs={"engine_name": "test_engine"}
        )
        base_state.messages.append(ai_message)

        # Execute validation node
        result = validation_node(base_state)

        # Should route to validation_router
        assert result.goto == "validation_router"
        
        # Should NOT create a ToolMessage for langchain tools
        # The original messages + AI message should be there, but no new ToolMessage
        updated_messages = result.update["messages"]
        assert len(updated_messages) == len(base_state.messages)
        
        # Last message should still be the AIMessage
        assert isinstance(updated_messages[-1], AIMessage)

    def test_multiple_mixed_tool_calls(self, validation_node, base_state):
        """Test handling multiple tool calls with mixed types."""
        # Create AIMessage with multiple tool calls
        ai_message = AIMessage(
            content="Processing multiple tools",
            tool_calls=[
                {
                    "id": "call_001",
                    "name": "TaskAnalysis",
                    "args": {
                        "task_type": "analysis",
                        "complexity": 5,
                        "requirements": ["Data", "Statistics"]
                    }
                },
                {
                    "id": "call_002",
                    "name": "calculator",
                    "args": {"expression": "100 / 5"}
                },
                {
                    "id": "call_003",
                    "name": "search_tool",
                    "args": {"query": "Python best practices"}
                }
            ]
        )
        base_state.messages.append(ai_message)

        # Execute validation node
        result = validation_node(base_state)

        # Should have created exactly 1 new ToolMessage (for TaskAnalysis only)
        updated_messages = result.update["messages"]
        new_messages = updated_messages[len(base_state.messages):]
        
        assert len(new_messages) == 1
        assert isinstance(new_messages[0], ToolMessage)
        assert new_messages[0].name == "TaskAnalysis"
        assert new_messages[0].tool_call_id == "call_001"

    def test_unknown_tool_handling(self, validation_node, base_state):
        """Test handling of unknown tools."""
        # Create AIMessage with unknown tool
        ai_message = AIMessage(
            content="Using unknown tool",
            tool_calls=[{
                "id": "call_unknown",
                "name": "unknown_tool",
                "args": {"param": "value"}
            }]
        )
        base_state.messages.append(ai_message)

        # Execute validation node
        result = validation_node(base_state)

        # Should create error ToolMessage for unknown tool
        tool_message = result.update["messages"][-1]
        assert isinstance(tool_message, ToolMessage)
        
        content = json.loads(tool_message.content)
        assert content["success"] is False
        assert "Unknown tool" in content["error"]

    def test_invalid_model_validation(self, validation_node, base_state):
        """Test validation of InvalidModel with missing required fields."""
        # Create AIMessage with InvalidModel missing required fields
        ai_message = AIMessage(
            content="Testing invalid model",
            tool_calls=[{
                "id": "call_invalid",
                "name": "InvalidModel",
                "args": {
                    "must_be_positive": -5  # Invalid: must be > 0
                    # Missing required_field
                }
            }]
        )
        base_state.messages.append(ai_message)

        # Execute validation node
        result = validation_node(base_state)

        # Should create error ToolMessage
        tool_message = result.update["messages"][-1]
        content = json.loads(tool_message.content)
        
        assert content["success"] is False
        assert content["error"] == "ValidationError"
        assert len(content["errors"]) >= 2  # At least 2 validation errors

    def test_dynamic_engine_attribution(self, validation_node, base_state):
        """Test that engine_name is extracted from AIMessage additional_kwargs."""
        # Create another engine with different routes
        alternate_engine = AugLLMConfig(
            model="gpt-3.5-turbo",
            temperature=0.5
        )
        alternate_engine.tool_routes = {
            "TaskAnalysis": "alternate_route"
        }
        base_state.engines["alternate_engine"] = alternate_engine

        # Create AIMessage with engine attribution
        ai_message = AIMessage(
            content="Using alternate engine",
            tool_calls=[{
                "id": "call_alt",
                "name": "TaskAnalysis",
                "args": {
                    "task_type": "testing",
                    "complexity": 3,
                    "requirements": ["Unit tests"]
                }
            }],
            additional_kwargs={"engine_name": "alternate_engine"}
        )
        base_state.messages.append(ai_message)

        # Execute validation node - it should use alternate_engine
        result = validation_node(base_state)

        # Should still create ToolMessage (since TaskAnalysis exists in alternate engine)
        tool_message = result.update["messages"][-1]
        assert isinstance(tool_message, ToolMessage)
        assert tool_message.name == "TaskAnalysis"

    def test_no_tool_calls_passthrough(self, validation_node, base_state):
        """Test that messages without tool calls pass through."""
        # Create AIMessage without tool calls
        ai_message = AIMessage(
            content="Just a regular response with no tool calls"
        )
        base_state.messages.append(ai_message)

        # Execute validation node
        result = validation_node(base_state)

        # Should route to validation_router with no new messages
        assert result.goto == "validation_router"
        assert len(result.update["messages"]) == len(base_state.messages)

    def test_malformed_tool_call(self, validation_node, base_state):
        """Test handling of malformed tool calls."""
        # Create AIMessage with malformed tool call (missing id)
        ai_message = AIMessage(
            content="Malformed tool call",
            tool_calls=[{
                # Missing "id" field
                "name": "TaskAnalysis",
                "args": {"task_type": "test"}
            }]
        )
        base_state.messages.append(ai_message)

        # Execute validation node - should handle gracefully
        result = validation_node(base_state)

        # Should continue processing even with malformed call
        assert result.goto == "validation_router"