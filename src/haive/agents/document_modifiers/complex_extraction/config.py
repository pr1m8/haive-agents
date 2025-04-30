from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from haive.agents.document_modifiers.complex_extraction.state import ComplexExtractionInput,ComplexExtractionOutput,ComplexExtractionState
from pydantic import BaseModel, Field
from typing import Optional, Type
from haive.core.models.llm.base import AzureLLMConfig   
from haive.core.engine.agent.agent import RunnableConfig
import uuid

class ComplexExtractionAgentConfig(AgentConfig):
    """
    Configuration for the complex extraction agent.
    
    This agent handles the extraction of complex structured data from text
    using a validation and retry mechanism with optional JSONPatch corrections.
    """
    llm_config: Optional[AugLLMConfig] = Field(
        default=AzureLLMConfig(model="gpt-4o"),
        description="The LLM configuration to use for the agent"
    )
    extraction_model: Optional[Type[BaseModel]] = Field(
        default=None,
        description="The Pydantic model to extract data into"
    )
    max_retries: int = Field(
        default=3,
        description="Maximum number of extraction attempts"
    )
    force_tool_choice: bool = Field(
        default=True,
        description="Whether to force the tool choice to use the extraction model"
    )
    state_schema: Type[BaseModel] = Field(
        default=ComplexExtractionState,
        description="State schema for the agent"
    )
    system_prompt: str = Field(
        default="You are a precise data extraction assistant. Extract the requested information accurately from the provided text.",
        description="System prompt for extraction"
    )
    use_jsonpatch: bool = Field(
        default=True,
        description="Whether to use JSONPatch retries for validation"
    )
    runnable_config: RunnableConfig = Field(
        default=RunnableConfig(
            configurable={"thread_id": str(uuid.uuid4())},
            debug=True
        ),
        description="The runnable configuration to use for the agent"
    )

    input_schema: Type[BaseModel] = Field(
        default=ComplexExtractionInput,
        description="The input schema for the agent"
    )
    output_schema: Type[BaseModel] = Field(
        default=ComplexExtractionOutput,
        description="The output schema for the agent"   
    )
