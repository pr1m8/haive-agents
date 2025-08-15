models.task_analysis.base
=========================

.. py:module:: models.task_analysis.base

.. autoapi-nested-parse::

   Base classes and enums for task complexity analysis.

   This module defines the fundamental building blocks for task complexity analysis
   including task representations, dependency types, and complexity classifications.


   .. autolink-examples:: models.task_analysis.base
      :collapse:


Attributes
----------

.. autoapisummary::

   models.task_analysis.base.ComplexityType


Classes
-------

.. autoapisummary::

   models.task_analysis.base.ComplexityLevel
   models.task_analysis.base.ComputationalComplexity
   models.task_analysis.base.DependencyNode
   models.task_analysis.base.DependencyType
   models.task_analysis.base.KnowledgeComplexity
   models.task_analysis.base.ResourceType
   models.task_analysis.base.SolvabilityStatus
   models.task_analysis.base.Task
   models.task_analysis.base.TaskStep
   models.task_analysis.base.TaskType
   models.task_analysis.base.TimeComplexity


Module Contents
---------------

.. py:class:: ComplexityLevel

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Overall complexity classification for tasks.

   .. attribute:: TRIVIAL

      Simple, single-step tasks (1-2 minutes)

   .. attribute:: SIMPLE

      Straightforward tasks with few steps (5-15 minutes)

   .. attribute:: MODERATE

      Multi-step tasks with some dependencies (30 minutes - 2 hours)

   .. attribute:: COMPLEX

      Involved tasks with multiple branches (2-8 hours)

   .. attribute:: COMPLICATED

      Sophisticated tasks requiring expertise (1-3 days)

   .. attribute:: EXPERT

      High-expertise tasks with uncertainty (weeks)

   .. attribute:: RESEARCH

      Unknown solution path, investigation required (months)

   .. attribute:: UNSOLVABLE

      Currently impossible or undefined problems

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ComplexityLevel
      :collapse:

   .. py:attribute:: COMPLEX
      :value: 'complex'



   .. py:attribute:: COMPLICATED
      :value: 'complicated'



   .. py:attribute:: EXPERT
      :value: 'expert'



   .. py:attribute:: MODERATE
      :value: 'moderate'



   .. py:attribute:: RESEARCH
      :value: 'research'



   .. py:attribute:: SIMPLE
      :value: 'simple'



   .. py:attribute:: TRIVIAL
      :value: 'trivial'



   .. py:attribute:: UNSOLVABLE
      :value: 'unsolvable'



.. py:class:: ComputationalComplexity

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Computational complexity classifications.

   .. attribute:: CONSTANT

      O(1) - Fixed time regardless of input size

   .. attribute:: LOGARITHMIC

      O(log n) - Scales logarithmically with input

   .. attribute:: LINEAR

      O(n) - Scales linearly with input size

   .. attribute:: LINEARITHMIC

      O(n log n) - Common in efficient algorithms

   .. attribute:: QUADRATIC

      O(n²) - Scales quadratically

   .. attribute:: POLYNOMIAL

      O(n^k) - Polynomial time complexity

   .. attribute:: EXPONENTIAL

      O(2^n) - Exponential time complexity

   .. attribute:: UNKNOWN

      Complexity cannot be determined

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ComputationalComplexity
      :collapse:

   .. py:attribute:: CONSTANT
      :value: 'constant'



   .. py:attribute:: EXPONENTIAL
      :value: 'exponential'



   .. py:attribute:: LINEAR
      :value: 'linear'



   .. py:attribute:: LINEARITHMIC
      :value: 'linearithmic'



   .. py:attribute:: LOGARITHMIC
      :value: 'logarithmic'



   .. py:attribute:: POLYNOMIAL
      :value: 'polynomial'



   .. py:attribute:: QUADRATIC
      :value: 'quadratic'



   .. py:attribute:: UNKNOWN
      :value: 'unknown'



