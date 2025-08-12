#!/usr/bin/env python3
"""Update all imports after agent base consolidation using rope.

This script uses the rope refactoring library to update all imports
and usages of the old agent classes to the new consolidated versions.

Transformations:
- from haive.agents.base.enhanced_agent import Agent → from haive.agents.base.agent import Agent
- from haive.agents.simple.agent_v3 import SimpleAgentV3 → from haive.agents.simple.agent import SimpleAgent
- SimpleAgentV3 → SimpleAgent (class usages)
- EnhancedAgent → Agent (if any remaining)
"""

import os
import sys
from pathlib import Path

from rope.base.project import Project


def update_imports_in_project(project_path: str, dry_run: bool = True):
    """Update all imports in the project using rope.

    Args:
        project_path: Path to the haive-agents package
        dry_run: If True, only show what would be changed
    """
    print(
        f"{'DRY RUN' if dry_run else 'EXECUTING'}: Updating imports in {project_path}"
    )

    # Initialize rope project
    project = Project(project_path)

    try:
        # Define the import transformations
        transformations = [
            # Fix enhanced_agent imports
            (
                "from haive.agents.base.enhanced_agent import Agent",
                "from haive.agents.base.agent import Agent",
            ),
            # Fix SimpleAgentV3 imports
            (
                "from haive.agents.simple.agent_v3 import SimpleAgentV3",
                "from haive.agents.simple.agent import SimpleAgent",
            ),
            # Fix any remaining old imports
            (
                "from haive.agents.simple.agent_v2 import SimpleAgentV2",
                "from haive.agents.simple.agent import SimpleAgent",
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
                with open(file_path) as f:
                    content = f.read()

                original_content = content

                # Apply import transformations
                for old_import, new_import in transformations:
                    if old_import in content:
                        content = content.replace(old_import, new_import)
                        print(f"  {rel_path}: Updated import")

                # Update class usages
                if "SimpleAgentV3" in content:
                    # Be careful to only replace class usages, not in strings or comments
                    import re

                    # Match SimpleAgentV3 when it's used as a class (followed by ( or :)
                    content = re.sub(
                        r"\bSimpleAgentV3\b(?=\s*[\(:])", "SimpleAgent", content
                    )
                    # Match SimpleAgentV3 in type hints
                    content = re.sub(
                        r"\bSimpleAgentV3\b(?=\s*[\],])", "SimpleAgent", content
                    )
                    print(f"  {rel_path}: Updated SimpleAgentV3 class references")

                # Update any EnhancedAgent references
                if "EnhancedAgent" in content and "class EnhancedAgent" not in content:
                    content = re.sub(r"\bEnhancedAgent\b", "Agent", content)
                    print(f"  {rel_path}: Updated EnhancedAgent references")

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

    finally:
        project.close()


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
