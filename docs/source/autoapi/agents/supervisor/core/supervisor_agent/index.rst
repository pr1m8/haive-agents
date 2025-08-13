
:py:mod:`agents.supervisor.core.supervisor_agent`
=================================================

.. py:module:: agents.supervisor.core.supervisor_agent

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

Classes
-------

.. autoapisummary::

   agents.supervisor.core.supervisor_agent.SupervisorAgent
   agents.supervisor.core.supervisor_agent.SupervisorState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorAgent {
        node [shape=record];
        "SupervisorAgent" [label="SupervisorAgent"];
        "haive.agents.react.agent.ReactAgent" -> "SupervisorAgent";
      }

.. autoclass:: agents.supervisor.core.supervisor_agent.SupervisorAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SupervisorState:

   .. graphviz::
      :align: center

      digraph inheritance_SupervisorState {
        node [shape=record];
        "SupervisorState" [label="SupervisorState"];
        "pydantic.BaseModel" -> "SupervisorState";
      }

.. autopydantic_model:: agents.supervisor.core.supervisor_agent.SupervisorState
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. rubric:: Related Links

.. autolink-examples:: agents.supervisor.core.supervisor_agent
   :collapse:
   
.. autolink-skip:: next
