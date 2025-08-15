agents.reflection.agent
=======================

.. py:module:: agents.reflection.agent

.. autoapi-nested-parse::

   Reflection agents using generic pre/post hook pattern.


   .. autolink-examples:: agents.reflection.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reflection.agent.TMainAgent
   agents.reflection.agent.TPostAgent
   agents.reflection.agent.TPreAgent


Classes
-------

.. autoapisummary::

   agents.reflection.agent.ExpertAgent
   agents.reflection.agent.GradedReflectionMultiAgent
   agents.reflection.agent.GradingAgent
   agents.reflection.agent.PrePostMultiAgent
   agents.reflection.agent.ReflectionAgent
   agents.reflection.agent.ReflectionMultiAgent
   agents.reflection.agent.StructuredOutputMultiAgent
   agents.reflection.agent.ToolBasedReflectionAgent


Functions
---------

.. autoapisummary::

   agents.reflection.agent.create
   agents.reflection.agent.create_expert_agent
   agents.reflection.agent.create_graded_reflection_agent
   agents.reflection.agent.create_reflection_agent
   agents.reflection.agent.create_tool_based_reflection_agent
   agents.reflection.agent.model_post_init


Module Contents
---------------

.. py:class:: ExpertAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Agent with configurable expertise.


   .. autolink-examples:: ExpertAgent
      :collapse:

   .. py:method:: model_post_init(__context: Any) -> None

      Set up expert prompt from config.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:attribute:: expertise_config
      :type:  agents.reflection.models.ExpertiseConfig
      :value: None



.. py:class:: GradedReflectionMultiAgent

   Bases: :py:obj:`PrePostMultiAgent`\ [\ :py:obj:`haive.agents.simple.agent.SimpleAgent`\ , :py:obj:`TMainAgent`\ , :py:obj:`haive.agents.simple.agent.SimpleAgent`\ ]


   Grade → Main → Reflect pattern.

   Pattern:
   1. Main agent responds
   2. Grading agent evaluates (with structured output)
   3. Message transform for reflection
   4. Reflection agent improves based on grade


   .. autolink-examples:: GradedReflectionMultiAgent
      :collapse:

   .. py:method:: create(main_agent: TMainAgent, name: str | None = None, grading_system_prompt: str = GRADING_SYSTEM_PROMPT, reflection_system_prompt: str = REFLECTION_SYSTEM_PROMPT, **kwargs) -> GradedReflectionMultiAgent
      :classmethod:


      Create graded reflection multi-agent.


      .. autolink-examples:: create
         :collapse:


   .. py:attribute:: grading_model
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: post_agent
      :type:  haive.agents.simple.agent.SimpleAgent
      :value: None



   .. py:attribute:: post_transform_type
      :type:  haive.core.graph.node.message_transformation_v2.TransformationType
      :value: None



   .. py:attribute:: pre_agent
      :type:  haive.agents.simple.agent.SimpleAgent
      :value: None



   .. py:attribute:: use_post_transform
      :type:  bool
      :value: None



.. py:class:: GradingAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Agent that grades responses with structured output.


   .. autolink-examples:: GradingAgent
      :collapse:

   .. py:method:: model_post_init(__context: Any) -> None

      Set up grading configuration.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:attribute:: structured_output_model
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: structured_output_version
      :type:  str
      :value: None



.. py:class:: PrePostMultiAgent

   Bases: :py:obj:`haive.agents.multi.base.agent.MultiAgent`, :py:obj:`Generic`\ [\ :py:obj:`TPreAgent`\ , :py:obj:`TMainAgent`\ , :py:obj:`TPostAgent`\ ]


   Generic pre/post hook multi-agent pattern.

   This provides a general pattern for:
   - Pre-processing (optional)
   - Main processing
   - Post-processing (optional)

   With optional message transformation between stages.


   .. autolink-examples:: PrePostMultiAgent
      :collapse:

   .. py:method:: model_post_init(__context: Any) -> None

      Set up the agents list.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:attribute:: main_agent
      :type:  TMainAgent
      :value: None



   .. py:attribute:: post_agent
      :type:  TPostAgent | None
      :value: None



   .. py:attribute:: post_transform_type
      :type:  haive.core.graph.node.message_transformation_v2.TransformationType
      :value: None



   .. py:attribute:: pre_agent
      :type:  TPreAgent | None
      :value: None



   .. py:attribute:: pre_transform_type
      :type:  haive.core.graph.node.message_transformation_v2.TransformationType
      :value: None



   .. py:attribute:: skip_post_if_empty
      :type:  bool
      :value: None



   .. py:attribute:: skip_pre_if_empty
      :type:  bool
      :value: None



   .. py:attribute:: use_post_transform
      :type:  bool
      :value: None



   .. py:attribute:: use_pre_transform
      :type:  bool
      :value: None



