agents.base.serialization_mixin
===============================

.. py:module:: agents.base.serialization_mixin

.. autoapi-nested-parse::

   Serialization mixin for Agent classes.

   This mixin provides proper serialization support for Agent instances in LangGraph,
   handling both pickle and msgpack serialization formats.


   .. autolink-examples:: agents.base.serialization_mixin
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.base.serialization_mixin.logger


Classes
-------

.. autoapisummary::

   agents.base.serialization_mixin.SerializationMixin


Module Contents
---------------

.. py:class:: SerializationMixin

   Mixin for serializing and deserializing Agent instances.

   This mixin provides methods for handling serialization with both pickle and
   msgpack, focusing on addressing the specific needs of agents within LangGraph.

   LangGraph uses msgpack under the hood for serialization during graph execution.
   This mixin ensures agents can be properly serialized without errors.


   .. autolink-examples:: SerializationMixin
      :collapse:

   .. py:method:: __getstate__() -> dict[str, Any]

      Prepare instance for pickling.

      Excludes non-serializable components like graph, compiled_graph,
      checkpointer, store, etc. and handles complex type objects.

      :returns: Dict containing serializable state.


      .. autolink-examples:: __getstate__
         :collapse:


   .. py:method:: __reduce__() -> tuple

      Make agent picklable for both pickle and msgpack.

      This special method enables proper serialization with both pickle and msgpack.
      We return a tuple of (constructor, args, state) that can be used to reconstruct
      this object.

      :returns: Tuple of (constructor, empty args, state) for reconstruction.


      .. autolink-examples:: __reduce__
         :collapse:


   .. py:method:: __setstate__(state: dict[str, Any]) -> None

      Reconstruct instance after unpickling.

      Handles reconstruction of the state dictionary, rebuilding special fields
      like schemas and structured output models.

      :param state: Dictionary containing serialized state.


      .. autolink-examples:: __setstate__
         :collapse:


   .. py:method:: _deserialize_from_msgpack(data: dict[str, Any]) -> SerializationMixin
      :classmethod:


      Reconstruct an agent from msgpack-serialized data.

      :param data: Serialized data dictionary from _serialize_for_msgpack.

      :returns: Reconstructed agent instance.


      .. autolink-examples:: _deserialize_from_msgpack
         :collapse:


   .. py:method:: _serialize_for_msgpack() -> dict[str, Any]

      Create a msgpack-serializable representation of this object.

      This method is used for explicitly controlling what's serialized when
      msgpack is directly used (e.g., in checkpointing).

      :returns: Dict containing msgpack-serializable data.


      .. autolink-examples:: _serialize_for_msgpack
         :collapse:


.. py:data:: logger

