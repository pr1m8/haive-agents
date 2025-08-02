"""Structured debate conversation agent with positions and formal argumentation.

This module implements a debate conversation agent that manages structured debates
between multiple participants with defined positions, argument tracking, and
optional judging/scoring capabilities.
"""
import logging
from typing import Any, Literal
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langgraph.types import Command
from pydantic import BaseModel, Field, model_validator
from haive.agents.conversation.base.agent import BaseConversationAgent
from haive.agents.conversation.debate.state import DebateState
from haive.agents.simple.agent import SimpleAgent
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DebateConversation(BaseConversationAgent):
    """Structured debate conversation with positions and formal argumentation.

    This agent orchestrates formal debates between participants using a
    reducer-based state system for automatic tracking and phase management.

    Features:
    - Automatic round tracking via reducers
    - Phase transitions based on computed properties
    - Structured debate format with opening/closing statements
    - Optional judging and scoring
    - Configurable argument requirements
    """
    mode: Literal['debate'] = Field(default='debate', description='Conversation mode identifier')
    state_schema: type[BaseModel] = Field(default=DebateState, description='State schema class to use for this agent')
    debate_positions: dict[str, str] = Field(default_factory=dict, description='Mapping of participant names to their debate positions')
    enable_opening_statements: bool = Field(default=True, description='Whether to include opening statements phase')
    enable_closing_statements: bool = Field(default=True, description='Whether to include closing statements phase')
    arguments_per_side: int = Field(default=3, ge=1, le=10, description='Number of main arguments each participant should make')
    enable_judge: bool = Field(default=False, description='Whether to include a judge for scoring the debate')
    judge_name: str = Field(default='Judge', description='Name identifier for the judge participant')
    enforce_position_consistency: bool = Field(default=True, description='Ensure participants argue for their assigned positions')
    require_evidence: bool = Field(default=False, description='Require participants to cite evidence for claims')
    time_limit_per_turn: int | None = Field(default=None, ge=50, le=1000, description='Word limit per turn (if set)')
    debate_format: Literal['traditional', 'oxford', 'parliamentary'] = Field(default='traditional', description='Style of debate format to follow')

    @model_validator(mode='after')
    def validate_debate_setup(self) -> 'DebateConversation':
        """Validate debate configuration and participant setup."""
        if not self.state_schema or self.state_schema != DebateState:
            self.state_schema = DebateState
        if self.participant_agents and self.debate_positions:
            for participant in self.participant_agents:
                if participant not in self.debate_positions and participant != self.judge_name and self.enable_judge:
                    logger.warning(f"No position assigned to participant '{participant}'. They will be assigned a neutral position.")
        if self.enable_judge and self.judge_name in self.debate_positions:
            raise ValueError(f"Judge '{self.judge_name}' cannot have a debate position")
        return self

    def setup_agent(self) -> None:
        """Setup the debate agent with proper state schema."""
        self.state_schema = DebateState
        self.set_schema = True
        super().setup_agent()
        logger.debug(f'DebateConversation setup complete with state schema: {self.state_schema}')

    def get_conversation_state_schema(self) -> type[DebateState]:
        """Return the DebateState schema for this conversation."""
        return DebateState

    def _custom_initialization(self, state: DebateState) -> dict[str, Any]:
        """Initialize debate-specific state fields."""
        arguments_made = {}
        rebuttals = {}
        positions = self.debate_positions if self.debate_positions is not None else {}
        for name in positions:
            arguments_made[name] = []
            rebuttals[name] = []
        if self.enable_judge:
            arguments_made[self.judge_name] = []
            rebuttals[self.judge_name] = []
        return {'debate_positions': positions.copy(), 'arguments_made': arguments_made, 'rebuttals': rebuttals, 'arguments_per_side': self.arguments_per_side, 'opening_statements_complete': not self.enable_opening_statements, 'closing_statements_complete': False, 'current_phase': 'opening' if self.enable_opening_statements else 'arguments', 'phase_transitions': [('start', 0)], 'argument_scores': {}, 'judge_feedback': [], 'total_arguments': 0, 'total_rebuttals': 0}

    def _create_initial_message(self) -> BaseMessage:
        """Create the debate introduction message."""
        positions = self.debate_positions if self.debate_positions is not None else {}
        positions_str = '\n'.join([f'  • {name}: {position}' for name, position in positions.items()]) if positions else 'No positions assigned yet'
        structure = []
        phase_num = 1
        if self.enable_opening_statements:
            structure.append(f'{phase_num}. Opening Statements - Each participant presents their position')
            phase_num += 1
        structure.append(f'{phase_num}. Main Arguments - Each participant makes {self.arguments_per_side} arguments')
        phase_num += 1
        if self.enable_opening_statements or self.enable_closing_statements:
            structure.append(f'{phase_num}. Rebuttals - Participants respond to opposing arguments')
            phase_num += 1
        if self.enable_closing_statements:
            structure.append(f'{phase_num}. Closing Statements - Final summaries from each participant')
        if self.enable_judge:
            structure.append(f'\nThe debate will be judged by: {self.judge_name}')
        structure_str = '\n'.join(structure)
        rules = []
        if self.require_evidence:
            rules.append('All claims must be supported with evidence')
        if self.time_limit_per_turn:
            rules.append(f'Responses limited to {self.time_limit_per_turn} words')
        if self.enforce_position_consistency:
            rules.append('Participants must argue for their assigned position')
        rules_str = '\n'.join([f'  • {rule}' for rule in rules]) if rules else 'Standard debate rules apply'
        return HumanMessage(content=f'🎭 Welcome to the Formal Debate!\n\n📋 **Topic**: {self.topic}\n\n👥 **Participants and Positions**:\n{positions_str}\n\n📜 **Debate Format** ({self.debate_format}):\n{structure_str}\n\n⚖️ **Rules**:\n{rules_str}\n\nLet us begin! {(next(iter(positions.keys())) if positions else 'Participants')}, please present your opening statement.')

    def select_speaker(self, state: DebateState) -> Command:
        """Select the next speaker based on debate phase and rules."""
        updates = {}
        logger.debug(f'select_speaker: phase={state.current_phase}, should_end_debate={state.should_end_debate}')
        if state.should_end_debate:
            logger.info('Debate should end based on computed property')
            return Command(update={'conversation_ended': True, 'current_phase': 'complete'})
        if state.phase_should_transition:
            logger.info(f'Phase should transition: {state.current_phase} -> {state.next_phase}')
            transition_updates = self._transition_to_phase(state, state.next_phase)
            return Command(update=transition_updates)
        if state.current_phase == 'opening':
            speaker_update = self._select_opening_speaker(state)
        elif state.current_phase == 'arguments':
            speaker_update = self._select_argument_speaker(state)
        elif state.current_phase == 'rebuttals':
            speaker_update = self._select_rebuttal_speaker(state)
        elif state.current_phase == 'closing':
            speaker_update = self._select_closing_speaker(state)
        elif state.current_phase == 'judging' and self.enable_judge:
            speaker_update = {'current_speaker': self.judge_name}
        else:
            speaker_update = {'conversation_ended': True}
        updates.update(speaker_update)
        return Command(update=updates)

    def _transition_to_phase(self, state: DebateState, new_phase: str) -> dict[str, Any]:
        """Create state updates for transitioning to a new phase."""
        messages = {'arguments': 'Opening statements complete. Moving to main arguments.', 'rebuttals': 'Main arguments complete. Moving to rebuttals.', 'closing': 'Rebuttals complete. Moving to closing statements.', 'judging': 'Closing statements complete. The judge will now deliberate.', 'complete': 'Debate complete!'}
        message = messages.get(new_phase, f'Transitioning to {new_phase}')
        transition_msg = SystemMessage(content=f'\n🔄 {message}\n')
        updates = {'current_phase': new_phase, 'phase_transitions': [(new_phase, state.turn_count)], 'messages': [transition_msg]}
        if new_phase == 'complete':
            updates['conversation_ended'] = True
            return updates
        if new_phase in ['arguments', 'rebuttals', 'closing']:
            if state.debate_positions:
                updates['current_speaker'] = next(iter(state.debate_positions.keys()))
            else:
                logger.warning('No debate positions available for speaker selection')
        elif new_phase == 'judging':
            updates['current_speaker'] = self.judge_name
        return updates

    def _select_opening_speaker(self, state: DebateState) -> dict[str, Any]:
        """Select speaker for opening statements."""
        speakers_done = set()
        opening_count = 0
        for msg in state.messages:
            if isinstance(msg, AIMessage) and hasattr(msg, 'name'):
                if msg.name in state.debate_positions and opening_count < len(state.debate_positions):
                    speakers_done.add(msg.name)
                    opening_count += 1
        for speaker in state.debate_positions:
            if speaker not in speakers_done:
                return {'current_speaker': speaker}
        return {}

    def _select_argument_speaker(self, state: DebateState) -> dict[str, Any]:
        """Select speaker for main arguments phase."""
        if state.all_arguments_complete:
            return {}
        candidates = []
        for speaker, progress in state.debate_progress.items():
            if progress < 1.0:
                candidates.append(speaker)
        if candidates:
            min_args = min((len(state.arguments_made.get(s, [])) for s in candidates))
            for speaker in candidates:
                if len(state.arguments_made.get(speaker, [])) == min_args:
                    return {'current_speaker': speaker}
        return {}

    def _select_rebuttal_speaker(self, state: DebateState) -> dict[str, Any]:
        """Select speaker for rebuttal phase."""
        rebuttal_counts = {speaker: len(rebuttals) for speaker, rebuttals in state.rebuttals.items()}
        candidates = [speaker for speaker in state.debate_positions if rebuttal_counts.get(speaker, 0) == 0]
        if candidates:
            return {'current_speaker': candidates[0]}
        return {}

    def _select_closing_speaker(self, state: DebateState) -> dict[str, Any]:
        """Select speaker for closing statements."""
        closing_speakers = set()
        for msg in reversed(state.messages):
            if isinstance(msg, AIMessage) and hasattr(msg, 'name'):
                if msg.name in state.debate_positions:
                    content_lower = str(msg.content).lower()
                    if any((word in content_lower for word in ['closing', 'conclusion', 'final statement', 'summary'])):
                        closing_speakers.add(msg.name)
                    if len(closing_speakers) == len(state.debate_positions):
                        break
        for speaker in state.debate_positions:
            if speaker not in closing_speakers:
                return {'current_speaker': speaker}
        return {}

    def _prepare_agent_input(self, state: DebateState, agent_name: str) -> dict[str, Any]:
        """Prepare input for a specific agent with debate context."""
        base_input = super()._prepare_agent_input(state, agent_name)
        participant_info = state.get_participant_summary(agent_name)
        context_parts = [f'🎭 Debate Phase: {state.current_phase.title()}', f'📌 Your Position: {participant_info['position']}', f'📊 Your Progress: {participant_info['arguments_made']} arguments, {participant_info['rebuttals_made']} rebuttals', f'📈 Completion: {participant_info['progress']:.0%}']
        instructions = self._get_phase_instructions(state, agent_name)
        if instructions:
            context_parts.append(f'\n📝 Instructions: {instructions}')
        if state.current_phase == 'rebuttals':
            opponent_summary = self._get_opponent_summary(state, agent_name)
            if opponent_summary:
                context_parts.append(f'\n👥 Opponent Arguments:\n{opponent_summary}')
        context_msg = SystemMessage(content='\n'.join(context_parts))
        messages = base_input.get('messages', [])
        base_input['messages'] = [context_msg, *messages]
        return base_input

    def _get_phase_instructions(self, state: DebateState, agent_name: str) -> str:
        """Get phase-specific instructions for an agent."""
        phase = state.current_phase
        if not self.enable_opening_statements and (not self.enable_closing_statements):
            return 'Make ONE concise argument. Keep it under 100 words.'
        if phase == 'opening':
            return 'Present your opening statement. Clearly state your position and preview your main arguments. Be compelling and set the tone.'
        if phase == 'arguments':
            participant_info = state.get_participant_summary(agent_name)
            args_made = participant_info['arguments_made']
            remaining = self.arguments_per_side - args_made
            return f'Present argument {args_made + 1} of {self.arguments_per_side}. Make a specific, well-supported point for your position. You have {remaining} more arguments after this.'
        if phase == 'rebuttals':
            return "Respond to your opponent's arguments. Point out flaws, contradictions, or weaknesses. Defend your own position against their attacks."
        if phase == 'closing':
            return 'Present your closing statement. Summarize your strongest points, address key rebuttals, and make a final compelling case for your position.'
        if phase == 'judging' and agent_name == self.judge_name:
            return 'As the judge, evaluate both sides fairly. Consider argument strength, evidence quality, and rebuttal effectiveness. Declare a winner and explain why.'
        return ''

    def _get_opponent_summary(self, state: DebateState, agent_name: str) -> str:
        """Get summary of opponent arguments for rebuttal context."""
        summaries = []
        for opponent, arguments in state.arguments_made.items():
            if opponent != agent_name and opponent in state.debate_positions:
                position = state.debate_positions[opponent]
                summaries.append(f'{opponent} ({position}):')
                for i, arg in enumerate(arguments[-3:], 1):
                    arg_summary = arg[:150] + '...' if len(arg) > 150 else arg
                    summaries.append(f'  {i}. {arg_summary}')
        return '\n'.join(summaries)

    def process_response(self, state: DebateState) -> Command:
        """Process agent response using reducers for automatic tracking."""
        updates = {}
        if not state.current_speaker or not state.messages:
            return Command(update=updates)
        last_msg = state.messages[-1]
        if not isinstance(last_msg, AIMessage) or not hasattr(last_msg, 'name'):
            return Command(update=updates)
        speaker = last_msg.name
        content = str(last_msg.content)
        phase = state.current_phase
        if phase == 'arguments' and speaker in state.debate_positions:
            current_args = len(state.arguments_made.get(speaker, []))
            if current_args < self.arguments_per_side:
                updates['total_arguments'] = 1
                arguments = dict(state.arguments_made)
                if speaker not in arguments:
                    arguments[speaker] = []
                arguments[speaker].append(content[:200])
                updates['arguments_made'] = arguments
        elif phase == 'rebuttals' and speaker in state.debate_positions:
            current_rebuttals = len(state.rebuttals.get(speaker, []))
            if current_rebuttals == 0:
                updates['total_rebuttals'] = 1
                rebuttals_dict = dict(state.rebuttals)
                if speaker not in rebuttals_dict:
                    rebuttals_dict[speaker] = []
                target = self._identify_rebuttal_target(content, state, speaker)
                if target:
                    rebuttals_dict[speaker].append((target, content[:200]))
                else:
                    rebuttals_dict[speaker].append(('general', content[:200]))
                updates['rebuttals'] = rebuttals_dict
        elif phase == 'judging' and speaker == self.judge_name:
            updates['judge_feedback'] = [content]
            winner = self._extract_debate_winner(content, state)
            if winner:
                updates['debate_winner'] = winner
        if phase == 'opening':
            opening_speakers = set()
            for msg in state.messages:
                if isinstance(msg, AIMessage) and hasattr(msg, 'name'):
                    if msg.name in state.debate_positions:
                        opening_speakers.add(msg.name)
            if len(opening_speakers) >= len(state.debate_positions):
                updates['opening_statements_complete'] = True
        elif phase == 'closing':
            closing_speakers = set()
            for msg in reversed(state.messages):
                if isinstance(msg, AIMessage) and hasattr(msg, 'name'):
                    if msg.name in state.debate_positions:
                        content_lower = str(msg.content).lower()
                        if any((word in content_lower for word in ['closing', 'conclusion', 'final'])):
                            closing_speakers.add(msg.name)
            if len(closing_speakers) >= len(state.debate_positions):
                updates['closing_statements_complete'] = True
        return Command(update=updates)

    def _identify_rebuttal_target(self, content: str, state: DebateState, speaker: str) -> str | None:
        """Identify who a rebuttal is targeting."""
        content_lower = content.lower()
        for opponent in state.debate_positions:
            if opponent != speaker and opponent.lower() in content_lower:
                return opponent
        opponents = [p for p in state.debate_positions if p != speaker]
        return opponents[0] if opponents else None

    def _extract_debate_winner(self, judge_content: str, state: DebateState) -> str | None:
        """Extract winner from judge's decision."""
        content_lower = judge_content.lower()
        for participant in state.debate_positions:
            if any((phrase in content_lower for phrase in [f'{participant.lower()} wins', f'winner is {participant.lower()}', f'victory to {participant.lower()}', f'{participant.lower()} has won'])):
                return participant
        return None

    def _check_custom_end_conditions(self, state: DebateState) -> dict[str, Any] | None:
        """Check custom end conditions using computed properties."""
        if state.should_end_debate:
            return {'conversation_ended': True}
        return None

    def conclude_conversation(self, state: DebateState) -> Command:
        """Create debate conclusion using state statistics."""
        stats = state.debate_statistics
        summary_parts = [f"🏁 Debate Concluded: '{self.topic}'", f'📊 Total Rounds: {stats['current_round']}', f'🔄 Total Turns: {stats['total_turns']}', '']
        summary_parts.append('👥 Participant Performance:')
        for speaker in state.debate_positions:
            summary = state.get_participant_summary(speaker)
            summary_parts.append(f'  • {summary['name']} ({summary['position']}): {summary['arguments_made']} arguments, {summary['rebuttals_made']} rebuttals')
            if summary['score'] > 0:
                summary_parts.append(f'    Score: {summary['score']:.2f}')
        if state.debate_winner:
            summary_parts.extend(['', f'🏆 Winner: {state.debate_winner}'])
        if state.judge_feedback:
            summary_parts.extend(['', "⚖️ Judge's Comments:", state.judge_feedback[-1][:500] if state.judge_feedback else ''])
        summary_parts.extend(['', '📈 Debate Statistics:', f'  • Total Arguments: {stats['total_arguments']}', f'  • Total Rebuttals: {stats['total_rebuttals']}', f'  • Phases Completed: {len(state.phase_transitions)}', f'  • Progress: {state.conversation_progress:.0%}'])
        conclusion_msg = SystemMessage(content='\n'.join(summary_parts))
        return Command(update={'messages': [conclusion_msg], 'conversation_ended': True, 'current_phase': 'complete'})

    @classmethod
    def create_simple_debate(cls, topic: str, position_a: tuple[str, str], position_b: tuple[str, str], enable_judge: bool=False, arguments_per_side: int=3, temperature: float=0.7, **kwargs) -> 'DebateConversation':
        """Create a simple two-sided debate conversation."""
        name_a, pos_a = position_a
        name_b, pos_b = position_b
        agents = {}
        engine_a = AugLLMConfig(name=f'{name_a.lower()}_engine', system_message=f"You are {name_a}, participating in a formal debate on the topic: '{topic}'. Your position is: {pos_a}. You must:\n1. Make compelling, logical arguments for your position\n2. Use evidence and examples to support your claims\n3. Respond effectively to counterarguments\n4. Maintain a respectful, professional tone\n5. Stay consistent with your assigned position throughout\nBe persuasive but intellectually honest. Keep responses concise.", temperature=temperature)
        agents[name_a] = SimpleAgent(name=f'{name_a}_agent', engine=engine_a, state_schema=DebateState)
        engine_b = AugLLMConfig(name=f'{name_b.lower()}_engine', system_message=f"You are {name_b}, participating in a formal debate on the topic: '{topic}'. Your position is: {pos_b}. You must:\n1. Make compelling, logical arguments for your position\n2. Use evidence and examples to support your claims\n3. Respond effectively to counterarguments\n4. Maintain a respectful, professional tone\n5. Stay consistent with your assigned position throughout\nBe persuasive but intellectually honest. Keep responses concise.", temperature=temperature)
        agents[name_b] = SimpleAgent(name=f'{name_b}_agent', engine=engine_b, state_schema=DebateState)
        if enable_judge:
            judge_engine = AugLLMConfig(name='judge_engine', system_message=f"You are an impartial judge evaluating a debate on: '{topic}'. You must:\n1. Fairly evaluate arguments from both sides\n2. Consider logic, evidence, and rhetorical effectiveness\n3. Note strengths and weaknesses of each position\n4. Declare a winner based on debate performance, not personal bias\n5. Provide clear reasoning for your decision\nBe objective, thorough, and fair in your judgment.", temperature=0.3)
            agents['Judge'] = SimpleAgent(name='Judge_agent', engine=judge_engine, state_schema=DebateState)
        return cls(name='DebateConversation', participant_agents=agents, topic=topic, debate_positions={name_a: pos_a, name_b: pos_b}, enable_judge=enable_judge, arguments_per_side=arguments_per_side, state_schema=DebateState, **kwargs)

    def __repr__(self) -> str:
        """String representation of the debate conversation."""
        positions = ', '.join([f'{name}={pos[:20]}...' for name, pos in self.debate_positions.items()])
        return f"DebateConversation(topic='{self.topic}', positions=[{positions}], arguments_per_side={self.arguments_per_side})"