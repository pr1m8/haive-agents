agents.research.open_perplexity.examples.batch_research
=======================================================

.. py:module:: agents.research.open_perplexity.examples.batch_research

.. autoapi-nested-parse::

   Batch research example demonstrating how to use the Open Perplexity research agent.
   to process multiple research topics in sequence.


   .. autolink-examples:: agents.research.open_perplexity.examples.batch_research
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.research.open_perplexity.examples.batch_research.RESEARCH_TOPICS
   agents.research.open_perplexity.examples.batch_research.logger


Functions
---------

.. autoapisummary::

   agents.research.open_perplexity.examples.batch_research.conduct_research
   agents.research.open_perplexity.examples.batch_research.main


Module Contents
---------------

.. py:function:: conduct_research(agent: haive.agents.open_perplexity.agent.ResearchAgent, topic: dict[str, str], output_dir: str) -> dict

   Conduct research on a specific topic and save the report.

   :param agent: The research agent
   :param topic: Dict containing the research topic with title and query
   :param output_dir: Directory to save the report

   :returns: Dict containing research results and metadata


   .. autolink-examples:: conduct_research
      :collapse:

.. py:function:: main() -> None

   Run batch research on multiple topics.


   .. autolink-examples:: main
      :collapse:

.. py:data:: RESEARCH_TOPICS

.. py:data:: logger

