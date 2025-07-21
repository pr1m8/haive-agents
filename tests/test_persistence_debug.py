"""Test script to debug PostgreSQL persistence issues with ReactAgent."""

import logging
import sys
from pathlib import Path

# Load environment variables from the project root .env file
from dotenv import load_dotenv

project_root = Path(__file__).parent.parent.parent.parent
env_path = project_root / ".env"
print(f"Loading .env from: {env_path}")
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
    print("\n=== Starting ReactAgent Persistence Test ===\n")

    try:
        # Import required modules
        from haive.tools.tools.search_tools import tavily_search_tool

        from haive.agents.react.agent import ReactAgent

        print("✅ Imports successful")

        # Create ReactAgent
        print("\n🔧 Creating ReactAgent...")
        search_agent = ReactAgent(name="search_agent")
        print(f"✅ ReactAgent created: {search_agent.name}")

        # Add tavily_search_tool
        print("\n🔧 Adding tavily_search_tool...")
        search_agent.engine.tools = [tavily_search_tool]
        print(f"✅ Tools added: {[tool.name for tool in search_agent.engine.tools]}")

        # Check persistence configuration
        print("\n🔍 Checking persistence configuration...")
        if hasattr(search_agent, "persistence"):
            print(f"Persistence type: {type(search_agent.persistence).__name__}")
            if hasattr(search_agent.persistence, "db_host"):
                print(f"Database host: {search_agent.persistence.db_host}")
                print(f"Database port: {search_agent.persistence.db_port}")
                print(f"Database name: {search_agent.persistence.db_name}")

        # Check if checkpointer is set up
        if hasattr(search_agent, "_checkpointer"):
            print(
                f"✅ Checkpointer configured: {type(search_agent._checkpointer).__name__}"
            )
        else:
            print("⚠️  No checkpointer configured")

        # Run the agent
        print("\n🚀 Running agent with test query...")
        result = search_agent.run(
            {"messages": ["What is the weather in France"]}, debug=True
        )

        print("\n✅ Agent execution completed")
        print(f"Result type: {type(result)}")
        if hasattr(result, "content"):
            print(f"Result content: {result.content[:200]}...")
        else:
            print(f"Result: {str(result)[:200]}...")

    except Exception as e:
        print(f"\n❌ Error occurred: {type(e).__name__}")
        print(f"Error message: {str(e)}")

        # Print full traceback
        import traceback

        print("\nFull traceback:")
        traceback.print_exc()

        # Check if it's the foreign key error
        if "foreign key constraint" in str(e):
            print("\n⚠️  Foreign key constraint error detected!")
            print(
                "This suggests the thread was not created before checkpoint insertion."
            )
            print("\nPossible causes:")
            print("1. PostgresSaverWithThreadCreation is not being used")
            print("2. Thread creation logic is failing")
            print("3. Database schema mismatch")


if __name__ == "__main__":
    test_react_agent_persistence()
