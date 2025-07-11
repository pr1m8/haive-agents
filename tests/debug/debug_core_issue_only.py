#!/usr/bin/env python3

"""CORE ISSUE ANALYSIS: Why is LangGraph's input_model different from our schema?

The error shows LangGraph is validating against an input_model, not the main schema.
Let's trace exactly where this input_model comes from.
"""

import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")

from haive.core.engine.aug_llm.config import AugLLMConfig

# Direct imports to avoid syntax error issues
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

# Replicate the exact notebook setup
RAG_QUERY_REFINEMENT = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert query optimization specialist..."),
        (
            "human",
            "Analyze and refine the following user query.\n\n**Original Query:** {query}\n\n**Context (if provided):** {context}\n\nFocus on improvements.",
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



# Check what methods exist for schema derivation
methods = [
    attr for attr in dir(config) if "schema" in attr.lower() or "input" in attr.lower()
]
for method in sorted(methods):
    if not method.startswith("_"):
        pass


try:
    input_schema = config.derive_input_schema()
    for name, field_info in input_schema.model_fields.items():
        if name in ["engine", "context", "query"]:
            pass

    test_data = {"query": "test"}
    try:
        instance = input_schema.model_validate(test_data)
    except Exception as e:
        pass")
        # This tells us if the issue is in the input schema itself

except Exception as e:
    pass")


try:
    computed_fields = config._compute_input_fields()
    for name, (field_type, field_info) in computed_fields.items():
        if name in ["engine", "context", "query"]:
            required = getattr(
                field_info,
                "is_required",
                lambda: hasattr(field_info, "default") and field_info.default is ...,
            )()

except Exception as e:
    pass")




try:
    input_vars = config._get_input_variables()

    input_fields = config.get_input_fields()


except Exception as e:
    pass")

