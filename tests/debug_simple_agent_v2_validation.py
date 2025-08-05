#!/usr/bin/env python3

"""COMPREHENSIVE DEBUG TEST for SimpleAgent V2 Validation Error.

This test traces EVERY step of the validation process to find exactly
where the engine/context fields get marked as required when they shouldn't be.
"""

import contextlib
import traceback
from typing import Any

from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

# Import the exact components from the notebook
from haive.agents.simple.agent_v2 import SimpleAgentV2
from haive.core.engine.aug_llm import AugLLMConfig


class QueryRefinementSuggestion(BaseModel):
    """Individual query refinement suggestion."""

    refined_query: str = Field(description="The refined/improved query")
    improvement_type: str = Field(description="Type of improvement made")
    rationale: str = Field(description="Why this refinement improves the query")
    expected_benefit: str = Field(description="Expected improvement in retrieval")


class QueryRefinementResponse(BaseModel):
    """Query refinement analysis and suggestions."""

    original_query: str = Field(description="The original user query")
    query_analysis: str = Field(description="Analysis of the original query")
    query_type: str = Field(description="Classification of query type")
    complexity_level: str = Field(description="simple, moderate, or complex")
    refinement_suggestions: list[QueryRefinementSuggestion] = Field(
        description="List of suggested query improvements"
    )
    best_refined_query: str = Field(description="The recommended best refined query")
    search_strategy_recommendations: list[str] = Field(
        description="Recommendations for search strategy"
    )


# Create the exact prompt from the notebook
RAG_QUERY_REFINEMENT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert query optimization specialist for RAG systems. Your role is to analyze user queries and suggest improvements that will lead to better document retrieval and more accurate answers.

**Query Analysis Dimensions:**
1. **Clarity**: Is the query clear and unambiguous?
2. **Specificity**: Is the query specific enough to retrieve relevant documents?
3. **Scope**: Is the query scope appropriate (not too broad or narrow)?
4. **Terminology**: Does the query use appropriate domain-specific terms?
5. **Intent**: Is the user's intent clearly expressed?
6. **Context**: Is sufficient context provided for understanding?

**Refinement Strategies:**
- **Add Specificity**: Include specific terms, entities, timeframes, or constraints
- **Clarify Intent**: Make the desired outcome or answer type explicit
- **Expand Context**: Add background information that helps with retrieval
- **Use Better Terminology**: Replace colloquial terms with domain-specific language
- **Break Down Complex Queries**: Split multi-part questions into focused sub-queries
- **Add Constraints**: Include relevant filters or limitations

**Query Types to Consider:**
- Factual (seeking specific facts)
- Analytical (requiring analysis or comparison)
- Procedural (asking for step-by-step guidance)
- Conceptual (understanding abstract ideas)
- Temporal (time-based information)
- Causal (cause-and-effect relationships)

Provide multiple refinement suggestions with clear rationales.""",
        ),
        (
            "human",
            """Analyze and refine the following user query to improve retrieval and answer quality.

**Original Query:** {query}

**Context (if provided):** {context}

**Analysis Required:**
1. Analyze the current query's strengths and weaknesses
2. Classify the query type and complexity
3. Provide multiple refinement suggestions
4. Recommend the best refined query
5. Suggest optimal search strategies

Focus on improvements that will lead to better document retrieval and more comprehensive answers.""",
        ),
    ]
)


def debug_step(step_name: str, data: Any, file_location: str = "") -> None:
    """Debug helper to print step information."""
    if file_location:
        pass

    if hasattr(data, "__dict__"):
        pass

    if isinstance(data, dict):
        pass

    with contextlib.suppress(Exception):
        pass


def inspect_pydantic_model(model_class: type, name: str) -> None:
    """Inspect a Pydantic model's fields and requirements."""
    if hasattr(model_class, "model_fields"):
        fields = model_class.model_fields

        for field_name, field_info in fields.items():
            # Check if field is required
            (
                field_info.is_required()
                if hasattr(field_info, "is_required")
                else (field_info.default is ...)
            )
            getattr(field_info, "default", "NO_DEFAULT")

            if field_name in ["context", "engine"]:
                pass


