from asyncio.log import logger

from haive.agents.rag.base.config import BaseRAGConfig
from haive.core.engine.agent.agent import Agent, register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from langgraph.graph import START, END
from langgraph.types import Command
@register_agent(BaseRAGConfig)
class BaseRAGAgent(Agent[BaseRAGConfig]):
    """
    Base RAG agent that focuses on document retrieval.
    
    This agent implements a basic workflow:
    1. Receive a query
    2. Retrieve relevant documents using existing retriever/vectorstore engine
    """

    def setup_workflow(self) -> None:
        """
        Set up the dynamic workflow for the RAG agent.
        
        Creates a simple graph for document retrieval using existing engines.
        """
        # Get the engine from the config
        retriever_engine = self.config.engine
        
        # Debug: Log retriever details
        logger.info(f"Setting up retriever node with engine: {retriever_engine.name} (ID: {getattr(retriever_engine, 'id', 'unknown')})")
        
        # Enable debug mode in NodeFactory for better visibility
        from haive.core.graph.node.factory import NodeFactory
        NodeFactory.set_debug(True, log_path="retriever_node_debug.log")
        
        # Create a dynamic graph builder with your existing state schema
        graph_builder = DynamicGraph(
            name=f"{self.config.name}_workflow",
            components=[retriever_engine],
            state_schema=self.config.state_schema,
            input_schema=self.config.input_schema,
            output_schema=self.config.output_schema
        )
        
        # Explicit input/output mapping - be very specific about which fields go where
        input_mapping = {"query": "query"}  # Map state.query to retriever input
        output_mapping = {"documents": "retrieved_documents"}  # Map retriever result.documents to state.retrieved_documents
        
        logger.info(f"Adding retrieve_documents node with explicit mappings:")
        logger.info(f"Input mapping: {input_mapping}")
        logger.info(f"Output mapping: {output_mapping}")
        
        # Test the retriever directly with a query to verify it works
        try:
            # Directly invoke the retriever with a simple query
            test_query = "test query"
            logger.info(f"Testing retriever directly with query: '{test_query}'")
            test_result = retriever_engine.invoke(test_query)
            
            # Log the result to see what's being returned
            logger.info(f"Retriever direct test returned {len(test_result)} documents")
            logger.info(f"Result type: {type(test_result).__name__}")
            
            # Check the keys in the result if it's a dictionary
            if isinstance(test_result, dict):
                logger.info(f"Result keys: {list(test_result.keys())}")
                
                # Get the documents from the correct key if needed
                if "documents" in test_result:
                    logger.info(f"Found {len(test_result['documents'])} documents in 'documents' key")
                    
                    # Adjust output mapping if necessary
                    if not output_mapping:
                        output_mapping = {"documents": "retrieved_documents"}
                        logger.info(f"Updated output mapping to: {output_mapping}")
        except Exception as e:
            logger.error(f"Error testing retriever: {e}")
        
        # Create a custom retriever node function to ensure proper input/output handling
        def retriever_node(state):
            logger.info(f"Retriever node called with state: {state}")
            
            # Extract query from state
            query = state.query
            logger.info(f"Processing query: '{query}'")
            
            try:
                # Directly invoke the retriever
                result = retriever_engine.invoke(query)
                logger.info(f"Retriever returned result of type: {type(result).__name__}")
                
                if isinstance(result, list):
                    logger.info(f"Retrieved {len(result)} documents")
                    
                    # Create a proper update dictionary for the Command
                    return Command(
                        update={
                            "retrieved_documents": result,
                            "query": query,  # Preserve the query
                            "answer": ""  # Initialize empty answer
                        },
                        goto=END
                    )
                elif isinstance(result, dict) and "documents" in result:
                    # Handle case where retriever returns a dict with 'documents' key
                    documents = result["documents"]
                    logger.info(f"Retrieved {len(documents)} documents from 'documents' key")
                    
                    return Command(
                        update={
                            "retrieved_documents": documents,
                            "query": query,
                            "answer": ""
                        },
                        goto=END
                    )
                else:
                    logger.warning(f"Unexpected retriever result format: {type(result).__name__}")
                    return Command(
                        update={
                            "retrieved_documents": [],
                            "query": query,
                            "answer": "",
                            "error": f"Unexpected retriever result format: {type(result).__name__}"
                        },
                        goto=END
                    )
            except Exception as e:
                logger.error(f"Error in retriever node: {e}")
                return Command(
                    update={
                        "retrieved_documents": [],
                        "query": query,
                        "answer": "",
                        "error": str(e)
                    },
                    goto=END
                )
        
        # Add the custom retriever node
        graph_builder.add_node("retrieve_documents", retriever_node)
        
        # Set workflow edges
        graph_builder.add_edge(START, "retrieve_documents")
        
        # Log the state schema
        logger.info(f"State schema fields: {list(self.config.state_schema.__annotations__.keys())}")
        
        # Compile the graph
        self.graph = graph_builder.build()
        
        logger.info(f"Basic retrieval workflow set up for {self.config.name}")