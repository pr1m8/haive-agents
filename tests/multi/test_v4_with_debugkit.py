#!/usr/bin/env python3
"""Test V4 multi-agent with full debugkit instrumentation.

This test is set up to diagnose why multi-agent tests are running slowly.
It uses the new debugkit utilities for comprehensive debugging.
"""

import asyncio
import os
import sys


# Add paths for imports
sys.path.insert(0, os.path.abspath("packages/haive-agents/src"))
sys.path.insert(0, os.path.abspath("packages/haive-core/src"))

# Import debugkit FIRST
from haive.core.utils.debugkit import debugkit


# Enable comprehensive debugging
debugkit.configure(
    ice_enabled=True,
    trace_enabled=True,
    profile_enabled=True,
    log_level="TRACE",
    show_locals=True,
    show_types=True,
    pretty_print=True,
)

# Set environment variables for maximum visibility
os.environ["LANGCHAIN_VERBOSE"] = "true"
os.environ["LANGCHAIN_TRACING_V2"] = "false"  # Disable cloud tracing
os.environ["HAIVE_DEBUG"] = "true"
os.environ["LOGURU_LEVEL"] = "TRACE"

# Now import the rest
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig


# Structured output model
class TestResult(BaseModel):
    """Test result with timing."""

    status: str = Field(description="Status: success or error")
    duration: float = Field(description="Execution time in seconds")
    message: str = Field(description="Result message")


@debugkit.instrument(capture_locals=True, log_calls=True)
def create_test_config():
    """Create test configuration with timeout."""
    debugkit.ice("Creating AugLLMConfig with timeout")

    config = AugLLMConfig(
        temperature=0.1,  # Low for consistency
        max_tokens=50,  # Small for speed
        timeout=30,  # 30 second timeout - CRITICAL!
        streaming=False,  # Disable streaming for debugging
    )

    debugkit.ice("Config created", config=config)
    return config


@debugkit.instrument(capture_locals=True, log_calls=True)
def create_test_agents(config: AugLLMConfig):
    """Create test agents with debugging."""
    with debugkit.log_context("agent_creation"):
        debugkit.log.info("Creating test agents")

        # Agent 1: Analyzer
        debugkit.log.progress("Creating analyzer agent...")
        analyzer = SimpleAgentV3(
            name="analyzer",
            engine=config,
            system_message="You analyze input briefly.",
            debug=True,  # Enable agent-level debugging
        )
        debugkit.ice("Analyzer created", agent=analyzer.name)

        # Agent 2: Processor
        debugkit.log.progress("Creating processor agent...")
        processor = SimpleAgentV3(
            name="processor", engine=config, system_message="You process data briefly.", debug=True
        )
        debugkit.ice("Processor created", agent=processor.name)

        # Agent 3: Formatter with structured output
        debugkit.log.progress("Creating formatter agent...")
        formatter = SimpleAgentV3(
            name="formatter",
            engine=config,
            structured_output_model=TestResult,
            system_message="You format results briefly.",
            debug=True,
        )
        debugkit.ice("Formatter created", agent=formatter.name)

        debugkit.log.success("All agents created successfully")
        return analyzer, processor, formatter


@debugkit.instrument(capture_locals=True, log_calls=True, measure_time=True)
def test_v4_sequential():
    """Test V4 sequential execution with full debugging."""
    debugkit.log.header("V4 SEQUENTIAL TEST WITH DEBUGKIT")

    with debugkit.log_context("test_setup"):
        # Create configuration
        config = create_test_config()

        # Create agents
        analyzer, processor, formatter = create_test_agents(config)

        # Create multi-agent
        debugkit.log.info("Creating EnhancedMultiAgentV4")
        multi = EnhancedMultiAgentV4(
            name="v4_debug_test",
            agents=[analyzer, processor, formatter],
            execution_mode="sequential",
        )

        debugkit.ice(
            "Multi-agent created",
            agent_count=len(multi.agents),
            agent_names=multi.get_agent_names(),
            execution_mode=multi.execution_mode,
        )

    with debugkit.log_context("graph_compilation"):
        debugkit.log.progress("Compiling graph...")

        with debugkit.timer("compilation") as timer:
            compiled = multi.compile()

        debugkit.log.success(f"Graph compiled in {timer.elapsed:.2f}s")
        debugkit.ice("Compiled graph", nodes=list(compiled.nodes.keys()))

    with debugkit.log_context("test_execution"):
        test_input = {"messages": [HumanMessage(content="Test message for debugging")]}

        debugkit.log.info("Starting test execution")
        debugkit.ice("Test input", input=test_input)

        with debugkit.timer("execution") as timer:
            try:
                # Add progress tracking
                debugkit.log.progress("Invoking compiled graph...")
                result = compiled.invoke(test_input)

                debugkit.log.success(f"Execution completed in {timer.elapsed:.2f}s")
                debugkit.ice(
                    "Result",
                    result_type=type(result),
                    message_count=len(result.get("messages", [])),
                )

            except Exception as e:
                debugkit.log.error(f"Execution failed: {e}")
                debugkit.log.exception(e)
                raise

    # Performance summary
    debugkit.log.metrics(
        {
            "setup_time": "N/A",
            "compilation_time": f"{timer.elapsed:.2f}s",
            "execution_time": f"{timer.elapsed:.2f}s",
            "total_agents": len(multi.agents),
            "execution_mode": multi.execution_mode,
        },
        title="Test Performance Summary",
    )

    return result


