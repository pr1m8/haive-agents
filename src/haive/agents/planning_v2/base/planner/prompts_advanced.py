"""Advanced prompt patterns for the planner using MessagesPlaceholder."""

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from haive.agents.planning_v2.base.planner.prompts import PLANNER_SYSTEM_MESSAGE

# Alternative approach using MessagesPlaceholder for maximum flexibility
planner_prompt_with_placeholder = ChatPromptTemplate.from_messages(
    [
        ("system", PLANNER_SYSTEM_MESSAGE),
        MessagesPlaceholder(
            "context_messages", optional=True
        ),  # Optional context messages
        (
            "human",
            """Please create a comprehensive plan for the following objective:

{objective}

Requirements:
- Break down the objective into clear, actionable steps
- Ensure all steps are specific and measurable
- Order steps logically with proper dependencies
- Include validation and verification steps
- Consider potential risks and mitigation strategies

Create a detailed plan that can be executed step-by-step to successfully achieve this objective.""",
        ),
    ]
)


# Another pattern: Using callable partials for dynamic context
def get_environment_context():
    """Dynamically generate context based on environment."""
    import os

    env = os.getenv("ENVIRONMENT", "development")

    contexts = {
        "development": "Focus on rapid prototyping and testing.",
        "staging": "Include comprehensive testing and rollback procedures.",
        "production": "Emphasize stability, monitoring, and zero-downtime deployment.",
    }

    return f"\nEnvironment Context: {contexts.get(env, 'Standard deployment practices.')}\n"


# Planner with dynamic environment context
planner_prompt_dynamic = ChatPromptTemplate.from_messages(
    [
        ("system", PLANNER_SYSTEM_MESSAGE),
        (
            "human",
            """Please create a comprehensive plan for the following objective:

{objective}
{env_context}
Requirements:
- Break down the objective into clear, actionable steps
- Ensure all steps are specific and measurable
- Order steps logically with proper dependencies
- Include validation and verification steps
- Consider potential risks and mitigation strategies

Create a detailed plan that can be executed step-by-step to successfully achieve this objective.""",
        ),
    ]
).partial(
    env_context=get_environment_context
)  # Callable partial!


# Example usage with MessagesPlaceholder
async def plan_with_context_messages(objective: str, context_items: list[str] = None):
    """Create a plan with optional context messages.

    Args:
        objective: The planning objective
        context_items: List of context strings to include as messages

    Returns:
        Plan result
    """
    from haive.agents.planning_v2.base.planner.agent import PlannerAgent

    # Build context messages if provided
    context_messages = []
    if context_items:
        for item in context_items:
            context_messages.append(SystemMessage(content=f"Context: {item}"))

    # Create planner with placeholder prompt
    planner = PlannerAgent(
        name="flexible_planner", prompt_template=planner_prompt_with_placeholder
    )

    # Run with optional context messages
    inputs = {"objective": objective}
    if context_messages:
        inputs["context_messages"] = context_messages

    return await planner.arun(inputs)
