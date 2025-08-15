enhanced_react_agent.v2
=======================

.. py:module:: enhanced_react_agent.v2

.. autoapi-nested-parse::

   Enhanced ReactAgent implementation using Agent[AugLLMConfig].

   ReactAgent = Agent[AugLLMConfig] + reasoning loop with tools.


   .. autolink-examples:: enhanced_react_agent.v2
      :collapse:


Attributes
----------

.. autoapisummary::

   enhanced_react_agent.v2.logger


Classes
-------

.. autoapisummary::

   enhanced_react_agent.v2.ReactAgent


Module Contents
---------------

.. py:class:: ReactAgent

   Bases: :py:obj:`haive.agents.simple.enhanced_simple_real.EnhancedAgentBase`


   Enhanced ReactAgent with reasoning and action loop.

   ReactAgent = Agent[AugLLMConfig] + reasoning loop with tools.

   The ReAct pattern (Reasoning and Acting) allows the agent to:
   1. Reason about what action to take
   2. Take the action (use a tool)
   3. Observe the result
   4. Reason again based on the observation
   5. Continue until task is complete

   .. attribute:: max_iterations

      Maximum reasoning iterations (default: 10)

   .. attribute:: tools

      List of tools available to the agent

   .. attribute:: react_prompt

      Optional custom prompt for ReAct pattern

   .. rubric:: Examples

   Basic usage::

       from langchain_core.tools import tool

       @tool
       def calculator(expression: str) -> str:
           '''Calculate math expressions'''
           return str(eval(expression))

       agent = ReactAgent(
           name="math_agent",
           tools=[calculator],
           engine=AugLLMConfig()
       )

       result = agent.run("What is 15 * 23 + 7?")

   With multiple tools::

       agent = ReactAgent(
           name="research_agent",
           tools=[web_search, calculator, file_reader],
           max_iterations=15,
           react_prompt="You are a research assistant..."
       )


   .. autolink-examples:: ReactAgent
      :collapse:

   .. py:method:: _get_react_prompt() -> str

      Get the ReAct system prompt.


      .. autolink-examples:: _get_react_prompt
         :collapse:


   .. py:method:: add_tool(tool: langchain_core.tools.BaseTool) -> None

      Add a tool to the agent's toolkit.

      :param tool: The tool to add


      .. autolink-examples:: add_tool
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build the ReAct reasoning graph.

      Creates a graph with:
      1. Reasoning node - decides what action to take
      2. Tool node - executes the selected tool
      3. Observation node - processes tool results
      4. Decision routing - continue or finish


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: get_reasoning_summary() -> str

      Get a summary of the reasoning process.


      .. autolink-examples:: get_reasoning_summary
         :collapse:


   .. py:method:: get_tool_names() -> list[str]

      Get list of available tool names.


      .. autolink-examples:: get_tool_names
         :collapse:


   .. py:method:: record_reasoning_step(thought: str, action: str | None = None, observation: str | None = None) -> None

      Record a reasoning step.

      :param thought: The reasoning thought
      :param action: The action taken (if any)
      :param observation: The observation made (if any)


      .. autolink-examples:: record_reasoning_step
         :collapse:


   .. py:method:: remove_tool(tool_name: str) -> bool

      Remove a tool by name.

      :param tool_name: Name of the tool to remove

      :returns: True if tool was removed, False if not found
      :rtype: bool


      .. autolink-examples:: remove_tool
         :collapse:


   .. py:method:: reset_reasoning() -> None

      Reset the reasoning history.


      .. autolink-examples:: reset_reasoning
         :collapse:


   .. py:method:: validate_react_config() -> ReactAgent

      Validate ReactAgent configuration.


      .. autolink-examples:: validate_react_config
         :collapse:


   .. py:attribute:: execution_mode
      :type:  Literal['react', 'tool-calling', 'hybrid']
      :value: None



   .. py:attribute:: max_iterations
      :type:  int
      :value: None



   .. py:attribute:: react_prompt
      :type:  str | None
      :value: None



   .. py:attribute:: reasoning_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: tools
      :type:  list[langchain_core.tools.BaseTool]
      :value: None



.. py:data:: logger

