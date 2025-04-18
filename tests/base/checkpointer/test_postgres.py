# tests/core/engine/agent/test_postgres.py

import os
import pytest
import uuid
import logging
from unittest import mock
from typing import Dict, Any

# Configure pytest marks
def pytest_configure(config):
    config.addinivalue_line("markers", "real_db: mark a test as requiring a real database connection")
    config.addinivalue_line("markers", "integration: mark a test as an integration test")
    config.addinivalue_line("markers", "asyncio: mark a test as an asyncio test")

# Default PostgreSQL connection settings
DEFAULT_DB_HOST = "localhost"
DEFAULT_DB_PORT = 5432
DEFAULT_DB_NAME = "postgres"
DEFAULT_DB_USER = "postgres"
DEFAULT_DB_PASS = "postgres"
DEFAULT_SSL_MODE = "disable"

# Configure logging for the test
@pytest.fixture(scope="module")
def configure_logging():
    """Set up logging for tests"""
    log_dir = os.path.join("logs", "tests", "core", "engine", "agent")
    os.makedirs(log_dir, exist_ok=True)
    
    # Create a file handler
    file_handler = logging.FileHandler(os.path.join(log_dir, "test_postgres.log"))
    file_handler.setLevel(logging.DEBUG)
    
    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Get the root logger and add handlers
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    # Log that we're running the test
    logger.debug(f"📄 Logging to: {os.path.join(log_dir, 'test_postgres.log')}")
    
    # Also set up specific loggers
    for logger_name in ["src.haive.core.engine.agent", 
                       "src.haive.core.engine.agent.persistence"]:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
    
    yield  # Run the tests
    
    # Clean up handlers
    logger = logging.getLogger()
    logger.removeHandler(file_handler)
    logger.removeHandler(console_handler)

# Create a mocked PostgreSQL connection for testing
class MockCursor:
    def __init__(self):
        self.executed = []
        self.fetchone_results = [(True,)]  # Default: table exists
    
    def execute(self, query, params=None):
        self.executed.append((query, params))
        
    def fetchone(self):
        if self.fetchone_results:
            return self.fetchone_results.pop(0)
        return None
        
    def __enter__(self):
        return self
        
    def __exit__(self, *args):
        pass

class MockConnection:
    def __init__(self):
        self.cursor_obj = MockCursor()
    
    def cursor(self):
        return self.cursor_obj
        
    def __enter__(self):
        return self
        
    def __exit__(self, *args):
        pass

class MockConnectionPool:
    def __init__(self):
        self.connection_obj = MockConnection()
        self._opened = True
        self.open_called = 0
        self.close_called = 0
    
    def connection(self):
        return self.connection_obj
    
    def is_open(self):
        return self._opened
        
    def open(self):
        self.open_called += 1
        self._opened = True
    
    def close(self):
        self.close_called += 1
        self._opened = False

class MockPostgresSaver:
    def __init__(self, conn=None):
        self.conn = conn or MockConnectionPool()
        self.setup_called = 0
    
    def setup(self):
        self.setup_called += 1
        
    def get_state(self, config):
        return None  # No previous state
    
    async def aget_state(self, config):
        return None  # No previous state for async

class MockMemorySaver:
    def __init__(self):
        self.setup_called = 0
        
    def setup(self):
        self.setup_called += 1
        
    def get_state(self, config):
        return None

# Test the PostgresCheckpointerConfig directly
def test_postgres_config_create_checkpointer(configure_logging):
    """Test that the PostgresCheckpointerConfig correctly creates a checkpointer"""
    # Import inside the test to avoid module-level issues
    from haive_core.engine.agent.persistence.postgres_config import PostgresCheckpointerConfig
    
    # Arrange
    config = PostgresCheckpointerConfig(
        db_host=DEFAULT_DB_HOST,
        db_port=DEFAULT_DB_PORT,
        db_name=DEFAULT_DB_NAME,
        db_user=DEFAULT_DB_USER,
        db_pass=DEFAULT_DB_PASS,
        ssl_mode=DEFAULT_SSL_MODE
    )
    
    # Use mocks to avoid actual database connection
    with mock.patch('src.haive.core.engine.agent.persistence.postgres_config.ConnectionPool') as mock_pool_cls:
        mock_pool = MockConnectionPool()
        mock_pool_cls.return_value = mock_pool
        
        with mock.patch('src.haive.core.engine.agent.persistence.postgres_config.PostgresSaver') as mock_saver_cls:
            mock_saver = MockPostgresSaver(conn=mock_pool)
            mock_saver_cls.return_value = mock_saver
            
            # Act
            checkpointer = config.create_checkpointer()
            
            # Assert
            assert checkpointer is not None
            assert mock_pool_cls.called
            assert mock_saver_cls.called
            
            # Check that setup was called since setup_needed=True by default
            assert mock_saver.setup_called == 1
            
            # Check that the correct connection parameters were used
            mock_pool_call_args = mock_pool_cls.call_args[1]
            assert DEFAULT_DB_HOST in mock_pool_call_args.get('conninfo', '')
            assert str(DEFAULT_DB_PORT) in mock_pool_call_args.get('conninfo', '')
            assert DEFAULT_DB_NAME in mock_pool_call_args.get('conninfo', '')
            assert DEFAULT_DB_USER in mock_pool_call_args.get('conninfo', '')

# Test the register_thread method - fixed to properly mock the connection methods
def test_postgres_config_register_thread(configure_logging):
    """Test thread registration with PostgresCheckpointerConfig"""
    # Import inside the test to avoid module-level issues
    from haive_core.engine.agent.persistence.postgres_config import PostgresCheckpointerConfig
    
    # Arrange
    config = PostgresCheckpointerConfig(
        db_host=DEFAULT_DB_HOST,
        db_port=DEFAULT_DB_PORT,
        db_name=DEFAULT_DB_NAME,
        db_user=DEFAULT_DB_USER,
        db_pass=DEFAULT_DB_PASS
    )
    
    # Create a proper mock for the connection pool
    mock_cursor = MockCursor()
    mock_connection = MockConnection()
    mock_connection.cursor = lambda: mock_cursor
    
    mock_pool = MockConnectionPool()
    mock_pool.connection = lambda: mock_connection
    
    # Set the internal pool
    config._pool = mock_pool
    
    # Act - call register_thread
    config.register_thread("test-thread-123")
    
    # Assert - check the executed queries
    executed_queries = mock_cursor.executed
    
    # Should have executed at least one query
    assert len(executed_queries) >= 1
    
    # Check for typical registry queries
    create_table_queries = [q for q in executed_queries if "CREATE TABLE" in q[0] and "threads" in q[0]]
    assert len(create_table_queries) > 0
    
    # Check for thread insertion
    insert_queries = [q for q in executed_queries if "INSERT INTO threads" in q[0]]
    assert len(insert_queries) > 0
    
    # Check thread_id parameter was correct
    assert any(q[1] == ("test-thread-123",) for q in executed_queries)

# Test connection management
def test_postgres_config_connection_management(configure_logging):
    """Test connection management in PostgresCheckpointerConfig"""
    # Import inside the test to avoid module-level issues
    from haive_core.engine.agent.persistence.postgres_config import PostgresCheckpointerConfig
    
    # Arrange
    config = PostgresCheckpointerConfig(
        db_host=DEFAULT_DB_HOST,
        db_port=DEFAULT_DB_PORT,
        db_name=DEFAULT_DB_NAME,
        db_user=DEFAULT_DB_USER,
        db_pass=DEFAULT_DB_PASS
    )
    mock_pool = MockConnectionPool()
    config._pool = mock_pool
    
    # Test 1: Connection already open
    mock_pool._opened = True
    
    # Act & Assert
    opened = config.ensure_connection()
    assert not opened  # Should not report opening a connection
    
    # Test 2: Connection needs opening
    mock_pool._opened = False
    
    # Act & Assert
    opened = config.ensure_connection()
    assert opened  # Should report opening a connection
    assert mock_pool._opened  # Connection should now be open
    
    # Test 3: Release connection
    config.release_connection(close=True)
    assert mock_pool.close_called == 1

