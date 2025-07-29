#!/usr/bin/env python3
"""Test problematic imports."""

print("Testing imports...")

# Test 1: DynamicSupervisorAgent
try:
    from haive.agents.experiments.dynamic_supervisor import DynamicSupervisorAgent
    print("✓ DynamicSupervisorAgent import works")
except Exception as e:
    print(f"✗ DynamicSupervisorAgent import failed: {e}")

# Test 2: self_discover module
try:
    from haive.agents.reasoning_and_critique.self_discover import SelfDiscoverAgent
    print("✓ self_discover import works")
except Exception as e:
    print(f"✗ self_discover import failed: {e}")

# Test 3: ToTAgent
try:
    from haive.agents.reasoning_and_critique.tot.agent import ToTAgent
    print("✓ ToTAgent import works")
except Exception as e:
    print(f"✗ ToTAgent import failed: {e}")

print("\nAll import tests completed!")