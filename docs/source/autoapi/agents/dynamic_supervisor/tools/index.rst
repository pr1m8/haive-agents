
:py:mod:`agents.dynamic_supervisor.tools`
=========================================

.. py:module:: agents.dynamic_supervisor.tools

Dynamic tool generation for supervisor agent.

This module handles the creation of dynamic tools based on registered agents.
It generates handoff tools for each agent and a choice validation tool.

Functions:
    create_agent_tools: Generate all tools from supervisor state
    create_handoff_tool: Create a handoff tool for a specific agent
    create_choice_tool: Create the agent choice validation tool

.. rubric:: Example

Generating tools from state::

    state = SupervisorStateWithTools()
    state.add_agent("search", agent, "Search expert")

    tools = create_agent_tools(state)
    # Returns: [handoff_to_search, choose_agent]


.. autolink-examples:: agents.dynamic_supervisor.tools
   :collapse:


Functions
---------

.. autoapisummary::

   agents.dynamic_supervisor.tools.create_add_agent_tool
   agents.dynamic_supervisor.tools.create_agent_tools
   agents.dynamic_supervisor.tools.create_choice_tool
   agents.dynamic_supervisor.tools.create_handoff_tool

.. py:function:: create_add_agent_tool() -> Any

   Create tool for requesting a new agent be added.

   This tool allows the supervisor to formally request a new agent
   when it identifies a missing capability. In a full implementation,
   this would interface with an agent builder or registry service.

   :returns: Add agent request tool

   .. rubric:: Example

   Requesting a new agent::

       tool = create_add_agent_tool()
       tool.invoke({
           "capability": "translation",
           "reason": "Need to translate results to French"
       })


   .. autolink-examples:: create_add_agent_tool
      :collapse:

.. py:function:: create_agent_tools(state: haive.agents.dynamic_supervisor.state.SupervisorStateWithTools) -> list[Any]

   Generate all tools from current agents in state.

   Creates handoff tools for each registered agent and a choice validation tool.
   Tools are generated dynamically based on the current agent registry.

   :param state: Supervisor state with agent registry

   :returns: List of tool instances ready for use

   .. rubric:: Example

   Getting tools for supervisor::

       tools = create_agent_tools(state)
       # Use tools in an engine or pass to LLM


   .. autolink-examples:: create_agent_tools
      :collapse:

.. py:function:: create_choice_tool(state: haive.agents.dynamic_supervisor.state.SupervisorStateWithTools) -> Any

   Create agent choice validation tool.

   This tool provides validated agent selection with dynamic options
   based on the current agent registry. It includes "END" as an option
   for when no suitable agent exists.

   :param state: Supervisor state instance

   :returns: Choice validation tool

   .. rubric:: Example

   Using the choice tool::

       tool = create_choice_tool(state)
       result = tool.invoke({"agent": "search_agent"})


   .. autolink-examples:: create_choice_tool
      :collapse:

.. py:function:: create_handoff_tool(state: haive.agents.dynamic_supervisor.state.SupervisorStateWithTools, agent_name: str) -> Any

   Create a handoff tool for a specific agent.

   The handoff tool executes the agent directly and returns results,
   following the pattern from our experimental implementation.

   :param state: Supervisor state instance
   :param agent_name: Name of the agent to create tool for

   :returns: Tool instance for handing off to the agent

   .. rubric:: Example

   Creating a handoff tool::

       tool = create_handoff_tool(state, "search_agent")
       # Creates: handoff_to_search_agent tool


   .. autolink-examples:: create_handoff_tool
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.dynamic_supervisor.tools
   :collapse:
   
.. autolink-skip:: next
