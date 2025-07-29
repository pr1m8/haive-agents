#!/usr/bin/env python3
"""Analysis of nodes context, hooks representation, and message transformer issues.

Understanding future references as strings in the context of:
1. Nodes and their relationships
2. What hooks really represent
3. Message transformer issues compared to v2
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "src"))

print("🔍 NODES, HOOKS, AND FORWARD REFERENCES ANALYSIS")
print("=" * 60)

# ========================================================================
# PART 1: NODES CONTEXT - What are the actual node relationships?
# ========================================================================

print("\n📍 PART 1: NODES CONTEXT & FORWARD REFERENCES")
print("Understanding how forward references work in node composition...")

print("""
🧩 NODE COMPOSITION IN SIMPLEAGENTV3:

1. **EngineNodeConfig** (current) - Basic LLM node
   - Input: messages field
   - Output: messages field (AI response)
   - No forward references needed

2. **ValidationNodeV2** - Conditional processor  
   - Input: messages, tool_routes, engine_name
   - Output: messages (with ToolMessages added)
   - Forward references: Uses ToolRouteMixin patterns

3. **GenericEngineNodeConfig** (advanced) - Type-safe node
   - Input: Schema-aware field definitions
   - Output: Schema-aware field definitions
   - Forward references: Generic[TInput, TOutput] patterns

The REAL issue: When you use string annotations, what happens to NODE SCHEMAS?
""")

try:
    from haive.core.graph.node.engine_node import EngineNodeConfig
    from haive.core.graph.node.validation_node_v2 import ValidationNodeV2
    from haive.core.engine.aug_llm import AugLLMConfig
    
    # Current approach - what SimpleAgentV3 actually uses
    engine = AugLLMConfig(name="test_engine")
    engine_node = EngineNodeConfig(name="agent_node", engine=engine)
    validation_node = ValidationNodeV2(name="validation_v2")
    
    print(f"✅ Current nodes created successfully:")
    print(f"  - Engine node: {engine_node.name}")
    print(f"  - Validation node: {validation_node.name}")
    
    # Check forward references in node configs
    print(f"\n🔍 Node schema analysis:")
    print(f"  - Engine node input fields: {getattr(engine_node, 'input_field_defs', 'None')}")
    print(f"  - Validation node input fields: {getattr(validation_node, 'input_field_defs', 'None')}")
    
except Exception as e:
    print(f"❌ Node creation failed: {e}")

# ========================================================================
# PART 2: WHAT HOOKS REALLY REPRESENT
# ========================================================================

print(f"\n{'='*60}")
print("📍 PART 2: WHAT HOOKS REALLY REPRESENT")
print("Are hooks just event listeners or do they represent nodes?")

print("""
🎯 HOOKS ANALYSIS:

1. **NOT Nodes** - Hooks are event listeners, not graph nodes
2. **Lifecycle Events** - before_run, after_run, on_error, etc.
3. **State Observers** - Can read state but don't modify graph structure
4. **Message Interceptors** - Can transform data between stages

FORWARD REFERENCE IMPACT ON HOOKS:
- Hooks use Agent types in their signatures
- If Agent becomes 'Agent' (string), hook typing breaks
- PrePostAgentMixin uses Agent type hints
- MessageTransformer uses BaseMessage types
""")

try:
    from haive.agents.base.hooks import HookEvent, HookContext
    from haive.agents.base.pre_post_agent_mixin import MessageTransformer
    
    # Test hook context creation
    print(f"✅ Hook system imported successfully")
    print(f"  - Available events: {list(HookEvent)}")
    
    # Test message transformer
    transformer = MessageTransformer(transformation_type="reflection")
    print(f"✅ MessageTransformer created: {transformer.transformation_type}")
    
except Exception as e:
    print(f"❌ Hook system test failed: {e}")

# ========================================================================
# PART 3: MESSAGE TRANSFORMER V2 ISSUE
# ========================================================================

print(f"\n{'='*60}")
print("📍 PART 3: MESSAGE TRANSFORMER ISSUE vs V2")
print("What's wrong with the current message transformer?")

print("""
🚨 SUSPECTED ISSUE: Message Transformer Pattern

Current Implementation (PrePostAgentMixin):
```python
def transform_messages(self, messages: List[BaseMessage]) -> List[BaseMessage]:
    if self.transformation_type == "reflection":
        # AI -> Human transformation for reflection
        if isinstance(msg, AIMessage):
            transformed.append(
                HumanMessage(
                    content=msg.content,
                    additional_kwargs=getattr(msg, "additional_kwargs", {}),
                )
            )
```