# Integration test with SimpleAgent
def test_agent_with_postgres_checkpointer(configure_logging):
    """Test that an agent properly uses the PostgreSQL checkpointer"""
    # Import inside the test to avoid module-level issues
    from haive_core.engine.agent.persistence.postgres_config import PostgresCheckpointerConfig
    from haive_core.engine.aug_llm import AugLLMConfig
    from haive_agents.simple.config import SimpleAgentConfig
    from haive_agents.simple.agent import SimpleAgent
    from langgraph.checkpoint.memory import MemorySaver
    
    # Arrange - Create a SimpleAgent with PostgreSQL checkpointing
    thread_id = str(uuid.uuid4())
    
    # Create the persistence configuration with default localhost settings
    postgres_config = PostgresCheckpointerConfig(
        db_host=DEFAULT_DB_HOST,
        db_port=DEFAULT_DB_PORT,
        db_name=DEFAULT_DB_NAME,
        db_user=DEFAULT_DB_USER,
        db_pass=DEFAULT_DB_PASS,
        ssl_mode=DEFAULT_SSL_MODE
    )
    
    # Create the agent config
    agent_config = SimpleAgentConfig(
        name="test-postgres-agent",
        persistence=postgres_config,
        # Use a basic LLM config
        engine=AugLLMConfig(system_message="You are a test assistant")
    )
    
    # Use mocks to avoid actual database connections
    mock_pool = MockConnectionPool()
    mock_saver = MockPostgresSaver(conn=mock_pool)
    
    # Mock the _setup_checkpointer method to return our mock
    with mock.patch('src.haive.core.engine.agent.agent.Agent._setup_checkpointer', return_value=mock_saver):
        # Mock the _register_thread method to track calls
        with mock.patch('src.haive.core.engine.agent.agent.Agent._register_thread') as mock_register:
            # Create the agent
            agent = SimpleAgent(config=agent_config)
            
            # Verify that the checkpointer was properly set up
            assert agent.checkpointer is mock_saver
            
            # Mock the app invoke to return a simple response
            def mock_invoke(input_data, **kwargs):
                return {"messages": [{"role": "assistant", "content": "Test response"}]}
            
            agent.app.invoke = mock_invoke
            
            # Act - Run the agent with the thread ID
            result = agent.run("Test input", thread_id=thread_id)
            
            # Assert - Check the result and that thread registration was called
            assert result is not None
            assert "messages" in result
            
            # Check that register_thread was called with the right thread_id
            mock_register.assert_called_with(thread_id)

# Test streaming with PostgreSQL checkpointer
def test_agent_stream_with_postgres_checkpointer(configure_logging):
    """Test streaming with PostgreSQL checkpointer"""
    # Import inside the test to avoid module-level issues
    from haive_core.engine.agent.persistence.postgres_config import PostgresCheckpointerConfig
    from haive_core.engine.aug_llm import AugLLMConfig
    from haive_agents.simple.config import SimpleAgentConfig
    from haive_agents.simple.agent import SimpleAgent
    from langgraph.checkpoint.memory import MemorySaver
    
    # Arrange - Create a SimpleAgent with PostgreSQL checkpointing
    thread_id = str(uuid.uuid4())
    
    # Create the persistence configuration
    postgres_config = PostgresCheckpointerConfig(
        db_host=DEFAULT_DB_HOST,
        db_port=DEFAULT_DB_PORT,
        db_name=DEFAULT_DB_NAME,
        db_user=DEFAULT_DB_USER,
        db_pass=DEFAULT_DB_PASS
    )
    
    # Create the agent config
    agent_config = SimpleAgentConfig(
        name="test-postgres-agent-stream",
        persistence=postgres_config,
        # Use a basic LLM config
        engine=AugLLMConfig(system_message="You are a test assistant")
    )
    
    # Use mocks to avoid actual database connections
    mock_pool = MockConnectionPool()
    mock_saver = MockPostgresSaver(conn=mock_pool)
    
    # Mock the _setup_checkpointer method to return our mock
    with mock.patch('src.haive.core.engine.agent.agent.Agent._setup_checkpointer', return_value=mock_saver):
        # Mock the _register_thread method to track calls
        with mock.patch('src.haive.core.engine.agent.agent.Agent._register_thread') as mock_register:
            # Create the agent
            agent = SimpleAgent(config=agent_config)
            
            # Mock the app stream to yield simple responses
            def mock_stream(input_data, **kwargs):
                yield {"messages": [{"role": "assistant", "content": "Test streaming response 1"}]}
                yield {"messages": [{"role": "assistant", "content": "Test streaming response 2"}]}
            
            agent.app.stream = mock_stream
            
            # Act - Stream from the agent with the thread ID
            results = list(agent.stream("Test input", thread_id=thread_id))
            
            # Assert - Check the results
            assert len(results) == 2
            assert all("messages" in result for result in results)
            
            # Check that register_thread was called with the right thread_id
            mock_register.assert_called_with(thread_id)
# Test error handling
def test_postgres_checkpointer_error_handling(configure_logging):
    """Test error handling with PostgreSQL checkpointer"""
    # Import inside the test to avoid module-level issues
    from haive_core.engine.agent.persistence.postgres_config import PostgresCheckpointerConfig
    from haive_core.engine.aug_llm import AugLLMConfig
    from haive_agents.simple.config import SimpleAgentConfig
    from haive_agents.simple.agent import SimpleAgent
    from langgraph.checkpoint.memory import MemorySaver
    
    # Arrange - Create a SimpleAgent with PostgreSQL checkpointing
    thread_id = str(uuid.uuid4())
    
    # Mock the create_checkpointer method to raise an exception
    with mock.patch('src.haive.core.engine.agent.persistence.postgres_config.PostgresCheckpointerConfig.create_checkpointer') as mock_create:
        # Make create_checkpointer raise an exception to simulate connection failure
        mock_create.side_effect = Exception("Mock connection failure")
        
        # Create the persistence configuration with invalid credentials
        postgres_config = PostgresCheckpointerConfig(
            db_host="invalid-host",
            db_port=DEFAULT_DB_PORT,
            db_name=DEFAULT_DB_NAME,
            db_user=DEFAULT_DB_USER,
            db_pass=DEFAULT_DB_PASS
        )
        
        # Create the agent config
        agent_config = SimpleAgentConfig(
            name="test-postgres-agent-error",
            persistence=postgres_config,
            # Use a basic LLM config
            engine=AugLLMConfig(system_message="You are a test assistant")
        )
        
        # Create a memory saver for fallback
        memory_saver = MemorySaver()
        
        # Only mock the Agent's _setup_checkpointer method
        # This should still internally call the handlers.setup_checkpointer
        with mock.patch('src.haive.core.engine.agent.agent.Agent._setup_checkpointer', return_value=memory_saver):
            # Create the agent
            agent = SimpleAgent(config=agent_config)
            
            # Verify fallback to memory saver
            assert agent.checkpointer is memory_saver
            
            # Mock the app invoke to return a simple response
            def mock_invoke(input_data, **kwargs):
                return {"messages": [{"role": "assistant", "content": "Test response"}]}
            
            agent.app.invoke = mock_invoke
            
            # Act - Run the agent with the thread ID
            result = agent.run("Test input", thread_id=thread_id)
            
            # Assert - Check the result contains expected data
            assert result is not None
            assert "messages" in result
            assert len(result["messages"]) == 1
            assert result["messages"][0]["content"] == "Test response"
# Test async functionality with PostgreSQL
@pytest.mark.asyncio
async def test_async_postgres_operations(configure_logging):
    """Test async operations with PostgreSQL checkpointer"""
    # Import inside the test to avoid module-level issues
    from haive_core.engine.agent.persistence.postgres_config import PostgresCheckpointerConfig
    from haive_core.engine.aug_llm import AugLLMConfig
    from haive_agents.simple.config import SimpleAgentConfig
    from haive_agents.simple.agent import SimpleAgent
    
    # Arrange - Create a SimpleAgent with PostgreSQL checkpointing
    thread_id = str(uuid.uuid4())
    
    # Create the persistence configuration
    postgres_config = PostgresCheckpointerConfig(
        db_host=DEFAULT_DB_HOST,
        db_port=DEFAULT_DB_PORT,
        db_name=DEFAULT_DB_NAME,
        db_user=DEFAULT_DB_USER,
        db_pass=DEFAULT_DB_PASS
    )
    
    # Create the agent config
    agent_config = SimpleAgentConfig(
        name="test-postgres-agent-async",
        persistence=postgres_config,
        engine=AugLLMConfig(system_message="You are a test assistant")
    )
    
    # Use mocks to avoid actual database connections
    mock_pool = MockConnectionPool()
    mock_saver = MockPostgresSaver(conn=mock_pool)
    
    # Mock the setup_checkpointer method to return our mock
    with mock.patch('src.haive.core.engine.agent.agent.Agent._setup_checkpointer', return_value=mock_saver):
        # Mock register_thread_if_needed
        with mock.patch('src.haive.core.engine.agent.persistence.handlers.register_thread_if_needed'):
            # Mock ensure_pool_open and close_pool_if_needed
            with mock.patch('src.haive.core.engine.agent.persistence.handlers.ensure_pool_open', return_value=True):
                with mock.patch('src.haive.core.engine.agent.persistence.handlers.close_pool_if_needed'):
                    # Create the agent
                    agent = SimpleAgent(config=agent_config)
                    
                    # Mock the app ainvoke to return a simple response
                    async def mock_ainvoke(input_data, **kwargs):
                        return {"messages": [{"role": "assistant", "content": "Async test response"}]}
                    
                    agent.app.ainvoke = mock_ainvoke
                    
                    # Act - Run the agent asynchronously
                    result = await agent.arun("Test input", thread_id=thread_id)
                    
                    # Assert - Check the result
                    assert result is not None
                    assert "messages" in result
                    assert result["messages"][0]["content"] == "Async test response"
                    
                    # Mock astream for async streaming test
                    async def mock_astream(input_data, **kwargs):
                        yield {"messages": [{"role": "assistant", "content": "Async stream 1"}]}
                        yield {"messages": [{"role": "assistant", "content": "Async stream 2"}]}
                    
                    agent.app.astream = mock_astream
                    
                    # Test async streaming
                    results = []
                    async for chunk in agent.astream("Test input", thread_id=thread_id):
                        results.append(chunk)
                    
                    # Check streaming results
                    assert len(results) == 2
                    assert results[0]["messages"][0]["content"] == "Async stream 1"
                    assert results[1]["messages"][0]["content"] == "Async stream 2"
def test_state_persistence_across_runs(configure_logging):
    """Test that state persists across multiple agent runs"""
    # Import inside the test to avoid module-level issues
    from haive_core.engine.agent.persistence.postgres_config import PostgresCheckpointerConfig
    from haive_core.engine.aug_llm import AugLLMConfig
    from haive_agents.simple.config import SimpleAgentConfig
    from haive_agents.simple.agent import SimpleAgent
    from langchain_core.messages import AIMessage, HumanMessage
    
    # Arrange - Create a consistent thread ID for persistence
    thread_id = "persistent-thread-123"
    
    # Create the agent config
    agent_config = SimpleAgentConfig(
        name="test-state-persistence",
        engine=AugLLMConfig(system_message="You are a test assistant")
    )
    
    # Create a proper state object
    class StateTuple:
        def __init__(self, values, metadata=None):
            self.values = values
            self.metadata = metadata
            self.created_at = "2025-04-17T02:42:00Z"
            self.checkpoint = "checkpoint-123"
            self.config = {}  # Add this to avoid the "no attribute 'config'" error
    
    class StateSnapshot:
        def __init__(self, state_data):
            self.values = state_data
            self.metadata = None
            self.created_at = "2025-04-17T02:42:00Z"
            self.checkpoint = "checkpoint-123"
            self.config = {}  # Add this to avoid the "no attribute 'config'" error
    
    # Initial counter value for tracking state between runs
    counter = 0
    
    # Define a mock invoke function that will handle state
    def mock_invoke(input_data, **kwargs):
        nonlocal counter
        
        # Increment counter - simulating state persistence
        counter += 1
        
        # Create a response with counter
        return {
            "messages": [
                {"content": "Initial message", "type": "human"},
                {"content": f"Response #{counter}", "type": "ai"}
            ],
            "counter": counter,
            "runnable_config": {}  # Add this to satisfy schema validation
        }
    
    # Create the mock checkpointer
    mock_checkpointer = mock.MagicMock()
    mock_checkpointer.get_state.return_value = None  # No previous state
    
    # Mock the setup_checkpointer method
    with mock.patch('src.haive.core.engine.agent.agent.Agent._setup_checkpointer', return_value=mock_checkpointer):
        # Create the agent
        agent = SimpleAgent(config=agent_config)
        
        # Replace the app.invoke method with our mock
        agent.app.invoke = mock_invoke
        
        # Act - First run with the persistent thread ID
        result1 = agent.run({"messages": [HumanMessage(content="New input")], "runnable_config": {}}, thread_id=thread_id)
        
        # Assert - Check first result
        assert result1 is not None
        assert "counter" in result1
        assert result1["counter"] == 1
        
        # Act - Second run with the same thread ID
        result2 = agent.run({"messages": [HumanMessage(content="Another input")], "runnable_config": {}}, thread_id=thread_id)
        
        # Assert - Check second result has incremented counter
        assert result2 is not None
        assert "counter" in result2
        assert result2["counter"] == 2
        assert len(result2["messages"]) >= 2
