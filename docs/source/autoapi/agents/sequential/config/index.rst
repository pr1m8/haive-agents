
:py:mod:`agents.sequential.config`
==================================

.. py:module:: agents.sequential.config

Configuration for SequentialAgent that connects components in a linear workflow.

from typing import Any
This module defines the configuration class for SequentialAgent, which
automates the process of connecting multiple engine components in a sequence.


.. autolink-examples:: agents.sequential.config
   :collapse:

Classes
-------

.. autoapisummary::

   agents.sequential.config.SequentialAgentConfig
   agents.sequential.config.StepConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SequentialAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_SequentialAgentConfig {
        node [shape=record];
        "SequentialAgentConfig" [label="SequentialAgentConfig"];
        "haive.core.engine.agent.config.AgentConfig" -> "SequentialAgentConfig";
      }

.. autoclass:: agents.sequential.config.SequentialAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StepConfig:

   .. graphviz::
      :align: center

      digraph inheritance_StepConfig {
        node [shape=record];
        "StepConfig" [label="StepConfig"];
        "pydantic.BaseModel" -> "StepConfig";
      }

.. autopydantic_model:: agents.sequential.config.StepConfig
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



Functions
---------

.. autoapisummary::

   agents.sequential.config.build_agent
   agents.sequential.config.from_aug_llms
   agents.sequential.config.from_components
   agents.sequential.config.from_steps
   agents.sequential.config.get_step_by_name
   agents.sequential.config.setup_components
   agents.sequential.config.validate_steps

.. py:function:: build_agent(config: SequentialAgentConfig) -> haive.agents.sequential.agent.SequentialAgent

   Build a SequentialAgent from configuration.


   .. autolink-examples:: build_agent
      :collapse:

.. py:function:: from_aug_llms(aug_llms: list[haive.core.engine.aug_llm.AugLLMConfig], name: str | None = None, id: str | None = None, state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> SequentialAgentConfig

   Create a SequentialAgentConfig from a list of AugLLMConfig instances.


   .. autolink-examples:: from_aug_llms
      :collapse:

.. py:function:: from_components(components: list[Any], name: str | None = None, id: str | None = None, state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> SequentialAgentConfig

   Create a SequentialAgentConfig from a list of components.


   .. autolink-examples:: from_components
      :collapse:

.. py:function:: from_steps(steps: list[StepConfig], name: str | None = None, id: str | None = None, entry_point: str | None = None, state_schema: type[haive.core.schema.state_schema.StateSchema] | None = None, **kwargs) -> SequentialAgentConfig

   Create a SequentialAgentConfig from a list of steps.


   .. autolink-examples:: from_steps
      :collapse:

.. py:function:: get_step_by_name(config: SequentialAgentConfig, name: str) -> StepConfig | None

   Get a step configuration by name.


   .. autolink-examples:: get_step_by_name
      :collapse:

.. py:function:: setup_components(config: SequentialAgentConfig) -> SequentialAgentConfig

   Setup components for a configuration.


   .. autolink-examples:: setup_components
      :collapse:

.. py:function:: validate_steps(steps: list[StepConfig]) -> bool

   Validate that steps list is not empty.


   .. autolink-examples:: validate_steps
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.sequential.config
   :collapse:
   
.. autolink-skip:: next
