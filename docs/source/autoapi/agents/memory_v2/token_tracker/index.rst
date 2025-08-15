agents.memory_v2.token_tracker
==============================

.. py:module:: agents.memory_v2.token_tracker

.. autoapi-nested-parse::

   Token tracking component for memory operations.

   Monitors token usage across memory operations and triggers
   summarization or rewriting when approaching context limits.


   .. autolink-examples:: agents.memory_v2.token_tracker
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_v2.token_tracker.logger


Classes
-------

.. autoapisummary::

   agents.memory_v2.token_tracker.TokenThresholds
   agents.memory_v2.token_tracker.TokenTracker
   agents.memory_v2.token_tracker.TokenUsageEntry


Module Contents
---------------

.. py:class:: TokenThresholds(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Token usage thresholds for different alert levels.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TokenThresholds
      :collapse:

   .. py:method:: get_status(usage_ratio: float) -> str

      Get status based on usage ratio.


      .. autolink-examples:: get_status
         :collapse:


   .. py:attribute:: critical
      :type:  float
      :value: None



   .. py:attribute:: emergency
      :type:  float
      :value: None



   .. py:attribute:: warning
      :type:  float
      :value: None



.. py:class:: TokenTracker(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Track token usage across memory operations with intelligent monitoring.

   Features:
   - Real-time token tracking by operation
   - Threshold monitoring with alerts
   - Usage pattern analysis
   - Recommendations for optimization

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TokenTracker
      :collapse:

   .. py:method:: _update_averages(operation: str) -> None

      Update operation averages.


      .. autolink-examples:: _update_averages
         :collapse:


   .. py:method:: can_fit_operation(estimated_tokens: int) -> bool

      Check if an operation can fit within remaining tokens.

      :param estimated_tokens: Estimated tokens for the operation

      :returns: True if operation can fit, False otherwise


      .. autolink-examples:: can_fit_operation
         :collapse:


   .. py:method:: estimate_tokens_for_content(content: str) -> int

      Estimate tokens for given content.

      Simple estimation: ~4 characters per token (rough approximation).
      In production, would use proper tokenizer.

      :param content: Text content to estimate

      :returns: Estimated token count


      .. autolink-examples:: estimate_tokens_for_content
         :collapse:


   .. py:method:: get_recommendations() -> list[str]

      Get recommendations based on usage patterns.

      :returns: List of recommendation strings


      .. autolink-examples:: get_recommendations
         :collapse:


   .. py:method:: get_remaining_tokens() -> int

      Get number of tokens remaining before limit.


      .. autolink-examples:: get_remaining_tokens
         :collapse:


   .. py:method:: get_status() -> str

      Get current status based on thresholds.


      .. autolink-examples:: get_status
         :collapse:


   .. py:method:: get_usage_ratio() -> float

      Get current usage ratio (0.0 to 1.0).


      .. autolink-examples:: get_usage_ratio
         :collapse:


   .. py:method:: get_usage_summary() -> dict[str, Any]

      Get comprehensive usage summary.

      :returns: Dictionary with usage statistics and analysis


      .. autolink-examples:: get_usage_summary
         :collapse:


   .. py:method:: reset_tokens(keep_history: bool = True) -> None

      Reset token counts while optionally keeping history.

      :param keep_history: Whether to keep usage history


      .. autolink-examples:: reset_tokens
         :collapse:


   .. py:method:: suggest_compression_targets(target_reduction: float = 0.3) -> list[tuple[str, int]]

      Suggest operations to target for compression.

      :param target_reduction: Target reduction ratio (0.0 to 1.0)

      :returns: List of (operation, potential_savings) tuples


      .. autolink-examples:: suggest_compression_targets
         :collapse:


   .. py:method:: track(operation: str, tokens: int, metadata: dict[str, Any] | None = None) -> None

      Track tokens for an operation.

      :param operation: Name of the operation
      :param tokens: Number of tokens used
      :param metadata: Optional metadata about the operation


      .. autolink-examples:: track
         :collapse:


   .. py:attribute:: max_context_tokens
      :type:  int
      :value: None



   .. py:attribute:: operation_averages
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: peak_usage
      :type:  int
      :value: None



   .. py:attribute:: thresholds
      :type:  TokenThresholds
      :value: None



   .. py:attribute:: tokens_by_operation
      :type:  dict[str, int]
      :value: None



   .. py:attribute:: total_tokens
      :type:  int
      :value: None



   .. py:attribute:: usage_history
      :type:  list[TokenUsageEntry]
      :value: None



   .. py:attribute:: window_size
      :type:  int
      :value: None



.. py:class:: TokenUsageEntry(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Single token usage entry for tracking.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TokenUsageEntry
      :collapse:

   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: operation
      :type:  str
      :value: None



   .. py:attribute:: timestamp
      :type:  str
      :value: None



   .. py:attribute:: tokens
      :type:  int
      :value: None



.. py:data:: logger

