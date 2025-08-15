agents.reasoning_and_critique.mcts.example
==========================================

.. py:module:: agents.reasoning_and_critique.mcts.example


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.mcts.example.logger
   agents.reasoning_and_critique.mcts.example.question


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.mcts.example.run_mcts_agent_example
   agents.reasoning_and_critique.mcts.example.setup_tavily_tool


Module Contents
---------------

.. py:function:: run_mcts_agent_example(question: str, tools: list[langchain_core.tools.BaseTool] | None = None) -> dict[str, Any]

   Run an example MCTS agent workflow with the given question.

   :param question: User question to answer
   :param tools: Optional list of tools to use

   :returns: Result of the agent run


   .. autolink-examples:: run_mcts_agent_example
      :collapse:

.. py:function:: setup_tavily_tool() -> langchain_core.tools.BaseTool

   Set up Tavily search tool.


   .. autolink-examples:: setup_tavily_tool
      :collapse:

.. py:data:: logger

.. py:data:: question
   :value: 'Generate a table with the average size and weight, as well as the oldest recorded instance for...


