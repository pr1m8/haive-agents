#!/usr/bin/env python3
"""Trace EXACTLY where and how the Pydantic validation breaks without model_rebuild().

This will show the precise call stack and failure point.
"""

import sys
import traceback
from pathlib import Path

# Direct imports to avoid broken module paths
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))

print("🔍 EXACT FAILURE TRACE - Without model_rebuild()")
print("=" * 60)

print("\n📍 Step 1: Importing modules...")
try:
    print("  → Importing AugLLMConfig...")
    from haive.core.engine.aug_llm import AugLLMConfig
    print("  ✅ AugLLMConfig imported successfully")
    
    print("  → Importing SimpleAgentV3...")
    from haive.agents.simple.agent_v3 import SimpleAgentV3
    print("  ✅ SimpleAgentV3 imported successfully")
    
except Exception as e:
    print(f"  ❌ Import failed: {e}")
    print("\n📚 IMPORT FAILURE STACK TRACE:")
    traceback.print_exc()
    sys.exit(1)

print("\n📍 Step 2: Creating AugLLMConfig...")
try:
    engine = AugLLMConfig(name="test_engine", temperature=0.1)
    print(f"  ✅ Engine created: {engine.name}")
except Exception as e:
    print(f"  ❌ Engine creation failed: {e}")
    print("\n📚 ENGINE CREATION STACK TRACE:")
    traceback.print_exc()
    sys.exit(1)

print("\n📍 Step 3: Attempting SimpleAgentV3 creation...")
print("  → About to call SimpleAgentV3.__init__...")

try:
    # This is where it should break
    agent = SimpleAgentV3(name="test_agent", engine=engine)
    print(f"  ✅ Agent created successfully: {agent.name}")
    print("  🤔 Unexpected success - the error might be fixed by the mixin changes!")
    
except Exception as e:
    print(f"  ❌ Agent creation failed: {e}")
    print(f"  🎯 Error type: {type(e).__name__}")
    
    print("\n📚 EXACT FAILURE STACK TRACE:")
    traceback.print_exc()
    
    print("\n🔬 DETAILED ERROR ANALYSIS:")
    
    # Get the exception details
    exc_type, exc_value, exc_traceback = sys.exc_info()
    
    print(f"Exception Type: {exc_type.__name__}")
    print(f"Exception Message: {exc_value}")
    
    print("\n📋 CALL STACK BREAKDOWN:")
    for i, frame_summary in enumerate(traceback.extract_tb(exc_traceback)):
        filename = Path(frame_summary.filename).name
        print(f"  {i+1:2d}. {filename}:{frame_summary.lineno} in {frame_summary.name}")
        print(f"      → {frame_summary.line}")
    
    print("\n🎯 FAILURE POINT ANALYSIS:")
    if "PydanticUserError" in str(exc_type):
        print("  → This is a Pydantic model definition error")
        print("  → Happens during class construction, not instance creation")
        print("  → Forward reference issue in the class inheritance")
    elif "AttributeError" in str(exc_type):
        print("  → This is a missing attribute error")
        print("  → Happens during instance initialization")
    elif "ValidationError" in str(exc_type):
        print("  → This is a Pydantic validation error")
        print("  → Happens during field validation")
    else:
        print(f"  → Unknown error type: {exc_type}")
    
    print("\n🔧 WHERE EXACTLY IT BREAKS:")
    last_frame = traceback.extract_tb(exc_traceback)[-1]
    print(f"  File: {last_frame.filename}")
    print(f"  Line: {last_frame.lineno}")
    print(f"  Function: {last_frame.name}")
    print(f"  Code: {last_frame.line}")

print(f"\n{'='*60}")
print("🎯 EXACT FAILURE TRACE COMPLETE")
print("💡 This shows the precise point where Pydantic breaks without model_rebuild()")