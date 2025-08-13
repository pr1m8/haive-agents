#!/usr/bin/env python3
"""Funky Prompt Template Examples.

This demonstrates creative ways to use prompt templates that map to various state keys,
showing how agents can use different input patterns beyond just 'messages'.

Date: August 7, 2025
"""

import asyncio
from datetime import datetime
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema import StateSchema
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3


# Custom state schemas with funky fields
class RecipeState(StateSchema):
    """State for recipe generation."""

    ingredients: list[str] = Field(default_factory=list)
    cuisine_type: str = Field(default="")
    dietary_restrictions: list[str] = Field(default_factory=list)
    cooking_time_minutes: int = Field(default=30)
    skill_level: str = Field(default="intermediate")
    kitchen_tools: list[str] = Field(default_factory=list)
    mood: str = Field(default="adventurous")


class StoryState(StateSchema):
    """State for story generation."""

    protagonist_name: str = Field(default="")
    protagonist_traits: list[str] = Field(default_factory=list)
    setting_description: str = Field(default="")
    genre: str = Field(default="")
    plot_twist_required: bool = Field(default=True)
    target_word_count: int = Field(default=500)
    emotional_arc: str = Field(default="")
    forbidden_words: list[str] = Field(default_factory=list)


class CodeReviewState(StateSchema):
    """State for code review."""

    code_snippet: str = Field(default="")
    programming_language: str = Field(default="")
    review_focus_areas: list[str] = Field(default_factory=list)
    severity_threshold: str = Field(default="medium")
    suggest_refactoring: bool = Field(default=True)
    check_patterns: dict[str, bool] = Field(default_factory=dict)
    context_description: str = Field(default="")


# Structured outputs
class Recipe(BaseModel):
    """Generated recipe."""

    name: str = Field(description="Recipe name")
    prep_time: int = Field(description="Prep time in minutes")
    cook_time: int = Field(description="Cook time in minutes")
    ingredients_list: list[str] = Field(description="Ingredients with quantities")
    instructions: list[str] = Field(description="Step-by-step instructions")
    difficulty: str = Field(description="Difficulty level")
    tips: list[str] = Field(description="Cooking tips")


class Story(BaseModel):
    """Generated story."""

    title: str = Field(description="Story title")
    content: str = Field(description="Full story content")
    word_count: int = Field(description="Actual word count")
    themes: list[str] = Field(description="Main themes")
    plot_twist_location: str = Field(description="Where the twist occurs")


class CodeReview(BaseModel):
    """Code review results."""

    overall_quality: str = Field(description="Overall code quality assessment")
    issues_found: list[dict[str, str]] = Field(description="List of issues")
    refactoring_suggestions: list[str] = Field(description="Refactoring ideas")
    positive_aspects: list[str] = Field(description="What's done well")
    security_concerns: list[str] = Field(description="Security issues if any")


