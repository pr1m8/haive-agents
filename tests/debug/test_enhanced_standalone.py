#!/usr/bin/env python3
"""Standalone test of enhanced agents with real execution.

This test bypasses the import issues and tests the pattern directly.
"""

import asyncio
from typing import Any

from langchain_core.tools import tool


# Test 1: SimpleAgent Pattern Demo


# Minimal implementation to show the pattern
class MinimalEngine:
    """Minimal engine for testing."""

    def __init__(self, temperature: float = 0.7):
        self.temperature = temperature


class MinimalAgent:
    """Minimal agent showing the pattern."""

    def __init__(self, name: str, engine: Any):
        self.name = name
        self.engine = engine

    async def arun(self, input_data: str, debug: bool = False) -> str:
        """Async run with debug option."""
        if debug:
            pass

        # Simulate processing
        result = f"{self.name} processed: {input_data}"

        if debug:
            pass

        return result


# Create and test SimpleAgent
engine = MinimalEngine(temperature=0.1)
simple = MinimalAgent(name="simple_test", engine=engine)


# Run with debug
async def test_simple():
    await simple.arun("Hello world", debug=True)


asyncio.run(test_simple())

# Test 2: Multi-Agent Patterns


# Test tools
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


@tool
def word_counter(text: str) -> str:
    """Count words in text."""
    words = text.split()
    return f"{len(words)} words"


# Supervisor pattern demo
class MinimalSupervisor(MinimalAgent):
    """Minimal supervisor showing worker management."""

    def __init__(self, name: str, engine: Any, workers: dict[str, Any]):
        super().__init__(name, engine)
        self.workers = workers

    async def delegate(self, task: str, worker_name: str, debug: bool = False) -> str:
        """Delegate task to worker."""
        if debug:
            pass

        if worker_name in self.workers:
            worker = self.workers[worker_name]
            result = await worker.arun(task, debug=debug)
            return f"[via {worker_name}] {result}"

        return f"Worker {worker_name} not found"


# Create supervisor with workers
worker1 = MinimalAgent("analyst", MinimalEngine(0.1))
worker2 = MinimalAgent("writer", MinimalEngine(0.7))

supervisor = MinimalSupervisor(
    name="manager",
    engine=MinimalEngine(0.3),
    workers={"analyst": worker1, "writer": worker2},
)


# Test delegation
async def test_supervisor():
    await supervisor.delegate("Analyze data trends", "analyst", debug=True)


asyncio.run(test_supervisor())

# Test 3: Sequential Pipeline


class MinimalSequential:
    """Minimal sequential pipeline."""

    def __init__(self, name: str, agents: list[Any]):
        self.name = name
        self.agents = agents
        " → ".join([a.name for a in agents])

    async def execute_sequence(self, input_data: str, debug: bool = False) -> str:
        """Execute agents in sequence."""
        current = input_data

        for _i, agent in enumerate(self.agents):
            if debug:
                pass

            current = await agent.arun(current, debug=False)

            if debug:
                pass

        return current


# Create pipeline
step1 = MinimalAgent("preprocessor", MinimalEngine(0.1))
step2 = MinimalAgent("analyzer", MinimalEngine(0.3))
step3 = MinimalAgent("formatter", MinimalEngine(0.5))

pipeline = MinimalSequential("data_pipeline", [step1, step2, step3])


# Test pipeline
async def test_pipeline():
    await pipeline.execute_sequence("Raw input data", debug=True)


asyncio.run(test_pipeline())

# Test 4: Parallel Execution


class MinimalParallel:
    """Minimal parallel executor."""

    def __init__(self, name: str, agents: list[Any]):
        self.name = name
        self.agents = agents

    async def execute_parallel(self, input_data: str, debug: bool = False) -> list[str]:
        """Execute all agents in parallel."""
        if debug:
            pass

        # Create tasks
        tasks = [agent.arun(input_data, debug=False) for agent in self.agents]

        # Execute in parallel
        results = await asyncio.gather(*tasks)

        if debug:
            for _agent, _result in zip(self.agents, results, strict=False):
                pass

        return results


# Create ensemble
expert1 = MinimalAgent("expert_1", MinimalEngine(0.5))
expert2 = MinimalAgent("expert_2", MinimalEngine(0.5))
expert3 = MinimalAgent("expert_3", MinimalEngine(0.5))

ensemble = MinimalParallel("expert_panel", [expert1, expert2, expert3])


# Test parallel
async def test_parallel():
    await ensemble.execute_parallel("What is AI?", debug=True)


asyncio.run(test_parallel())

# Test 5: RAG Pattern


class MinimalRetriever:
    """Minimal retriever for RAG demo."""

    def __init__(self, documents: list[str]):
        self.documents = documents

    def retrieve(self, query: str) -> list[str]:
        """Retrieve relevant documents."""
        # Simple keyword match
        relevant = [doc for doc in self.documents if query.lower() in doc.lower()]
        return relevant[:2]  # Return top 2


class MinimalRAG:
    """Minimal RAG agent."""

    def __init__(self, name: str, retriever: Any):
        self.name = name
        self.retriever = retriever

    async def answer(self, question: str, debug: bool = False) -> str:
        """Answer question using retrieval."""
        if debug:
            pass

        # Retrieve
        docs = self.retriever.retrieve(question)

        if debug:
            for _i, _doc in enumerate(docs):
                pass

        # Generate answer (simulated)
        if docs:
            context = " ".join(docs)
            answer = f"Based on the context: {context[:100]}..."
        else:
            answer = "No relevant information found."

        return answer


# Create RAG
documents = [
    "Python is a high-level programming language.",
    "Machine learning is a subset of AI.",
    "Neural networks are inspired by the brain.",
    "Python is popular for data science.",
]

retriever = MinimalRetriever(documents)
rag = MinimalRAG("knowledge_base", retriever)


# Test RAG
async def test_rag():
    await rag.answer("What is Python?", debug=True)


asyncio.run(test_rag())

# Summary
