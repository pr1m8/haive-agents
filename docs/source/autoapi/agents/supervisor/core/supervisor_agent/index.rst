agents.supervisor.core.supervisor_agent
=======================================

.. py:module:: agents.supervisor.core.supervisor_agent

.. autoapi-nested-parse::

   SupervisorAgent - Basic supervisor with intelligent routing.

   This module provides the SupervisorAgent class, which acts as an orchestrator
   for multiple specialized agents. It uses LLM-based reasoning to analyze tasks
   and route them to the most appropriate agent.

   **Current Status**: This is the **basic supervisor** implementation. For dynamic
   agent management capabilities, use DynamicSupervisor. For simple routing without
   ReactAgent overhead, use SimpleSupervisor.

   The SupervisorAgent extends ReactAgent to leverage its looping behavior for
   continuous routing decisions across multi-turn conversations.

   Key Features:
       - **LLM-based routing**: Intelligent task analysis and agent selection
       - **Agent registration**: Register specialized agents with descriptions
       - **Tool aggregation**: Automatically collects tools from registered agents
       - **Conversation tracking**: Maintains context across interactions
       - **Custom routing**: Override route_to_agent() for custom logic
       - **ReactAgent base**: Inherits looping and tool execution capabilities

   Architecture:
       1. User sends query to supervisor
       2. Supervisor analyzes query and conversation history
       3. LLM makes routing decision based on agent capabilities
       4. Query forwarded to selected agent
       5. Agent response returned through supervisor
       6. Loop continues for multi-turn conversations

   .. rubric:: Example

   Basic supervisor setup::

       >>> from haive.agents.supervisor import SupervisorAgent
       >>> from haive.agents.simple import SimpleAgent
       >>> from haive.core.engine.aug_llm import AugLLMConfig
       >>>
       >>> # Create specialized agents
       >>> writer = SimpleAgent(
       ...     name="writer",
       ...     engine=AugLLMConfig(),
       ...     system_message="You are an expert writer"
       ... )
       >>>
       >>> researcher = SimpleAgent(
       ...     name="researcher",
       ...     engine=AugLLMConfig(),
       ...     system_message="You are a research specialist"
       ... )
       >>>
       >>> # Create supervisor
       >>> supervisor = SupervisorAgent(
       ...     name="project_manager",
       ...     engine=AugLLMConfig(temperature=0.3),
       ...     registered_agents={
       ...         "writer": writer,
       ...         "researcher": researcher
       ...     }
       ... )
       >>>
       >>> # Supervisor automatically routes to appropriate agent
       >>> result = await supervisor.arun("Research AI trends and write a summary")

   Custom routing logic::

       >>> class PrioritySupervisor(SupervisorAgent):
       ...     def route_to_agent(self, query: str) -> str:
       ...         # Custom routing for priority tasks
       ...         if "urgent" in query.lower():
       ...             return "priority_handler"
       ...         # Fall back to LLM routing
       ...         return super().route_to_agent(query)

   .. seealso::

      - :class:`haive.agents.supervisor.DynamicSupervisor`: For runtime agent management
      - :class:`haive.agents.supervisor.SimpleSupervisor`: For lightweight routing
      - :class:`haive.agents.react.agent.ReactAgent`: Base class providing loop behavior


   .. autolink-examples:: agents.supervisor.core.supervisor_agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.supervisor.core.supervisor_agent.DEFAULT_SUPERVISOR_PROMPT
   agents.supervisor.core.supervisor_agent.logger


Classes
-------

.. autoapisummary::

   agents.supervisor.core.supervisor_agent.SupervisorAgent
   agents.supervisor.core.supervisor_agent.SupervisorState


Module Contents
---------------

.. py:class:: SupervisorAgent

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Supervisor agent that routes between multiple specialized agents.

   Extends ReactAgent to leverage its looping behavior for continuous
   routing decisions based on conversation context.


   .. autolink-examples:: SupervisorAgent
      :collapse:

   .. py:method:: _create_routing_prompt() -> langchain_core.prompts.ChatPromptTemplate

      Create routing prompt with current agent descriptions.


      .. autolink-examples:: _create_routing_prompt
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build supervisor graph with agent routing.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_with_agents(agents: list[tuple[str, haive.agents.base.Agent, str]], name: str = 'supervisor', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, **kwargs) -> SupervisorAgent
      :classmethod:


      Create supervisor with pre-registered agents.

      :param agents: List of (name, agent, description) tuples
      :param name: Supervisor name
      :param engine: Custom engine config
      :param \*\*kwargs: Additional arguments

      :returns: Configured SupervisorAgent

      .. rubric:: Example

      supervisor = SupervisorAgent.create_with_agents([
          ("writer", writer_agent, "Creative writing tasks"),
          ("coder", coder_agent, "Programming tasks"),
          ("analyst", analyst_agent, "Data analysis")
      ])


      .. autolink-examples:: create_with_agents
         :collapse:


   .. py:method:: ensure_supervisor_engine(v)
      :classmethod:


      Ensure supervisor has a low-temperature engine for routing.


      .. autolink-examples:: ensure_supervisor_engine
         :collapse:


   .. py:method:: register_agent(name: str, agent: haive.agents.base.Agent, description: str) -> None

      Register an agent with the supervisor.

      :param name: Unique name for the agent
      :param agent: The agent instance
      :param description: Description of capabilities


      .. autolink-examples:: register_agent
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup supervisor with routing configuration.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:method:: unregister_agent(name: str) -> None

      Remove an agent from supervision.


      .. autolink-examples:: unregister_agent
         :collapse:


   .. py:attribute:: agent_descriptions
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: registered_agents
      :type:  dict[str, haive.agents.base.Agent]
      :value: None



   .. py:attribute:: supervisor_prompt
      :type:  langchain_core.prompts.ChatPromptTemplate | None
      :value: None



.. py:class:: SupervisorState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for supervisor operations.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SupervisorState
      :collapse:

   .. py:attribute:: messages
      :type:  list[Any]
      :value: None



   .. py:attribute:: routing_decision
      :type:  str | None
      :value: None



   .. py:attribute:: target_agent
      :type:  str | None
      :value: None



.. py:data:: DEFAULT_SUPERVISOR_PROMPT

.. py:data:: logger

