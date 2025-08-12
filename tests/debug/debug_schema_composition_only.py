#!/usr/bin/env python3

"""Focused debug: Trace exactly how the schema composer builds the final schema.
and why engine/context fields are marked as required.
"""

import contextlib
import logging

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.schema_composer import SchemaComposer


# Enable debug logging for schema composer
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Exact notebook setup
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


config = AugLLMConfig(
    prompt_template=RAG_QUERY_REFINEMENT,
    structured_output_model=QueryRefinementResponse,
    structured_output_version="v2",
)


# Create composer like the agent does
composer = SchemaComposer(name="TestState")

# Add engine fields
composer.add_fields_from_engine(config)


# Let's see what happens if we set tools
composer_with_tools = SchemaComposer(name="TestStateWithTools")
composer_with_tools.has_tools = True  # Force tool detection
composer_with_tools.add_fields_from_engine(config)


# Step-by-step field creation
input_fields = config.get_input_fields()
for name, (_field_type, _field_info) in input_fields.items():
    if name in ["engine", "context", "query"]:
        pass


# Check composer fields before build
for name, _field_def in composer.fields.items():
    if name in ["engine", "context", "query"]:
        pass

final_schema = composer.build()

for name, _field_info in final_schema.model_fields.items():
    if name in ["engine", "context", "query"]:
        pass


# Test schema validation
test_data = {
    "query": "test query"
    # Missing context and engine intentionally
}

with contextlib.suppress(Exception):
    instance = final_schema.model_validate(test_data)

test_data_full = {"query": "test query", "context": "", "engine": config}

with contextlib.suppress(Exception):
    instance = final_schema.model_validate(test_data_full)

# Let's check what the composer's _detect_base_class_requirements method is doing

# Call the base class detection explicitly
composer._detect_base_class_requirements()
