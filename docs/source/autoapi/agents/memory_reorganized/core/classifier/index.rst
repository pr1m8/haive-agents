agents.memory_reorganized.core.classifier
=========================================

.. py:module:: agents.memory_reorganized.core.classifier

.. autoapi-nested-parse::

   Memory classification system using LLM-based analysis.

   This module provides intelligent classification of memories into types, importance
   scoring, and metadata extraction using language models.


   .. autolink-examples:: agents.memory_reorganized.core.classifier
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.memory_reorganized.core.classifier.logger


Classes
-------

.. autoapisummary::

   agents.memory_reorganized.core.classifier.MemoryClassifier
   agents.memory_reorganized.core.classifier.MemoryClassifierConfig


Module Contents
---------------

.. py:class:: MemoryClassifier(config: MemoryClassifierConfig = None)

   LLM-based memory classifier for automatic memory type detection and metadata.
   extraction.

   This classifier analyzes memory content to:
   - Determine memory types (semantic, episodic, procedural, etc.)
   - Calculate importance scores
   - Extract entities, topics, and sentiment
   - Provide classification reasoning

   Initialize memory classifier with configuration.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryClassifier
      :collapse:

   .. py:method:: _extract_entities_simple(text: str) -> list[str]

      Simple entity extraction using regex patterns.


      .. autolink-examples:: _extract_entities_simple
         :collapse:


   .. py:method:: _extract_topics_simple(text: str) -> list[str]

      Simple topic extraction using key analysis.


      .. autolink-examples:: _extract_topics_simple
         :collapse:


   .. py:method:: _fallback_classification(content: str) -> haive.agents.memory.core.types.MemoryClassificationResult

      Provide fallback classification when LLM fails.


      .. autolink-examples:: _fallback_classification
         :collapse:


   .. py:method:: _fallback_query_intent(query: str) -> haive.agents.memory.core.types.MemoryQueryIntent

      Provide fallback query intent when LLM fails.


      .. autolink-examples:: _fallback_query_intent
         :collapse:


   .. py:method:: _parse_classification_result(llm_response: str, original_content: str) -> haive.agents.memory.core.types.MemoryClassificationResult

      Parse LLM response into structured classification result.


      .. autolink-examples:: _parse_classification_result
         :collapse:


   .. py:method:: _parse_query_intent(llm_response: str, original_query: str) -> haive.agents.memory.core.types.MemoryQueryIntent

      Parse LLM response for query intent analysis.


      .. autolink-examples:: _parse_query_intent
         :collapse:


   .. py:method:: _setup_classification_prompts() -> None

      Setup prompts for different classification tasks.


      .. autolink-examples:: _setup_classification_prompts
         :collapse:


   .. py:method:: _setup_llm() -> None

      Setup LLM for classification tasks.


      .. autolink-examples:: _setup_llm
         :collapse:


   .. py:method:: batch_classify(contents: list[str], contexts: list[dict[str, Any]] | None = None) -> list[haive.agents.memory.core.types.MemoryClassificationResult]

      Classify multiple memories in batch for efficiency.

      :param contents: List of memory contents to classify
      :param contexts: Optional list of contexts for each memory

      :returns: List of MemoryClassificationResult for each content


      .. autolink-examples:: batch_classify
         :collapse:


   .. py:method:: classify_memory(content: str, user_context: dict[str, Any] | None = None, conversation_context: dict[str, Any] | None = None) -> haive.agents.memory.core.types.MemoryClassificationResult

      Classify a single memory content into types and extract metadata.

      :param content: Memory content to classify
      :param user_context: Optional user context for classification
      :param conversation_context: Optional conversation context

      :returns: MemoryClassificationResult with types, importance, and metadata


      .. autolink-examples:: classify_memory
         :collapse:


   .. py:method:: classify_query_intent(query: str) -> haive.agents.memory.core.types.MemoryQueryIntent

      Analyze user query to determine memory retrieval intent.

      :param query: User query to analyze

      :returns: MemoryQueryIntent with retrieval strategy and parameters


      .. autolink-examples:: classify_query_intent
         :collapse:


   .. py:method:: create_memory_entry(content: str, user_context: dict[str, Any] | None = None, conversation_context: dict[str, Any] | None = None, namespace: str | None = None) -> haive.agents.memory.core.types.MemoryEntry

      Create a complete memory entry with automatic classification.

      :param content: Memory content
      :param user_context: Optional user context
      :param conversation_context: Optional conversation context
      :param namespace: Optional memory namespace

      :returns: MemoryEntry with full classification and metadata


      .. autolink-examples:: create_memory_entry
         :collapse:


   .. py:attribute:: config


.. py:class:: MemoryClassifierConfig(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Configuration for memory classification system.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MemoryClassifierConfig
      :collapse:

   .. py:attribute:: batch_size
      :type:  int
      :value: None



   .. py:attribute:: confidence_threshold
      :type:  float
      :value: None



   .. py:attribute:: enable_entity_extraction
      :type:  bool
      :value: None



   .. py:attribute:: enable_sentiment_analysis
      :type:  bool
      :value: None



   .. py:attribute:: enable_topic_modeling
      :type:  bool
      :value: None



   .. py:attribute:: importance_threshold_critical
      :type:  float
      :value: None



   .. py:attribute:: importance_threshold_high
      :type:  float
      :value: None



   .. py:attribute:: llm_config
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: max_content_length
      :type:  int
      :value: None



.. py:data:: logger

