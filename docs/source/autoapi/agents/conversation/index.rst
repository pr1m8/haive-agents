agents.conversation
===================

.. py:module:: agents.conversation

.. autoapi-nested-parse::

   Conversation Agents - Multi-Agent Dialogue Orchestration System.

   A comprehensive suite of multi-agent conversation orchestrators for facilitating
   different types of agent-to-agent interactions and dialogues. This package provides
   specialized conversation frameworks that enable multiple agents to interact with each
   other according to different patterns, structures, and rules.

   Architecture:
       The conversation system is built around a hierarchical architecture:

       - BaseConversationAgent: Core orchestration logic and state management
       - Specialized conversation types: Each with unique interaction patterns
       - Shared state system: Common message handling and flow control
       - Integration layer: Seamless connection with other Haive components

   Core Conversation Types:
       BaseConversationAgent: Foundation for all conversation agents with core
           orchestration logic, state management, and message routing capabilities.

       RoundRobinConversation: Simple turn-taking conversation where each agent
           speaks in sequence. Useful for panel discussions and ordered dialogues.

       DirectedConversation: Conversations with a directed flow controlled by a
           moderator. Supports dynamic speaker selection and flow control.

       DebateConversation: Structured debates with positions, arguments, rebuttals,
           and judging. Includes scoring and evaluation mechanisms.

       CollaborativeConversation: Multiple agents collaborating on a shared task.
           Features task decomposition, role assignment, and result synthesis.

       SocialMediaConversation: Simulated social media interactions with posts,
           replies, reactions, and viral propagation patterns.

   State Management:
       Each conversation type maintains rich state information including:
       - Participant registry and roles
       - Message history and threading
       - Turn management and flow control
       - Context and memory management
       - Performance metrics and analytics

   Usage Patterns:
       Basic Round Robin Conversation::

           from haive.agents.conversation import RoundRobinConversation
           from haive.agents.simple import SimpleAgent

           # Create participants
           alice = SimpleAgent(name="Alice")
           bob = SimpleAgent(name="Bob")
           charlie = SimpleAgent(name="Charlie")

           # Create conversation
           conversation = RoundRobinConversation(
               participants=[alice, bob, charlie],
               topic="Future of AI",
               rounds=3
           )

           # Run conversation
           result = await conversation.arun()

       Structured Debate::

           from haive.agents.conversation import DebateConversation

           debate = DebateConversation(
               topic="Should AI be regulated?",
               pro_agents=[pro_agent1, pro_agent2],
               con_agents=[con_agent1, con_agent2],
               judge_agent=judge_agent,
               rounds=5
           )

           result = await debate.arun()
           winner = result.get("winner")

       Collaborative Task::

           from haive.agents.conversation import CollaborativeConversation

           collaboration = CollaborativeConversation(
               participants={
                   "designer": designer_agent,
                   "engineer": engineer_agent,
                   "product_manager": pm_agent
               },
               task="Design a new mobile app",
               deliverables=["mockup", "specs", "timeline"]
           )

           result = await collaboration.arun()

   Advanced Features:
       - Dynamic participant addition/removal
       - Conversation branching and merging
       - Real-time conversation monitoring
       - Conversation recording and playback
       - Integration with external chat systems
       - Conversation analytics and insights

   Integration:
       Conversation agents integrate seamlessly with:
       - Haive core schema system for state management
       - Graph-based workflow execution
       - Tool integration for enhanced capabilities
       - Persistence systems for conversation history
       - Monitoring and analytics platforms

   .. rubric:: Examples

   For comprehensive examples, see the documentation and examples directory:
   - examples/basic_round_robin.py
   - examples/structured_debate.py
   - examples/collaborative_design.py
   - examples/social_media_simulation.py

   .. seealso::

      - :mod:`~haive.agents.base.agent`: Base agent classes that conversation agents extend
      - :mod:`~haive.agents.simple.agent`: Simple agent used for conversation participants
      - :mod:`~haive.core.graph.state_graph`: State graph system for conversation flow
      - :mod:`~haive.core.schema`: State schema system for conversation state

   Version: 1.0.0
   Author: Haive Team
   License: MIT


   .. autolink-examples:: agents.conversation
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/conversation/base/index
   /autoapi/agents/conversation/collaberative/index
   /autoapi/agents/conversation/debate/index
   /autoapi/agents/conversation/directed/index
   /autoapi/agents/conversation/round_robin/index
   /autoapi/agents/conversation/social_media/index


