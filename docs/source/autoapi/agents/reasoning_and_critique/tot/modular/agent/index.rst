agents.reasoning_and_critique.tot.modular.agent
===============================================

.. py:module:: agents.reasoning_and_critique.tot.modular.agent


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.tot.modular.agent.logger


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.tot.modular.agent.ToTAgent


Module Contents
---------------

.. py:class:: ToTAgent

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.tot.modular.config.ToTAgentConfig`\ ]


   .. py:method:: _create_expand_node(state)


   .. py:method:: _create_prune_node(state)


   .. py:method:: _create_score_node(state)


   .. py:method:: get_state_value(state: dict | pydantic.BaseModel, key: str, default=None)


   .. py:method:: run(input_data: str | dict[str, Any], **kwargs) -> dict[str, Any]


   .. py:method:: setup_workflow() -> None


.. py:data:: logger

