agents.base
===========

.. py:module:: agents.base

.. autoapi-nested-parse::

   Base Agent Module - Core abstractions for Haive agents.

   This module provides the base agent class and related utilities for building
   intelligent agents in the Haive framework. It properly exports the Agent class
   from the agent.py module, along with supporting types and utilities.

   Key Components:
       * Classes: Agent (from agent.py), GenericAgent
       * Mixins: ExecutionMixin, StateMixin, SerializationMixin
       * Types: AgentInput, AgentOutput, AgentState

   .. rubric:: Example

   Basic usage::

       from haive.agents.base import Agent
       from haive.core.graph.state_graph.base_graph2 import BaseGraph

       class MyAgent(Agent):
           def setup_agent(self):
               # Custom setup logic
               pass

           def build_graph(self) -> BaseGraph:
               # Build and return the agent's workflow graph
               return my_graph

       # Create agent with configuration
       agent = MyAgent(
           name="my_agent",
           engine=my_llm_engine,
           config=AgentConfig(
               persistence=PostgresCheckpointerConfig(),
               runnable_config={
                   "configurable": {
                       "recursion_limit": 100
                   }
               }
           )
       )

       result = agent.invoke(input_data)

   .. seealso::

      :mod:`haive.agents.base.agent`: Main Agent implementation
      :mod:`haive.agents.base.generic_agent`: Generic typed agent
      :mod:`haive.agents.base.mixins`: Agent capability mixins


   .. autolink-examples:: agents.base
      :collapse:


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/agents/base/agent/index
   /autoapi/agents/base/agent_structured_output_mixin/index
   /autoapi/agents/base/agent_with_token_tracking/index
   /autoapi/agents/base/compiled_agent/index
   /autoapi/agents/base/debug_utils/index
   /autoapi/agents/base/enhanced_init/index
   /autoapi/agents/base/hooks/index
   /autoapi/agents/base/mixins/index
   /autoapi/agents/base/pre_post_agent_mixin/index
   /autoapi/agents/base/serialization_mixin/index
   /autoapi/agents/base/smart_output_parsing/index
   /autoapi/agents/base/structured_output_handler/index
   /autoapi/agents/base/typed_agent/index
   /autoapi/agents/base/types/index
   /autoapi/agents/base/universal_agent/index
   /autoapi/agents/base/workflow/index


