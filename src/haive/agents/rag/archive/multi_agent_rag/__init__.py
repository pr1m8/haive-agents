"""Module exports - multi-agent RAG workflows.

Many submodules have optional dependencies. Imports are wrapped in try/except
so the package remains importable even when some dependencies are missing.
"""

import logging

logger = logging.getLogger(__name__)

__all__: list[str] = []

_import_blocks = [
    ("additional_workflows", "haive.agents.rag.multi_agent_rag.additional_workflows"),
    ("advanced_workflows", "haive.agents.rag.multi_agent_rag.advanced_workflows"),
    ("agents", "haive.agents.rag.multi_agent_rag.agents"),
    ("compatibility", "haive.agents.rag.multi_agent_rag.compatibility"),
    ("complete_rag_workflows", "haive.agents.rag.multi_agent_rag.complete_rag_workflows"),
    ("enhanced_multi_rag", "haive.agents.rag.multi_agent_rag.enhanced_multi_rag"),
    ("enhanced_state_schemas", "haive.agents.rag.multi_agent_rag.enhanced_state_schemas"),
    ("enhanced_workflows", "haive.agents.rag.multi_agent_rag.enhanced_workflows"),
    ("graded_rag_workflows", "haive.agents.rag.multi_agent_rag.graded_rag_workflows"),
    ("graded_rag_workflows_v2", "haive.agents.rag.multi_agent_rag.graded_rag_workflows_v2"),
    ("grading_components", "haive.agents.rag.multi_agent_rag.grading_components"),
    ("multi_rag", "haive.agents.rag.multi_agent_rag.multi_rag"),
    ("simple_enhanced_workflows", "haive.agents.rag.multi_agent_rag.simple_enhanced_workflows"),
    ("specialized_workflows", "haive.agents.rag.multi_agent_rag.specialized_workflows"),
    ("specialized_workflows_v2", "haive.agents.rag.multi_agent_rag.specialized_workflows_v2"),
    ("state", "haive.agents.rag.multi_agent_rag.state"),
]

for _name, _module_path in _import_blocks:
    try:
        __import__(_module_path)
    except (ImportError, Exception) as e:
        logger.debug("multi_agent_rag: failed to import %s: %s", _name, e)
