# For backward compatibility
from haive.agents.rag.db_rag.graph_db.agent import GraphDBRAGAgent


#GraphDBAgent = GraphDBRAGAgent

def main():
    agent = GraphDBRAGAgent()
    for output in agent.app.stream({"question": "What is the movie with the highest rating?"}, config=agent.runnable_config, debug=True):
        print(output)

if __name__ == "__main__":
    main()