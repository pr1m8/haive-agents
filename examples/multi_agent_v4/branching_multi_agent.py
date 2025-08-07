#!/usr/bin/env python3
"""Branching Multi-Agent Example with EnhancedMultiAgentV4.

This example demonstrates a conditional branching workflow where:
1. A classifier agent determines the type of query
2. Based on classification, routes to either:
   - Technical agent (for coding/technical questions)
   - Creative agent (for writing/creative tasks)
   - Research agent (for fact-finding/research)
3. A final summarizer agent processes the output

Date: August 7, 2025
"""

import asyncio
from typing import List, Literal

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


# Structured output models
class QueryClassification(BaseModel):
    """Classification of user query."""
    
    category: Literal["technical", "creative", "research"] = Field(
        description="Category of the query"
    )
    confidence: float = Field(
        ge=0.0, le=1.0, 
        description="Confidence in classification"
    )
    reasoning: str = Field(description="Brief reasoning for classification")


class FinalSummary(BaseModel):
    """Final summary of the multi-agent response."""
    
    query_type: str = Field(description="Type of query processed")
    agent_used: str = Field(description="Which agent handled the query")
    summary: str = Field(description="Concise summary of the response")
    key_points: List[str] = Field(description="Key points from the response")


# Tools for technical agent
@tool
def code_analyzer(code: str) -> str:
    """Analyze code and provide insights."""
    lines = code.count('\n') + 1
    return f"Code analysis: {lines} lines, appears to be Python code"


@tool
def documentation_search(topic: str) -> str:
    """Search documentation for a topic."""
    return f"Documentation found for '{topic}': Official docs recommend using async/await patterns"


# Tools for research agent
@tool
def fact_checker(statement: str) -> str:
    """Check facts and verify information."""
    return f"Fact check: '{statement}' - Status: Verified with high confidence"


@tool
def web_search(query: str) -> str:
    """Search the web for information."""
    return f"Web search for '{query}': Found 10 relevant results from reputable sources"


# Create agents
def create_agents():
    """Create all agents for the branching workflow."""
    
    # 1. Classifier agent - determines query type
    classifier = SimpleAgentV3(
        name="classifier",
        engine=AugLLMConfig(
            temperature=0.1,
            system_message="You are a query classifier. Analyze queries and categorize them as technical, creative, or research.",
            structured_output_model=QueryClassification
        ),
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "{system_message}"),
            ("human", "Classify this query: {messages}")
        ])
    )
    
    # 2. Technical agent - handles coding/technical questions
    technical = ReactAgent(
        name="technical_expert",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are a technical expert specializing in programming and software development."
        ),
        tools=[code_analyzer, documentation_search]
    )
    
    # 3. Creative agent - handles creative writing tasks
    creative = SimpleAgentV3(
        name="creative_writer",
        engine=AugLLMConfig(
            temperature=0.8,
            system_message="You are a creative writer skilled in storytelling, poetry, and imaginative content."
        ),
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "{system_message}"),
            ("human", "{messages}")
        ])
    )
    
    # 4. Research agent - handles fact-finding and research
    research = ReactAgent(
        name="researcher",
        engine=AugLLMConfig(
            temperature=0.2,
            system_message="You are a research specialist focused on finding accurate, verified information."
        ),
        tools=[fact_checker, web_search]
    )
    
    # 5. Summarizer agent - processes final output
    summarizer = SimpleAgentV3(
        name="summarizer",
        engine=AugLLMConfig(
            temperature=0.1,
            system_message="You are a summarizer who creates concise, well-structured summaries.",
            structured_output_model=FinalSummary
        ),
        prompt_template=ChatPromptTemplate.from_messages([
            ("system", "{system_message}"),
            ("human", "Summarize this response:\n\n{messages}\n\nOriginal query type: {query_type}")
        ])
    )
    
    return classifier, technical, creative, research, summarizer


async def test_branching_workflow():
    """Test the branching multi-agent workflow."""
    
    print("🌳 Branching Multi-Agent Workflow Example")
    print("=" * 60)
    
    # Create agents
    classifier, technical, creative, research, summarizer = create_agents()
    
    # Test queries
    test_queries = [
        "How do I implement a binary search tree in Python?",
        "Write a haiku about artificial intelligence",
        "What are the health benefits of meditation according to recent studies?"
    ]
    
    for query in test_queries:
        print(f"\n📋 Query: {query}")
        print("-" * 60)
        
        # Step 1: Classify the query
        print("1️⃣ Classifying query...")
        classification_result = await classifier.arun({
            "messages": [HumanMessage(content=query)]
        })
        
        # The result should be a QueryClassification instance
        if isinstance(classification_result, QueryClassification):
            print(f"   Category: {classification_result.category}")
            print(f"   Confidence: {classification_result.confidence:.0%}")
            print(f"   Reasoning: {classification_result.reasoning}")
            
            # Step 2: Route to appropriate agent
            print(f"\n2️⃣ Routing to {classification_result.category} agent...")
            
            if classification_result.category == "technical":
                agent_result = await technical.arun({
                    "messages": [HumanMessage(content=query)]
                })
                agent_used = "technical_expert"
            elif classification_result.category == "creative":
                agent_result = await creative.arun({
                    "messages": [HumanMessage(content=query)]
                })
                agent_used = "creative_writer"
            else:  # research
                agent_result = await research.arun({
                    "messages": [HumanMessage(content=query)]
                })
                agent_used = "researcher"
            
            # Extract response text
            if hasattr(agent_result, 'content'):
                response_text = agent_result.content
            elif isinstance(agent_result, dict) and 'messages' in agent_result:
                # Get last AI message
                messages = agent_result['messages']
                response_text = messages[-1].content if messages else "No response"
            else:
                response_text = str(agent_result)
            
            print(f"   Response preview: {response_text[:100]}...")
            
            # Step 3: Summarize the response
            print(f"\n3️⃣ Creating final summary...")
            summary_result = await summarizer.arun({
                "messages": [HumanMessage(content=response_text)],
                "query_type": classification_result.category
            })
            
            if isinstance(summary_result, FinalSummary):
                print(f"\n📊 Final Summary:")
                print(f"   Query Type: {summary_result.query_type}")
                print(f"   Agent Used: {summary_result.agent_used}")
                print(f"   Summary: {summary_result.summary}")
                print(f"   Key Points:")
                for i, point in enumerate(summary_result.key_points, 1):
                    print(f"     {i}. {point}")
            else:
                print(f"   Summary: {summary_result}")
        else:
            print(f"   Classification failed: {classification_result}")


async def test_multi_agent_branching():
    """Test using EnhancedMultiAgentV4 with conditional routing."""
    
    print("\n\n🔄 Testing EnhancedMultiAgentV4 with Branching")
    print("=" * 60)
    
    # Create a more complex branching workflow
    classifier, technical, creative, research, summarizer = create_agents()
    
    # Create a multi-agent that includes all agents
    # Note: EnhancedMultiAgentV4 currently supports sequential/parallel modes
    # For true conditional branching, we'd need custom routing logic
    
    print("Note: EnhancedMultiAgentV4 currently supports sequential and parallel modes.")
    print("For conditional branching, we use manual routing as shown above.")
    print("Future enhancement: Add 'conditional' mode with routing rules.")
    
    # Example of sequential workflow
    sequential_workflow = EnhancedMultiAgentV4(
        name="sequential_workflow",
        agents=[classifier, technical, summarizer],
        execution_mode="sequential"
    )
    
    print("\n📋 Testing sequential workflow (classifier → technical → summarizer):")
    query = "Explain Python decorators"
    
    result = await sequential_workflow.arun({
        "messages": [HumanMessage(content=query)]
    })
    
    print(f"Sequential result type: {type(result)}")


async def main():
    """Run all branching examples."""
    
    # Test manual branching workflow
    await test_branching_workflow()
    
    # Test multi-agent approaches
    await test_multi_agent_branching()
    
    print("\n\n✅ Branching workflow examples completed!")
    print("\n💡 Key Insights:")
    print("1. Manual branching gives full control over routing logic")
    print("2. Classifier with structured output enables type-safe routing")
    print("3. Different agents can specialize in different domains")
    print("4. Final summarizer provides consistent output format")
    print("5. Future: EnhancedMultiAgentV4 could add 'conditional' mode")


if __name__ == "__main__":
    asyncio.run(main())