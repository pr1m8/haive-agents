#!/usr/bin/env python3
"""Update remaining imports after React and Multi agent consolidation.

This script updates:
- ReactAgentV3 → ReactAgent
- EnhancedMultiAgentV4 → MultiAgent
"""

import os
import re
import sys
from pathlib import Path


def update_imports_in_project(project_path: str, dry_run: bool = True):
    """Update all imports in the project.

    Args:
        project_path: Path to the haive-agents package
        dry_run: If True, only show what would be changed
    """
    print(
        f"{'DRY RUN' if dry_run else 'EXECUTING'}: Updating imports in {project_path}"
    )

    # Define the transformations
    transformations = [
        # React imports
        (
            "from haive.agents.react.agent_v3 import ReactAgentV3",
            "from haive.agents.react.agent import ReactAgent",
        ),
        (
            "from haive.agents.react import ReactAgentV3",
            "from haive.agents.react import ReactAgent",
        ),
        # Multi imports
        (
            "from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4",
            "from haive.agents.multi.agent import MultiAgent",
        ),
        (
            "from haive.agents.multi import EnhancedMultiAgentV4",
            "from haive.agents.multi import MultiAgent",
        ),
    ]

    # Get all Python files
    python_files = []
    src_path = Path(project_path) / "src"
    for root, dirs, files in os.walk(src_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    print(f"Found {len(python_files)} Python files to process")

    changes_made = 0

    # Process each file
    for file_path in python_files:
        rel_path = os.path.relpath(file_path, project_path)

        try:
            # Read file content
            with open(file_path, "r") as f:
                content = f.read()

            original_content = content

            # Apply import transformations
            for old_import, new_import in transformations:
                if old_import in content:
                    content = content.replace(old_import, new_import)
                    print(f"  {rel_path}: Updated import")

            # Update class usages
            if "ReactAgentV3" in content:
                # Match ReactAgentV3 when used as a class
                content = re.sub(r"\bReactAgentV3\b", "ReactAgent", content)
                print(f"  {rel_path}: Updated ReactAgentV3 class references")

            if "EnhancedMultiAgentV4" in content:
                content = re.sub(r"\bEnhancedMultiAgentV4\b", "MultiAgent", content)
                print(f"  {rel_path}: Updated EnhancedMultiAgentV4 class references")

            # Write back if changed
            if content != original_content:
                changes_made += 1
                if not dry_run:
                    with open(file_path, "w") as f:
                        f.write(content)

        except Exception as e:
            print(f"  ERROR processing {rel_path}: {e}")

    print(
        f"\nTotal files {'that would be' if dry_run else ''} modified: {changes_made}"
    )

    if dry_run and changes_made > 0:
        print("\nRun with --execute to apply these changes")


def main():
    """Main entry point."""
    # Get the haive-agents package path
    script_dir = Path(__file__).parent
    package_path = script_dir.parent

    # Check if this is a dry run
    dry_run = "--execute" not in sys.argv

    # Run the update
    update_imports_in_project(str(package_path), dry_run=dry_run)


if __name__ == "__main__":
    main()
