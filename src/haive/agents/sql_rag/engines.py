from langchain_core.output_parsers import StrOutputParser

from haive.agents.rag.sql_rag.models import (
    GradeAnswer,
    GradeHallucinations,
    GuardrailsOutput,
    SQLAnalysisOutput,
    SQLQueryOutput,
    SQLValidationOutput,
)
from haive.agents.rag.sql_rag.prompts import (
    ANALYZE_QUERY_PROMPT,
    ANSWER_GRADING_PROMPT,
    GENERATE_FINAL_ANSWER_PROMPT,
    GENERATE_SQL_PROMPT,
    GUARDRAILS_PROMPT,
    HALLUCINATION_CHECK_PROMPT,
    VALIDATE_SQL_PROMPT,
)
from haive.core.engine.aug_llm.base import AugLLMConfig

# Engine for analyzing queries
analyze_query_aug_llm_config = AugLLMConfig(
    name="analyze_query_config",
    prompt_template=ANALYZE_QUERY_PROMPT,
    structured_output_model=SQLAnalysisOutput
)

# Engine for generating SQL
generate_sql_aug_llm_config = AugLLMConfig(
    name="generate_sql_config",
    prompt_template=GENERATE_SQL_PROMPT,
    structured_output_model=SQLQueryOutput
)

# Engine for validating SQL
validate_sql_aug_llm_config = AugLLMConfig(
    name="validate_sql_config",
    prompt_template=VALIDATE_SQL_PROMPT,
    structured_output_model=SQLValidationOutput
)

# Engine for guardrails
guardrails_aug_llm_config = AugLLMConfig(
    name="guardrails_config",
    prompt_template=GUARDRAILS_PROMPT,
    structured_output_model=GuardrailsOutput
)

# Engine for generating final answer
generate_final_answer_aug_llm_config = AugLLMConfig(
    name="generate_final_answer_config",
    prompt_template=GENERATE_FINAL_ANSWER_PROMPT,
    output_parser=StrOutputParser()
)

# Engine for hallucination checking
hallucination_check_aug_llm_config = AugLLMConfig(
    name="hallucination_check_config",
    prompt_template=HALLUCINATION_CHECK_PROMPT,
    structured_output_model=GradeHallucinations
)

# Engine for answer grading
answer_grading_aug_llm_config = AugLLMConfig(
    name="answer_grading_config",
    prompt_template=ANSWER_GRADING_PROMPT,
    structured_output_model=GradeAnswer
)

# Default engines configuration
default_sql_engines = {
    "analyze_query": analyze_query_aug_llm_config,
    "generate_sql": generate_sql_aug_llm_config,
    "validate_sql": validate_sql_aug_llm_config,
    "guardrails": guardrails_aug_llm_config,
    "generate_final_answer": generate_final_answer_aug_llm_config,
    "hallucination_check": hallucination_check_aug_llm_config,
    "answer_grading": answer_grading_aug_llm_config
}