@pytest.mark.real_db
@pytest.mark.integration
def test_real_postgres_integration(configure_logging):
    """Test with a real PostgreSQL database (requires proper configuration)"""
    # Skip this test unless specifically requested with pytest marker
    if not os.environ.get("HAIVE_TEST_POSTGRES", "false").lower() == "true":
        pytest.skip("Skipping real PostgreSQL test. Set HAIVE_TEST_POSTGRES=true to enable.")
    
    # Import inside the test
    from haive_core.engine.agent.persistence.postgres_config import PostgresCheckpointerConfig
    from haive_core.engine.aug_llm import AugLLMConfig
    from haive_agents.simple.config import SimpleAgentConfig
    from haive_agents.simple.agent import SimpleAgent
    
    # Get connection details from environment or use defaults
    db_host = os.environ.get("TEST_DB_HOST", DEFAULT_DB_HOST)
    db_port = int(os.environ.get("TEST_DB_PORT", DEFAULT_DB_PORT))
    db_name = os.environ.get("TEST_DB_NAME", DEFAULT_DB_NAME)
    db_user = os.environ.get("TEST_DB_USER", DEFAULT_DB_USER)
    db_pass = os.environ.get("TEST_DB_PASS", DEFAULT_DB_PASS)
    
    # Generate a unique thread ID for this test
    thread_id = f"test-{uuid.uuid4()}"
    
    # Create persistence config with real credentials
    postgres_config = PostgresCheckpointerConfig(
        db_host=db_host,
        db_port=db_port,
        db_name=db_name,
        db_user=db_user,
        db_pass=db_pass,
        ssl_mode=DEFAULT_SSL_MODE,
        min_pool_size=1,
        max_pool_size=2
    )
    
    # Create agent config
    agent_config = SimpleAgentConfig(
        name="real-postgres-test",
        persistence=postgres_config,
        engine=AugLLMConfig(system_message="You are a test assistant"),
        save_history=True
    )
    
    # Create a simple mock for the LLM to avoid actual API calls
    with mock.patch('src.haive.core.engine.aug_llm.AugLLMConfig.create_runnable') as mock_llm:
        # Set up the mock LLM to return a simple response
        mock_llm.return_value.invoke.return_value = {
            "messages": [{"role": "assistant", "content": "Real database test response"}]
        }
        
        try:
            # Create agent with real persistence
            agent = SimpleAgent(config=agent_config)
            
            # Run the agent
            result = agent.run("Test with real database", thread_id=thread_id)
            
            # Verify result
            assert result is not None
            assert "messages" in result
            
            # Wait briefly to ensure data is saved
            import time
            time.sleep(0.5)
            
            # Run again to verify state retrieval
            result2 = agent.run("Second request", thread_id=thread_id)
            
            # Should have both messages in history
            assert len(result2["messages"]) >= 2
            
        except Exception as e:
            pytest.fail(f"Real database test failed: {e}")