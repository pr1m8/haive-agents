#!/usr/bin/env python3
"""Test with minimal schema to isolate the issue."""

import contextlib

from langchain_core.messages import HumanMessage

from haive.core.schema.prebuilt.messages_state import MessagesState
from haive.core.schema.schema_composer import SchemaComposer


def test_minimal_schema():
    """Test creating a minimal schema."""
    # Test 1: Basic MessagesState
    with contextlib.suppress(Exception):
        MessagesState()

    # Test 2: MessagesState with messages
    with contextlib.suppress(Exception):
        MessagesState(messages=[HumanMessage(content="test")])

    # Test 3: Create schema with SchemaComposer
    try:
        composer = SchemaComposer(name="TestSchema")
        # Don't add any fields, just build
        TestSchema = composer.build()

        # Try to instantiate
        TestSchema()
    except Exception:
        import traceback

        traceback.print_exc()

    # Test 4: SchemaComposer with base MessagesState
    try:

        # First check if MessagesState works

        # Now try composer
        composer = SchemaComposer(name="TestSchemaWithBase")
        composer.set_base_class(MessagesState)
        TestSchemaWithBase = composer.build()

        # Try to instantiate
        TestSchemaWithBase()
    except Exception:
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_minimal_schema()
