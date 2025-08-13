#!/usr/bin/env python3
"""Clean up supervisor __init__.py after consolidation."""

import re
from pathlib import Path


def clean_supervisor_init():
    """Clean up the supervisor __init__.py file."""
    init_file = (
        Path(__file__).parent.parent
        / "src"
        / "haive"
        / "agents"
        / "supervisor"
        / "__init__.py"
    )

    if not init_file.exists():
        print("ERROR: __init__.py not found")
        return

    content = init_file.read_text()
    lines = content.split("\n")

    # Track what we're keeping
    cleaned_lines = []
    imports_seen = set()

    # Define what files were archived
    archived_files = {
        "dynamic_supervisor",
        "dynamic_supervisor_fixed",
        "proper_dynamic_supervisor",
        "rebuild_dynamic_supervisor",
        "integrated_supervisor",
        "internal_dynamic_supervisor",
    }

    for line in lines:
        # Skip archived imports
        if any(
            f"from haive.agents.supervisor.{archived} import" in line
            for archived in archived_files
        ):
            continue

        # Clean up DynamicSupervisor imports (keep only one)
        if "from haive.agents.supervisor.clean_dynamic_supervisor import" in line:
            if "clean_dynamic_supervisor" not in imports_seen:
                imports_seen.add("clean_dynamic_supervisor")
                cleaned_lines.append(line)
            else:
                continue  # Skip duplicate

        # Skip imports from archived files in __all__
        elif any(archived in line for archived in archived_files):
            continue
        else:
            cleaned_lines.append(line)

    # Clean up __all__ section
    new_content = "\n".join(cleaned_lines)

    # Remove references to archived classes from __all__
    archived_classes = [
        "DynamicSupervisorAgent",
        "DynamicSupervisorFixed",
        "ProperDynamicSupervisor",
        "RebuildDynamicSupervisor",
        "IntegratedDynamicSupervisor",
        "InternalDynamicSupervisor",
    ]

    for cls in archived_classes:
        new_content = new_content.replace(f'"{cls}",', "")
        new_content = new_content.replace(f'"{cls}"', "")

    # Clean up empty lines and formatting
    new_content = re.sub(r"\n\s*\n\s*\n", "\n\n", new_content)

    # Write back
    init_file.write_text(new_content)
    print("✅ Cleaned supervisor __init__.py")


if __name__ == "__main__":
    clean_supervisor_init()
