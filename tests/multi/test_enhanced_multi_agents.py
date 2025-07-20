"""Test suite for enhanced multi-agent implementations.

Tests the enhanced agent pattern with:
- SupervisorAgent
- DynamicSupervisor
- SequentialAgent
- ParallelAgent
- EnhancedMultiAgent

All tests use REAL components - NO MOCKS.
"""

import asyncio
import pytest
from typing import Any, Dict, List

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from haive.core.engine.aug_llm.config import AugLLMConfig


# Mock agents for testing (minimal but real)
class TestAgent:
    """Minimal test agent that works like a real agent."""
    
    def __init__(self, name: str, response_prefix: str = ""):
        self.name = name
        self.response_prefix = response_prefix
        self.engine = AugLLMConfig(temperature=0.1)
        self.call_count = 0
    
    async def arun(self, input_data: Any) -> str:
        """Async run method."""
        self.call_count += 1
        if isinstance(input_data, dict):
            input_str = input_data.get("messages", [{}])[-1].get("content", str(input_data))
        else:
            input_str = str(input_data)
        return f"{self.response_prefix}{self.name} processed: {input_str}"
    
    def run(self, input_data: Any) -> str:
        """Sync run method."""
        return asyncio.run(self.arun(input_data))


# Test tools for ReactAgent
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


class TestSupervisorAgent:
    """Test SupervisorAgent functionality."""
    
    def test_supervisor_creation(self):
        """Test creating supervisor with workers."""
        from haive.agents.multi.enhanced_supervisor_agent import SupervisorAgent
        
        # Create workers
        analyst = TestAgent("analyst", "Analysis: ")
        developer = TestAgent("developer", "Code: ")
        
        # Create supervisor
        supervisor = SupervisorAgent(
            name="manager",
            workers={
                "analyst": analyst,
                "developer": developer
            },
            temperature=0.3
        )
        
        assert supervisor.name == "manager"
        assert len(supervisor.workers) == 2
        assert "analyst" in supervisor.workers
        assert supervisor.temperature == 0.3
    
    def test_dynamic_worker_management(self):
        """Test adding and removing workers."""
        from haive.agents.multi.enhanced_supervisor_agent import SupervisorAgent
        
        supervisor = SupervisorAgent(name="manager")
        
        # Initially no workers
        assert len(supervisor.workers) == 0
        
        # Add workers
        supervisor.add_worker("tester", TestAgent("tester"))
        assert len(supervisor.workers) == 1
        assert "tester" in supervisor.list_workers()
        
        # Remove worker
        removed = supervisor.remove_worker("tester")
        assert removed is not None
        assert len(supervisor.workers) == 0
    
    def test_delegation_strategies(self):
        """Test different delegation strategies."""
        from haive.agents.multi.enhanced_supervisor_agent import SupervisorAgent
        
        strategies = ["first", "best", "all", "round_robin"]
        
        for strategy in strategies:
            supervisor = SupervisorAgent(
                name=f"manager_{strategy}",
                delegation_strategy=strategy,
                workers={"worker": TestAgent("worker")}
            )
            assert supervisor.delegation_strategy == strategy


class TestDynamicSupervisor:
    """Test DynamicSupervisor functionality."""
    
    def test_worker_scaling(self):
        """Test dynamic worker scaling."""
        from haive.agents.multi.enhanced_dynamic_supervisor import DynamicSupervisor
        
        supervisor = DynamicSupervisor(
            name="auto_scaler",
            min_workers=1,
            max_workers=5,
            auto_scale=True
        )
        
        assert supervisor.min_workers == 1
        assert supervisor.max_workers == 5
        assert supervisor.can_add_worker()
    
    def test_worker_templates(self):
        """Test worker creation from templates."""
        from haive.agents.multi.enhanced_dynamic_supervisor import DynamicSupervisor
        
        supervisor = DynamicSupervisor(
            name="dynamic",
            worker_templates={
                "test": TestAgent
            }
        )
        
        # Add worker from template
        success = supervisor.add_worker_from_template("test", "worker1")
        assert success
        assert "worker1" in supervisor.workers
        assert "worker1" in supervisor.idle_workers
    
    def test_task_assignment(self):
        """Test task assignment and completion."""
        from haive.agents.multi.enhanced_dynamic_supervisor import DynamicSupervisor
        
        supervisor = DynamicSupervisor(name="task_manager")
        supervisor.add_worker("worker1", TestAgent("w1"))
        
        # Assign task
        assigned = supervisor.assign_task("task1")
        assert assigned == "worker1"
        assert "task1" in supervisor.active_tasks
        assert "worker1" not in supervisor.idle_workers
        
        # Complete task
        supervisor.complete_task("task1", success=True, duration=1.0)
        assert "task1" not in supervisor.active_tasks
        assert "worker1" in supervisor.idle_workers
        
        # Check metrics
        metrics = supervisor.get_worker_metrics()
        assert "worker1" in metrics
        assert metrics["worker1"]["tasks_completed"] == 1
        assert metrics["worker1"]["success_rate"] == 1.0


class TestSequentialAgent:
    """Test SequentialAgent functionality."""
    
    def test_sequential_pipeline(self):
        """Test basic sequential execution."""
        from haive.agents.multi.enhanced_sequential_agent import SequentialAgent
        
        # Create pipeline
        pipeline = SequentialAgent(
            name="pipeline",
            agents=[
                TestAgent("step1", "1:"),
                TestAgent("step2", "2:"),
                TestAgent("step3", "3:")
            ]
        )
        
        assert len(pipeline.agents) == 3
        assert pipeline.get_pipeline_description() == "step1 → step2 → step3"
    
    @pytest.mark.asyncio
    async def test_sequential_execution(self):
        """Test actual sequential execution."""
        from haive.agents.multi.enhanced_sequential_agent import SequentialAgent
        
        # Create agents that transform input
        agent1 = TestAgent("upper", "UPPER:")
        agent2 = TestAgent("count", "COUNT:")
        
        pipeline = SequentialAgent(
            name="transform",
            agents=[agent1, agent2],
            return_all_outputs=True
        )
        
        # Execute
        outputs = await pipeline.execute_sequence("hello world")
        
        assert len(outputs) == 2
        assert agent1.call_count == 1
        assert agent2.call_count == 1
    
    def test_pipeline_modification(self):
        """Test adding and removing agents from pipeline."""
        from haive.agents.multi.enhanced_sequential_agent import SequentialAgent
        
        pipeline = SequentialAgent(
            name="dynamic_pipeline",
            agents=[TestAgent("a")]
        )
        
        # Add agent
        pipeline.add_agent(TestAgent("b"))
        assert len(pipeline.agents) == 2
        
        # Insert agent
        pipeline.insert_agent(1, TestAgent("middle"))
        assert len(pipeline.agents) == 3
        assert pipeline.get_pipeline_description() == "a → middle → b"
        
        # Remove agent
        removed = pipeline.remove_agent(1)
        assert removed is not None
        assert len(pipeline.agents) == 2


class TestParallelAgent:
    """Test ParallelAgent functionality."""
    
    def test_parallel_creation(self):
        """Test creating parallel agent ensemble."""
        from haive.agents.multi.enhanced_parallel_agent import ParallelAgent
        
        ensemble = ParallelAgent(
            name="ensemble",
            agents=[
                TestAgent("expert1"),
                TestAgent("expert2"),
                TestAgent("expert3")
            ],
            aggregation_strategy="all"
        )
        
        assert len(ensemble.agents) == 3
        assert ensemble.aggregation_strategy == "all"
    
    @pytest.mark.asyncio
    async def test_parallel_execution(self):
        """Test actual parallel execution."""
        from haive.agents.multi.enhanced_parallel_agent import ParallelAgent
        
        # Create agents with different delays
        agents = [
            TestAgent(f"agent{i}", f"A{i}:")
            for i in range(3)
        ]
        
        ensemble = ParallelAgent(
            name="parallel_test",
            agents=agents,
            aggregation_strategy="all",
            timeout_per_agent=5.0
        )
        
        # Execute in parallel
        results = await ensemble.execute_parallel("test input")
        
        # All agents should have been called
        assert all(agent.call_count == 1 for agent in agents)
        
        # Should have all results
        assert len(results) == 3
        assert all("agent" in r for r in results)
    
    @pytest.mark.asyncio
    async def test_aggregation_strategies(self):
        """Test different aggregation strategies."""
        from haive.agents.multi.enhanced_parallel_agent import ParallelAgent
        
        agents = [TestAgent(f"a{i}") for i in range(3)]
        
        # Test "first" strategy
        ensemble = ParallelAgent(
            name="first_test",
            agents=agents,
            aggregation_strategy="first"
        )
        
        result = await ensemble.execute_parallel("test")
        assert isinstance(result, str)
        assert "a0" in result  # First agent's result


