from enum import Enum
from typing import List, Dict, Any, Optional, Union
from pydantic import BaseModel, Field, field_validator

class DataSourceType(str, Enum):
    """Enumeration of data source types"""
    WEB = "web"
    GITHUB = "github"
    ACADEMIC = "academic"
    NEWS = "news"
    SOCIAL_MEDIA = "social_media"
    DOCUMENTS = "documents"
    API = "api"
    OTHER = "other"

class ContentReliability(str, Enum):
    """Enumeration of content reliability levels"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"

class ContentFreshness(str, Enum):
    """Enumeration of content freshness levels"""
    VERY_RECENT = "very_recent"  # Days
    RECENT = "recent"  # Weeks
    SOMEWHAT_RECENT = "somewhat_recent"  # Months
    OUTDATED = "outdated"  # Years
    UNKNOWN = "unknown"

class ResearchDepth(str, Enum):
    """Enumeration of research depth levels"""
    SUPERFICIAL = "superficial"
    INTERMEDIATE = "intermediate"
    DEEP = "deep"
    COMPREHENSIVE = "comprehensive"

class ResearchSource(BaseModel):
    """Model for tracking and evaluating research sources"""
    url: Optional[str] = Field(default=None, description="URL of the source")
    title: Optional[str] = Field(default=None, description="Title of the source")
    source_type: DataSourceType = Field(default=DataSourceType.WEB, description="Type of data source")
    content_snippet: Optional[str] = Field(default=None, description="Snippet of relevant content")
    reliability: ContentReliability = Field(default=ContentReliability.UNKNOWN, description="Assessed reliability")
    freshness: ContentFreshness = Field(default=ContentFreshness.UNKNOWN, description="Content freshness/recency")
    relevance_score: float = Field(default=0.0, ge=0.0, le=1.0, description="Relevance score (0.0 - 1.0)")
    citation: Optional[str] = Field(default=None, description="Formatted citation for the source")
    access_timestamp: Optional[str] = Field(default=None, description="When the source was accessed")
    
    @field_validator('relevance_score')
    def validate_relevance_score(cls, v):
        """Ensure relevance score is between 0 and 1"""
        return max(0.0, min(1.0, v))

class ResearchFinding(BaseModel):
    """Model for a specific research finding"""
    finding: str = Field(description="The actual finding or insight")
    confidence: float = Field(default=0.5, ge=0.0, le=1.0, description="Confidence in this finding (0.0 - 1.0)")
    sources: List[ResearchSource] = Field(default_factory=list, description="Sources supporting this finding")
    explanation: Optional[str] = Field(default=None, description="Explanation of the finding's significance")
    related_findings: List[str] = Field(default_factory=list, description="Related findings")
    
    @field_validator('confidence')
    def validate_confidence(cls, v):
        """Ensure confidence is between 0 and 1"""
        return max(0.0, min(1.0, v))

class ResearchSummary(BaseModel):
    """Summary of research findings and assessment"""
    topic: str = Field(description="Research topic")
    question: Optional[str] = Field(default=None, description="Specific research question")
    key_findings: List[ResearchFinding] = Field(default_factory=list, description="Key findings from research")
    sources_count: int = Field(default=0, description="Total number of sources consulted")
    high_reliability_sources: int = Field(default=0, description="Number of high reliability sources")
    recent_sources: int = Field(default=0, description="Number of recent sources")
    research_depth: ResearchDepth = Field(default=ResearchDepth.SUPERFICIAL, description="Overall research depth")
    contradictions: List[str] = Field(default_factory=list, description="Contradictory findings identified")
    confidence_score: float = Field(default=0.5, ge=0.0, le=1.0, description="Overall confidence score")
    limitations: List[str] = Field(default_factory=list, description="Research limitations")
    
    @field_validator('confidence_score')
    def validate_confidence_score(cls, v):
        """Ensure confidence score is between 0 and 1"""
        return max(0.0, min(1.0, v))
    
    def assess_depth(self) -> ResearchDepth:
        """Assess research depth based on source counts and diversity"""
        if self.sources_count >= 20 and self.high_reliability_sources >= 10:
            return ResearchDepth.COMPREHENSIVE
        elif self.sources_count >= 10 and self.high_reliability_sources >= 5:
            return ResearchDepth.DEEP
        elif self.sources_count >= 5 and self.high_reliability_sources >= 2:
            return ResearchDepth.INTERMEDIATE
        else:
            return ResearchDepth.SUPERFICIAL

class DataSourceConfig(BaseModel):
    """Configuration for a data source"""
    name: str = Field(description="Name of the data source")
    source_type: DataSourceType = Field(description="Type of data source")
    enabled: bool = Field(default=True, description="Whether this source is enabled")
    priority: int = Field(default=5, ge=1, le=10, description="Priority (1-10, higher = more important)")
    api_key: Optional[str] = Field(default=None, description="API key for the data source if required")
    max_results: int = Field(default=10, description="Maximum number of results to return")
    search_params: Dict[str, Any] = Field(default_factory=dict, description="Custom search parameters")

    @field_validator('priority')
    def validate_priority(cls, v):
        """Ensure priority is between 1 and 10"""
        return max(1, min(10, v)) 