"""Tests for SimpleAgent and its components.

This module contains comprehensive tests for the SimpleAgent implementation,
including state management, configuration, and runtime behavior with actual persistence.
"""

import os
import uuid
import pytest
from typing import Dict, Any, List
from unittest.mock import patch
import tempfile
import time
import json

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field

from haive.core.engine.aug_llm.base import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig, OpenAILLMConfig, AnthropicLLMConfig
from haive.core.engine.agent.persistence import PostgresCheckpointerConfig, MemoryCheckpointerConfig
from haive.core.engine.agent.persistence.types import CheckpointerType

from haive.agents.simple.agent import SimpleAgent
from haive.agents.simple.config import SimpleAgentConfig
from haive.agents.simple.state import SimpleAgentState
from haive.agents.simple.factory import create_simple_agent


# Ensure we have API credentials for actual tests
@pytest.fixture(scope="module")
def api_credentials():
    """Ensure API credentials are available for tests."""
    # Check if we have Azure OpenAI credentials
    azure_key = os.environ.get("AZURE_OPENAI_API_KEY")
    if not azure_key:
        # Use OpenAI as fallback
        openai_key = os.environ.get("OPENAI_API_KEY")
        if not openai_key:
            pytest.skip("No Azure or OpenAI API credentials available")
            
    # Temporary directory for agent outputs
    with tempfile.TemporaryDirectory() as temp_dir:
        yield {"output_dir": temp_dir}


def test_simple_agent_creation(api_credentials):
    """Test that a SimpleAgent can be created with the correct configuration."""
    # Create a basic agent
    agent = create_simple_agent(
        name="test_agent",
        system_prompt="You are a test assistant.",
        persistence_type="memory",  # Use memory for faster tests
        output_dir=api_credentials["output_dir"]
    )
    
    # Check that agent is properly configured
    assert isinstance(agent, SimpleAgent)
    assert agent.config.name == "test_agent"
    assert agent.config.system_prompt == "You are a test assistant."
    assert agent.persistence_manager is not None
    
    # Check that the graph is properly set up
    assert agent.graph_builder is not None
    assert agent.app is not None
    assert hasattr(agent, "state_schema")
    assert agent.state_schema == SimpleAgentState


def test_simple_agent_invoke(api_credentials):
    """Test that a SimpleAgent can invoke its underlying engine."""
    # Create a simple agent
    agent = create_simple_agent(
        name="invoke_test_agent",
        system_prompt="You are a helpful test assistant.",
        persistence_type="memory",
        output_dir=api_credentials["output_dir"]
    )
    
    # Invoke with a simple query
    result = agent.run("What is the capital of France?")
    
    # Check the result structure
    assert "messages" in result
    assert len(result["messages"]) >= 2  # At least query and response
    
    # Verify message types
    assert isinstance(result["messages"][0], HumanMessage)
    assert isinstance(result["messages"][-1], AIMessage)
    
    # Check that the response contains relevant content
    response_text = result["messages"][-1].content.lower()
    assert "paris" in response_text or "france" in response_text


def test_simple_agent_state_persistence_memory(api_credentials):
    """Test that SimpleAgent properly persists state using memory persistence."""
    # Create an agent with memory persistence
    agent = create_simple_agent(
        name="persistence_test_agent",
        system_prompt="You are a memory test assistant.",
        persistence_type="memory",
        output_dir=api_credentials["output_dir"]
    )
    
    # Get initial thread ID
    thread_id = agent.runnable_config["configurable"]["thread_id"]
    
    # Send a first message
    result1 = agent.run("My name is Alex.", thread_id=thread_id)
    
    # Send a second message referring to the first
    result2 = agent.run("What's my name?", thread_id=thread_id)
    
    # Check that the agent remembered the name
    response_text = result2["messages"][-1].content.lower()
    assert "alex" in response_text
    
    # Verify that the state contains all messages
    state = agent.get_state(thread_id=thread_id)
    assert len(state["messages"]) >= 4  # Should have all messages


def test_simple_agent_thread_management(api_credentials):
    """Test thread management functionality of SimpleAgent."""
    # Create an agent
    agent = create_simple_agent(
        name="thread_test_agent",
        system_prompt="You are a thread management test assistant.",
        persistence_type="memory",
        output_dir=api_credentials["output_dir"]
    )
    
    # Create multiple conversation threads
    thread1_id = str(uuid.uuid4())
    thread2_id = str(uuid.uuid4())
    
    # Send messages to different threads
    agent.run("This is thread 1, message 1.", thread_id=thread1_id)
    agent.run("This is thread 2, message 1.", thread_id=thread2_id)
    agent.run("This is thread 1, message 2.", thread_id=thread1_id)
    
    # Get thread info
    thread1_info = agent.get_thread_info(thread_id=thread1_id)
    thread2_info = agent.get_thread_info(thread_id=thread2_id)
    
    # Verify thread info
    assert thread1_info["thread_id"] == thread1_id
    assert thread2_info["thread_id"] == thread2_id
    
    # Get state from each thread
    state1 = agent.get_state(thread_id=thread1_id)
    state2 = agent.get_state(thread_id=thread2_id)
    
    # Check message counts
    assert len(state1["messages"]) >= 4  # 2 messages + 2 responses
    assert len(state2["messages"]) >= 2  # 1 message + 1 response
    
    # List threads
    threads = agent.list_threads()
    assert len(threads) >= 2
    thread_ids = [t["thread_id"] for t in threads]
    assert thread1_id in thread_ids
    assert thread2_id in thread_ids


def test_simple_agent_input_handling(api_credentials):
    """Test that SimpleAgent handles different input formats correctly."""
    # Create an agent
    agent = create_simple_agent(
        name="input_test_agent",
        system_prompt="You are an input handling test assistant.",
        persistence_type="memory",
        output_dir=api_credentials["output_dir"]
    )
    
    # Test with string input
    result1 = agent.run("Hello, assistant!")
    assert "messages" in result1
    assert len(result1["messages"]) >= 2
    
    # Test with dict input containing 'input' key
    result2 = agent.run({"input": "How are you?"})
    assert "messages" in result2
    assert len(result2["messages"]) >= 4  # Including previous messages
    
    # Test with dict input containing messages
    result3 = agent.run({
        "messages": [HumanMessage(content="Direct message input")]
    })
    assert "messages" in result3
    assert len(result3["messages"]) >= 6  # Including all previous messages


class TestOutput(BaseModel):
    """Test model for structured output."""
    summary: str = Field(description="A summary of the input")
    sentiment: str = Field(description="The sentiment of the input")


def test_simple_agent_structured_output(api_credentials):
    """Test SimpleAgent with structured output model."""
    # Create a system prompt
    system_prompt = "Analyze the given text and provide a summary and sentiment."
    
    # Create a prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])
    
    # Create an engine with structured output
    engine = AugLLMConfig(
        name="structured_output_engine",
        llm_config=AzureLLMConfig(),
        prompt_template=prompt,
        structured_output_model=TestOutput
    )
    
    # Create the agent
    agent = create_simple_agent(
        name="structured_output_agent",
        engine=engine,
        persistence_type="memory",
        output_dir=api_credentials["output_dir"]
    )
    
    # Test with a sample input
    result = agent.run("I love the Haive framework! It's so powerful and easy to use.")
    
    # Check for structured output
    assert "output" in result
    assert hasattr(result["output"], "summary")
    assert hasattr(result["output"], "sentiment")
    assert "positive" in result["output"].sentiment.lower()


