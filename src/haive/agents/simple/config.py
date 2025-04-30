"""
Configuration for SimpleAgent with factory methods.

This module defines the configuration class for SimpleAgent, including
validation logic and factory methods for easy creation.
"""

import logging
import traceback
from datetime import datetime
from typing import Optional, Dict, Type, Any, Union

from pydantic import BaseModel, Field, field_validator,model_validator
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig, LLMConfig

# Setup logging
logger = logging.getLogger(__name__)

class SimpleAgentConfig(AgentConfig):
    """
    Configuration for a simple single-node agent.
    
    This is a basic agent with a single reasoning node that processes input
    and generates output without complex workflow or tool usage.
    """
    engine: Optional[Any] = Field(
        default=AugLLMConfig(),
        description="The engine to use for the agent."
    )
    
    node_name: str = Field(
        default="simple_agent_node", 
        description="Name for the single processing node."
    )
    
    input_mapping: Optional[Dict[str, str]] = Field(
        default={'messages': 'messages'}, 
        description="Maps state fields to engine input fields."
    )
    
    output_mapping: Optional[Dict[str, str]] = Field(
        default={'messages': 'messages'}, 
        description="Maps engine output fields to state fields."
    )
    
    system_prompt: str = Field(
        default="You are a helpful assistant.", 
        description="System prompt for the agent."
    )
    
    state_schema: Optional[Union[Type[BaseModel], Dict[str, Any]]] = Field(
        default=None, 
        description="Schema for the agent state."
    )
    
    visualize: bool = Field(
        default=True, 
        description="Whether to visualize the graph."
    )
    
    structured_output_model: Optional[Type[BaseModel]] = Field(
        default=None,
        description="Optional model for structured output parsing"
    )
    @field_validator("input_mapping", "output_mapping", mode="after")
    def validate_mappings(cls, v, info):
        """
        Validates that the input and output mappings are properly structured.
        
        Args:
            v: The value to validate
            info: ValidationInfo with the field name
            
        Returns:
            The validated mapping or None
        """
        field_name = info.field_name
        
        # None is acceptable as it means we'll use defaults
        if v is None:
            return v
            
        # Ensure it's a dictionary
        if not isinstance(v, dict):
            logger.error(f"🚨 {field_name} must be a dictionary, got {type(v)}")
            raise TypeError(f"{field_name} must be a dictionary, got {type(v)}")
        
        # Ensure all keys and values are strings
        for key, value in v.items():
            if not isinstance(key, str):
                logger.error(f"🚨 All keys in {field_name} must be strings, got {type(key)}")
                raise TypeError(f"All keys in {field_name} must be strings")
            if not isinstance(value, str):
                logger.error(f"🚨 All values in {field_name} must be strings, got {type(value)}")
                raise TypeError(f"All values in {field_name} must be strings")
        
        # Check for special handling of the 'messages' field in input_mapping
        if field_name == "input_mapping" and v and "messages" not in v and not hasattr(cls, "_has_warned_messages"):
            logger.warning(f"⚠️ No 'messages' field found in input_mapping. This may cause issues if using messages as input.")
            # Set a class attribute to prevent repeated warnings
            setattr(cls, "_has_warned_messages", True)
        
        logger.debug(f"✅ {field_name} validated successfully: {v}")
        return v
    @model_validator(mode="after")
    def validate_engine_mappings_compatibility(self):
        """
        Validates that the engine and mappings are compatible.
        
        Checks that input_mapping and output_mapping align with the engine's
        expected input and output fields.
        """
        if not hasattr(self, "engine") or self.engine is None:
            return self
            
        # Skip validation if no mappings are defined
        if not self.input_mapping and not self.output_mapping:
            return self
        
        # Try to get engine's input and output fields if available
        input_fields = []
        output_fields = []
        
        # Check if engine has schemas
        if hasattr(self.engine, "derive_input_schema") and callable(self.engine.derive_input_schema):
            try:
                input_schema = self.engine.derive_input_schema()
                input_fields = list(input_schema.model_fields.keys())
            except Exception as e:
                logger.warning(f"⚠️ Could not derive input schema from engine: {e}")
        
        if hasattr(self.engine, "derive_output_schema") and callable(self.engine.derive_output_schema):
            try:
                output_schema = self.engine.derive_output_schema()
                output_fields = list(output_schema.model_fields.keys())
            except Exception as e:
                logger.warning(f"⚠️ Could not derive output schema from engine: {e}")
        
        # If we have input mapping and input fields, validate field existence
        if self.input_mapping and input_fields:
            for engine_field in self.input_mapping.values():
                if engine_field not in input_fields:
                    logger.warning(f"⚠️ Input mapping maps to non-existent engine field '{engine_field}'. Available fields: {input_fields}")
        
        # If we have output mapping and output fields, validate field existence
        if self.output_mapping and output_fields:
            for engine_field, _ in self.output_mapping.items():
                if engine_field not in output_fields:
                    logger.warning(f"⚠️ Output mapping references non-existent engine field '{engine_field}'. Available fields: {output_fields}")
        
        return self
    @field_validator("engine", mode="after")
    def check_engine_present(cls, v):
        """
        Ensures that `engine` is an instance of `AugLLMConfig`
        """
        try:
            if v is None:
                logger.error("🚨 Engine is required but got None")
                raise ValueError("Engine is required.")
            
            # Get the class name rather than doing direct isinstance check
            engine_class_name = v.__class__.__name__
            if engine_class_name != "AugLLMConfig" and not isinstance(v, AugLLMConfig):
                logger.error(f"🚨 Invalid engine type: Expected AugLLMConfig, got {type(v)}")
                raise TypeError(f"Expected AugLLMConfig, but got {type(v)}")
            
            logger.debug(f"✅ Engine validated successfully: {v}")
            return v
        except Exception as e:
            logger.error("🚨 Error in check_engine_present", exc_info=True)
            logger.error(traceback.format_exc())
            raise
            
    def build_agent(self):
        """
        Build and return a SimpleAgent instance based on this configuration.
        
        Returns:
            SimpleAgent instance
        """
        from haive.agents.simple.agent import SimpleAgent
        return SimpleAgent(self)
        
    @classmethod
    def from_aug_llm(cls, 
                    aug_llm: AugLLMConfig, 
                    name: Optional[str] = None, 
                    system_prompt: Optional[str] = None, 
                    **kwargs) -> 'SimpleAgentConfig':
        """
        Create a SimpleAgentConfig from an existing AugLLMConfig.
        
        Args:
            aug_llm: Existing AugLLMConfig to use
            name: Optional agent name
            system_prompt: Optional system prompt
            **kwargs: Additional kwargs for the config
            
        Returns:
            SimpleAgentConfig instance
        """
        try:
            logger.debug(f"🛠️ Creating SimpleAgentConfig with AugLLMConfig: {aug_llm}")
            if not isinstance(aug_llm, AugLLMConfig):
                logger.error(f"🚨 from_aug_llm received incorrect type: {type(aug_llm)}")
                raise TypeError(f"Expected AugLLMConfig but received {type(aug_llm)}")

            # Initialize input and output mappings
            input_mapping = None
            output_mapping = None

            # Set the system prompt in the AugLLMConfig if provided
            if system_prompt and system_prompt != aug_llm.system_prompt:
                aug_llm.system_prompt = system_prompt
                
                # Update prompt template if it exists
                if hasattr(aug_llm, 'prompt_template') and aug_llm.prompt_template:
                    # Try to update system message in prompt template
                    try:
                        messages = aug_llm.prompt_template.messages
                        for i, message in enumerate(messages):
                            if hasattr(message, 'type') and message.type == 'system':
                                messages[i] = SystemMessage(content=system_prompt)
                                break
                        
                        # Create new prompt template
                        aug_llm.prompt_template = ChatPromptTemplate.from_messages(messages)
                        
                        # Try to get input and output variables from aug_llm
                        if hasattr(aug_llm, '_get_input_variables'):
                            input_mapping = aug_llm._get_input_variables()
                        if hasattr(aug_llm, '_get_output_variables'):
                            output_mapping = aug_llm._get_output_variables()
                    except Exception as e:
                        logger.warning(f"Could not update prompt template: {e}")

            return cls(
                name=name or f"simple_agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                engine=aug_llm,
                system_prompt=system_prompt or aug_llm.system_message or "You are a helpful assistant.",
                input_mapping=input_mapping,
                output_mapping=output_mapping,
                **kwargs
            )
        except Exception as e:
            logger.error("🚨 Error in from_aug_llm", exc_info=True)
            logger.error(traceback.format_exc())
            raise
    @classmethod
    def from_scratch(cls, 
                    system_prompt: Optional[str] = None, 
                    model: str = "gpt-4o", 
                    temperature: float = 0.7, 
                    name: Optional[str] = None, 
                    **kwargs) -> 'SimpleAgentConfig':
        """
        Create a SimpleAgentConfig from scratch.
        
        Args:
            system_prompt: Optional system prompt
            model: Model name to use
            temperature: Temperature for generation
            name: Optional agent name
            **kwargs: Additional kwargs for the config
            
        Returns:
            SimpleAgentConfig instance
        """
        try:
            logger.debug(f"🛠️ Creating AugLLMConfig from scratch with model: {model}")

            # Create LLM config
            llm_config = AzureLLMConfig(
                model=model,
                parameters={"temperature": temperature}
            )

            # Set default system prompt if not provided
            system_prompt = system_prompt or "You are a helpful assistant."
            
            # Create prompt template with system message and message placeholder
            messages = [
                SystemMessage(content=system_prompt),
                MessagesPlaceholder(variable_name="messages")
            ]
            prompt_template = ChatPromptTemplate.from_messages(messages)

            # Create AugLLMConfig
            aug_llm = AugLLMConfig(
                name=f"{name or 'simple'}_llm",
                llm_config=llm_config,
                prompt_template=prompt_template,
                system_prompt=system_prompt
            )

            # Create and return SimpleAgentConfig
            return cls(
                name=name or f"simple_agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                engine=aug_llm,
                system_prompt=system_prompt,
                **kwargs
            )
        except Exception as e:
            logger.error("🚨 Error in from_scratch", exc_info=True)
            logger.error(traceback.format_exc())
            raise