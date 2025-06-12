"""
Structured debate conversation with positions and formal argumentation.
"""

import logging
from typing import Any, Dict, List, Literal, Optional, Set, Tuple

from haive.core.logging.rich_logger import LogLevel, get_logger
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from pydantic import Field, model_validator

from haive.agents.conversation.base.agent import BaseConversationAgent
from haive.agents.conversation.debate.state import DebateState

logger = get_logger(__name__)
logger.set_level(LogLevel.WARNING)


class DebateConversation(BaseConversationAgent):
    """
    Structured debate conversation with positions and formal argumentation.

    Features:
    - Opening statements
    - Argument and rebuttal phases
    - Closing statements
    - Optional scoring/judging
    """

    mode: Literal["debate"] = Field(default="debate")

    # Debate configuration
    debate_positions: Dict[str, str] = Field(
        default_factory=dict,
        description="Mapping of participant names to their positions",
    )

    # Debate structure
    enable_opening_statements: bool = Field(default=True)
    enable_closing_statements: bool = Field(default=True)
    arguments_per_side: int = Field(default=3)
    enable_judge: bool = Field(default=False)
    judge_name: str = Field(default="Judge")

    # Debate rules
    enforce_position_consistency: bool = Field(
        default=True,
        description="Ensure participants argue for their assigned positions",
    )
    require_evidence: bool = Field(
        default=False, description="Require participants to cite evidence"
    )
    time_limit_per_turn: Optional[int] = Field(
        default=None, description="Word limit per turn (if set)"
    )

    @model_validator(mode="after")
    def validate_positions(self):
        """Ensure all participants have positions."""
        if self.participant_agents and self.debate_positions:
            for participant in self.participant_agents:
                if (
                    participant not in self.debate_positions
                    and participant != self.judge_name
                ):
                    logger.warning(f"No position assigned to {participant}")
        return self

    def get_conversation_state_schema(self) -> type:
        """Use debate state schema."""
        return DebateState

    def _custom_initialization(self, state: DebateState) -> Dict[str, Any]:
        """Initialize debate-specific state."""
        return {
            "debate_positions": self.debate_positions,
            "arguments_made": {name: [] for name in self.debate_positions},
            "opening_statements_complete": not self.enable_opening_statements,
            "closing_statements_complete": False,
            "in_rebuttal_phase": False,
        }

    def _create_initial_message(self) -> BaseMessage:
        """Create debate introduction."""
        positions_str = "\n".join(
            [
                f"- {name}: {position}"
                for name, position in self.debate_positions.items()
            ]
        )

        structure = []
        if self.enable_opening_statements:
            structure.append("1. Opening statements")
        structure.append(
            f"2. Arguments and rebuttals ({self.arguments_per_side} per side)"
        )
        if self.enable_closing_statements:
            structure.append("3. Closing statements")

        structure_str = "\n".join(structure)

        return HumanMessage(
            content=f"""Welcome to the debate!

Topic: {self.topic}

Positions:
{positions_str}

Debate Structure:
{structure_str}

Let's begin with opening statements."""
        )

    def select_speaker(self, state: DebateState) -> Dict[str, Any]:
        """Select speaker based on debate phase."""
        # Opening statements phase
        if not state.opening_statements_complete:
            return self._select_opening_speaker(state)

        # Closing statements phase
        if state.in_rebuttal_phase and self._all_arguments_complete(state):
            if not state.closing_statements_complete and self.enable_closing_statements:
                return self._select_closing_speaker(state)

        # Main debate phase
        return self._select_debate_speaker(state)

    def _select_opening_speaker(self, state: DebateState) -> Dict[str, Any]:
        """Select speaker for opening statements."""
        # Find who hasn't given opening statement
        messages = state.messages
        speakers_done = set()

        for msg in messages:
            if isinstance(msg, AIMessage) and hasattr(msg, "name"):
                if "opening statement" in str(msg.content).lower():
                    speakers_done.add(msg.name)

        for speaker in state.debate_positions:
            if speaker not in speakers_done:
                return {"current_speaker": speaker}

        # All done with opening statements
        transition_msg = SystemMessage(
            content="Opening statements complete. Moving to main arguments."
        )
        return {
            "current_speaker": list(state.debate_positions.keys())[0],
            "opening_statements_complete": True,
            "messages": [transition_msg],
        }

    def _select_debate_speaker(self, state: DebateState) -> Dict[str, Any]:
        """Select speaker for main debate."""
        # Alternate between different positions
        last_speaker = state.current_speaker
        if not last_speaker:
            return {"current_speaker": list(state.debate_positions.keys())[0]}

        last_position = state.debate_positions.get(last_speaker, "")

        # Find someone with a different position
        for speaker, position in state.debate_positions.items():
            if speaker != last_speaker and position != last_position:
                # Check if they've made fewer arguments
                if len(state.arguments_made.get(speaker, [])) < self.arguments_per_side:
                    return {"current_speaker": speaker}

        # Everyone has made enough arguments - move to rebuttals
        if not state.in_rebuttal_phase:
            transition_msg = SystemMessage(
                content="Main arguments complete. Moving to rebuttals."
            )
            return {
                "in_rebuttal_phase": True,
                "messages": [transition_msg],
                "current_speaker": list(state.debate_positions.keys())[0],
            }

        # In rebuttal phase - continue alternating
        return self._select_next_debater(state)

    def _select_closing_speaker(self, state: DebateState) -> Dict[str, Any]:
        """Select speaker for closing statements."""
        # Find who hasn't given closing statement
        closing_speakers = set()

        for msg in state.messages[
            -len(state.debate_positions) * 2 :
        ]:  # Check recent messages
            if isinstance(msg, AIMessage) and hasattr(msg, "name"):
                if (
                    "closing" in str(msg.content).lower()
                    or "conclusion" in str(msg.content).lower()
                ):
                    closing_speakers.add(msg.name)

        for speaker in state.debate_positions:
            if speaker not in closing_speakers:
                return {"current_speaker": speaker}

        # All done
        return {"closing_statements_complete": True, "conversation_ended": True}

    def _select_next_debater(self, state: DebateState) -> Dict[str, Any]:
        """Simple alternation between debaters."""
        speakers = list(state.debate_positions.keys())
        current_idx = (
            speakers.index(state.current_speaker)
            if state.current_speaker in speakers
            else -1
        )
        next_idx = (current_idx + 1) % len(speakers)
        return {"current_speaker": speakers[next_idx]}

    def _all_arguments_complete(self, state: DebateState) -> bool:
        """Check if all main arguments are complete."""
        for speaker in state.debate_positions:
            if len(state.arguments_made.get(speaker, [])) < self.arguments_per_side:
                return False
        return True

    def _prepare_agent_input(
        self, state: DebateState, agent_name: str
    ) -> Dict[str, Any]:
        """Prepare input with debate context."""
        base_input = super()._prepare_agent_input(state, agent_name)

        # Add debate phase context
        phase_context = self._get_phase_context(state)
        position = state.debate_positions.get(agent_name, "")

        context_msg = SystemMessage(
            content=f"""Debate Context:
Phase: {phase_context}
Your Position: {position}
Arguments Made: {len(state.arguments_made.get(agent_name, []))} of {self.arguments_per_side}

{self._get_phase_instructions(state, agent_name)}"""
        )

        messages = base_input.get("messages", [])
        # Add context at the beginning
        base_input["messages"] = [context_msg] + messages

        return base_input

    def _get_phase_context(self, state: DebateState) -> str:
        """Get current debate phase."""
        if not state.opening_statements_complete:
            return "Opening Statements"
        elif not state.in_rebuttal_phase:
            return "Main Arguments"
        elif not state.closing_statements_complete:
            return "Rebuttals and Closing"
        else:
            return "Conclusion"

    def _get_phase_instructions(self, state: DebateState, agent_name: str) -> str:
        """Get instructions for current phase."""
        if not state.opening_statements_complete:
            return "Please provide your opening statement. Introduce your position clearly."
        elif not state.in_rebuttal_phase:
            return "Present a strong argument for your position. Be specific and persuasive."
        elif not state.closing_statements_complete:
            if self._should_give_closing(state, agent_name):
                return "Provide your closing statement. Summarize your key points."
            else:
                return "Respond to opposing arguments. Point out weaknesses in their reasoning."
        return ""

    def _should_give_closing(self, state: DebateState, agent_name: str) -> bool:
        """Check if this agent should give closing statement."""
        # Simple heuristic - if we're near the end
        return state.round_number >= state.max_rounds - 1

    def process_response(self, state: DebateState) -> Dict[str, Any]:
        """Track arguments and rebuttals."""
        update = {}

        if state.current_speaker and state.messages:
            last_msg = state.messages[-1]
            if isinstance(last_msg, AIMessage) and hasattr(last_msg, "name"):
                speaker = last_msg.name
                content = last_msg.content

                # Track arguments
                if not state.in_rebuttal_phase:
                    arguments = dict(state.arguments_made)
                    if speaker not in arguments:
                        arguments[speaker] = []  # type: ignore
                    arguments[speaker].append(
                        str(content)[:100]
                    )  # Store summary  # type: ignore
                    update["arguments_made"] = arguments

                # Track rebuttals
                elif state.in_rebuttal_phase:
                    # Simple rebuttal detection
                    rebuttals = dict(state.rebuttals)
                    if speaker not in rebuttals:
                        rebuttals[speaker] = []  # type: ignore

                    # Find who they're responding to
                    for other_speaker in state.debate_positions:
                        if (
                            other_speaker != speaker
                            and other_speaker.lower() in str(content).lower()
                        ):
                            rebuttals[speaker].append((other_speaker, str(content)[:100]))  # type: ignore
                            break

                    update["rebuttals"] = rebuttals

        return update

    def _create_conclusion(self, state: DebateState, reason: str) -> Dict[str, Any]:
        """Create debate conclusion with summary."""
        # Generate debate summary
        summary_parts = [f"Debate on '{self.topic}' concluded."]

        # Summarize positions and arguments
        for speaker, position in state.debate_positions.items():
            arg_count = len(state.arguments_made.get(speaker, []))
            rebuttal_count = len(state.rebuttals.get(speaker, []))
            summary_parts.append(
                f"- {speaker} ({position}): {arg_count} arguments, {rebuttal_count} rebuttals"
            )

        conclusion_msg = SystemMessage(content="\n".join(summary_parts))

        return {"messages": [conclusion_msg], "conversation_ended": True}

    @classmethod
    def create_simple_debate(
        cls,
        topic: str,
        position_a: Tuple[str, str],  # (name, position)
        position_b: Tuple[str, str],  # (name, position)
        **kwargs,
    ):
        """
        Create a simple two-sided debate.

        Args:
            topic: Debate topic
            position_a: Tuple of (debater_name, position_description)
            position_b: Tuple of (debater_name, position_description)
            **kwargs: Additional debate configuration
        """
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.simple.agent import SimpleAgent

        name_a, pos_a = position_a
        name_b, pos_b = position_b

        # Create debater agents
        agents = {}

        engine_a = AugLLMConfig(
            name=f"{name_a.lower()}_engine",
            system_message=(
                f"You are {name_a}, debating the topic: {topic}. "
                f"Your position is: {pos_a}. "
                "Make compelling arguments, respond to counterarguments, and maintain your position. "
                "Be respectful but firm in your argumentation."
            ),
            temperature=0.7,
        )
        agents[name_a] = SimpleAgent(name=f"{name_a}_agent", engine=engine_a)

        engine_b = AugLLMConfig(
            name=f"{name_b.lower()}_engine",
            system_message=(
                f"You are {name_b}, debating the topic: {topic}. "
                f"Your position is: {pos_b}. "
                "Make compelling arguments, respond to counterarguments, and maintain your position. "
                "Be respectful but firm in your argumentation."
            ),
            temperature=0.7,
        )
        agents[name_b] = SimpleAgent(name=f"{name_b}_agent", engine=engine_b)

        return cls(
            participant_agents=agents,
            topic=topic,
            debate_positions={name_a: pos_a, name_b: pos_b},
            **kwargs,
        )
