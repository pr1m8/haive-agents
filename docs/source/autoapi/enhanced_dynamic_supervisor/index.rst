enhanced_dynamic_supervisor
===========================

.. py:module:: enhanced_dynamic_supervisor

.. autoapi-nested-parse::

   Enhanced DynamicSupervisor implementation extending SupervisorAgent.

   DynamicSupervisor = SupervisorAgent + dynamic worker management + adaptive strategies.


   .. autolink-examples:: enhanced_dynamic_supervisor
      :collapse:


Attributes
----------

.. autoapisummary::

   enhanced_dynamic_supervisor.logger


Classes
-------

.. autoapisummary::

   enhanced_dynamic_supervisor.DynamicSupervisor
   enhanced_dynamic_supervisor.MockWorkerTemplate


Module Contents
---------------

.. py:class:: DynamicSupervisor

   Bases: :py:obj:`haive.agents.multi.enhanced_supervisor_agent.SupervisorAgent`


   Enhanced DynamicSupervisor with adaptive worker management.

   DynamicSupervisor extends SupervisorAgent with:
   1. Dynamic worker addition/removal during execution
   2. Worker performance tracking
   3. Adaptive delegation strategies
   4. Worker pooling and recycling

   .. attribute:: max_workers

      Maximum number of concurrent workers

   .. attribute:: min_workers

      Minimum number of workers to maintain

   .. attribute:: worker_performance

      Track worker performance metrics

   .. attribute:: auto_scale

      Enable automatic scaling based on load

   .. attribute:: recycling_enabled

      Enable worker recycling

   .. rubric:: Examples

   Dynamic scaling based on load::

       supervisor = DynamicSupervisor(
           name="auto_scaling_manager",
           min_workers=2,
           max_workers=10,
           auto_scale=True
       )

       # Starts with min workers, scales up as needed
       supervisor.add_worker("base_analyst", AnalystAgent())
       supervisor.add_worker("base_researcher", ResearchAgent())

       # During high load, automatically adds workers
       result = supervisor.run("Process 100 documents")

   Worker performance tracking::

       supervisor = DynamicSupervisor(
           name="performance_manager",
           track_performance=True
       )

       # After execution, check performance
       metrics = supervisor.get_worker_metrics()
       # Shows success rate, average time, task count per worker


   .. autolink-examples:: DynamicSupervisor
      :collapse:

   .. py:method:: __repr__() -> str

      String representation with dynamic info.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: add_worker_from_template(template_name: str, worker_name: str) -> bool

      Create and add a worker from template.

      :param template_name: Name of the template to use
      :param worker_name: Name for the new worker

      :returns: True if worker was added successfully


      .. autolink-examples:: add_worker_from_template
         :collapse:


   .. py:method:: assign_task(task_id: str, worker_name: str | None = None) -> str | None

      Assign a task to a worker.

      :param task_id: Unique task identifier
      :param worker_name: Specific worker to assign to (optional)

      :returns: Name of assigned worker or None


      .. autolink-examples:: assign_task
         :collapse:


   .. py:method:: can_add_worker() -> bool

      Check if more workers can be added.


      .. autolink-examples:: can_add_worker
         :collapse:


   .. py:method:: complete_task(task_id: str, success: bool = True, duration: float = 0.0) -> None

      Mark a task as completed.

      :param task_id: Task identifier
      :param success: Whether task succeeded
      :param duration: Task duration in seconds


      .. autolink-examples:: complete_task
         :collapse:


   .. py:method:: get_best_worker() -> str | None

      Get the best performing idle worker.


      .. autolink-examples:: get_best_worker
         :collapse:


   .. py:method:: get_worker_metrics() -> dict[str, dict[str, Any]]

      Get performance metrics for all workers.


      .. autolink-examples:: get_worker_metrics
         :collapse:


   .. py:method:: remove_idle_worker() -> str | None

      Remove an idle worker.

      :returns: Name of removed worker or None


      .. autolink-examples:: remove_idle_worker
         :collapse:


   .. py:method:: should_scale_down() -> bool

      Determine if should scale down workers.


      .. autolink-examples:: should_scale_down
         :collapse:


   .. py:method:: should_scale_up() -> bool

      Determine if should scale up workers.


      .. autolink-examples:: should_scale_up
         :collapse:


   .. py:method:: validate_min_workers(v: int, info) -> int
      :classmethod:


      Ensure min_workers <= max_workers.


      .. autolink-examples:: validate_min_workers
         :collapse:


   .. py:attribute:: active_tasks
      :type:  dict[str, str]
      :value: None



   .. py:attribute:: auto_scale
      :type:  bool
      :value: None



   .. py:attribute:: idle_workers
      :type:  set[str]
      :value: None



   .. py:attribute:: max_workers
      :type:  int
      :value: None



   .. py:attribute:: min_workers
      :type:  int
      :value: None



   .. py:attribute:: recycling_enabled
      :type:  bool
      :value: None



   .. py:attribute:: worker_performance
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: worker_templates
      :type:  dict[str, type]
      :value: None



   .. py:attribute:: worker_timeout
      :type:  float
      :value: None



.. py:class:: MockWorkerTemplate

   Template for creating workers.


   .. autolink-examples:: MockWorkerTemplate
      :collapse:

   .. py:attribute:: engine
      :value: None



.. py:data:: logger

