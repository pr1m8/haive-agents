#!/usr/bin/env python3
"""Minimal test to check if ValidationNodeV2 integration works without broken imports."""

import sys
import asyncio
from pathlib import Path

# Direct imports to avoid broken module paths
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))

try:
    from haive.agents.simple.agent_v3 import SimpleAgentV3
    from haive.core.engine.aug_llm import AugLLMConfig
    print("✅ Direct imports successful")
except ImportError as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)

async def test_basic():
    """Test basic SimpleAgentV3 creation."""
    print("🧪 Testing SimpleAgentV3 basic creation...")
    
    try:
        # Create basic config
        engine = AugLLMConfig(name="test", temperature=0.1)
        print(f"✅ AugLLMConfig created: {engine.name}")
        
        # Create agent
        agent = SimpleAgentV3(name="test_agent", engine=engine)
        print(f"✅ SimpleAgentV3 created: {agent.name}")
        
        # Check properties
        print(f"✅ Has graph: {hasattr(agent, 'graph')}")
        print(f"✅ Has add_tool: {hasattr(agent, 'add_tool')}")
        print(f"✅ Has needs_recompile: {hasattr(agent, 'needs_recompile')}")
        
        return True
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_basic())
    print(f"\n🎯 Test {'PASSED' if success else 'FAILED'}")
    sys.exit(0 if success else 1)