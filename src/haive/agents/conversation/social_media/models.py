# src/haive/agents/conversation/social_media.py
"""
Social media style conversation with likes, reactions, and viral mechanics.
"""

import logging
import random
from typing import Any, Dict, List, Literal, Optional, Set, Tuple

from pydantic import BaseModel, Field

from haive.agents.conversation.base.state import ConversationState

logger = logging.getLogger(__name__)


# Tool schemas for social media interactions
class LikePostInput(BaseModel):
    """Input for liking a post."""

    post_author: str = Field(description="Author of the post to like")
    reason: Optional[str] = Field(default=None, description="Reason for liking")


class ReplyPostInput(BaseModel):
    """Input for replying to a post."""

    reply_to: str = Field(description="Author to reply to")
    content: str = Field(description="Reply content")


class SharePostInput(BaseModel):
    """Input for sharing/retweeting a post."""

    original_author: str = Field(description="Original author of the post")
    comment: Optional[str] = Field(default=None, description="Comment when sharing")


class SocialMediaState(ConversationState):
    """Extended state for social media conversations."""

    # Social metrics
    likes: Dict[str, int] = Field(default_factory=dict)
    replies: Dict[str, List[str]] = Field(default_factory=dict)
    shares: Dict[str, int] = Field(default_factory=dict)
    followers: Dict[str, Set[str]] = Field(default_factory=dict)

    # Posting metrics
    posts_count: Dict[str, int] = Field(default_factory=dict)
    engagement_rate: Dict[str, float] = Field(default_factory=dict)

    # Viral mechanics
    viral_threshold: int = Field(default=10)
    trending_topics: List[str] = Field(default_factory=list)
    viral_posts: List[Tuple[str, str]] = Field(
        default_factory=list
    )  # (author, content)

    # Platform state
    platform_type: Literal["twitter", "instagram", "tiktok", "generic"] = Field(
        default="generic"
    )
    hashtags_used: Dict[str, List[str]] = Field(default_factory=dict)