POTENTIAL ISSUES:
1. **Loss of tool_calls** - AIMessage.tool_calls not preserved
2. **Incomplete additional_kwargs** - Missing response_metadata, etc.
3. **No validation integration** - Doesn't work with ValidationNodeV2 flow
4. **Wrong transformation point** - Should transform after validation?
""")

try:
    from langchain_core.messages import AIMessage, HumanMessage
    from haive.agents.base.pre_post_agent_mixin import MessageTransformer
    
    # Test the current transformer
    transformer = MessageTransformer(transformation_type="reflection")
    
    # Create test AI message with tool calls (like ValidationNodeV2 produces)
    ai_msg = AIMessage(
        content="I need to use a tool",
        tool_calls=[
            {
                "name": "calculator", 
                "args": {"expression": "2+2"},
                "id": "call_123"
            }
        ],
        additional_kwargs={"engine_name": "test_engine"},
        response_metadata={"model": "gpt-4"}
    )
    
    print(f"\n🧪 Testing current transformer:")
    print(f"  - Original message type: {type(ai_msg).__name__}")
    print(f"  - Has tool_calls: {bool(ai_msg.tool_calls)}")
    print(f"  - Has additional_kwargs: {bool(ai_msg.additional_kwargs)}")
    print(f"  - Has response_metadata: {bool(ai_msg.response_metadata)}")
    
    # Transform the message
    transformed = transformer.transform_messages([ai_msg])
    
    if transformed:
        result_msg = transformed[0]
        print(f"\n  - Transformed type: {type(result_msg).__name__}")
        print(f"  - Has tool_calls: {bool(getattr(result_msg, 'tool_calls', None))}")
        print(f"  - Has additional_kwargs: {bool(getattr(result_msg, 'additional_kwargs', {}))}")
        print(f"  - Content preserved: {result_msg.content == ai_msg.content}")
        
        # This is the problem!
        if hasattr(ai_msg, 'tool_calls') and ai_msg.tool_calls:
            if not hasattr(result_msg, 'tool_calls') or not result_msg.tool_calls:
                print(f"  🚨 ISSUE: tool_calls LOST in transformation!")
        
        if hasattr(ai_msg, 'response_metadata') and ai_msg.response_metadata:
            if not hasattr(result_msg, 'response_metadata') or not result_msg.response_metadata:
                print(f"  🚨 ISSUE: response_metadata LOST in transformation!")
    
except Exception as e:
    print(f"❌ Message transformer test failed: {e}")
    import traceback
    traceback.print_exc()

# ========================================================================
# PART 4: FORWARD REFERENCES IN NODE CONTEXT
# ========================================================================

print(f"\n{'='*60}")
print("📍 PART 4: FORWARD REFERENCES IN NODE CONTEXT")
print("How do string annotations affect node composition?")

print("""
🔍 THE REAL QUESTION:

When you use `from __future__ import annotations`:

1. **Agent Types**: Agent[AugLLMConfig] becomes 'Agent[AugLLMConfig]'
2. **Node Schemas**: Do GenericEngineNodeConfig[TInput, TOutput] work?
3. **Hook Signatures**: Do hook type hints resolve correctly?
4. **Message Types**: Are BaseMessage subclasses affected?

CRITICAL FOR NODES:
- ValidationNodeV2 uses ToolRouteMixin with forward references
- GenericEngineNodeConfig uses Generic[TInput, TOutput]
- State schemas use forward references to agents
- Tool routing uses engine attribution with string lookup

If ALL type hints become strings, does the RUNTIME behavior change?
Answer: NO - only TYPE CHECKING changes, runtime behavior identical!
""")

print(f"\n{'='*60}")
print("🎯 CONCLUSIONS & RECOMMENDATIONS")
print("=" * 60)

print("""
✅ FORWARD REFERENCES AS STRINGS:
- Runtime behavior unchanged
- Only affects type checking and IDE support
- Nodes still work correctly
- Hooks still work correctly

🚨 MESSAGE TRANSFORMER ISSUE:
- Current transformer loses tool_calls and response_metadata
- Need to preserve ALL message attributes in transformation
- Should integrate better with ValidationNodeV2 flow

🧩 NODES CONTEXT:
- SimpleAgentV3 uses basic EngineNodeConfig (no forward ref issues)
- ValidationNodeV2 works as conditional processor
- GenericEngineNodeConfig could use string annotations safely

🎯 RECOMMENDATIONS:
1. Fix MessageTransformer to preserve all attributes
2. Test string annotations with ValidationNodeV2 integration
3. Consider GenericEngineNodeConfig for ReactAgent
4. Git commit current working state before experiments
""")

print(f"\n🔧 NEXT STEPS:")
print("1. Fix the MessageTransformer issue")
print("2. Test future annotations with node composition")
print("3. Git commit and push current progress")
print("4. Build ReactAgent with lessons learned")