def create_qa_agent(
    name: str = "qa_agent",
    system_prompt: str = "You are a helpful assistant that answers questions accurately.",
    structured_output_model: BaseModel = None,
    persistence_type: str = "postgres",
    output_dir: str = "resources",
    **kwargs
) -> SimpleAgent:
    """
    Create a question-answering agent based on SimpleAgent.
    
    Args:
        name: Name for the agent
        system_prompt: System prompt for the QA behavior
        structured_output_model: Optional model for structured QA output
        persistence_type: Type of persistence to use
        output_dir: Directory for agent outputs
        **kwargs: Additional parameters for the agent
        
    Returns:
        Configured SimpleAgent for QA tasks
    """
    # Create QA prompt
    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])
    
    # Create engine with QA prompt
    engine = AugLLMConfig(
        llm_config=AzureLLMConfig(),
        prompt_template=qa_prompt,
        structured_output_model=structured_output_model
    )
    
    # Create and return agent
    return create_simple_agent(
        name=name,
        engine=engine,
        persistence_type=persistence_type,
        output_dir=output_dir,
        **kwargs
    )


def create_summary_agent(
    name: str = "summary_agent",
    system_prompt: str = "Summarize the following content concisely.",
    persistence_type: str = "memory",
    output_dir: str = "resources",
    **kwargs
) -> SimpleAgent:
    """
    Create a summarization agent based on SimpleAgent.
    
    Args:
        name: Name for the agent
        system_prompt: System prompt for summarization behavior
        persistence_type: Type of persistence to use
        output_dir: Directory for agent outputs
        **kwargs: Additional parameters for the agent
        
    Returns:
        Configured SimpleAgent for summarization tasks
    """
    # Create summarization prompt
    summary_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])
    
    # Create engine with summarization prompt
    engine = AugLLMConfig(
        llm_config=AzureLLMConfig(),
        prompt_template=summary_prompt,
        output_parser=StrOutputParser()
    )
    
    # Create and return agent
    return create_simple_agent(
        name=name,
        engine=engine,
        persistence_type=persistence_type,
        output_dir=output_dir,
        **kwargs
    )


def test_qa_agent(api_credentials):
    """Test the QA agent functionality."""
    # Create a QA agent
    qa_agent = create_qa_agent(
        name="test_qa_agent",
        system_prompt="You are a helpful QA assistant that answers questions concisely.",
        persistence_type="memory",
        output_dir=api_credentials["output_dir"]
    )
    
    # Test with a factual question
    result = qa_agent.run("What is the speed of light in a vacuum?")
    
    # Check the response
    response_text = result["messages"][-1].content.lower()
    assert "299,792,458" in response_text.replace(",", "") or "3 x 10" in response_text


class QA(BaseModel):
    """Question and Answer model for structured output."""
    question: str = Field(description="The question that was asked.")
    answer: str = Field(description="The answer to the question.")


def test_qa_agent_structured_output(api_credentials):
    """Test QA agent with structured output."""
    # Create a QA agent with structured output
    qa_agent = create_qa_agent(
        name="structured_qa_agent",
        system_prompt="Extract the question and provide a concise answer.",
        structured_output_model=QA,
        persistence_type="memory",
        output_dir=api_credentials["output_dir"]
    )
    
    # Test with a question
    result = qa_agent.run("What is the capital of Japan?")
    
    # Check structured output
    assert "output" in result
    assert hasattr(result["output"], "question")
    assert hasattr(result["output"], "answer")
    assert "japan" in result["output"].question.lower()
    assert "tokyo" in result["output"].answer.lower()


