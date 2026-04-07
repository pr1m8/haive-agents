"""RAG (Retrieval-Augmented Generation) agents for the Haive framework.

Available agents:
- BaseRAGAgent: Foundation retriever with HuggingFace embeddings
- SimpleRAGAgent: Retriever + answer agent in sequence
- DynamicRAGAgent: Multi-source dynamic retrieval
- LLMRAGAgent: LLM-based RAG
- AgenticRAGAgent: ReactAgent with retrieval tools
- CorrectiveRAGAgent: Self-correcting retrieval
- SelfReflectiveRAGAgent: Reflective retrieval with grading
- SelfRouteRAGAgent: Query-aware retrieval routing
- StepBackRAGAgent: Abstract query generation for better retrieval
- HyDERAGAgent: Hypothetical document embeddings
- FLARERAGAgent: Forward-looking active retrieval
- MultiQueryRAGAgent: Multiple query variants
- RAGFusionAgent: Reciprocal rank fusion
- SpeculativeRAGAgent: Hypothesis + parallel verification
- DocumentGradingRAGAgent: Document relevance grading
- AdaptiveRAGAgent: Adaptive strategy selection
- QueryDecomposerAgent: Hierarchical query decomposition
- HallucinationGraderAgent: Output hallucination detection
- MemoryAwareRAGAgent: RAG with memory context
"""