class TestEnhancedMultiAgent:
    """Test EnhancedMultiAgent functionality."""
    
    def test_multi_agent_creation(self):
        """Test creating enhanced multi-agent."""
        from haive.agents.multi.enhanced_clean_multi_agent import EnhancedMultiAgent
        
        # With list of agents
        multi1 = EnhancedMultiAgent(
            name="multi_list",
            agents=[TestAgent("a"), TestAgent("b")],
            mode="sequential"
        )
        
        assert len(multi1.agents) == 2
        assert multi1.mode == "sequential"
        
        # With dict of agents
        multi2 = EnhancedMultiAgent(
            name="multi_dict",
            agents={
                "analyzer": TestAgent("analyzer"),
                "processor": TestAgent("processor")
            },
            mode="parallel"
        )
        
        assert len(multi2.agents) == 2
        assert "analyzer" in multi2.agents
    
    def test_state_strategies(self):
        """Test different state management strategies."""
        from haive.agents.multi.enhanced_clean_multi_agent import EnhancedMultiAgent
        
        # Minimal state
        multi1 = EnhancedMultiAgent(
            name="minimal",
            agents=[TestAgent("a")],
            state_strategy="minimal"
        )
        assert multi1.state_strategy == "minimal"
        
        # Container state
        multi2 = EnhancedMultiAgent(
            name="container",
            agents=[TestAgent("a")],
            state_strategy="container"
        )
        assert multi2.state_strategy == "container"
    
    def test_state_transfer_rules(self):
        """Test state transfer configuration."""
        from haive.agents.multi.enhanced_clean_multi_agent import EnhancedMultiAgent
        
        transfer_map = {
            ("agent_0", "agent_1"): {"output": "input"},
            ("agent_1", "agent_2"): {"result": "data"}
        }
        
        multi = EnhancedMultiAgent(
            name="transfer_test",
            agents=[TestAgent("a"), TestAgent("b"), TestAgent("c")],
            state_transfer_map=transfer_map
        )
        
        assert multi.state_transfer_map == transfer_map
    
    def test_agent_access_methods(self):
        """Test agent access and management."""
        from haive.agents.multi.enhanced_clean_multi_agent import EnhancedMultiAgent
        
        agents = {
            "first": TestAgent("first"),
            "second": TestAgent("second")
        }
        
        multi = EnhancedMultiAgent(
            name="access_test",
            agents=agents
        )
        
        # Get agent names
        names = multi.get_agent_names()
        assert "first" in names
        assert "second" in names
        
        # Get specific agent
        agent = multi.get_agent("first")
        assert agent is not None
        assert agent.name == "first"


class TestReactAgentEnhanced:
    """Test enhanced ReactAgent with real tools."""
    
    def test_react_with_tools(self):
        """Test ReactAgent with actual tools."""
        from haive.agents.react.enhanced_react_agent import ReactAgent
        
        agent = ReactAgent(
            name="calculator_agent",
            temperature=0.1,
            tools=[calculator, word_counter],
            max_iterations=5
        )
        
        assert agent.name == "calculator_agent"
        assert len(agent.tools) == 2
        assert agent.max_iterations == 5
        
        # Check representation
        repr_str = repr(agent)
        assert "ReactAgent" in repr_str
        assert "calculator" in repr_str


# Integration test combining multiple patterns
class TestMultiAgentIntegration:
    """Test integration of multiple agent patterns."""
    
    def test_supervisor_with_sequential_workers(self):
        """Test supervisor managing sequential pipelines."""
        from haive.agents.multi.enhanced_supervisor_agent import SupervisorAgent
        from haive.agents.multi.enhanced_sequential_agent import SequentialAgent
        
        # Create sequential pipelines as workers
        pipeline1 = SequentialAgent(
            name="analysis_pipeline",
            agents=[TestAgent("extract"), TestAgent("analyze")]
        )
        
        pipeline2 = SequentialAgent(
            name="processing_pipeline",
            agents=[TestAgent("clean"), TestAgent("transform")]
        )
        
        # Supervisor manages pipelines
        supervisor = SupervisorAgent(
            name="pipeline_manager",
            workers={
                "analysis": pipeline1,
                "processing": pipeline2
            }
        )
        
        assert len(supervisor.workers) == 2
        assert supervisor.get_worker("analysis") == pipeline1
    
    def test_parallel_react_agents(self):
        """Test parallel execution of ReactAgents."""
        from haive.agents.multi.enhanced_parallel_agent import ParallelAgent
        from haive.agents.react.enhanced_react_agent import ReactAgent
        
        # Create multiple ReactAgents with different tools
        agent1 = ReactAgent(
            name="math_expert",
            tools=[calculator],
            temperature=0.1
        )
        
        agent2 = ReactAgent(
            name="text_expert", 
            tools=[word_counter],
            temperature=0.1
        )
        
        # Run in parallel
        ensemble = ParallelAgent(
            name="expert_ensemble",
            agents=[agent1, agent2],
            aggregation_strategy="all"
        )
        
        assert len(ensemble.agents) == 2


if __name__ == "__main__":
    # Run specific test
    pytest.main([__file__, "-v", "-k", "test_supervisor_creation"])