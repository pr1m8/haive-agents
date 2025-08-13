"""Planner Prompts - Advanced prompt templates for strategic planning.

This module provides sophisticated prompt templates designed for creating
comprehensive, actionable plans using modern prompt engineering techniques.
"""

from langchain_core.prompts import ChatPromptTemplate

# ============================================================================
# SYSTEM MESSAGES - Core Planner Identity and Capabilities
# ============================================================================

STRATEGIC_PLANNER_SYSTEM_MESSAGE = """You are an expert strategic planner with deep expertise in task decomposition, workflow optimization, and project management.

## Your Core Capabilities

**Planning Expertise:**
- Break down complex objectives into clear, actionable steps
- Identify optimal sequencing and dependencies
- Estimate effort and resource requirements
- Consider risk factors and mitigation strategies
- Design plans that are both thorough and practical

**Analysis Skills:**
- Understand implicit requirements and constraints
- Identify critical path dependencies
- Recognize when parallel vs sequential execution is optimal
- Anticipate potential failure points and plan accordingly

**Communication Style:**
- Be specific and actionable in all step descriptions
- Provide clear reasoning for planning decisions
- Include measurable success criteria
- Use professional, clear language

## Planning Principles

1. **CLARITY**: Every step must be unambiguous and actionable
2. **COMPLETENESS**: Address all aspects of the objective thoroughly
3. **EFFICIENCY**: Optimize for the shortest path to success
4. **RESILIENCE**: Consider what could go wrong and plan accordingly
5. **MEASURABILITY**: Include clear success criteria and expected outcomes

## Output Requirements

You must always provide:
- A comprehensive list of specific, actionable steps
- Clear reasoning for your planning approach
- Explicit success criteria for the overall objective
- Tool requirements for each step
- Priority levels and time estimates when relevant
- Risk factors and dependencies when applicable

Remember: Your plans will be executed by other agents, so be extremely clear and specific about what needs to be done at each step."""

RESEARCH_PLANNER_SYSTEM_MESSAGE = """You are a specialized research planning expert who excels at designing comprehensive information gathering and analysis workflows.

## Research Planning Expertise

**Information Architecture:**
- Design systematic information gathering strategies
- Plan for comprehensive source coverage
- Structure analysis workflows for maximum insight
- Organize findings for clear presentation

**Research Methodology:**
- Use proven research methodologies and frameworks
- Plan for data validation and cross-referencing
- Design comparative analysis approaches
- Structure synthesis and summarization workflows

**Quality Assurance:**
- Plan for source credibility assessment
- Include fact-checking and verification steps
- Design peer review and validation processes
- Ensure comprehensive coverage of the topic

Focus on creating research plans that are systematic, thorough, and yield high-quality, reliable insights."""

CREATIVE_PLANNER_SYSTEM_MESSAGE = """You are a creative planning specialist who excels at designing innovative, non-linear workflows for creative and analytical tasks.

## Creative Planning Approach

**Innovation Focus:**
- Design workflows that encourage creative exploration
- Plan for iterative refinement and improvement
- Include brainstorming and ideation phases
- Structure feedback and revision cycles

**Flexibility:**
- Create plans that can adapt to emerging insights
- Allow for creative detours and exploration
- Plan for multiple solution pathways
- Include experimentation and testing phases

**Quality Enhancement:**
- Plan for multiple drafts and iterations
- Include review and refinement cycles
- Structure feedback incorporation processes
- Design for continuous improvement

Focus on creating plans that balance structure with creative freedom, ensuring both innovation and practical execution."""

# ============================================================================
# PROMPT TEMPLATES - Context-Aware Planning Prompts
# ============================================================================

BASIC_PLANNING_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", STRATEGIC_PLANNER_SYSTEM_MESSAGE),
        (
            "human",
            """Please create a comprehensive plan for this objective:

**Objective:** {objective}

**Available Tools:** {available_tools}
**Complexity Level:** {complexity_level}
**Time Constraints:** {time_constraints}

Create a detailed plan that addresses this objective thoroughly. Consider the available tools, time constraints, and desired complexity level in your planning.""",
        ),
    ]
)

RESEARCH_PLANNING_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", RESEARCH_PLANNER_SYSTEM_MESSAGE),
        (
            "human",
            """Design a comprehensive research plan for this objective:

**Research Objective:** {objective}

**Available Research Tools:** {available_tools}
**Domain Focus:** {domain_focus}
**Complexity Level:** {complexity_level}
**Time Constraints:** {time_constraints}

Create a systematic research plan that will yield comprehensive, reliable insights on this topic. Focus on information gathering, analysis, and synthesis.""",
        ),
    ]
)

CREATIVE_PLANNING_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", CREATIVE_PLANNER_SYSTEM_MESSAGE),
        (
            "human",
            """Design an innovative approach for this creative objective:

**Creative Objective:** {objective}

**Available Tools:** {available_tools}
**Creative Domain:** {domain_focus}
**Complexity Level:** {complexity_level}
**Time Constraints:** {time_constraints}

Create a plan that balances creative exploration with practical execution. Include ideation, development, and refinement phases.""",
        ),
    ]
)

ADAPTIVE_PLANNING_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", STRATEGIC_PLANNER_SYSTEM_MESSAGE),
        (
            "human",
            """Create an adaptive plan considering previous attempts:

**Objective:** {objective}

**Available Tools:** {available_tools}
**Previous Attempts:** {previous_attempts}
**Lessons Learned:** {lessons_learned}
**Time Constraints:** {time_constraints}

Based on the previous attempts and lessons learned, create an improved plan that addresses the identified issues and builds on successful approaches.""",
        ),
    ]
)

CONTEXTUAL_PLANNING_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", STRATEGIC_PLANNER_SYSTEM_MESSAGE),
        (
            "human",
            """Create a contextual plan with full situational awareness:

**Primary Objective:** {objective}

**Context Information:**
- Available Tools: {available_tools}
- Domain Focus: {domain_focus}
- Complexity Level: {complexity_level}
- Time Constraints: {time_constraints}
- Risk Tolerance: {risk_tolerance}
- Success Metrics: {success_metrics}

**Additional Context:**
{additional_context}

Create a comprehensive plan that takes all contextual factors into account. Adapt your planning approach based on the specific domain, constraints, and requirements.""",
        ),
    ]
)

# ============================================================================
# PROMPT SELECTION LOGIC
# ============================================================================


def get_planning_template(
    objective: str,
    domain_focus: str = None,
    has_previous_attempts: bool = False,
    additional_context: str = None,
) -> ChatPromptTemplate:
    """Select the most appropriate planning template based on context.

    Args:
        objective: The planning objective
        domain_focus: Specific domain or area of focus
        has_previous_attempts: Whether there were previous planning attempts
        additional_context: Any additional context information

    Returns:
        ChatPromptTemplate: The most suitable template for the context

    Examples:
        Research planning::

            template = get_planning_template(
                objective="Research AI trends",
                domain_focus="artificial_intelligence"
            )

        Adaptive planning::

            template = get_planning_template(
                objective="Complete analysis",
                has_previous_attempts=True
            )
    """
    # If there are previous attempts, use adaptive planning
    if has_previous_attempts:
        return ADAPTIVE_PLANNING_TEMPLATE

    # If there's extensive additional context, use contextual planning
    if additional_context and len(additional_context) > 100:
        return CONTEXTUAL_PLANNING_TEMPLATE

    # Domain-specific template selection
    if domain_focus:
        domain_lower = domain_focus.lower()

        if any(
            keyword in domain_lower
            for keyword in ["research", "analysis", "investigation", "study", "survey"]
        ):
            return RESEARCH_PLANNING_TEMPLATE

        if any(
            keyword in domain_lower
            for keyword in [
                "creative",
                "design",
                "writing",
                "art",
                "innovation",
                "brainstorm",
            ]
        ):
            return CREATIVE_PLANNING_TEMPLATE

    # Check objective content for template hints
    objective_lower = objective.lower()

    if any(
        keyword in objective_lower
        for keyword in [
            "research",
            "analyze",
            "investigate",
            "study",
            "find information",
        ]
    ):
        return RESEARCH_PLANNING_TEMPLATE

    if any(
        keyword in objective_lower
        for keyword in [
            "create",
            "design",
            "write",
            "brainstorm",
            "innovate",
            "develop",
        ]
    ):
        return CREATIVE_PLANNING_TEMPLATE

    # Default to basic planning template
    return BASIC_PLANNING_TEMPLATE


# ============================================================================
# PROMPT UTILITIES
# ============================================================================


def format_tools_list(tools: list) -> str:
    """Format tools list for inclusion in prompts.

    Args:
        tools: List of available tools

    Returns:
        str: Formatted tools description
    """
    if not tools:
        return "No specific tools available"

    if len(tools) == 1:
        return f"Available tool: {tools[0]}"

    return f"Available tools: {', '.join(tools)}"


def format_previous_attempts(attempts: list) -> str:
    """Format previous attempts for inclusion in prompts.

    Args:
        attempts: List of previous attempt descriptions

    Returns:
        str: Formatted previous attempts description
    """
    if not attempts:
        return "No previous attempts"

    formatted = []
    for i, attempt in enumerate(attempts, 1):
        formatted.append(f"{i}. {attempt}")

    return "\n".join(formatted)


def create_planning_context(
    objective: str,
    available_tools: list = None,
    domain_focus: str = None,
    complexity_level: str = "moderate",
    time_constraints: str = None,
    previous_attempts: list = None,
    additional_context: str = None,
) -> dict:
    """Create a complete context dictionary for planning prompts.

    Args:
        objective: The main objective
        available_tools: Tools available for execution
        domain_focus: Specific domain focus
        complexity_level: Desired complexity level
        time_constraints: Time limitations
        previous_attempts: Previous planning attempts
        additional_context: Additional context information

    Returns:
        dict: Complete context for planning prompts

    Examples:
        Basic context::

            context = create_planning_context(
                objective="Research market trends",
                available_tools=["web_search", "calculator"],
                complexity_level="detailed"
            )

        Advanced context::

            context = create_planning_context(
                objective="Analyze competitor strategy",
                available_tools=["web_search", "document_reader"],
                domain_focus="business_analysis",
                time_constraints="Complete within 2 hours",
                previous_attempts=["Initial research was too broad"]
            )
    """
    return {
        "objective": objective,
        "available_tools": format_tools_list(available_tools or []),
        "domain_focus": domain_focus or "general",
        "complexity_level": complexity_level,
        "time_constraints": time_constraints or "No specific time constraints",
        "previous_attempts": format_previous_attempts(previous_attempts or []),
        "lessons_learned": (
            "Apply lessons from previous attempts"
            if previous_attempts
            else "No previous lessons"
        ),
        "additional_context": additional_context or "No additional context",
        "risk_tolerance": "moderate",
        "success_metrics": "Successful completion of the objective",
    }
