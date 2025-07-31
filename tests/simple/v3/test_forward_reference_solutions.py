#!/usr/bin/env python3
"""Test different solutions for forward reference issues in complex Pydantic inheritance.

Shows multiple approaches from best to worst.
"""

from pathlib import Path
import sys


# Direct imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))


# ========================================================================
# SOLUTION 1: from __future__ import annotations (BEST)
# ========================================================================


test_code_1 = """
from __future__ import annotations  # At very top of file

from typing import Any
from pydantic import BaseModel, Field
from haive.core.engine.aug_llm import AugLLMConfig

class Agent[AugLLMConfig]:  # Forward reference deferred
    engine: AugLLMConfig = Field(...)

class SimpleAgentV3(
    Agent[AugLLMConfig],    # This becomes a string annotation
    # Other mixins...
):
    pass

# NO model_rebuild() needed!
"""


# ========================================================================
# SOLUTION 2: String Annotations (MANUAL)
# ========================================================================


test_code_2 = """
class SimpleAgentV3(
    "Agent[AugLLMConfig]",  # Manual string annotation
    RecompileMixin,
    DynamicToolRouteMixin,
):
    pass
"""


# ========================================================================
# SOLUTION 3: TYPE_CHECKING Pattern
# ========================================================================


test_code_3 = """
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from haive.agents.base.enhanced_agent import Agent
else:
    from haive.agents.base.enhanced_agent import Agent as _Agent
    Agent = _Agent  # Runtime alias

class SimpleAgentV3(
    Agent[AugLLMConfig],  # Available in both contexts
    # Other mixins...
):
    pass
"""


# ========================================================================
# SOLUTION 4: Delayed Class Construction
# ========================================================================


test_code_4 = '''
def create_simple_agent_v3():
    """Create SimpleAgentV3 class after all imports available."""
    from haive.agents.base.enhanced_agent import Agent
    from haive.core.common.mixins.recompile_mixin import RecompileMixin
    # ... other imports

    class SimpleAgentV3(
        Agent[AugLLMConfig],
        RecompileMixin,
        DynamicToolRouteMixin,
    ):
        pass

    return SimpleAgentV3

# Call at end of module
SimpleAgentV3 = create_simple_agent_v3()
'''


# ========================================================================
# SOLUTION 5: model_rebuild() (CURRENT)
# ========================================================================


test_code_5 = """
class SimpleAgentV3(
    Agent[AugLLMConfig],
    RecompileMixin,
    DynamicToolRouteMixin,
):
    pass

# At end of file
try:
    SimpleAgentV3.model_rebuild()
except Exception as e:
    logger.warning(f"Failed to rebuild: {e}")
"""


# ========================================================================
# SOLUTION 6: Generic Type Aliases (ADVANCED)
# ========================================================================


test_code_6 = """
from typing import TypeAlias

# Create aliases after imports
AugLLMAgent: TypeAlias = Agent[AugLLMConfig]
RecompilableAgent: TypeAlias = type("RecompilableAgent", (AugLLMAgent, RecompileMixin), {})

class SimpleAgentV3(
    RecompilableAgent,
    DynamicToolRouteMixin,
):
    pass
"""
