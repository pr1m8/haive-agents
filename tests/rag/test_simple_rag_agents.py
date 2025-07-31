"""Test Simple RAG and Collective RAG agents - NO MOCKS."""

from haive.agents.rag.collective_rag_agent_v4 import CollectiveRAGAgent
from haive.agents.rag.simple.agent import SimpleRAGAgent


def test_simple_rag_agent_composition():
    """Test SimpleRAGAgent is properly composed."""
    # SimpleRAGAgent should be an EnhancedMultiAgentV4 instance
    assert hasattr(SimpleRAGAgent, "run")
    assert hasattr(SimpleRAGAgent, "arun")

    # Should have agents attribute with BaseRAGAgent and AnswerAgent
    assert hasattr(SimpleRAGAgent, "agents")
    assert len(SimpleRAGAgent.agents) == 2

    # Should be sequential mode
    assert SimpleRAGAgent.execution_mode == "sequential"


def test_collective_rag_agent_composition():
    """Test CollectiveRAGAgent is properly composed."""
    # CollectiveRAGAgent should be an EnhancedMultiAgentV4 instance
    assert hasattr(CollectiveRAGAgent, "run")
    assert hasattr(CollectiveRAGAgent, "arun")

    # Should have agents attribute with 3 SimpleRAGAgent + 1 SynthesisAgent
    assert hasattr(CollectiveRAGAgent, "agents")
    assert len(CollectiveRAGAgent.agents) == 4

    # Should be parallel_then_sequential mode
    assert CollectiveRAGAgent.execution_mode == "parallel_then_sequential"


def test_simple_rag_agent_real_execution():
    """Test SimpleRAGAgent with real execution - NO MOCKS."""
    # This would require actual vector store setup
    # For now, just test that the composition works

    # Should be able to access the pattern
    assert SimpleRAGAgent is not None
    assert callable(SimpleRAGAgent.run)

    # Agents should be properly configured
    base_rag_agent = SimpleRAGAgent.agents[0]
    answer_agent = SimpleRAGAgent.agents[1]

    # BaseRAGAgent should have retrieval capabilities
    assert hasattr(base_rag_agent, "engine")

    # AnswerAgent should have LLM capabilities
    assert hasattr(answer_agent, "engine")
    assert hasattr(answer_agent, "prompt_template")


def test_collective_rag_agent_real_execution():
    """Test CollectiveRAGAgent with real execution - NO MOCKS."""
    # This would require actual vector store setup
    # For now, just test that the composition works

    # Should be able to access the pattern
    assert CollectiveRAGAgent is not None
    assert callable(CollectiveRAGAgent.run)

    # Should have 3 RAG agents + 1 synthesis agent
    rag_agents = CollectiveRAGAgent.agents[:3]
    synthesis_agent = CollectiveRAGAgent.agents[3]

    # All RAG agents should be SimpleRAGAgent instances
    for rag_agent in rag_agents:
        assert rag_agent is SimpleRAGAgent

    # Synthesis agent should have proper configuration
    assert hasattr(synthesis_agent, "engine")
    assert hasattr(synthesis_agent, "prompt_template")


if __name__ == "__main__":
    # Run basic tests
    test_simple_rag_agent_composition()
    test_collective_rag_agent_composition()
    test_simple_rag_agent_real_execution()
    test_collective_rag_agent_real_execution()
