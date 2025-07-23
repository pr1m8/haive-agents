#!/usr/bin/env python3
"""Test with minimal schema to isolate the issue."""

from haive.core.schema.prebuilt.messages_state import MessagesState
from haive.core.schema.schema_composer import SchemaComposer
from langchain_core.messages import HumanMessage


def test_minimal_schema():
    """Test creating a minimal schema."""
    print("\n" + "=" * 60)
    print("TEST: Minimal Schema Creation")
    print("=" * 60)

    # Test 1: Basic MessagesState
    print("\n1. Testing basic MessagesState...")
    try:
        state = MessagesState()
        print("✅ MessagesState created successfully")
        print(f"   Fields: {list(state.model_dump().keys())}")
    except Exception as e:
        print(f"❌ MessagesState failed: {e}")

    # Test 2: MessagesState with messages
    print("\n2. Testing MessagesState with messages...")
    try:
        state = MessagesState(messages=[HumanMessage(content="test")])
        print("✅ MessagesState with messages created successfully")
    except Exception as e:
        print(f"❌ MessagesState with messages failed: {e}")

    # Test 3: Create schema with SchemaComposer
    print("\n3. Testing SchemaComposer...")
    try:
        composer = SchemaComposer(name="TestSchema")
        # Don't add any fields, just build
        TestSchema = composer.build()
        print(f"✅ Schema built: {TestSchema.__name__}")

        # Try to instantiate
        test_state = TestSchema()
        print("✅ Schema instance created")
    except Exception as e:
        print(f"❌ SchemaComposer failed: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()

    # Test 4: SchemaComposer with base MessagesState
    print("\n4. Testing SchemaComposer with MessagesState base...")
    try:
        from haive.core.schema.state_schema import StateSchema

        # First check if MessagesState works
        print("   Checking MessagesState base...")
        print(
            f"   MessagesState is StateSchema: {issubclass(MessagesState, StateSchema)}"
        )
        print(
            f"   MessagesState MRO: {[c.__name__ for c in MessagesState.__mro__[:5]]}"
        )

        # Now try composer
        composer = SchemaComposer(name="TestSchemaWithBase")
        composer.set_base_class(MessagesState)
        TestSchemaWithBase = composer.build()
        print(f"✅ Schema with base built: {TestSchemaWithBase.__name__}")

        # Try to instantiate
        test_state2 = TestSchemaWithBase()
        print("✅ Schema with base instance created")
        print(f"   Fields: {list(test_state2.model_dump().keys())}")
    except Exception as e:
        print(f"❌ SchemaComposer with base failed: {type(e).__name__}: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_minimal_schema()
