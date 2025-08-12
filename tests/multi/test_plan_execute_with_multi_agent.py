#!/usr/bin/env python3
"""Test Plan and Execute pattern using current MultiAgent.

This demonstrates the ReactAgent -> SimpleAgent sequential pattern
for plan and execute workflows using the working MultiAgent class.
"""

import asyncio
from typing import Literal

from pydantic import BaseModel, Field

from haive.agents.multi.agent import MultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.tools import calculator_tool


# Simple models for plan and execute
class Plan(BaseModel):
    """A simple plan with steps."""
    
    steps: list[str] = Field(description="List of steps to execute in order")
    objective: str = Field(description="The overall objective of this plan")


class ExecutionResult(BaseModel):
    """Result from executing a step."""
    
    step_completed: str = Field(description="The step that was completed") 
    result: str = Field(description="The result or outcome of this step")
    status: Literal["success", "partial", "failed"] = Field(default="success")


class FinalResponse(BaseModel):
    """Final response to the user."""
    
    response: str = Field(description="The final answer or response to user")
    plan_successful: bool = Field(description="Whether the plan was completed successfully")


def test_simple_plan_execute_sequential():
    """Test simple plan and execute using MultiAgent sequential pattern."""
    
    # Create planner agent (ReactAgent for reasoning about the problem)
    planner = ReactAgent(
        name="planner",
        engine=AugLLMConfig(
            temperature=0.7,
            structured_output_model=Plan,
            system_message="You are a strategic planner. Break down problems into clear, actionable steps."
        ),
        tools=[calculator_tool]  # Planner can use tools for initial analysis
    )
    
    # Create executor agent (SimpleAgent for structured execution)
    executor = SimpleAgent(
        name="executor", 
        engine=AugLLMConfig(
            temperature=0.3,
            structured_output_model=ExecutionResult,
            system_message="You are an executor. Execute the given step and provide clear results."
        )
    )
    
    # Create finalizer agent (SimpleAgent for final response)
    finalizer = SimpleAgent(
        name="finalizer",
        engine=AugLLMConfig(
            temperature=0.5,
            structured_output_model=FinalResponse,
            system_message="You are a finalizer. Review the execution results and provide the final response."
        )
    )
    
    # Create sequential multi-agent workflow
    plan_execute_workflow = MultiAgent(
        name="plan_execute_workflow",
        agents=[planner, executor, finalizer],
        execution_mode="sequential",
        build_mode="auto"  # Build immediately
    )
    
    # Test that it compiles
    assert plan_execute_workflow.compiled, "MultiAgent should auto-compile with build_mode='auto'"
    
    # Test basic properties
    assert len(plan_execute_workflow.agents) == 3
    assert "planner" in plan_execute_workflow.agent_dict
    assert "executor" in plan_execute_workflow.agent_dict
    assert "finalizer" in plan_execute_workflow.agent_dict
    
    print("✅ Plan and Execute MultiAgent created successfully")
    print(f"   - Agents: {list(plan_execute_workflow.agent_dict.keys())}")
    print(f"   - Execution mode: {plan_execute_workflow.execution_mode}")
    print(f"   - Compiled: {plan_execute_workflow.compiled}")
    
    return plan_execute_workflow


async def test_plan_execute_real_execution():
    """Test the plan and execute workflow with real LLM execution."""
    
    workflow = test_simple_plan_execute_sequential()
    
    # Execute with a simple math problem
    result = await workflow.arun("Calculate the compound interest on $1000 at 5% for 10 years")
    
    print(f"\n✅ Plan and Execute executed successfully")
    print(f"   - Result type: {type(result)}")
    
    # Check if we got structured output
    if hasattr(result, 'response'):
        print(f"   - Response: {result.response}")
    if hasattr(result, 'plan_successful'):
        print(f"   - Plan successful: {result.plan_successful}")
    
    return result


if __name__ == "__main__":
    # Test creation
    workflow = test_simple_plan_execute_sequential()
    
    # Test execution
    asyncio.run(test_plan_execute_real_execution())