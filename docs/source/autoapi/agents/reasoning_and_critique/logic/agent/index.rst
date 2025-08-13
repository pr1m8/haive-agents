
:py:mod:`agents.reasoning_and_critique.logic.agent`
===================================================

.. py:module:: agents.reasoning_and_critique.logic.agent


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.logic.agent.ReasoningSystem
   agents.reasoning_and_critique.logic.agent.ReasoningSystemState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReasoningSystem:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningSystem {
        node [shape=record];
        "ReasoningSystem" [label="ReasoningSystem"];
        "haive.agents.base.agent.Agent" -> "ReasoningSystem";
      }

.. autoclass:: agents.reasoning_and_critique.logic.agent.ReasoningSystem
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReasoningSystemState:

   .. graphviz::
      :align: center

      digraph inheritance_ReasoningSystemState {
        node [shape=record];
        "ReasoningSystemState" [label="ReasoningSystemState"];
        "haive.core.schema.state_schema.StateSchema" -> "ReasoningSystemState";
      }

.. autoclass:: agents.reasoning_and_critique.logic.agent.ReasoningSystemState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.logic.agent.create_bias_detector
   agents.reasoning_and_critique.logic.agent.create_logical_reasoner
   agents.reasoning_and_critique.logic.agent.create_premise_extractor
   agents.reasoning_and_critique.logic.agent.create_synthesis_agent
   agents.reasoning_and_critique.logic.agent.create_uncertainty_analyzer

.. py:function:: create_bias_detector() -> haive.core.engine.aug_llm.AugLLMConfig

   Create bias detector configuration.


   .. autolink-examples:: create_bias_detector
      :collapse:

.. py:function:: create_logical_reasoner() -> haive.core.engine.aug_llm.AugLLMConfig

   Create logical reasoner configuration.


   .. autolink-examples:: create_logical_reasoner
      :collapse:

.. py:function:: create_premise_extractor() -> haive.core.engine.aug_llm.AugLLMConfig

   Create premise extractor configuration.


   .. autolink-examples:: create_premise_extractor
      :collapse:

.. py:function:: create_synthesis_agent() -> haive.core.engine.aug_llm.AugLLMConfig

   Create synthesis agent configuration.


   .. autolink-examples:: create_synthesis_agent
      :collapse:

.. py:function:: create_uncertainty_analyzer() -> haive.core.engine.aug_llm.AugLLMConfig

   Create uncertainty analyzer configuration.


   .. autolink-examples:: create_uncertainty_analyzer
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.logic.agent
   :collapse:
   
.. autolink-skip:: next
