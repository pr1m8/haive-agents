"""Run the SimpleAgentV3 structured output test with debug

This runs the exact test from the test suite to see how it works.

Date: August 7, 2025
"""

import asyncio
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Simplified Pydantic model
class QueryRefinementSuggestion(BaseModel):
    """Individual query refinement suggestion."""

    refined_query: str = Field(description="The refined/improved query")
    improvement_type: str = Field(description="Type of improvement made")
    rationale: str = Field(description="Why this refinement improves the query")


class QueryRefinementResponse(BaseModel):
    """Query refinement analysis and suggestions."""

    original_query: str = Field(description="The original user query")
    query_analysis: str = Field(description="Analysis of the query")
    query_type: str = Field(description="Classification of query type")
    complexity_level: str = Field(description="simple, moderate, or complex")
    refinement_suggestions: list[QueryRefinementSuggestion] = Field(
        description="List of suggested query improvements"
    )
    best_refined_query: str = Field(description="The recommended best refined query")


# Simplified prompt
RAG_QUERY_REFINEMENT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a query refinement expert. Analyze queries and suggest improvements.",
        ),
        ("human", "Analyze and refine this query: {query}"),
    ]
).partial(context="")


async def main():
    """Run the test."""
    print("Creating SimpleAgentV3 with structured_output_version='v2'...")
    print("=" * 60)

    # Create agent exactly like in the test
    agent = SimpleAgentV3(
        name="query_refiner",
        engine=AugLLMConfig(
            prompt_template=RAG_QUERY_REFINEMENT,
            structured_output_model=QueryRefinementResponse,
            structured_output_version="v2",  # Tool-based approach
            temperature=0.1,
        ),
        debug=True,  # Enable debug!
    )

    print("\n🔍 RUNNING AGENT...")
    print("=" * 60)

    # Run the agent
    try:
        result = await agent.arun({"query": "what is the tallest building in france"})

        print("\n" + "=" * 60)
        print("✅ EXECUTION COMPLETE")
        print("=" * 60)

        print(f"\nResult type: {type(result).__name__}")
        print(
            f"Result keys: {list(result.keys()) if hasattr(result, 'keys') else 'Not a dict'}"
        )

        # Check for structured output
        if hasattr(result, "get_latest_structured_output"):
            print("\n✅ Has get_latest_structured_output method!")
            structured_output = result.get_latest_structured_output()

            if structured_output:
                print(f"Structured output type: {type(structured_output).__name__}")
                if hasattr(structured_output, "model_dump"):
                    data = structured_output.model_dump()
                    print(f"\nStructured data:")
                    print(f"  - Original query: {data.get('original_query')}")
                    print(f"  - Query type: {data.get('query_type')}")
                    print(f"  - Best refined: {data.get('best_refined_query')}")
            else:
                print("❌ No structured output returned")
        else:
            print("\n❌ No get_latest_structured_output method")

        # Check messages
        if hasattr(result, "messages"):
            print(f"\n📬 Messages: {len(result.messages)}")
            for i, msg in enumerate(result.messages[-3:]):
                print(f"  [{i}] {type(msg).__name__}: {str(msg.content)[:80]}...")

    except Exception as e:
        print(f"\n❌ Error: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()

    print("\n" + "=" * 60)
    print("🔍 OBSERVATIONS")
    print("=" * 60)
    print("This is the exact pattern from the test suite.")
    print("Let's see if it works with a single agent...")


if __name__ == "__main__":
    print("SimpleAgentV3 Structured Output Test (from test suite)")
    print("=" * 50 + "\n")
    asyncio.run(main())
