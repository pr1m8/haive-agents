
:py:mod:`agents.memory_reorganized.base.token_state`
====================================================

.. py:module:: agents.memory_reorganized.base.token_state

Memory state with integrated token tracking and summarization hooks.

This module extends MessagesStateWithTokenUsage to add memory-specific functionality
with pre-hooks for summarization and token management.


.. autolink-examples:: agents.memory_reorganized.base.token_state
   :collapse:

Classes
-------

.. autoapisummary::

   agents.memory_reorganized.base.token_state.MemoryStateWithTokens


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MemoryStateWithTokens:

   .. graphviz::
      :align: center

      digraph inheritance_MemoryStateWithTokens {
        node [shape=record];
        "MemoryStateWithTokens" [label="MemoryStateWithTokens"];
        "haive.core.schema.prebuilt.messages.messages_with_token_usage.MessagesStateWithTokenUsage" -> "MemoryStateWithTokens";
      }

.. autoclass:: agents.memory_reorganized.base.token_state.MemoryStateWithTokens
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: agents.memory_reorganized.base.token_state
   :collapse:
   
.. autolink-skip:: next