@debugkit.instrument(capture_locals=True, log_calls=True, measure_time=True)
def test_v4_with_routing():
    """Test V4 with conditional routing and debugging."""
    debugkit.log.header("V4 CONDITIONAL ROUTING TEST")

    with debugkit.log_context("setup"):
        config = create_test_config()
        analyzer, processor, formatter = create_test_agents(config)

        # Create multi-agent with conditional mode
        multi = EnhancedMultiAgentV4(
            name="v4_routing_test",
            agents=[analyzer, processor, formatter],
            execution_mode="conditional",
            entry_point="analyzer",
        )

        # Add routing logic
        debugkit.log.info("Adding conditional routing")

        def route_condition(state):
            """Route based on message content."""
            debugkit.ice("Routing decision", state_keys=list(state.keys()))
            messages = state.get("messages", [])
            if messages:
                content = str(messages[-1].content).lower()
                debugkit.ice("Routing based on content", content=content[:50])
                return "complex" in content
            return False

        multi.add_conditional_edge(
            "analyzer", route_condition, true_agent="processor", false_agent="formatter"
        )

        debugkit.ice("Routing configured")

    with debugkit.log_context("compilation"):
        with debugkit.timer("routing_compilation"):
            compiled = multi.compile()
        debugkit.log.success("Routing graph compiled")

    # Test both paths
    test_cases = [
        ("Simple test message", "formatter"),  # Should go to formatter
        ("Complex analysis required", "processor"),  # Should go to processor
    ]

    for test_msg, expected_route in test_cases:
        with debugkit.log_context(f"test_case_{expected_route}"):
            debugkit.log.info(f"Testing route to {expected_route}")

            test_input = {"messages": [HumanMessage(content=test_msg)]}

            with debugkit.timer(f"execution_{expected_route}"):
                result = compiled.invoke(test_input)

            debugkit.log.success(f"Route test completed for {expected_route}")


@debugkit.instrument(capture_locals=True, log_calls=True)
async def test_async_execution():
    """Test async execution with debugging."""
    debugkit.log.header("ASYNC EXECUTION TEST")

    config = create_test_config()
    agent = SimpleAgentV3(name="async_test", engine=config)

    with debugkit.timer("async_execution"):
        result = await agent.arun("Test async execution")

    debugkit.ice("Async result", result=result)
    return result


def run_all_tests():
    """Run all tests with comprehensive debugging."""
    debugkit.log.header("HAIVE V4 MULTI-AGENT DEBUG TEST SUITE", style="bold blue")

    # Configuration summary
    debugkit.log.info("Debug Configuration:")
    debugkit.log.json(
        {
            "ice_enabled": debugkit.config.ice_enabled,
            "trace_enabled": debugkit.config.trace_enabled,
            "profile_enabled": debugkit.config.profile_enabled,
            "log_level": debugkit.config.log_level,
            "langchain_verbose": os.environ.get("LANGCHAIN_VERBOSE"),
            "haive_debug": os.environ.get("HAIVE_DEBUG"),
        },
        title="Debug Settings",
    )

    try:
        # Test 1: Sequential
        debugkit.log.divider("TEST 1: SEQUENTIAL EXECUTION")
        test_v4_sequential()

        # Test 2: Routing
        debugkit.log.divider("TEST 2: CONDITIONAL ROUTING")
        test_v4_with_routing()

        # Test 3: Async
        debugkit.log.divider("TEST 3: ASYNC EXECUTION")
        asyncio.run(test_async_execution())

        debugkit.log.success("ALL TESTS COMPLETED", style="bold green")

    except Exception as e:
        debugkit.log.error(f"TEST SUITE FAILED: {e}", style="bold red")
        debugkit.log.exception(e)
        raise

    finally:
        # Performance report
        if hasattr(debugkit, "get_performance_report"):
            report = debugkit.get_performance_report()
            debugkit.log.table(report, title="Performance Report")


if __name__ == "__main__":
    debugkit.log.info("Starting V4 Multi-Agent Debug Test")
    debugkit.log.warning("This test has comprehensive debugging enabled")
    debugkit.log.info("Watch for progress messages and timing information")

    # Uncomment to run (not running as requested)
    # run_all_tests()

    debugkit.log.info("""
    🎯 TO RUN THIS TEST:
    
    1. Ensure you have an LLM API key configured
    2. Run: poetry run python test_v4_with_debugkit.py
    3. Watch the detailed output to see where it hangs
    4. Check the logs for:
       - Schema composition loops
       - LLM call timeouts  
       - Graph compilation issues
       - State transition problems
    
    The debugkit will show you exactly where the code is spending time.
    """)
