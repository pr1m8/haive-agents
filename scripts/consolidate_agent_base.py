#!/usr/bin/env python3
"""Safe Agent Base Consolidation Script for haive-agents.

This script consolidates multiple agent base classes into ONE base agent:
- EnhancedAgent → Agent (becomes THE base agent)
- SimpleAgentV3 → SimpleAgent (removes version suffixes)

Safety features:
- Git checkpoints before each operation
- Dry run mode by default
- Compilation validation
- Comprehensive import testing
- Archival of old files (not deletion)"""

import os
import py_compile
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


class AgentBaseConsolidator:
    """Safely consolidates agent base classes with full validation."""

    def __init__(self, dry_run: bool = True):
        """Initialize consolidator with safety features."""
        self.dry_run = dry_run or os.getenv("DRY_RUN", "").lower() in (
            "1",
            "true",
            "yes",
        )
        self.project_root = Path.cwd()
        self.src_root = self.project_root / "src" / "haive" / "agents"
        self.changes_log = []
        self.errors = []

        # Verify we're in the right directory
        if not (self.src_root).exists():
            raise RuntimeError(
                f"Not in haive-agents root! Expected {self.src_root} to exist"
            )

    def log(self, message: str, level: str = "INFO"):
        """Log message with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prefix = "🧪 [DRY RUN]" if self.dry_run else "🚀"
        print(f"{prefix} [{timestamp}] {level}: {message}")
        self.changes_log.append(f"{level}: {message}")

    def create_checkpoint(self, phase: str) -> str:
        """Create a git checkpoint for rollback."""
        checkpoint_name = (
            f"consolidation-{phase}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        )

        if not self.dry_run:
            subprocess.run(["git", "add", "-A"], check=True)
            subprocess.run(["git", "stash", "push", "-m", checkpoint_name], check=True)
            subprocess.run(["git", "stash", "apply"], check=True)

        self.log(f"Created checkpoint: {checkpoint_name}")
        return checkpoint_name

    def create_archive_dir(self, base_path: Path) -> Path:
        """Create archive directory for old files."""
        archive_dir = base_path / "archive"

        if not self.dry_run:
            archive_dir.mkdir(exist_ok=True)

            # Create README in archive
            readme_content = f"""# Archived Agent Files

These files were archived during the agent base consolidation on {datetime.now().strftime('%Y-%m-%d')}.

## Why These Were Archived:
- Consolidating multiple agent base classes into ONE base agent
- Removing version suffixes (V2, V3, etc.)
- Simplifying the agent hierarchy

## Original Files:
- agent.py → Replaced by enhanced_agent.py content
- agent_v2.py → Functionality merged into agent.py
- agent_v3.py → Renamed to agent.py (without V3 suffix)

