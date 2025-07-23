#!/usr/bin/env python3
"""Debug with full traceback to find the error source."""

import asyncio
import sys
import traceback

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.simple.agent_v3 import SimpleAgentV3


async def test_with_traceback():
    """Test with full traceback."""
    print("\n" + "=" * 60)
    print("TRACEBACK DEBUG: SimpleAgent v3 Execution")
    print("=" * 60)

    try:
        # Create config
        config = AugLLMConfig(
            temperature=0.1, max_tokens=50, llm_config=DeepSeekLLMConfig()
        )
        print("\n✅ Step 1: AugLLMConfig created")

        # Create agent
        agent = SimpleAgentV3(
            name="traceback_agent", engine=config, debug=True  # Enable debug
        )
        print("\n✅ Step 2: SimpleAgentV3 created")
        print(f"   - State schema: {agent.state_schema}")
        print(f"   - Input schema: {agent.input_schema}")
        print(f"   - Output schema: {agent.output_schema}")

        # Check if we can create state instance directly
        print("\n🔍 Step 3: Testing state schema instantiation...")
        try:
            # Try creating with empty dict
            state = agent.state_schema()
            print("✅ State created with empty dict")
        except Exception as e:
            print(f"❌ State creation failed: {type(e).__name__}")
            print("\nFull traceback:")
            traceback.print_exc()

        # Try to prepare input
        print("\n🔍 Step 4: Testing input preparation...")
        test_input = "Hello world"
        try:
            prepared = agent._prepare_input(test_input)
            print(f"✅ Input prepared: {type(prepared).__name__}")
            print(f"   Content: {prepared}")
        except Exception as e:
            print(f"❌ Input preparation failed: {type(e).__name__}")
            print("\nFull traceback:")
            traceback.print_exc()

        # Try execution
        print("\n🔍 Step 5: Testing execution...")
        try:
            result = await agent.arun(test_input)
            print("✅ Execution successful!")
            print(f"Response: {result}")
        except Exception as e:
            print(f"\n❌ Execution failed: {type(e).__name__}: {e}")
            print("\n🔍 FULL TRACEBACK:")
            print("=" * 60)
            traceback.print_exc()
            print("=" * 60)

            # Extra debugging - check the actual error location
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print("\n🔍 TRACEBACK ANALYSIS:")
            tb_list = traceback.extract_tb(exc_traceback)
            for i, (filename, line_num, func_name, text) in enumerate(tb_list):
                if "haive" in filename:
                    print(f"\n[{i}] {filename}:{line_num}")
                    print(f"    Function: {func_name}")
                    print(f"    Line: {text}")

            # Check the actual validation error
            if hasattr(e, "errors"):
                print("\n🔍 VALIDATION ERRORS:")
                for error in e.errors():
                    print(f"  - {error}")

            return False

        return True

    except Exception as e:
        print(f"\n❌ Unexpected error: {type(e).__name__}: {e}")
        print("\n🔍 FULL TRACEBACK:")
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(test_with_traceback())
    print(f"\n{'✅ SUCCESS' if success else '❌ FAILED'}")
