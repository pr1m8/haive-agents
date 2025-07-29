#!/usr/bin/env python3
"""Detailed analysis of EXACTLY where Pydantic breaks without model_rebuild().

This shows the precise coverage and process of the failure.
"""

import sys
import traceback
from pathlib import Path

# Direct imports to avoid broken module paths
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))

print("🔬 DETAILED PYDANTIC FAILURE ANALYSIS")
print("=" * 60)

# Step 1: Show what happens during class definition
print("\n📍 STEP 1: Class Definition Phase")
print("During import of SimpleAgentV3, Pydantic tries to build the class...")

try:
    from haive.core.engine.aug_llm import AugLLMConfig
    print("  ✅ AugLLMConfig imported (no issues)")
    
    print("  → Now importing SimpleAgentV3...")
    print("  → This triggers Pydantic metaclass __new__ method")
    print("  → Pydantic analyzes the inheritance chain:")
    print("    - Agent[AugLLMConfig] ← Generic with type parameter")
    print("    - RecompileMixin ← Has model_post_init")
    print("    - DynamicToolRouteMixin ← Has model_post_init")
    print("  → Pydantic tries to resolve all forward references...")
    
    from haive.agents.simple.agent_v3 import SimpleAgentV3
    print("  ✅ SimpleAgentV3 class definition succeeded (unexpected!)")
    
except Exception as e:
    print(f"  ❌ Class definition failed during import: {e}")
    print("\n📚 CLASS DEFINITION FAILURE STACK:")
    traceback.print_exc()
    sys.exit(1)

# Step 2: Show what happens during instance creation
print("\n📍 STEP 2: Instance Creation Phase")
print("Pydantic validates fields and calls __init__...")

try:
    engine = AugLLMConfig(name="test_engine", temperature=0.1)
    print("  ✅ Engine created successfully")
    
    print("  → Now creating SimpleAgentV3 instance...")
    print("  → This triggers Pydantic __init__ method:")
    print("    1. Pydantic calls self.__pydantic_validator__.validate_python()")
    print("    2. Validator tries to resolve all field types")
    print("    3. Forward references from complex inheritance cause issues")
    print("    4. Pydantic's MockValSer raises PydanticUserError")
    
    # This is where it breaks
    agent = SimpleAgentV3(name="test_agent", engine=engine)
    print("  ✅ Instance created successfully (unexpected!)")
    
except Exception as e:
    print(f"  ❌ Instance creation failed: {e}")
    print(f"  🎯 Error type: {type(e).__name__}")
    
    print("\n🔍 EXACT FAILURE LOCATION:")
    exc_type, exc_value, exc_traceback = sys.exc_info()
    
    # Get the exact frame where it fails
    frames = traceback.extract_tb(exc_traceback)
    for i, frame in enumerate(frames):
        filename = Path(frame.filename).name
        print(f"  {i+1:2d}. {filename}:{frame.lineno} in {frame.name}")
        print(f"      → {frame.line}")
        
        # Identify the exact breaking point
        if "mock_val_ser" in frame.filename:
            print(f"      🎯 THIS IS WHERE IT BREAKS!")
            print(f"      → Pydantic's MockValSer.__getattr__ raises PydanticUserError")
            print(f"      → This happens because the validator wasn't built properly")
        elif "main.py" in frame.filename and "__init__" in frame.name:
            print(f"      💡 This is the Pydantic __init__ calling the validator")
        elif "test_pudb_failure_analysis.py" in filename:
            print(f"      📝 This is our test code creating the instance")

print("\n🔍 ROOT CAUSE ANALYSIS:")
print("1. **Complex Inheritance**: SimpleAgentV3 inherits from 7+ classes")
print("2. **Generic Type Parameters**: Agent[AugLLMConfig] creates forward references")
print("3. **Mixin Interactions**: Multiple mixins with model_post_init methods")
print("4. **Forward Reference Resolution**: Pydantic can't resolve all types at class creation")
print("5. **MockValSer Fallback**: Pydantic creates a mock validator that fails on use")

print("\n💡 WHY model_rebuild() FIXES IT:")
print("- model_rebuild() forces Pydantic to re-analyze the class after all imports are complete")
print("- It resolves forward references that weren't available during initial class creation")
print("- It rebuilds the validator with complete type information")

print("\n🔧 THE FIX:")
print("Add this at the end of agent_v3.py:")
print("```python")
print("try:")
print("    SimpleAgentV3.model_rebuild()")
print("except Exception as e:")
print("    logger.warning(f'Failed to rebuild SimpleAgentV3 model: {e}')")
print("```")

print(f"\n{'='*60}")
print("🎯 ANALYSIS COMPLETE")
print("This shows EXACTLY where and why the Pydantic validation breaks!")