## Migration Guide:
1. `from haive.agents.base.enhanced_agent import Agent` → `from haive.agents.base.agent import Agent`
2. `SimpleAgentV3` → `SimpleAgent`
3. `SimpleAgentV2` → `SimpleAgent`
"""
            (archive_dir / "README.md").write_text(readme_content)

        self.log(f"Created archive directory: {archive_dir}")
        return archive_dir

    def compile_check(self, file_path: Path) -> bool:
        """Check if a Python file compiles successfully."""
        try:
            py_compile.compile(str(file_path), doraise=True)
            return True
        except py_compile.PyCompileError as e:
            self.errors.append(f"Compilation error in {file_path}: {e}")
            return False

    def validate_imports(self) -> bool:
        """Validate that key imports still work."""
        test_imports = [
            "from haive.agents.base import Agent",
            "from haive.agents.simple import SimpleAgent",
            "from haive.agents.react import ReactAgent",
            "from haive.agents.multi import MultiAgent",
        ]

        for import_stmt in test_imports:
            cmd = ["python", "-c", import_stmt]

            if self.dry_run:
                self.log(f"Would test import: {import_stmt}")
            else:
                result = subprocess.run(
                    cmd, check=False, capture_output=True, text=True
                )
                if result.returncode != 0:
                    self.errors.append(f"Import failed: {import_stmt}\n{result.stderr}")
                    return False
                self.log(f"✅ Import works: {import_stmt}")

        return True

    def phase_1_fix_base_init(self):
        """Fix export conflicts in base/__init__.py."""
        self.log("📋 Phase 1: Fixing base/__init__.py export conflicts", "PHASE")

        init_file = self.src_root / "base" / "__init__.py"

        if not init_file.exists():
            self.errors.append(f"base/__init__.py not found at {init_file}")
            return False

        if self.dry_run:
            self.log("Would update base/__init__.py to remove Agent import conflict")
            self.log("  - Remove: from haive.agents.base.agent import Agent")
            self.log("  - Keep: from haive.agents.base.enhanced_agent import Agent")
            return True

        # Read current content
        content = init_file.read_text()

        # Create backup
        backup_path = init_file.with_suffix(".py.backup")
        shutil.copy(init_file, backup_path)

        # Update imports - remove the conflicting import
        new_content = content.replace(
            "from haive.agents.base.agent import Agent\n",
            "# Removed old Agent import - using enhanced_agent as THE Agent\n",
        )

        # Also update the enhanced import to be THE Agent
        new_content = new_content.replace(
            "from haive.agents.base.enhanced_agent import Agent as EnhancedAgent",
            "from haive.agents.base.enhanced_agent import Agent  # This is now THE base Agent",
        )

        # Remove EnhancedAgent from __all__ since it's now just Agent
        new_content = new_content.replace('"EnhancedAgent",', "")

        init_file.write_text(new_content)
        self.log("✅ Updated base/__init__.py")

        return self.compile_check(init_file)

    def phase_2_fix_simple_init(self):
        """Fix lazy loading mappings in simple/__init__.py."""
        self.log("📋 Phase 2: Fixing simple/__init__.py lazy loading", "PHASE")

        init_file = self.src_root / "simple" / "__init__.py"

        if not init_file.exists():
            self.errors.append(f"simple/__init__.py not found at {init_file}")
            return False

        if self.dry_run:
            self.log("Would update simple/__init__.py lazy loading mappings")
            self.log('  - Change: "SimpleAgent": ("...agent_v2", "SimpleAgentV2")')
            self.log('  - To: "SimpleAgent": ("...agent", "SimpleAgent")')
            self.log("  - Remove SimpleAgentV3 mapping")
            return True

        # Create new content with correct mappings
        new_content = '''# SimpleAgent Package - Ultra-fast lazy loading
"""SimpleAgent package with ultra-optimized import performance.
Achieves sub-3 second import times through comprehensive lazy loading.
"""

import importlib

_SIMPLE_AGENT_IMPORTS = {
    "SimpleAgent": ("haive.agents.simple.agent", "SimpleAgent"),
}


def __getattr__(name: str):
    """Lazy load SimpleAgent classes to avoid import-time overhead."""
    if name in _SIMPLE_AGENT_IMPORTS:
        module_path, class_name = _SIMPLE_AGENT_IMPORTS[name]
        
        # Import module and get class only when accessed
        module = importlib.import_module(module_path)
        agent_class = getattr(module, class_name)
        
        # Cache in globals for subsequent access
        globals()[name] = agent_class
        return agent_class
    
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


__all__ = ["SimpleAgent"]
'''

        # Backup and write
        backup_path = init_file.with_suffix(".py.backup")
        shutil.copy(init_file, backup_path)
        init_file.write_text(new_content)

        self.log("✅ Updated simple/__init__.py")
        return self.compile_check(init_file)

    def phase_3_consolidate_base_agent(self):
        """Move enhanced_agent.py → agent.py (making it THE base agent)."""
        self.log("📋 Phase 3: Consolidating EnhancedAgent → Agent", "PHASE")

        base_dir = self.src_root / "base"
        old_agent = base_dir / "agent.py"
        enhanced_agent = base_dir / "enhanced_agent.py"
        archive_dir = self.create_archive_dir(base_dir)

        if not enhanced_agent.exists():
            self.errors.append(f"enhanced_agent.py not found at {enhanced_agent}")
            return False

        if self.dry_run:
            self.log(
                f"Would archive: {old_agent} → {archive_dir / 'agent_original.py'}"
            )
            self.log(f"Would move: {enhanced_agent} → {old_agent}")
            return True

        # Archive the old agent.py
        if old_agent.exists():
            shutil.move(str(old_agent), str(archive_dir / "agent_original.py"))
            self.log("✅ Archived old agent.py")

        # Move enhanced_agent.py to agent.py
        shutil.move(str(enhanced_agent), str(old_agent))
        self.log("✅ Moved enhanced_agent.py → agent.py")

        return self.compile_check(old_agent)

    def phase_4_consolidate_simple_agent(self):
        """Move agent_v3.py → agent.py (removing version suffix)."""
        self.log("📋 Phase 4: Consolidating SimpleAgentV3 → SimpleAgent", "PHASE")

        simple_dir = self.src_root / "simple"
        old_agent = simple_dir / "agent.py"
        agent_v3 = simple_dir / "agent_v3.py"
        agent_v2 = simple_dir / "agent_v2.py"
        archive_dir = self.create_archive_dir(simple_dir)

        if not agent_v3.exists():
            self.errors.append(f"agent_v3.py not found at {agent_v3}")
            return False

        if self.dry_run:
            self.log(f"Would archive: {agent_v2} → {archive_dir / 'agent_v2.py'}")
            self.log(
                f"Would archive: {old_agent} → {archive_dir / 'agent_original.py'}"
            )
            self.log(f"Would move: {agent_v3} → {old_agent}")
            self.log("Would update class name: SimpleAgentV3 → SimpleAgent")
            return True

        # Archive old versions
        if agent_v2.exists():
            shutil.move(str(agent_v2), str(archive_dir / "agent_v2.py"))
            self.log("✅ Archived agent_v2.py")

        if old_agent.exists():
            shutil.move(str(old_agent), str(archive_dir / "agent_original.py"))
            self.log("✅ Archived old agent.py")

        # Read agent_v3 content and update class name
        content = agent_v3.read_text()
        content = content.replace("class SimpleAgentV3", "class SimpleAgent")
        content = content.replace(
            "SimpleAgentV3", "SimpleAgent"
        )  # Update any self-references

        # Write as the new agent.py
        old_agent.write_text(content)

        # Remove the old v3 file
        agent_v3.unlink()
        self.log("✅ Moved agent_v3.py → agent.py and updated class name")

        return self.compile_check(old_agent)

    def phase_5_validate_all(self):
        """Run comprehensive validation on all changes."""
        self.log("📋 Phase 5: Comprehensive validation", "PHASE")

        # Find all Python files and compile check
        python_files = list(self.src_root.rglob("*.py"))
        failed_files = []

        for py_file in python_files:
            if "archive" in str(py_file):
                continue  # Skip archived files

            if not self.compile_check(py_file):
                failed_files.append(py_file)

        if failed_files:
            self.log(f"❌ {len(failed_files)} files failed compilation", "ERROR")
            return False

        self.log(f"✅ All {len(python_files)} Python files compile successfully")

        # Test imports
        if not self.validate_imports():
            self.log("❌ Import validation failed", "ERROR")
            return False

        self.log("✅ All imports work correctly")
        return True

    def run(self):
        """Execute the complete consolidation process."""
        print("=" * 60)
        print("🔧 AGENT BASE CONSOLIDATION")
        print(f"🧪 Mode: {'DRY RUN' if self.dry_run else 'LIVE EXECUTION'}")
        print(f"📁 Project root: {self.project_root}")
        print("=" * 60)

        phases = [
            ("fix_base_init", self.phase_1_fix_base_init),
            ("fix_simple_init", self.phase_2_fix_simple_init),
            ("consolidate_base", self.phase_3_consolidate_base_agent),
            ("consolidate_simple", self.phase_4_consolidate_simple_agent),
            ("validate", self.phase_5_validate_all),
        ]

        for phase_name, phase_func in phases:
            if not self.dry_run:
                self.create_checkpoint(phase_name)

            try:
                if not phase_func():
                    self.log(f"❌ Phase {phase_name} failed!", "ERROR")
                    self.print_summary()
                    return False
            except Exception as e:
                self.log(f"❌ Exception in phase {phase_name}: {e}", "ERROR")
                self.print_summary()
                return False

        self.print_summary()
        return True

    def print_summary(self):
        """Print consolidation summary."""
        print("\n" + "=" * 60)
        print("📊 CONSOLIDATION SUMMARY")
        print("=" * 60)

        if self.errors:
            print(f"\n❌ Errors ({len(self.errors)}):")
            for error in self.errors:
                print(f"  - {error}")

        print(f"\n📝 Changes log ({len(self.changes_log)} entries):")
        for change in self.changes_log[-10:]:  # Show last 10
            print(f"  - {change}")

        if self.dry_run:
            print("\n🧪 This was a DRY RUN - no actual changes were made")
            print("   To execute for real, run without DRY_RUN=1")
        else:
            print("\n✅ Consolidation completed!")
            print("   Next steps:")
            print("   1. Run: poetry run pytest tests/ -v")
            print("   2. Update remaining imports with rope")
            print("   3. Commit changes")


def main():
    """Main entry point."""
    # Check for dry run mode
    dry_run = os.getenv("DRY_RUN", "1").lower() in ("1", "true", "yes")

    if not dry_run:
        response = input("⚠️  This will modify files! Are you sure? (yes/no): ")
        if response.lower() != "yes":
            print("Aborted.")
            return

    consolidator = AgentBaseConsolidator(dry_run=dry_run)
    success = consolidator.run()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
