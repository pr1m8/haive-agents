"""Grade models for the Haive framework.

This module provides comprehensive grading capabilities including:
- Binary grades (pass/fail)
- Numeric grades with custom ranges
- Letter grades (A-F)
- Qualitative assessments
- Rubric-based grading
- Scale-based grading (Likert, satisfaction, etc.)
- Composite grades combining multiple methods
"""

from haive.agents.common.models.grade.base import Grade, GradeType
from haive.agents.common.models.grade.binary import BinaryGrade
from haive.agents.common.models.grade.composite import CompositeGrade
from haive.agents.common.models.grade.letter_grade import LetterGrade, LetterValue
from haive.agents.common.models.grade.numeric import NumericGrade, PercentageGrade
from haive.agents.common.models.grade.qualitative import (
    QualitativeGrade,
    QualityLevel,
    SentimentType,
)
from haive.agents.common.models.grade.rubric import RubricCriterion, RubricGrade
from haive.agents.common.models.grade.scale import LikertScale, SatisfactionScale, ScaleGrade

__all__ = [
    # Base classes and enums
    "Grade",
    "GradeType",
    # Grade implementations
    "BinaryGrade",
    "CompositeGrade",
    "LetterGrade",
    "NumericGrade",
    "PercentageGrade",
    "QualitativeGrade",
    "RubricGrade",
    "ScaleGrade",
    # Supporting enums and classes
    "LetterValue",
    "QualityLevel",
    "SentimentType",
    "RubricCriterion",
    "LikertScale",
    "SatisfactionScale",
]
