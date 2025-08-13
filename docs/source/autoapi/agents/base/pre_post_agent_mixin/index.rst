
:py:mod:`agents.base.pre_post_agent_mixin`
==========================================

.. py:module:: agents.base.pre_post_agent_mixin

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

Classes
-------

.. autoapisummary::

   agents.base.pre_post_agent_mixin.MessageTransformer
   agents.base.pre_post_agent_mixin.PrePostAgentMixin


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MessageTransformer:

   .. graphviz::
      :align: center

      digraph inheritance_MessageTransformer {
        node [shape=record];
        "MessageTransformer" [label="MessageTransformer"];
      }

.. autoclass:: agents.base.pre_post_agent_mixin.MessageTransformer
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PrePostAgentMixin:

   .. graphviz::
      :align: center

      digraph inheritance_PrePostAgentMixin {
        node [shape=record];
        "PrePostAgentMixin" [label="PrePostAgentMixin"];
      }

.. autoclass:: agents.base.pre_post_agent_mixin.PrePostAgentMixin
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.base.pre_post_agent_mixin.create_graded_reflection_agent
   agents.base.pre_post_agent_mixin.create_reflection_agent
   agents.base.pre_post_agent_mixin.create_structured_output_agent

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



.. rubric:: Related Links

.. autolink-examples:: agents.base.pre_post_agent_mixin
   :collapse:
   
.. autolink-skip:: next
