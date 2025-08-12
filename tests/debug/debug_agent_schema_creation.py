#!/usr/bin/env python3

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.core.engine.aug_llm import AugLLMConfig


# Exact notebook setup
RAG_QUERY_REFINEMENT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert query optimization specialist for RAG systems...""",
        ),
        (
            "human",
            """Analyze and refine the following user query to improve retrieval and answer quality.

**Original Query:** {query}

**Context (if provided):** {context}

Focus on improvements that will lead to better document retrieval and more comprehensive answers.""",
        ),
    ]
).partial(context="")


class QueryRefinementResponse(BaseModel):
    original_query: str = Field(description="The original user query")
    best_refined_query: str = Field(description="The recommended best refined query")


config = AugLLMConfig(
    prompt_template=RAG_QUERY_REFINEMENT,
    structured_output_model=QueryRefinementResponse,
    structured_output_version="v2",
)


try:
    # Try to import and see class definition
    from haive.agents.simple.agent_v2 import SimpleAgentV2

    for name, field_info in SimpleAgentV2.model_fields.items():
        if name in ["engine", "structured_output_model", "prompt_template"]:
            pass

    agent = SimpleAgentV2(engine=config)

    if hasattr(agent, "composer"):
        schema_class = agent.composer.build()

        # Check the problematic fields
        for name in ["engine", "context", "query"]:
            if name in schema_class.model_fields:
                field_info = schema_class.model_fields[name]
            else:
                pass
    else:
        pass

except Exception:
    import traceback

    traceback.print_exc()
