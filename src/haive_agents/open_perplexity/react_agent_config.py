from typing import Optional, List, Dict, Any, Union
from pydantic import Field
import uuid
from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from langchain_core.tools import BaseTool

from haive_core.models.llm.base import AzureLLMConfig
from haive_core.engine.aug_llm import AugLLMConfig
from haive_agents.v2.config import ReactAgentConfig
from haive_agents.rag.base.config import BaseRAGConfig
from haive_core.engine.retriever import VectorStoreRetrieverConfig
from haive_core.models.vectorstore.base import VectorStoreConfig

# Import agent-specific modules
from haive_agents.open_perplexity.prompts import RESEARCH_SYSTEM_PROMPT
from haive_agents.open_perplexity.structured_tools import RESEARCH_TOOLS

def create_research_react_agent_config(name: Optional[str] = None, 
                                 llm_model: str = "gpt-4o", 
                                 temperature: float = 0.2) -> ReactAgentConfig:
    """
    Create a ReactAgentConfig specifically for deep research tasks.
    
    Args:
        name: Optional name for the agent
        llm_model: Model to use (default: gpt-4o)
        temperature: Temperature setting (default: 0.2)
        
    Returns:
        Configured ReactAgentConfig
    """
    # Create a name if not provided
    if not name:
        name = f"open_perplexity_research_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Create LLM configuration
    llm_config = AzureLLMConfig(
        model=llm_model,
        parameters={
            "temperature": temperature,
            "max_tokens": 4000
        }
    )
    
    # Create system message for the ReactAgent
    system_message = RESEARCH_SYSTEM_PROMPT
    
    # Create ReactAgentConfig with research-specific tools
    react_config = ReactAgentConfig(
        name=name,
        llm_config=llm_config,
        system_prompt=system_message,
        tools=RESEARCH_TOOLS,
        max_iterations=15,  # Increased for thorough research
        verbose=True
    )
    
    return react_config

def create_research_rag_engine(name: Optional[str] = None,
                         llm_model: str = "gpt-4o",
                         temperature: float = 0.2) -> AugLLMConfig:
    """
    Create an AugLLMConfig for research document retrieval tasks.
    
    Args:
        name: Optional name for the engine
        llm_model: Model to use (default: gpt-4o)
        temperature: Temperature setting (default: 0.2)
        
    Returns:
        Configured AugLLMConfig for RAG
    """
    # Create a name if not provided
    if not name:
        name = f"open_perplexity_retrieval_engine_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Create LLM configuration
    llm_config = AzureLLMConfig(
        model=llm_model,
        parameters={
            "temperature": temperature,
            "max_tokens": 4000
        }
    )
    
    # Create system message
    system_message = """
    You are a research document retrieval assistant. Your role is to:
    1. Retrieve relevant documents about the research topic
    2. Extract key information and insights
    3. Focus on high-quality, reliable sources
    4. Identify connections between pieces of information
    
    Be thorough and accurate in your retrieval and analysis. Prioritize authoritative sources while
    considering multiple perspectives on the topic.
    """
    
    # Create AugLLM configuration
    rag_engine = AugLLMConfig(
        name=name,
        llm_config=llm_config,
        prompt_template=ChatPromptTemplate.from_messages([
            SystemMessage(content=system_message),
            MessagesPlaceholder(variable_name="messages")
        ])
    )
    
    return rag_engine

def create_research_rag_agent_config(vectorstore_config: VectorStoreConfig, 
                                name: Optional[str] = None,
                                llm_model: str = "gpt-4o",
                                temperature: float = 0.2) -> BaseRAGConfig:
    """
    Create a BaseRAGConfig for research document retrieval tasks.
    This function requires a vectorstore_config with loaded documents.
    
    Args:
        vectorstore_config: Vector store configuration with loaded documents
        name: Optional name for the agent
        llm_model: Model to use (default: gpt-4o)
        temperature: Temperature setting (default: 0.2)
        
    Returns:
        Configured BaseRAGConfig
    """
    # Create a name if not provided
    if not name:
        name = f"open_perplexity_retrieval_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Create the RAG engine
    rag_engine = create_research_rag_engine(
        name=f"{name}_engine",
        llm_model=llm_model,
        temperature=temperature
    )
    
    # Create a retriever config from the vector store
    retriever_config = VectorStoreRetrieverConfig(
        name=f"retriever_for_{name}",
        vector_store_config=vectorstore_config,
        search_type="similarity_score_threshold",  # Use similarity with threshold for better results
        search_kwargs={
            "k": 8,  # Retrieve more documents for comprehensive research
            "score_threshold": 0.7  # Only include highly relevant documents
        }
    )
    
    # Create BaseRAGConfig with proper retriever configuration
    rag_config = BaseRAGConfig(
        name=name,
        engine=rag_engine,
        retriever_config=retriever_config
    )
    
    return rag_config 