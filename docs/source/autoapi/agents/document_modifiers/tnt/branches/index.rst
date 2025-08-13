
:py:mod:`agents.document_modifiers.tnt.branches`
================================================

.. py:module:: agents.document_modifiers.tnt.branches

Branch decision functions for taxonomy generation workflow.

This module contains functions that determine the flow of the taxonomy generation process
by making decisions about which branch of the workflow to follow next.

.. rubric:: Example

Basic usage of branch decision functions::

    state = TaxonomyGenerationState(...)
    next_node = should_review(state)
    # Returns either 'update_taxonomy' or 'review_taxonomy'


.. autolink-examples:: agents.document_modifiers.tnt.branches
   :collapse:


Functions
---------

.. autoapisummary::

   agents.document_modifiers.tnt.branches.should_review

.. py:function:: should_review(state: haive.agents.document_modifiers.tnt.state.TaxonomyGenerationState) -> str

   Determines whether to continue refining the taxonomy or proceed to review.

   This function compares the number of taxonomy revisions against the number of
   minibatches to decide if enough iterations have been performed to warrant a
   final review.

   :param state: The current state containing:
                 - minibatches: List of document batch indices
                 - clusters: List of taxonomy revisions
   :type state: TaxonomyGenerationState

   :returns:

             Next node name in the workflow:
                 - 'update_taxonomy': Continue refining if more minibatches need processing
                 - 'review_taxonomy': Proceed to final review if all minibatches processed
   :rtype: str

   .. rubric:: Example

   >>> state = TaxonomyGenerationState(minibatches=[[1,2], [3,4]], clusters=[[...]])
   >>> next_node = should_review(state)
   >>> print(next_node)
   'update_taxonomy'  # Since only one revision exists for two minibatches


   .. autolink-examples:: should_review
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: agents.document_modifiers.tnt.branches
   :collapse:
   
.. autolink-skip:: next
