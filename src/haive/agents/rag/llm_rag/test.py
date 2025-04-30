from haive.agents.rag.base import BaseRAGConfig
from haive.core.engine.retriever.retriever import VectorStoreRetrieverConfig
from haive.core.engine.vectorstore.vectorstore import VectorStoreConfig
from langchain_core.documents import Document
retriever_config = VectorStoreRetrieverConfig(
    name="retriever",
    description="Retriever for documents",
    vector_store_config=VectorStoreConfig(
        name="vector_store",
        description="Vector store for documents",
        documents=[Document(page_content="Hello, world!", metadata={"source": "test.txt"}),
                   Document(page_content='python is a programming language', metadata={"source": "test.txt"})]
    )
)
a = BaseRAGConfig(retriever_config=retriever_config)
print(a)

agent = a.create_runnable()
print(agent)