Attributes
----------

.. autoapisummary::

   agents.conversation.ConversationStatus
   agents.conversation.ConversationType
   agents.conversation.MessageType
   agents.conversation.ParticipantRole
   agents.conversation.__author__
   agents.conversation.__license__
   agents.conversation.__version__


Classes
-------

.. autoapisummary::

   agents.conversation.CollaborativeConfig
   agents.conversation.ConversationConfig
   agents.conversation.ConversationParticipant
   agents.conversation.DebateConfig


Functions
---------

.. autoapisummary::

   agents.conversation.create_collaboration
   agents.conversation.create_conversation
   agents.conversation.create_debate
   agents.conversation.get_conversation_types
   agents.conversation.validate_participants


Package Contents
----------------

.. py:class:: CollaborativeConfig

   Bases: :py:obj:`ConversationConfig`


   Configuration specific to collaborative conversations.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CollaborativeConfig
      :collapse:

   .. py:attribute:: deliverables
      :type:  NotRequired[list[str]]


   .. py:attribute:: progress_tracking
      :type:  NotRequired[bool]


   .. py:attribute:: role_assignment
      :type:  NotRequired[dict[str, str]]


   .. py:attribute:: task_decomposition
      :type:  NotRequired[bool]


.. py:class:: ConversationConfig

   Bases: :py:obj:`typing_extensions.TypedDict`


   Configuration for conversation agents.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ConversationConfig
      :collapse:

   .. py:attribute:: allow_interruptions
      :type:  NotRequired[bool]


   .. py:attribute:: auto_moderation
      :type:  NotRequired[bool]


   .. py:attribute:: max_turns
      :type:  NotRequired[int]


   .. py:attribute:: save_history
      :type:  NotRequired[bool]


   .. py:attribute:: timeout_seconds
      :type:  NotRequired[float]


.. py:class:: ConversationParticipant

   Bases: :py:obj:`Protocol`


   Protocol for agents that can participate in conversations.


   .. autolink-examples:: ConversationParticipant
      :collapse:

   .. py:method:: arun(input_data: Any) -> Any
      :async:


      Run the agent with input data.


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: get_role() -> ParticipantRole

      Get the participant's role in the conversation.


      .. autolink-examples:: get_role
         :collapse:


   .. py:attribute:: name
      :type:  str


.. py:class:: DebateConfig

   Bases: :py:obj:`ConversationConfig`


   Configuration specific to debate conversations.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DebateConfig
      :collapse:

   .. py:attribute:: allow_rebuttals
      :type:  NotRequired[bool]


   .. py:attribute:: rounds
      :type:  NotRequired[int]


   .. py:attribute:: scoring_system
      :type:  NotRequired[str]


   .. py:attribute:: time_per_round
      :type:  NotRequired[float]


.. py:function:: create_collaboration(task: str, participants: dict[str, ConversationParticipant], deliverables: list[str] | None = None, config: CollaborativeConfig | None = None) -> haive.agents.conversation.collaberative.agent.CollaborativeConversation

   Create a collaborative conversation for team tasks.

   :param task: Task description for the collaboration
   :param participants: Dictionary mapping roles to participant agents
   :param deliverables: Optional list of expected deliverables
   :param config: Optional collaboration configuration

   :returns: Configured collaborative conversation

   .. rubric:: Examples

   Software development team::

       collaboration = create_collaboration(
           task="Design a new mobile app",
           participants={
               "designer": ui_designer,
               "engineer": developer,
               "product_manager": pm
           },
           deliverables=["mockup", "specs", "timeline"]
       )

   Research team::

       collaboration = create_collaboration(
           task="Analyze market trends",
           participants={
               "analyst": data_analyst,
               "researcher": market_researcher,
               "strategist": business_strategist
           },
           config={"progress_tracking": True}
       )


   .. autolink-examples:: create_collaboration
      :collapse:

.. py:function:: create_conversation(conversation_type: ConversationType, participants: list[ConversationParticipant], topic: str, config: ConversationConfig | None = None, **kwargs: Any) -> haive.agents.conversation.base.agent.BaseConversationAgent

   Create a conversation agent of the specified type.

   :param conversation_type: Type of conversation to create
   :param participants: List of agents to participate in the conversation
   :param topic: Topic or subject of the conversation
   :param config: Optional configuration for the conversation
   :param \*\*kwargs: Additional keyword arguments specific to the conversation type

   :returns: Configured conversation agent

   .. rubric:: Examples

   Round robin conversation::

       conversation = create_conversation(
           "round_robin",
           participants=[alice, bob, charlie],
           topic="Future of AI",
           config={"max_turns": 10}
       )

   Debate conversation::

       debate = create_conversation(
           "debate",
           participants=[pro_agent, con_agent],
           topic="Should AI be regulated?",
           judge_agent=judge_agent,
           rounds=3
       )


   .. autolink-examples:: create_conversation
      :collapse:

.. py:function:: create_debate(topic: str, pro_agents: list[ConversationParticipant], con_agents: list[ConversationParticipant], judge_agent: ConversationParticipant | None = None, rounds: int = 3, config: DebateConfig | None = None) -> haive.agents.conversation.debate.agent.DebateConversation

   Create a structured debate conversation.

   :param topic: Topic to debate
   :param pro_agents: Agents arguing for the topic
   :param con_agents: Agents arguing against the topic
   :param judge_agent: Optional judge agent to score the debate
   :param rounds: Number of debate rounds
   :param config: Optional debate configuration

   :returns: Configured debate conversation

   .. rubric:: Examples

   Simple debate::

       debate = create_debate(
           topic="Should AI be regulated?",
           pro_agents=[regulatory_expert],
           con_agents=[tech_advocate],
           judge_agent=neutral_judge
       )

   Multi-participant debate::

       debate = create_debate(
           topic="Climate change solutions",
           pro_agents=[scientist1, activist],
           con_agents=[economist, skeptic],
           rounds=5,
           config={"time_per_round": 300}
       )


   .. autolink-examples:: create_debate
      :collapse:

.. py:function:: get_conversation_types() -> list[ConversationType]

   Get list of available conversation types.

   :returns: List of available conversation type strings


   .. autolink-examples:: get_conversation_types
      :collapse:

.. py:function:: validate_participants(participants: list[ConversationParticipant], min_participants: int = 2, max_participants: int | None = None) -> bool

   Validate that participants meet conversation requirements.

   :param participants: List of participant agents
   :param min_participants: Minimum number of participants required
   :param max_participants: Maximum number of participants allowed

   :returns: True if participants are valid, False otherwise

   :raises ValueError: If validation fails with specific error details


   .. autolink-examples:: validate_participants
      :collapse:

.. py:type:: ConversationStatus
   :canonical: Literal['pending', 'active', 'paused', 'completed', 'cancelled']


.. py:type:: ConversationType
   :canonical: Literal['round_robin', 'directed', 'debate', 'collaborative', 'social_media']


.. py:type:: MessageType
   :canonical: Literal['statement', 'question', 'response', 'argument', 'rebuttal', 'judgment']


.. py:type:: ParticipantRole
   :canonical: Literal['speaker', 'moderator', 'judge', 'observer']


.. py:data:: __author__
   :value: 'Haive Team'


.. py:data:: __license__
   :value: 'MIT'


.. py:data:: __version__
   :value: '1.0.0'


