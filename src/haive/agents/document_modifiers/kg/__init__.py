"""Knowledge Graph document modifiers.

This module provides tools for transforming documents into knowledge graphs.
"""

# Import classes from submodules

try:
    from haive.agents.document_modifiers.kg.kg_base.kg_transformer import ParallelKGTransformer
    from haive.agents.document_modifiers.kg.kg_iterative_refinement.iterative_graph_transformer import (
        IterativeGraphTransformer,
        StructuredKGAgent,
    )
    from haive.agents.document_modifiers.kg.kg_map_merge.structured_kg_agent import (
        StructuredKGAgent as MapMergeStructuredKGAgent,
    )


except ImportError:
    ParallelKGTransformer = None

try:
    pass
except ImportError:
    IterativeGraphTransformer = None

try:
    pass
except ImportError:
    StructuredKGAgent = None

__all__ = [
    "IterativeGraphTransformer",
    "ParallelKGTransformer",
    "StructuredKGAgent",
]
