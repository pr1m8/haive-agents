
:py:mod:`agents.research.open_perplexity.cli`
=============================================

.. py:module:: agents.research.open_perplexity.cli

CLI tool for running the open_perplexity research agent.

This module provides command-line utilities for running research tasks
and visualizing research states. It supports loading research questions
from text files, configuring research parameters, and generating reports.


.. autolink-examples:: agents.research.open_perplexity.cli
   :collapse:


Functions
---------

.. autoapisummary::

   agents.research.open_perplexity.cli.main
   agents.research.open_perplexity.cli.run_research
   agents.research.open_perplexity.cli.visualize_state

.. py:function:: main() -> None

   CLI entry point for the research tool.

   Parses command-line arguments and executes the appropriate command
   based on user input.


   .. autolink-examples:: main
      :collapse:

.. py:function:: run_research(text_path: str, **kwargs) -> None

   Run a research process on text from the specified file.

   Loads a research question from a text file, configures a research agent with
   the specified parameters, runs the research process, and saves the results.

   :param text_path: Path to a text file containing research question
   :param \*\*kwargs: Additional arguments to pass to the agent, including:
                      - output: Path to save the generated report
                      - save_state_path: Path to save the state history
                      - depth: Research depth (1-5)
                      - concurrent_searches: Number of concurrent searches
                      - max_sources: Maximum sources per query
                      - vector_store_path: Path for the vector store


   .. autolink-examples:: run_research
      :collapse:

.. py:function:: visualize_state(state_path: str, step: int | None = None, output_md: str | None = None) -> None

   Visualize a specific state from a saved state history file.

   Loads a state from a saved state history file, displays a visualization
   of the research state, and optionally generates a markdown report.

   :param state_path: Path to a saved state history JSON file
   :param step: Index of the state to visualize (default: last state)
   :param output_md: Path to save the markdown report (optional)


   .. autolink-examples:: visualize_state
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.research.open_perplexity.cli
   :collapse:
   
.. autolink-skip:: next
