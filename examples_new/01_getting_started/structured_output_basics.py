#!/usr/bin/env python3
"""Structured Output Basics - Get Organized Responses from Your Agent

This example shows how to get structured, predictable output from agents
using Pydantic models. Instead of free-form text, you get organized data!

What you'll learn:
- How to define structured output models with Pydantic
- How to configure agents to return structured data
- Why structured output is useful for building applications"""

# Suppress logging for a cleaner demo
import logging

logging.getLogger().setLevel(logging.ERROR)


from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import BaseModel, Field

# Import what we need
from haive.agents.simple.agent import SimpleAgent

# ============================================
# Step 1: Define Your Output Structure
# ============================================
# We use Pydantic models to define exactly what we want back


class MovieReview(BaseModel):
    """A structured movie review with specific fields."""

    movie_title: str = Field(description="The title of the movie")
    rating: float = Field(ge=0, le=10, description="Rating from 0 to 10")
    summary: str = Field(description="A brief summary of the movie")
    pros: list[str] = Field(description="List of positive aspects")
    cons: list[str] = Field(description="List of negative aspects")
    recommended: bool = Field(description="Whether you recommend this movie")


# ============================================
# Step 2: Create an Agent with Structured Output
# ============================================
# Tell the agent to return data in our MovieReview format

config = AugLLMConfig(
    temperature=0.3,  # Lower temperature for consistent structure
    structured_output_model=MovieReview,  # This is the magic line!
    system_message="You are a movie critic who provides structured reviews.",
)

agent = SimpleAgent(name="movie_critic", engine=config)

# ============================================
# Step 3: Get a Structured Review!
# ============================================
print("🎬 Structured Output Example - Movie Reviews")
print("=" * 50)

# Ask for a movie review
request = "Review the movie 'The Matrix' (1999)"
print(f"You: {request}")
print("\n🎬 Generating structured review...")

# The response will be a MovieReview object, not just text!
review = agent.run(request)

# ============================================
# Step 4: Access the Structured Data
# ============================================
print("\n📊 Structured Movie Review:")
print("=" * 50)
print(f"Title: {review.movie_title}")
print(f"Rating: {review.rating}/10 {'⭐' * int(review.rating)}")
print(f"Summary: {review.summary}")
print("\n✅ Pros:")
for pro in review.pros:
    print(f"  - {pro}")
print("\n❌ Cons:")
for con in review.cons:
    print(f"  - {con}")
print(f"\nRecommended: {'Yes! 👍' if review.recommended else 'No 👎'}")
print("=" * 50)

# ============================================
# Example 2: Weather Report Structure
# ============================================
print("\n🌤️ Another Example: Weather Reports")
print("=" * 50)


class WeatherReport(BaseModel):
    """A structured weather report."""

    location: str = Field(description="The location for the weather")
    temperature: float = Field(description="Temperature in Celsius")
    conditions: str = Field(
        description="Weather conditions (sunny, cloudy, rainy, etc.)"
    )
    humidity: int = Field(ge=0, le=100, description="Humidity percentage")
    wind_speed: float = Field(ge=0, description="Wind speed in km/h")
    advice: str = Field(description="What to wear or bring")


# Create a weather agent
weather_config = AugLLMConfig(
    temperature=0.3,
    structured_output_model=WeatherReport,
    system_message="You are a weather reporter. Provide realistic weather information.",
)

weather_agent = SimpleAgent(name="weather_reporter", engine=weather_config)

# Get a weather report
print("You: What's the weather like in Paris today?")
print("\n🌤️ Generating weather report...")

weather = weather_agent.run("What's the weather like in Paris today?")

print(f"\n📊 Weather Report for {weather.location}:")
print("=" * 50)
print(f"🌡️  Temperature: {weather.temperature}°C")
print(f"☁️  Conditions: {weather.conditions}")
print(f"💧 Humidity: {weather.humidity}%")
print(f"💨 Wind Speed: {weather.wind_speed} km/h")
print(f"👕 Advice: {weather.advice}")
print("=" * 50)

# ============================================
# Why Use Structured Output?
# ============================================
print("\n🎯 Why Structured Output is Powerful:")
print("=" * 50)
print("1. PREDICTABLE: Always get data in the exact format you need")
print("2. TYPE-SAFE: Python knows the types of all fields")
print("3. VALIDATED: Pydantic ensures data meets your requirements")
print("4. EASY TO USE: Access data with dot notation (review.rating)")
print("5. API-READY: Perfect for building web APIs and applications")

# ============================================
# Working with the Data
# ============================================
print("\n💾 You Can Do Anything with Structured Data:")
print("=" * 50)

# Convert to dictionary
review_dict = review.model_dump()
print(f"As dictionary: {list(review_dict.keys())}")

# Convert to JSON
review_json = review.model_dump_json(indent=2)
print(f"\nAs JSON (first 100 chars):\n{review_json[:100]}...")

# Check if highly rated
if review.rating >= 8 and review.recommended:
    print(f"\n⭐ '{review.movie_title}' is highly recommended!")

# ============================================
# Try It Yourself!
# ============================================
print("\n💡 Ideas for Your Own Structured Outputs:")
print("- Recipe with ingredients and steps")
print("- Product review with features and price")
print("- Travel itinerary with destinations and activities")
print("- Character profile for a game or story")
print("- Task list with priorities and deadlines")
print("\nStructured output turns your agent into a data generator! 🚀")
