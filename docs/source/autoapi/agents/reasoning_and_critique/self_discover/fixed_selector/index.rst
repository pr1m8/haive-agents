agents.reasoning_and_critique.self_discover.fixed_selector
==========================================================

.. py:module:: agents.reasoning_and_critique.self_discover.fixed_selector

.. autoapi-nested-parse::

   Fixed SelfDiscoverSelector that properly handles prompt template variables.


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.fixed_selector
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.fixed_selector.logger


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.fixed_selector.FixedSelfDiscoverSelector


Module Contents
---------------

.. py:class:: FixedSelfDiscoverSelector

   Bases: :py:obj:`SimpleAgentV3`


   Fixed version of SelfDiscoverSelector that properly passes prompt variables.


   .. autolink-examples:: FixedSelfDiscoverSelector
      :collapse:

   .. py:method:: _prepare_input(input_data: Any) -> Any

      Override to properly format the prompt with all variables.


      .. autolink-examples:: _prepare_input
         :collapse:


   .. py:attribute:: engine
      :type:  haive.core.engine.aug_llm.AugLLMConfig
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: prompt_template
      :type:  langchain_core.prompts.ChatPromptTemplate
      :value: None



.. py:data:: logger

