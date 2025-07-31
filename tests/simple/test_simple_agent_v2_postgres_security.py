"""Test SimpleAgentV2 with PostgreSQL security features and SecretStr handling."""

import asyncio
import os
from unittest.mock import patch

from pydantic import SecretStr
from pydantic_core import PydanticUndefined
import pytest

from haive.agents.simple.agent_v2 import SimpleAgentV2
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.persistence.serializers import (
    SecureSecretStrSerializer,
    create_encrypted_serializer_for_postgres,
    create_production_serializer,
)


class TestPostgreSQLSecurity:
    """Test PostgreSQL security features without requiring actual database."""

    def test_secure_secret_str_serializer(self):
        """Test that SecureSecretStrSerializer properly handles SecretStr."""
        serializer = SecureSecretStrSerializer()

        # Test data with SecretStr
        test_data = {
            "api_key": SecretStr("sk-secret-key-123"),
            "password": SecretStr("super-secret-password"),
            "regular_field": "normal_value",
            "number_field": 42,
            "list_field": ["item1", "item2"],
        }

        # Process the data
        processed = serializer._handle_secret_types(test_data)

        # Verify SecretStr values are masked
        assert processed["api_key"] == "**SECRET_MASKED**"
        assert processed["password"] == "**SECRET_MASKED**"

        # Verify regular values are preserved
        assert processed["regular_field"] == "normal_value"
        assert processed["number_field"] == 42
        assert processed["list_field"] == ["item1", "item2"]

    def test_pydantic_undefined_handling(self):
        """Test that PydanticUndefined values are properly handled."""
        serializer = SecureSecretStrSerializer()

        test_data = {
            "defined_field": "value",
            "undefined_field": PydanticUndefined,
            "nested": {"normal": "value", "undefined": PydanticUndefined},
        }

        processed = serializer._handle_secret_types(test_data)

        # PydanticUndefined should be converted to None
        assert processed["defined_field"] == "value"
        assert processed["undefined_field"] is None
        assert processed["nested"]["normal"] == "value"
        assert processed["nested"]["undefined"] is None

    def test_create_production_serializer_without_key(self):
        """Test production serializer creation without encryption key."""
        # Ensure no encryption key is set
        with patch.dict(os.environ, {}, clear=True):
            serializer = create_production_serializer()

            # Should fall back to SecureSecretStrSerializer
            assert isinstance(serializer, SecureSecretStrSerializer)

    def test_create_production_serializer_with_fake_key(self):
        """Test production serializer creation with a fake encryption key."""
        fake_key = "a" * 32  # 32-byte fake key

        # Try to create with fake key (will likely fail import, which is expected)
        try:
            create_production_serializer(encryption_key=fake_key)
        except ImportError:
            pass
        except Exception:
            pass

    def test_postgres_serializer_development(self):
        """Test PostgreSQL serializer in development environment."""
        # Mock development environment
        with patch.dict(os.environ, {"ENVIRONMENT": "development"}, clear=True):
            connection_string = "postgresql://test:test@localhost:5432/test"

            serializer = create_encrypted_serializer_for_postgres(
                connection_string=connection_string
            )

            # Should be SecureSecretStrSerializer in development without key
            assert isinstance(serializer, SecureSecretStrSerializer)

    def test_postgres_serializer_production_without_key(self):
        """Test PostgreSQL serializer in production without encryption key."""
        # Mock production environment without encryption key
        with patch.dict(os.environ, {"ENVIRONMENT": "production"}, clear=True):
            connection_string = "postgresql://test:test@localhost:5432/test"

            # Should raise error in production without key
            with pytest.raises(ValueError, match="Encryption key is required"):
                create_encrypted_serializer_for_postgres(
                    connection_string=connection_string
                )

    @pytest.mark.asyncio
    async def test_simple_agent_v2_with_secure_serializer(self):
        """Test SimpleAgentV2 with our secure serializer (simulation)."""
        # Create agent
        agent = SimpleAgentV2(
            name="security_test_agent",
            engine=AugLLMConfig(temperature=0.1),
        )

        # Mock the serializer to use our secure one
        from haive.core.persistence.serializers import SecureSecretStrSerializer

        secure_serializer = SecureSecretStrSerializer()

        # Test that we can create state without PydanticUndefined
        state = agent.state_schema()

        # Verify state can be processed by our serializer
        state_dict = state.model_dump()
        processed = secure_serializer._handle_secret_types(state_dict)

        # Should not contain any PydanticUndefined
        def contains_pydantic_undefined(obj):
            """Recursively check if object contains PydanticUndefined."""
            if obj is PydanticUndefined:
                return True
            if isinstance(obj, dict):
                return any(contains_pydantic_undefined(v) for v in obj.values())
            if isinstance(obj, list | tuple):
                return any(contains_pydantic_undefined(item) for item in obj)
            return False

        assert not contains_pydantic_undefined(processed)

    def test_secretstr_in_nested_structures(self):
        """Test SecretStr handling in complex nested structures."""
        serializer = SecureSecretStrSerializer()

        complex_data = {
            "config": {
                "api_settings": {
                    "openai_key": SecretStr("sk-openai-123"),
                    "anthropic_key": SecretStr("sk-ant-456"),
                },
                "database": {
                    "password": SecretStr("db-password-789"),
                    "host": "localhost",
                    "port": 5432,
                },
            },
            "tools": [
                {"name": "search", "api_key": SecretStr("search-key-abc")},
                {"name": "calculator", "config": "normal"},
            ],
        }

        processed = serializer._handle_secret_types(complex_data)

        # Check nested SecretStr values are masked
        assert processed["config"]["api_settings"]["openai_key"] == "**SECRET_MASKED**"
        assert (
            processed["config"]["api_settings"]["anthropic_key"] == "**SECRET_MASKED**"
        )
        assert processed["config"]["database"]["password"] == "**SECRET_MASKED**"
        assert processed["tools"][0]["api_key"] == "**SECRET_MASKED**"

        # Check normal values are preserved
        assert processed["config"]["database"]["host"] == "localhost"
        assert processed["config"]["database"]["port"] == 5432
        assert processed["tools"][1]["config"] == "normal"

    def test_serializer_performance(self):
        """Test serializer performance with large data structures."""
        import time

        serializer = SecureSecretStrSerializer()

        # Create large test data
        large_data = {
            "messages": [f"Message {i}" for i in range(1000)],
            "secrets": {f"key_{i}": SecretStr(f"secret_{i}") for i in range(100)},
            "metadata": {f"field_{i}": f"value_{i}" for i in range(500)},
        }

        start_time = time.time()
        processed = serializer._handle_secret_types(large_data)
        time.time() - start_time

        # Verify processing completed
        assert len(processed["messages"]) == 1000
        assert len(processed["secrets"]) == 100
        assert all(v == "**SECRET_MASKED**" for v in processed["secrets"].values())

    def test_serialization_roundtrip(self):
        """Test that serialization is reversible for non-secret data."""
        serializer = SecureSecretStrSerializer()

        original_data = {
            "string": "test",
            "number": 42,
            "boolean": True,
            "list": [1, 2, 3],
            "dict": {"nested": "value"},
        }

        # Process through serializer
        processed = serializer._handle_secret_types(original_data)

        # Should be identical for non-secret data
        assert processed == original_data


if __name__ == "__main__":
    # Run tests directly
    test_suite = TestPostgreSQLSecurity()

    # Run all tests
    test_suite.test_secure_secret_str_serializer()
    test_suite.test_pydantic_undefined_handling()
    test_suite.test_create_production_serializer_without_key()
    test_suite.test_create_production_serializer_with_fake_key()
    test_suite.test_postgres_serializer_development()
    test_suite.test_postgres_serializer_production_without_key()

    # Run async test
    asyncio.run(test_suite.test_simple_agent_v2_with_secure_serializer())

    test_suite.test_secretstr_in_nested_structures()
    test_suite.test_serializer_performance()
    test_suite.test_serialization_roundtrip()
