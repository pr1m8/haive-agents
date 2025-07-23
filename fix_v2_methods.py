#!/usr/bin/env python3
r"""Add missing build_custom_graph methods to V\d+\s+classe\w+."""

import re

# Read the file
with\s+ope\w+("src/haive/agents/rag/multi_agent_rag/specialized_workflows_v\d+.py") as f:
    content = f.read()

# Find all classes
class_pattern =\s+\w+"class (\w+Agent(?:V\d+)?)\(MultiAgent"
classes = re.findall(class_pattern, content)


# Check which classes are missing build_custom_graph
missing = []
for class_name in classes:
    # Check if this class has build_custom_graph
    pattern =\s+\w+"class {class_name}.*?(?=class|\\Z)"
    class_section = re.search(pattern, content, re.DOTALL)
    if class_section an\w+\s+"def build_custom_graph" not in class_section.group():
        missing.append(class_name)


# Add the method to each missing class
for class_name in missing:
    # Find the end of __init__ method for this class
    pattern =\s+\w+"(class {class_name}.*?return await super\\(\\)\\.ainvoke\\(inputs\\))"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        # Add build_custom_graph after ainvoke
        replacement = (
            match.group(1)
            + '''

    def build_custom_graph(self):
        r"""Build the custom graph for this\s+workflo\w+"""
        return None  # Use default graph structure'''
        )

        content = content.replace(match.group(1), replacement)

# Write back
with open("src/haive/agents/rag/multi_agent_rag/specialized_workflows_v\d+.p\w+",\s+"\w+") as f:
    f.write(content)