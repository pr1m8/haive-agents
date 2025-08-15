agents.planning.base.agents.executor
====================================

.. py:module:: agents.planning.base.agents.executor

.. autoapi-nested-parse::

   Base Executor Agent - Task execution agent with tavily search capabilities.

   This module provides the foundational executor agent designed to carry out
   specific steps from plans using available tools, particularly search capabilities.


   .. autolink-examples:: agents.planning.base.agents.executor
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.base.agents.executor.BaseExecutorAgent


Functions
---------

.. autoapisummary::

   agents.planning.base.agents.executor.create_base_executor
   agents.planning.base.agents.executor.create_research_executor


Module Contents
---------------

.. py:class:: BaseExecutorAgent

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Base executor agent with comprehensive execution capabilities.

   This agent specializes in executing specific steps from plans, using tools
   effectively to accomplish tasks with precision and thoroughness.

   Features:
   - Comprehensive search capabilities via Tavily
   - Detailed execution reporting
   - Tool usage optimization
   - Quality assurance and validation
   - Progress tracking and recommendations

   .. rubric:: Examples

   Basic execution:

       executor = BaseExecutorAgent()
       result = await executor.arun("Search for current AI trends")

   Custom configuration:

       executor = BaseExecutorAgent(
           name="research_executor",
           engine=AugLLMConfig(
               model="gpt-4",
               temperature=0.1,
               system_message="Expert research execution specialist"
           ),
           tools=[tavily_search_tool, custom_tool]
       )
       result = await executor.arun("Execute research step 3")


   .. autolink-examples:: BaseExecutorAgent
      :collapse:

   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate
      :value: None



   .. py:attribute:: tools
      :type:  list
      :value: None



.. py:function:: create_base_executor(name: str = 'base_executor', model: str = 'gpt-4o-mini', temperature: float = 0.1, additional_tools: list | None = None) -> BaseExecutorAgent

   Create a base executor agent with default configuration.

   :param name: Name for the executor agent
   :param model: LLM model to use for execution
   :param temperature: Sampling temperature (lower = more focused execution)
   :param additional_tools: Extra tools to add beyond default search tools

   :returns: Configured executor ready for task execution
   :rtype: BaseExecutorAgent

   .. rubric:: Examples

   Basic executor:

       executor = create_base_executor()

   Custom executor with additional tools:

       from haive.tools.tools import calculator_tool
       executor = create_base_executor(
           name="research_executor",
           model="gpt-4",
           temperature=0.05,
           additional_tools=[calculator_tool]
       )


   .. autolink-examples:: create_base_executor
      :collapse:

.. py:function:: create_research_executor(name: str = 'research_executor') -> BaseExecutorAgent

   Create a specialized executor optimized for research tasks.

   This creates an executor specifically tuned for research and information
   gathering tasks with enhanced search capabilities.

   :returns: Executor optimized for research execution
   :rtype: BaseExecutorAgent


   .. autolink-examples:: create_research_executor
      :collapse:

