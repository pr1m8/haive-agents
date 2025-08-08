"""CollectiveRAGAgent - Multiple RAG sources with synthesis."""

from pydantic import Field

from haive.agents.multi.agent import MultiAgent
from haive.agents.rag.simple.agent import SimpleRAGAgent
from haive.agents.rag.synthesis_agent import SynthesisAgent


class CollectiveRAGAgent(MultiAgent):
    """Collective RAG = Multiple SimpleRAGAgent + SynthesisAgent, parallel then sequential."""

    agents: list = Field(
        default_factory=lambda: [
            SimpleRAGAgent(name="rag_source_1"),
            SimpleRAGAgent(name="rag_source_2"),
            SimpleRAGAgent(name="rag_source_3"),
            SynthesisAgent(name="synthesizer"),
        ]
    )

    execution_mode: str = Field(default="parallel_then_sequential")
