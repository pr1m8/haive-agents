"""
Directed conversation agent where participants respond to mentions and direct questions.
"""

import logging
import re
from typing import Any, Dict, List, Literal, Optional, Set

from haive.core.logging.rich_logger import LogLevel, get_logger
from langchain_core.messages import AIMessage, BaseMessage, SystemMessage
from pydantic import Field

from haive.agents.conversation.base.agent import BaseConversationAgent
from haive.agents.conversation.directed.state import DirectedConversationState

logger = get_logger(__name__)
logger.set_level(LogLevel.WARNING)


class DirectedConversation(BaseConversationAgent):
    """
    Directed conversation where agents respond to mentions and questions.

    Participants speak when:
    - They are directly mentioned (@name)
    - A question is directed at them
    - They haven't spoken in a while (configurable)
    """

    mode: Literal["directed"] = Field(default="directed")

    # Directed conversation settings
    mention_patterns: List[str] = Field(
        default_factory=lambda: ["@{name}", "{name},", "{name}:"],
        description="Patterns to detect mentions (use {name} as placeholder)",
    )
    fallback_to_round_robin: bool = Field(
        default=True, description="Use round-robin if no one is mentioned"
    )
    max_silence_turns: int = Field(
        default=3, description="Max turns before forcing someone to speak"
    )
    allow_self_selection: bool = Field(
        default=True, description="Allow agents to volunteer to speak"
    )

    def get_conversation_state_schema(self) -> type:
        """Use extended state schema."""
        return DirectedConversationState

    def select_speaker(self, state: DirectedConversationState) -> Dict[str, Any]:
        """Select speaker based on mentions and context."""
        # Check pending speakers first
        if state.pending_speakers:
            next_speaker = state.pending_speakers[0]
            remaining = state.pending_speakers[1:]
            return {"current_speaker": next_speaker, "pending_speakers": remaining}

        # Extract mentions from last message
        mentioned = self._extract_mentions(state)

        if mentioned:
            # Multiple mentions become pending speakers
            if len(mentioned) > 1:
                return {
                    "current_speaker": mentioned[0],
                    "pending_speakers": mentioned[1:],
                    "mentioned_speakers": mentioned,
                }
            else:
                return {
                    "current_speaker": mentioned[0],
                    "mentioned_speakers": mentioned,
                }

        # No mentions - use fallback strategy
        if self.fallback_to_round_robin:
            return self._select_round_robin(state)
        else:
            return self._select_least_active(state)

    def _extract_mentions(self, state: DirectedConversationState) -> List[str]:
        """Extract mentioned speakers from the last message."""
        if not state.messages:
            return []

        last_message = state.messages[-1]
        if not isinstance(last_message, (AIMessage, BaseMessage)) or not hasattr(
            last_message, "content"
        ):
            return []

        content = last_message.content
        mentioned = []

        # Check each speaker for mentions
        for speaker in state.speakers:
            for pattern in self.mention_patterns:
                # Create regex pattern
                speaker_pattern = pattern.format(name=speaker)
                # Escape special regex characters in the pattern
                escaped_pattern = re.escape(speaker_pattern).replace(
                    r"\{name\}", speaker
                )

                if re.search(str(escaped_pattern), str(content), re.IGNORECASE):
                    if speaker not in mentioned:
                        mentioned.append(speaker)
                    break

        # Also check for questions directed at specific people
        if "?" in content:
            mentioned.extend(
                self._extract_question_targets(str(content), state.speakers)
            )

        return list(
            dict.fromkeys(mentioned)
        )  # Remove duplicates while preserving order

    def _extract_question_targets(self, content: str, speakers: List[str]) -> List[str]:
        """Extract who questions are directed at."""
        targets = []

        # Look for patterns like "What do you think, Alice?"
        question_patterns = [
            r"what (?:do you think|about|is your opinion),?\s*(\w+)\?",
            r"(\w+),?\s*what (?:do you think|about)",
            r"how (?:about you|do you feel),?\s*(\w+)\?",
        ]

        for pattern in question_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                # Check if match is a speaker name
                for speaker in speakers:
                    if match.lower() == speaker.lower():
                        targets.append(speaker)

        return targets

    def _select_round_robin(self, state: DirectedConversationState) -> Dict[str, Any]:
        """Fallback to round-robin selection."""
        current_speaker = state.current_speaker
        speakers = state.speakers

        if not current_speaker:
            return {"current_speaker": speakers[0] if speakers else None}

        try:
            current_idx = speakers.index(current_speaker)
            next_idx = (current_idx + 1) % len(speakers)
            return {"current_speaker": speakers[next_idx]}
        except ValueError:
            return {"current_speaker": speakers[0] if speakers else None}

    def _select_least_active(self, state: DirectedConversationState) -> Dict[str, Any]:
        """Select the speaker who has been least active."""
        # Count messages per speaker
        message_count = {speaker: 0 for speaker in state.speakers}

        for msg in state.messages:
            if isinstance(msg, AIMessage) and hasattr(msg, "name"):
                if msg.name in message_count:
                    message_count[msg.name] += 1

        # Find speaker with minimum messages
        if message_count:
            least_active = min(message_count.items(), key=lambda x: x[1])[0]
            return {"current_speaker": least_active}

        return {"current_speaker": state.speakers[0] if state.speakers else None}

    def process_response(self, state: DirectedConversationState) -> Dict[str, Any]:
        """Track interaction patterns."""
        update = {}

        # Update interaction count
        if state.current_speaker and state.mentioned_speakers:
            interaction_count = dict(state.interaction_count)

            if state.current_speaker not in interaction_count:
                interaction_count[state.current_speaker] = {}

            for mentioned in state.mentioned_speakers:
                if mentioned != state.current_speaker:
                    current = interaction_count[state.current_speaker].get(mentioned, 0)
                    interaction_count[state.current_speaker][mentioned] = current + 1

            update["interaction_count"] = interaction_count

        # Clear mentioned speakers
        update["mentioned_speakers"] = []

        return update

    def _prepare_agent_input(
        self, state: DirectedConversationState, agent_name: str
    ) -> Dict[str, Any]:
        """Prepare input with mention context."""
        base_input = super()._prepare_agent_input(state, agent_name)

        # Add context about why they're speaking
        if agent_name in state.mentioned_speakers:
            mention_msg = SystemMessage(
                content=f"[You were mentioned in the conversation. Please respond.]"
            )
            messages = base_input.get("messages", [])
            # Insert before the last message
            if messages:
                messages = messages[:-1] + [mention_msg] + messages[-1:]
            else:
                messages = [mention_msg]
            base_input["messages"] = messages

        return base_input

    @classmethod
    def create_classroom(
        cls,
        teacher_name: str = "Teacher",
        student_names: Optional[List[str]] = None,
        topic: str = "Today's lesson",
        **kwargs,
    ):
        """
        Create a classroom-style directed conversation.

        Args:
            teacher_name: Name of the teacher
            student_names: List of student names
            topic: Lesson topic
            **kwargs: Additional conversation arguments
        """
        if student_names is None:
            student_names = ["Alice", "Bob", "Charlie"]

        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.simple.agent import SimpleAgent

        # Create teacher agent
        teacher_engine = AugLLMConfig(
            name=f"{teacher_name.lower()}_engine",
            system_message=(
                f"You are {teacher_name}, a teacher leading a discussion about {topic}. "
                "Ask questions to specific students using their names. "
                "Provide feedback and guide the discussion."
            ),
            temperature=0.6,
        )

        agents = {
            teacher_name: SimpleAgent(
                name=f"{teacher_name}_agent", engine=teacher_engine
            )
        }

        # Create student agents
        for student in student_names:
            student_engine = AugLLMConfig(
                name=f"{student.lower()}_engine",
                system_message=(
                    f"You are {student}, a student in class. "
                    "Answer when the teacher asks you questions. "
                    "You can also ask questions or respond to other students."
                ),
                temperature=0.7,
            )
            agents[student] = SimpleAgent(
                name=f"{student}_agent", engine=student_engine
            )

        return cls(
            participant_agents=agents,  # type: ignore
            topic=topic,
            mention_patterns=["@{name}", "{name},", "{name}:", "ask {name}"],
            **kwargs,
        )
