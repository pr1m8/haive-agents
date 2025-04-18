from haive_core.engine.agent.agent import AgentConfig
from haive_core.engine.aug_llm import AugLLMConfig
from haive_agents.rag.base.config import BaseRAGConfig
from haive_agents.rag.sql_rag.state import OverallState, InputState, OutputState
from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Any, Optional, Type, Union
from langchain_community.utilities import SQLDatabase
import os
from dotenv import load_dotenv
from haive_core.models.llm.base import LLMConfig, AzureLLMConfig
load_dotenv('.env')


class SQLDatabaseConfig(BaseModel):
    """Configuration model for connecting to a SQL database."""

    db_type: str = Field(
        default=os.getenv("SQL_DB_TYPE", "postgresql"),
        description="Type of SQL database (postgresql, mysql, sqlite, etc.)"
    )
    db_uri: Optional[str] = Field(
        default=None,
        description="The database connection URI (if provided directly)"
    )
    db_user: str = Field(
        default=os.getenv('SQL_DB_USER', 'postgres'),
        description="The database username"
    )
    db_password: str = Field(
        default=os.getenv('SQL_DB_PASSWORD', 'postgres'),
        description="The database password"
    )
    db_host: str = Field(
        default=os.getenv('SQL_DB_HOST', 'localhost'),
        description="The database host"
    )
    db_port: str = Field(
        default=os.getenv('SQL_DB_PORT', '5432'),
        description="The database port"
    )
    db_name: str = Field(
        default=os.getenv('SQL_DB_NAME', 'postgres'),
        description="The database name"
    )
    include_tables: Optional[List[str]] = Field(
        default_factory=lambda: os.getenv("SQL_INCLUDE_TABLES", "").split(",") if os.getenv("SQL_INCLUDE_TABLES") else None,
        description="Specific tables to include, if None then include all"
    )
    exclude_tables: List[str] = Field(
        default_factory=lambda: os.getenv("SQL_EXCLUDE_TABLES", "").split(",") if os.getenv("SQL_EXCLUDE_TABLES") else [],
        description="Tables to exclude from schema"
    )
    sample_rows_in_table_info: int = Field(
        default=3,
        description="Number of sample rows to include in table info"
    )
    custom_query: Optional[str] = Field(
        default=None,
        description="Custom query to execute for schema info"
    )
   
    def get_connection_string(self) -> str:
        """Generate a connection string based on the database type."""
        if self.db_uri:
            return self.db_uri
            
        if self.db_type == "postgresql":
            return f"postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        elif self.db_type == "mysql":
            return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        elif self.db_type == "sqlite":
            # For SQLite, the db_name is the path to the file
            return f"sqlite:///{self.db_name}"
        elif self.db_type == "mssql":
            return f"mssql+pyodbc://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")
   
    def get_sql_db(self) -> Optional[SQLDatabase]:
        """Creates and returns a SQLDatabase object for interacting with the database."""
        try:
            connection_string = self.get_connection_string()
            db = SQLDatabase.from_uri(
                connection_string,
                include_tables=self.include_tables,
                exclude_tables=self.exclude_tables,
                sample_rows_in_table_info=self.sample_rows_in_table_info,
            )
            print(f"✅ Connected to {self.db_type} database at {connection_string}")
            return db
        except Exception as e:
            print(f"🚨 Failed to connect to database: {e}")
            return None

    def get_db_schema(self) -> Dict[str, Any]:
        """Retrieves the schema and basic table info from the database."""
        db = self.get_sql_db()
        if not db:
            return {"tables": [], "dialect": "unknown"}

        schema = {
            "tables": db.get_usable_table_names(),
            "dialect": str(db.dialect),
            "table_info": {}
        }

        for table in schema["tables"]:
            schema["table_info"][table] = db.get_table_info([table])
        
        return schema


class SQLRAGConfig(BaseRAGConfig):
    """Configuration for the SQL RAG Agent"""
    
    engines: Dict[str, AugLLMConfig] = Field(
        description="The LLM runnable configs for the SQL database agent",
        default={
            "analyze_query": None,
            "validate_sql": None,
            "generate_sql": None,
            "guardrails": None,
            "generate_final_answer": None,
            "hallucination_check": None,
            "answer_grading": None
        }
    )
    
    llm_config: LLMConfig = Field(
        default_factory=AzureLLMConfig,
        description="The LLM config for the SQL database agent"
    )
    
    domain_name: str = Field(
        default="database",
        description="The domain name the agent is specialized for (e.g., 'SQL database', 'database records', etc.)"
    )
    
    domain_categories: List[str] = Field(
        default=["database"],
        description="Valid categories for the guardrails to recognize, in addition to 'end'"
    )
    
    state_schema: Any = Field(
        default=OverallState,
        description="The state schema for the SQL database agent"
    )
    
    db_config: SQLDatabaseConfig = Field(
        default_factory=SQLDatabaseConfig,
        description="The database config for the SQL database agent"
    )
    
    input_schema: Any = Field(
        default=InputState,
        description="The input schema for the SQL database agent"
    )
    
    output_schema: Any = Field(
        default=OutputState,
        description="The output schema for the SQL database agent"
    )
    
    hallucination_check: bool = Field(
        default=True,
        description="Whether to check for hallucinations in the response"
    )
    
    answer_grading: bool = Field(
        default=True,
        description="Whether to grade the answer for relevance to the question"
    )
    
    examples_path: Optional[str] = Field(
        default=None,
        description="Path to examples JSON file"
    )
    
    domain_examples: Dict[str, List[Dict[str, str]]] = Field(
        default_factory=dict,
        description="Examples for different domains to guide the model"
    )
    
    max_iterations: int = Field(
        default=5,
        description="Maximum number of iterations for retrying SQL queries"
    )
    
    @field_validator('engines')
    def check_required_engines(cls, v):
        """Ensure all required engines are present."""
        required_engines = ["analyze_query", "validate_sql", "generate_sql", "guardrails", "generate_final_answer"]
        missing = [engine for engine in required_engines if engine not in v or v[engine] is None]
        if missing:
            raise ValueError(f"Missing required engines: {', '.join(missing)}")
        return v

# For backward compatibility
SQLAgentConfig = SQLRAGConfig