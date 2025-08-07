# Examples and Tests Organization Plan

**Purpose**: Reorganize the haive-agents examples, demos, and tests for better discoverability and maintenance
**Date**: August 7, 2025

## 🎯 Goals

1. **Clear Separation**: Distinguish between examples, demos, tests, and experiments
2. **Progressive Learning**: Organize by skill level (beginner → intermediate → advanced)
3. **Topic-Based Grouping**: Group related functionality together
4. **Easy Discovery**: Clear entry points and navigation
5. **Maintainability**: Reduce duplication and improve consistency

## 📁 Proposed New Structure

### examples/

**Purpose**: Runnable examples for learning and reference

```
examples/
├── README.md                           # Main examples index
├── 01_getting_started/                 # Beginner examples
│   ├── README.md
│   ├── simple_agent_basic.py
│   ├── react_agent_with_tools.py
│   └── structured_output_basics.py
├── 02_single_agents/                   # Single agent patterns
│   ├── README.md
│   ├── agent_with_hooks.py
│   ├── agent_with_memory.py
│   ├── agent_with_custom_state.py
│   └── funky_prompt_templates.py      # MOVE FROM multi_agent_v4/
├── 03_multi_agents/                    # Multi-agent workflows
│   ├── README.md
│   ├── sequential_workflow.py         # ReactAgent → SimpleAgent
│   ├── parallel_workflow.py
│   ├── conditional_routing.py         # Clean branching example
│   ├── dynamic_routing.py             # Dynamic branching agent
│   └── complex_coordination.py
├── 04_specialized/                     # Domain-specific examples
│   ├── README.md
│   ├── rag_workflows/
│   │   ├── simple_rag.py
│   │   ├── agentic_rag.py
│   │   └── multi_agent_rag.py
│   ├── planning_agents/
│   │   ├── plan_and_execute.py
│   │   └── self_discover.py
│   ├── research_agents/
│   │   ├── web_researcher.py
│   │   └── document_analyzer.py
│   └── memory_agents/
│       ├── conversation_memory.py
│       └── long_term_memory.py
├── 05_advanced/                        # Advanced patterns
│   ├── README.md
│   ├── dynamic_tool_generation.py
│   ├── meta_agent_patterns.py
│   ├── custom_validation_nodes.py
│   └── enterprise_workflows.py
└── 06_integrations/                    # External integrations
    ├── README.md
    ├── supabase_persistence.py
    ├── mcp_integration.py
    └── vector_stores.py
```

### demos/

**Purpose**: Complete applications showcasing real-world usage

```
demos/
├── README.md                           # Demos index
├── customer_service_bot/
│   ├── README.md
│   ├── main.py
│   ├── agents/
│   └── requirements.txt
├── research_assistant/
│   ├── README.md
│   ├── main.py
│   └── components/
├── content_creation_pipeline/
│   ├── README.md
│   ├── workflow.py
│   └── agents/
└── game_playing_agents/
    ├── README.md
    ├── chess_agent.py
    └── strategy_games.py
```

### tests/

**Purpose**: Proper test organization by functionality

```
tests/
├── README.md                           # Testing guide
├── conftest.py                         # Shared fixtures
├── unit/                               # Unit tests
│   ├── agents/
│   │   ├── test_simple_agent.py
│   │   ├── test_react_agent.py
│   │   └── test_multi_agent.py
│   ├── base/
│   │   ├── test_hooks.py
│   │   └── test_mixins.py
│   └── utils/
├── integration/                        # Integration tests
│   ├── test_agent_workflows.py
│   ├── test_persistence.py
│   └── test_memory_systems.py
├── e2e/                               # End-to-end tests
│   ├── test_complete_workflows.py
│   └── test_real_llm_execution.py
└── performance/                        # Performance tests
    ├── test_agent_latency.py
    └── test_memory_usage.py
```

### experiments/

**Purpose**: Experimental code and research

```
experiments/
├── README.md                           # Experiments index
├── structured_output/                  # Our recent work
│   ├── automatic_extraction.py
│   ├── handler_patterns.py
│   └── validation_experiments.py
├── agent_architectures/
│   ├── meta_agents.py
│   └── hierarchical_agents.py
└── performance_optimizations/
    ├── lazy_loading.py
    └── caching_strategies.py
```

## 🔄 Migration Strategy

### Phase 1: Core Organization (Priority 1)

1. Create new directory structure
2. Move key examples to appropriate locations:
   - `funky_prompt_templates.py` → `examples/02_single_agents/`
   - `final_branching_example.py` → `examples/03_multi_agents/conditional_routing.py`
   - `dynamic_branching_agent.py` → `examples/03_multi_agents/dynamic_routing.py`
   - Clean examples from `multi_agent_v4/` directory

### Phase 2: Test Reorganization (Priority 2)

1. Consolidate duplicate tests
2. Remove debug files from tests/
3. Organize by functionality, not file names
4. Create proper test fixtures

### Phase 3: Documentation (Priority 3)

1. Create comprehensive README files
2. Add cross-references between related examples
3. Create learning paths for different user types

### Phase 4: Cleanup (Priority 4)

1. Remove obsolete files
2. Archive experimental code appropriately
3. Clean up naming conventions

## 📋 File Consolidation Rules

### Keep (High Value)

- Working examples with good documentation
- Complete workflows demonstrating patterns
- Real LLM integration examples
- Performance benchmarks

### Archive (Historical Value)

- Debug files with valuable insights
- Experimental approaches that didn't work
- Version comparison files

### Remove (Low Value)

- Duplicate examples
- Incomplete implementations
- Debug files without documentation
- Files with only print statements

## 🎯 Entry Points

### For New Users

1. `examples/README.md` → Overview and learning path
2. `examples/01_getting_started/` → First examples to try
3. `demos/` → Complete applications

### For Developers

1. `tests/README.md` → Testing guide
2. `experiments/README.md` → Research and exploration
3. Individual package READMEs

### For Contributors

1. Contribution guidelines in each section
2. Template files for new examples
3. Testing requirements

## 🔗 Cross-References

Each example should reference:

- Related examples in other categories
- Relevant tests that validate the pattern
- Documentation in the main docs/
- Real-world demos that use the pattern

## 📊 Success Metrics

1. **Discoverability**: New users can find relevant examples quickly
2. **Learning Path**: Clear progression from simple to advanced
3. **Maintainability**: Reduced duplication and clear organization
4. **Testing**: Comprehensive test coverage with clear organization
5. **Documentation**: Each example has clear purpose and usage

## 🚀 Next Steps

1. **Create directory structure** with README files
2. **Move high-value examples** to new locations
3. **Consolidate tests** by functionality
4. **Update documentation** with new structure
5. **Create learning paths** for different user types

---

This organization will make the haive-agents package much more approachable for new users while maintaining the depth needed for advanced use cases.
