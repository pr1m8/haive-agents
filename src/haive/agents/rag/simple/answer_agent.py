"""Answer Agent for RAG - SimpleAgent with document context prompt."""

from langchain_core.prompts import ChatPromptTemplate
from pydantic import Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


class AnswerAgent(SimpleAgentV3):
    """SimpleAgent configured for answering questions based on retrieved documents."""

    prompt_template: ChatPromptTemplate = Field(
        default_factory=lambda: ChatPromptTemplate.from_template(
            """You are a helpful assistant that answers questions based on retrieved documents.

Retrieved Documents:
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

Detailed Answer:"""
        )
    )

    system_message: str = Field(
        default="You are a helpful assistant that answers questions based on retrieved context. Always ground your answers in the provided documents."
    )
