"""Smart Output Parsing with Post-Hooks Integration.

This module demonstrates how to use GenericEngineNodeConfig and post-hooks
to handle specific output parsing in a smart, flexible manner.
"""

import logging
from typing import Any, Callable, Generic, Optional, TypeVar, Union

from langchain_core.messages import BaseMessage
from langchain_core.output_parsers.base import BaseOutputParser
from pydantic import BaseModel, Field

from haive.agents.base.hooks import HookEvent, HookContext
from haive.core.graph.node.callable_node import CallableNodeConfig
from haive.core.graph.node.engine_node_generic import GenericEngineNodeConfig
from haive.core.graph.node.output_parsing_v2 import (
    PydanticParserNodeConfig,
    create_pydantic_parser_node,
)

logger = logging.getLogger(__name__)

# Type variables
TInput = TypeVar("TInput", bound=BaseModel)
TOutput = TypeVar("TOutput", bound=BaseModel)
TParsed = TypeVar("TParsed", bound=BaseModel)


class SmartOutputParsingMixin:
    """Mixin to add smart output parsing capabilities to agents."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._output_parsing_hooks: dict[str, Callable] = {}
        self._setup_output_parsing_hooks()
    
    def _setup_output_parsing_hooks(self):
        """Setup post-processing hooks for output parsing."""
        if hasattr(self, 'add_hook'):
            # Add post-run hook for output parsing
            self.add_hook(HookEvent.AFTER_RUN, self._smart_output_parsing_hook)
    
    def _smart_output_parsing_hook(self, context: HookContext):
        """Post-hook that intelligently parses agent output based on context."""
        if not context.result:
            return
            
        # Detect what type of parsing is needed
        parsing_strategy = self._detect_parsing_strategy(context)
        
        if parsing_strategy:
            logger.info(f"Applying smart output parsing: {parsing_strategy}")
            parsed_result = self._apply_parsing_strategy(context, parsing_strategy)
            
            # Update context with parsed result
            if parsed_result is not None:
                context.metadata['parsed_output'] = parsed_result
                context.metadata['parsing_strategy'] = parsing_strategy
    
    def _detect_parsing_strategy(self, context: HookContext) -> Optional[str]:
        """Detect what parsing strategy should be applied."""
        result = context.result
        
        # Check if result has tool calls (structured output)
        if hasattr(result, 'tool_calls') and result.tool_calls:
            return "tool_calls"
        
        # Check if result content looks like JSON
        if hasattr(result, 'content'):
            content = result.content
            if isinstance(content, str):
                if content.strip().startswith('{') and content.strip().endswith('}'):
                    return "json"
                elif content.strip().startswith('[') and content.strip().endswith(']'):
                    return "list"
                elif '```json' in content:
                    return "json_markdown"
        
        # Check if agent has structured output model
        if hasattr(self, 'engine') and hasattr(self.engine, 'structured_output_model'):
            return "pydantic"
        
        return None
    
    def _apply_parsing_strategy(self, context: HookContext, strategy: str) -> Any:
        """Apply the detected parsing strategy."""
        try:
            if strategy == "tool_calls":
                return self._parse_tool_calls(context.result)
            elif strategy == "json":
                return self._parse_json_content(context.result)
            elif strategy == "json_markdown":
                return self._parse_json_markdown(context.result)
            elif strategy == "list":
                return self._parse_list_content(context.result)
            elif strategy == "pydantic":
                return self._parse_pydantic_content(context.result)
        except Exception as e:
            logger.warning(f"Smart parsing failed with strategy {strategy}: {e}")
            return None
    
    def _parse_tool_calls(self, result: Any) -> Any:
        """Parse tool calls from AI message."""
        if hasattr(result, 'tool_calls') and result.tool_calls:
            # Extract structured data from tool calls
            parsed_calls = []
            for tool_call in result.tool_calls:
                parsed_calls.append({
                    'name': tool_call.get('name'),
                    'args': tool_call.get('args'),
                    'id': tool_call.get('id')
                })
            return {'tool_calls': parsed_calls}
        return None
    
    def _parse_json_content(self, result: Any) -> Any:
        """Parse JSON content from message."""
        import json
        
        if hasattr(result, 'content'):
            try:
                return json.loads(result.content)
            except json.JSONDecodeError:
                return None
        return None
    
    def _parse_json_markdown(self, result: Any) -> Any:
        """Parse JSON content from markdown code blocks."""
        import json
        import re
        
        if hasattr(result, 'content'):
            content = result.content
            # Extract JSON from markdown code blocks
            json_match = re.search(r'```json\s*(.*?)\s*```', content, re.DOTALL)
            if json_match:
                try:
                    return json.loads(json_match.group(1))
                except json.JSONDecodeError:
                    return None
        return None
    
    def _parse_list_content(self, result: Any) -> Any:
        """Parse list content from message."""
        import json
        
        if hasattr(result, 'content'):
            try:
                return json.loads(result.content)
            except json.JSONDecodeError:
                # Try comma-separated parsing
                content = result.content.strip('[]')
                items = [item.strip().strip('"\'') for item in content.split(',')]
                return items
        return None
    
    def _parse_pydantic_content(self, result: Any) -> Any:
        """Parse content using engine's structured output model."""
        if hasattr(self, 'engine') and hasattr(self.engine, 'structured_output_model'):
            model_class = self.engine.structured_output_model
            if hasattr(result, 'content'):
                try:
                    import json
                    data = json.loads(result.content)
                    return model_class.model_validate(data)
                except Exception:
                    return None
        return None


class SmartGenericEngineNode(GenericEngineNodeConfig[TInput, TOutput]):
    """Enhanced GenericEngineNodeConfig with smart output parsing."""
    
    # Output parsing configuration
    enable_smart_parsing: bool = Field(
        default=True, 
        description="Enable smart output parsing post-processing"
    )
    
    parsing_strategies: list[str] = Field(
        default_factory=lambda: ["tool_calls", "json", "pydantic", "list"],
        description="Enabled parsing strategies in priority order"
    )
    
    custom_parsers: dict[str, BaseOutputParser] = Field(
        default_factory=dict,
        description="Custom parsers for specific content types"
    )
    
    post_processing_callables: list[Callable] = Field(
        default_factory=list,
        description="Custom post-processing functions"
    )
    
    def __call__(self, state, config=None):
        """Execute with smart output parsing post-processing."""
        # Execute the base engine node
        result = super().__call__(state, config)
        
        if self.enable_smart_parsing and hasattr(result, 'update'):
            # Apply smart parsing to the result
            parsed_update = self._apply_smart_parsing(result.update, state)
            if parsed_update:
                # Update the result with parsed data
                result.update.update(parsed_update)
        
        return result
    
    def _apply_smart_parsing(self, update_dict: dict, state) -> dict[str, Any]:
        """Apply smart parsing to update dictionary."""
        parsed_data = {}
        
        # Check for messages field
        if 'messages' in update_dict:
            messages = update_dict['messages']
            if messages and len(messages) > 0:
                last_message = messages[-1]
                
                # Apply parsing strategies in order
                for strategy in self.parsing_strategies:
                    parsed = self._apply_strategy(strategy, last_message, state)
                    if parsed is not None:
                        parsed_data[f'parsed_{strategy}'] = parsed
                        break
        
        # Apply custom parsers
        for parser_name, parser in self.custom_parsers.items():
            if 'messages' in update_dict:
                try:
                    content = self._extract_content(update_dict['messages'][-1])
                    if content:
                        parsed = parser.parse(content)
                        parsed_data[f'parsed_{parser_name}'] = parsed
                except Exception as e:
                    logger.debug(f"Custom parser {parser_name} failed: {e}")
        
        # Apply post-processing callables
        for callable_func in self.post_processing_callables:
            try:
                additional_data = callable_func(update_dict, state)
                if isinstance(additional_data, dict):
                    parsed_data.update(additional_data)
            except Exception as e:
                logger.debug(f"Post-processing callable failed: {e}")
        
        return parsed_data
    
    def _apply_strategy(self, strategy: str, message: Any, state) -> Any:
        """Apply a specific parsing strategy."""
        if strategy == "tool_calls":
            return self._parse_tool_calls(message)
        elif strategy == "json":
            return self._parse_json_content(message)
        elif strategy == "pydantic":
            return self._parse_pydantic_content(message, state)
        elif strategy == "list":
            return self._parse_list_content(message)
        return None
    
    def _parse_tool_calls(self, message: Any) -> Optional[list]:
        """Parse tool calls from message."""
        if hasattr(message, 'tool_calls') and message.tool_calls:
            return [
                {
                    'name': tc.get('name'),
                    'args': tc.get('args'),
                    'id': tc.get('id')
                }
                for tc in message.tool_calls
            ]
        return None
    
    def _parse_json_content(self, message: Any) -> Any:
        """Parse JSON from message content."""
        import json
        
        content = self._extract_content(message)
        if content:
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                return None
        return None
    
    def _parse_pydantic_content(self, message: Any, state) -> Any:
        """Parse using structured output model."""
        if hasattr(self, 'output_schema') and self.output_schema:
            content = self._extract_content(message)
            if content:
                try:
                    import json
                    data = json.loads(content)
                    return self.output_schema.model_validate(data)
                except Exception:
                    return None
        return None
    
    def _parse_list_content(self, message: Any) -> Optional[list]:
        """Parse list from message content."""
        import json
        
        content = self._extract_content(message)
        if content:
            try:
                result = json.loads(content)
                if isinstance(result, list):
                    return result
            except json.JSONDecodeError:
                # Try simple comma-separated parsing
                if content.startswith('[') and content.endswith(']'):
                    content = content.strip('[]')
                items = [item.strip().strip('"\'') for item in content.split(',')]
                return items
        return None
    
    def _extract_content(self, message: Any) -> Optional[str]:
        """Extract content from message."""
        if isinstance(message, BaseMessage):
            return message.content
        elif hasattr(message, 'content'):
            return message.content
        elif isinstance(message, str):
            return message
        return None


