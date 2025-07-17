#!/usr/bin/env python3

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.engine.vectorstore.vectorstore import VectorStoreConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.rag.base.agent import BaseRAGAgent

# Same exact setup as the failing notebook
RAG_QUERY_REFINEMENT = ChatPromptTemplate.from_messages(
    [
        ("system", """You are an expert query optimization specialist..."""),
        (
            "human",
            """Analyze and refine the following user query.

**Original Query:** {query}
**Context (if provided):** {context}

Focus on improvements.""",
        ),
    ]
).partial(context="")


class QueryRefinementResponse(BaseModel):
    original_query: str = Field(description="The original user query")
    best_refined_query: str = Field(description="The recommended best refined query")



try:
    # Create vector store config (BaseRAGAgent needs this)
    vectorstore_config = VectorStoreConfig(
        name="test_vectorstore",
        documents=["test document"],  # Minimal docs
    )

    # Create BaseRAGAgent
    rag_agent = BaseRAGAgent(name="rag_test", engine=vectorstore_config)


    # Test with same input
    rag_result = rag_agent.run(
        {"query": "what is the tallest building in france"}, debug=True
    )

except Exception as e:
    pass

    try:
        rag_agent = BaseRAGAgent(name="rag_test", engine=vectorstore_config)
        if hasattr(rag_agent, "composer"):
            schema_class = rag_agent.composer.build()

            # Check critical fields
            for name in ["engine", "context", "query"]:
                if name in schema_class.model_fields:
                    field_info = schema_class.model_fields[name]
                else:
                    pass
    except Exception as e2:
        pass")



try:
    # Import the states that could be involved
    from haive.core.schema.prebuilt.messages.messages_with_token_usage import (
        MessagesStateWithTokenUsage,
    )
    from haive.core.schema.prebuilt.messages_state import MessagesState
    from haive.core.schema.prebuilt.meta_state import MetaStateSchema


    # Check their fields
    for state_name, state_class in [
        ("MessagesState", MessagesState),
        ("MetaStateSchema", MetaStateSchema),
        ("MessagesStateWithTokenUsage", MessagesStateWithTokenUsage),
    ]:
        for name, field_info in state_class.model_fields.items():
            if name in ["engine", "context", "query", "messages"]:
                pass

except Exception as e:
    pass")


try:
    from haive.agents.simple.agent_v2 import SimpleAgentV2

    config = AugLLMConfig(
        prompt_template=RAG_QUERY_REFINEMENT,
        structured_output_model=QueryRefinementResponse,
        structured_output_version="v2",
    )

    agent = SimpleAgentV2(engine=config)

    # Get the base classes
    for i, cls in enumerate(SimpleAgentV2.__mro__):
        pass

    # Try to access the composer's detected base class
    if hasattr(agent, "composer"):

except Exception as e:
    import traceback

    traceback.print_exc()
