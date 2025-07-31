"""Test script to debug PostgreSQL persistence issues with ReactAgent."""

import logging
from pathlib import Path
import sys

# Load environment variables from the project root .env file
from dotenv import load_dotenv


project_root = Path(__file__).parent.parent.parent.parent
env_path = project_root / ".env"
load_dotenv(env_path)

# Set up detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)

# Ensure we see all persistence-related logs
logging.getLogger("haive.core.persistence").setLevel(logging.DEBUG)
logging.getLogger("haive.agents").setLevel(logging.DEBUG)
logging.getLogger("langgraph").setLevel(logging.DEBUG)


def test_react_agent_persistence():
    """Test ReactAgent with google_search_tool and PostgreSQL persistence."""
    try:
        # Import required modules
        from haive.agents.react.agent import ReactAgent
        from haive.tools.tools.search_tools import tavily_search_tool

        # Create ReactAgent
        search_agent = ReactAgent(name="search_agent")

        # Add tavily_search_tool
        search_agent.engine.tools = [tavily_search_tool]

        # Check persistence configuration
        if hasattr(search_agent, "persistence"):
            if hasattr(search_agent.persistence, "db_host"):
                pass

        # Check if checkpointer is set up
        if hasattr(search_agent, "_checkpointer"):
            pass
        else:
            pass

        # Run the agent
        result = search_agent.run(
            {"messages": ["What is the weather in France"]}, debug=True
        )

        if hasattr(result, "content"):
            pass
        else:
            pass

    except Exception as e:

        # Print full traceback
        import traceback

        traceback.print_exc()

        # Check if it's the foreign key error
        if "foreign key constraint" in str(e):
            pass


if __name__ == "__main__":
    test_react_agent_persistence()
