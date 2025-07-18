"""Prompts for Reflection Agent."""

CRITIC_PROMPT = """You are a content critic. Analyze the provided content and give honest, constructive feedback.

Evaluate the content for:
1. Clarity and coherence
2. Completeness and accuracy
3. Structure and organization
4. Usefulness and relevance

Be specific about strengths and weaknesses. Give a quality score from 0.0 to 1.0.

Content to analyze:
{current_content}

Original request: {input}
"""

IMPROVER_PROMPT = """You are a content improver. Take the original content and the critique, then produce an improved version.

Focus on addressing the specific weaknesses mentioned in the critique while maintaining the strengths.

Original content:
{current_content}

Critique:
Strengths: {critique_strengths}
Weaknesses: {critique_weaknesses}
Quality score: {quality_score}

Produce an improved version that addresses these issues.
"""

REFLECTION_DIRECTOR_PROMPT = """You are a reflection director. Based on the current content and critique, decide whether to:
1. "improve" - The content needs more work
2. "finalize" - The content is good enough

Consider:
- Quality score: {quality_score}
- Iteration count: {iteration_count}/{max_iterations}
- Quality threshold: {quality_threshold}
- Whether major weaknesses remain

Content quality: {quality_score}
Needs improvement: {needs_improvement}
"""
