
:py:mod:`agents.base.agent`
===========================

.. py:module:: agents.base.agent

Enhanced Agent hierarchy with engine-focused generics and backward compatibility.

This module provides the enhanced agent architecture:
- Workflow: Pure orchestration without LLM
- Agent: Workflow + Engine (generic on engine type)
- MultiAgent: Agent + multi-agent coordination

Key features:
- Engine-centric generics: Agent[EngineT]
- Full backward compatibility with existing code
- Clear separation of concerns: orchestration vs LLM vs coordination
- Type safety when needed, flexibility when desired


.. autolink-examples:: agents.base.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.base.agent.Agent
   agents.base.agent.TypedInvokableEngine


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Agent:

   .. graphviz::
      :align: center

      digraph inheritance_Agent {
        node [shape=record];
        "Agent" [label="Agent"];
        "TypedInvokableEngine[EngineT]" -> "Agent";
        "haive.agents.base.mixins.execution_mixin.ExecutionMixin" -> "Agent";
        "haive.agents.base.mixins.state_mixin.StateMixin" -> "Agent";
        "haive.agents.base.mixins.persistence_mixin.PersistenceMixin" -> "Agent";
        "haive.agents.base.serialization_mixin.SerializationMixin" -> "Agent";
        "haive.agents.base.agent_structured_output_mixin.StructuredOutputMixin" -> "Agent";
        "haive.agents.base.pre_post_agent_mixin.PrePostAgentMixin" -> "Agent";
        "abc.ABC" -> "Agent";
      }

.. autoclass:: agents.base.agent.Agent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TypedInvokableEngine:

   .. graphviz::
      :align: center

      digraph inheritance_TypedInvokableEngine {
        node [shape=record];
        "TypedInvokableEngine" [label="TypedInvokableEngine"];
        "haive.core.engine.base.InvokableEngine[pydantic.BaseModel, pydantic.BaseModel]" -> "TypedInvokableEngine";
        "Generic[EngineT]" -> "TypedInvokableEngine";
      }

.. autopydantic_model:: agents.base.agent.TypedInvokableEngine
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





.. rubric:: Related Links

.. autolink-examples:: agents.base.agent
   :collapse:
   
.. autolink-skip:: next
