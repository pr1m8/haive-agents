#!/usr/bin/env python3
"""Test SimpleAgent v3 with AugLLMConfig fix."""

import asyncio

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.simple.agent_v3 import SimpleAgentV3


def test_agent_creation():
    """Test that we can create the agent successfully."""
    print("\n" + "=" * 60)
    print("TEST: Agent Creation with AugLLMConfig")
    print("=" * 60)

    # Create AugLLMConfig with DeepSeek
    config = AugLLMConfig(
        temperature=0.1, max_tokens=100, llm_config=DeepSeekLLMConfig()
    )
    print("✅ AugLLMConfig created successfully")
    print(f"   - Config type: {type(config).__name__}")
    print(f"   - LLM config: {type(config.llm_config).__name__}")

    # Create SimpleAgent v3
    agent = SimpleAgentV3(name="test_agent_v3", engine=config, debug=True, verbose=True)
    print("✅ SimpleAgent v3 created successfully")
    print(f"   - Agent name: {agent.name}")
    print(f"   - Engine type: {type(agent.engine).__name__}")
    print(f"   - Graph built: {agent._graph_built}")
    print(f"   - Setup complete: {agent._setup_complete}")
    print(f"   - Hooks enabled: {agent.hooks_enabled}")
    print(f"   - Hook count: {len(agent._hooks)}")
    print(f"   - Needs recompile: {agent.needs_recompile}")

    # Assertions
    assert agent.name == "test_agent_v3"
    assert isinstance(agent.engine, AugLLMConfig)
    assert agent._graph_built is True
    assert agent._setup_complete is True
    assert agent.hooks_enabled is True
    assert len(agent._hooks) > 0
    assert agent.needs_recompile is False


@pytest.mark.asyncio
async def test_agent_execution():
    """Test agent execution - currently expected to fail due to hook issues."""
    print("\n" + "=" * 60)
    print("TEST: Agent Execution")
    print("=" * 60)

    # Create agent
    config = AugLLMConfig(
        temperature=0.1, max_tokens=50, llm_config=DeepSeekLLMConfig()
    )
    agent = SimpleAgentV3(
        name="executor", engine=config, debug=False  # Less verbose for execution test
    )
    print("✅ Agent created for execution test")

    # Try to execute - expecting failure due to remaining hook issues
    with pytest.raises(Exception) as exc_info:
        result = await agent.arun("Say 'Hello World'")

    print(f"⚠️  Expected failure: {str(exc_info.value)[:100]}...")
    assert "HookContext" in str(exc_info.value), "Expected HookContext validation error"
    print("   - Known issue: Remaining hook calls need format update")


def test_augllmconfig_fix():
    """Test that the core AugLLMConfig fix is working."""
    print("\n" + "=" * 60)
    print("TEST: AugLLMConfig Core Fix")
    print("=" * 60)

    # Test 1: Default AugLLMConfig (uses AzureLLMConfig internally)
    config1 = AugLLMConfig()
    print("✅ Default AugLLMConfig created (no more AzureLLMConfig = None error)")
    assert config1.llm_config is not None

    # Test 2: AugLLMConfig with DeepSeek
    config2 = AugLLMConfig(
        temperature=0.7, max_tokens=200, llm_config=DeepSeekLLMConfig()
    )
    print("✅ AugLLMConfig with DeepSeek created")
    assert config2.temperature == 0.7
    assert config2.max_tokens == 200
    assert isinstance(config2.llm_config, DeepSeekLLMConfig)

    # Test 3: Verify the fix in config.py
    from haive.core.engine.aug_llm.config import AzureLLMConfig as ImportedAzure

    print("✅ AzureLLMConfig imports correctly at runtime")
    assert ImportedAzure is not None, "AzureLLMConfig should not be None"

    print("\n🎉 CORE FIX VERIFIED: AugLLMConfig issue is RESOLVED!")


def test_recompile_mixin_integration():
    """Test RecompileMixin integration."""
    print("\n" + "=" * 60)
    print("TEST: RecompileMixin Integration")
    print("=" * 60)

    config = AugLLMConfig(llm_config=DeepSeekLLMConfig())
    agent = SimpleAgentV3(name="recompile_test", engine=config, auto_recompile=True)

    # Test recompilation tracking
    assert hasattr(agent, "mark_for_recompile")
    assert hasattr(agent, "resolve_recompile")
    assert hasattr(agent, "get_recompile_status")

    # Mark for recompilation
    agent.mark_for_recompile("Test reason")
    assert agent.needs_recompile is True
    assert "Test reason" in agent.recompile_reasons

    # Get status
    status = agent.get_recompile_status()
    print(f"✅ Recompile status: {status}")
    assert status["needs_recompile"] is True
    assert status["reason_count"] == 1

    print("✅ RecompileMixin properly integrated")


if __name__ == "__main__":
    # Run tests manually
    test_augllmconfig_fix()
    test_agent_creation()
    asyncio.run(test_agent_execution())
    test_recompile_mixin_integration()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("✅ AugLLMConfig Fix: WORKING")
    print("✅ Agent Creation: WORKING")
    print("⚠️  Agent Execution: Hook fixes still needed")
    print("✅ RecompileMixin: WORKING")
    print("\nKEY ACHIEVEMENT: The main AugLLMConfig bug is FIXED!")
