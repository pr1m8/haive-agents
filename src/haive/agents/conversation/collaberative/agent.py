from typing import Any, Dict, List, Literal, Optional

from haive.core.logging.rich_logger import LogLevel, get_logger
from pydantic import Field

from haive.agents.conversation.base.agent import BaseConversationAgent
from haive.agents.conversation.collaberative.state import CollaborativeState

logger = get_logger(__name__)
logger.set_level(LogLevel.WARNING)

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage

from haive.agents.conversation.base.agent import BaseConversationAgent


class CollaborativeConversation(BaseConversationAgent):
    """
    Collaborative conversation for building shared content.

    Features:
    - Structured document building
    - Section-based contributions
    - Review and approval process
    - Version tracking
    - Multiple output formats
    """

    mode: Literal["collaborative"] = Field(default="collaborative")

    # Document structure
    document_title: str = Field(default="Collaborative Document")
    sections: List[str] = Field(
        default_factory=lambda: ["Introduction", "Main Content", "Conclusion"],
        description="Sections to collaborate on",
    )

    # Collaboration settings
    require_approval: bool = Field(
        default=False, description="Require approval before finalizing sections"
    )
    min_contributions_per_section: int = Field(
        default=1, description="Minimum contributions per section"
    )
    allow_revisions: bool = Field(
        default=True, description="Allow revision of completed sections"
    )

    # Output configuration
    output_format: Literal["markdown", "code", "outline", "report"] = Field(
        default="markdown"
    )
    include_attribution: bool = Field(
        default=True, description="Include contributor names in output"
    )

    def get_conversation_state_schema(self) -> type:
        """Use collaborative state schema."""
        return CollaborativeState

    def _custom_initialization(self, state: CollaborativeState) -> Dict[str, Any]:
        """Initialize collaborative-specific state."""
        # Initialize document with title
        if self.output_format == "markdown":
            initial_doc = f"# {self.document_title}\n\n"
        elif self.output_format == "code":
            initial_doc = f"# {self.document_title}\n# Collaborative Code\n\n"
        elif self.output_format == "outline":
            initial_doc = f"{self.document_title}\n{'=' * len(self.document_title)}\n\n"
        else:  # report
            initial_doc = f"{self.document_title.upper()}\n\n"

        return {
            "shared_document": initial_doc,
            "sections_order": self.sections,
            "current_section": self.sections[0] if self.sections else None,
            "output_format": self.output_format,
            "document_sections": {section: "" for section in self.sections},
        }

    def _create_initial_message(self) -> BaseMessage:
        """Create collaborative session introduction."""
        sections_list = "\n".join([f"- {section}" for section in self.sections])

        return HumanMessage(
            content=f"""📝 Collaborative Session: {self.document_title}

Topic: {self.topic}

We'll work together on these sections:
{sections_list}

Format: {self.output_format}
Min contributions per section: {self.min_contributions_per_section}

Let's start with: {self.sections[0] if self.sections else 'open discussion'}"""
        )

    def select_speaker(self, state: CollaborativeState) -> Dict[str, Any]:
        """Select speaker based on contribution balance and current section."""
        # Check if we need to move to next section
        section_update = self._check_section_completion(state)
        if section_update:
            return section_update

        # Get current section
        current_section = state.current_section
        if not current_section:
            return {"conversation_ended": True}

        # Count contributions to current section
        section_contributors = {}
        for contributor, section, _ in state.contributions:
            if section == current_section:
                section_contributors[contributor] = (
                    section_contributors.get(contributor, 0) + 1
                )

        # Find who hasn't contributed enough
        speakers = state.speakers
        min_contributor = None
        min_count = float("inf")

        for speaker in speakers:
            count = section_contributors.get(speaker, 0)
            if count < min_count:
                min_count = count
                min_contributor = speaker

        # If everyone has contributed minimum, pick least active overall
        if min_count >= self.min_contributions_per_section:
            return self._select_least_active_overall(state)

        return {"current_speaker": min_contributor}

    def _check_section_completion(
        self, state: CollaborativeState
    ) -> Optional[Dict[str, Any]]:
        """Check if current section is complete and move to next."""
        current_section = state.current_section
        if not current_section:
            return None

        # Count contributions to current section
        section_contribution_count = sum(
            1 for _, section, _ in state.contributions if section == current_section
        )

        # Check if section has enough contributions
        min_total = self.min_contributions_per_section * len(state.speakers)
        if section_contribution_count >= min_total:
            # Mark section complete
            completed = list(state.completed_sections)
            completed.append(current_section)

            # Find next section
            next_section = None
            for section in state.sections_order:
                if section not in completed:
                    next_section = section
                    break

            if next_section:
                transition_msg = SystemMessage(
                    content=f"✅ Section '{current_section}' complete. "
                    f"Moving to '{next_section}'."
                )
                return {
                    "completed_sections": completed,
                    "current_section": next_section,
                    "messages": [transition_msg],
                    "current_speaker": state.speakers[0] if state.speakers else None,
                }
            else:
                # All sections complete
                return self._finalize_document(state)

        return None

    def _select_least_active_overall(self, state: CollaborativeState) -> Dict[str, Any]:
        """Select speaker who has contributed least overall."""
        contribution_count = dict(state.contribution_count)

        min_speaker = None
        min_count = float("inf")

        for speaker in state.speakers:
            count = contribution_count.get(speaker, 0)
            if count < min_count:
                min_count = count
                min_speaker = speaker

        return {"current_speaker": min_speaker}

    def _prepare_agent_input(
        self, state: CollaborativeState, agent_name: str
    ) -> Dict[str, Any]:
        """Prepare input with collaboration context."""
        base_input = super()._prepare_agent_input(state, agent_name)

        # Get current section content
        current_section = state.current_section
        section_content = state.document_sections.get(str(current_section), "")

        # Create context message
        context_parts = [
            f"Current Section: {current_section}",
            f"Your total contributions: {state.contribution_count.get(agent_name, 0)}",
            f"Format: {state.output_format}",
        ]

        if section_content:
            context_parts.append(f"\nCurrent content:\n{section_content}")

        context_msg = SystemMessage(content="\n".join(context_parts))

        # Add instruction based on section state
        if section_content:
            instruction = SystemMessage(
                content="Build upon or enhance the existing content. "
                "Be constructive and collaborative."
            )
        else:
            instruction = SystemMessage(
                content=f"Start the '{current_section}' section. "
                "Provide a solid foundation for others to build on."
            )

        messages = [context_msg, instruction] + base_input.get("messages", [])
        base_input["messages"] = messages

        return base_input

    def process_response(self, state: CollaborativeState) -> Dict[str, Any]:
        """Process contribution and update document."""
        update = {}

        if not state.current_speaker or not state.messages:
            return update

        last_msg = state.messages[-1]
        if not isinstance(last_msg, AIMessage) or not hasattr(last_msg, "name"):
            return update

        contributor = last_msg.name
        content = last_msg.content
        current_section = state.current_section

        # Add contribution
        contribution = (contributor, current_section, content)
        update["contributions"] = [contribution]

        # Update contribution count
        count = dict(state.contribution_count)
        count[str(contributor)] = count.get(str(contributor), 0) + 1
        update["contribution_count"] = count

        # Update section content
        sections = dict(state.document_sections)
        if current_section not in sections:
            sections[str(current_section)] = ""

        # Add content with attribution if enabled
        if self.include_attribution:
            attribution = f"\n[{contributor}]: "
        else:
            attribution = "\n"

        sections[str(current_section)] += attribution + str(content) + "\n"
        update["document_sections"] = sections

        # Update main document
        update["shared_document"] = self._compile_document(state, sections)

        return update

    def _compile_document(
        self, state: CollaborativeState, sections: Dict[str, str]
    ) -> str:
        """Compile sections into final document."""
        doc_parts = [state.shared_document.split("\n\n")[0]]  # Keep title

        for section in state.sections_order:
            if section in sections and sections[section]:
                if self.output_format == "markdown":
                    doc_parts.append(f"## {section}\n{sections[section]}")
                elif self.output_format == "outline":
                    doc_parts.append(f"{section}:\n{sections[section]}")
                elif self.output_format == "code":
                    doc_parts.append(f"# {section}\n{sections[section]}")
                else:  # report
                    doc_parts.append(f"{section.upper()}\n\n{sections[section]}")

        return "\n\n".join(doc_parts)

    def _finalize_document(self, state: CollaborativeState) -> Dict[str, Any]:
        """Finalize the collaborative document."""
        # Create final summary
        total_contributions = len(state.contributions)
        contributor_summary = []

        for speaker, count in state.contribution_count.items():
            contributor_summary.append(f"- {speaker}: {count} contributions")

        summary_msg = SystemMessage(
            content=f"""📄 Document Complete!

Title: {self.document_title}
Total Contributions: {total_contributions}

Contributors:
{chr(10).join(contributor_summary)}

The final document has been compiled."""
        )

        return {"messages": [summary_msg], "conversation_ended": True}

    def _check_custom_end_conditions(
        self, state: CollaborativeState
    ) -> Optional[Dict[str, Any]]:
        """Check if all sections are complete."""
        if len(state.completed_sections) >= len(self.sections):
            return self._finalize_document(state)
        return None

    @classmethod
    def create_brainstorming_session(
        cls,
        topic: str,
        participants: List[str],
        sections: Optional[List[str]] = None,
        **kwargs,
    ):
        """
        Create a brainstorming/ideation session.

        Args:
            topic: Brainstorming topic
            participants: List of participant names
            sections: Optional custom sections
            **kwargs: Additional configuration
        """
        if sections is None:
            sections = ["Problem Statement", "Ideas", "Evaluation", "Action Items"]

        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.simple.agent import SimpleAgent

        agents = {}
        for name in participants:
            engine = AugLLMConfig(
                name=f"{name.lower()}_engine",
                system_message=(
                    f"You are {name}, participating in a brainstorming session. "
                    "Be creative, build on others' ideas, and think outside the box. "
                    "Keep contributions focused and constructive."
                ),
                temperature=0.8,
            )
            agents[name] = SimpleAgent(name=f"{name}_agent", engine=engine)

        return cls(
            participant_agents=agents,
            topic=topic,
            document_title=f"Brainstorming: {topic}",
            sections=sections,
            output_format="outline",
            **kwargs,
        )

    @classmethod
    def create_code_review(
        cls,
        code_description: str,
        reviewers: Dict[str, str],  # name -> expertise
        **kwargs,
    ):
        """
        Create a collaborative code review session.

        Args:
            code_description: Description of code being reviewed
            reviewers: Dictionary mapping reviewer names to expertise
            **kwargs: Additional configuration
        """
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.simple.agent import SimpleAgent

        agents = {}
        for name, expertise in reviewers.items():
            engine = AugLLMConfig(
                name=f"{name.lower()}_engine",
                system_message=(
                    f"You are {name}, a {expertise} reviewing code. "
                    "Provide constructive feedback on code quality, design, "
                    "performance, and best practices. Be specific and helpful."
                ),
                temperature=0.6,
            )
            agents[name] = SimpleAgent(name=f"{name}_agent", engine=engine)

        return cls(
            participant_agents=agents,
            topic=code_description,
            document_title="Code Review",
            sections=["Overview", "Strengths", "Issues", "Suggestions", "Conclusion"],
            output_format="markdown",
            **kwargs,
        )
