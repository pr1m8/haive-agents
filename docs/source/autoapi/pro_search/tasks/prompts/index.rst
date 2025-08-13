
:py:mod:`pro_search.tasks.prompts`
==================================

.. py:module:: pro_search.tasks.prompts

Chat prompt templates for recursive conditional planning with tree-based decomposition.
from typing import Any, Dict
These prompts guide task decomposition, execution planning, and adaptive replanning.


.. autolink-examples:: pro_search.tasks.prompts
   :collapse:


Functions
---------

.. autoapisummary::

   pro_search.tasks.prompts.create_decomposition_aug_llm
   pro_search.tasks.prompts.create_execution_planning_aug_llm
   pro_search.tasks.prompts.create_replanning_analysis_aug_llm

.. py:function:: create_decomposition_aug_llm(llm_config: dict[str, Any])

   Create AugLLMConfig for task decomposition.


   .. autolink-examples:: create_decomposition_aug_llm
      :collapse:

.. py:function:: create_execution_planning_aug_llm(llm_config: dict[str, Any])

   Create AugLLMConfig for execution planning.


   .. autolink-examples:: create_execution_planning_aug_llm
      :collapse:

.. py:function:: create_replanning_analysis_aug_llm(llm_config: dict[str, Any])

   Create AugLLMConfig for replanning analysis.


   .. autolink-examples:: create_replanning_analysis_aug_llm
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: pro_search.tasks.prompts
   :collapse:
   
.. autolink-skip:: next
