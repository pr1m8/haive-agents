#!/usr/bin/env python3
"""Test Sphinx import handling."""

from pathlib import Path
import sys


# Simulate sphinx import
sys.path.insert(0, str(Path(__file__).parent / "docs/source"))
