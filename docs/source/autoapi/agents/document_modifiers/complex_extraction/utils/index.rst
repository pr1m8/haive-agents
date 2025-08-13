
:py:mod:`agents.document_modifiers.complex_extraction.utils`
============================================================

.. py:module:: agents.document_modifiers.complex_extraction.utils


Classes
-------

.. autoapisummary::

   agents.document_modifiers.complex_extraction.utils.RetryStrategy


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RetryStrategy:

   .. graphviz::
      :align: center

      digraph inheritance_RetryStrategy {
        node [shape=record];
        "RetryStrategy" [label="RetryStrategy"];
        "TypedDict" -> "RetryStrategy";
      }

.. autoclass:: agents.document_modifiers.complex_extraction.utils.RetryStrategy
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   agents.document_modifiers.complex_extraction.utils.add_or_overwrite_messages
   agents.document_modifiers.complex_extraction.utils.aggregate_messages
   agents.document_modifiers.complex_extraction.utils.decode
   agents.document_modifiers.complex_extraction.utils.dedict
   agents.document_modifiers.complex_extraction.utils.default_aggregator
   agents.document_modifiers.complex_extraction.utils.encode

.. py:function:: add_or_overwrite_messages(left: list, right: list | dict) -> list

   Append or replace messages depending on format.


   .. autolink-examples:: add_or_overwrite_messages
      :collapse:

.. py:function:: aggregate_messages(messages: collections.abc.Sequence[langchain_core.messages.AnyMessage]) -> langchain_core.messages.AIMessage

.. py:function:: decode(state: pydantic.BaseModel) -> dict

   Ensure the output is in the expected format.

   This function handles extracting data from the AI message's tool calls and optionally
   parsing it into a Pydantic object based on the configuration.

   :param state: The state containing messages and configuration

   :returns: A dictionary with the extracted data


   .. autolink-examples:: decode
      :collapse:

.. py:function:: dedict(x: pydantic.BaseModel) -> list

   Get the messages from the state.


   .. autolink-examples:: dedict
      :collapse:

.. py:function:: default_aggregator(messages: collections.abc.Sequence[langchain_core.messages.AnyMessage]) -> langchain_core.messages.AIMessage

   Aggregates a sequence of messages into a single AI message.


   .. autolink-examples:: default_aggregator
      :collapse:

.. py:function:: encode(state: pydantic.BaseModel) -> dict

   Ensure the input is the correct format.


   .. autolink-examples:: encode
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.complex_extraction.utils
   :collapse:
   
.. autolink-skip:: next
