#!/usr/bin/env python3
"""Fix old multi-agent imports after consolidation."""

import os
import sys
from pathlib import Path


def fix_imports(dry_run: bool = True):
    """Fix old multi-agent imports."""
    package_root = Path(__file__).parent.parent
    src_dir = package_root / "src"

    # Define replacements
    replacements = [
        (
            "from haive.agents.multi.clean import MultiAgent",
            "from haive.agents.multi.agent import MultiAgent",
        ),
        (
            "from haive.agents.multi.multi_agent import MultiAgent",
            "from haive.agents.multi.agent import MultiAgent",
        ),
    ]

    print(f"{'DRY RUN' if dry_run else 'EXECUTING'}: Fixing old multi-agent imports")

    # Find all Python files
    python_files = []
    for root, dirs, files in os.walk(src_dir):
        # Skip archive directories
        if "archive" in root:
            continue
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    changes_made = 0

    for file_path in python_files:
        try:
            with open(file_path, "r") as f:
                content = f.read()

            original_content = content

            # Apply replacements
            for old, new in replacements:
                if old in content:
                    content = content.replace(old, new)
                    rel_path = os.path.relpath(file_path, package_root)
                    print(f"  {rel_path}: Fixed import")

            # Write back if changed
            if content != original_content:
                changes_made += 1
                if not dry_run:
                    with open(file_path, "w") as f:
                        f.write(content)

        except Exception as e:
            print(f"  ERROR: {e}")

    print(
        f"\nTotal files {'that would be' if dry_run else ''} modified: {changes_made}"
    )

    if dry_run and changes_made > 0:
        print("\nRun with --execute to apply changes")


def main():
    dry_run = "--execute" not in sys.argv
    fix_imports(dry_run)


if __name__ == "__main__":
    main()