def test_debug_simple_agent_v2_validation():
    """Comprehensive debug test to trace every step of SimpleAgentV2 validation.

    This will help us find exactly where the engine/context validation error occurs.
    Traces the ENTIRE schema creation and composition process.
    """
    # STEP 1: Test the prompt template
    debug_step(
        "STEP 1: Prompt Template Analysis",
        RAG_QUERY_REFINEMENT,
        "langchain_core.prompts.ChatPromptTemplate",
    )

    # STEP 2: Create AugLLMConfig and inspect it

    config = AugLLMConfig(
        structured_output_model=QueryRefinementResponse,
        structured_output_version="v2",
        prompt_template=RAG_QUERY_REFINEMENT,
    )

    debug_step(
        "AugLLMConfig Created",
        config,
        "packages/haive-core/src/haive/core/engine/aug_llm/config.py",
    )

    # Test the _get_input_variables method
    try:
        config._get_input_variables()
    except Exception:
        traceback.print_exc()

    # Test the _compute_input_fields method
    try:
        input_fields = config._compute_input_fields()
        for field_name, _field_tuple in input_fields.items():
            if field_name in ["context", "engine"]:
                pass
    except Exception:
        traceback.print_exc()

    # STEP 3: Trace Schema Creation and Composition Process

    # Before creating the agent, let's trace schema composition

    # Let's manually trace what happens during agent creation
    try:
        # Check if we can access the schema composer
        try:
            # Let's trace what base schemas are available

            # Check MessagesState and other base schemas
            try:
                from haive.core.schema.prebuilt.messages_state import MessagesState

                inspect_pydantic_model(MessagesState, "MessagesState (Base)")
            except Exception:
                pass

            try:
                from haive.core.schema.prebuilt.meta_state import MetaStateSchema

                inspect_pydantic_model(MetaStateSchema, "MetaStateSchema (Base)")
            except Exception:
                pass

            try:
                from haive.core.schema.prebuilt.messages.messages_with_token_usage import (
                    MessagesStateWithTokenUsage,
                )

                inspect_pydantic_model(
                    MessagesStateWithTokenUsage, "MessagesStateWithTokenUsage (Base)"
                )
            except Exception:
                pass

        except Exception:
            pass

        # Check what input/output schemas the engine will contribute
        if hasattr(config, "derive_input_schema"):
            try:
                engine_input_schema = config.derive_input_schema()
                inspect_pydantic_model(engine_input_schema, "Engine Input Schema")
            except Exception:
                traceback.print_exc()

        if hasattr(config, "derive_output_schema"):
            try:
                engine_output_schema = config.derive_output_schema()
                inspect_pydantic_model(engine_output_schema, "Engine Output Schema")
            except Exception:
                traceback.print_exc()

        # Now create the agent and trace the schema composition
        agent = SimpleAgentV2(engine=config)
        debug_step(
            "SimpleAgentV2 Created",
            agent,
            "packages/haive-agents/src/haive/agents/simple/agent_v2.py",
        )

        # Trace the schema that was actually created
        if hasattr(agent, "state_schema"):
            # Check if we can access the schema composer instance
            if hasattr(agent, "_schema_composer"):
                composer = agent._schema_composer
                debug_step(
                    "Schema Composer Instance",
                    composer,
                    "packages/haive-core/src/haive/core/schema/schema_composer.py",
                )

                # Check the composer's base schema
                if hasattr(composer, "base_state_schema"):
                    inspect_pydantic_model(composer.base_state_schema, "Composer Base Schema")

                # Check the composer's engines
                if hasattr(composer, "engines"):
                    for i, engine in enumerate(composer.engines):
                        if hasattr(engine, "derive_input_schema"):
                            try:
                                eng_input = engine.derive_input_schema()
                                inspect_pydantic_model(eng_input, f"Engine {i} Input Schema")
                            except Exception:
                                pass

                # Check the composed schema fields
                if hasattr(composer, "composed_schema"):
                    inspect_pydantic_model(composer.composed_schema, "Final Composed Schema")
            else:
                pass
        else:
            pass

    except Exception:
        traceback.print_exc()
        return

    # STEP 4: Inspect the agent's state schema

    if hasattr(agent, "state_schema"):
        inspect_pydantic_model(agent.state_schema, "Agent State Schema")
    else:
        pass

    # STEP 5: Trace Graph Building and Compilation Process

    # Let's trace the graph building process

    # Check if agent has build_graph method
    if hasattr(agent, "build_graph"):
        try:
            # Get the graph before compilation
            graph = agent.build_graph()
            debug_step("Built Graph", graph, "BaseGraph or StateGraph")

            # Check graph properties
            if hasattr(graph, "nodes"):
                pass

            if hasattr(graph, "edges"):
                pass

            # Check if graph has a schema or input model
            if hasattr(graph, "schema"):
                inspect_pydantic_model(graph.schema, "Graph Schema")

        except Exception:
            traceback.print_exc()

    # Check the compiled app
    if hasattr(agent, "_app") and agent._app:
        app = agent._app
        debug_step("LangGraph App", app, "langgraph.pregel")

        # Trace app creation properties
        if hasattr(app, "channels"):
            pass

        if hasattr(app, "input_channels"):
            pass

        if hasattr(app, "output_channels"):
            pass

        # Check for input_model - THIS IS THE CRITICAL PART
        if hasattr(app, "input_model") and app.input_model:
            inspect_pydantic_model(app.input_model, "LangGraph Input Model")

            # Trace where this input_model comes from

            # THIS IS LIKELY WHERE THE BUG IS
            state_fields = agent.state_schema.model_fields if hasattr(agent, "state_schema") else {}
            input_fields = (
                app.input_model.model_fields if hasattr(app.input_model, "model_fields") else {}
            )

            for critical_field in ["context", "engine"]:
                if critical_field in state_fields:
                    state_field = state_fields[critical_field]
                    state_required = (
                        state_field.is_required()
                        if hasattr(state_field, "is_required")
                        else (state_field.default is ...)
                    )
                else:
                    pass

                if critical_field in input_fields:
                    input_field = input_fields[critical_field]
                    input_required = (
                        input_field.is_required()
                        if hasattr(input_field, "is_required")
                        else (input_field.default is ...)
                    )

                    if critical_field in state_fields:
                        state_field = state_fields[critical_field]
                        state_required = (
                            state_field.is_required()
                            if hasattr(state_field, "is_required")
                            else (state_field.default is ...)
                        )
                        if state_required != input_required:
                            pass
                else:
                    pass

            # Check if we can trace the input model creation

        else:
            pass
    else:
        pass

    # STEP 5.5: Trace Engine Registration and Field Mapping

    try:
        from haive.core.engine.base import EngineRegistry

        registry = EngineRegistry.get_instance()

        if hasattr(registry, "engines"):
            # Check our specific engine
            engine_name = getattr(config, "name", None)
            if engine_name and engine_name in registry.engines:
                engine_info = registry.engines[engine_name]
                debug_step(
                    f"Engine Registry Info: {engine_name}",
                    engine_info,
                    "packages/haive-core/src/haive/core/engine/base.py",
                )

        # Check field mappings if they exist
        if hasattr(registry, "input_mappings"):
            pass

        if hasattr(registry, "output_mappings"):
            pass

        # Check if the engine has field information
        if hasattr(config, "input_fields"):
            pass

        if hasattr(config, "output_fields"):
            pass

        # Check if there are any field metadata or annotations
        if hasattr(config, "_field_metadata"):
            pass

    except Exception:
        traceback.print_exc()

    # STEP 6: Try to run with debug and catch the exact error

    test_input = {"query": "what is the tallest building in france"}

    try:
        agent.run(test_input, debug=True)
    except Exception as e:
        # Get the full traceback
        traceback.print_exc()

        # Analyze the validation error
        if "validation errors" in str(e):
            pass


if __name__ == "__main__":
    test_debug_simple_agent_v2_validation()
