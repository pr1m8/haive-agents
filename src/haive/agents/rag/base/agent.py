"""Base RAG Agent - retrieval-augmented generation.

Uses OpenAI embeddings by default to avoid HuggingFace/CUDA issues.
"""

from typing import Any

from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langgraph.graph import END, START, StateGraph
from pydantic import Field, PrivateAttr

from haive.agents.base.agent import Agent


class BaseRAGAgent(Agent):
    """Base RAG agent that performs retrieval then answers.

    Uses OpenAI embeddings + FAISS vector store by default.
    Add documents via add_documents() before querying.
    """

    engine: Any = Field(default=None, description="Not used - RAG has its own retriever")
    _retriever: Any = PrivateAttr(default=None)
    _vectorstore: Any = PrivateAttr(default=None)

    def model_post_init(self, __context: Any) -> None:
        super().model_post_init(__context)
        # Initialize FAISS with OpenAI embeddings
        embeddings = OpenAIEmbeddings()
        self._vectorstore = FAISS.from_documents(
            [Document(page_content="RAG agent initialized.", metadata={"type": "system"})],
            embeddings,
        )
        self._retriever = self._vectorstore.as_retriever(search_kwargs={"k": 3})

    def add_documents(self, documents: list[Document]) -> None:
        """Add documents to the vector store for retrieval."""
        self._vectorstore.add_documents(documents)

    def compile(self, **kwargs) -> Any:
        """Compile the RAG graph."""
        if not self._is_compiled or kwargs:
            if not hasattr(self, "graph") or self.graph is None:
                self._graph_built = False
                self._build_initial_graph()
            if not self.graph:
                raise RuntimeError("No graph")
            if hasattr(self.graph, "to_langgraph"):
                lg = self.graph.to_langgraph(state_schema=self.state_schema)
            else:
                lg = self.graph
            self._app = lg.compile(
                checkpointer=self.checkpointer, store=self.store, **kwargs
            )
            self._compiled_graph = self._app
            self._is_compiled = True
        return self._compiled_graph or self._app

    def build_graph(self) -> StateGraph:
        """Build: retrieve -> generate answer."""
        from langchain_core.runnables import RunnablePassthrough
        from haive.core.engine.aug_llm import AugLLMConfig

        graph = StateGraph(dict)

        def retrieve(state: dict) -> dict:
            query = ""
            msgs = state.get("messages", [])
            if msgs:
                last = msgs[-1]
                query = last.content if hasattr(last, "content") else str(last)
            elif state.get("query"):
                query = state["query"]

            docs = self._retriever.invoke(query) if query else []
            context = "\n".join(d.page_content for d in docs)
            return {"context": context, "query": query}

        def generate(state: dict) -> dict:
            from langchain_openai import ChatOpenAI
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            context = state.get("context", "")
            query = state.get("query", "")
            prompt = f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer based on the context. If no relevant context, answer from your knowledge."
            response = llm.invoke(prompt)
            return {"messages": [AIMessage(content=response.content)]}

        graph.add_node("retrieve", retrieve)
        graph.add_node("generate", generate)
        graph.add_edge(START, "retrieve")
        graph.add_edge("retrieve", "generate")
        graph.add_edge("generate", END)

        return graph

    class Config:
        arbitrary_types_allowed = True
