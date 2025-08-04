"""Synthesis Agent for RAG - SimpleAgentV3 that synthesizes multiple RAG results."""

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


class SynthesisAgent(SimpleAgentV3):
    """SimpleAgentV3 configured for synthesizing results from multiple RAG sources."""

    engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.7,
            max_tokens=2000,
            system_message=(
                "You are an expert at synthesizing information from multiple knowledge sources. "
                "Provide comprehensive, coherent answers that integrate insights from all sources."
            ))
    )

    prompt_template: ChatPromptTemplate = Field(
        default_factory=lambda: ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert at synthesizing information from multiple knowledge sources. Provide comprehensive, coherent answers that integrate insights from all sources."),
                (
                    "human",
                    """Results from Multiple RAG Sources:
{rag_results}

Each source above has retrieved relevant documents and provided answers based on their specific knowledge base. Your task is to synthesize all this information into a comprehensive, coherent answer.

Instructions:
1. Read all the results from different RAG sources carefully
2. Identify common themes and complementary information across sources
3. Note any contradictions or conflicting information between sources
4. Create a comprehensive synthesis that:
   - Incorporates insights from all relevant sources
   - Clearly indicates which information comes from which source
   - Resolves or explains any contradictions
   - Provides a complete answer to the original question
5. Structure your response clearly with appropriate sections if needed
6. Be explicit about the confidence level based on source agreement

Comprehensive Synthesized Answer:"""),
            ]
        )
    )
