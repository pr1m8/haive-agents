agents.planning.base.agents.planner
===================================

.. py:module:: agents.planning.base.agents.planner

.. autoapi-nested-parse::

   Base Planner Agent - Sophisticated planning agent with comprehensive system prompt.

   This module provides the foundational planner agent with an extensive system prompt
   designed for creating detailed, actionable plans with thorough analysis and reasoning.


   .. autolink-examples:: agents.planning.base.agents.planner
      :collapse:


Classes
-------

.. autoapisummary::

   agents.planning.base.agents.planner.BasePlannerAgent


Functions
---------

.. autoapisummary::

   agents.planning.base.agents.planner.create_base_planner
   agents.planning.base.agents.planner.create_conversation_summary_planner


Module Contents
---------------

.. py:class:: BasePlannerAgent

   Bases: :py:obj:`SimpleAgentV3`


   Base planner agent with comprehensive planning capabilities.

   This agent specializes in creating detailed, strategic plans by breaking down
   complex objectives into clear, actionable steps with thorough analysis.

   Features:
   - Comprehensive objective analysis
   - Detailed step-by-step planning
   - Risk assessment and mitigation
   - Resource and tool identification
   - Timeline and dependency management
   - Success criteria definition

   .. rubric:: Examples

   Basic planning:

       planner = BasePlannerAgent()
       plan = await planner.arun("Create a comprehensive business plan")

   Custom configuration:

       planner = BasePlannerAgent(
           name="strategic_planner",
           engine=AugLLMConfig(
               model="gpt-4",
               temperature=0.2,
               system_message="Expert strategic planning specialist"
           )
       )
       plan = await planner.arun("Launch new product line")


   .. autolink-examples:: BasePlannerAgent
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



   .. py:attribute:: structured_output_model
      :value: None



.. py:function:: create_base_planner(name: str = 'base_planner', model: str = 'gpt-4o-mini', temperature: float = 0.3, structured_output_model=None) -> BasePlannerAgent

   Create a base planner agent with default configuration.

   :param name: Name for the planner agent
   :param model: LLM model to use for planning
   :param temperature: Sampling temperature for planning (lower = more focused)
   :param structured_output_model: Custom output model (defaults to BasePlan)

   :returns: Configured planner ready for use
   :rtype: BasePlannerAgent

   .. rubric:: Examples

   Basic planner:

       planner = create_base_planner()

   Custom planner:

       planner = create_base_planner(
           name="strategic_planner",
           model="gpt-4",
           temperature=0.2
       )


   .. autolink-examples:: create_base_planner
      :collapse:

.. py:function:: create_conversation_summary_planner(name: str = 'conversation_planner') -> BasePlannerAgent

   Create a specialized planner for conversation summary tasks.

   This creates a planner specifically tuned for analyzing conversations
   and creating detailed summaries with strategic planning approach.

   :returns: Planner optimized for conversation analysis
   :rtype: BasePlannerAgent


   .. autolink-examples:: create_conversation_summary_planner
      :collapse:

