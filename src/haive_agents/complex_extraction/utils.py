from typing import TypedDict, Optional, Union, Callable, Sequence
from typing import Sequence,Dict,Union,List
from langchain_core.runnables import Runnable
from langchain_core.messages import AIMessage, AnyMessage, BaseMessage
from langchain_core.messages import ToolCall
import jsonpatch
from haive_agents.complex_extraction.models import PatchFunctionParameters
from pydantic import BaseModel
from typing import Type
import uuid
from langgraph.graph import add_messages
from langchain_core.prompt_values import PromptValue
from langgraph.types import Command

def encode(state: BaseModel) -> dict:
    """Ensure the input is the correct format."""
    if isinstance(state.messages, PromptValue):
        return Command(update={"messages": state.messages.to_messages(), "input_format": "list"})
    if isinstance(state.messages, list):
        return Command(update={"messages": state.messages, "input_format": "list"}) 
    raise ValueError(f"Unexpected input type: {type(state.messages)}")

def decode(state:BaseModel) -> AIMessage:
    """Ensure the output is in the expected format."""
    return Command(update={"extracted_data": state.messages[-1]})

def default_aggregator(messages: Sequence[AnyMessage]) -> AIMessage:
    """
    Aggregates a sequence of messages into a single AI message.
    """
    for m in messages[::-1]:
        if m.type == "ai":
            return m
    raise ValueError("No AI message found in the sequence.")

def aggregate_messages(messages: Sequence[AnyMessage],) -> AIMessage:
    # Get all the AI messages and apply json patches
    resolved_tool_calls: Dict[Union[str, None], ToolCall] = {}
    content: Union[str, List[Union[str, dict]]] = ""
    for m in messages:
        if m.type != "ai":
            continue
        if not content:
            content = m.content
        for tc in m.tool_calls:
            if tc["name"] == PatchFunctionParameters.__name__:
                tcid = tc["args"]["tool_call_id"]
                # Add logging in later. 
                if tcid not in resolved_tool_calls:
                    #logger.debug(
                    #    f"JsonPatch tool call ID {tc['args']['tool_call_id']} not found."
                    #    f"Valid tool call IDs: {list(resolved_tool_calls.keys())}"
                    #)
                    tcid = next(iter(resolved_tool_calls.keys()), None)
                orig_tool_call = resolved_tool_calls[tcid]
                current_args = orig_tool_call["args"]
                patches = tc["args"].get("patches") or []
                orig_tool_call["args"] = jsonpatch.apply_patch(
                    current_args,
                    patches,
                )
                orig_tool_call["id"] = tc["id"]
            else:
                resolved_tool_calls[tc["id"]] = tc.copy()
    return AIMessage(
        content=content,
        tool_calls=list(resolved_tool_calls.values()),
    )
def add_or_overwrite_messages(left: list, right: Union[list, dict]) -> list:
            """Append or replace messages depending on format."""
            if isinstance(right, dict) and "finalize" in right:
                finalized = right["finalize"]
                if not isinstance(finalized, list):
                    finalized = [finalized]
                for m in finalized:
                    if m.id is None:
                        m.id = str(uuid.uuid4())
                return finalized
            res = add_messages(left, right)
            if not isinstance(res, list):
                return [res]
            return res
def dedict(x:BaseModel) -> list:
        """Get the messages from the state."""
        return x.messages

class RetryStrategy(TypedDict, total=False):
    """The retry strategy for a tool call."""

    max_attempts: int
    """The maximum number of attempts to make."""
    fallback: Optional[
        Union[
            Runnable[Sequence[AnyMessage], AIMessage],
            Runnable[Sequence[AnyMessage], BaseMessage],
            Callable[[Sequence[AnyMessage]], AIMessage],
        ]
    ]
    """The function to use once validation fails."""
    aggregate_messages: Optional[Callable[[Sequence[AnyMessage]], AIMessage]] = default_aggregator