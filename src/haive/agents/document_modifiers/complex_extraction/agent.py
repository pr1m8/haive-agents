import operator
import uuid
import logging
import functools
from typing import Any, Dict, List, Optional, Type, Union, Callable, Sequence, Literal

from pydantic import BaseModel, Field
from langchain_core.messages import (
    AIMessage, AnyMessage, BaseMessage, HumanMessage, ToolCall, ToolMessage
)
from langchain_core.prompt_values import PromptValue
from langchain_core.runnables import Runnable, RunnableLambda
from langchain_core.language_models import BaseChatModel
from langchain_core.tools import BaseTool, Tool

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ValidationNode
from langgraph.types import Command

from haive.core.engine.agent.agent import Agent, AgentConfig, register_agent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.agents.document_modifiers.complex_extraction.state import ComplexExtractionState
from haive.core.models.llm.base import AzureLLMConfig
from haive.agents.document_modifiers.complex_extraction.utils import default_aggregator,encode,decode
from haive.agents.document_modifiers.complex_extraction.models import RetryStrategy,PatchFunctionParameters
from haive.agents.document_modifiers.complex_extraction.config import ComplexExtractionAgentConfig
# Set up logging
logger = logging.getLogger(__name__)

from typing import TypedDict
#fr
# Type for RetryStrategy




@register_agent(ComplexExtractionAgentConfig)
class ComplexExtractionAgent(Agent[ComplexExtractionAgentConfig]):
    """
    Agent that extracts complex structured information from text.
    
    This agent uses validation with retries and optional JSONPatch-based error correction
    to reliably extract structured data according to a specified schema.
    """
    
    def __init__(self, config: ComplexExtractionAgentConfig=ComplexExtractionAgentConfig()):
        """Initialize the complex extraction agent."""
        self.extraction_model = config.extraction_model
        self.max_retries = config.max_retries
        self.force_tool_choice = config.force_tool_choice
        self.use_jsonpatch = config.use_jsonpatch
        self.extraction_tool = None
        self.extraction_runnable = None
        self.llm = config.llm_config.instantiate()
        
        # Try importing jsonpatch if needed
        if self.use_jsonpatch:
            try:
                import jsonpatch
                self.jsonpatch = jsonpatch
            except ImportError:
                logger.warning("jsonpatch library not installed - falling back to regular validation")
                self.use_jsonpatch = False
                self.jsonpatch = None
        
        # Set up extraction tool if model is provided
        if self.extraction_model:
            self._setup_extraction_tool()
            
        # Call parent init
        super().__init__(config)
        #self.app = encode | self.app | decode
    
    def _setup_extraction_tool(self):
        """Set up the extraction tool based on the provided model."""
        if not self.extraction_model:
            logger.warning("No extraction model provided")
            return
            
        # Create a tool from the extraction model
        extract_name = f"extract_{self.extraction_model.__name__}"
        
        def extract_func(text: str) -> Dict[str, Any]:
            """Extract structured data according to the schema."""
            # This is just a placeholder implementation
            # The actual extraction is performed by the LLM
            return {}
        
        # Create and configure the tool
        extract_data = Tool.from_function(
            func=extract_func,
            name=extract_name,
            description=f"Extract {self.extraction_model.__name__} data from text",
            args_schema=self.extraction_model
        )
        
        # Store the tool
        self.extraction_tool = extract_data
        logger.info(f"Created extraction tool: {extract_name}")
    
    def _bind_validator_with_retries(
        self,
        llm: Union[
            Runnable[Sequence[AnyMessage], AIMessage],
            Runnable[Sequence[BaseMessage], BaseMessage],
        ],
        *,
        validator: ValidationNode,
        retry_strategy: RetryStrategy,
        tool_choice: Optional[str] = None,
    ) -> StateGraph:
        """
        Bind a tool validator with retry logic and return the graph builder.
        
        Args:
            llm: The LLM to generate responses
            validator: Validation node for checking tool call validity
            retry_strategy: Strategy for handling retries
            tool_choice: Optional tool name to force
            
        Returns:
            StateGraph builder (not compiled)
        """
        # Define message merging function
        
        
        # Create the state graph
        builder = StateGraph(self.state_schema)

        # Function to extract messages from state
        def dedict(x: Any) -> list:
            """Extract messages from state."""
            if isinstance(x, dict) and "messages" in x:
                return x["messages"]
            elif hasattr(x, "messages"):
                return x.messages
            else:
                raise ValueError(f"Cannot extract messages from {type(x)}")

        # Define model and fallback nodes
        model = dedict | llm | (lambda msg: {"messages": [msg], "attempt_number": 1})
        
        # Get fallback runnable
        fbrunnable = retry_strategy.get("fallback")
        if fbrunnable is None:
            fb_runnable = llm
        elif isinstance(fbrunnable, Runnable):
            fb_runnable = fbrunnable
        else:
            fb_runnable = RunnableLambda(fbrunnable)
            
        fallback = dedict | fb_runnable | (lambda msg: {"messages": [msg], "attempt_number": 1})

        # Function to count initial messages
        def count_messages(state: Any) -> Dict[str, Any]:
            """Count initial messages in state."""
            if isinstance(state, dict):
                return {"initial_num_messages": len(state.get("messages", []))}
            else:
                return {"initial_num_messages": len(getattr(state, "messages", []))}

        # Add nodes to the graph
        builder.add_node("count_messages", count_messages)
        builder.add_node("llm", model)
        builder.add_node("fallback", fallback)

        # Set up message selection and validation
        select_messages = retry_strategy.get("aggregate_messages") or default_aggregator

        def select_generated_messages(state: Any) -> list:
            """Select only messages generated in this run."""
            if isinstance(state, dict):
                selected = state["messages"][state["initial_num_messages"]:]
            else:
                selected = state.messages[state.initial_num_messages:]
            return [select_messages(selected)]

        def endict_validator_output(x: Sequence[AnyMessage]) -> Dict[str, Any]:
            """Format validator output for the graph."""
            if tool_choice and not x:
                return {
                    "messages": [
                        HumanMessage(
                            content=f"ValidationError: please respond with a valid tool call [tool_choice={tool_choice}].",
                            additional_kwargs={"is_error": True},
                        )
                    ]
                }
            return {"messages": x}

        # Create validator node
        validator_runnable = select_generated_messages | validator | endict_validator_output
        builder.add_node("validator", validator_runnable)

        # Define finalizer class
        class Finalizer:
            """Select final message to return."""
            def __init__(self, aggregator: Optional[Callable[[list], AIMessage]] = None):
                self._aggregator = aggregator or default_aggregator

            def __call__(self, state: Any) -> dict:
                """Return the aggregated message."""
                if isinstance(state, dict):
                    initial_num_messages = state["initial_num_messages"]
                    generated_messages = state["messages"][initial_num_messages:]
                else:
                    initial_num_messages = state.initial_num_messages
                    generated_messages = state.messages[initial_num_messages:]
                    
                return Command(update={
                    "messages": {
                        "finalize": self._aggregator(generated_messages),
                    }
                })

        # Add finalizer node
        builder.add_node("finalizer", Finalizer(retry_strategy.get("aggregate_messages")))
        builder.add_node('encode', encode)
        builder.add_node('decode', decode)
        # Define graph connectivity
        builder.add_edge(START, "encode")
        builder.add_edge("encode", "count_messages")
        builder.add_edge("count_messages", "llm")
        #builder.add_edge("llm", "decode")
        #builder.add_edge("decode", "finalizer")
        builder.add_edge("finalizer", 'decode')
        builder.add_edge('decode', END)


        # Define routing functions
        def route_validator(state: Any):
            """Decide whether to run validation."""
            messages = state["messages"] if isinstance(state, dict) else state.messages
            if not messages:
                return END
                
            last_msg = messages[-1]
            has_tool_calls = (hasattr(last_msg, "tool_calls") and last_msg.tool_calls) or \
                             (isinstance(last_msg, dict) and last_msg.get("tool_calls"))
                
            if has_tool_calls or tool_choice is not None:
                return "validator"
            return END

        def route_validation(state: Any):
            """Route based on validation result."""
            max_attempts = retry_strategy.get("max_attempts", 3)
            attempt_num = state["attempt_number"] if isinstance(state, dict) else state.attempt_number
            
            if attempt_num > max_attempts:
                raise ValueError(f"Could not extract a valid value in {max_attempts} attempts.")
                
            messages = state["messages"] if isinstance(state, dict) else state.messages
            for m in messages[::-1]:
                if m.type == "ai":
                    break
                if hasattr(m, "additional_kwargs") and m.additional_kwargs.get("is_error"):
                    return "fallback"
            return "finalizer"

        # Add conditional edges
        builder.add_conditional_edges("llm", route_validator, ["validator", END])
        builder.add_edge("fallback", "validator")
        builder.add_conditional_edges(
            "validator", route_validation, ["finalizer", "fallback"]
        )
        #builder.add_edge("finalizer", END)

        # Return the builder (not compiled)
        return builder
    
    def bind_validator_with_jsonpatch_retries(
        self,
        llm: BaseChatModel,
        *,
        tools: list,
        tool_choice: Optional[str] = None,
        max_attempts: int = 3,
    ) -> StateGraph:
        """
        Bind a validator with JSONPatch-based retries, returning the StateGraph builder.
        
        Args:
            llm: The LLM to use
            tools: List of tools to validate
            tool_choice: Optional tool to force
            max_attempts: Maximum retry attempts
            
        Returns:
            StateGraph builder (not compiled)
        """
        # Ensure jsonpatch is available
        if not self.jsonpatch:
            raise ImportError(
                "The 'jsonpatch' library is required for JSONPatch-based retries."
            )

        # Create bound LLMs
        bound_llm = llm.bind_tools(tools, tool_choice=tool_choice)
        fallback_llm = llm.bind_tools([PatchFunctionParameters])

        # Define message aggregation function
        def aggregate_messages(messages: Sequence[AnyMessage]) -> AIMessage:
            """Aggregate messages with JSONPatch corrections."""
            # Get all the AI messages and apply json patches
            resolved_tool_calls = {}
            content = ""
            
            for m in messages:
                if m.type != "ai":
                    continue
                    
                if not content:
                    content = m.content
                    
                if not hasattr(m, "tool_calls"):
                    continue
                    
                for tc in m.tool_calls:
                    if tc.get("name") == PatchFunctionParameters.__name__:
                        # Get target tool call ID
                        tcid = tc.get("args", {}).get("tool_call_id")
                        if tcid not in resolved_tool_calls:
                            logger.debug(
                                f"JsonPatch tool call ID {tcid} not found. "
                                f"Valid tool call IDs: {list(resolved_tool_calls.keys())}"
                            )
                            # Fallback to first available tool call
                            tcid = next(iter(resolved_tool_calls.keys()), None)
                            if not tcid:
                                continue
                                
                        # Get original tool call and apply patches
                        orig_tool_call = resolved_tool_calls[tcid]
                        current_args = orig_tool_call.get("args", {})
                        patches = tc.get("args", {}).get("patches", [])
                        
                        try:
                            # Apply JSON patches
                            orig_tool_call["args"] = self.jsonpatch.apply_patch(
                                current_args,
                                patches,
                            )
                            # Update ID to latest
                            orig_tool_call["id"] = tc["id"]
                        except Exception as e:
                            logger.error(f"Error applying JSONPatch: {e}")
                    else:
                        # Regular tool call - add to resolved list
                        resolved_tool_calls[tc["id"]] = tc.copy()
            
            # Create final AI message with resolved tool calls
            return AIMessage(
                content=content,
                tool_calls=list(resolved_tool_calls.values()),
            )

        # Create format error function
        def format_exception(error: BaseException, call: Dict[str, Any], schema: Type[BaseModel]):
            """Format validation error for JSONPatch correction."""
            schema_json = schema.schema_json() if hasattr(schema, "schema_json") else str(schema)
            return (
                f"Error:\n\n```\n{repr(error)}\n```\n"
                "Expected Parameter Schema:\n\n" + f"```json\n{schema_json}\n```\n"
                f"Please respond with a JSONPatch to correct the error for tool_call_id=[{call.get('id', 'unknown')}]."
            )

        # Create validator and retry strategy
        validator = ValidationNode(
            tools + [PatchFunctionParameters],
            format_error=format_exception,
        )
        
        retry_strategy = RetryStrategy(
            max_attempts=max_attempts,
            fallback=fallback_llm,
            aggregate_messages=aggregate_messages,
        )
        
        # Return the graph builder
        return self._bind_validator_with_retries(
            bound_llm,
            validator=validator,
            retry_strategy=retry_strategy,
            tool_choice=tool_choice)
    
    def bind_validator_with_retries(
        self,
        llm: BaseChatModel,
        *,
        tools: list,
        tool_choice: Optional[str] = None,
        max_attempts: int = 3,
    ) -> StateGraph:
        """
        Bind a validator with standard retries (no JSONPatch), returning StateGraph builder.
        
        Args:
            llm: The LLM to use
            tools: List of tools to validate
            tool_choice: Optional tool to force
            max_attempts: Maximum retry attempts
            
        Returns:
            StateGraph builder (not compiled)
        """
        bound_llm = llm.bind_tools(tools, tool_choice=tool_choice)
        retry_strategy = RetryStrategy(max_attempts=max_attempts)
        validator = ValidationNode(tools)
        
        # Return the graph builder without compiling
        return self._bind_validator_with_retries(
            bound_llm,
            validator=validator,
            tool_choice=tool_choice,
            retry_strategy=retry_strategy,
        )
    
    def setup_workflow(self) -> None:
        """Set up the agent workflow."""
        logger.info(f"Setting up workflow for ComplexExtractionAgent {self.config.name}")
        
        self.graph = self.bind_validator_with_jsonpatch_retries(self.llm, tools=[self.extraction_tool])
        #self.app = deddict
        # Note: We don't compile the graph here - that's done by the parent in compile()
    
    def extract_node(self, state: Any) -> Dict[str, Any]:
        """
        Main extraction node function.
        
        Args:
            state: Current state
            
        Returns:
            Updated state
        """
        # Check if we have the extraction runnable
        if hasattr(self, 'extraction_runnable') and self.extraction_runnable:
            try:
                # Get messages from state
                if isinstance(state, dict) and 'messages' in state:
                    messages = state['messages']
                elif hasattr(state, 'messages'):
                    messages = state.messages
                else:
                    # No messages found
                    return {"error": "No messages found in state"}
                
                if not messages:
                    # No messages to process
                    return state
                
                # Invoke the extraction runnable
                result = self.extraction_runnable.invoke(messages)
                
                # Extract data from the result
                extracted_data = None
                if hasattr(result, 'tool_calls') and result.tool_calls:
                    for tool_call in result.tool_calls:
                        if tool_call.get('name') == self.extraction_tool.name:
                            extracted_data = tool_call.get('args', {})
                            break
                
                # Return updated state
                updates = {
                    'extracted_data': extracted_data
                }
                
                # Add result message if it's not already in messages
                if hasattr(result, 'content') or hasattr(result, 'tool_calls'):
                    if isinstance(state, dict):
                        updated_messages = list(state.get('messages', []))
                        updated_messages.append(result)
                        updates['messages'] = updated_messages
                    else:
                        updates['messages'] = list(state.messages) + [result]
                
                return updates
            except Exception as e:
                # Log error and return error in state
                logger.error(f"Error in extraction node: {str(e)}")
                return {"error": str(e)}
        
        # If we don't have the extraction runnable, just pass through
        return state
    
    def run(self, input_data: Union[str, List[str], Dict[str, Any], BaseModel], **kwargs) -> Dict[str, Any]:
        """
        Run the extraction agent on input data.
        
        Args:
            input_data: Input text or data to extract information from
            **kwargs: Additional runtime configuration
            
        Returns:
            Dictionary with extracted data and execution results
        """
        # Ensure we have a validation workflow
        if hasattr(self, 'extraction_model') and self.extraction_model and not hasattr(self, 'extraction_runnable'):
            self.setup_workflow()
            
        # Convert input data to messages
        if isinstance(input_data, str) or (isinstance(input_data, list) and all(isinstance(i, str) for i in input_data)):
            #messages = self._prepare_extraction_messages(input_data)
            
            # Create state with messages
            #input_state = {
            ##    "messages": messages
            #}
            
            # Run the graph with the input state
            result = super().run(input_data, **kwargs)
        else:
            # Use parent run method for complex inputs
            result = super().run(input_data, **kwargs)
        
        # Try to extract data from messages if not already in result
        if 'extracted_data' not in result or not result.get('extracted_data'):
            extracted_data = None
            if 'messages' in result:
                for message in reversed(result['messages']):
                    if hasattr(message, 'tool_calls') and message.tool_calls:
                        for tool_call in message.tool_calls:
                            if hasattr(self, 'extraction_tool') and tool_call.get('name') == self.extraction_tool.name:
                                extracted_data = tool_call.get('args', {})
                                break
                if extracted_data:
                    result['extracted_data'] = extracted_data
        
        return result
    #def compile(self):
        #self.app = dec
    def _prepare_extraction_messages(self, input_data: Union[str, List[str], Dict[str, Any], BaseModel]) -> List[BaseMessage]:
        """
        Prepare messages for extraction.
        
        Args:
            input_data: Input data in various formats
            
        Returns:
            List of messages ready for extraction
        """
        # Handle string input
        if isinstance(input_data, str):
            return [HumanMessage(content=f"Extract {self.extraction_model.__name__} from the following text:\n\n{input_data}")]
            
        # Handle list of strings
        elif isinstance(input_data, list) and all(isinstance(item, str) for item in input_data):
            combined = "\n".join(input_data)
            return [HumanMessage(content=f"Extract {self.extraction_model.__name__} from the following text:\n\n{combined}")]
            
        # Handle BaseMessage
        elif isinstance(input_data, BaseMessage):
            return [input_data]
            
        # Handle list of BaseMessages
        elif isinstance(input_data, list) and all(isinstance(item, BaseMessage) for item in input_data):
            return input_data
            
        # Handle dict
        elif isinstance(input_data, dict):
            # Check if messages field is present
            if 'messages' in input_data:
                messages = input_data['messages']
                if isinstance(messages, list):
                    return messages
                
            # Check for text or content fields
            content = input_data.get('text') or input_data.get('content')
            if content:
                return [HumanMessage(content=f"Extract {self.extraction_model.__name__} from the following text:\n\n{content}")]
                
        # Handle BaseModel
        elif isinstance(input_data, BaseModel):
            # Try to convert to dict
            if hasattr(input_data, "model_dump"):
                model_dict = input_data.model_dump()
            elif hasattr(input_data, "dict"):
                model_dict = input_data.dict()
            else:
                model_dict = {attr: getattr(input_data, attr) for attr in input_data.__annotations__}
                
            # Check for text content
            content = model_dict.get('text') or model_dict.get('content')
            if content:
                return [HumanMessage(content=f"Extract {self.extraction_model.__name__} from the following text:\n\n{content}")]
        
        # Default case - convert to string
        return [HumanMessage(content=f"Extract {self.extraction_model.__name__} from the following:\n\n{str(input_data)}")]

