
:py:mod:`agents.reasoning_and_critique.self_discover.example`
=============================================================

.. py:module:: agents.reasoning_and_critique.self_discover.example



Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.example.analyze_reasoning_process
   agents.reasoning_and_critique.self_discover.example.create_custom_domain_agent
   agents.reasoning_and_critique.self_discover.example.example_advanced_configuration
   agents.reasoning_and_critique.self_discover.example.example_compare_models
   agents.reasoning_and_critique.self_discover.example.example_logical_reasoning
   agents.reasoning_and_critique.self_discover.example.example_math_problem
   agents.reasoning_and_critique.self_discover.example.example_svg_interpretation
   agents.reasoning_and_critique.self_discover.example.run_batch_problems

.. py:function:: analyze_reasoning_process(agent_results: list[dict], output_file: str | None = None)

   Analyze the reasoning process across multiple problems to identify patterns.

   :param agent_results: List of results from run_batch_problems
   :param output_file: Optional file to save analysis


   .. autolink-examples:: analyze_reasoning_process
      :collapse:

.. py:function:: create_custom_domain_agent(domain: str, custom_modules: list[str] | None = None, model: str = 'gpt-4o') -> haive.agents.reasoning_and_critique.self_discover.agent2.SelfDiscoverAgent

   Create a SelfDiscover agent specialized for a particular domain.

   :param domain: Domain to specialize in (e.g., "math", "logic", "programming")
   :param custom_modules: Optional custom reasoning modules
   :param model: Model to use

   :returns: Specialized SelfDiscoverAgent


   .. autolink-examples:: create_custom_domain_agent
      :collapse:

.. py:function:: example_advanced_configuration()

   Example showing advanced configuration of the SelfDiscover agent.


   .. autolink-examples:: example_advanced_configuration
      :collapse:

.. py:function:: example_compare_models()

   Example comparing different models on the same problem.


   .. autolink-examples:: example_compare_models
      :collapse:

.. py:function:: example_logical_reasoning()

   Example using SelfDiscover for a logical reasoning problem.


   .. autolink-examples:: example_logical_reasoning
      :collapse:

.. py:function:: example_math_problem()

   Example using SelfDiscover on a math problem.


   .. autolink-examples:: example_math_problem
      :collapse:

.. py:function:: example_svg_interpretation()

   Example using SelfDiscover to interpret an SVG path.


   .. autolink-examples:: example_svg_interpretation
      :collapse:

.. py:function:: run_batch_problems(agent: haive.agents.reasoning_and_critique.self_discover.agent2.SelfDiscoverAgent, problems: list[str], output_file: str | None = None)

   Run a batch of problems through a SelfDiscover agent and optionally save results.

   :param agent: SelfDiscoverAgent to use
   :param problems: List of problem statements
   :param output_file: Optional file to save results


   .. autolink-examples:: run_batch_problems
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.reasoning_and_critique.self_discover.example
   :collapse:
   
.. autolink-skip:: next
