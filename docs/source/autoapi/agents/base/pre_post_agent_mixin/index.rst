agents.base.pre_post_agent_mixin
================================

.. py:module:: agents.base.pre_post_agent_mixin

.. autoapi-nested-parse::

   Pre/Post Agent Processing Mixin.

   This mixin generalizes the pre/post agent pattern from the reflection agents
   to the enhanced base agent, allowing any agent to have pre-processing and
   post-processing stages with message transformation support.

   The pattern supports:
   - Optional pre-processing agent
   - Main agent processing
   - Optional post-processing agent
   - Message transformation between stages
   - Hook integration for monitoring

   .. rubric:: Examples

   Basic usage with reflection::

       class MyReflectionAgent(Agent, PrePostAgentMixin):
           def setup_agent(self):
               # Set up main agent
               self.main_agent = SimpleAgent(name="writer", engine=config)

               # Set up post-processing with reflection
               self.post_agent = SimpleAgent(name="reflector", engine=reflection_config)
               self.use_post_transform = True
               self.post_transform_type = "reflection"

   Graded reflection pattern::

       class MyGradedAgent(Agent, PrePostAgentMixin):
           def setup_agent(self):
               self.pre_agent = SimpleAgent(name="grader", engine=grading_config)
               self.main_agent = SimpleAgent(name="responder", engine=main_config)
               self.post_agent = SimpleAgent(name="improver", engine=reflection_config)

               self.use_pre_transform = False
               self.use_post_transform = True

   Factory pattern::

       agent = create_reflection_agent(
           main_agent=SimpleAgent(name="writer", engine=config),
           reflection_type="graded"
       )


   .. autolink-examples:: agents.base.pre_post_agent_mixin
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.pre_post_agent_mixin.TMainAgent
   agents.base.pre_post_agent_mixin.TPostAgent
   agents.base.pre_post_agent_mixin.TPreAgent
   agents.base.pre_post_agent_mixin.logger


Classes
-------

.. autoapisummary::

   agents.base.pre_post_agent_mixin.MessageTransformer
   agents.base.pre_post_agent_mixin.PrePostAgentMixin


Functions
---------

.. autoapisummary::

   agents.base.pre_post_agent_mixin.create_graded_reflection_agent
   agents.base.pre_post_agent_mixin.create_reflection_agent
   agents.base.pre_post_agent_mixin.create_structured_output_agent


Module Contents
---------------

.. py:class:: MessageTransformer(transformation_type: str = 'reflection', preserve_first: bool = True)

   Simple message transformer for reflection patterns.

   Initialize transformer.

   :param transformation_type: Type of transformation ("reflection", "ai_to_human", etc.)
   :param preserve_first: Whether to preserve the first message


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MessageTransformer
      :collapse:

   .. py:method:: transform_messages(messages: list[langchain_core.messages.BaseMessage]) -> list[langchain_core.messages.BaseMessage]

      Transform messages according to the transformation type.

      :param messages: Input messages to transform

      :returns: Transformed messages


      .. autolink-examples:: transform_messages
         :collapse:


   .. py:attribute:: preserve_first
      :value: True



   .. py:attribute:: transformation_type
      :value: 'reflection'



.. py:class:: PrePostAgentMixin

   Mixin that adds pre/post agent processing capabilities.

   This mixin generalizes the PrePostMultiAgent pattern from reflection agents
   to work with any enhanced agent. It provides:

   - Optional pre-processing agent
   - Main agent processing (the agent this mixin is applied to)
   - Optional post-processing agent
   - Message transformation between stages
   - Hook integration for monitoring
   - Configurable transformation types


   .. autolink-examples:: PrePostAgentMixin
      :collapse:

   .. py:method:: arun(input_data: Any) -> Any
      :async:


      Override arun to use pre/post processing if agents are configured.

      :param input_data: Input for the agent

      :returns: Result from pre/post processing or standard arun


      .. autolink-examples:: arun
         :collapse:


   .. py:method:: model_post_init(__context: Any) -> None

      Initialize the mixin after Pydantic validation.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:method:: run_with_pre_post_processing(input_data: Any) -> dict[str, Any]
      :async:


      Execute the agent with pre/post processing stages.

      This method orchestrates the full pre → main → post workflow with
      proper message transformation and hook integration.

      :param input_data: Input for the agent workflow

      :returns: Combined results from all processing stages


      .. autolink-examples:: run_with_pre_post_processing
         :collapse:


   .. py:method:: setup_transformers() -> None

      Set up message transformers based on configuration.


      .. autolink-examples:: setup_transformers
         :collapse:


   .. py:attribute:: combine_results
      :type:  bool
      :value: None



   .. py:attribute:: post_agent
      :type:  Agent | None
      :value: None



   .. py:attribute:: post_transform_type
      :type:  str
      :value: None



   .. py:attribute:: pre_agent
      :type:  Agent | None
      :value: None



   .. py:attribute:: pre_transform_type
      :type:  str
      :value: None



   .. py:attribute:: preserve_original
      :type:  bool
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



.. py:function:: create_graded_reflection_agent(main_agent: haive.agents.base.agent.Agent, grading_agent: haive.agents.base.agent.Agent | None = None, reflection_agent: haive.agents.base.agent.Agent | None = None, name: str | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Create an agent with grading and reflection processing.

   :param main_agent: The primary agent that generates responses
   :param grading_agent: Optional custom grading agent
   :param reflection_agent: Optional custom reflection agent
   :param name: Name for the enhanced agent
   :param \*\*kwargs: Additional configuration

   :returns: Agent with grading and reflection capabilities


   .. autolink-examples:: create_graded_reflection_agent
      :collapse:

.. py:function:: create_reflection_agent(main_agent: haive.agents.base.agent.Agent, reflection_agent: haive.agents.base.agent.Agent | None = None, name: str | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Create an agent with reflection post-processing.

   :param main_agent: The primary agent that generates responses
   :param reflection_agent: Optional custom reflection agent
   :param name: Name for the enhanced agent
   :param \*\*kwargs: Additional configuration

   :returns: Agent with reflection capabilities


   .. autolink-examples:: create_reflection_agent
      :collapse:

.. py:function:: create_structured_output_agent(main_agent: haive.agents.base.agent.Agent, output_model: type[pydantic.BaseModel], name: str | None = None, **kwargs) -> haive.agents.base.agent.Agent

   Create an agent with structured output post-processing.

   :param main_agent: The primary agent that generates responses
   :param output_model: Pydantic model for structured output
   :param name: Name for the enhanced agent
   :param \*\*kwargs: Additional configuration

   :returns: Agent with structured output capabilities


   .. autolink-examples:: create_structured_output_agent
      :collapse:

.. py:data:: TMainAgent

.. py:data:: TPostAgent

.. py:data:: TPreAgent

.. py:data:: logger

