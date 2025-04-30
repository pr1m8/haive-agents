from agents.simple.state import SimpleAgentState
from typing import List

class ReflexionState(SimpleAgentState):
    """State for the Reflexion agent."""
    #messages: List[BaseMessage] = []
    reflections_count: int = 0
    answer: str = ""
    