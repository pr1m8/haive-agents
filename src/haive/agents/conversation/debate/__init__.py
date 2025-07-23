"""Module exports."""

from haive.agents.conversation.debate.agent import (
    DebateConversation,
    conclude_conversation,
    create_simple_debate,
    get_conversation_state_schema,
    process_response,
    select_speaker,
    setup_agent,
    validate_debate_setup,
)
from haive.agents.conversation.debate.example import (
    example_oxford_debate,
    example_panel_debate,
    example_simple_debate,
    example_socratic_debate,
)
from haive.agents.conversation.debate.state import (
    DebateState,
    all_arguments_complete,
    all_rebuttals_complete,
    debate_progress,
    debate_statistics,
    get_participant_summary,
    in_rebuttal_phase,
    next_phase,
    phase_should_transition,
    should_end_debate,
)

__all__ = [
    "DebateConversation",
    "DebateState",
    "all_arguments_complete",
    "all_rebuttals_complete",
    "conclude_conversation",
    "create_simple_debate",
    "debate_progress",
    "debate_statistics",
    "example_oxford_debate",
    "example_panel_debate",
    "example_simple_debate",
    "example_socratic_debate",
    "get_conversation_state_schema",
    "get_participant_summary",
    "in_rebuttal_phase",
    "next_phase",
    "phase_should_transition",
    "process_response",
    "select_speaker",
    "setup_agent",
    "should_end_debate",
    "validate_debate_setup",
]
