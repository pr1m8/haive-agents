agents.reasoning_and_critique.lats.agent
========================================

.. py:module:: agents.reasoning_and_critique.lats.agent


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.lats.agent.logger


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.lats.agent.LATSAgent
   agents.reasoning_and_critique.lats.agent.LATSAgentConfig


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.lats.agent.create_lats_agent


Module Contents
---------------

.. py:class:: LATSAgent

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`LATSAgentConfig`\ ]


   A Look-Ahead Tree Search (LATS) agent that uses tree search to.
   explore multiple response candidates and find optimal solutions.

   This agent builds a tree of possible responses and evaluates them
   using reflection to select the best path.


   .. autolink-examples:: LATSAgent
      :collapse:

   .. py:method:: _get_best_node(root: haive.agents.reasoning_and_critique.lats.models.Node) -> haive.agents.reasoning_and_critique.lats.models.Node

      Get the best node in the tree based on reflections.


      .. autolink-examples:: _get_best_node
         :collapse:


   .. py:method:: _is_solved(root: haive.agents.reasoning_and_critique.lats.models.Node) -> bool

      Check if a solution has been found in the tree.


      .. autolink-examples:: _is_solved
         :collapse:


   .. py:method:: _select(root: haive.agents.reasoning_and_critique.lats.models.Node) -> haive.agents.reasoning_and_critique.lats.models.Node

      Select the best leaf node for expansion using UCB1.


      .. autolink-examples:: _select
         :collapse:


   .. py:method:: run(input_text: str | dict[str, Any]) -> dict[str, Any]

      Run the LATS agent with the given input.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the LATS agent workflow graph.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: stream(input_text: str | dict[str, Any])

      Stream the LATS agent execution with the given input.


      .. autolink-examples:: stream
         :collapse:


.. py:class:: LATSAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for a Look-Ahead Tree Search (LATS) agent.
   This agent uses tree search to explore multiple response candidates
   and select the best one based on reflections.


   .. autolink-examples:: LATSAgentConfig
      :collapse:

   .. py:method:: from_scratch(system_prompt: str | None = None, tools: list[Any] | None = None, model: str = 'gpt-4o', temperature: float = 0.7, candidates_per_expansion: int = 5, max_tree_height: int = 5, name: str | None = None, **kwargs) -> LATSAgentConfig
      :classmethod:


      Create a LATSAgentConfig from scratch.

      :param system_prompt: Optional system prompt
      :param tools: Optional tools to use
      :param model: Model name to use
      :param temperature: Temperature for generation
      :param candidates_per_expansion: Number of candidates per expansion
      :param max_tree_height: Maximum tree height
      :param name: Optional agent name
      :param \*\*kwargs: Additional kwargs for the config

      :returns: LATSAgentConfig instance


      .. autolink-examples:: from_scratch
         :collapse:


   .. py:attribute:: candidates_per_expansion
      :type:  int
      :value: None



   .. py:attribute:: exploration_weight
      :type:  float
      :value: None



   .. py:attribute:: max_tree_height
      :type:  int
      :value: None



   .. py:attribute:: model
      :type:  str
      :value: None



   .. py:attribute:: reflection_prompt
      :type:  str
      :value: None



   .. py:attribute:: system_prompt
      :type:  str
      :value: None



   .. py:attribute:: temperature
      :type:  float
      :value: None



   .. py:attribute:: tools
      :type:  list[Any]
      :value: None



.. py:function:: create_lats_agent(system_prompt: str | None = None, tools: list[Any] | None = None, model: str = 'gpt-4o', temperature: float = 0.7, candidates_per_expansion: int = 5, max_tree_height: int = 5, name: str | None = None, **kwargs) -> LATSAgent

   Create a LATS agent with the specified configuration.

   :param system_prompt: Optional system prompt for generation
   :param tools: Optional tools to use
   :param model: Model to use
   :param temperature: Temperature for generation
   :param candidates_per_expansion: Number of candidates per expansion
   :param max_tree_height: Maximum tree height
   :param name: Optional agent name
   :param \*\*kwargs: Additional configuration parameters

   :returns: LATSAgent instance


   .. autolink-examples:: create_lats_agent
      :collapse:

.. py:data:: logger

