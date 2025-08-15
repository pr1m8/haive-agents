agents.supervisor.core.simple_supervisor
========================================

.. py:module:: agents.supervisor.core.simple_supervisor

.. autoapi-nested-parse::

   SimpleSupervisor - Lightweight supervisor for basic routing needs.

   This module provides the SimpleSupervisor class, a lightweight alternative to
   SupervisorAgent that extends MultiAgent instead of ReactAgent. It's designed
   for scenarios where you need simple routing without the overhead of ReactAgent's
   looping behavior.

   **Current Status**: This is a **lightweight supervisor** for simple use cases.
   For full-featured supervision with tool execution, use SupervisorAgent. For
   dynamic agent management, use DynamicSupervisor.

   The SimpleSupervisor uses an LLM to make routing decisions but executes in a
   single pass without the continuous looping of ReactAgent-based supervisors.

   Key Features:
       - **Lightweight design**: Extends MultiAgent for minimal overhead
       - **Single-pass execution**: No continuous looping
       - **LLM routing**: Intelligent agent selection
       - **Clean API**: Simple agent registration with descriptions
       - **Custom prompts**: Configurable routing prompts
       - **Direct execution**: Routes and executes in one step

   Use Cases:
       - Simple request routing to specialized agents
       - One-shot task delegation
       - Lightweight agent coordination
       - When ReactAgent features aren't needed

   .. rubric:: Example

   Basic routing setup::

       >>> from haive.agents.supervisor import SimpleSupervisor
       >>> from haive.agents.simple import SimpleAgent
       >>> from haive.core.engine.aug_llm import AugLLMConfig
       >>>
       >>> # Create specialized agents
       >>> calculator = SimpleAgent(name="calculator", engine=config)
       >>> writer = SimpleAgent(name="writer", engine=config)
       >>>
       >>> # Create simple supervisor
       >>> supervisor = SimpleSupervisor(
       ...     name="router",
       ...     engine=AugLLMConfig(temperature=0.3),
       ...     agents={
       ...         "calculator": AgentInfo(
       ...             agent=calculator,
       ...             description="Handles math and calculations"
       ...         ),
       ...         "writer": AgentInfo(
       ...             agent=writer,
       ...             description="Handles writing and content creation"
       ...         )
       ...     }
       ... )
       >>>
       >>> # Single-pass routing and execution
       >>> result = await supervisor.arun("Calculate 15% of 200")

   Custom routing prompt::

       >>> custom_prompt = ChatPromptTemplate.from_template(
       ...     "Route this request to the best agent: {query}\\n"
       ...     "Agents: {agent_descriptions}\\n"
       ...     "Choice:"
       ... )
       >>>
       >>> supervisor = SimpleSupervisor(
       ...     name="custom_router",
       ...     engine=config,
       ...     prompt_template=custom_prompt,
       ...     agents={...}
       ... )

   .. seealso::

      - :class:`haive.agents.supervisor.SupervisorAgent`: Full-featured supervisor
      - :class:`haive.agents.supervisor.DynamicSupervisor`: Dynamic agent management
      - :class:`haive.agents.multi.MultiAgent`: Base class


   .. autolink-examples:: agents.supervisor.core.simple_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.supervisor.core.simple_supervisor.DEFAULT_SUPERVISOR_PROMPT
   agents.supervisor.core.simple_supervisor.logger


Classes
-------

.. autoapisummary::

   agents.supervisor.core.simple_supervisor.AgentInfo
   agents.supervisor.core.simple_supervisor.SimpleSupervisor


Module Contents
---------------

.. py:class:: AgentInfo(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Information about a registered agent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AgentInfo
      :collapse:

   .. py:attribute:: agent
      :type:  haive.agents.base.Agent
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



.. py:class:: SimpleSupervisor

   Bases: :py:obj:`haive.agents.multi.archive.multi_agent.MultiAgent`


   Simple supervisor that routes between agents using LLM decisions.

   This supervisor:
   1. Accepts a user message
   2. Uses an LLM to decide which agent should handle it
   3. Routes to that agent
   4. Returns the agent's response

   The routing decision is based on agent descriptions and conversation context.


   .. autolink-examples:: SimpleSupervisor
      :collapse:

   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build supervisor graph with dynamic routing.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: create_with_agents(agents: list[tuple[str, haive.agents.base.Agent, str]], name: str = 'supervisor', supervisor_llm: haive.core.engine.aug_llm.AugLLMConfig | None = None, **kwargs) -> SimpleSupervisor
      :classmethod:


      Create supervisor with a list of agents.

      :param agents: List of (name, agent, description) tuples
      :param name: Supervisor name
      :param supervisor_llm: LLM for routing decisions
      :param \*\*kwargs: Additional arguments

      :returns: SimpleSupervisor instance

      .. rubric:: Example

      supervisor = SimpleSupervisor.create_with_agents([
          ("writer", writer_agent, "Writes creative content"),
          ("coder", coder_agent, "Writes and reviews code"),
          ("analyst", analyst_agent, "Analyzes data and trends")
      ])


      .. autolink-examples:: create_with_agents
         :collapse:


   .. py:method:: register_agent(name: str, agent: haive.agents.base.Agent, description: str) -> None

      Register an agent with the supervisor.

      :param name: Unique name for the agent
      :param agent: The agent instance
      :param description: Description of agent capabilities


      .. autolink-examples:: register_agent
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup supervisor with routing LLM.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: agent_info
      :type:  dict[str, AgentInfo]
      :value: None



   .. py:attribute:: supervisor_llm
      :type:  haive.core.engine.aug_llm.AugLLMConfig | None
      :value: None



   .. py:attribute:: supervisor_prompt
      :type:  langchain_core.prompts.ChatPromptTemplate | None
      :value: None



.. py:data:: DEFAULT_SUPERVISOR_PROMPT

.. py:data:: logger

