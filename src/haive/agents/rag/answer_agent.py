"""Answer Agent for RAG - SimpleAgentV3 with document context prompt."""

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


class AnswerAgent(SimpleAgentV3):
    """SimpleAgentV3 configured for answering questions based on retrieved documents."""

    engine: AugLLMConfig = Field(
        default_factory=lambda: AugLLMConfig(
            temperature=0.7,
            max_tokens=2000,
            system_message=(
                "You are a helpful assistant that answers questions based on retrieved documents. "
                "Always ground your answers in the provided documents. "
                "Provide detailed, comprehensive answers with proper citations."
            ),
        )
    )

    prompt_template: ChatPromptTemplate = Field(
        default_factory=lambda: ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful assistant that answers questions based on retrieved documents. Always ground your answers in the provided documents. Provide detailed, comprehensive answers with proper citations.",
                ),
                (
                    "human",
                    """Retrieved Documents:
{retrieved_documents}

These documents contain relevant information to answer the user's question. Please read them carefully and use them to provide a comprehensive, detailed answer.

User Question: {query}

Instructions:
1. Carefully analyze all retrieved documents
2. Identify the most relevant information for answering the question
3. Provide a detailed, comprehensive answer based on the documents
4. Quote directly from the documents when appropriate
5. If the documents don't contain enough information, say so clearly
6. Always cite which document(s) you're using for each part of your answer

Detailed Answer:""",
                ),
            ]
        )
    )
