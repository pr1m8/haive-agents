#!/usr/bin/env python3
"""Test the current plan and execute v2 with fixed MultiAgent."""

import sys
import os

# Add the source directory to Python path to avoid import issues
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from typing import Literal

from pydantic import BaseModel, Field

from haive.agents.multi.agent import MultiAgent
from haive.agents.react.agent import ReactAgent  
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.tools import calculator_tool


# Simple models for plan and execute (copying from v2 but simplified)
class Plan(BaseModel):
    """A plan with list of steps."""
    
    objective: str = Field(description="The main objective")
    steps: list[str] = Field(description="List of steps to execute")


class ExecutionResult(BaseModel):
    """Result from executing a step."""
    
    step_completed: str = Field(description="The step that was completed")
    result: str = Field(description="The result or outcome") 
    step_completed: bool = Field(default=True, description="Whether step was completed")


class FinalResponse(BaseModel):
    """Final response decision."""
    
    action: Literal["continue", "respond"] = Field(description="Whether to continue or respond")
    response: str = Field(description="The response content")


def test_plan_execute_v2_with_current_multi_agent():
    """Test plan and execute using current MultiAgent (sequential mode)."""
    
    # Create planner agent
    planner = SimpleAgent(
        name="planner",
        engine=AugLLMConfig(
            temperature=0.7,
            structured_output_model=Plan,
            system_message="You are a strategic planner. Create clear step-by-step plans."
        )
    )
    
    # Create executor agent  
    executor = ReactAgent(
        name="executor", 
        engine=AugLLMConfig(
            temperature=0.3,
            structured_output_model=ExecutionResult,
            system_message="You are an executor. Execute the given step and provide results."
        ),
        tools=[calculator_tool]
    )
    
    # Create finalizer agent
    finalizer = SimpleAgent(
        name="finalizer",
        engine=AugLLMConfig(
            temperature=0.5,
            structured_output_model=FinalResponse,
            system_message="You are a finalizer. Decide if more work is needed or if you can respond."
        )
    )
    
    # Create MultiAgent workflow
    plan_execute_agent = MultiAgent(
        name="plan_execute_v2",
        agents=[planner, executor, finalizer],
        execution_mode="sequential",  # Sequential: planner -> executor -> finalizer
        build_mode="auto"
    )
    
    # Test basic properties
    print("✅ Plan and Execute V2 agent created successfully")
    print(f"   - Agent type: {type(plan_execute_agent)}")
    print(f"   - Agents: {list(plan_execute_agent.agent_dict.keys())}")
    print(f"   - Execution mode: {plan_execute_agent.execution_mode}")
    print(f"   - Build mode: {plan_execute_agent.build_mode}")
    print(f"   - Compiled: {plan_execute_agent.compiled}")
    print(f"   - State schema: {plan_execute_agent.state_schema}")
    
    # Verify it compiled
    assert plan_execute_agent.compiled, "Should auto-compile with build_mode='auto'"
    
    return plan_execute_agent


async def test_plan_execute_v2_execution():
    """Test execution of the plan and execute workflow."""
    
    agent = test_plan_execute_v2_with_current_multi_agent()
    
    # Test with a simple math problem  
    result = await agent.arun("Calculate the area of a circle with radius 5")
    
    print(f"\n✅ Plan and Execute V2 executed")
    print(f"   - Result type: {type(result)}")
    
    # Check for results
    if hasattr(result, 'response'):
        print(f"   - Response: {result.response}")
    if hasattr(result, 'action'):
        print(f"   - Action: {result.action}")
        
    return result


if __name__ == "__main__":
    import asyncio
    
    # Test creation
    agent = test_plan_execute_v2_with_current_multi_agent()
    
    # Test execution  
    asyncio.run(test_plan_execute_v2_execution())