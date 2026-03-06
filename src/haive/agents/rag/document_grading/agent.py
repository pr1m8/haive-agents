"""Document Grading RAG Agent.

Iterative document grading with structured output.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.models.llm.base import OpenAILLMConfig, LLMConfig
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import END, START
from pydantic import BaseModel, Field

from haive.agents.base.agent import Agent
from haive.agents.multi.base import SequentialAgent
from haive.agents.rag.base.agent import BaseRAGAgent
from haive.agents.simple.agent import SimpleAgent


class SingleDocumentGrade(BaseModel):
    """Grade for a single document."""

    relevance_score: float = Field(ge=0.0, le=1.0, description="Relevance score 0-1")
    is_relevant: bool = Field(description="Whether document is relevant")
    reasoning: str = Field(description="Explanation for the grade")


SINGLE_DOC_GRADING_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert document grader. Assess this document's relevance to the query.

Provide:
1. A relevance score (0.0-1.0)
2. Whether it's relevant (true/false)
3. Clear reasoning for your assessment""",
        ),
        (
            "human",
            """Grade this document for relevance.

Query: {query}

Document:
{document}

Provide your assessment.""",
        ),
    ]
)


class DocumentGradingAgent(Agent):
    """Agent that iterates over documents and grades each one."""

    name: str = "Document Grader"
    relevance_threshold: float = 0.7

    def build_graph(self) -> BaseGraph:
        """Build document grading graph."""
        from typing import Any

        graph = BaseGraph(name="DocumentGrading")

        grading_engine = AugLLMConfig(
            prompt_template=SINGLE_DOC_GRADING_PROMPT,
            structured_output_model=SingleDocumentGrade,
            output_key="document_grade",
        )

        threshold = self.relevance_threshold

        def grade_documents(state: dict[str, Any]) -> dict[str, Any]:
            """Grade each retrieved document for relevance."""
            query = getattr(state, "query", "")
            docs = getattr(state, "retrieved_documents", [])

            graded_docs = []
            for doc in docs:
                content = doc.page_content if hasattr(doc, "page_content") else str(doc)
                try:
                    grade = grading_engine.invoke({"query": query, "document": content[:500]})
                    if grade.is_relevant and grade.relevance_score >= threshold:
                        graded_docs.append(doc)
                except Exception:
                    graded_docs.append(doc)

            return {
                "graded_documents": graded_docs,
                "retrieved_documents": graded_docs,
                "num_relevant": len(graded_docs),
                "num_total": len(docs),
            }

        graph.add_node("grade_documents", grade_documents)
        graph.add_edge(START, "grade_documents")
        graph.add_edge("grade_documents", END)

        return graph


class DocumentGradingRAGAgent(SequentialAgent):
    """RAG with document grading and filtering."""

    @classmethod
    def from_documents(
        cls,
        documents: list[Document],
        llm_config: LLMConfig | None = None,
        relevance_threshold: float = 0.7,
        **kwargs,
    ):
        """Create Document Grading RAG from documents."""
        if not llm_config:
            llm_config = OpenAILLMConfig(model="gpt-4o-mini")

        retrieval_agent = BaseRAGAgent.from_documents(
            documents=documents, name="Grading RAG Retriever"
        )

        grading_agent = DocumentGradingAgent(
            relevance_threshold=relevance_threshold
        )

        answer_agent = SimpleAgent(
            engine=AugLLMConfig(
                llm_config=llm_config,
                prompt_template=ChatPromptTemplate.from_messages(
                    [
                        (
                            "system",
                            "Answer based only on relevant documents that passed grading.",
                        ),
                        (
                            "human",
                            "Answer the query using these relevant documents.\n\nQuery: {query}\nRelevant Documents: {graded_documents}",
                        ),
                    ]
                ),
            ),
            name="Graded Answer Generator",
        )

        return cls(
            agents=[retrieval_agent, grading_agent, answer_agent],
            name=kwargs.pop("name", "Document Grading RAG Agent"),
            **kwargs,
        )
