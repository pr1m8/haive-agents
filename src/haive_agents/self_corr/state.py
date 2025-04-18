from haive_agents.rag.base.config import BaseRAGState
from pydantic import Field
from typing import Dict, Any, List, Optional
from langchain_core.documents import Document

class SelfCorrectiveRAGState(BaseRAGState):
    """
    State schema for self-corrective RAG agents.
    
    Extends the base RAG state with fields for tracking answer quality,
    correction iterations, and assessment of hallucinations.
    """
    # Document filtering fields
    filtered_documents: List[Document] = Field(
        default_factory=list,
        description="Documents filtered for relevance"
    )
    
    relevance_scores: Dict[str, float] = Field(
        default_factory=dict,
        description="Relevance scores for documents"
    )
    
    # Evaluation fields
    answer_score: float = Field(
        default=0.0, 
        description="Quality score for the generated answer (0.0 to 1.0)"
    )
    
    correction_iterations: int = Field(
        default=0, 
        description="Number of correction iterations performed"
    )
    
    hallucination_assessment: Dict[str, Any] = Field(
        default_factory=dict, 
        description="Assessment of hallucinations in the answer"
    )
    
    final_answer: bool = Field(
        default=False, 
        description="Whether this is the final answer"
    )
    
    # Final output fields
    final_confidence: Optional[float] = Field(
        default=None,
        description="Final confidence score in the answer"
    )
