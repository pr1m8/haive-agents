# src/haive/agents/react/test_react_agent.py

import os
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime

from langchain_core.tools import Tool

from haive_agents.react_agent2.agent2 import create_react_agent
from src.config.settings import RESOURCES_DIR

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example tools
def search_web(query: str) -> str:
    """Search the web for information."""
    logger.info(f"Executing search_web with query: {query}")
    return f"Web results for '{query}':\n1. Wikipedia: Information about {query}\n2. News sites: Recent developments in {query}\n3. Blogs: Opinions on {query}"

def search_db(query: str) -> str:
    """Search internal database for information."""
    logger.info(f"Executing search_db with query: {query}")
    return f"Database results for '{query}':\n1. Internal document #42: {query} overview\n2. Internal document #56: {query} details\n3. Internal document #78: {query} procedures"

def get_weather(location: str, date: Optional[str] = None) -> str:
    """Get weather information for a location."""
    logger.info(f"Executing get_weather with location: {location}, date: {date}")
    if date:
        return f"Weather forecast for {location} on {date}: Sunny with a high of 72°F"
    else:
        return f"Current weather in {location}: Partly cloudy, 68°F"

def analyze_data(data: str) -> Dict[str, Any]:
    """Analyze provided data."""
    logger.info(f"Executing analyze_data with data: {data[:50]}...")
    return {
        "word_count": len(data.split()),
        "character_count": len(data),
        "summary": f"Analysis of {len(data.split())} words"
    }

def main():
    """Run the React agent tests."""
    # Create tools
    tools = [
        Tool(name="search_web", func=search_web, description="Search the web for information about a topic"),
        Tool(name="search_db", func=search_db, description="Search internal databases for information"),
        Tool(name="get_weather", func=get_weather, description="Get weather information for a location"),
        Tool(name="analyze_data", func=analyze_data, description="Analyze provided data and return insights")
    ]
    
    # Create React agent
    agent = create_react_agent(
        tools=tools,
        model="gpt-4o",
        temperature=0.7,
        name="BusinessIntelligenceAgent",
        max_iterations=5,
        use_memory=True,
        visualize=True
    )
    
    # Test the agent with different questions
    questions = [
        "What's the weather in New York?",
        "Can you search for purchase order #45678 details and status?",
        "What's the current market trend for AI technology companies?"
    ]
    
    # Run the agent for each question
    for i, question in enumerate(questions):
        logger.info(f"\n----- Question {i+1}: {question} -----\n")
        
        try:
            # Run the agent
            result = agent.run(question)
            
            # Print AI responses
            logger.info("\n--- AI ---\n")
            messages = result.get("messages", [])
            for msg in messages:
                if hasattr(msg, "type") and msg.type == "ai":
                    logger.info(msg.content or "(No content)")
                elif isinstance(msg, dict) and msg.get("type") == "ai":
                    logger.info(msg.get("content", "(No content)"))
                
            # Log structured output if present
            if "structured_output" in result:
                logger.info("\n--- Structured Output ---\n")
                logger.info(result["structured_output"])
                
        except Exception as e:
            logger.error(f"Error running agent: {str(e)}", exc_info=True)
    
    # Indicate where visualization is saved
    logger.info(f"\nVisualization saved to: {RESOURCES_DIR}")
    logger.info(f"Check for image files with the pattern: {agent.config.name}_*.png")

if __name__ == "__main__":
    main()