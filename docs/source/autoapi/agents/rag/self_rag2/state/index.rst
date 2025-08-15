agents.rag.self_rag2.state
==========================

.. py:module:: agents.rag.self_rag2.state

.. autoapi-nested-parse::

   State for the self-rag agent.


   .. autolink-examples:: agents.rag.self_rag2.state
      :collapse:


Classes
-------

.. autoapisummary::

   agents.rag.self_rag2.state.GraphState


Module Contents
---------------

.. py:class:: GraphState

   Bases: :py:obj:`typing_extensions.TypedDict`


   Represents the state of our graph.

   .. attribute:: question

      question

   .. attribute:: generation

      LLM generation

   .. attribute:: documents

      list of documents

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GraphState
      :collapse:

   .. py:attribute:: documents
      :type:  list[str]


   .. py:attribute:: generation
      :type:  str


   .. py:attribute:: question
      :type:  str


