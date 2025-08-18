haive-agents
============

AI Agent implementations for the Haive framework.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   API Reference <autoapi/haive/agents/index>

Overview
--------

The haive-agents package provides various agent implementations:

- **Simple Agents** - Basic agents with prompt templates
- **React Agents** - Reasoning and acting agents with tool use
- **Multi Agents** - Orchestration of multiple agents
- **RAG Agents** - Retrieval-augmented generation agents
- **Research Agents** - Specialized research workflows
- **Planning Agents** - Strategic planning and execution

Installation
------------

.. code-block:: bash

   pip install haive-agents

Quick Start
-----------

.. code-block:: python

   from haive.agents import SimpleAgent
   from haive.core.engine import AugLLMConfig

   # Create a simple agent
   agent = SimpleAgent(
       name="assistant",
       engine=AugLLMConfig(temperature=0.7)
   )

   # Use the agent
   response = agent.run("Hello, how can you help me?")

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`