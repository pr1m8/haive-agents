agents.patterns.hybrid_multi_agent_patterns
===========================================

.. py:module:: agents.patterns.hybrid_multi_agent_patterns

.. autoapi-nested-parse::

   Hybrid Multi-Agent Patterns - Advanced compositions using base patterns.

   This module demonstrates advanced multi-agent patterns that combine different
   agent types and execution modes, using the base agent.py and SimpleAgentV3
   patterns as building blocks.

   Patterns include:
   1. Parallel-then-Sequential workflows
   2. Conditional routing with multiple branches
   3. Hierarchical agent structures
   4. Dynamic agent composition


   .. autolink-examples:: agents.patterns.hybrid_multi_agent_patterns
      :collapse:


Classes
-------

.. autoapisummary::

   agents.patterns.hybrid_multi_agent_patterns.AdaptiveMultiAgent
   agents.patterns.hybrid_multi_agent_patterns.CollaborativeMultiAgent
   agents.patterns.hybrid_multi_agent_patterns.HybridMultiAgent
   agents.patterns.hybrid_multi_agent_patterns.ParallelResults
   agents.patterns.hybrid_multi_agent_patterns.TaskClassification


Functions
---------

.. autoapisummary::

   agents.patterns.hybrid_multi_agent_patterns.create_adaptive_agent
   agents.patterns.hybrid_multi_agent_patterns.create_collaborative_agent
   agents.patterns.hybrid_multi_agent_patterns.create_hybrid_agent
   agents.patterns.hybrid_multi_agent_patterns.example_adaptive_processing
   agents.patterns.hybrid_multi_agent_patterns.example_collaborative
   agents.patterns.hybrid_multi_agent_patterns.example_hybrid_classify_process


Module Contents
---------------

.. py:class:: AdaptiveMultiAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Adaptive multi-agent that changes behavior based on context.

   This agent dynamically adjusts its execution pattern based on
   input characteristics and intermediate results.


   .. autolink-examples:: AdaptiveMultiAgent
      :collapse:

   .. py:method:: _setup_adaptation_rules()

      Setup default adaptation rules.


      .. autolink-examples:: _setup_adaptation_rules
         :collapse:


   .. py:attribute:: adaptation_rules
      :type:  dict[str, collections.abc.Callable]
      :value: None



.. py:class:: CollaborativeMultiAgent(**kwargs)

   Bases: :py:obj:`haive.agents.multi.agent.MultiAgent`


   Collaborative multi-agent where agents work together.

   Agents share information and build on each other's work.


   .. autolink-examples:: CollaborativeMultiAgent
      :collapse:

   .. py:method:: _setup_collaboration()

      Setup collaboration edges.


      .. autolink-examples:: _setup_collaboration
         :collapse:


   .. py:attribute:: collaboration_mode
      :type:  str
      :value: None



