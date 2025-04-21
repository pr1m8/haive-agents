import logging

import sqlparse
from langchain_core.messages import AIMessage
from langgraph.graph import END, START
from langgraph.types import Command

from haive.agents.rag.sql_rag.config import SQLRAGConfig
from haive.agents.rag.sql_rag.engines import default_sql_engines
from haive.agents.rag.sql_rag.state import OverallState
from haive.agents.rag.sql_rag.utils import (
    create_sql_toolkit,
    create_tool_node_with_fallback,
    explore_database_schema,
    get_all_toolkit_tools,
)
from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.graph.branches import Branch

logger = logging.getLogger(__name__)

@register_agent(SQLRAGConfig)
class SQLRAGAgent(Agent[SQLRAGConfig]):
    """SQL RAG Agent for querying SQL databases with natural language.
    
    This agent implements a workflow that:
    1. Validates if a query is relevant to databases
    2. Gets database schema information
    3. Analyzes the query to determine relevant tables
    4. Generates SQL from natural language
    5. Validates and corrects the SQL
    6. Executes the query and generates a final answer
    """

    def __init__(self, config: SQLRAGConfig):
        """Initialize the SQL RAG Agent with the given configuration."""
        self._initialize_config(config)
        super().__init__(config)

    def _initialize_config(self, config):
        """Initialize the configuration and components."""
        try:
            # Initialize database connection
            self.sql_db = config.db_config.get_sql_db()
            if not self.sql_db:
                raise ValueError(f"Failed to connect to {config.db_config.db_type} database")

            # Explore the database schema thoroughly
            self.db_schema = explore_database_schema(self.sql_db)
            self.dialect = self.db_schema["dialect"]
            self.no_results = "No results found"

            # Create toolkit and get all tools
            self.toolkit = create_sql_toolkit(config.db_config, config.llm_config)
            self.tools = get_all_toolkit_tools(self.toolkit)

            # Create tool nodes for each tool
            self.tool_nodes = {}
            for tool in self.tools:
                self.tool_nodes[tool.name] = create_tool_node_with_fallback(tool)

            # Map engines from config
            self.engines = {}
            if hasattr(config, "engines") and config.engines:
                # Start with default engines
                self.engines = {**default_sql_engines}
                # Override with any provided in config
                for key, engine in config.engines.items():
                    if engine is not None:
                        self.engines[key] = engine
            else:
                # Use default engines
                self.engines = default_sql_engines

            logger.info(f"SQL RAG Agent initialized with {len(self.db_schema['tables'])} tables")

        except Exception as e:
            logger.error(f"Error initializing SQLRAGAgent: {e}")
            raise

    def check_domain_relevance(self, state: OverallState) -> Command:
        """Determines if the query is relevant to databases.
        """
        try:
            # Get domain information
            domain_name = self.config.domain_name
            domain_categories = self.config.domain_categories

            # If no categories defined, default to domain name
            if not domain_categories:
                domain_categories = [domain_name]

            # Default category to use
            category = domain_categories[0] if domain_categories else domain_name

            # Use the guardrails engine
            if "guardrails" not in self.engines:
                raise ValueError("Missing 'guardrails' engine in configuration")

            guardrails_output = self.engines["guardrails"].invoke({"question": state.question})
            database_records = None

            if guardrails_output.decision == "end":
                database_records = f"This question is not about {domain_name}. I can only answer questions about databases."

            return Command(update={
                "next_action": guardrails_output.decision,
                "database_records": database_records,
                "steps": ["check_domain_relevance"],
            })
        except Exception as e:
            logger.error(f"Error in check_domain_relevance: {e}")
            return Command(update={
                "error": f"Error checking domain relevance: {e!s}",
                "next_action": "end"
            })

    def retrieve_schema(self, state: OverallState) -> Command:
        """Retrieves database schema information for context.
        """
        try:
            # Find the get_schema tool
            get_schema_tool = next((tool for tool in self.tools if tool.name == "sql_db_schema"), None)

            schema_info = {}
            # Get schema for all tables (or limit to a subset for very large databases)
            if get_schema_tool:
                for table in self.db_schema["tables"][:10]:  # Limit to first 10 tables if there are many
                    try:
                        schema_info[table] = get_schema_tool.invoke({"table_names": table})
                    except Exception as e:
                        schema_info[table] = f"Error retrieving schema: {e!s}"
            else:
                # Fallback if tool not available
                for table in self.db_schema["tables"][:10]:
                    schema_info[table] = self.db_schema["table_info"].get(table, "Schema not available")

            # Format schema information
            schema_message = "Database Schema Information:\n\n"
            for table, info in schema_info.items():
                schema_message += f"Table: {table}\n{info}\n\n"

            return Command(update={
                "schema_info": schema_info,
                "database_schema": schema_message,
                "next_action": "analyze_query",
                "steps": state.steps + ["retrieve_schema"],
                "messages": state.messages + [AIMessage(content=schema_message)]
            })
        except Exception as e:
            logger.error(f"Error in retrieve_schema: {e}")
            return Command(update={
                "error": f"Error retrieving database schema: {e!s}",
                "next_action": "end"
            })

    def analyze_query(self, state: OverallState) -> Command:
        """Analyzes the query to determine relevant tables and fields.
        """
        try:
            if "analyze_query" not in self.engines:
                raise ValueError("Missing 'analyze_query' engine in configuration")

            analysis = self.engines["analyze_query"].invoke({
                "question": state.question,
                "schema": self.db_schema,
                "dialect": self.dialect
            })

            return Command(update={
                "query_analysis": analysis,
                "tables_needed": analysis.get("tables", []),
                "next_action": "generate_query",
                "steps": state.steps + ["analyze_query"]
            })
        except Exception as e:
            logger.error(f"Error in analyze_query: {e}")
            return Command(update={
                "error": f"Error analyzing query: {e!s}",
                "next_action": "end"
            })

    def generate_query(self, state: OverallState) -> Command:
        """Generates an SQL query from the natural language question.
        """
        try:
            if "generate_sql" not in self.engines:
                raise ValueError("Missing 'generate_sql' engine in configuration")

            # Get examples for few-shot learning if available
            examples = []
            if hasattr(self.config, "domain_examples") and self.config.domain_name in self.config.domain_examples:
                examples = self.config.domain_examples[self.config.domain_name]

            # Format examples
            fewshot_examples = ""
            if examples:
                fewshot_examples = "\n\n".join([
                    f"Question: {example['question']}\nSQL query: {example['query']}"
                    for example in examples
                ])

            sql_query = self.engines["generate_sql"].invoke({
                "question": state.question,
                "schema": self.db_schema,
                "dialect": self.dialect,
                "query_analysis": state.query_analysis,
                "fewshot_examples": fewshot_examples
            })

            logger.info(f"Generated SQL query: {sql_query}")

            # Format query with sqlparse
            try:
                formatted_query = sqlparse.format(sql_query, reindent=True, keyword_case="upper")
            except Exception as e:
                logger.warning(f"Error formatting SQL query: {e}")
                formatted_query = sql_query

            return Command(update={
                "sql_query": formatted_query,
                "next_action": "validate_query",
                "steps": state.steps + ["generate_query"]
            })
        except Exception as e:
            logger.error(f"Error in generate_query: {e}")
            return Command(update={
                "error": f"Error generating SQL query: {e!s}",
                "next_action": "end"
            })

    def validate_query(self, state: OverallState) -> Command:
        """Validates the SQL query for syntax and schema correctness.
        """
        try:
            if "validate_sql" not in self.engines:
                raise ValueError("Missing 'validate_sql' engine in configuration")

            validation_result = self.engines["validate_sql"].invoke({
                "question": state.question,
                "sql_query": state.sql_query,
                "schema": self.db_schema,
                "dialect": self.dialect
            })

            if validation_result.is_valid == False:
                return Command(update={
                    "next_action": "correct_query",
                    "sql_errors": validation_result.errors,
                    "steps": state.steps + ["validate_query"]
                })
            return Command(update={
                "next_action": "execute_query",
                "steps": state.steps + ["validate_query"]
            })
        except Exception as e:
            logger.error(f"Error in validate_query: {e}")
            return Command(update={
                "error": f"Error validating SQL query: {e!s}",
                "next_action": "end"
            })

    def correct_query(self, state: OverallState) -> Command:
        """Corrects the SQL query based on validation errors.
        """
        try:
            if "correct_sql" not in self.engines:
                raise ValueError("Missing 'correct_sql' engine in configuration")

            corrected_sql = self.engines["correct_sql"].invoke({
                "question": state.question,
                "sql_query": state.sql_query,
                "errors": state.sql_errors,
                "schema": self.db_schema,
                "dialect": self.dialect
            })

            # Format query with sqlparse
            try:
                formatted_query = sqlparse.format(corrected_sql, reindent=True, keyword_case="upper")
            except Exception as e:
                logger.warning(f"Error formatting corrected SQL query: {e}")
                formatted_query = corrected_sql

            return Command(update={
                "sql_query": formatted_query,
                "next_action": "validate_query",
                "steps": state.steps + ["correct_query"]
            })
        except Exception as e:
            logger.error(f"Error in correct_query: {e}")
            return Command(update={
                "error": f"Error correcting SQL query: {e!s}",
                "next_action": "end"
            })

    def execute_query(self, state: OverallState) -> Command:
        """Executes the SQL query against the database.
        """
        try:
            # Find the run_query tool
            run_query_tool = next((tool for tool in self.tools if tool.name == "sql_db_query"), None)

            if run_query_tool:
                try:
                    # Use the tool to execute the query
                    result = run_query_tool.invoke({"query": state.sql_query})

                    if not result or (isinstance(result, str) and result.strip() == ""):
                        result = self.no_results
                except Exception as e:
                    logger.error(f"Error executing SQL query: {e}")
                    result = f"Error executing query: {e!s}"
            else:
                # Execute directly if tool not available
                try:
                    result = self.sql_db.run(state.sql_query)
                    if not result:
                        result = self.no_results
                except Exception as e:
                    logger.error(f"Error executing SQL query directly: {e}")
                    result = f"Error executing query: {e!s}"

            return Command(update={
                "query_result": result,
                "next_action": "generate_answer",
                "steps": state.steps + ["execute_query"]
            })
        except Exception as e:
            logger.error(f"Error in execute_query: {e}")
            return Command(update={
                "error": f"Error executing SQL query: {e!s}",
                "next_action": "end"
            })

    def generate_answer(self, state: OverallState) -> Command:
        """Generates the final answer based on the query results.
        """
        try:
            if "generate_final_answer" not in self.engines:
                raise ValueError("Missing 'generate_final_answer' engine in configuration")

            # Check if we need to run hallucination detection
            should_check_hallucination = self.config.hallucination_check

            # Generate the final answer
            answer = self.engines["generate_final_answer"].invoke({
                "question": state.question,
                "sql_query": state.sql_query,
                "query_result": state.query_result,
                "schema": self.db_schema
            })

            # Proceed with the usual workflow
            result = {
                "answer": answer,
                "final_sql": state.sql_query,
                "next_action": "end",
                "steps": state.steps + ["generate_answer"]
            }

            # Run hallucination check if required
            if should_check_hallucination and "hallucination_check" in self.engines:
                try:
                    hallucination_result = self.engines["hallucination_check"].invoke({
                        "question": state.question,
                        "answer": answer,
                        "sql_query": state.sql_query,
                        "query_result": state.query_result
                    })

                    result["hallucination_check"] = hallucination_result

                    # If hallucinations detected, provide a warning
                    if hallucination_result.hallucination_detected:
                        warning = f"\n\nWarning: The answer may contain information not supported by the data. Areas of concern: {hallucination_result.problem_areas}"
                        result["answer"] = answer + warning

                except Exception as e:
                    logger.warning(f"Error in hallucination check: {e}")
                    # Continue with generated answer even if hallucination check fails

            return Command(update=result)
        except Exception as e:
            logger.error(f"Error in generate_answer: {e}")
            return Command(update={
                "error": f"Error generating answer: {e!s}",
                "answer": f"An error occurred while generating the answer: {e!s}",
                "next_action": "end"
            })

    def domain_router(self, state: OverallState) -> str:
        """Route based on domain relevance check."""
        if state.next_action == "end":
            return END
        return "retrieve_schema"

    def validation_router(self, state: OverallState) -> str:
        """Route based on query validation."""
        if state.next_action == "end":
            return END
        if state.next_action == "correct_query":
            return "correct_query"
        return "execute_query"

    def setup_workflow(self) -> None:
        """Set up the SQL RAG workflow.
        """
        # Add nodes for the workflow
        self.graph.add_node("check_domain_relevance", self.check_domain_relevance)
        self.graph.add_node("retrieve_schema", self.retrieve_schema)
        self.graph.add_node("analyze_query", self.analyze_query)
        self.graph.add_node("generate_query", self.generate_query)
        self.graph.add_node("validate_query", self.validate_query)
        self.graph.add_node("correct_query", self.correct_query)
        self.graph.add_node("execute_query", self.execute_query)
        self.graph.add_node("generate_answer", self.generate_answer)

        # Connect nodes
        self.graph.add_edge(START, "check_domain_relevance")

        # Add conditional edges
        domain_branch = Branch.from_dict({
            "end": END,
            "default": "retrieve_schema"
        })
        self.graph.add_conditional_edges("check_domain_relevance", domain_branch, lambda x: x["next_action"])

        # Linear flow
        self.graph.add_edge("retrieve_schema", "analyze_query")
        self.graph.add_edge("analyze_query", "generate_query")
        self.graph.add_edge("generate_query", "validate_query")

        # Validation branch
        validation_branch = Branch.from_dict({
            "correct_query": "correct_query",
            "end": END,
            "default": "execute_query"
        })
        self.graph.add_conditional_edges("validate_query", validation_branch, lambda x: x["next_action"])

        # Complete the flow
        self.graph.add_edge("correct_query", "validate_query")
        self.graph.add_edge("execute_query", "generate_answer")
        self.graph.add_edge("generate_answer", END)

        logger.info("SQL RAG workflow setup complete")

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
