agents.simple.v2.config
=======================

.. py:module:: agents.simple.v2.config

.. autoapi-nested-parse::

   Simple agent implementation with comprehensive schema handling.

   This module defines a basic single-node agent that uses AugLLMConfig for reasoning,
   with support for structured outputs, schema composition, and explicit input/output schemas.


   .. autolink-examples:: agents.simple.v2.config
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.simple.v2.config.logger


Classes
-------

.. autoapisummary::

   agents.simple.v2.config.SimpleAgent


Module Contents
---------------

.. py:class:: SimpleAgent(config: haive.agents.simple.config.SimpleAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.simple.config.SimpleAgentConfig`\ ]


   A simple agent with a single node workflow and comprehensive schema handling.

   Features:
   - Single processing node using AugLLMConfig
   - Support for explicit input/output schemas
   - Automatic schema derivation from engine
   - Intelligent input/output mapping
   - Structured output support

   Initialize the SimpleAgent with configuration.

   :param config: SimpleAgentConfig instance


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SimpleAgent
      :collapse:

   .. py:method:: has_messages_input() -> bool

      Check if this agent accepts a 'messages' input.

      :returns: True if agent has a messages field in input schema


      .. autolink-examples:: has_messages_input
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up a single-node workflow with the configured schemas and mappings.

      This creates a simple graph with one processing node that handles:
      - Receiving input according to input schema
      - Processing with the AugLLM engine
      - Outputting results according to output schema


      .. autolink-examples:: setup_workflow
         :collapse:


.. py:data:: logger

