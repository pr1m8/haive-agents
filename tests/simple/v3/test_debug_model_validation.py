#!/usr/bin/env python3
"""Debug test using Haive tracing utilities to find WHEN the model validation error occurs."""

import sys
import asyncio
from pathlib import Path

# Direct imports to avoid broken module paths
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))

# Import Haive debugging utilities
from haive.core.utils.dev.tracing import trace
from haive.core.utils.dev.debug_decorators import debug_decorators

print("🔧 Importing debugging utilities...")

# Enable tracing for pydantic and haive agents
trace.call_tracker.add_filter("pydantic")
trace.call_tracker.add_filter("SimpleAgentV3")
trace.call_tracker.add_filter("__init__")
trace.call_tracker.add_filter("model_")
trace.call_tracker.enable()

print("✅ Tracing enabled for: pydantic, SimpleAgentV3, __init__, model_*")

try:
    print("🔧 Attempting imports...")
    
    # Trace the import process
    @trace.calls
    def import_haive_components():
        from haive.core.engine.aug_llm import AugLLMConfig
        print("  ✅ AugLLMConfig imported")
        
        from haive.agents.simple.agent_v3 import SimpleAgentV3
        print("  ✅ SimpleAgentV3 imported")
        
        return AugLLMConfig, SimpleAgentV3
    
    AugLLMConfig, SimpleAgentV3 = import_haive_components()
    
except Exception as e:
    print(f"❌ Import failed: {e}")
    trace.stack()
    sys.exit(1)

@trace.calls
@debug_decorators.breakpoint_on_exception
async def test_with_tracing():
    """Test SimpleAgentV3 creation with full tracing."""
    print("\n🧪 Testing SimpleAgentV3 creation with tracing...")
    
    # Step 1: Create AugLLMConfig (trace this)
    print("📍 Step 1: Creating AugLLMConfig...")
    
    @trace.calls
    def create_engine():
        return AugLLMConfig(name="test", temperature=0.1)
    
    engine = create_engine()
    print(f"  ✅ Engine created: {engine.name}")
    
    # Step 2: Create SimpleAgentV3 (this is where error happens)
    print("📍 Step 2: Creating SimpleAgentV3...")
    
    # Add variable tracking
    trace.vars(engine=engine)
    
    @trace.calls
    def create_agent():
        # This is where the error occurs - let's trace it deeply
        print("    🔍 About to call SimpleAgentV3.__init__")
        agent = SimpleAgentV3(name="test_agent", engine=engine)
        print("    ✅ SimpleAgentV3.__init__ completed")
        return agent
    
    try:
        agent = create_agent()
        print(f"  ✅ Agent created: {agent.name}")
        return agent
        
    except Exception as e:
        print(f"  ❌ Agent creation failed: {e}")
        print("\n📊 Call trace up to failure:")
        trace.call_tracker.get_stats()
        
        print("\n📚 Stack trace:")
        trace.stack()
        
        # Re-raise to see full traceback
        raise

async def main():
    """Run debug test."""
    print("🚀 Starting Debug Test with Haive Tracing")
    print("=" * 60)
    
    try:
        agent = await test_with_tracing()
        print(f"\n✅ SUCCESS: Agent created: {agent.name}")
        
    except Exception as e:
        print(f"\n❌ FAILURE: {e}")
        
    finally:
        print("\n📊 Final Statistics:")
        stats = trace.stats()
        
        print("\n📋 Tracing Report:")
        report = trace.report()
        print(report)

if __name__ == "__main__":
    asyncio.run(main())