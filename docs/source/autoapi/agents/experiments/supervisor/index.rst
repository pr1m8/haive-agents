
:py:mod:`agents.experiments.supervisor`
=======================================

.. py:module:: agents.experiments.supervisor

Supervisor module for managing multi-agent systems.

This module provides a complete supervisor implementation that can manage
multiple agents, handle tool synchronization, and support dynamic agent creation.

Key Components:
    - BaseSupervisor: Core supervisor using ReactAgent
    - DynamicSupervisor: Extended supervisor with agent creation
    - SupervisorState: State model with agent registry
    - DynamicSupervisorState: Extended state for dynamic capabilities

Example Usage:
    Basic supervisor::

        from haive.agents.experiments.supervisor import BaseSupervisor
        from haive.agents.simple.agent import SimpleAgent

        # Create supervisor
        supervisor = BaseSupervisor(name="my_supervisor", engine=my_engine)

        # Register agents
        research_agent = SimpleAgent(name="researcher", engine=research_engine)
        supervisor.register_agent("research", "Research specialist", research_agent)

        # Use supervisor
        result = supervisor.invoke("Research quantum computing trends")

    Dynamic supervisor::

        from haive.agents.experiments.supervisor import DynamicSupervisor

        supervisor = DynamicSupervisor(name="dynamic_super", engine=my_engine)
        supervisor.enable_agent_creation()

        # Can create agents on the fly via tool calls
        result = supervisor.invoke("Create a coding agent and write Python code")


.. autolink-examples:: agents.experiments.supervisor
   :collapse:




