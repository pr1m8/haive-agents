
:py:mod:`pro_search.search.models`
==================================

.. py:module:: pro_search.search.models

Chat prompt templates for Perplexity-style search workflow.
from typing import Any, Dict
These prompts guide the LLM through reasoning, query generation, and synthesis.


.. autolink-examples:: pro_search.search.models
   :collapse:


Functions
---------

.. autoapisummary::

   pro_search.search.models.create_query_generation_aug_llm
   pro_search.search.models.create_reasoning_aug_llm
   pro_search.search.models.create_synthesis_aug_llm

.. py:function:: create_query_generation_aug_llm(llm_config: dict[str, Any])

   Create AugLLMConfig for query generation step.


   .. autolink-examples:: create_query_generation_aug_llm
      :collapse:

.. py:function:: create_reasoning_aug_llm(llm_config: dict[str, Any])

   Create AugLLMConfig for query reasoning step.


   .. autolink-examples:: create_reasoning_aug_llm
      :collapse:

.. py:function:: create_synthesis_aug_llm(llm_config: dict[str, Any])

   Create AugLLMConfig for synthesis step.


   .. autolink-examples:: create_synthesis_aug_llm
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: pro_search.search.models
   :collapse:
   
.. autolink-skip:: next
