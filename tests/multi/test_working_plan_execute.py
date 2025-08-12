#!/usr/bin/env python3
"""Test working plan and execute using current components after fixes."""

import asyncio
from pydantic import BaseModel, Field

from haive.agents.multi.agent import MultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Simple models for the workflow
class Plan(BaseModel):
    """Plan with steps."""
    objective: str = Field(description="The main objective") 
    steps: list[str] = Field(description="List of steps to execute")


class ExecutionReport(BaseModel):
    """Report from execution."""
    completed_steps: list[str] = Field(description="Steps that were completed")
    results: list[str] = Field(description="Results from each step")
    status: str = Field(description="Overall status: success, partial, failed")


class FinalResponse(BaseModel):
    """Final response to user."""
    answer: str = Field(description="The final answer to the user's question")
    summary: str = Field(description="Summary of how the answer was obtained")


def create_working_plan_execute():
    """Create a working plan and execute agent using current fixed components."""
    
    # Planner: ReactAgent for reasoning about the problem
    planner = ReactAgent(
        name="planner",
        engine=AugLLMConfig(
            structured_output_model=Plan,
            temperature=0.7,
            system_message="""You are a strategic planner. Analyze the user's request and create a clear, 
step-by-step plan to accomplish their objective. Break complex tasks into manageable steps."""
        ),
        tools=[]  # Could add research tools here
    )
    
    # Executor: ReactAgent for executing the plan
    executor = ReactAgent(
        name="executor", 
        engine=AugLLMConfig(
            structured_output_model=ExecutionReport,
            temperature=0.3,
            system_message="""You are an executor. Execute the steps from the plan and provide a detailed 
report of what was accomplished and the results obtained."""
        ),
        tools=[]  # Could add execution tools here
    )
    
    # Finalizer: SimpleAgent for creating the final response
    finalizer = SimpleAgent(
        name="finalizer",
        engine=AugLLMConfig(
            structured_output_model=FinalResponse,
            temperature=0.5,
            system_message="""You are a finalizer. Review the execution report and provide a clear, 
comprehensive final answer to the user's original question."""
        )
    )
    
    # Create the multi-agent workflow
    plan_execute_agent = MultiAgent(
        name="plan_execute_workflow",
        agents=[planner, executor, finalizer],
        execution_mode="sequential",  # Planner → Executor → Finalizer
        build_mode="auto"
    )
    
    return plan_execute_agent


def test_plan_execute_creation():
    """Test that the plan execute agent can be created."""
    
    agent = create_working_plan_execute()
    
    print("✅ Working Plan & Execute agent created successfully")
    print(f"   - Type: {type(agent)}")
    print(f"   - Agents: {list(agent.agent_dict.keys())}")
    print(f"   - Execution mode: {agent.execution_mode}")
    print(f"   - Auto-compiled: {hasattr(agent, 'app') and agent.app is not None}")
    
    # Check individual agents
    for agent_name, sub_agent in agent.agent_dict.items():
        print(f"   - {agent_name}: {type(sub_agent).__name__} with {sub_agent.engine.structured_output_model}")
    
    return agent


async def test_plan_execute_execution():
    """Test execution of the plan execute workflow."""
    
    agent = create_working_plan_execute()
    
    # Test with a simple question
    try:
        result = await agent.arun("How do I bake a chocolate cake?")
        
        print(f"\n✅ Plan & Execute executed successfully")
        print(f"   - Result type: {type(result)}")
        
        # Check the structured output
        if hasattr(result, 'answer'):
            print(f"   - Answer: {result.answer[:100]}...")
        if hasattr(result, 'summary'):
            print(f"   - Summary: {result.summary[:100]}...")
            
        return result
        
    except Exception as e:
        print(f"❌ Execution failed: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    # Test creation
    agent = test_plan_execute_creation()
    
    # Test execution
    result = asyncio.run(test_plan_execute_execution())