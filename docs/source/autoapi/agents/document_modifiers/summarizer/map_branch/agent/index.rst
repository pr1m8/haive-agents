
:py:mod:`agents.document_modifiers.summarizer.map_branch.agent`
===============================================================

.. py:module:: agents.document_modifiers.summarizer.map_branch.agent

Map-Reduce Summarizer Agent for document summarization.

This module provides the SummarizerAgent class which implements a map-reduce
approach to document summarization. It can handle large documents by splitting
them into manageable chunks, summarizing each chunk, and then combining the
summaries into a final coherent summary.

The agent handles token limit constraints and provides automatic fallback
mechanisms for oversized documents.

Classes:
    SummarizerAgent: Main agent for map-reduce document summarization

.. rubric:: Examples

Basic usage::

    from haive.agents.document_modifiers.summarizer.map_branch import SummarizerAgent
    from haive.agents.document_modifiers.summarizer.map_branch.config import SummarizerAgentConfig

    config = SummarizerAgentConfig(
        token_max=1000,
        name="document_summarizer"
    )
    agent = SummarizerAgent(config)

    documents = ["Long document text 1...", "Long document text 2..."]
    result = agent.run({"contents": documents})
    summary = result["final_summary"]

With custom token limits::

    config = SummarizerAgentConfig(
        token_max=2000,  # Allow longer intermediate summaries
        engines={
            "map_chain": custom_map_config,
            "reduce_chain": custom_reduce_config
        }
    )
    agent = SummarizerAgent(config)

.. seealso::

   - :class:`~haive.agents.document_modifiers.summarizer.map_branch.config.SummarizerAgentConfig`: Configuration class
   - :class:`~haive.agents.document_modifiers.summarizer.map_branch.state.SummaryState`: State management


.. autolink-examples:: agents.document_modifiers.summarizer.map_branch.agent
   :collapse:

Classes
-------

.. autoapisummary::

   agents.document_modifiers.summarizer.map_branch.agent.SummarizerAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SummarizerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SummarizerAgent {
        node [shape=record];
        "SummarizerAgent" [label="SummarizerAgent"];
        "haive.core.engine.agent.agent.Agent[haive.agents.document_modifiers.summarizer.map_branch.config.SummarizerAgentConfig]" -> "SummarizerAgent";
      }

.. autoclass:: agents.document_modifiers.summarizer.map_branch.agent.SummarizerAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.document_modifiers.summarizer.map_branch.agent.build_agent

.. py:function:: build_agent() -> SummarizerAgent

   Create a default SummarizerAgent instance.

   :returns: SummarizerAgent with default configuration.


   .. autolink-examples:: build_agent
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.summarizer.map_branch.agent
   :collapse:
   
.. autolink-skip:: next
