agents.reasoning_and_critique.self_discover.self_discover_simple_v4
===================================================================

.. py:module:: agents.reasoning_and_critique.self_discover.self_discover_simple_v4

.. autoapi-nested-parse::

   Self-Discover Simple V4 - Minimal implementation with proper state handling.

   This version:
   - Uses a single shared state dict
   - Each agent updates the state with its output
   - No complex state transformations
   - Clear, simple flow


   .. autolink-examples:: agents.reasoning_and_critique.self_discover.self_discover_simple_v4
      :collapse:


Attributes
----------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.MODULES


Classes
-------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.AdaptedModules
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.ModuleList
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.Plan
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.Solution


Functions
---------

.. autoapisummary::

   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.create_agents
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.create_self_discover_simple
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.main
   agents.reasoning_and_critique.self_discover.self_discover_simple_v4.run_self_discover


Module Contents
---------------

.. py:class:: AdaptedModules(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Adapted modules output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AdaptedModules
      :collapse:

   .. py:attribute:: adapted
      :type:  str
      :value: None



.. py:class:: ModuleList(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Selected modules output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ModuleList
      :collapse:

   .. py:attribute:: modules
      :type:  str
      :value: None



.. py:class:: Plan(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Reasoning plan output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Plan
      :collapse:

   .. py:attribute:: plan
      :type:  str
      :value: None



.. py:class:: Solution(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Final solution output.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Solution
      :collapse:

   .. py:attribute:: answer
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:function:: create_agents()

   Create the four agents for Self-Discover.


   .. autolink-examples:: create_agents
      :collapse:

.. py:function:: create_self_discover_simple()

   Create the Self-Discover agent.


   .. autolink-examples:: create_self_discover_simple
      :collapse:

.. py:function:: main()
   :async:


.. py:function:: run_self_discover(task: str, modules: str | None = None)
   :async:


   Run Self-Discover on a task.

   :param task: The task to solve
   :param modules: Optional custom modules (defaults to MODULES)

   :returns: Dict with the solution


   .. autolink-examples:: run_self_discover
      :collapse:

.. py:data:: MODULES
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """1. Pattern Analysis - Identify patterns and structures
      2. Logical Reasoning - Apply logic to solve problems
      3. Visual/Spatial - Understand spatial relationships
      4. Mathematical - Apply mathematical concepts
      5. Critical Thinking - Evaluate and analyze
      6. Problem Decomposition - Break down complex problems
      7. Hypothesis Testing - Test assumptions
      8. Comparative Analysis - Compare options
      9. Causal Reasoning - Understand cause and effect
      10. Systems Thinking - See the big picture"""

   .. raw:: html

      </details>



