"""Minimal Sphinx configuration for haive-agents with Furo and AutoAPI."""

import os
import sys
from pathlib import Path

# Add package to path
package_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(package_root / "src"))

# Project information
project = "haive-agents"
copyright = "2025, Haive Team"
author = "Haive Team"

# Extensions - minimal set
extensions = [
    "autoapi.extension",  # Must be first
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
]

# Add pygments style for better code highlighting
pygments_style = "sphinx"
pygments_dark_style = "monokai"

# AutoAPI configuration - hierarchical organization
autoapi_type = "python"
autoapi_dirs = [str(package_root / "src")]
autoapi_add_toctree_entry = True
autoapi_own_page_level = "module"  # Hierarchical organization
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
]

# Keep only imports from haive.agents namespace
autoapi_keep_files = False  # Don't keep generated files after build
autoapi_python_class_content = "class"
autoapi_member_order = "groupwise"

# Add source links to AutoAPI
autoapi_add_objects_to_toctree = True
autoapi_generate_api_docs = True

# Ignore experimental and test files
autoapi_ignore = [
    # Test and archive directories
    "*/archive/*",
    "*/tests/*",
    "*/test_*",
    "*_test.py",
    "*/experiments/*",
    "*/experimental/*",
    # Old and backup files
    "*_old.py",
    "*_backup.py",
    "*.backup",
    # Debug files
    "*/debug/*",
    "*debug*.py",
    # Experimental patterns (loose files that should be organized)
    "*/clean_*",
    "*/example_*",
    "*/simple_test*",
    "*/enhanced_*",
    "*/proper_*",
    "*/dynamic_*",
    "*_standalone.py",
    "*_generic.py",
    # Version suffixes
    "*_v2.py",
    "*_v3.py",
    "*_v4.py",
    "*_original.py",
    # Specific experimental files at root
    "*/agents/agent.py",  # Keep only organized agents
    "*/agents/base.py",  # Use base/ directory instead
    "*/agents/config.py",  # Use proper config location
    "*/agents/utils.py",  # Use utils/ directory
    "*/agents/flare.py",
    "*/agents/hyde.py",
    "*/agents/meta.py",
    "*/agents/routing.py",
    # All the experimental multi-agent files
    "*supervisor*.py",
    "*_multi_agent.py",
    "*_agent_*.py",
    # Specific modules showing at root that should be nested
    "*/hyde/*",
    "*/flare/*",
    "*/pro_search/*",
    "*/document_graders/*",
    "*/query_refinement/*",
    "*/answer_generators/*",
    "*/hallucination_graders/*",
    "*/utils.py",
    "*/models.py",
]

# Theme configuration
html_theme = "furo"
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "titles_only": False,
    "source_repository": "https://github.com/pr1m8/haive-agents",
    "source_branch": "main",
    "source_directory": "docs/source/",
}

# Add furo-intense CSS for dark mode fixes
html_css_files = [
    "css/furo-intense.css",
]

# Basic Sphinx configuration
templates_path = ["_templates"]
exclude_patterns = []
html_static_path = ["_static"]

# Source code links - GitHub repository
html_context = {
    "display_github": True,
    "github_user": "pr1m8",
    "github_repo": "haive-agents",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
    "source_suffix": ".rst",
}

# Add source link configuration for viewcode
viewcode_follow_imported_members = True
viewcode_enable_epub = False

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "langchain": ("https://api.python.langchain.com", None),
    "pydantic": ("https://docs.pydantic.dev", None),
}
