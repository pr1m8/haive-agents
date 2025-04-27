from haive.agents.rag.db_rag.sql_rag.config import SQLRAGConfig
from haive.agents.rag.db_rag.sql_rag.agent import SQLRAGAgent  

# For backward compatibility
SQLDatabaseAgent = SQLRAGAgent

def main():
    # Create a sample configuration
    config = SQLRAGConfig()
    # Initialize the agent
    agent = SQLRAGAgent(config)
    # Run a sample query
    result = agent.run({"question": "What tables are in this database?"})
    print(f"Result: {result}")
    
if __name__ == "__main__":
    main()