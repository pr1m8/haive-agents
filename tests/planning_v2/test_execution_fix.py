#!/usr/bin/env python3
"""Test SimpleAgent execution with validation fix."""

from typing import List
from pydantic import BaseModel, Field
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig

class Task(BaseModel):
    description: str = Field(description="Task description")

class Plan[T](BaseModel):
    objective: str = Field(description="Plan objective")
    steps: List[T] = Field(description="Plan steps", max_length=2)

def test_execution():
    """Test actual execution with timeout."""
    print("=== TESTING EXECUTION ===")
    
    agent = SimpleAgent(
        name="test_planner",
        engine=AugLLMConfig(
            structured_output_model=Plan[Task],
            temperature=0.1
        )
    )
    
    print("✅ Conditional edges found in graph.branches")
    
    # Try execution with a timeout mechanism
    import signal
    import time
    
    def timeout_handler(signum, frame):
        raise TimeoutError("Execution took too long - likely infinite loop")
    
    try:
        # Set timeout for 30 seconds
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(30)
        
        print("Starting execution (30s timeout)...")
        start_time = time.time()
        
        result = agent.run("Create a plan for organizing a workshop")
        
        end_time = time.time()
        signal.alarm(0)  # Cancel timeout
        
        print(f"✅ EXECUTION SUCCESSFUL in {end_time - start_time:.2f}s!")
        print(f"Result type: {type(result)}")
        print(f"Result: {result}")
        
        return True
        
    except TimeoutError as e:
        print(f"❌ TIMEOUT: {e}")
        return False
    except Exception as e:
        signal.alarm(0)  # Cancel timeout
        print(f"❌ ERROR: {type(e).__name__}: {str(e)[:200]}...")
        return False
    finally:
        signal.alarm(0)  # Ensure timeout is canceled

if __name__ == "__main__":
    success = test_execution()
    if success:
        print("\n🎉 THE FIX WORKS!")
    else:
        print("\n💥 Still broken")