agents.research.person.utils
============================

.. py:module:: agents.research.person.utils


Functions
---------

.. autoapisummary::

   agents.research.person.utils.deduplicate_and_format_sources
   agents.research.person.utils.format_all_notes
   agents.research.person.utils.get_config_from_runnable_config


Module Contents
---------------

.. py:function:: deduplicate_and_format_sources(search_response: Any, max_tokens_per_source: int, include_raw_content: bool = True) -> str

   Takes either a single search response or list of responses from Tavily API and formats them.
   Limits the raw_content to approximately max_tokens_per_source.

   :param search_response: Either:
                           - A dict with a 'results' key containing a list of search results
                           - A list of dicts, each containing search results
   :param max_tokens_per_source: Maximum number of tokens per source
   :param include_raw_content: Whether to include the raw_content from Tavily

   :returns: Formatted string with deduplicated sources
   :rtype: str


   .. autolink-examples:: deduplicate_and_format_sources
      :collapse:

.. py:function:: format_all_notes(completed_notes: list[str]) -> str

   Format a list of notes into a string.

   :param completed_notes: List of notes to format

   :returns: Formatted notes
   :rtype: str


   .. autolink-examples:: format_all_notes
      :collapse:

.. py:function:: get_config_from_runnable_config(config: dict[str, Any]) -> dict[str, Any]

   Extract configuration values from a runnable config.

   :param config: Runnable configuration

   :returns: Configuration values
   :rtype: dict


   .. autolink-examples:: get_config_from_runnable_config
      :collapse:

