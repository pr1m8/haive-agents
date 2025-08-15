agents.react_class.react_many_tools.state
=========================================

.. py:module:: agents.react_class.react_many_tools.state


Classes
-------

.. autoapisummary::

   agents.react_class.react_many_tools.state.ReactManyToolsState


Module Contents
---------------

.. py:class:: ReactManyToolsState

   Bases: :py:obj:`haive.agents.react.react.state.ReactAgentState`


   State for React Agent with many tools.

   Adds fields for tool selection, filtering, and document retrieval.


   .. autolink-examples:: ReactManyToolsState
      :collapse:

   .. py:attribute:: current_tool_category
      :type:  str | None
      :value: None



   .. py:attribute:: filtered_tools
      :type:  list[str]
      :value: None



   .. py:attribute:: query
      :type:  str | None
      :value: None



   .. py:attribute:: retrieval_metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: retrieved_documents
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: tool_categories
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: tool_filter_query
      :type:  str | None
      :value: None



