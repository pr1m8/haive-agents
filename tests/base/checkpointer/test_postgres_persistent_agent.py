"""
Updated test for PostgreSQL persistence with correct StateSnapshot handling.

Save as tests/agents/base/checkpointer/test_postgres_persistent_agent.py
"""
import os
import sys
import uuid
import pytest
import time
import logging
import traceback
from typing import Dict, Any, List, Optional, Union

# Set up logging
logging.basicConfig(level=logging.DEBUG, 
                   format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
# Silence noisy loggers
logging.getLogger("matplotlib").setLevel(logging.WARNING)
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
logging.getLogger("matplotlib.backends").setLevel(logging.ERROR)
logging.getLogger("matplotlib.text").setLevel(logging.ERROR)
logging.getLogger("matplotlib.ticker").setLevel(logging.ERROR)
logging.getLogger("matplotlib.figure").setLevel(logging.ERROR)
logging.getLogger("PIL").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("fontTools").setLevel(logging.ERROR)
logging.getLogger("asyncio").setLevel(logging.WARNING)

# Make matplotlib even quieter by setting the rcParams
try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    matplotlib.rcParams['figure.max_open_warning'] = 0  # Disable max figure warning
except ImportError:
    pass

logger = logging.getLogger(__name__)

def print_step(message):
    """Print a clearly visible step header."""
    print("\n" + "="*80)
    print(f"STEP: {message}")
    sys.stdout.flush()

# Add project root to path if needed
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    print(f"Added {project_root} to sys.path")

# Check for PostgreSQL dependencies
try:
    import psycopg
    from psycopg_pool import ConnectionPool
    from langgraph.checkpoint.postgres import PostgresSaver
    from langgraph.checkpoint.memory import MemorySaver
    POSTGRES_AVAILABLE = True
    print("✅ PostgreSQL dependencies available")
except ImportError as e:
    POSTGRES_AVAILABLE = False
    print(f"❌ PostgreSQL dependencies not available: {e}")
    traceback.print_exc()

# Try to import required components
try:
    # First, try to import abc.ABC directly
    try:
        from abc import ABC
        print("✅ Successfully imported ABC from abc module")
    except ImportError as e:
        print(f"❌ Error importing ABC from abc: {e}")
        traceback.print_exc()
    
    # Check Python version to help with debugging
    print(f"Python version: {sys.version}")
    
    # Now try the actual imports
    from haive_agents.simple.agent import SimpleAgentConfig
    from haive_agents.simple.factory import create_simple_agent
    from haive_core.engine.agent.persistence.types import CheckpointerType
    from haive_core.engine.agent.persistence.postgres_config import PostgresCheckpointerConfig
    from haive_core.engine.aug_llm import AugLLMConfig
    
    # Add more diagnostic info
    print("AugLLMConfig Path:", AugLLMConfig.__path__ if hasattr(AugLLMConfig, '__path__') else None)
    print("AugLLMConfig Class:", AugLLMConfig.__class__)
    print("AugLLMConfig File:", AugLLMConfig.__module__)
    print("✅ Required components available")
except ImportError as e:
    print(f"❌ Could not import required components: {e}")
    traceback.print_exc()
    pytest.skip("Required components not available", allow_module_level=True)

# Database connection parameters
DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable"
CONNECTION_KWARGS = {
    "autocommit": True,
    "prepare_threshold": 0,
}

def extract_messages_from_state(state: Any) -> List[Any]:
    """
    Extract messages from a state object, regardless of its type.
    Handles various state object formats.
    
    Args:
        state: The state object returned by agent.run()
        
    Returns:
        A list of messages, or an empty list if none found
    """
    if state is None:
        return []
        
    # Case 1: If it's a dictionary with messages
    if isinstance(state, dict) and "messages" in state:
        return state["messages"]
        
    # Case 2: If it has a channel_values attribute (StateSnapshot)
    if hasattr(state, "channel_values"):
        channel_values = state.channel_values
        if channel_values and "messages" in channel_values:
            return channel_values["messages"]
    
    # Case 3: If it has specific StateSnapshot attributes
    if hasattr(state, "values"):
        values = state.values
        if isinstance(values, dict) and "messages" in values:
            return values["messages"]
    
    # Case 4: Direct attribute check
    if hasattr(state, "messages"):
        return state.messages
        
    # Nothing found
    return []

def extract_message_content(message: Any) -> str:
    """
    Extract content from a message object, regardless of its type.
    
    Args:
        message: A message object
        
    Returns:
        The content as a string
    """
    if message is None:
        return ""
        
    # Case 1: Message has content attribute (LangChain messages)
    if hasattr(message, "content"):
        return str(message.content)
        
    # Case 2: Message is a tuple (type, content)
    if isinstance(message, tuple) and len(message) >= 2:
        return str(message[1])
        
    # Case 3: Message is a dictionary with content
    if isinstance(message, dict) and "content" in message:
        return str(message["content"])
        
    # Default: Convert to string
    return str(message)

def test_postgres_connection():
    """Test direct PostgreSQL connection."""
    print_step("Testing direct PostgreSQL connection")
    
    try:
        print(f"Using connection URI: {DB_URI}")
        with psycopg.connect(DB_URI) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT version()")
                version = cursor.fetchone()[0]
                print(f"✅ Connected to PostgreSQL: {version}")
        assert True, "PostgreSQL connection successful"
    except Exception as e:
        print(f"❌ PostgreSQL connection failed: {e}")
        assert False, f"PostgreSQL connection failed: {e}"

def test_memory_persistence():
    """Test SimpleAgent with MemorySaver persistence."""
    print_step("Testing SimpleAgent with MemorySaver")
    
    try:
        # Create a unique test name and thread ID
        test_name = f"memory_test_{uuid.uuid4().hex[:8]}"
        thread_id = f"memory_thread_{uuid.uuid4().hex[:8]}"
        print(f"Using test name: {test_name}, thread_id: {thread_id}")
        
        # Create a memory checkpointer config
        memory_persistence = {
            "type": CheckpointerType.memory,
            "setup_needed": True
        }
        
        # Create a simple agent with memory persistence
        print("Creating SimpleAgent with memory persistence...")
        agent = create_simple_agent(
            name=test_name,
            system_message="You are a test assistant with memory. Remember what the user tells you.",
            persistence_config=memory_persistence
        )
        
        # Create LangGraph config format with thread_id
        config = {"configurable": {"thread_id": thread_id}}
        print(f"Using config: {config}")
        
        # First message using proper HumanMessage format
        print("Sending first message...")
        from langchain_core.messages import HumanMessage
        
        # Use proper LangGraph message format for input
        input_message = HumanMessage(content="Hello, my name is TestUser.")
        response1 = agent.run({"messages": [input_message]}, config=config)
        
        # Print response info for debugging
        print(f"Response type: {type(response1)}")
        
        # Extract messages
        messages1 = extract_messages_from_state(response1)
        print(f"First response has {len(messages1)} messages")
        
        # Wait briefly between messages
        time.sleep(1)
        
        # Verify state was saved
        try:
            saved_state = agent.app.get_state(config)
            print(f"Saved state exists: {saved_state is not None}")
            if saved_state and hasattr(saved_state, 'values'):
                print(f"Saved state messages count: {len(saved_state.values.get('messages', []))}")
        except Exception as e:
            print(f"Error checking saved state: {e}")
        
        # Second message to test memory - using the SAME config
        print("Sending second message...")
        input_message2 = HumanMessage(content="What's my name?")
        response2 = agent.run({"messages": [input_message2]}, config=config)
        
        # Extract messages from second response
        messages2 = extract_messages_from_state(response2)
        print(f"Second response has {len(messages2)} messages")
        
        # Get the last message's content
        if messages2:
            last_message = messages2[-1]
            content = extract_message_content(last_message)
            print(f"Last message content: {content}")
            
            # Check for evidence of memory in response content
            # We accept either more messages (history retained) or the name in the content
            memory_success = False
            
            # Option 1: More messages than first response (retained history)
            if len(messages2) > len(messages1):
                print("Memory working: second response has more messages than first")
                memory_success = True
                
            # Option 2: Name is mentioned in response (context awareness)
            elif "testuser" in content.lower() or "test user" in content.lower():
                print("Memory working: response mentions the user's name")
                memory_success = True
                
            # Assertion
            assert memory_success, "Memory not working: response doesn't show evidence of persistence"
        else:
            print("No messages found in second response")
            assert False, "No messages in second response"
        
        print("✅ Memory persistence test passed!")
        
    except Exception as e:
        import traceback
        print(f"❌ Test failed: {e}")
        traceback.print_exc()
        assert False, f"Test failed: {e}"

def test_postgres_persistence():
    """Test SimpleAgent with PostgreSQL persistence."""
    print_step("Testing SimpleAgent with PostgreSQL persistence")
    
    if not POSTGRES_AVAILABLE:
        pytest.skip("PostgreSQL dependencies not available")
    
    try:
        # Create a unique test name and thread ID
        test_name = f"postgres_test_{uuid.uuid4().hex[:8]}"
        thread_id = f"postgres_thread_{uuid.uuid4().hex[:8]}"
        print(f"Using test name: {test_name}, thread_id: {thread_id}")
        
        # Create a PostgreSQL checkpointer config
        postgres_persistence = PostgresCheckpointerConfig(
            db_host="localhost",
            db_port=5432,
            db_name="postgres",
            db_user="postgres",
            db_pass="postgres",
            ssl_mode="disable",
            setup_needed=True
        )
        
        # Register thread in advance
        # This is a common pattern - register the thread before creating the agent
        try:
            postgres_persistence.register_thread(thread_id)
            print(f"Pre-registered thread {thread_id} in PostgreSQL")
        except Exception as e:
            print(f"Error pre-registering thread: {e}")
            traceback.print_exc()
        
        # Create agent with PostgreSQL persistence
        print("Creating SimpleAgent with PostgreSQL persistence...")
        agent = create_simple_agent(
            name=test_name,
            system_message="You are a test assistant with memory. Remember what the user tells you.",
            persistence_config=postgres_persistence
        )
        
        # Create LangGraph style config
        config = {"configurable": {"thread_id": thread_id}}
        
        # First message using proper HumanMessage format
        print("Sending first message...")
        from langchain_core.messages import HumanMessage
        
        input_message = HumanMessage(content="Hello, my name is PostgresUser.")
        response1 = agent.run({"messages": [input_message]}, config=config)
        
        # Print response info
        print(f"First response type: {type(response1)}")
        
        # Extract messages
        messages1 = extract_messages_from_state(response1)
        print(f"First response has {len(messages1)} messages")
        if messages1:
            last_message = messages1[-1]
            content = extract_message_content(last_message)
            print(f"First response content: {content}")
        
        # Verify state was saved
        try:
            saved_state = agent.app.get_state(config)
            print(f"Saved state exists: {saved_state is not None}")
            if saved_state and hasattr(saved_state, 'values'):
                print(f"Saved state messages count: {len(saved_state.values.get('messages', []))}")
        except Exception as e:
            print(f"Error checking saved state: {e}")
        
        # Wait briefly between messages
        time.sleep(1)
        
        # Second message - using the same config
        print("Sending second message...")
        input_message2 = HumanMessage(content="What's my name?")
        response2 = agent.run({"messages": [input_message2]}, config=config)
        
        # Extract messages
        messages2 = extract_messages_from_state(response2)
        print(f"Second response has {len(messages2)} messages")
        
        # Get the last message's content
        if messages2:
            last_message = messages2[-1]
            content = extract_message_content(last_message)
            print(f"Last message content: {content}")
            
            # Check for evidence of memory in response content
            # We accept either more messages (history retained) or the name in the content
            memory_success = False
            
            # Option 1: More messages than first response (retained history)
            if len(messages2) > len(messages1):
                print("Memory working: second response has more messages than first")
                memory_success = True
                
            # Option 2: Name is mentioned in response (context awareness)
            elif "postgresuser" in content.lower() or "postgres user" in content.lower():
                print("Memory working: response mentions the user's name")
                memory_success = True
                
            # Assertion
            assert memory_success, "Memory not working: response doesn't show evidence of persistence"
        else:
            print("No messages found in second response")
            assert False, "No messages in second response"
        
        print("✅ PostgreSQL persistence test passed!")
        
    except Exception as e:
        import traceback
        print(f"❌ Test failed: {e}")
        traceback.print_exc()
        assert False, f"Test failed: {e}"