#!/usr/bin/env python3
"""Test SimpleAgentV3 with the new LangGraph ValidationNodeConfigV2."""

import asyncio
import logging
from pydantic import BaseModel, Field
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig

# Set up logging to see what's happening
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SimpleAnalysis(BaseModel):
    """Simple analysis model for testing."""
    topic: str = Field(description="The main topic")
    summary: str = Field(description="Brief summary")
    confidence: float = Field(description="Confidence score 0-1", ge=0.0, le=1.0)

async def test_simple_agent_with_new_validation():
    """Test SimpleAgentV3 with new ValidationNodeConfigV2."""
    
    print("🧪 Testing SimpleAgentV3 with LangGraph ValidationNodeConfigV2...")
    
    try:
        # Create agent with structured output
        agent = SimpleAgentV3(
            name="test_agent",
            engine=AugLLMConfig(
                structured_output_model=SimpleAnalysis,
                structured_output_version="v2",
                temperature=0.7
            ),
            debug=True  # Enable debug for detailed logging
        )
        
        print(f"✅ Agent created: {agent.name}")
        print(f"✅ Engine: {agent.engine}")
        print(f"✅ Structured output model: {agent.structured_output_model}")
        
        # Test the agent
        result = await agent.arun("Analyze the benefits of renewable energy")
        
        print(f"🎯 Agent execution completed!")
        print(f"📊 Result type: {type(result)}")
        print(f"📊 Result: {result}")
        
        # Check if we got structured output
        if isinstance(result, SimpleAnalysis):
            print("✅ SUCCESS: Got structured output!")
            print(f"  Topic: {result.topic}")
            print(f"  Summary: {result.summary}")
            print(f"  Confidence: {result.confidence}")
        else:
            print(f"⚠️ Result is not SimpleAnalysis instance: {type(result)}")
            print(f"  Content: {result}")
            
        return True
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        logger.exception("Test failed with exception")
        return False

if __name__ == "__main__":
    print("🚀 Starting ValidationNodeConfigV2 test...")
    success = asyncio.run(test_simple_agent_with_new_validation())
    
    if success:
        print("\n✅ Test completed successfully!")
    else:
        print("\n❌ Test failed!")