.. py:class:: DependencyNode(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a dependency relationship between tasks or steps.

   .. attribute:: source_id

      ID of the source task/step

   .. attribute:: target_id

      ID of the target task/step

   .. attribute:: dependency_type

      Type of dependency relationship

   .. attribute:: condition

      Optional condition for conditional dependencies

   .. attribute:: weight

      Strength/importance of the dependency (0.0 to 1.0)

   .. attribute:: description

      Human-readable description of the dependency

   .. rubric:: Example

   .. code-block:: python

       dependency = DependencyNode(
       source_id="lookup_winner",
       target_id="lookup_birthday",
       dependency_type=DependencyType.SEQUENTIAL,
       weight=1.0,
       description="Must know winner before looking up their birthday"
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DependencyNode
      :collapse:

   .. py:method:: allows_parallelization() -> bool

      Check if this dependency allows parallel execution.

      :returns: True if source and target can run in parallel


      .. autolink-examples:: allows_parallelization
         :collapse:


   .. py:method:: creates_join_point() -> bool

      Check if this dependency creates a join point.

      :returns: True if this is a join dependency


      .. autolink-examples:: creates_join_point
         :collapse:


   .. py:method:: is_blocking() -> bool

      Check if this dependency creates a blocking relationship.

      :returns: True if the target cannot proceed without the source


      .. autolink-examples:: is_blocking
         :collapse:


   .. py:attribute:: condition
      :type:  str | None
      :value: None



   .. py:attribute:: dependency_type
      :type:  DependencyType
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: source_id
      :type:  str
      :value: None



   .. py:attribute:: target_id
      :type:  str
      :value: None



   .. py:attribute:: weight
      :type:  float
      :value: None



.. py:class:: DependencyType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of dependency relationships between tasks.

   .. attribute:: SEQUENTIAL

      Task B cannot start until Task A completes (A → B)

   .. attribute:: PARALLEL

      Tasks can execute simultaneously (A || B)

   .. attribute:: CONDITIONAL

      Task B only executes if Task A meets conditions (A ?→ B)

   .. attribute:: ITERATIVE

      Task B feeds back to Task A (A ↔ B)

   .. attribute:: JOIN

      Multiple tasks must complete before next task (A,B → C)

   .. attribute:: SPLIT

      One task creates multiple parallel branches (A → B,C)

   .. attribute:: OPTIONAL

      Task is optional based on conditions

   .. attribute:: ALTERNATIVE

      Either Task A or Task B, but not both (A ⊕ B)

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DependencyType
      :collapse:

   .. py:attribute:: ALTERNATIVE
      :value: 'alternative'



   .. py:attribute:: CONDITIONAL
      :value: 'conditional'



   .. py:attribute:: ITERATIVE
      :value: 'iterative'



   .. py:attribute:: JOIN
      :value: 'join'



   .. py:attribute:: OPTIONAL
      :value: 'optional'



   .. py:attribute:: PARALLEL
      :value: 'parallel'



   .. py:attribute:: SEQUENTIAL
      :value: 'sequential'



   .. py:attribute:: SPLIT
      :value: 'split'



.. py:class:: KnowledgeComplexity

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Knowledge complexity requirements.

   .. attribute:: BASIC

      General knowledge or simple lookup

   .. attribute:: INTERMEDIATE

      Domain-specific knowledge required

   .. attribute:: ADVANCED

      Deep expertise in specific domain

   .. attribute:: EXPERT

      Cutting-edge expertise, research-level knowledge

   .. attribute:: INTERDISCIPLINARY

      Knowledge across multiple domains

   .. attribute:: UNKNOWN

      Knowledge requirements unclear

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: KnowledgeComplexity
      :collapse:

   .. py:attribute:: ADVANCED
      :value: 'advanced'



   .. py:attribute:: BASIC
      :value: 'basic'



   .. py:attribute:: EXPERT
      :value: 'expert'



   .. py:attribute:: INTERDISCIPLINARY
      :value: 'interdisciplinary'



   .. py:attribute:: INTERMEDIATE
      :value: 'intermediate'



   .. py:attribute:: UNKNOWN
      :value: 'unknown'



.. py:class:: ResourceType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of resources required for task execution.

   .. attribute:: HUMAN

      Human expertise or labor

   .. attribute:: COMPUTATIONAL

      Computing resources

   .. attribute:: DATA

      Access to specific datasets or information

   .. attribute:: TOOLS

      Specialized tools or software

   .. attribute:: FINANCIAL

      Monetary resources

   .. attribute:: TIME

      Significant time investment

   .. attribute:: NETWORK

      Network access or connectivity

   .. attribute:: STORAGE

      Data storage capabilities

   .. attribute:: EXPERTISE

      Specialized domain expertise

   .. attribute:: APPROVAL

      Authorization or approval from authorities

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ResourceType
      :collapse:

   .. py:attribute:: APPROVAL
      :value: 'approval'



   .. py:attribute:: COMPUTATIONAL
      :value: 'computational'



   .. py:attribute:: DATA
      :value: 'data'



   .. py:attribute:: EXPERTISE
      :value: 'expertise'



   .. py:attribute:: FINANCIAL
      :value: 'financial'



   .. py:attribute:: HUMAN
      :value: 'human'



   .. py:attribute:: NETWORK
      :value: 'network'



   .. py:attribute:: STORAGE
      :value: 'storage'



   .. py:attribute:: TIME
      :value: 'time'



   .. py:attribute:: TOOLS
      :value: 'tools'



.. py:class:: SolvabilityStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Current solvability status of a task.

   .. attribute:: TRIVIAL

      Task is trivially solvable with basic knowledge/tools

   .. attribute:: READY

      Task is immediately solvable with available resources

   .. attribute:: FEASIBLE

      Task is solvable with some effort or resource acquisition

   .. attribute:: CHALLENGING

      Task is solvable but requires significant effort

   .. attribute:: THEORETICAL

      Task is theoretically solvable but practically difficult

   .. attribute:: RESEARCH

      Task requires research or unknown solution paths

   .. attribute:: IMPOSSIBLE

      Task is currently impossible given constraints

   .. attribute:: UNDEFINED

      Solvability cannot be determined

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: SolvabilityStatus
      :collapse:

   .. py:attribute:: CHALLENGING
      :value: 'challenging'



   .. py:attribute:: FEASIBLE
      :value: 'feasible'



   .. py:attribute:: IMPOSSIBLE
      :value: 'impossible'



   .. py:attribute:: READY
      :value: 'ready'



   .. py:attribute:: RESEARCH
      :value: 'research'



   .. py:attribute:: THEORETICAL
      :value: 'theoretical'



   .. py:attribute:: TRIVIAL
      :value: 'trivial'



   .. py:attribute:: UNDEFINED
      :value: 'undefined'



.. py:class:: Task(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a complex task that can contain subtasks and steps.

   This is the main building block for task complexity analysis.
   Tasks can contain either other Tasks or TaskSteps, creating a
   hierarchical structure that AutoTree can automatically handle.

   .. attribute:: name

      Descriptive name for the task

   .. attribute:: description

      Detailed description of the task

   .. attribute:: task_type

      Primary type of this task

   .. attribute:: subtasks

      List of subtasks and steps (Union type for AutoTree)

   .. attribute:: dependencies

      Dependency relationships

   .. attribute:: estimated_duration_minutes

      Total estimated duration

   .. attribute:: complexity_level

      Overall complexity assessment

   .. attribute:: required_resources

      Resources needed for the entire task

   .. attribute:: success_criteria

      How to measure successful completion

   .. rubric:: Example

   .. code-block:: python

       # Create a complex task with mixed subtasks and steps
       main_task = Task(
       name="Analyze Wimbledon Champion Age",
       description="Find recent champion, calculate age, and analyze",
       task_type=TaskType.RESEARCH,
       subtasks=[
       TaskStep(
       name="Find winner",
       description="Look up most recent Wimbledon champion",
       task_type=TaskType.FACTUAL
       ),
       Task(
       name="Age Analysis",
       description="Calculate and analyze age",
       task_type=TaskType.COMPUTATIONAL,
       subtasks=[
       TaskStep(name="Get birthday", ...),
       TaskStep(name="Calculate age", ...),
       TaskStep(name="Find square root", ...)
       ]
       )
       ]
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Task
      :collapse:

   .. py:method:: calculate_total_duration() -> float

      Calculate total estimated duration for all subtasks.

      :returns: Total duration in minutes


      .. autolink-examples:: calculate_total_duration
         :collapse:


   .. py:method:: create_auto_tree() -> haive.core.common.structures.tree.AutoTree

      Create an AutoTree representation of this task.

      :returns: AutoTree instance wrapping this task


      .. autolink-examples:: create_auto_tree
         :collapse:


   .. py:method:: get_all_steps() -> list[TaskStep]

      Get all TaskStep objects from the entire task hierarchy.

      :returns: Flattened list of all TaskStep objects


      .. autolink-examples:: get_all_steps
         :collapse:


   .. py:method:: get_all_tasks() -> list[Task]

      Get all Task objects from the hierarchy including self.

      :returns: List of all Task objects in the hierarchy


      .. autolink-examples:: get_all_tasks
         :collapse:


   .. py:method:: get_breadth() -> int

      Get the breadth (number of direct subtasks) of this task.

      :returns: Number of direct subtasks


      .. autolink-examples:: get_breadth
         :collapse:


   .. py:method:: get_max_depth() -> int

      Calculate the maximum depth of the task hierarchy.

      :returns: Maximum depth (0 for leaf tasks)


      .. autolink-examples:: get_max_depth
         :collapse:


   .. py:method:: has_parallel_opportunities() -> bool

      Check if this task has opportunities for parallelization.

      :returns: True if some subtasks can potentially run in parallel


      .. autolink-examples:: has_parallel_opportunities
         :collapse:


   .. py:attribute:: can_be_parallelized
      :type:  bool
      :value: None



   .. py:attribute:: complexity_level
      :type:  ComplexityLevel | None
      :value: None



   .. py:attribute:: dependencies
      :type:  list[DependencyNode]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: estimated_duration_minutes
      :type:  float | None
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: priority
      :type:  int
      :value: None



   .. py:attribute:: required_resources
      :type:  list[ResourceType]
      :value: None



   .. py:attribute:: subtasks
      :type:  list[Union[Task, TaskStep]]
      :value: None



   .. py:attribute:: success_criteria
      :type:  list[str]
      :value: None



   .. py:attribute:: task_type
      :type:  TaskType
      :value: None



.. py:class:: TaskStep(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Individual executable step within a task.

   Represents an atomic unit of work that cannot be further decomposed
   in the current analysis context.

   .. attribute:: name

      Descriptive name for the step

   .. attribute:: description

      Detailed description of what the step involves

   .. attribute:: task_type

      The type of task this step represents

   .. attribute:: estimated_duration_minutes

      Estimated time to complete

   .. attribute:: required_resources

      Resources needed for this step

   .. attribute:: difficulty_level

      Subjective difficulty assessment

   .. attribute:: can_be_automated

      Whether this step can be automated

   .. attribute:: requires_human_judgment

      Whether human judgment is essential

   .. attribute:: dependencies

      IDs of other steps this depends on

   .. attribute:: outputs

      What this step produces

   .. rubric:: Example

   .. code-block:: python

       step = TaskStep(
       name="Look up Wimbledon winner",
       description="Search for the most recent Wimbledon men's singles champion",
       task_type=TaskType.FACTUAL,
       estimated_duration_minutes=5,
       required_resources=[ResourceType.NETWORK, ResourceType.DATA],
       can_be_automated=True
       )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskStep
      :collapse:

   .. py:method:: get_complexity_score() -> float

      Calculate a complexity score for this step.

      Combines duration, difficulty, and resource requirements.

      :returns: Complexity score (0.0 to 10.0)


      .. autolink-examples:: get_complexity_score
         :collapse:


   .. py:method:: get_duration_hours() -> float

      Get estimated duration in hours.

      :returns: Duration in hours


      .. autolink-examples:: get_duration_hours
         :collapse:


   .. py:method:: is_blocking() -> bool

      Check if this step blocks other steps.

      :returns: True if other steps depend on this one


      .. autolink-examples:: is_blocking
         :collapse:


   .. py:attribute:: can_be_automated
      :type:  bool
      :value: None



   .. py:attribute:: dependencies
      :type:  set[str]
      :value: None



   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: difficulty_level
      :type:  int
      :value: None



   .. py:attribute:: estimated_duration_minutes
      :type:  float
      :value: None



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: outputs
      :type:  list[str]
      :value: None



   .. py:attribute:: required_resources
      :type:  list[ResourceType]
      :value: None



   .. py:attribute:: requires_human_judgment
      :type:  bool
      :value: None



   .. py:attribute:: task_type
      :type:  TaskType
      :value: None



.. py:class:: TaskType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of tasks based on their fundamental nature.

   .. attribute:: FACTUAL

      Tasks requiring factual information lookup

   .. attribute:: COMPUTATIONAL

      Tasks involving calculations or data processing

   .. attribute:: RESEARCH

      Tasks requiring investigation and analysis

   .. attribute:: CREATIVE

      Tasks involving creative or generative work

   .. attribute:: DECISION

      Tasks requiring decision-making or judgment

   .. attribute:: COORDINATION

      Tasks involving coordination between multiple entities

   .. attribute:: COMMUNICATION

      Tasks involving information exchange

   .. attribute:: VERIFICATION

      Tasks involving validation or checking

   .. attribute:: SYNTHESIS

      Tasks combining multiple inputs into new outputs

   .. attribute:: ITERATIVE

      Tasks that require multiple cycles or refinement

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TaskType
      :collapse:

   .. py:attribute:: COMMUNICATION
      :value: 'communication'



   .. py:attribute:: COMPUTATIONAL
      :value: 'computational'



   .. py:attribute:: COORDINATION
      :value: 'coordination'



   .. py:attribute:: CREATIVE
      :value: 'creative'



   .. py:attribute:: DECISION
      :value: 'decision'



   .. py:attribute:: FACTUAL
      :value: 'factual'



   .. py:attribute:: ITERATIVE
      :value: 'iterative'



   .. py:attribute:: RESEARCH
      :value: 'research'



   .. py:attribute:: SYNTHESIS
      :value: 'synthesis'



   .. py:attribute:: VERIFICATION
      :value: 'verification'



.. py:class:: TimeComplexity

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Time complexity categories for task completion.

   .. attribute:: INSTANT

      Less than 1 minute

   .. attribute:: QUICK

      1-10 minutes

   .. attribute:: SHORT

      10-60 minutes

   .. attribute:: MEDIUM

      1-8 hours

   .. attribute:: LONG

      1-7 days

   .. attribute:: EXTENDED

      1-4 weeks

   .. attribute:: PROJECT

      1-6 months

   .. attribute:: RESEARCH

      6+ months or unknown timeline

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TimeComplexity
      :collapse:

   .. py:attribute:: EXTENDED
      :value: 'extended'



   .. py:attribute:: INSTANT
      :value: 'instant'



   .. py:attribute:: LONG
      :value: 'long'



   .. py:attribute:: MEDIUM
      :value: 'medium'



   .. py:attribute:: PROJECT
      :value: 'project'



   .. py:attribute:: QUICK
      :value: 'quick'



   .. py:attribute:: RESEARCH
      :value: 'research'



   .. py:attribute:: SHORT
      :value: 'short'



.. py:data:: ComplexityType

