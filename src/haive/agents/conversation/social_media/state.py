from typing import Dict, List, Literal, Set, Tuple

from haive.core.logging.rich_logger import LogLevel, get_logger
from pydantic import Field

from haive.agents.conversation.base.state import ConversationState

logger = get_logger(__name__)
logger.set_level(LogLevel.WARNING)


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
