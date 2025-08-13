
:py:mod:`agents.research.open_perplexity.examples.run_from_file`
================================================================

.. py:module:: agents.research.open_perplexity.examples.run_from_file

Example script that demonstrates running the open_perplexity research agent.
from typing import Any
with a research question loaded from a text file.


.. autolink-examples:: agents.research.open_perplexity.examples.run_from_file
   :collapse:


Functions
---------

.. autoapisummary::

   agents.research.open_perplexity.examples.run_from_file.load_research_question
   agents.research.open_perplexity.examples.run_from_file.parse_arguments
   agents.research.open_perplexity.examples.run_from_file.run_research
   agents.research.open_perplexity.examples.run_from_file.setup_logging

.. py:function:: load_research_question(file_path) -> Any

   Load research question from a text file.


   .. autolink-examples:: load_research_question
      :collapse:

.. py:function:: parse_arguments() -> Any

   Parse command line arguments.


   .. autolink-examples:: parse_arguments
      :collapse:

.. py:function:: run_research(question_file, output_dir=None, research_depth=2, max_sources=5) -> bool

   Run research based on a question from a file.

   :param question_file: Path to file containing the research question
   :param output_dir: Directory for outputs (default: ./outputs)
   :param research_depth: Depth of research (1-3)
   :param max_sources: Maximum number of sources per query

   :returns: Boolean indicating success or failure


   .. autolink-examples:: run_research
      :collapse:

.. py:function:: setup_logging(log_file='research_run.log') -> Any

   Set up logging configuration.


   .. autolink-examples:: setup_logging
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.research.open_perplexity.examples.run_from_file
   :collapse:
   
.. autolink-skip:: next
