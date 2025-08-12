#!/usr/bin/env python3
"""Consolidate Supervisor agent classes.

This script consolidates:
1. SupervisorAgentV2 → SupervisorAgent (make V2 the primary)
2. Archive experimental variants
3. Complete the modular structure
"""

import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Get the package root
PACKAGE_ROOT = Path(__file__).parent.parent
SRC_DIR = PACKAGE_ROOT / "src" / "haive" / "agents"


def create_archive_dir(base_dir: Path, archive_name: str) -> Path:
    """Create archive directory with README."""
    archive_dir = base_dir / "archive" / archive_name
    archive_dir.mkdir(parents=True, exist_ok=True)

    # Create README
    readme_path = archive_dir / "README.md"
    readme_content = f"""# Archived Supervisor Files - {archive_name}

These files were archived during supervisor consolidation on {datetime.now().strftime('%Y-%m-%d')}.

## Why These Were Archived:
- Consolidating supervisor implementations
- Removing experimental variants and version suffixes
- Completing the modular structure

## Migration Guide:
- `SupervisorAgent` now uses the V2 implementation with agent registry
- `DynamicSupervisor` uses the clean implementation
- See CONSOLIDATION_COMPLETE.md for details
"""
    readme_path.write_text(readme_content)
    return archive_dir


def consolidate_supervisor(dry_run: bool = True) -> list[tuple[str, str]]:
    """Consolidate Supervisor agents."""
    print("\n🔄 Consolidating Supervisor Agents...")
    supervisor_dir = SRC_DIR / "supervisor"
    changes = []

    if dry_run:
        print("  [DRY RUN] Would perform:")

    # Create archive directory
    archive_dir = create_archive_dir(supervisor_dir, "supervisor_consolidation")

    # 1. Make agent_v2.py the primary SupervisorAgent
    agent_v2 = supervisor_dir / "agent_v2.py"
    agent_primary = supervisor_dir / "agent.py"

    if agent_v2.exists():
        if not dry_run:
            # Backup current agent.py
            if agent_primary.exists():
                shutil.copy2(agent_primary, archive_dir / "agent_original.py")
                print("  Archived: agent.py → archive/agent_original.py")

            # Move v2 to be the primary
            shutil.copy2(agent_v2, agent_primary)
            print("  Copied: agent_v2.py → agent.py")

            # Archive the v2 file
            shutil.move(str(agent_v2), str(archive_dir / "agent_v2.py"))
            print("  Archived: agent_v2.py")
        else:
            print("    Archive current agent.py")
            print("    Copy agent_v2.py → agent.py")
            print("    Archive agent_v2.py")

        changes.append(("SupervisorAgentV2", "SupervisorAgent"))

    # 2. Archive experimental dynamic variants
    experimental_files = [
        "dynamic_supervisor.py",  # Keep clean_dynamic_supervisor.py as primary
        "dynamic_supervisor_fixed.py",
        "proper_dynamic_supervisor.py",
        "rebuild_dynamic_supervisor.py",
        "enhanced_dynamic_supervisor.py",
        "integrated_supervisor.py",
        "internal_dynamic_supervisor.py",
    ]

    for filename in experimental_files:
        file_path = supervisor_dir / filename
        if file_path.exists():
            if not dry_run:
                shutil.move(str(file_path), str(archive_dir / filename))
                print(f"  Archived: {filename}")
            else:
                print(f"    Archive: {filename}")

    # 3. Clean up files that already exist in subdirectories
    duplicate_files = [
        # Files that exist in both root and subdirectories
        "dynamic_state.py",  # Also in state/
        "routing.py",  # Also in utils/
        "registry.py",  # Also in utils/
    ]

    for filename in duplicate_files:
        file_path = supervisor_dir / filename
        # Check if file exists in a subdirectory
        subdir_locations = [
            supervisor_dir / "state" / filename,
            supervisor_dir / "utils" / filename,
            supervisor_dir / "core" / filename,
        ]

        if file_path.exists() and any(loc.exists() for loc in subdir_locations):
            if not dry_run:
                # Keep the subdirectory version, archive the root version
                shutil.move(str(file_path), str(archive_dir / filename))
                print(f"  Archived duplicate: {filename}")
            else:
                print(f"    Archive duplicate: {filename}")

    # 4. Update __init__.py to use the new structure
    init_file = supervisor_dir / "__init__.py"
    if init_file.exists():
        if not dry_run:
            # Backup current init
            shutil.copy2(init_file, archive_dir / "__init__.py.backup")

            # Read current content
            content = init_file.read_text()

            # Remove commented v2 imports
            lines = content.split("\n")
            new_lines = []
            skip_next = False

            for line in lines:
                if "# V2 imports commented out" in line:
                    skip_next = True
                    continue
                if skip_next and line.strip().startswith("#"):
                    if line.strip() == "# )":
                        skip_next = False
                    continue
                new_lines.append(line)

            content = "\n".join(new_lines)
            init_file.write_text(content)
            print("  Updated: __init__.py")
        else:
            print("    Update: __init__.py")

    return changes


def update_supervisor_imports(dry_run: bool = True) -> None:
    """Update imports to use consolidated supervisors."""
    print("\n📝 Updating Supervisor imports...")

    if dry_run:
        print("  [DRY RUN] Would update imports")
        return

    # Define replacements
    replacements = [
        # Dynamic supervisor variants
        (
            "from haive.agents.supervisor.dynamic_supervisor import DynamicSupervisorAgent",
            "from haive.agents.supervisor.clean_dynamic_supervisor import DynamicSupervisor",
        ),
        (
            "from haive.agents.supervisor.proper_dynamic_supervisor import ProperDynamicSupervisor",
            "from haive.agents.supervisor.clean_dynamic_supervisor import DynamicSupervisor",
        ),
        (
            "from haive.agents.supervisor.rebuild_dynamic_supervisor import RebuildDynamicSupervisor",
            "from haive.agents.supervisor.clean_dynamic_supervisor import DynamicSupervisor",
        ),
    ]

    # Find and update files
    src_path = PACKAGE_ROOT / "src"
    changes_made = 0

    for root, dirs, files in os.walk(src_path):
        # Skip archive directories
        if "archive" in root:
            continue

        for file in files:
            if file.endswith(".py"):
                file_path = Path(root) / file

                try:
                    content = file_path.read_text()
                    original_content = content

                    for old, new in replacements:
                        if old in content:
                            content = content.replace(old, new)
                            rel_path = file_path.relative_to(PACKAGE_ROOT)
                            print(f"  Updated: {rel_path}")

                    if content != original_content:
                        file_path.write_text(content)
                        changes_made += 1

                except Exception as e:
                    print(f"  ERROR: {e}")

    print(f"  Total files updated: {changes_made}")


def main():
    """Main consolidation function."""
    print("=" * 60)
    print("Supervisor Agent Consolidation Script")
    print("=" * 60)

    # Check if this is a dry run
    dry_run = "--execute" not in sys.argv

    if dry_run:
        print("\n⚠️  DRY RUN MODE - No changes will be made")
        print("Run with --execute to apply changes\n")
    else:
        print("\n✅ EXECUTE MODE - Changes will be applied\n")

    # 1. Consolidate Supervisor agents
    changes = consolidate_supervisor(dry_run)

    # 2. Update imports
    update_supervisor_imports(dry_run)

    print("\n" + "=" * 60)
    if dry_run:
        print("DRY RUN COMPLETE - Review the changes above")
        print("Run with --execute to apply these changes")
    else:
        print("SUPERVISOR CONSOLIDATION COMPLETE!")
        print(f"Total consolidations: {len(changes)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
