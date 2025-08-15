agents.reasoning_and_critique.reflexion.agent
=============================================

.. py:module:: agents.reasoning_and_critique.reflexion.agent


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.reflexion.agent.ReflexionAgent


Module Contents
---------------

.. py:class:: ReflexionAgent(config: haive.agents.reflexion.config.ReflexionConfig = ReflexionConfig())

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.agents.reflexion.config.ReflexionConfig`\ ]


   Agent that uses Reflexion to answer questions.


   .. autolink-examples:: ReflexionAgent
      :collapse:

   .. py:method:: create_tool_node(tools: list[langchain_core.tools.BaseTool | collections.abc.Callable]) -> langgraph.prebuilt.ToolNode

      Create a tool node from a list of tools.

      :param tools: list of tools to create a tool node from

      :returns: a tool node from the list of tools
      :rtype: ToolNode


      .. autolink-examples:: create_tool_node
         :collapse:


   .. py:method:: final_answer(state: dict)

      Final answer tool.


      .. autolink-examples:: final_answer
         :collapse:


   .. py:method:: setup_workflow() -> None

      Setup the reflexion workflow graph.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: answer_writer


   .. py:attribute:: config
      :type:  haive.agents.reflexion.config.ReflexionConfig


   .. py:attribute:: event_loop_branch


   .. py:attribute:: responder


   .. py:attribute:: revisor


   .. py:attribute:: tool_node


