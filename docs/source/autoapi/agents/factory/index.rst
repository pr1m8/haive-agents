agents.factory
==============

.. py:module:: agents.factory


Functions
---------

.. autoapisummary::

   agents.factory.create_simple_agent


Module Contents
---------------

.. py:function:: create_simple_agent(name: str, system_message: str = 'You are a helpful assistant', model: str = 'gpt-4o', use_chat_history: bool = True, persistence_config: Any | None = None, **kwargs) -> haive.agents.simple.config.SimpleAgentConfig

   Factory function to create a SimpleAgent configuration.

   :param name: Name for the agent
   :param system_message: System message/instructions for the agent
   :param model: Model to use (default: gpt-4o)
   :param use_chat_history: Whether to use chat history
   :param persistence_config: Optional persistence configuration
   :param \*\*kwargs: Additional parameters for SimpleAgentConfig

   :returns: Configured SimpleAgentConfig


   .. autolink-examples:: create_simple_agent
      :collapse:

