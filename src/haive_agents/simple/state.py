from pydantic import BaseModel, Field
from typing import Annotated, Sequence, List, Optional, Dict, Any
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import add_messages
from haive_core.schema.state_schema import StateSchema

class SimpleAgentState(StateSchema):
    """
    Base state for simple agents.
    
    This provides a standard chat-based state with a messages field that
    supports proper message history management through the add_messages reducer.
    """
    messages: Annotated[Sequence[BaseMessage], add_messages] = Field(
        default_factory=list,
        description="Chat message history"
    )
   
    
  
    
    def add_human_message(self, content: str) -> 'SimpleAgentState':
        """
        Add a human message to the state.
        
        Args:
            content: Message content
            
        Returns:
            Self for chaining
        """
        if not hasattr(self, "messages"):
            self.messages = []
        
        message = HumanMessage(content=content)
        self.messages = add_messages(self.messages, [message])
        return self
    
    def add_ai_message(self, content: str) -> 'SimpleAgentState':
        """
        Add an AI message to the state.
        
        Args:
            content: Message content
            
        Returns:
            Self for chaining
        """
        if not hasattr(self, "messages"):
            self.messages = []
        
        message = AIMessage(content=content)
        self.messages = add_messages(self.messages, [message])
        return self
    
    def extract_last_message_content(self) -> Optional[str]:
        """
        Extract the content of the last message in the state.
        
        Returns:
            Content of the last message or None if no messages
        """
        if not hasattr(self, "messages") or not self.messages:
            return None
        
        last_message = self.messages[-1]
        return last_message.content if hasattr(last_message, "content") else None
        
    @classmethod
    def with_messages(cls, messages: List[BaseMessage]) -> 'SimpleAgentState':
        """
        Create a new instance with the given messages.
        
        Args:
            messages: Initial messages
            
        Returns:
            New SimpleAgentState instance
        """
        return cls(messages=messages) 