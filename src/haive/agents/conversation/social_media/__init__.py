"""Social Media Conversation
=======================

Agent conversations that simulate social media platform interactions.

The social media conversation implements a specialized conversation pattern that mimics
typical social media interactions, including:

- Posts and threaded replies
- Reactions and engagement metrics
- User profiles and personas
- Content moderation mechanisms
- Network effects and virality patterns

This module enables the simulation of social media dynamics between multiple agent
personas, allowing for the study of information spread, content engagement, and
social interactions in a controlled environment.

Features:
--------
- Post and reply mechanics
- Like/reaction tracking
- Content engagement metrics
- Persona-based participants
- Configurable moderation rules
- Viral content simulation

Usage:
------
```python
from haive.agents.conversation import SocialMediaConversation

# Create a social media conversation
social = SocialMediaConversation.create_thread(
    original_poster="TechEnthusiast",
    topic="The Impact of Large Language Models",
    participants=["AI_Researcher", "Skeptic", "Educator", "Student"],
    max_depth=3,
    max_replies_per_post=5
)

# Run the conversation
result = social.invoke()

# Access conversation results
thread = result["thread"]
engagement = result["engagement_metrics"]
```

The social media conversation is particularly useful for:
- Simulating information spread and engagement
- Testing content moderation strategies
- Exploring social dynamics in online discussions
- Training agents to recognize and respond to social media patterns
"""

from haive.agents.conversation.social_media.agent import SocialMediaConversation
from haive.agents.conversation.social_media.models import Post, Reaction, Thread
from haive.agents.conversation.social_media.state import SocialMediaState

__all__ = ["Post", "Reaction", "SocialMediaConversation", "SocialMediaState", "Thread"]
