
:py:mod:`agents.research.storm.example`
=======================================

.. py:module:: agents.research.storm.example

Example demonstrating how to use the STORM agent to generate.
a comprehensive Wikipedia-style article on a given topic.


.. autolink-examples:: agents.research.storm.example
   :collapse:


Functions
---------

.. autoapisummary::

   agents.research.storm.example.main
   agents.research.storm.example.run_storm_agent
   agents.research.storm.example.setup_environment

.. py:function:: main() -> None

   Main entry point for the script.


   .. autolink-examples:: main
      :collapse:

.. py:function:: run_storm_agent(topic: str, output_file: str | None = None, num_perspectives: int = 3, max_turns: int = 5, verbose: bool = False)
   :async:


   Run the STORM agent on a given topic.

   :param topic: The topic to research and write about
   :param output_file: Optional file path to save the generated article
   :param num_perspectives: Number of perspectives to interview
   :param max_turns: Maximum number of conversation turns per interview
   :param verbose: Whether to enable verbose logging


   .. autolink-examples:: run_storm_agent
      :collapse:

.. py:function:: setup_environment() -> None

   Set up required environment variables.


   .. autolink-examples:: setup_environment
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.research.storm.example
   :collapse:
   
.. autolink-skip:: next