async def funky_recipe_agent():
    """Demonstrate recipe agent with complex prompt template."""
    print("\n🍳 FUNKY RECIPE AGENT")
    print("=" * 60)

    # Create agent with funky prompt template using multiple state fields
    recipe_agent = SimpleAgentV3(
        name="master_chef",
        engine=AugLLMConfig(
            temperature=0.7,
            system_message="You are a creative chef who adapts recipes based on constraints.",
            structured_output_model=Recipe,
        ),
        state_schema=RecipeState,
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Create a recipe with these requirements:

🥘 Cuisine Type: {cuisine_type}
📝 Available Ingredients: {ingredients}
⏱️ Maximum Cooking Time: {cooking_time_minutes} minutes
🎯 Skill Level: {skill_level}
🚫 Dietary Restrictions: {dietary_restrictions}
🔧 Kitchen Tools Available: {kitchen_tools}
😊 Cooking Mood: {mood}

Special Instructions:
- The recipe should match the {mood} mood
- Must use at least 3 of the provided ingredients
- Should be achievable with the listed kitchen tools
- Keep it within the time limit
- Respect all dietary restrictions

Be creative and make it delicious!""",
                ),
            ]
        ),
    )

    # Execute with funky state inputs
    result = await recipe_agent.arun(
        {
            "ingredients": [
                "chickpeas",
                "tahini",
                "lemon",
                "garlic",
                "cumin",
                "olive oil",
                "paprika",
            ],
            "cuisine_type": "Middle Eastern Fusion",
            "dietary_restrictions": ["vegan", "gluten-free"],
            "cooking_time_minutes": 25,
            "skill_level": "beginner",
            "kitchen_tools": ["food processor", "mixing bowl", "measuring cups"],
            "mood": "adventurous but healthy",
        }
    )

    print(f"✨ Recipe: {result.name}")
    print(f"⏱️  Total Time: {result.prep_time + result.cook_time} min")
    print(f"📊 Difficulty: {result.difficulty}")
    print("\n🥗 Ingredients:")
    for ing in result.ingredients_list[:3]:
        print(f"   • {ing}")
    print(f"   ... and {len(result.ingredients_list) - 3} more")
    print(f"\n💡 Tips: {result.tips[0] if result.tips else 'None'}")


async def funky_story_agent():
    """Demonstrate story agent with creative constraints."""
    print("\n\n📚 FUNKY STORY AGENT")
    print("=" * 60)

    story_agent = SimpleAgentV3(
        name="story_weaver",
        engine=AugLLMConfig(
            temperature=0.8,
            system_message="You are a creative writer who crafts stories with specific constraints.",
            structured_output_model=Story,
        ),
        state_schema=StoryState,
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Write a {genre} story with these elements:

👤 Protagonist: {protagonist_name}
✨ Character Traits: {protagonist_traits}
🌍 Setting: {setting_description}
📊 Target Length: {target_word_count} words
🎭 Emotional Arc: {emotional_arc}
🌀 Plot Twist: {"REQUIRED - surprise the reader!" if plot_twist_required else "optional"}

⚠️ FORBIDDEN WORDS (do not use these): {forbidden_words}

Make the story engaging and ensure the emotional arc progresses from {emotional_arc}.
The protagonist should clearly demonstrate their traits throughout the story.""",
                ),
            ]
        ),
    )

    result = await story_agent.arun(
        {
            "protagonist_name": "Dr. Elena Vasquez",
            "protagonist_traits": ["brilliant", "socially awkward", "secretly kind"],
            "setting_description": "A floating research station above Jupiter's clouds",
            "genre": "soft science fiction",
            "plot_twist_required": True,
            "target_word_count": 300,
            "emotional_arc": "isolation → connection → sacrifice",
            "forbidden_words": ["suddenly", "very", "really", "just"],
        }
    )

    print(f"📖 Title: {result.title}")
    print(f"📏 Word Count: {result.word_count}")
    print(f"🎭 Themes: {', '.join(result.themes)}")
    print(f"🌀 Plot Twist: {result.plot_twist_location}")
    print("\n📄 Story Preview:")
    print(f"{result.content[:150]}...")


