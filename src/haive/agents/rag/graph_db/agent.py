from haive.agents.rag.graph_db.state import OverallState, InputState, OutputState
from haive.agents.rag.graph_db.engines import (
    correct_cypher_aug_llm_config, validate_cypher_aug_llm_config,
    guardrails_aug_llm_config, text2cypher_aug_llm_config,
    generate_final_aug_llm_config
)
from haive.agents.rag.graph_db.config import GraphDBRAGConfig
from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.graph.branches import Branch
from pydantic import BaseModel, Field
from typing import List, Dict, Literal, Annotated, Union, Any, Optional
from haive.core.engine.aug_llm import AugLLMConfig
from langgraph.types import Command
from langgraph.graph import START, END
from neo4j.exceptions import CypherSyntaxError
from neo4j import GraphDatabase
from langchain_neo4j import Neo4jGraph, Neo4jVector
from langchain_neo4j.chains.graph_qa.cypher_utils import CypherQueryCorrector, Schema
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain_core.documents import Document
import os
import json
import logging

logger = logging.getLogger(__name__)
@register_agent(GraphDBRAGConfig)
class GraphDBRAGAgent(Agent[GraphDBRAGConfig]):
    """
    Graph Database RAG Agent for querying Neo4j databases with natural language.
    
    This agent implements a workflow that:
    1. Validates if a query is within the configured domain
    2. Generates a Cypher query from natural language
    3. Validates and corrects the Cypher query
    4. Executes the query and generates a final answer
    """
    
    def __init__(self, config: GraphDBRAGConfig):
        """Initialize the Graph DB RAG Agent with the given configuration."""
        self._initialize_config(config)
        super().__init__(config)
        
    def _initialize_config(self, config):
        """Initialize the configuration and components."""
        try:
            # Initialize graph database connection
            self.graph_db = config.graph_db_config.get_graph_db()
            if not self.graph_db:
                raise ValueError("Failed to connect to Neo4j database")
                
            # Get schema information
            self.graph_db_enhanced_schema = self.graph_db.schema
            self.graph_db_structured_schema = self.graph_db.structured_schema
            
            # Set up corrector schema for relationship direction correction
            self.corrector_schema = [
                Schema(el["start"], el["type"], el["end"])
                for el in self.graph_db_structured_schema.get("relationships", [])
            ]

            self.cypher_query_corrector = CypherQueryCorrector(self.corrector_schema)
            self.no_results = "No results found"
            
            # Initialize example selector
            self._initialize_example_selector(config)
            
        except Exception as e:
            logger.error(f"Error initializing GraphDBRAGAgent: {e}")
            raise

    def _initialize_example_selector(self, config):
        """Initialize the example selector with examples appropriate for the domain."""
        try:
            # Check if we have domain-specific examples
            domain_examples = []
            
            # Try to get examples for the configured domain
            if hasattr(config, 'domain_examples') and config.domain_name in config.domain_examples:
                domain_examples = config.domain_examples[config.domain_name]
            
            # Try to load examples from a file if specified
            if hasattr(config, 'example_config') and config.example_config:
                examples_path = config.example_config.examples_path
                if examples_path and os.path.exists(examples_path):
                    with open(examples_path, "r") as f:
                        domain_examples = json.load(f)
                elif config.example_config.examples:
                    domain_examples = config.example_config.examples
            
            # Default examples if none are provided
            if not domain_examples:
                # Get default examples for the domain
                domain_examples = self._get_default_examples(config.domain_name)
            
            # Create documents for embedding
            documents = [
                Document(page_content=ex["query"], metadata={"question": ex["question"]})
                for ex in domain_examples
            ]
            
            # Try to use OpenAI embeddings, falling back to default if not available
            try:
                embedding = OpenAIEmbeddings()
                vectorstore = Chroma.from_documents(documents, embedding, collection_name="cypher_examples")
                self.example_selector = SemanticSimilarityExampleSelector(
                    vectorstore=vectorstore,
                    k=getattr(config, 'example_config', {}).get('k', 2) if hasattr(config, 'example_config') else 2,
                    input_keys=["question"],
                )
            except Exception as e:
                logger.warning(f"Failed to initialize semantic example selector: {e}")
                # Simple fallback - just use all examples
                self.example_selector = type('SimpleSelector', (), {
                    'select_examples': lambda self, query: domain_examples
                })()
                
        except Exception as e:
            logger.error(f"Error initializing example selector: {e}")
            # Create a dummy selector that returns empty examples if all else fails
            self.example_selector = type('DummySelector', (), {
                'select_examples': lambda self, query: []
            })()

    def _get_default_examples(self, domain_name):
        """Get default examples for the specified domain."""
        # Default examples by domain
        default_examples = {
            "movies": [
                {"question": "Which movie has the highest rating?", 
                 "query": "MATCH (m:Movie) RETURN m.title, m.rating ORDER BY m.rating DESC LIMIT 1"},
                {"question": "Who directed The Matrix?", 
                 "query": "MATCH (p:Person)-[:DIRECTED]->(m:Movie {title: 'The Matrix'}) RETURN p.name"},
                {"question": "What are the top 5 highest-rated movies?", 
                 "query": "MATCH (m:Movie) RETURN m.title, m.rating ORDER BY m.rating DESC LIMIT 5"}
            ],
            "healthcare": [
                {"question": "Which patients have diabetes?", 
                 "query": "MATCH (p:Patient)-[:HAS_CONDITION]->(c:Condition {name: 'Diabetes'}) RETURN p.name"},
                {"question": "What medications are prescribed for hypertension?", 
                 "query": "MATCH (m:Medication)<-[:PRESCRIBED]-(c:Condition {name: 'Hypertension'}) RETURN m.name"},
                {"question": "Who are the doctors specializing in cardiology?", 
                 "query": "MATCH (d:Doctor {specialty: 'Cardiology'}) RETURN d.name"}
            ],
            # Add more domains as needed
            "general": [
                {"question": "What are the connections between A and B?", 
                 "query": "MATCH (a)-[r]-(b) RETURN a, r, b LIMIT 10"},
                {"question": "What properties does node type X have?", 
                 "query": "MATCH (x:X) RETURN x LIMIT 1"},
                {"question": "How many relationships exist in the database?", 
                 "query": "MATCH ()-[r]->() RETURN count(r)"}
            ]
        }
        
        return default_examples.get(domain_name, default_examples["general"])

    def check_domain_relevance(self, state: OverallState) -> Command:
        """
        Determines if the query is relevant to the configured domain.
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
            
            # Format the guardrails prompt with domain information
            formatted_prompt = self.engines["guardrails"].prompt_template.format(
                domain_name=domain_name,
                category=category,
                question=state.question
            )
            
            # Invoke the guardrails engine
            guardrails_output = self.engines["guardrails"].invoke({"question": state.question})
            database_records = None
            
            if guardrails_output.decision == "end":
                database_records = f"This question is not about {domain_name}. Therefore I cannot answer this question."
                
            return Command(update={
                "next_action": guardrails_output.decision,
                "database_records": database_records,
                "steps": ["check_domain_relevance"],
            })
        except Exception as e:
            logger.error(f"Error in check_domain_relevance: {e}")
            return Command(update={
                "error": f"Error checking domain relevance: {str(e)}",
                "next_action": "end"
            })

    def generate_query(self, state: OverallState) -> Command:
        """
        Generates a Cypher query from the natural language question.
        """
        try:
            if "text2cypher" not in self.engines:
                raise ValueError("Missing 'text2cypher' engine in configuration")
                
            # Get examples for few-shot learning
            examples = self.example_selector.select_examples({"question": state.question})
            
            fewshot_examples = "\n".join([
                f"Question: {example['question']}\nCypher query: {example['query']}"
                for example in examples
            ])
            
            cypher_statement = self.engines["text2cypher"].invoke({
                "question": state.question,
                "fewshot_examples": fewshot_examples
            })
            
            logger.info(f"Generated Cypher query: {cypher_statement}")
            
            return Command(update={
                "cypher_statement": cypher_statement,
                "steps": state.steps + ["generate_query"],
            })
        except Exception as e:
            logger.error(f"Error in generate_query: {e}")
            return Command(update={
                "error": f"Error generating Cypher query: {str(e)}",
                "next_action": "end"
            })

    def validate_query(self, state: OverallState) -> Command:
        """
        Validates the Cypher query and checks for errors.
        """
        try:
            if "validate_cypher" not in self.engines:
                raise ValueError("Missing 'validate_cypher' engine in configuration")
                
            validation_result = self.engines["validate_cypher"].invoke({
                "question": state.question,
                "cypher": state.cypher_statement,
                "schema": self.graph_db_enhanced_schema.schema,
            })
            
            if validation_result.is_valid == False:
                return Command(update={
                    "next_action": "correct_cypher",
                    "cypher_errors": validation_result.errors,
                    "steps": state.steps + ["validate_query"],
                })
            else:
                return Command(update={
                    "next_action": "execute_query",
                    "steps": state.steps + ["validate_query"],
                })
        except Exception as e:
            logger.error(f"Error in validate_query: {e}")
            return Command(update={
                "error": f"Error validating Cypher query: {str(e)}",
                "next_action": "end"
            })

    def correct_query(self, state: OverallState) -> Command:
        """
        Corrects the Cypher query based on validation errors.
        """
        try:
            if "correct_cypher" not in self.engines:
                raise ValueError("Missing 'correct_cypher' engine in configuration")
                
            corrected_cypher = self.engines["correct_cypher"].invoke({
                "question": state.question,
                "errors": state.cypher_errors,
                "cypher": state.cypher_statement,
                "schema": self.graph_db_enhanced_schema.schema,
            })
            
            return Command(update={
                "next_action": "validate_query",
                "cypher_statement": corrected_cypher,
                "steps": state.steps + ["correct_query"],
            })
        except Exception as e:
            logger.error(f"Error in correct_query: {e}")
            return Command(update={
                "error": f"Error correcting Cypher query: {str(e)}",
                "next_action": "end"
            })

    def execute_query(self, state: OverallState) -> Command:
        """
        Executes the Cypher query against the Neo4j database.
        """
        try:
            records = self.graph_db.query(state.cypher_statement)
            
            return Command(update={
                "database_records": records if records else self.no_results,
                "next_action": "generate_answer",
                "steps": state.steps + ["execute_query"],
            })
        except Exception as e:
            logger.error(f"Error in execute_query: {e}")
            return Command(update={
                "error": f"Error executing Cypher query: {str(e)}",
                "next_action": "end"
            })

    def generate_answer(self, state: OverallState) -> Command:
        """
        Generates the final answer based on the query results.
        """
        try:
            if "generate_final_answer" not in self.engines:
                raise ValueError("Missing 'generate_final_answer' engine in configuration")
                
            if state.database_records == self.no_results:
                answer = f"I couldn't find any information about your question: {state.question}"
            else:
                answer = self.engines["generate_final_answer"].invoke({
                    "question": state.question,
                    "results": state.database_records
                })
            
            return Command(update={
                "answer": answer,
                "next_action": "end",
                "steps": state.steps + ["generate_answer"],
            })
        except Exception as e:
            logger.error(f"Error in generate_answer: {e}")
            return Command(update={
                "error": f"Error generating answer: {str(e)}",
                "answer": f"An error occurred while generating the answer: {str(e)}",
                "next_action": "end"
            })

    def domain_router(self, state: OverallState) -> str:
        """Route based on domain relevance check."""
        if state.next_action == "end":
            return END
        return "generate_query"

    def validation_router(self, state: OverallState) -> str:
        """Route based on query validation."""
        if state.next_action == "end":
            return END
        elif state.next_action == "correct_cypher":
            return "correct_query"
        return "execute_query"

    def setup_workflow(self) -> None:
        """
        Set up the Graph DB RAG workflow.
        """
        # Add nodes for the workflow
        self.graph.add_node("check_domain_relevance", self.check_domain_relevance)
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
            "default": "generate_query"
        })
        self.graph.add_conditional_edges("check_domain_relevance", domain_branch, lambda x: x["next_action"])
        
        self.graph.add_edge("generate_query", "validate_query")
        
        validation_branch = Branch.from_dict({
            "correct_cypher": "correct_query",
            "end": END,
            "default": "execute_query"
        })
        self.graph.add_conditional_edges("validate_query", validation_branch, lambda x: x["next_action"])
        
        self.graph.add_edge("correct_query", "validate_query")
        self.graph.add_edge("execute_query", "generate_answer")
        self.graph.add_edge("generate_answer", END)
        
        logger.info("Graph DB RAG workflow setup complete")

# For backward compatibility
GraphDBAgent = GraphDBRAGAgent

def main():
    agent = GraphDBRAGAgent()
    for output in agent.app.stream({"question": "What is the movie with the highest rating?"}, config=agent.runnable_config, debug=True):
        print(output)

if __name__ == "__main__":
    main()