#!/usr/bin/env python3
"""Fix common syntax errors in files."""

import os
import re

# Files and their known syntax error lines
fixes = [
    ("src/haive/agents/reflection/structured_output.py", 429),
    ("src/haive/agents/reflection/message_transformer.py", 574),
    ("src/haive/agents/rag/simple/enhanced_v3/agent.py", 522),
    ("src/haive/agents/memory_v2/test_simple_memory_with_deepseek.py", 24),
    ("src/haive/agents/memory_v2/test_react_memory_coordinator.py", 322),
    ("src/haive/agents/memory_v2/test_graph_memory_simple.py", 34),
    ("src/haive/agents/memory_v2/react_memory_coordinator.py", 484),
    ("src/haive/agents/memory_v2/long_term_memory_agent.py", 579),
    ("src/haive/agents/memory_v2/test_simple_memory_agent_fixed.py", 46),
    ("src/haive/agents/memory_v2/test_deepseek_integration.py", 28),
]

# Common pattern: extra quotes and colons in print statements
pattern = re.compile(r'print\("([^"]+)":.*"\)')
replacement = r'print("\1")'

for filepath, line_num in fixes:
    if os.path.exists(filepath):

        with open(filepath) as f:
            lines = f.readlines()

        # Check the specific line
        if line_num <= len(lines):
            line = lines[line_num - 1]

            # Common fixes
            if ':"' in line and "print" in line:
                # Fix print statements with extra :" pattern
                fixed_line = pattern.sub(replacement, line)
                if fixed_line != line:
                    lines[line_num - 1] = fixed_line

                    with open(filepath, "w") as f:
                        f.writelines(lines)
            elif line.count('"') % 2 != 0:
                # Odd number of quotes - likely unterminated string
                pass
