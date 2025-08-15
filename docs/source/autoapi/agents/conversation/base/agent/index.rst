agents.conversation.base.agent
==============================

.. py:module:: agents.conversation.base.agent

.. autoapi-nested-parse::

   Base conversation agent providing core multi-agent conversation functionality.

   This base class handles the orchestration of conversations between multiple agents,
   with support for different conversation modes and patterns. It implements the core
   graph-based state management system that all conversation types extend.

   The BaseConversationAgent provides:

   1. A common orchestration flow for all conversation types
   2. Agent compilation and execution management
   3. Message routing and processing
   4. Automatic state tracking via reducers
   5. Conversation initialization and conclusion
   6. Extension points for specialized conversation behaviors

   The conversation flow follows a standard pattern:
   initialize → select_speaker → execute_agent → process_response → check_end → conclude

   Each conversation type extends this base by implementing the abstract methods,
   particularly the `select_speaker` method that defines the conversation pattern.


   .. autolink-examples:: agents.conversation.base.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.conversation.base.agent.logger


Classes
-------

.. autoapisummary::

   agents.conversation.base.agent.BaseConversationAgent


Module Contents
---------------

.. py:class:: BaseConversationAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Base conversation agent that orchestrates multi-agent conversations.

   This abstract base class provides the core functionality for managing
   conversations between multiple agents, with hooks for customization.

   The BaseConversationAgent implements a graph-based conversation flow
   that all specialized conversation types extend and customize. It handles
   agent compilation, message routing, state tracking, and conversation
   lifecycle management.

   .. attribute:: participant_agents

      Mapping of participant names to agent instances or configs.

      :type: Dict[str, Union[SimpleAgent, AugLLMConfig]]

   .. attribute:: topic

      The conversation topic.

      :type: str

   .. attribute:: max_rounds

      Maximum number of conversation rounds.

      :type: int

   .. attribute:: mode

      Conversation mode identifier (e.g., "round_robin", "debate").

      :type: str

   .. attribute:: recursion_limit

      Maximum recursion depth for agent execution.

      :type: int

   .. attribute:: handle_errors

      Whether to handle agent execution errors gracefully.

      :type: bool

   .. attribute:: max_turns_safety

      Absolute maximum turns as a safety limit.

      :type: int

   .. note::

      This is an abstract base class. Concrete conversation types must implement
      at minimum the `select_speaker` method to define their conversation pattern.


   .. autolink-examples:: BaseConversationAgent
      :collapse:

   .. py:method:: _add_custom_graph_elements(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Hook for subclasses to add custom nodes and edges.

      Override this method to extend the graph structure.


      .. autolink-examples:: _add_custom_graph_elements
         :collapse:


   .. py:method:: _check_custom_end_conditions(state: Any) -> dict[str, Any] | None

      Check custom end conditions. Override in subclasses.


      .. autolink-examples:: _check_custom_end_conditions
         :collapse:


   .. py:method:: _compile_participants()

      Compile all participant agents.


      .. autolink-examples:: _compile_participants
         :collapse:


   .. py:method:: _create_initial_message() -> langchain_core.messages.BaseMessage

      Create the initial conversation message.


      .. autolink-examples:: _create_initial_message
         :collapse:


   .. py:method:: _create_orchestrator_engine() -> haive.core.engine.aug_llm.AugLLMConfig

      Create the default orchestrator engine.


      .. autolink-examples:: _create_orchestrator_engine
         :collapse:


   .. py:method:: _custom_initialization(state: Any) -> dict[str, Any]

      Hook for custom initialization. Override in subclasses.


      .. autolink-examples:: _custom_initialization
         :collapse:


   .. py:method:: _extract_agent_messages(result: Any, input_messages: list[langchain_core.messages.BaseMessage]) -> list[langchain_core.messages.BaseMessage]

      Extract new messages from agent result.


      .. autolink-examples:: _extract_agent_messages
         :collapse:


   .. py:method:: _handle_agent_error(error: Exception, agent_name: str) -> langgraph.types.Command

      Handle errors from agent execution.


      .. autolink-examples:: _handle_agent_error
         :collapse:


   .. py:method:: _prepare_agent_input(state: Any, agent_name: str) -> dict[str, Any]

      Prepare input for an agent. Override for custom behavior.


      .. autolink-examples:: _prepare_agent_input
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the conversation graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: check_end(state: Any) -> langgraph.types.Command

      Check if conversation should end.


      .. autolink-examples:: check_end
         :collapse:


   .. py:method:: conclude_conversation(state: Any) -> langgraph.types.Command

      Create final conclusion for the conversation.


      .. autolink-examples:: conclude_conversation
         :collapse:


   .. py:method:: convert_persistence_boolean(values: dict[str, Any]) -> dict[str, Any]
      :classmethod:


      Convert persistence=True to actual persistence configuration.


      .. autolink-examples:: convert_persistence_boolean
         :collapse:


   .. py:method:: create(participants: dict[str, haive.agents.simple.agent.SimpleAgent | haive.core.engine.aug_llm.AugLLMConfig], **kwargs) -> BaseConversationAgent
      :classmethod:


      Create a conversation with participants.


      .. autolink-examples:: create
         :collapse:


   .. py:method:: execute_agent(state: Any) -> langgraph.types.Command

      Execute the current speaker's agent.


      .. autolink-examples:: execute_agent
         :collapse:


   .. py:method:: get_conversation_state_schema() -> type

      Get the state schema for this conversation type.

      Override in subclasses to provide custom state schemas.


      .. autolink-examples:: get_conversation_state_schema
         :collapse:


   .. py:method:: get_input_fields() -> dict[str, tuple[type, Any]]

      Define input fields.


      .. autolink-examples:: get_input_fields
         :collapse:


   .. py:method:: get_output_fields() -> dict[str, tuple[type, Any]]

      Define output fields.


      .. autolink-examples:: get_output_fields
         :collapse:


   .. py:method:: initialize_conversation(state: Any) -> langgraph.types.Command

      Initialize the conversation.


      .. autolink-examples:: initialize_conversation
         :collapse:


   .. py:method:: process_response(state: Any) -> langgraph.types.Command

      Process the agent's response.

      Override in subclasses to add custom response processing.


      .. autolink-examples:: process_response
         :collapse:


   .. py:method:: select_speaker(state: Any) -> langgraph.types.Command
      :abstractmethod:


      Select the next speaker in the conversation.

      This is the primary method that defines the conversation pattern and must
      be implemented by all conversation type subclasses. It determines which
      participant should speak next based on the current conversation state.

      The implementation of this method defines the fundamental behavior of each
      conversation type. For example:
      - Round-robin conversations select speakers in a fixed rotating order
      - Debate conversations select based on debate phase and structure
      - Directed conversations use a moderator to select the next speaker

      :param state: The current conversation state, containing speakers,
                    message history, and conversation metadata.
      :type state: Any

      :returns:

                A langgraph Command object with state updates. Must include either:
                    - update={"current_speaker": speaker_name} to continue conversation
                    - update={"current_speaker": None, "conversation_ended": True} to end
      :rtype: Command

      :raises NotImplementedError: If not implemented by a subclass.

      .. note::

         This is the core method that differentiates conversation types. Each
         subclass must implement this method to define its unique conversation pattern.


      .. autolink-examples:: select_speaker
         :collapse:


   .. py:method:: setup_agent() -> None

      Set up the conversation orchestrator.

      This method performs critical initialization steps for the conversation agent:

      1. Configures the state schema for conversation tracking
      2. Creates a default orchestrator engine if none is provided
      3. Compiles all participant agents to ensure they're ready for execution
      4. Sets up persistence if persistence=True was passed

      This method is called automatically during the agent's lifecycle and
      should rarely need to be called directly.

      :returns: None


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: _compiled_agents
      :type:  dict[str, haive.agents.simple.agent.SimpleAgent]
      :value: None



   .. py:attribute:: handle_errors
      :type:  bool
      :value: None



   .. py:attribute:: max_rounds
      :type:  int
      :value: None



   .. py:attribute:: max_turns_safety
      :type:  int
      :value: None



   .. py:attribute:: mode
      :type:  str
      :value: None



   .. py:attribute:: participant_agents
      :type:  dict[str, haive.agents.simple.agent.SimpleAgent | haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: recursion_limit
      :type:  int
      :value: None



   .. py:attribute:: topic
      :type:  str
      :value: None



.. py:data:: logger

