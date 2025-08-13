
:py:mod:`agents.document_modifiers.tnt.agent`
=============================================

.. py:module:: agents.document_modifiers.tnt.agent

Taxonomy generation agent implementation.

from typing import Any, Dict, Optional
This module implements an agent that generates taxonomies from conversation histories
through an iterative process of document summarization, clustering, and refinement.
It uses LLM-based processing at each step to generate high-quality taxonomies.

The agent follows these main steps:
1. Document summarization
2. Minibatch creation
3. Initial taxonomy generation
4. Iterative taxonomy refinement
5. Final taxonomy review

.. rubric:: Example

Basic usage of the taxonomy agent::

    config = TaxonomyAgentConfig(
        state_schema=TaxonomyGenerationState,
        visualize=True,
        name="TaxonomyAgent"
    )
    agent = TaxonomyAgent(config)
    result = agent.run(input_data={"documents": [...]})


.. autolink-examples:: agents.document_modifiers.tnt.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.document_modifiers.tnt.agent.TaxonomyAgent
   agents.document_modifiers.tnt.agent.TaxonomyAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaxonomyAgent:

   .. graphviz::
      :align: center

      digraph inheritance_TaxonomyAgent {
        node [shape=record];
        "TaxonomyAgent" [label="TaxonomyAgent"];
        "haive.core.engine.agent.agent.Agent[TaxonomyAgentConfig]" -> "TaxonomyAgent";
      }

.. autoclass:: agents.document_modifiers.tnt.agent.TaxonomyAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaxonomyAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_TaxonomyAgentConfig {
        node [shape=record];
        "TaxonomyAgentConfig" [label="TaxonomyAgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "TaxonomyAgentConfig";
      }

.. autoclass:: agents.document_modifiers.tnt.agent.TaxonomyAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.tnt.agent
   :collapse:
   
.. autolink-skip:: next
