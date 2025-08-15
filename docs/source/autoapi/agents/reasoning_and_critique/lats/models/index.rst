agents.reasoning_and_critique.lats.models
=========================================

.. py:module:: agents.reasoning_and_critique.lats.models


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.lats.models.Node
   agents.reasoning_and_critique.lats.models.Reflection


Module Contents
---------------

.. py:class:: Node(messages: list[langchain_core.messages.BaseMessage], reflection: Reflection, parent: Optional[Node] = None)

   .. py:method:: __repr__() -> str


   .. py:method:: _get_all_children()


   .. py:method:: _mark_tree_as_solved()


   .. py:method:: backpropagate(reward: float)

      Update the score of this node and its parents.


      .. autolink-examples:: backpropagate
         :collapse:


   .. py:method:: get_best_solution() -> Any | None

      Return the best solution from within the current sub-tree.


      .. autolink-examples:: get_best_solution
         :collapse:


   .. py:method:: get_messages(include_reflections: bool = True)


   .. py:method:: get_trajectory(include_reflections: bool = True) -> list[langchain_core.messages.BaseMessage]

      Get messages representing this search branch.


      .. autolink-examples:: get_trajectory
         :collapse:


   .. py:method:: upper_confidence_bound(exploration_weight=1.0) -> Any

      Return the UCT score. This helps balance exploration vs. exploitation of a branch.


      .. autolink-examples:: upper_confidence_bound
         :collapse:


   .. py:attribute:: _is_solved


   .. py:property:: best_child_score
      :type: Any


      Return the child with the highest value.

      .. autolink-examples:: best_child_score
         :collapse:


   .. py:attribute:: children
      :value: []



   .. py:attribute:: depth


   .. py:property:: height
      :type: int


      Check for how far we've rolled out the tree.

      .. autolink-examples:: height
         :collapse:


   .. py:property:: is_solved
      :type: bool


      If any solutions exist, we can end the search.

      .. autolink-examples:: is_solved
         :collapse:


   .. py:property:: is_terminal
      :type: bool



   .. py:attribute:: messages


   .. py:attribute:: parent
      :value: None



   .. py:attribute:: reflection


   .. py:attribute:: value
      :value: 0



   .. py:attribute:: visits
      :value: 0



.. py:class:: Reflection(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   !!! abstract "Usage Documentation"
       [Models](../concepts/models.md)

   A base class for creating Pydantic models.

   .. attribute:: __class_vars__

      The names of the class variables defined on the model.

   .. attribute:: __private_attributes__

      Metadata about the private attributes of the model.

   .. attribute:: __signature__

      The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

   .. attribute:: __pydantic_complete__

      Whether model building is completed, or if there are still undefined fields.

   .. attribute:: __pydantic_core_schema__

      The core schema of the model.

   .. attribute:: __pydantic_custom_init__

      Whether the model has a custom `__init__` function.

   .. attribute:: __pydantic_decorators__

      Metadata containing the decorators defined on the model.
      This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.

   .. attribute:: __pydantic_generic_metadata__

      Metadata for generic models; contains data used for a similar purpose to
      __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.

   .. attribute:: __pydantic_parent_namespace__

      Parent namespace of the model, used for automatic rebuilding of models.

   .. attribute:: __pydantic_post_init__

      The name of the post-init method for the model, if defined.

   .. attribute:: __pydantic_root_model__

      Whether the model is a [`RootModel`][pydantic.root_model.RootModel].

   .. attribute:: __pydantic_serializer__

      The `pydantic-core` `SchemaSerializer` used to dump instances of the model.

   .. attribute:: __pydantic_validator__

      The `pydantic-core` `SchemaValidator` used to validate instances of the model.

   .. attribute:: __pydantic_fields__

      A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.

   .. attribute:: __pydantic_computed_fields__

      A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

   .. attribute:: __pydantic_extra__

      A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
      is set to `'allow'`.

   .. attribute:: __pydantic_fields_set__

      The names of fields explicitly set during instantiation.

   .. attribute:: __pydantic_private__

      Values of private attributes set on the model instance.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Reflection
      :collapse:

   .. py:method:: as_message() -> Any


   .. py:attribute:: found_solution
      :type:  bool
      :value: None



   .. py:property:: normalized_score
      :type: float



   .. py:attribute:: reflections
      :type:  str
      :value: None



   .. py:attribute:: score
      :type:  int
      :value: None



