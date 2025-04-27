from haive.core.engine.agent.agent import AgentConfig   
from haive.core.engine.aug_llm import AugLLMConfig
from haive.agents.rag.base.config import BaseRAGConfig
from haive.agents.rag.graph_db.engines import (
    correct_cypher_aug_llm_config, validate_cypher_aug_llm_config, 
    text2cypher_aug_llm_config, guardrails_aug_llm_config, 
    generate_final_aug_llm_config
)
from haive.agents.rag.graph_db.state import OverallState, InputState, OutputState
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict, List, Any, Union
import os
from langchain_neo4j import Neo4jGraph
from dotenv import load_dotenv

# Try to load environment variables from .env file if it exists
load_dotenv('.env')


class GraphDBConfig(BaseModel):
    """Configuration model for connecting to a Neo4j graph database."""
    
    graph_db_uri: str = Field(default=os.getenv("NEO4J_URI", ""), description="The URI of the Neo4j database.")
    graph_db_user: str = Field(default=os.getenv("NEO4J_USER", ""), description="The username for the Neo4j database.")
    graph_db_password: str = Field(default=os.getenv("NEO4J_PASSWORD", ""), description="The password for the Neo4j database.")
    graph_db_database: str = Field(default=os.getenv("NEO4J_DATABASE", ""), description="The database name in Neo4j.")
    enhanced_schema: bool = Field(default=True, description="Enable enhanced schema scanning.")

    def get_graph_db(self) -> Optional[Neo4jGraph]:
        """
        Creates and returns a Neo4jGraph object for interacting with the Neo4j database.
        Ensures proper security handling and configuration.
        """
        try:
            graph_db = Neo4jGraph(
                url=self.graph_db_uri,
                username=self.graph_db_user,
                password=self.graph_db_password,
                database=self.graph_db_database,
                timeout=10,
                sanitize=True,
                refresh_schema=True,
                enhanced_schema=self.enhanced_schema,
            )
            print(f"✅ Successfully connected to Neo4j at {self.graph_db_uri}")
            return graph_db
        except Exception as e:
            print(f"🚨 Error connecting to Neo4j: {e}")
            return None

    def get_graph_db_schema(self) -> Optional[Dict]:
        """
        Retrieves the graph schema from the Neo4j database.
        Uses enhanced schema if enabled.
        """
        graph_db = self.get_graph_db()
        if graph_db:
            return graph_db.get_schema()
        else:
            return None


class ExampleConfig(BaseModel):
    """Configuration for the example selector used by the agent."""
    
    examples_path: Optional[str] = Field(
        default=None, 
        description="Path to a JSON file containing Cypher query examples."
    )
    examples: Optional[List[Dict[str, str]]] = Field(
        default=None,
        description="List of examples to use in lieu of a file. Each example should have 'question' and 'query' keys."
    )
    k: int = Field(
        default=2,
        description="Number of examples to retrieve from the example selector."
    )
    

class GraphDBRAGConfig(AgentConfig):
    """Configuration model for the Graph Database RAG Agent."""
    
    engines: Dict[str, AugLLMConfig] = Field(
        description="The LLM runnable configs for the graph database agent",
        default={
            "correct_cypher": correct_cypher_aug_llm_config,
            "validate_cypher": validate_cypher_aug_llm_config,
            "text2cypher": text2cypher_aug_llm_config,
            "guardrails": guardrails_aug_llm_config,
            "generate_final_answer": generate_final_aug_llm_config
        }
    )
    
    domain_name: str = Field(
        default="general",
        description="The domain name the agent is specialized for (e.g., 'movies', 'healthcare', etc.)"
    )
    
    domain_categories: List[str] = Field(
        default_factory=list,
        description="Valid categories for the guardrails to recognize, in addition to 'end'"
    )
    
    example_config: Optional[ExampleConfig] = Field(
        default=None,
        description="Configuration for the Cypher query examples used by the agent."
    )
    
    state_schema: Any = Field(
        default=OverallState,
        description="The state schema for the graph database agent"
    )
    
    graph_db_config: GraphDBConfig = Field(
        default_factory=GraphDBConfig,
        description="The graph database config for the graph database agent"
    )
    
    input_schema: Any = Field(
        default=InputState,
        description="The input schema for the graph database agent"
    )
    
    output_schema: Any = Field(
        default=OutputState,
        description="The output schema for the graph database agent"
    )
    
    domain_examples: Dict[str, List[Dict[str, str]]] = Field(
        default_factory=dict,
        description="Examples for different domains to guide the model"
    )

    @field_validator("engines")
    def validate_engines(cls, engines):
        """Ensure all required engines are present."""
        required_engines = [
            "correct_cypher", 
            "validate_cypher", 
            "text2cypher", 
            "guardrails", 
            "generate_final_answer"
        ]
        
        for engine_name in required_engines:
            if engine_name not in engines:
                if engine_name == "text2cypher" and "generate_cypher" in engines:
                    # Handle potential name mismatch
                    engines["text2cypher"] = engines["generate_cypher"]
                else:
                    raise ValueError(f"Missing required engine: {engine_name}")
        
        return engines

# For backward compatibility
GraphDBAgentConfig = GraphDBRAGConfig