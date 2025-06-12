# src/haive/agents/conversation/base/agent.py
"""
Base conversation agent providing core multi-agent conversation functionality.

This base class handles the orchestration of conversations between multiple agents,
with support for different conversation modes and patterns.
"""


from abc import abstractmethod
from typing import Any, Dict, List, Literal, Optional, Tuple, Union

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.graph.state_graph.base_graph2 import BaseGraph
from haive.core.logging.rich_logger import LogLevel, get_logger
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langgraph.graph import END, START
from langgraph.types import Command
from pydantic import Field, PrivateAttr

from haive.agents.base.agent import Agent
from haive.agents.conversation.base.state import ConversationState
from haive.agents.simple.agent import SimpleAgent

logger = get_logger(__name__)
logger.set_level(LogLevel.WARNING)


class BaseConversationAgent(Agent):
    """
    Base conversation agent that orchestrates multi-agent conversations.

    This abstract base class provides the core functionality for managing
    conversations between multiple agents, with hooks for customization.
    """

    # Agents participating in the conversation
    participant_agents: Dict[str, Union[SimpleAgent, AugLLMConfig]] = Field(
        default_factory=dict, description="Agent instances or configs by name"
    )

    # Compiled agents cache
    _compiled_agents: Dict[str, SimpleAgent] = PrivateAttr(default_factory=dict)

    # Configuration
    topic: str = Field(default="General discussion")
    max_rounds: int = Field(default=10)
    mode: str = Field(default="round_robin", description="Conversation mode")

    # Error handling
    recursion_limit: int = Field(default=50, description="Maximum recursion depth")
    handle_errors: bool = Field(
        default=True, description="Whether to handle errors gracefully"
    )

    def setup_agent(self):
        """Set up the conversation orchestrator."""
        # Set the state schema
        self.state_schema = self.get_conversation_state_schema()
        self.set_schema = False

        # Ensure we have a default engine for orchestration
        if not self.engine and not self.engines:
            self.engine = self._create_orchestrator_engine()
            self.engines["orchestrator"] = self.engine

        # Compile participant agents
        self._compile_participants()

        super().setup_agent()

    def get_conversation_state_schema(self) -> type:
        """
        Get the state schema for this conversation type.

        Override in subclasses to provide custom state schemas.
        """
        return ConversationState

    def _create_orchestrator_engine(self) -> AugLLMConfig:
        """Create the default orchestrator engine."""
        return AugLLMConfig(
            name="conversation_orchestrator",
            system_message=f"You are orchestrating a {self.mode} conversation about: {self.topic}",
        )

    def _compile_participants(self):
        """Compile all participant agents."""
        for name, agent_or_config in self.participant_agents.items():
            if isinstance(agent_or_config, AugLLMConfig):
                # Create SimpleAgent from config
                agent = SimpleAgent(name=f"{name}_agent", engine=agent_or_config)
            else:
                agent = agent_or_config

            # Compile the agent
            if not hasattr(agent, "_compiled_graph") or not agent._compiled_graph:
                agent.compile()

            self._compiled_agents[name] = agent

    def build_graph(self) -> BaseGraph:
        """Build the conversation graph."""
        graph = BaseGraph(
            name=f"{self.name}_conversation",
            state_schema=self.get_conversation_state_schema(),
        )

        # Core nodes
        graph.add_node("initialize", self.initialize_conversation)
        graph.add_node("select_speaker", self.select_speaker)
        graph.add_node("execute_agent", self.execute_agent)
        graph.add_node("process_response", self.process_response)
        graph.add_node("check_end", self.check_end)

        # Core flow
        graph.add_edge(START, "initialize")
        graph.add_edge("initialize", "select_speaker")
        graph.add_edge("execute_agent", "process_response")
        graph.add_edge("process_response", "check_end")

        # Conditional routing
        graph.add_conditional_edges(
            "select_speaker",
            self._should_continue_conversation,
            {True: "execute_agent", False: END},
        )

        graph.add_conditional_edges(
            "check_end",
            lambda x: not x.get("conversation_ended", False),  # type: ignore
            {True: "select_speaker", False: END},
        )

        # Add custom nodes and edges
        self._add_custom_graph_elements(graph)

        return graph

    def _add_custom_graph_elements(self, graph: BaseGraph):
        """
        Hook for subclasses to add custom nodes and edges.

        Override this method to extend the graph structure.
        """
        pass

    def initialize_conversation(self, state: Any) -> Dict[str, Any]:
        """Initialize the conversation."""
        # Get speaker names
        speaker_names = list(self._compiled_agents.keys())

        # Create initial message
        initial_message = self._create_initial_message()

        # Base initialization
        update = {
            "messages": [initial_message],
            "speakers": speaker_names,
            "topic": self.topic,
            "max_rounds": self.max_rounds,
            "round_number": 0,
            "mode": self.mode,
        }

        # Add custom initialization
        custom_init = self._custom_initialization(state)
        update.update(custom_init)

        return update

    @abstractmethod
    def select_speaker(self, state: Any) -> Dict[str, Any]:
        """
        Select the next speaker.

        Must be implemented by subclasses to define speaker selection logic.
        """
        raise NotImplementedError("Subclasses must implement select_speaker")

    def execute_agent(self, state: Any) -> Dict[str, Any]:
        """Execute the current speaker's agent."""
        current_speaker = state.current_speaker

        if not current_speaker or current_speaker not in self._compiled_agents:
            return {"conversation_ended": True}

        agent = self._compiled_agents[current_speaker]

        # Prepare input for agent
        agent_input = self._prepare_agent_input(state, current_speaker)

        try:
            # Execute agent with recursion limit
            config = {"recursion_limit": self.recursion_limit}
            result = agent.invoke(agent_input, config)

            # Extract new messages
            new_messages = self._extract_agent_messages(
                result, agent_input.get("messages", [])
            )

            # Add speaker name to messages
            for msg in new_messages:
                if isinstance(msg, AIMessage):
                    msg.name = current_speaker

            return {"messages": new_messages}

        except Exception as e:
            if self.handle_errors:
                return self._handle_agent_error(e, current_speaker)
            else:
                raise

    def process_response(self, state: Any) -> Dict[str, Any]:
        """
        Process the agent's response.

        Override in subclasses to add custom response processing.
        """
        return {}

    def check_end(self, state: Any) -> Dict[str, Any]:
        """Check if conversation should end."""
        # Check round limit
        if state.round_number >= state.max_rounds:
            return self._create_conclusion(state, "max_rounds")

        # Check custom end conditions
        custom_end = self._check_custom_end_conditions(state)
        if custom_end:
            return custom_end

        return {}

    # Helper methods

    def _should_continue_conversation(self, state: Any) -> bool:
        """Check if conversation should continue."""
        return state.current_speaker is not None and not state.conversation_ended

    def _create_initial_message(self) -> BaseMessage:
        """Create the initial conversation message."""
        return HumanMessage(
            content=f"Topic: {self.topic}\nLet's begin our {self.mode} discussion."
        )

    def _custom_initialization(self, state: Any) -> Dict[str, Any]:
        """Hook for custom initialization. Override in subclasses."""
        return {}

    def _prepare_agent_input(self, state: Any, agent_name: str) -> Dict[str, Any]:
        """Prepare input for an agent. Override for custom behavior."""
        return {"messages": state.messages}

    def _extract_agent_messages(
        self, result: Any, input_messages: List[BaseMessage]
    ) -> List[BaseMessage]:
        """Extract new messages from agent result."""
        new_messages = []

        if isinstance(result, dict) and "messages" in result:
            result_messages = result.get("messages", [])
            # Get only new messages (after what we sent)
            if len(result_messages) > len(input_messages):
                new_messages = result_messages[len(input_messages) :]

        return new_messages

    def _handle_agent_error(self, error: Exception, agent_name: str) -> Dict[str, Any]:
        """Handle errors from agent execution."""
        logger.error(f"Error executing agent {agent_name}: {error}")
        error_msg = AIMessage(
            content=f"[Error from {agent_name}]: {str(error)}", name=agent_name
        )
        return {"messages": [error_msg]}

    def _check_custom_end_conditions(self, state: Any) -> Optional[Dict[str, Any]]:
        """Check custom end conditions. Override in subclasses."""
        return None

    def _create_conclusion(self, state: Any, reason: str) -> Dict[str, Any]:
        """Create conclusion message."""
        conclusion_msg = SystemMessage(
            content=f"Conversation ended: {reason}. Total rounds: {state.round_number}"
        )
        return {"messages": [conclusion_msg], "conversation_ended": True}

    def get_input_fields(self) -> Dict[str, Tuple[type, Any]]:
        """Define input fields."""
        return {"messages": (List[BaseMessage], []), "topic": (str, None)}

    def get_output_fields(self) -> Dict[str, Tuple[type, Any]]:
        """Define output fields."""
        return {
            "messages": (List[BaseMessage], []),
            "round_number": (int, 0),
            "conversation_ended": (bool, False),
        }

    # Factory method for easy creation
    @classmethod
    def create(
        cls, participants: Dict[str, Union[SimpleAgent, AugLLMConfig]], **kwargs
    ):
        """Create a conversation with participants."""
        return cls(participant_agents=participants, **kwargs)
