"""Module exports."""

from haive.agents.document_modifiers.kg.kg_iterative_refinement.agent import (
    IterativeGraphTransformer,
)
from haive.agents.document_modifiers.kg.kg_iterative_refinement.config import (
    IterativeGraphTransformerConfig,
)
from haive.agents.document_modifiers.base.utils import normalize_contents
from haive.agents.document_modifiers.kg.kg_iterative_refinement.state import (
    IterativeGraphTransformerState,
)


# Create module-level function for compatibility
def should_refine(state: IterativeGraphTransformerState) -> str:
    """Check if the iterative refinement should continue."""
    return state.should_refine()


from haive.agents.document_modifiers.kg.kg_iterative_refinement.utils import (
    replace_empty_placeholders,
)

__all__ = [
    "IterativeGraphTransformer",
    "IterativeGraphTransformerConfig",
    "IterativeGraphTransformerState",
    "normalize_contents",
    "replace_empty_placeholders",
    "should_refine",
]
