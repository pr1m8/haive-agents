#!/usr/bin/env python3
"""Test the simple sequential pattern that we got working - ReactAgent → SimpleAgent."""

import asyncio
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Simple models for the sequential workflow
class Plan(BaseModel):
    """Plan with steps."""
    steps: list[str] = Field(description="List of steps to execute")


class FinalResult(BaseModel):
    """Final result."""
    result: str = Field(description="The final answer")


async def test_sequential_react_then_simple():
    """Test the sequential pattern: ReactAgent → SimpleAgent that we got working."""
    
    # Step 1: ReactAgent for planning/reasoning
    planner = ReactAgent(
        name="planner",
        engine=AugLLMConfig(
            structured_output_model=Plan,
            temperature=0.7,
            system_message="Create a step-by-step plan to answer the user's question."
        ),
        tools=[]
    )
    
    # Step 2: SimpleAgent for final structured output
    finalizer = SimpleAgent(
        name="finalizer", 
        engine=AugLLMConfig(
            structured_output_model=FinalResult,
            temperature=0.3,
            system_message="Provide the final answer based on the plan."
        )
    )
    
    print("✅ Sequential agents created")
    print(f"   - Planner: {planner.name} (ReactAgent)")
    print(f"   - Finalizer: {finalizer.name} (SimpleAgent)")
    
    # Execute step 1: Planning
    print("\n🔄 Step 1: Planning...")
    plan_result = await planner.arun("How do I bake a chocolate cake?")
    print(f"   - Plan type: {type(plan_result)}")
    if hasattr(plan_result, 'steps'):
        print(f"   - Steps: {plan_result.steps}")
    
    # Execute step 2: Final answer
    print("\n🔄 Step 2: Final answer...")
    # Pass the plan as context to the finalizer
    final_input = f"Based on this plan: {plan_result}, provide the final answer to: How do I bake a chocolate cake?"
    final_result = await finalizer.arun(final_input)
    print(f"   - Final type: {type(final_result)}")
    if hasattr(final_result, 'result'):
        print(f"   - Result: {final_result.result[:200]}...")
    
    print("\n✅ Sequential execution completed successfully")
    return plan_result, final_result


if __name__ == "__main__":
    # Test the sequential pattern that we know works
    asyncio.run(test_sequential_react_then_simple())