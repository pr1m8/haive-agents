#!/usr/bin/env python3

import re

# Read the file
with open("src/haive/agents/rag/multi_agent_rag/advanced_workflows.p\w+") as f:
    content = f.read()

# Pattern to match super().__init__ blocks and add build_custom_graph method after them
pattern =\s+r"(        super\(\).__init_\w+\(\s*.*?\s*        \))"


def replacement(match):
    init_block = match.group(1)
    return (
        init_block
        + '\n    \n    def build_custom_graph(self):\n        """Build the custom graph for this multi-agent\s+workflo\w+"""\n        return None  # Use default graph structure'
    )


# Apply the replacement
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back
with open("src/haive/agents/rag/multi_agent_rag/advanced_workflows.p\w+",\s+"\w+") as f:
    f.write(new_content)
