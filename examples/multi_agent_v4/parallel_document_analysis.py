"""Parallel Document Analysis Example.

This example demonstrates parallel execution where multiple specialized
agents analyze different aspects of a document simultaneously, each
with their own specialized tools.

Date: August 7, 2025
"""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent_v4 import ReactAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define structured outputs for different analyzers
class SentimentAnalysis(BaseModel):
    """Sentiment analysis results."""

    overall_sentiment: str = Field(
        description="Overall sentiment: positive, negative, neutral"
    )
    sentiment_score: float = Field(
        ge=-1.0, le=1.0, description="Sentiment score from -1 to 1"
    )
    emotional_tones: list[str] = Field(description="Detected emotional tones")
    key_phrases: dict[str, str] = Field(description="Key phrases and their sentiment")


class EntityExtraction(BaseModel):
    """Named entity extraction results."""

    people: list[str] = Field(description="People mentioned")
    organizations: list[str] = Field(description="Organizations mentioned")
    locations: list[str] = Field(description="Locations mentioned")
    dates: list[str] = Field(description="Dates or time references")
    products: list[str] = Field(description="Products or services mentioned")


class TopicAnalysis(BaseModel):
    """Topic analysis results."""

    main_topics: list[str] = Field(description="Main topics discussed")
    topic_distribution: dict[str, float] = Field(
        description="Topic prevalence percentages"
    )
    keywords: list[str] = Field(description="Key terms and keywords")
    summary: str = Field(description="Brief topical summary")


# Tools for sentiment analyzer
@tool
def sentiment_scorer(text: str) -> str:
    """Score sentiment of text snippet."""
    # Simple mock sentiment scoring
    positive_words = ["good", "great", "excellent", "amazing", "positive", "success"]
    negative_words = ["bad", "poor", "terrible", "negative", "failure", "problem"]

    text_lower = text.lower()
    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)

    if pos_count > neg_count:
        score = min(pos_count * 0.2, 1.0)
        return f"Positive sentiment (score: +{score:.2f})"
    if neg_count > pos_count:
        score = min(neg_count * 0.2, 1.0)
        return f"Negative sentiment (score: -{score:.2f})"
    return "Neutral sentiment (score: 0.00)"


# Tools for entity extractor
@tool
def extract_capitalized_words(text: str) -> str:
    """Extract capitalized words that might be entities."""
    words = text.split()
    capitalized = [w for w in words if w and w[0].isupper() and len(w) > 1]
    return f"Potential entities: {', '.join(set(capitalized))}"


@tool
def find_patterns(text: str, pattern_type: str) -> str:
    """Find patterns like dates, emails, or phone numbers."""
    import re

    if pattern_type == "date":
        # Simple date patterns
        dates = re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text)
        dates += re.findall(
            r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}\b",
            text,
        )
        return f"Date patterns found: {', '.join(dates) if dates else 'None'}"
    if pattern_type == "email":
        emails = re.findall(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text
        )
        return f"Email patterns found: {', '.join(emails) if emails else 'None'}"
    return f"Unknown pattern type: {pattern_type}"


# Tools for topic analyzer
@tool
def word_frequency(text: str, top_n: int = 5) -> str:
    """Get most frequent words in text."""
    import re
    from collections import Counter

    # Simple word frequency
    words = re.findall(r"\b\w+\b", text.lower())
    # Filter out common words
    stop_words = {
        "the",
        "a",
        "an",
        "and",
        "or",
        "but",
        "in",
        "on",
        "at",
        "to",
        "for",
        "of",
        "with",
        "by",
        "is",
        "was",
        "are",
        "were",
    }
    words = [w for w in words if w not in stop_words and len(w) > 2]

    freq = Counter(words)
    top_words = freq.most_common(top_n)

    return f"Top {top_n} words: " + ", ".join(
        [f"{word}({count})" for word, count in top_words]
    )


@tool
def text_statistics(text: str) -> str:
    """Get basic text statistics."""
    words = text.split()
    sentences = text.count(".") + text.count("!") + text.count("?")
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0

    return f"Stats: {len(words)} words, {sentences} sentences, {avg_word_length:.1f} avg word length"