async def funky_code_review_agent():
    """Demonstrate code review with complex pattern matching."""
    print("\n\n🔍 FUNKY CODE REVIEW AGENT")
    print("=" * 60)

    review_agent = SimpleAgentV3(
        name="code_critic",
        engine=AugLLMConfig(
            temperature=0.2,
            system_message="You are a thorough code reviewer with high standards.",
            structured_output_model=CodeReview,
        ),
        state_schema=CodeReviewState,
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Review this {programming_language} code:

```{programming_language}
{code_snippet}
```

📋 Context: {context_description}
🎯 Focus Areas: {review_focus_areas}
⚠️ Severity Threshold: {severity_threshold}
🔧 Suggest Refactoring: {suggest_refactoring}

Pattern Checks Required:
{check_patterns}

Provide a thorough review considering:
1. Code quality and readability
2. Potential bugs or issues
3. Performance implications
4. Security concerns
5. Best practices for {programming_language}

Be {"extremely strict" if severity_threshold == "high" else "balanced"} in your review.""",
                ),
            ]
        ),
    )

    result = await review_agent.arun(
        {
            "code_snippet": """
def process_user_data(users):
    result = []
    for user in users:
        if user['age'] > 18:
            user['status'] = 'adult'
            result.append(user)
    return result
""",
            "programming_language": "Python",
            "review_focus_areas": ["error handling", "performance", "security"],
            "severity_threshold": "high",
            "suggest_refactoring": True,
            "check_patterns": {
                "uses_type_hints": True,
                "has_docstrings": True,
                "follows_naming_conventions": True,
                "handles_edge_cases": True,
            },
            "context_description": "Part of a user management system handling sensitive data",
        }
    )

    print(f"🎯 Overall Quality: {result.overall_quality}")
    print(f"\n❌ Issues Found: {len(result.issues_found)}")
    for issue in result.issues_found[:2]:
        print(f"   • {issue.get('type', 'Issue')}: {issue.get('description', '')}")
    print("\n✅ Positive Aspects:")
    for aspect in result.positive_aspects[:2]:
        print(f"   • {aspect}")
    print(f"\n🔒 Security Concerns: {len(result.security_concerns)}")


async def multi_modal_funky_agent():
    """Demonstrate agent that combines multiple funky inputs."""
    print("\n\n🎨 MULTI-MODAL FUNKY AGENT")
    print("=" * 60)

    class MultiModalState(StateSchema):
        """State with various input types."""

        timestamp: datetime = Field(default_factory=datetime.now)
        user_preferences: dict[str, Any] = Field(default_factory=dict)
        numerical_data: list[float] = Field(default_factory=list)
        boolean_flags: dict[str, bool] = Field(default_factory=dict)
        nested_config: dict[str, dict[str, Any]] = Field(default_factory=dict)

    class Analysis(BaseModel):
        """Multi-modal analysis result."""

        summary: str
        insights: list[str]
        recommendations: dict[str, str]
        confidence_scores: dict[str, float]

    analyzer = SimpleAgentV3(
        name="multi_modal_analyzer",
        engine=AugLLMConfig(
            temperature=0.4,
            system_message="Analyze complex multi-modal inputs comprehensively.",
            structured_output_model=Analysis,
        ),
        state_schema=MultiModalState,
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Analyze this multi-modal data:

⏰ Timestamp: {timestamp}

👤 User Preferences:
{user_preferences}

📊 Numerical Data Points: {numerical_data}

🎛️ Feature Flags:
{boolean_flags}

🔧 Nested Configuration:
{nested_config}

Provide comprehensive analysis considering:
- Temporal patterns based on the timestamp
- User preference implications
- Statistical insights from numerical data
- Feature flag combinations and their effects
- Configuration complexity and optimization opportunities""",
                ),
            ]
        ),
    )

    result = await analyzer.arun(
        {
            "timestamp": datetime.now(),
            "user_preferences": {
                "theme": "dark",
                "language": "en-US",
                "notifications": "minimal",
                "data_sharing": "anonymous",
            },
            "numerical_data": [23.5, 45.2, 67.8, 34.1, 56.7, 78.9],
            "boolean_flags": {
                "premium_user": True,
                "beta_features": True,
                "analytics_enabled": False,
                "two_factor_auth": True,
            },
            "nested_config": {
                "api_settings": {"rate_limit": 1000, "timeout": 30, "retry_count": 3},
                "cache_config": {
                    "ttl": 3600,
                    "max_size": "1GB",
                    "eviction_policy": "LRU",
                },
            },
        }
    )

    print(f"📊 Summary: {result.summary[:100]}...")
    print("\n💡 Key Insights:")
    for insight in result.insights[:2]:
        print(f"   • {insight}")
    print(f"\n🎯 Top Recommendation: {list(result.recommendations.values())[0]}")


async def main():
    """Run all funky prompt template examples."""
    print("🎪 FUNKY PROMPT TEMPLATE EXAMPLES")
    print("=" * 60)
    print("Demonstrating creative ways to map state fields to prompts")

    await funky_recipe_agent()
    await funky_story_agent()
    await funky_code_review_agent()
    await multi_modal_funky_agent()

    print("\n\n🎯 KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Prompt templates can use ANY state field, not just 'messages'")
    print("2. Complex structured inputs enable rich agent behaviors")
    print("3. Multiple data types can be combined in creative ways")
    print("4. State schemas provide type safety for all inputs")
    print("5. Conditional logic in prompts based on state values")


if __name__ == "__main__":
    # Suppress logging
    import logging
    import os

    logging.getLogger().setLevel(logging.CRITICAL)
    os.environ["HAIVE_LOG_LEVEL"] = "CRITICAL"

    asyncio.run(main())
