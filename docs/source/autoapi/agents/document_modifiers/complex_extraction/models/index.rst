agents.document_modifiers.complex_extraction.models
===================================================

.. py:module:: agents.document_modifiers.complex_extraction.models


Classes
-------

.. autoapisummary::

   agents.document_modifiers.complex_extraction.models.JsonPatch
   agents.document_modifiers.complex_extraction.models.PatchFunctionParameters
   agents.document_modifiers.complex_extraction.models.RetryStrategy


Module Contents
---------------

.. py:class:: JsonPatch(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A JSON Patch document represents an operation to be performed on a JSON document.

   Note that the op and path are ALWAYS required. Value is required for ALL operations except 'remove'.

   Examples:
   \`\`\`json
   {"op": "add", "path": "/a/b/c", "patch_value": 1}
   {"op": "replace", "path": "/a/b/c", "patch_value": 2}
   {"op": "remove", "path": "/a/b/c"}
   \`\`\`

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: JsonPatch
      :collapse:

   .. py:attribute:: op
      :type:  Literal['add', 'remove', 'replace']
      :value: None



   .. py:attribute:: path
      :type:  str
      :value: None



   .. py:attribute:: value
      :type:  Any
      :value: None



.. py:class:: PatchFunctionParameters(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Respond with all JSONPatch operation to correct validation errors caused by passing in incorrect or incomplete parameters in a previous tool call.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PatchFunctionParameters
      :collapse:

   .. py:attribute:: patches
      :type:  list[JsonPatch]
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: tool_call_id
      :type:  str
      :value: None



.. py:class:: RetryStrategy

   Bases: :py:obj:`TypedDict`


   The retry strategy for a tool call.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RetryStrategy
      :collapse:

   .. py:attribute:: aggregate_messages
      :type:  collections.abc.Callable[[collections.abc.Sequence[langchain_core.messages.AnyMessage]], langchain_core.messages.AIMessage] | None


   .. py:attribute:: fallback
      :type:  langchain_core.runnables.Runnable[collections.abc.Sequence[langchain_core.messages.AnyMessage], langchain_core.messages.AIMessage] | langchain_core.runnables.Runnable[collections.abc.Sequence[langchain_core.messages.AnyMessage], langchain_core.messages.BaseMessage] | collections.abc.Callable[[collections.abc.Sequence[langchain_core.messages.AnyMessage]], langchain_core.messages.AIMessage] | None

      The function to use once validation fails.

      .. autolink-examples:: fallback
         :collapse:


   .. py:attribute:: max_attempts
      :type:  int

      The maximum number of attempts to make.

      .. autolink-examples:: max_attempts
         :collapse:


