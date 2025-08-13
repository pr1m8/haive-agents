
:py:mod:`agents.supervisor.core.simple_supervisor`
==================================================

.. py:module:: agents.supervisor.core.simple_supervisor

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

Classes
-------

.. autoapisummary::

   agents.supervisor.core.simple_supervisor.AgentInfo
   agents.supervisor.core.simple_supervisor.SimpleSupervisor


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AgentInfo:

   .. graphviz::
      :align: center

      digraph inheritance_AgentInfo {
        node [shape=record];
        "AgentInfo" [label="AgentInfo"];
        "pydantic.BaseModel" -> "AgentInfo";
      }

.. autopydantic_model:: agents.supervisor.core.simple_supervisor.AgentInfo
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SimpleSupervisor:

   .. graphviz::
      :align: center

      digraph inheritance_SimpleSupervisor {
        node [shape=record];
        "SimpleSupervisor" [label="SimpleSupervisor"];
        "haive.agents.multi.archive.multi_agent.MultiAgent" -> "SimpleSupervisor";
      }

.. autoclass:: agents.supervisor.core.simple_supervisor.SimpleSupervisor
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.supervisor.core.simple_supervisor
   :collapse:
   
.. autolink-skip:: next