class SmartCallableOutputParser(CallableNodeConfig):
    """CallableNodeConfig specialized for output parsing with smart routing."""
    
    parsing_functions: dict[str, Callable] = Field(
        default_factory=dict,
        description="Content type to parsing function mapping"
    )
    
    detection_function: Optional[Callable] = Field(
        default=None,
        description="Function to detect content type for routing"
    )
    
    def __call__(self, state, config=None):
        """Execute with smart content detection and routing."""
        if self.detection_function:
            # Use detection function to determine parsing strategy
            content_type = self.detection_function(state)
            
            if content_type in self.parsing_functions:
                # Override the callable function based on detection
                original_func = self.callable_func
                self.callable_func = self.parsing_functions[content_type]
                
                try:
                    result = super().__call__(state, config)
                    return result
                finally:
                    # Restore original function
                    self.callable_func = original_func
        
        # Fall back to normal execution
        return super().__call__(state, config)


# Factory functions for easy creation

def create_smart_engine_node(
    engine,
    name: str,
    input_schema: Optional[type[BaseModel]] = None,
    output_schema: Optional[type[BaseModel]] = None,
    parsing_strategies: Optional[list[str]] = None,
    **kwargs
) -> SmartGenericEngineNode:
    """Create a smart generic engine node with output parsing."""
    return SmartGenericEngineNode(
        engine=engine,
        name=name,
        input_schema=input_schema,
        output_schema=output_schema,
        parsing_strategies=parsing_strategies or ["tool_calls", "json", "pydantic"],
        **kwargs
    )


def create_smart_parsing_callable(
    parsing_functions: dict[str, Callable],
    detection_function: Callable,
    name: str = "smart_parser",
    **kwargs
) -> SmartCallableOutputParser:
    """Create a smart callable parser with content detection."""
    return SmartCallableOutputParser(
        name=name,
        callable_func=lambda x: None,  # Placeholder, will be overridden
        parsing_functions=parsing_functions,
        detection_function=detection_function,
        **kwargs
    )


# Example usage patterns

def detect_content_type(state) -> str:
    """Example content type detection function."""
    messages = getattr(state, 'messages', [])
    if messages:
        last_message = messages[-1]
        content = getattr(last_message, 'content', '')
        
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            return "structured"
        elif content.strip().startswith('{'):
            return "json"
        elif content.strip().startswith('['):
            return "list"
        else:
            return "text"
    return "empty"


def parse_json_content(state) -> dict:
    """Example JSON parsing function."""
    import json
    
    messages = getattr(state, 'messages', [])
    if messages:
        content = getattr(messages[-1], 'content', '')
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {}
    return {}


def parse_structured_content(state) -> dict:
    """Example structured content parsing function."""
    messages = getattr(state, 'messages', [])
    if messages:
        last_message = messages[-1]
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            return {
                'tool_calls': [
                    {
                        'name': tc.get('name'),
                        'args': tc.get('args')
                    }
                    for tc in last_message.tool_calls
                ]
            }
    return {}