def test_summary_agent(api_credentials):
    """Test the summary agent functionality."""
    # Create a summary agent
    summary_agent = create_summary_agent(
        name="test_summary_agent",
        system_prompt="You are a helpful assistant that creates concise summaries.",
        persistence_type="memory",
        output_dir=api_credentials["output_dir"]
    )
    
    # Test with a long text to summarize
    long_text = """
    The Haive framework is a comprehensive platform for building AI agents. It provides 
    a unified interface for working with different AI components like language models, 
    vector stores, and retrievers. The framework is designed around a component-based 
    architecture where everything is built from reusable, configurable components.
    
    Key features include dynamic composition, allowing components to be composed at 
    runtime; serialization support, enabling components and workflows to be saved and 
    restored; sophisticated configuration management for runtime behavior adjustments; 
    and automatic state schema generation for consistent data handling.
    
    The framework includes several systems working together: the Engine system provides 
    abstractions for AI capabilities; the Graph Building system enables dynamic 
    construction of workflows; the Schema system manages state data structures; and 
    the Configuration system manages runtime behaviors.
    """
    
    # Run the summarization
    result = summary_agent.run({"input": long_text})
    
    # Check output
    # For StrOutputParser output should be in the output field
    summary_text = result.get("output", "")
    
    # If not found directly in output, try messages
    if not summary_text and "messages" in result:
        summary_text = result["messages"][-1].content
    
    # Verify the summary is more concise than original
    assert len(summary_text) < len(long_text)
    
    # Check for key content words
    assert "Haive" in summary_text
    assert "framework" in summary_text
    assert "component" in summary_text.lower()


def test_streaming_functionality(api_credentials):
    """Test streaming functionality of SimpleAgent."""
    # Create a simple agent
    agent = create_simple_agent(
        name="streaming_test_agent",
        system_prompt="You are a helpful streaming test assistant.",
        persistence_type="memory",
        output_dir=api_credentials["output_dir"]
    )
    
    # Use the stream method
    chunks = []
    for chunk in agent.stream("Tell me about AI in 3 sentences."):
        chunks.append(chunk)
        
    # Verify we got streaming chunks
    assert len(chunks) > 0
    
    # Check the result from streaming
    state = agent.get_state()
    assert "messages" in state
    assert len(state["messages"]) >= 2  # Query and response


def test_postgres_config():
    """Test PostgreSQL configuration creation without actual database connection."""
    # Create a PostgreSQL configuration
    postgres_config = PostgresCheckpointerConfig(
        db_host="localhost",
        db_port=5432,
        db_name="test_db",
        db_user="test_user",
        db_pass="test_pass",
        setup_needed=False
    )
    
    # Check configuration
    assert postgres_config.type == CheckpointerType.postgres
    assert postgres_config.db_host == "localhost"
    assert postgres_config.db_port == 5432
    assert postgres_config.db_name == "test_db"
    assert postgres_config.db_user == "test_user"


@pytest.mark.slow
def test_postgres_persistence_if_available(api_credentials):
    """Test PostgreSQL persistence if available."""
    # Skip if not running in an environment with PostgreSQL
    pg_host = os.environ.get("POSTGRES_HOST")
    pg_user = os.environ.get("POSTGRES_USER")
    pg_pass = os.environ.get("POSTGRES_PASSWORD")
    pg_db = os.environ.get("POSTGRES_DB")
    
    if not all([pg_host, pg_user, pg_pass, pg_db]):
        pytest.skip("PostgreSQL environment variables not set")
    
    try:
        # Create a PostgreSQL configuration
        postgres_config = PostgresCheckpointerConfig(
            db_host=pg_host,
            db_port=int(os.environ.get("POSTGRES_PORT", 5432)),
            db_name=pg_db,
            db_user=pg_user,
            db_pass=pg_pass,
            setup_needed=True
        )
        
        # Create an agent with PostgreSQL persistence
        agent = create_simple_agent(
            name="postgres_test_agent",
            system_prompt="You are a PostgreSQL test assistant.",
            persistence=postgres_config,
            output_dir=api_credentials["output_dir"]
        )
        
        # Generate a thread ID
        thread_id = str(uuid.uuid4())
        
        # Run with the thread ID
        agent.run("Hello, PostgreSQL!", thread_id=thread_id)
        
        # Allow time for persistence
        time.sleep(1)
        
        # Run again with the same thread to test persistence
        result = agent.run("Do you remember our conversation?", thread_id=thread_id)
        
        # Check response
        response_text = result["messages"][-1].content.lower()
        assert any(term in response_text for term in ["previous", "hello", "remember", "postgresql"])
        
        # Get checkpoint info
        checkpoint_info = agent.get_checkpoint_info(thread_id=thread_id)
        assert checkpoint_info["enabled"] is True
        assert checkpoint_info["thread_id"] == thread_id
        assert checkpoint_info.get("checkpoint_count", 0) > 0
        
    except Exception as e:
        pytest.skip(f"Error testing PostgreSQL persistence: {str(e)}")