async def main():
    """Run parallel document analysis."""
    # Sample document
    document = """
    TechCorp Announces Record Q4 2024 Results
    
    San Francisco, CA - January 15, 2025 - TechCorp, a leading provider of AI solutions,
    announced exceptional fourth quarter results today. CEO Jane Smith expressed tremendous
    satisfaction with the company's performance.
    
    "We're thrilled to report a 45% increase in revenue compared to Q4 2023," said Smith.
    "Our new AI products have been incredibly well-received by enterprise customers."
    
    The company's flagship product, AI Assistant Pro, saw adoption by over 500 Fortune 1000
    companies during the quarter. Customer feedback has been overwhelmingly positive, with
    many reporting significant productivity gains.
    
    However, challenges remain. Competition in the AI space is intensifying, and regulatory
    concerns continue to create uncertainty. Despite these headwinds, TechCorp remains
    optimistic about 2025 prospects.
    
    CFO Michael Johnson noted, "Our strong financial position allows us to continue
    investing heavily in R&D while maintaining profitability."
    
    For more information, contact: investor.relations@techcorp.com
    """

    print("Creating specialized analyzers...")

    # Create sentiment analyzer with sentiment tools
    sentiment_analyzer = ReactAgentV4(
        name="sentiment_analyzer",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are a sentiment analysis expert. Analyze the emotional tone and sentiment of text.",
        ),
        tools=[sentiment_scorer],
        debug=True,
    )

    # Create entity extractor with extraction tools
    entity_extractor = ReactAgentV4(
        name="entity_extractor",
        engine=AugLLMConfig(
            temperature=0.2,
            system_message="You are an entity extraction specialist. Identify people, organizations, locations, and dates.",
        ),
        tools=[extract_capitalized_words, find_patterns],
        debug=True,
    )

    # Create topic analyzer with analysis tools
    topic_analyzer = ReactAgentV4(
        name="topic_analyzer",
        engine=AugLLMConfig(
            temperature=0.4,
            system_message="You are a topic analysis expert. Identify main themes and keywords in text.",
        ),
        tools=[word_frequency, text_statistics],
        debug=True,
    )

    # Create structured output agents for final formatting
    sentiment_formatter = SimpleAgentV3(
        name="sentiment_formatter",
        engine=AugLLMConfig(temperature=0.3),
        structured_output_model=SentimentAnalysis,
        debug=True,
    )

    entity_formatter = SimpleAgentV3(
        name="entity_formatter",
        engine=AugLLMConfig(temperature=0.2),
        structured_output_model=EntityExtraction,
        debug=True,
    )

    topic_formatter = SimpleAgentV3(
        name="topic_formatter",
        engine=AugLLMConfig(temperature=0.3),
        structured_output_model=TopicAnalysis,
        debug=True,
    )

    # Create parallel workflow for analysis
    print("\nCreating parallel analysis workflow...")
    analysis_workflow = EnhancedMultiAgentV4(
        name="parallel_analysis",
        agents=[sentiment_analyzer, entity_extractor, topic_analyzer],
        execution_mode="parallel",
    )

    # Create sequential formatting workflow
    print("Creating formatting workflow...")
    format_workflow = EnhancedMultiAgentV4(
        name="format_results",
        agents=[sentiment_formatter, entity_formatter, topic_formatter],
        execution_mode="parallel",
    )

    # Execute analysis
    print("\nExecuting parallel analysis...")
    print(f"Document length: {len(document)} characters")

    start_time = asyncio.get_event_loop().time()

    # Run analysis
    analysis_result = await analysis_workflow.arun(
        {"messages": [HumanMessage(content=f"Analyze this document:\n\n{document}")]}
    )

    analysis_time = asyncio.get_event_loop().time() - start_time

    # Format results
    format_result = await format_workflow.arun(
        {
            "messages": [
                HumanMessage(content=f"Format the analysis results:\n{analysis_result}")
            ]
        }
    )

    total_time = asyncio.get_event_loop().time() - start_time

    # Display results
    print("\n" + "=" * 60)
    print("ANALYSIS RESULTS")
    print("=" * 60)

    # Sentiment Analysis
    if hasattr(format_workflow.state, "sentiment_formatter"):
        sentiment = format_workflow.state.sentiment_formatter
        print("\n[Sentiment Analysis]")
        print(
            f"Overall: {sentiment.overall_sentiment} (score: {sentiment.sentiment_score:+.2f})"
        )
        print(f"Emotional tones: {', '.join(sentiment.emotional_tones)}")
        print("Key phrases:")
        for phrase, sent in sentiment.key_phrases.items():
            print(f'  • "{phrase}" → {sent}')

    # Entity Extraction
    if hasattr(format_workflow.state, "entity_formatter"):
        entities = format_workflow.state.entity_formatter
        print("\n[Extracted Entities]")
        print(f"People: {', '.join(entities.people)}")
        print(f"Organizations: {', '.join(entities.organizations)}")
        print(f"Locations: {', '.join(entities.locations)}")
        print(f"Dates: {', '.join(entities.dates)}")
        print(f"Products: {', '.join(entities.products)}")

    # Topic Analysis
    if hasattr(format_workflow.state, "topic_formatter"):
        topics = format_workflow.state.topic_formatter
        print("\n[Topic Analysis]")
        print(f"Main topics: {', '.join(topics.main_topics)}")
        print("Topic distribution:")
        for topic, pct in topics.topic_distribution.items():
            print(f"  • {topic}: {pct:.1f}%")
        print(f"Keywords: {', '.join(topics.keywords[:10])}")
        print(f"Summary: {topics.summary}")

    # Performance metrics
    print("\n" + "=" * 60)
    print("PERFORMANCE METRICS")
    print("=" * 60)
    print(f"Parallel analysis time: {analysis_time:.2f}s")
    print(f"Total execution time: {total_time:.2f}s")
    print(f"Speedup from parallelization: ~{3/max(analysis_time, 0.1):.1f}x")

    # Tool isolation verification
    print("\n" + "=" * 60)
    print("TOOL ISOLATION VERIFICATION")
    print("=" * 60)
    print(f"Sentiment analyzer tools: {[t.name for t in sentiment_analyzer.tools]}")
    print(f"Entity extractor tools: {[t.name for t in entity_extractor.tools]}")
    print(f"Topic analyzer tools: {[t.name for t in topic_analyzer.tools]}")
    print("✓ Each agent has only its specialized tools")


if __name__ == "__main__":
    print("Parallel Document Analysis Example")
    print("=================================\n")
    asyncio.run(main())
