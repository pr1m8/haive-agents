#!/usr/bin/env python3
"""Get detailed error information."""

import traceback

# Test self_discover import
print("Testing self_discover import...")
try:
    from haive.agents.reasoning_and_critique.self_discover import SelfDiscoverAgent
    print("✓ self_discover import works")
except Exception as e:
    print("✗ self_discover import failed:")
    traceback.print_exc()

print("\n" + "="*50 + "\n")

# Test ToTAgent import
print("Testing ToTAgent import...")
try:
    from haive.agents.reasoning_and_critique.tot.agent import ToTAgent
    print("✓ ToTAgent import works")
except Exception as e:
    print("✗ ToTAgent import failed:")
    traceback.print_exc()