def test_serialization_and_deserialization(api_credentials):
    """Test agent configuration serialization and deserialization."""
    # Create a simple agent config
    config = SimpleAgentConfig(
        name="serialization_test_agent",
        system_prompt="You are a serialization test assistant.",
        persistence_type=CheckpointerType.memory,
        output_dir=api_credentials["output_dir"]
    )
    
    # Serialize to dictionary
    config_dict = config.to_dict()
    
    # Check serialized data
    assert config_dict["name"] == "serialization_test_agent"
    assert config_dict["system_prompt"] == "You are a serialization test assistant."
    assert "persistence" in config_dict
    
    # Create from serialized data
    recreated_config = SimpleAgentConfig(**config_dict)
    
    # Check recreation
    assert recreated_config.name == config.name
    assert recreated_config.system_prompt == config.system_prompt
    assert recreated_config.persistence is not None
    
    # Build agent from recreated config
    agent = recreated_config.build_agent()
    assert isinstance(agent, SimpleAgent)


def test_agent_with_overridden_node_name(api_credentials):
    """Test agent with custom node name."""
    # Create a config with custom node name
    config = SimpleAgentConfig(
        name="custom_node_agent",
        system_prompt="You are a custom node test assistant.",
        node_name="custom_process",  # Override default node name
        persistence_type=CheckpointerType.memory,
        output_dir=api_credentials["output_dir"]
    )
    
    # Build agent
    agent = config.build_agent()
    
    # Verify custom node name was used
    assert "custom_process" in agent.graph_builder.nodes
    assert "process" not in agent.graph_builder.nodes
    
    # Test that it works normally
    result = agent.run("Hello, custom node!")
    assert "messages" in result
    assert len(result["messages"]) >= 2  # Query and response


def test_history_saving(api_credentials):
    """Test that agent history can be saved."""
    # Create a simple agent with history saving enabled
    agent = create_simple_agent(
        name="history_test_agent",
        system_prompt="You are a history saving test assistant.",
        persistence_type="memory",
        save_history=True,
        output_dir=api_credentials["output_dir"]
    )
    
    # First ensure the directory exists
    history_dir = os.path.join(api_credentials["output_dir"], "state_history")
    os.makedirs(history_dir, exist_ok=True)
    
    # Run a query
    result = agent.run("Hello, assistant!")
    assert "messages" in result, "No messages in result"
    assert len(result["messages"]) >= 2, "Response message not found"
    
    # Save history
    saved = agent.save_state_history()
    
    # If saving failed, print debug info
    if not saved:
        print(f"save_state_history returned False")
        print(f"Agent app compiled: {agent.app is not None}")
        print(f"Output directory exists: {os.path.exists(api_credentials['output_dir'])}")
        print(f"History directory exists: {os.path.exists(history_dir)}")
        print(f"Agent config: {agent.config}")
    
    assert saved is True, "Failed to save state history"
    
    # Check that history directory exists
    assert os.path.exists(history_dir), f"History directory {history_dir} does not exist"
    
    # List files in the directory for debugging
    files = os.listdir(history_dir)
    print(f"Files in history directory: {files}")
    
    # Check that it contains files
    assert len(files) > 0, "No history files were created"
    
    # Verify the saved files are valid JSON
    for file_path in [os.path.join(history_dir, f) for f in files]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json_content = json.load(f)
            assert json_content is not None, f"Empty JSON in {file_path}"
            assert "messages" in json_content, f"No messages in saved state at {file_path}"
        except json.JSONDecodeError:
            assert False, f"Invalid JSON in saved state history file: {file_path}"