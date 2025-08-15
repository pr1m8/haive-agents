models.mixins
=============

.. py:module:: models.mixins


Classes
-------

.. autoapisummary::

   models.mixins.Reasoning


Module Contents
---------------

.. py:class:: Reasoning(*args, **kwargs)

   Bases: :py:obj:`pydantic.RootModel`


   A mixin for reasoning about the world.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Reasoning
      :collapse:

   .. py:attribute:: reasoning
      :value: []



