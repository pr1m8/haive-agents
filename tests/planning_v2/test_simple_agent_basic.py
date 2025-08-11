#!/usr/bin/env python3
"""Test basic SimpleAgent functionality."""

import asyncio
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate

async def test_basic_simple_agent():
    """Test if SimpleAgent works at all."""
    print("\n=== TESTING BASIC SIMPLE AGENT ===\n")
    
    # Create basic agent without structured output
    agent = SimpleAgent(
        name="basic_test",
        engine=AugLLMConfig(temperature=0.1, max_tokens=50),
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Keep responses very brief."),
            ("human", "{query}")
        ])
    )
    
    print("1. Basic agent (no tools/structured output):")
    print(f"   Nodes: {list(agent.graph.nodes.keys())}")
    print(f"   Edges: {list(agent.graph.edges)}")
    
    try:
        result = await agent.arun({"query": "Say hello"})
        print(f"\n   ✅ Basic agent works! Result type: {type(result)}")
        if hasattr(result, 'messages'):
            print(f"   Messages count: {len(result.messages)}")
    except Exception as e:
        print(f"\n   ❌ Basic agent failed: {e}")

async def test_structured_output_agent():
    """Test SimpleAgent with structured output."""
    print("\n\n2. Agent with structured output:")
    
    from pydantic import BaseModel, Field
    
    class SimpleResponse(BaseModel):
        answer: str = Field(description="The answer")
        confidence: float = Field(description="Confidence 0-1")
    
    agent = SimpleAgent(
        name="structured_test",
        engine=AugLLMConfig(
            temperature=0.1,
            structured_output_model=SimpleResponse
        ),
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant."),
            ("human", "{query}")
        ])
    )
    
    print(f"   Nodes: {list(agent.graph.nodes.keys())}")
    print(f"   Edges: {list(agent.graph.edges)}")
    
    # Check for validation issues
    validation_edges = [e for e in agent.graph.edges if e[0] == "validation"]
    print(f"   Edges FROM validation: {validation_edges}")
    
    try:
        result = await agent.arun({"query": "What is 2+2?"})
        print(f"\n   Result after run: {type(result)}")
    except RecursionError as e:
        print(f"\n   ❌ RecursionError as expected: Graph stuck at validation node")
    except Exception as e:
        print(f"\n   ❌ Other error: {type(e).__name__}: {e}")

async def main():
    """Run all tests."""
    await test_basic_simple_agent()
    await test_structured_output_agent()
    
    print("\n\n=== SUMMARY ===")
    print("- Basic SimpleAgent (no validation) likely works")
    print("- SimpleAgent with structured output hits recursion due to missing validation edges")
    print("- The validation node is a dead end in the graph")

if __name__ == "__main__":
    asyncio.run(main())