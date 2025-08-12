"""Configuration file for pytest to properly handle imports and logging.
Save as tests/conftest.py.
"""

import logging
from pathlib import Path
from typing import Any
import uuid

from langchain_core.runnables import RunnableConfig
from pydantic import Field
import pytest

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.base import (
    Engine,
    EngineType,
    InvokableEngine,
    NonInvokableEngine,
)
from haive.core.engine.embeddings import EmbeddingsEngineConfig
from haive.core.engine.retriever import BaseRetrieverConfig, RetrieverType
from haive.core.engine.vectorstore import VectorStoreConfig, VectorStoreProvider
from haive.core.models.embeddings.base import HuggingFaceEmbeddingConfig
from haive.core.models.llm.base import AzureLLMConfig


# --------------------------------------------------------------------
# ✅ Add the project root to sys.path so imports work across project
# --------------------------------------------------------------------

# Optional: global root logger setup (safe)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)


# --------------------------------------------------------------------
# ✅ Dynamic per-test log file creation (mirroring test structure)
# --------------------------------------------------------------------
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Set up logging to both file and console for each test file."""
    rel_test_path = Path(item.fspath).resolve().relative_to(Path.cwd())
    log_file_path = Path("logs/tests") / rel_test_path.with_suffix(".log")
    log_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Clear existing handlers
    root_logger = logging.getLogger()

    # Properly close file handlers before removing them
    for handler in list(root_logger.handlers):
        if isinstance(handler, logging.FileHandler):
            handler.close()  # Close file handlers properly
        root_logger.removeHandler(handler)

    # Set up dual logging (file + console)
    file_handler = logging.FileHandler(log_file_path, mode="w")
    stream_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s", datefmt="%H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)
    root_logger.setLevel(logging.DEBUG)

    logging.getLogger().debug(f"📄 Logging to: {log_file_path}")


# Helper function for consistent naming
def generate_test_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


# --------------------------------------------------------------------
# ✅ Test Engine Classes (Simplified / Mock Implementations)
# --------------------------------------------------------------------


# Mock engines with specific behavior for testing core Engine logic
class MockEngine(Engine):
    """Mock engine for testing with custom ID."""

    engine_type: EngineType = EngineType.LLM
    id: str = Field(default_factory=lambda: generate_test_id("mock-engine"))
    name: str = Field(default_factory=lambda: f"mock_engine_{uuid.uuid4().hex[:4]}")

    def create_runnable(self, runnable_config: RunnableConfig | None = None) -> Any:
        return lambda x: x  # Simple pass-through runnable


class MockInvokableEngine(InvokableEngine):
    """Mock invokable engine for testing invoke/ainvoke."""

    engine_type: EngineType = EngineType.LLM
    id: str = Field(default_factory=lambda: generate_test_id("mock-invokable"))
    name: str = Field(default_factory=lambda: f"mock_invokable_engine_{uuid.uuid4().hex[:4]}")

    def create_runnable(self, runnable_config: RunnableConfig | None = None) -> Any:
        return self  # Runnable is the engine itself for testing

    def invoke(self, input_data: Any, runnable_config: RunnableConfig | None = None) -> Any:
        # Return input data plus a marker
        if isinstance(input_data, dict):
            return {**input_data, "invoked_by": self.name}
        return {"result": input_data, "invoked_by": self.name}

    async def ainvoke(self, input_data: Any, runnable_config: RunnableConfig | None = None) -> Any:
        # Async version of invoke
        return self.invoke(input_data, runnable_config)


class MockNonInvokableEngine(NonInvokableEngine):
    """Mock non-invokable engine for testing instantiation."""

    engine_type: EngineType = EngineType.EMBEDDINGS
    id: str = Field(default_factory=lambda: generate_test_id("mock-non-invokable"))
    name: str = Field(default_factory=lambda: f"mock_non_invokable_engine_{uuid.uuid4().hex[:4]}")

    def create_runnable(self, runnable_config: RunnableConfig | None = None) -> Any:
        # Return a simple dictionary indicating creation
        return {"instance_created_by": self.name}


# --------------------------------------------------------------------
# ✅ Mock Engine Fixtures
# --------------------------------------------------------------------


@pytest.fixture
def mock_engine() -> MockEngine:
    """Provides a basic mock engine instance."""
    return MockEngine()


@pytest.fixture
def mock_invokable_engine() -> MockInvokableEngine:
    """Provides a mock invokable engine instance."""
    return MockInvokableEngine()


@pytest.fixture
def mock_non_invokable_engine() -> MockNonInvokableEngine:
    """Provides a mock non-invokable engine instance."""
    return MockNonInvokableEngine()


# --------------------------------------------------------------------
# ✅ Real Engine Fixtures (Using Actual Config Classes)
# --------------------------------------------------------------------
# These use the actual config classes but might need credentials/setup
# to fully instantiate runnables in real tests.


@pytest.fixture
def real_llm_engine():
    """Create a real LLM engine for testing."""
    return AugLLMConfig(
        id=f"test-llm-{uuid.uuid4().hex[:8]}",
        name=f"test_llm_{uuid.uuid4().hex[:8]}",
        engine_type=EngineType.LLM,
        model="gpt-4o",
        temperature=0.7,
        description="Test LLM Engine",
    )


@pytest.fixture
def real_aug_llm_engine() -> AugLLMConfig:
    """Provides a real AugLLM engine config instance."""
    # AugLLM often wraps another LLM config
    base_llm = AzureLLMConfig(
        id=generate_test_id("aug-base-llm"),
        name=f"aug_base_llm_{uuid.uuid4().hex[:4]}",
        model="gpt-4o-mini",
        api_key="sk-test-key-for-tests",
        temperature=0.1,
    )
    return AugLLMConfig(
        id=generate_test_id("real-aug-llm"),
        name=f"real_aug_llm_{uuid.uuid4().hex[:4]}",
        engine_type=EngineType.LLM,
        llm_config=base_llm,  # Pass the base LLM config
        temperature=0.7,  # Can override base config temp
        description="Real AugLLM Config for Testing",
    )


@pytest.fixture
def real_embeddings_engine() -> EmbeddingsEngineConfig:
    """Provides a real Embeddings engine config instance."""
    # Using HuggingFace embeddings as it's often locally runnable
    hf_config = HuggingFaceEmbeddingConfig(model="sentence-transformers/all-MiniLM-L6-v2")
    return EmbeddingsEngineConfig(
        id=generate_test_id("real-embeddings"),
        name=f"real_embeddings_{uuid.uuid4().hex[:4]}",
        engine_type=EngineType.EMBEDDINGS,
        embedding_config=hf_config,
        description="Real Embeddings Config for Testing",
    )


@pytest.fixture
def real_vectorstore_engine(
    real_embeddings_engine: EmbeddingsEngineConfig,
) -> VectorStoreConfig:
    """Provides a real VectorStore engine config instance (In-Memory)."""
    return VectorStoreConfig(
        id=generate_test_id("real-vs"),
        name=f"real_vectorstore_{uuid.uuid4().hex[:4]}",
        engine_type=EngineType.VECTOR_STORE,
        vector_store_provider=VectorStoreProvider.IN_MEMORY,
        embedding_model=real_embeddings_engine.embedding_config,  # Reuse embedding config
        description="Real In-Memory VectorStore Config for Testing",
    )


@pytest.fixture
def real_retriever_engine(
    real_vectorstore_engine: VectorStoreConfig,
) -> BaseRetrieverConfig:
    """Provides a real Retriever engine config instance."""
    return BaseRetrieverConfig(
        id=generate_test_id("real-retriever"),
        name=f"real_retriever_{uuid.uuid4().hex[:4]}",
        engine_type=EngineType.RETRIEVER,
        retriever_type=RetrieverType.VECTOR_STORE,
        vector_store_config=real_vectorstore_engine,  # Use the real VS config
        k=3,  # Default number of documents to retrieve
        description="Real Retriever Config for Testing",
    )


# --------------------------------------------------------------------
# ✅ Agent Fixtures for Testing Auto-Wrap Behavior
# --------------------------------------------------------------------

from datetime import datetime

from langchain_core.tools import tool
from pydantic import BaseModel

# Import our agents
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


# Test models for structured output
class SimpleResult(BaseModel):
    """Simple structured output model for testing."""
    message: str = Field(description="Result message")
    confidence: float = Field(description="Confidence score", ge=0.0, le=1.0, default=0.8)
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())


class AnalysisResult(BaseModel):
    """More complex structured output model."""
    summary: str = Field(description="Analysis summary")
    key_points: list[str] = Field(description="Key findings", default_factory=list)
    score: float = Field(description="Overall score", ge=0.0, le=10.0)
    recommendation: str = Field(description="Next steps recommendation")


# Test tools
@tool
def simple_calculator(expression: str) -> str:
    """Calculate simple math expressions safely."""
    try:
        # Safe eval with limited builtins
        allowed_names = {"__builtins__": {}}
        result = eval(expression, allowed_names, {})
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"


@tool
def text_analyzer(text: str) -> str:
    """Analyze text and return basic stats."""
    word_count = len(text.split())
    char_count = len(text)
    return f"Words: {word_count}, Characters: {char_count}"


# Test models for structured output
class ReactResult(BaseModel):
    """Structured output for ReactAgent testing."""
    analysis: str = Field(description="Analysis result")
    tool_calls_made: int = Field(description="Number of tool calls", default=0)
    confidence: float = Field(description="Confidence score", ge=0.0, le=1.0, default=0.8)


# Agent fixtures
@pytest.fixture
def simple_agent_with_structured_output():
    """SimpleAgent WITH structured output model (will auto-wrap)."""
    return SimpleAgent(
        name="simple_structured",
        engine=AugLLMConfig(
            llm_config=AzureLLMConfig(
                model="gpt-4o",
                temperature=0.3,
            ),
            system_message="You are a formatter agent that creates structured outputs.",
        ),
        structured_output_model=SimpleResult,
        structured_output_version="v2",
        debug=True,
    )


@pytest.fixture
def simple_agent_without_structured_output():
    """SimpleAgent WITHOUT structured output model (no auto-wrap)."""
    return SimpleAgent(
        name="simple_plain",
        engine=AugLLMConfig(
            llm_config=AzureLLMConfig(
                model="gpt-4o",
                temperature=0.5,
            ),
            system_message="You are a simple conversational agent.",
        ),
        debug=True,
    )


@pytest.fixture
def react_agent_with_tools():
    """ReactAgent with tools (no structured output)."""
    return ReactAgent(
        name="react_with_tools",
        engine=AugLLMConfig(
            llm_config=AzureLLMConfig(
                model="gpt-4o",
                temperature=0.7,
            ),
            system_message="You are a reasoning agent. Use tools when needed.",
            tools=[simple_calculator, text_analyzer],
        ),
        debug=True,
    )


@pytest.fixture
def complex_structured_agent():
    """SimpleAgent with complex structured output for advanced testing."""
    return SimpleAgent(
        name="complex_structured",
        engine=AugLLMConfig(
            llm_config=AzureLLMConfig(
                model="gpt-4o",
                temperature=0.2,
            ),
            system_message="You are an analysis agent that provides detailed structured outputs.",
        ),
        structured_output_model=AnalysisResult,
        structured_output_version="v2",
        debug=True,
    )


@pytest.fixture
def react_agent_with_structured_output():
    """ReactAgent WITH structured output model (will auto-wrap)."""
    return ReactAgent(
        name="react_structured",
        engine=AugLLMConfig(
            llm_config=AzureLLMConfig(
                model="gpt-4o",
                temperature=0.3,
            ),
            system_message="You are a reasoning agent that provides structured outputs.",
            tools=[simple_calculator, text_analyzer],
        ),
        structured_output_model=ReactResult,
        structured_output_version="v2",
        debug=True,
    )


@pytest.fixture
def all_test_agents(
    simple_agent_with_structured_output,
    simple_agent_without_structured_output,
    react_agent_with_tools,
    react_agent_with_structured_output,
    complex_structured_agent
):
    """Return all test agents for comparison testing."""
    return {
        "simple_structured": simple_agent_with_structured_output,
        "simple_plain": simple_agent_without_structured_output,
        "react_tools": react_agent_with_tools,
        "react_structured": react_agent_with_structured_output,
        "complex_structured": complex_structured_agent,
    }


# --------------------------------------------------------------------
# ℹ️ Note on Test vs Real Fixtures:
# - Mock fixtures are good for testing Engine base class logic without external deps.
# - Real fixtures use actual EngineConfig subclasses, useful for integration tests.
# - Agent fixtures provide different agent configurations for testing auto-wrap behavior
# - The 'Test...' classes and fixtures from the original file are removed as
#   they are largely covered by the mock and real fixtures now.
# --------------------------------------------------------------------
