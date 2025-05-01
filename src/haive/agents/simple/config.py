"""
Configuration for SimpleAgent with comprehensive schema handling.

This module defines the configuration class for SimpleAgent with explicit
input/output schema support, schema composition integration, and improved
mapping capabilities.
"""

import logging
import uuid
from datetime import datetime
from typing import Optional, Dict, Type, Any, Union, List, ClassVar

from pydantic import BaseModel, Field, field_validator, model_validator
from langchain_core.messages import SystemMessage, BaseMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from haive.core.schema.schema_composer import SchemaComposer
from haive.core.schema.state_schema import StateSchema

# Setup logging
logger = logging.getLogger(__name__)

class SimpleAgentConfig(AgentConfig):
    """
    Configuration for a simple single-node agent with comprehensive schema handling.
    
    This config supports:
    - Explicit input/output schemas
    - Auto-derived state schema
    - Structured output models
    - Intelligent input/output mappings
    """
    # Required engine (must be AugLLMConfig)
    engine: AugLLMConfig = Field(
        description="The AugLLM engine to use for reasoning"
    )
    
    # Schema definitions
    input_schema: Optional[Type[BaseModel]] = Field(
        default=None,
        description="Schema defining agent inputs (None for auto-derive)"
    )
    
    output_schema: Optional[Type[BaseModel]] = Field(
        default=None,
        description="Schema defining agent outputs (None for auto-derive)"
    )
    
    state_schema: Optional[Type[StateSchema]] = Field(
        default=None, 
        description="Schema for the agent state (None for auto-derive)"
    )
    
    # Mapping configuration
    input_mapping: Optional[Dict[str, str]] = Field(
        default=None, 
        description="Maps state fields to engine input fields (None for auto-derive)"
    )
    
    output_mapping: Optional[Dict[str, str]] = Field(
        default=None, 
        description="Maps engine output fields to state fields (None for auto-derive)"
    )
    
    # Node configuration
    node_name: str = Field(
        default="process",
        description="Name for the single processing node"
    )
    
    # Visualization settings
    visualize: bool = Field(
        default=True, 
        description="Whether to visualize the graph"
    )
    
    model_config = {
        "arbitrary_types_allowed": True
    }
    
    @field_validator("engine")
    def validate_engine(cls, v):
        """Ensure engine is an AugLLMConfig instance"""
        if not isinstance(v, AugLLMConfig):
            raise TypeError(f"Engine must be AugLLMConfig, got {type(v)}")
        return v
    
    @field_validator("input_mapping", "output_mapping", mode="after")
    def validate_mappings(cls, v, info):
        """Validate mappings if provided"""
        if v is None:
            return v  # None is allowed for auto-derivation
            
        if not isinstance(v, dict):
            raise TypeError(f"{info.field_name} must be a dictionary")
            
        # Validate all keys and values are strings
        for key, value in v.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise TypeError(f"All keys and values in {info.field_name} must be strings")
                
        return v
    
    @model_validator(mode="after")
    def derive_schemas(self):
        """
        Derive and reconcile schemas based on engine and provided schemas.
        
        This ensures all schemas are coherent with each other while respecting
        any explicitly provided schemas.
        """
        # Create schema composer from engine
        schema_composer = SchemaComposer.from_components([self.engine])
        
        # Step 1: Handle state schema
        if self.state_schema is None:
            # Auto-derive state schema
            self.state_schema = schema_composer.build()
            logger.debug(f"Auto-derived state schema: {self.state_schema.__name__}")
        #else:
            # Use the provided state schema but update schema composer
            #schema_composer = SchemaComposer.from_state_schema(self.state_schema)
        
        # Step 2: Handle input schema
        if self.input_schema is None:
            # Derive input schema
            self.input_schema = schema_composer.create_input_schema()
            logger.debug(f"Auto-derived input schema: {self.input_schema.__name__}")
        
        # Step 3: Handle output schema
        if self.output_schema is None:
            # Check if engine has structured output model
            if hasattr(self.engine, "structured_output_model") and self.engine.structured_output_model:
                # Use structured output model as output schema
                self.output_schema = self.engine.structured_output_model
                logger.debug(f"Using structured output model as output schema: {self.output_schema.__name__}")
            else:
                # Derive output schema
                self.output_schema = schema_composer.create_output_schema()
                logger.debug(f"Auto-derived output schema: {self.output_schema.__name__}")
                
        # Step 4: Validate schema compatibility
        self._validate_schema_compatibility()
        
        return self
    
    def _validate_schema_compatibility(self):
        """Validate that all schemas are compatible with each other"""
        # Check input schema fields exist in state schema
        if self.input_schema and self.state_schema:
            input_fields = set(self.input_schema.model_fields.keys())
            state_fields = set(self.state_schema.model_fields.keys())
            
            missing_fields = input_fields - state_fields
            if missing_fields:
                logger.warning(f"Input schema has fields not in state schema: {missing_fields}")
                
        # Check output schema fields exist in state schema
        if self.output_schema and self.state_schema:
            output_fields = set(self.output_schema.model_fields.keys())
            state_fields = set(self.state_schema.model_fields.keys())
            
            missing_fields = output_fields - state_fields
            if missing_fields:
                logger.warning(f"Output schema has fields not in state schema: {missing_fields}")
    
    def derive_input_mapping(self) -> Dict[str, str]:
        """
        Derive input mapping based on engine and schemas.
        
        Returns:
            Dictionary mapping state fields to engine input fields
        """
        # Use provided mapping if available
        if self.input_mapping is not None:
            return self.input_mapping
        
        # Get engine input fields
        engine_fields = set()
        if hasattr(self.engine, "get_input_fields") and callable(self.engine.get_input_fields):
            engine_fields = set(self.engine.get_input_fields().keys())
        
        # Get input schema fields
        input_fields = set()
        if self.input_schema:
            input_fields = set(self.input_schema.model_fields.keys())
        
        # Find common fields
        common_fields = engine_fields.intersection(input_fields)
        if common_fields:
            # Map common fields directly (1:1)
            mapping = {field: field for field in common_fields}
            logger.debug(f"Auto-derived input mapping from common fields: {mapping}")
            return mapping
        
        # If prompt template has input variables, use those
        if hasattr(self.engine, "prompt_template") and hasattr(self.engine.prompt_template, "input_variables"):
            input_vars = set(self.engine.prompt_template.input_variables)
            if input_vars.intersection(input_fields):
                mapping = {var: var for var in input_vars if var in input_fields}
                logger.debug(f"Auto-derived input mapping from prompt variables: {mapping}")
                return mapping
        
        # Default mapping: use 'messages' if available in both
        if "messages" in engine_fields and "messages" in input_fields:
            mapping = {"messages": "messages"}
            logger.debug(f"Using default input mapping: {mapping}")
            return mapping
        
        # Last resort: map all input fields to themselves and hope engine handles it
        mapping = {field: field for field in input_fields}
        logger.debug(f"Using fallback input mapping: {mapping}")
        return mapping
    
    def derive_output_mapping(self) -> Dict[str, str]:
        """
        Derive output mapping based on engine and schemas.
        
        Returns:
            Dictionary mapping engine output fields to state fields
        """
        # Use provided mapping if available
        if self.output_mapping is not None:
            return self.output_mapping
        
        # Handle structured output model specially
        structured_model = getattr(self.engine, "structured_output_model", None)
        if structured_model is not None:
            # Map model name to itself
            model_name = structured_model.__name__.lower()
            mapping = {model_name: model_name}
            logger.debug(f"Auto-derived output mapping for structured model: {mapping}")
            return mapping
        
        # Get engine output fields
        engine_fields = set()
        if hasattr(self.engine, "get_output_fields") and callable(self.engine.get_output_fields):
            engine_fields = set(self.engine.get_output_fields().keys())
        
        # Get output schema fields
        output_fields = set()
        if self.output_schema:
            output_fields = set(self.output_schema.model_fields.keys())
        
        # Find common fields
        common_fields = engine_fields.intersection(output_fields)
        if common_fields:
            # Map common fields directly (1:1)
            mapping = {field: field for field in common_fields}
            logger.debug(f"Auto-derived output mapping from common fields: {mapping}")
            return mapping
        
        # Default output mapping based on common patterns
        if "content" in engine_fields:
            field = "output" if "output" in output_fields else "content"
            mapping = {"content": field}
            logger.debug(f"Using content-based output mapping: {mapping}")
            return mapping
            
        if "messages" in engine_fields and "messages" in output_fields:
            mapping = {"messages": "messages"}
            logger.debug(f"Using messages-based output mapping: {mapping}")
            return mapping
            
        # Last resort: map engine fields to same-named state fields
        mapping = {field: field for field in engine_fields}
        logger.debug(f"Using fallback output mapping: {mapping}")
        return mapping
    
    def build_agent(self):
        """Build and return a SimpleAgent instance"""
        from haive.agents.simple.agent import SimpleAgent
        return SimpleAgent(self)
    
    @classmethod
    def from_aug_llm(cls, 
                    aug_llm: AugLLMConfig, 
                    name: Optional[str] = None,
                    id: Optional[str] = None,
                    input_schema: Optional[Type[BaseModel]] = None,
                    output_schema: Optional[Type[BaseModel]] = None,
                    state_schema: Optional[Type[StateSchema]] = None,
                    **kwargs) -> 'SimpleAgentConfig':
        """
        Create a SimpleAgentConfig from an existing AugLLMConfig.
        
        Args:
            aug_llm: Existing AugLLMConfig to use
            name: Optional agent name
            id: Optional unique identifier
            input_schema: Optional explicit input schema
            output_schema: Optional explicit output schema
            state_schema: Optional explicit state schema
            **kwargs: Additional kwargs for the config
            
        Returns:
            SimpleAgentConfig instance
        """
        # Generate default name if not provided
        if name is None:
            name = f"simple_agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Generate default ID if not provided
        if id is None:
            id = f"agent_{uuid.uuid4().hex[:8]}"
            
        return cls(
            id=id,
            name=name,
            engine=aug_llm,
            input_schema=input_schema,
            output_schema=output_schema,
            state_schema=state_schema,
            **kwargs
        )
    
    @classmethod
    def from_scratch(cls, 
                    system_prompt: str = "You are a helpful assistant.",
                    model: str = "gpt-4o", 
                    temperature: float = 0.7,
                    structured_output_model: Optional[Type[BaseModel]] = None,
                    name: Optional[str] = None,
                    id: Optional[str] = None,
                    input_schema: Optional[Type[BaseModel]] = None,
                    output_schema: Optional[Type[BaseModel]] = None,
                    state_schema: Optional[Type[StateSchema]] = None,
                    **kwargs) -> 'SimpleAgentConfig':
        """
        Create a SimpleAgentConfig from scratch with a new AugLLMConfig.
        
        Args:
            system_prompt: System prompt for the LLM
            model: Model identifier to use
            temperature: Generation temperature
            structured_output_model: Optional model for structured outputs
            name: Optional agent name
            id: Optional unique identifier
            input_schema: Optional explicit input schema
            output_schema: Optional explicit output schema 
            state_schema: Optional explicit state schema
            **kwargs: Additional kwargs for the config
            
        Returns:
            SimpleAgentConfig instance
        """
        # Create base LLM config
        llm_config = AzureLLMConfig(
            model=model,
            parameters={"temperature": temperature}
        )
        
        # Create messages for prompt template
        messages = [
            SystemMessage(content=system_prompt),
            MessagesPlaceholder(variable_name="messages")
        ]
        prompt_template = ChatPromptTemplate.from_messages(messages)
        
        # Create AugLLMConfig
        aug_llm = AugLLMConfig(
            name=f"llm_{uuid.uuid4().hex[:6]}",
            llm_config=llm_config,
            prompt_template=prompt_template,
            system_prompt=system_prompt,
            structured_output_model=structured_output_model
        )
        
        # If structured output model is provided but no output schema, use the model
        if structured_output_model is not None and output_schema is None:
            output_schema = structured_output_model
        
        # Create SimpleAgentConfig using from_aug_llm
        return cls.from_aug_llm(
            aug_llm=aug_llm,
            name=name,
            id=id,
            input_schema=input_schema,
            output_schema=output_schema,
            state_schema=state_schema,
            **kwargs
        )
    
    @classmethod
    def with_structured_output(cls,
                              output_model: Type[BaseModel],
                              system_prompt: Optional[str] = None,
                              model: str = "gpt-4o",
                              temperature: float = 0.2,
                              name: Optional[str] = None,
                              **kwargs) -> 'SimpleAgentConfig':
        """
        Create a SimpleAgentConfig with structured output capabilities.
        
        Args:
            output_model: Pydantic model for structured output
            system_prompt: Optional system prompt (default derived from model)
            model: Model identifier
            temperature: Generation temperature (lower for structured outputs)
            name: Optional agent name
            **kwargs: Additional kwargs for the config
            
        Returns:
            SimpleAgentConfig with structured output capability
        """
        # Derive system prompt from model if not provided
        if system_prompt is None:
            model_name = output_model.__name__
            system_prompt = (
                f"You are a helpful assistant that provides detailed responses in a specific format. "
                f"You will analyze the user's request and provide a structured {model_name} response."
            )
        
        # Create from scratch with structured output model
        return cls.from_scratch(
            system_prompt=system_prompt,
            model=model,
            temperature=temperature,
            structured_output_model=output_model,
            output_schema=output_model,  # Use model as output schema directly
            name=name or f"structured_{output_model.__name__.lower()}_agent",
            **kwargs
        )