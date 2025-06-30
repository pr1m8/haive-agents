"""Collaborative Conversation.

Multi-agent conversations focused on collaborative problem-solving and teamwork.

The collaborative conversation implements a specialized conversation pattern designed
for task-oriented teamwork and cooperative problem-solving between multiple agents.
This module enables:

- Joint task completion between specialized agents
- Role-based contributions to shared goals
- Brainstorming and idea refinement
- Consensus-building mechanisms
- Progress tracking toward objectives
- Final output synthesis from multiple contributors

Unlike debate or round-robin conversations, collaborative conversations emphasize
constructive cooperation toward a common objective rather than turn-taking or
dialectical exchange.

Features:
    - Task-oriented conversation structure
    - Role assignment and specialization
    - Work product tracking and versioning
    - Contribution assessment
    - Progress monitoring
    - Final deliverable synthesis
    - Configurable collaboration modes

Usage:
    Basic usage example::

        from haive.agents.conversation import CollaborativeConversation

        # Create a collaborative conversation for coding
        collab = CollaborativeConversation.create_team(
            objective="Design a REST API for a todo application",
            roles={
                "Architect": "Focus on overall system design and patterns",
                "Backend": "Define API endpoints and data models",
                "DevOps": "Consider deployment and scaling concerns"
            },
            max_rounds=5,
            output_format="markdown"
        )

        # Run the conversation
        result = collab.invoke()

        # Access collaboration results
        messages = result["messages"]
        final_output = result["work_product"]

Note:
    The collaborative conversation is particularly useful for:
    - Multi-agent problem solving with specialized roles
    - Simulating team dynamics and workflows
    - Producing composite outputs requiring diverse expertise
    - Brainstorming and idea refinement sessions
"""

from haive.agents.conversation.collaberative.agent import CollaborativeConversation
from haive.agents.conversation.collaberative.state import CollaborativeState

__all__ = ["CollaborativeConversation", "CollaborativeState"]
