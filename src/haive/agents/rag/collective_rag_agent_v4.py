"""CollectiveRAGAgent - Multiple RAG sources with synthesis."""

from typing import List

from pydantic import Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.rag.simple.agent import SimpleRAGAgent
from haive.agents.rag.synthesis_agent import SynthesisAgent


class CollectiveRAGAgent(EnhancedMultiAgentV4):
    """Collective RAG = Multiple SimpleRAGAgent + SynthesisAgent, parallel then sequential."""

    agents: List = Field(
        default_factory=lambda: [
            SimpleRAGAgent(name="rag_source_1"),
            SimpleRAGAgent(name="rag_source_2"),
            SimpleRAGAgent(name="rag_source_3"),
            SynthesisAgent(name="synthesizer"),
        ]
    )

    execution_mode: str = Field(default="parallel_then_sequential")
