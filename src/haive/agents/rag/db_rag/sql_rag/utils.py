from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda, RunnableWithFallbacks
from langgraph.prebuilt import ToolNode
from typing import List, Dict, Any, Optional, Union, Callable
from haive.core.engine.aug_llm import AugLLMConfig
from haive.agents.rag.db_rag.sql_rag.config import SQLDatabaseConfig


def create_sql_toolkit(
    db_config: SQLDatabaseConfig,
    llm_config: Optional[AugLLMConfig] = None
) -> SQLDatabaseToolkit:
    """
    Create a SQL Database Toolkit using the provided configuration.
    
    Args:
        db_config: Configuration for the SQL database
        llm_config: Configuration for the LLM (optional)
        
    Returns:
        SQLDatabaseToolkit instance
    """
    # Get database instance
    db = db_config.get_sql_db()
    if not db:
        raise ValueError("Failed to initialize SQL database connection")
    
    # Initialize LLM
    if llm_config:
        llm = llm_config.instantiate_llm()
    else:
        # Default to OpenAI
        llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    # Create and return toolkit
    return SQLDatabaseToolkit(db=db, llm=llm)


def get_all_toolkit_tools(toolkit: SQLDatabaseToolkit) -> List[BaseTool]:
    """
    Get all tools from a SQLDatabaseToolkit
    
    Args:
        toolkit: The SQLDatabaseToolkit instance
        
    Returns:
        List of all tools in the toolkit
    """
    return toolkit.get_tools()


def create_tool_node_with_fallback(
    tools: Union[BaseTool, List[BaseTool]]
) -> RunnableWithFallbacks:
    """
    Create a ToolNode with a fallback to handle errors and surface them to the agent.
    
    Args:
        tools: Tool or list of tools to create a node for
        
    Returns:
        ToolNode with fallback handler
    """
    # Convert single tool to list if needed
    if not isinstance(tools, list):
        tools = [tools]
    
    # Create tool node with fallback
    return ToolNode(tools).with_fallbacks(
        [RunnableLambda(handle_tool_error)], 
        exception_key="error"
    )


def handle_tool_error(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Handle tool execution errors by surfacing them to the agent.
    
    Args:
        state: Current state with error information
        
    Returns:
        Modified state with error messages
    """
    error = state.get("error")
    
    # Check if there are tool calls in the last message
    tool_calls = []
    if "messages" in state and state["messages"]:
        last_message = state["messages"][-1]
        if hasattr(last_message, "tool_calls"):
            tool_calls = last_message.tool_calls
    
    # If we have tool calls, create tool messages for each
    if tool_calls:
        from langchain_core.messages import ToolMessage
        return {
            "messages": [
                ToolMessage(
                    content=f"Error: {repr(error)}\nPlease fix your mistakes.",
                    tool_call_id=tc["id"],
                )
                for tc in tool_calls
            ]
        }
    
    # Otherwise, just add error to state
    return {
        "sql_errors": [f"Error: {repr(error)}"]
    }


def explore_database_schema(db: SQLDatabase) -> Dict[str, Any]:
    """
    Explore the database schema thoroughly to get schema information.
    This is used instead of relying on examples.
    
    Args:
        db: SQLDatabase instance
        
    Returns:
        Detailed schema information
    """
    schema_info = {
        "tables": db.get_usable_table_names(),
        "table_info": {},
        "table_samples": {},
        "relationships": [],
        "dialect": str(db.dialect)
    }
    
    # Get detailed information for each table
    for table in schema_info["tables"]:
        # Get schema for this table
        schema_info["table_info"][table] = db.get_table_info([table])
        
        # Get sample data
        try:
            samples = db.run(f"SELECT * FROM {table} LIMIT 3")
            schema_info["table_samples"][table] = samples
        except Exception as e:
            schema_info["table_samples"][table] = f"Error fetching samples: {str(e)}"
    
    # Try to detect relationships between tables
    try:
        # This is a simplified approach - won't work for all DB types
        # For a production system, this should be adapted to the specific DB dialect
        for table1 in schema_info["tables"]:
            for table2 in schema_info["tables"]:
                if table1 != table2:
                    # Look for potential foreign keys based on naming conventions
                    t1_info = schema_info["table_info"][table1]
                    t2_info = schema_info["table_info"][table2]
                    
                    # Look for columns with names like "{table}Id" in the other table
                    for col_line in t1_info.split("\n"):
                        if f"{table2.lower()}id" in col_line.lower() or f"{table2.lower()}_id" in col_line.lower():
                            schema_info["relationships"].append({
                                "from_table": table1,
                                "to_table": table2,
                                "relationship": "potential_foreign_key",
                                "column": col_line.strip()
                            })
    except Exception as e:
        # Relationship detection is best-effort
        schema_info["relationship_detection_error"] = str(e)
    
    return schema_info