.. py:class:: HybridMultiAgent

   Bases: :py:obj:`haive.agents.base.agent.Agent`


   Hybrid multi-agent with mixed execution patterns.

   This agent can combine parallel and sequential execution,
   conditional routing, and dynamic agent selection.

   .. rubric:: Example

   >>> agent = HybridMultiAgent(
   ...     name="hybrid_processor",
   ...     initial_agents=[classifier],
   ...     processing_agents=[simple_proc, complex_proc, research_proc],
   ...     synthesis_agents=[combiner, formatter],
   ...     execution_pattern="classify_then_process"
   ... )


   .. autolink-examples:: HybridMultiAgent
      :collapse:

   .. py:method:: _build_classify_then_process(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build classification followed by conditional processing.


      .. autolink-examples:: _build_classify_then_process
         :collapse:


   .. py:method:: _build_hierarchical(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)
      :abstractmethod:


      Build hierarchical agent structure.


      .. autolink-examples:: _build_hierarchical
         :collapse:


   .. py:method:: _build_parallel_then_sequential(graph: haive.core.graph.state_graph.base_graph2.BaseGraph)

      Build parallel execution followed by sequential synthesis.


      .. autolink-examples:: _build_parallel_then_sequential
         :collapse:


   .. py:method:: _create_classifier_agent() -> haive.agents.simple.agent.SimpleAgent

      Create task classifier agent.


      .. autolink-examples:: _create_classifier_agent
         :collapse:


   .. py:method:: _create_complex_processor() -> haive.agents.react.agent.ReactAgent

      Create complex task processor with tools.


      .. autolink-examples:: _create_complex_processor
         :collapse:


   .. py:method:: _create_formatter_agent() -> haive.agents.simple.agent.SimpleAgent

      Create final formatter agent.


      .. autolink-examples:: _create_formatter_agent
         :collapse:


   .. py:method:: _create_research_processor() -> haive.agents.react.agent.ReactAgent

      Create research processor with tools.


      .. autolink-examples:: _create_research_processor
         :collapse:


   .. py:method:: _create_simple_processor() -> haive.agents.simple.agent.SimpleAgent

      Create simple task processor.


      .. autolink-examples:: _create_simple_processor
         :collapse:


   .. py:method:: _create_synthesis_agent() -> haive.agents.simple.agent.SimpleAgent

      Create synthesis agent.


      .. autolink-examples:: _create_synthesis_agent
         :collapse:


   .. py:method:: build_graph() -> haive.core.graph.state_graph.base_graph2.BaseGraph

      Build hybrid execution graph.


      .. autolink-examples:: build_graph
         :collapse:


   .. py:method:: setup_agent() -> None

      Setup hybrid agent structure.


      .. autolink-examples:: setup_agent
         :collapse:


   .. py:attribute:: execution_pattern
      :type:  str
      :value: None



   .. py:attribute:: initial_agents
      :type:  list[haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: processing_agents
      :type:  list[haive.agents.base.agent.Agent]
      :value: None



   .. py:attribute:: routing_function
      :type:  collections.abc.Callable | None
      :value: None



   .. py:attribute:: synthesis_agents
      :type:  list[haive.agents.base.agent.Agent]
      :value: None



.. py:class:: ParallelResults(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Results from parallel agent execution.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ParallelResults
      :collapse:

   .. py:attribute:: agent_outputs
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: confidence_scores
      :type:  dict[str, float]
      :value: None



   .. py:attribute:: consensus_points
      :type:  list[str]
      :value: None



   .. py:attribute:: divergent_points
      :type:  list[str]
      :value: None



.. py:class:: TaskClassification(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Task classification result.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskClassification
      :collapse:

   .. py:attribute:: complexity_score
      :type:  float
      :value: None



   .. py:attribute:: recommended_approach
      :type:  str
      :value: None



   .. py:attribute:: required_capabilities
      :type:  list[str]
      :value: None



   .. py:attribute:: task_type
      :type:  str
      :value: None



.. py:function:: create_adaptive_agent(name: str = 'adaptive', debug: bool = True) -> AdaptiveMultiAgent

   Create an adaptive multi-agent.


   .. autolink-examples:: create_adaptive_agent
      :collapse:

.. py:function:: create_collaborative_agent(name: str = 'collaborative', collaboration_mode: str = 'consensus', debug: bool = True) -> CollaborativeMultiAgent

   Create a collaborative multi-agent.


   .. autolink-examples:: create_collaborative_agent
      :collapse:

.. py:function:: create_hybrid_agent(name: str = 'hybrid', execution_pattern: str = 'classify_then_process', debug: bool = True) -> HybridMultiAgent

   Create a hybrid multi-agent.


   .. autolink-examples:: create_hybrid_agent
      :collapse:

.. py:function:: example_adaptive_processing()
   :async:


   Example of adaptive processing.


   .. autolink-examples:: example_adaptive_processing
      :collapse:

.. py:function:: example_collaborative()
   :async:


   Example of collaborative multi-agent.


   .. autolink-examples:: example_collaborative
      :collapse:

.. py:function:: example_hybrid_classify_process()
   :async:


   Example of classification-based processing.


   .. autolink-examples:: example_hybrid_classify_process
      :collapse:

