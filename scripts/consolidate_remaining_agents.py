#!/usr/bin/env python3
"""Consolidate remaining agent classes: React, Multi, and Supervisor.

This script consolidates:
1. ReactAgentV3 → ReactAgent (make V3 the primary)
2. EnhancedMultiAgentV4 → MultiAgent (make V4 the primary)
3. Clean up Supervisor exports (already done in __init__.py)

Similar to the base agent consolidation, we:
- Archive old versions
- Update imports
- Rename classes to remove version suffixes
"""

import shutil
import subprocess
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
    readme_content = f"""# Archived Agent Files - {archive_name}

These files were archived during agent consolidation on {datetime.now().strftime('%Y-%m-%d')}.

## Why These Were Archived:
- Consolidating versioned agents to remove version suffixes
- Making V3/V4 versions the primary implementations
- Simplifying the agent hierarchy

## Migration Guide:
- See CONSOLIDATION_COMPLETE.md in the parent directory
"""
    readme_path.write_text(readme_content)
    return archive_dir


def archive_file(file_path: Path, archive_dir: Path) -> bool:
    """Archive a file to the archive directory."""
    if file_path.exists():
        dest = archive_dir / file_path.name
        shutil.copy2(file_path, dest)
        print(f"  Archived: {file_path.name}")
        return True
    return False


def consolidate_react_agents(dry_run: bool = True) -> list[tuple[str, str]]:
    """Consolidate ReactAgent versions."""
    print("\n🔄 Consolidating React Agents...")
    react_dir = SRC_DIR / "react"
    changes = []

    if dry_run:
        print("  [DRY RUN] Would perform:")

    # Create archive directory
    archive_dir = create_archive_dir(react_dir, "react_consolidation")

    # Archive old files
    old_files = [
        "agent.py",  # Original ReactAgent
        "agent.v2.py",
        "agent_v3.v2.py",
        "agent_v4.py",
        "enhanced_agent_v3.py",
        "enhanced_agent_v3.v2.py",
        "enhanced_react_agent.py",
        "enhanced_react_agent.v2.py",
    ]

    for old_file in old_files:
        file_path = react_dir / old_file
        if file_path.exists():
            if not dry_run:
                archive_file(file_path, archive_dir)
                file_path.unlink()
            else:
                print(f"    Archive and remove: {old_file}")

    # Move agent_v3.py → agent.py (make V3 the primary)
    agent_v3 = react_dir / "agent_v3.py"
    agent_new = react_dir / "agent.py"

    if agent_v3.exists():
        if not dry_run:
            # Backup current agent.py first if it exists
            if agent_new.exists():
                archive_file(agent_new, archive_dir)
            # Move V3 to be the new agent.py
            shutil.move(str(agent_v3), str(agent_new))
            print("  Moved: agent_v3.py → agent.py")

            # Update the class name in the file
            content = agent_new.read_text()
            content = content.replace("class ReactAgentV3", "class ReactAgent")
            content = content.replace("ReactAgentV3", "ReactAgent")  # Update references
            agent_new.write_text(content)
            print("  Updated: ReactAgentV3 → ReactAgent class name")
        else:
            print("    Move: agent_v3.py → agent.py")
            print("    Rename: ReactAgentV3 → ReactAgent")

        changes.append(("ReactAgentV3", "ReactAgent"))

    # Update __init__.py
    init_file = react_dir / "__init__.py"
    if init_file.exists():
        if not dry_run:
            content = init_file.read_text()
            # Remove V3 imports
            content = content.replace(
                "from haive.agents.react.agent_v3 import ReactAgentV3, create_react_agent, create_research_agent",
                "from haive.agents.react.agent import ReactAgent, create_react_agent, create_research_agent",
            )
            # Remove ReactAgentV3 from exports
            content = content.replace('"ReactAgentV3"', "")
            content = content.replace(", , ", ", ")  # Clean up double commas
            init_file.write_text(content)
            print("  Updated: __init__.py exports")
        else:
            print("    Update: __init__.py exports")

    return changes


def consolidate_multi_agents(dry_run: bool = True) -> list[tuple[str, str]]:
    """Consolidate MultiAgent versions."""
    print("\n🔄 Consolidating Multi Agents...")
    multi_dir = SRC_DIR / "multi"
    changes = []

    if dry_run:
        print("  [DRY RUN] Would perform:")

    # Create archive directory
    archive_dir = create_archive_dir(multi_dir, "multi_consolidation")

    # Archive old files
    old_files = [
        "agent.py",  # Old MultiAgent
        "multi_agent.py",
        "multi_agent_v4.py",
        "enhanced_multi_agent_v3.py",
        "clean.py",  # Current basic MultiAgent
    ]

    for old_file in old_files:
        file_path = multi_dir / old_file
        if file_path.exists():
            if not dry_run:
                archive_file(file_path, archive_dir)
                if old_file != "enhanced_multi_agent_v4.py":  # Don't remove V4 yet
                    file_path.unlink()
            else:
                print(f"    Archive: {old_file}")

    # Move enhanced_multi_agent_v4.py → agent.py (make V4 the primary)
    agent_v4 = multi_dir / "enhanced_multi_agent_v4.py"
    agent_new = multi_dir / "agent.py"

    if agent_v4.exists():
        if not dry_run:
            # Move V4 to be the new agent.py
            shutil.move(str(agent_v4), str(agent_new))
            print("  Moved: enhanced_multi_agent_v4.py → agent.py")

            # Update the class name in the file
            content = agent_new.read_text()
            content = content.replace("class EnhancedMultiAgentV4", "class MultiAgent")
            content = content.replace(
                "EnhancedMultiAgentV4", "MultiAgent"
            )  # Update references
            agent_new.write_text(content)
            print("  Updated: EnhancedMultiAgentV4 → MultiAgent class name")
        else:
            print("    Move: enhanced_multi_agent_v4.py → agent.py")
            print("    Rename: EnhancedMultiAgentV4 → MultiAgent")

        changes.append(("EnhancedMultiAgentV4", "MultiAgent"))

    # Update __init__.py
    init_file = multi_dir / "__init__.py"
    if init_file.exists():
        if not dry_run:
            content = init_file.read_text()
            # Update import
            content = content.replace(
                "from haive.agents.multi.clean import MultiAgent",
                "from haive.agents.multi.agent import MultiAgent",
            )
            init_file.write_text(content)
            print("  Updated: __init__.py imports")
        else:
            print("    Update: __init__.py imports")

    return changes


def update_all_imports(changes: list[tuple[str, str]], dry_run: bool = True) -> None:
    """Update all imports using the consolidated classes."""
    print("\n📝 Updating imports across the codebase...")

    if dry_run:
        print("  [DRY RUN] Would update:")
        for old, new in changes:
            print(f"    {old} → {new}")
        return

    # Use the import update script
    update_script = PACKAGE_ROOT / "scripts" / "update_imports_with_rope.py"
    if update_script.exists():
        print("  Using rope to update imports...")
        subprocess.run([sys.executable, str(update_script), "--execute"], check=False)
    else:
        print("  Warning: Import update script not found")


def main():
    """Main consolidation function."""
    print("=" * 60)
    print("Agent Consolidation Script - React, Multi, Supervisor")
    print("=" * 60)

    # Check if this is a dry run
    dry_run = "--execute" not in sys.argv

    if dry_run:
        print("\n⚠️  DRY RUN MODE - No changes will be made")
        print("Run with --execute to apply changes\n")
    else:
        print("\n✅ EXECUTE MODE - Changes will be applied\n")

    # Collect all changes
    all_changes = []

    # 1. Consolidate React agents
    react_changes = consolidate_react_agents(dry_run)
    all_changes.extend(react_changes)

    # 2. Consolidate Multi agents
    multi_changes = consolidate_multi_agents(dry_run)
    all_changes.extend(multi_changes)

    # 3. Supervisor already fixed in __init__.py
    print("\n✅ Supervisor duplicate imports already fixed")

    # 4. Update all imports
    if all_changes:
        update_all_imports(all_changes, dry_run)

    print("\n" + "=" * 60)
    if dry_run:
        print("DRY RUN COMPLETE - Review the changes above")
        print("Run with --execute to apply these changes")
    else:
        print("CONSOLIDATION COMPLETE!")
        print(f"Total changes applied: {len(all_changes)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
