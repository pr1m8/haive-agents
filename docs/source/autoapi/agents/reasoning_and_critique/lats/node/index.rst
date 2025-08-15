agents.reasoning_and_critique.lats.node
=======================================

.. py:module:: agents.reasoning_and_critique.lats.node


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.lats.node.Node
   agents.reasoning_and_critique.lats.node.NodeManager


Module Contents
---------------

.. py:class:: Node(**data)

   Bases: :py:obj:`pydantic.BaseModel`


   Node class for reflection/reflexion trees with proper serialization.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Node
      :collapse:

   .. py:method:: add_child(child: Node) -> None

      Add a child node.


      .. autolink-examples:: add_child
         :collapse:


   .. py:method:: get_path() -> list[Node]

      Get path from root to this node.


      .. autolink-examples:: get_path
         :collapse:


   .. py:method:: get_trajectory(include_reflections: bool = True) -> list[langchain_core.messages.BaseMessage]

      Get all messages in the path from root to this node.


      .. autolink-examples:: get_trajectory
         :collapse:


   .. py:method:: serialize_children(children: list[Node]) -> list[dict[str, Any]]

      Serialize children as IDs only to avoid recursion.


      .. autolink-examples:: serialize_children
         :collapse:


   .. py:method:: serialize_model() -> dict[str, Any]

      Custom model serializer to handle recursion.


      .. autolink-examples:: serialize_model
         :collapse:


   .. py:method:: serialize_parent(parent: Optional[Node]) -> dict[str, Any] | None

      Serialize parent node as ID only to avoid recursion.


      .. autolink-examples:: serialize_parent
         :collapse:


   .. py:attribute:: children
      :type:  list[Node]
      :value: None



   .. py:attribute:: depth
      :type:  int
      :value: None



   .. py:attribute:: messages
      :type:  list[langchain_core.messages.BaseMessage]


   .. py:attribute:: parent
      :type:  Optional[Node]
      :value: None



   .. py:attribute:: reflection
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: value
      :type:  float
      :value: 0.0



   .. py:attribute:: visits
      :type:  int
      :value: 0



.. py:class:: NodeManager

   Manages Node objects to rebuild references after serialization/deserialization.


   .. autolink-examples:: NodeManager
      :collapse:

   .. py:method:: get(node_id: int) -> Node | None

      Get a node by ID.


      .. autolink-examples:: get
         :collapse:


   .. py:method:: rebuild_references() -> None

      Rebuild parent-child references after deserialization.


      .. autolink-examples:: rebuild_references
         :collapse:


   .. py:method:: register(node: Node) -> None

      Register a node.


      .. autolink-examples:: register
         :collapse:


   .. py:attribute:: nodes
      :type:  dict[int, Node]


