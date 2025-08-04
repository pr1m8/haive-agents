"""Prompt templates for structured output agents.

This module provides prompt templates used by structured agents
to guide the conversion of unstructured text into structured formats.
"""

from langchain_core.prompts import ChatPromptTemplate

# Base structured output prompt
STRUCTURED_OUTPUT_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a structured output converter.

Your task is to extract and organize information from the previous message
into the required structured format.

Guidelines:
- Be thorough in extraction but concise in expression
- Capture all relevant information
- Organize logically according to the output schema
- Maintain the original meaning and context
- Add appropriate metadata when relevant

Focus on accuracy and completeness."""),
        ("human", "{input}"),
    ]
)


# Analysis-focused prompt
ANALYSIS_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an analysis structuring expert.

Extract analytical insights from the previous message and organize them
into a structured analysis format.

Focus on:
- Key findings and patterns
- Supporting evidence
- Actionable recommendations
- Confidence levels
- Limitations or caveats

Be objective and evidence-based."""),
        ("human", "{input}"),
    ]
)


# Task-focused prompt
TASK_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a task structuring specialist.

Convert the previous message into a structured task format with clear
steps, requirements, and dependencies.

Focus on:
- Clear task description
- Actionable steps in logical order
- Requirements and prerequisites
- Time estimates
- Complexity assessment
- Dependencies between steps

Make the output actionable and clear."""),
        ("human", "{input}"),
    ]
)


# Decision-focused prompt
DECISION_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a decision structuring expert.

Extract decision-related information from the previous message and
organize it into a structured decision format.

Focus on:
- The core decision or choice
- Reasoning and justification
- Alternative options considered
- Pros and cons
- Confidence level
- Next steps

Present a balanced view of the decision."""),
        ("human", "{input}"),
    ]
)


# Generic extraction with custom context
def create_contextual_prompt(additional_context: str) -> ChatPromptTemplate:
    """Create a prompt with custom context for specific extraction needs.

    Args:
        additional_context: Additional instructions for extraction

    Returns:
        ChatPromptTemplate with the custom context
    """
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""You are a structured output converter.

Extract and organize information from the previous message
into the required structured format.

{additional_context}

Maintain accuracy and completeness in your extraction."""),
            ("human", "{input}"),
        ]
    )


# Prompt selector based on output model
PROMPT_MAPPING = {
    "GenericStructuredOutput": STRUCTURED_OUTPUT_PROMPT,
    "AnalysisOutput": ANALYSIS_PROMPT,
    "TaskOutput": TASK_PROMPT,
    "DecisionOutput": DECISION_PROMPT,
}


def get_prompt_for_model(
    model_name: str, custom_context: str | None = None
) -> ChatPromptTemplate:
    """Get the appropriate prompt for a given output model.

    Args:
        model_name: Name of the output model class
        custom_context: Optional custom context to override default

    Returns:
        ChatPromptTemplate for the model
    """
    if custom_context:
        return create_contextual_prompt(custom_context)

    return PROMPT_MAPPING.get(model_name, STRUCTURED_OUTPUT_PROMPT)
