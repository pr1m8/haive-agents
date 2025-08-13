
:py:mod:`agents.dynamic_supervisor.agent`
=========================================

.. py:module:: agents.dynamic_supervisor.agent

Dynamic Supervisor Agent implementation.

This module contains the main DynamicSupervisorAgent class that extends
SimpleAgent to provide dynamic agent management capabilities.

Classes:
    DynamicSupervisorAgent: Main supervisor implementation

Functions:
    create_dynamic_supervisor: Factory function for creating supervisors

.. rubric:: Example

Creating a dynamic supervisor::

    from haive.agents.dynamic_supervisor import DynamicSupervisorAgent
    from haive.core.engine import AugLLMConfig

    supervisor = DynamicSupervisorAgent(
        name="task_router",
        engine=supervisor_engine,
        enable_agent_builder=True
    )

    # Run with initial agents
    state = supervisor.create_initial_state()
    state.add_agent("search", search_agent, "Search expert")

    result = await supervisor.arun(
        "Find information about Paris and translate to French",
        state=state
    )


.. autolink-examples:: agents.dynamic_supervisor.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.dynamic_supervisor.agent.DynamicSupervisorAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DynamicSupervisorAgent:

   .. graphviz::
      :align: center

      digraph inheritance_DynamicSupervisorAgent {
        node [shape=record];
        "DynamicSupervisorAgent" [label="DynamicSupervisorAgent"];
        "haive.agents.react.agent.ReactAgent" -> "DynamicSupervisorAgent";
      }

.. autoclass:: agents.dynamic_supervisor.agent.DynamicSupervisorAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.dynamic_supervisor.agent.create_dynamic_supervisor

.. py:function:: create_dynamic_supervisor(name: str = 'supervisor', model: str = 'gpt-4', temperature: float = 0.0, force_tool_use: bool = True, enable_agent_builder: bool = False, **kwargs) -> DynamicSupervisorAgent

   Factory function to create a configured dynamic supervisor.

   :param name: Supervisor name
   :param model: LLM model to use
   :param temperature: LLM temperature (0.0 for deterministic)
   :param force_tool_use: Whether to force tool usage
   :param enable_agent_builder: Enable agent request capability
   :param \*\*kwargs: Additional arguments for supervisor

   :returns: Configured DynamicSupervisorAgent instance

   .. rubric:: Example

   Quick supervisor creation::

       supervisor = create_dynamic_supervisor(
           name="task_coordinator",
           model="gpt-4",
           enable_agent_builder=True
       )


   .. autolink-examples:: create_dynamic_supervisor
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.dynamic_supervisor.agent
   :collapse:
   
.. autolink-skip:: next