.. py:class:: ReflectionAgent

   Bases: :py:obj:`haive.agents.simple.agent.SimpleAgent`


   Simple reflection agent for improving responses.


   .. autolink-examples:: ReflectionAgent
      :collapse:

   .. py:method:: model_post_init(__context: Any) -> None

      Set up reflection prompt.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:attribute:: reflection_mode
      :type:  str
      :value: None



.. py:class:: ReflectionMultiAgent

   Bases: :py:obj:`PrePostMultiAgent`\ [\ :py:obj:`haive.agents.base.agent.Agent`\ , :py:obj:`TMainAgent`\ , :py:obj:`haive.agents.simple.agent.SimpleAgent`\ ]


   Any agent with reflection post-processing.

   Pattern:
   1. Main agent responds
   2. Message transform (AI → Human)
   3. Reflection agent improves response


   .. autolink-examples:: ReflectionMultiAgent
      :collapse:

   .. py:method:: create(main_agent: TMainAgent, name: str | None = None, reflection_system_prompt: str = REFLECTION_SYSTEM_PROMPT, **kwargs) -> ReflectionMultiAgent
      :classmethod:


      Create reflection multi-agent.


      .. autolink-examples:: create
         :collapse:


   .. py:attribute:: post_agent
      :type:  haive.agents.simple.agent.SimpleAgent
      :value: None



   .. py:attribute:: post_transform_type
      :type:  haive.core.graph.node.message_transformation_v2.TransformationType
      :value: None



   .. py:attribute:: reflection_config
      :type:  agents.reflection.models.ReflectionConfig
      :value: None



   .. py:attribute:: use_post_transform
      :type:  bool
      :value: None



.. py:class:: StructuredOutputMultiAgent

   Bases: :py:obj:`PrePostMultiAgent`\ [\ :py:obj:`haive.agents.base.agent.Agent`\ , :py:obj:`TMainAgent`\ , :py:obj:`haive.agents.structured.StructuredOutputAgent`\ ]


   Any agent followed by structured output extraction.

   This is the pattern we already have:
   - Main agent produces unstructured output
   - StructuredOutputAgent extracts structure


   .. autolink-examples:: StructuredOutputMultiAgent
      :collapse:

   .. py:method:: create(main_agent: TMainAgent, output_model: type[pydantic.BaseModel], name: str | None = None, **kwargs) -> StructuredOutputMultiAgent
      :classmethod:


      Create with main agent and output model.


      .. autolink-examples:: create
         :collapse:


   .. py:attribute:: post_agent
      :type:  haive.agents.structured.StructuredOutputAgent
      :value: None



   .. py:attribute:: use_post_transform
      :type:  bool
      :value: None



.. py:class:: ToolBasedReflectionAgent

   Bases: :py:obj:`haive.agents.react.agent.ReactAgent`


   Reflection agent that uses tools to cite improvements.

   Similar to LangChain's reflexion but more flexible.


   .. autolink-examples:: ToolBasedReflectionAgent
      :collapse:

   .. py:method:: model_post_init(__context: Any) -> None

      Set up tool-based reflection.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:attribute:: reflection_mode
      :type:  str
      :value: None



   .. py:attribute:: require_citations
      :type:  bool
      :value: None



.. py:function:: create(*args, **kwargs)

   Create a basic reflection agent (alias for create_reflection_agent).


   .. autolink-examples:: create
      :collapse:

.. py:function:: create_expert_agent(name: str, domain: str, expertise_level: Literal['beginner', 'intermediate', 'expert', 'world-class'] = 'expert', **kwargs) -> ExpertAgent

   Create an expert agent.


   .. autolink-examples:: create_expert_agent
      :collapse:

.. py:function:: create_graded_reflection_agent(name: str = 'graded_reflector', main_agent: haive.agents.base.agent.Agent | None = None, **kwargs) -> GradingAgent | GradedReflectionMultiAgent

   Create grading agent or full graded reflection system.


   .. autolink-examples:: create_graded_reflection_agent
      :collapse:

.. py:function:: create_reflection_agent(name: str = 'reflector', engine: haive.core.engine.aug_llm.AugLLMConfig | None = None, **kwargs) -> ReflectionAgent

   Create a simple reflection agent.


   .. autolink-examples:: create_reflection_agent
      :collapse:

.. py:function:: create_tool_based_reflection_agent(name: str = 'tool_reflector', tools: list | None = None, **kwargs) -> ToolBasedReflectionAgent

   Create tool-based reflection agent.


   .. autolink-examples:: create_tool_based_reflection_agent
      :collapse:

.. py:function:: model_post_init(*args, **kwargs)

   Model post-init function (placeholder for compatibility).


   .. autolink-examples:: model_post_init
      :collapse:

.. py:data:: TMainAgent

.. py:data:: TPostAgent

.. py:data:: TPreAgent

