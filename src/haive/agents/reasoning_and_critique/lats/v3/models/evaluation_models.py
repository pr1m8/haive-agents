"""Evaluation and reflection models for LATS algorithm."""

from pydantic import BaseModel, Field


class ScoredAction(BaseModel):
    """An action with its evaluation score and reasoning."""

    action: str = Field(description="The action that was evaluated")
    score: float = Field(
        description="Quality score for this action (0.0-1.0)", ge=0.0, le=1.0
    )
    reasoning: str = Field(description="Detailed reasoning behind the score")

    # Solution assessment
    is_solution: bool = Field(
        description="Whether this action leads to a complete solution"
    )
    has_errors: bool = Field(description="Whether this action contains obvious errors")
    needs_refinement: bool = Field(
        description="Whether this action needs further refinement"
    )

    # Strategic assessment
    strategic_value: float = Field(
        description="Long-term strategic value of this action (0.0-1.0)", ge=0.0, le=1.0
    )
    risk_level: float = Field(
        description="Risk level of this action (0.0=safe, 1.0=risky)", ge=0.0, le=1.0
    )


class ReflectionEvaluation(BaseModel):
    """Structured output for reflecting on and evaluating candidate actions."""

    evaluation_context: str = Field(
        description="Context and criteria used for evaluation"
    )

    scored_actions: list[ScoredAction] = Field(
        description="Actions with their scores and reasoning", min_items=1
    )

    ranking_rationale: str = Field(
        description="Explanation of how actions were ranked and why"
    )

    best_action_recommendation: str = Field(
        description="Which action is recommended and why"
    )

    # Search guidance
    search_insights: str = Field(
        description="Insights about the search direction and what to explore next"
    )

    termination_recommendation: str = Field(
        description="Whether to continue searching or terminate (and why)"
    )


class UCBSelection(BaseModel):
    """Upper Confidence Bound selection decision."""

    selected_node_id: str = Field(description="ID of the selected node")
    selection_reasoning: str = Field(description="Why this node was selected")

    # UCB calculation details
    ucb_score: float = Field(description="UCB score of the selected node")
    exploitation_component: float = Field(description="Exploitation part of UCB score")
    exploration_component: float = Field(description="Exploration part of UCB score")

    # Alternative nodes considered
    alternative_nodes: list[dict] = Field(
        default_factory=list,
        description="Other nodes that were considered with their UCB scores",
    )

    # Search strategy insights
    strategy_notes: str = Field(
        description="Notes about the current search strategy and direction"
    )
