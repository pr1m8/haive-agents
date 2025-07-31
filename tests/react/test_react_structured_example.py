"""Example: ReactAgent with Structured Output for Code Analysis."""

import asyncio
from typing import Dict, List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.patterns.sequential_with_structured_output import (
    SequentialAgentWithStructuredOutput,
    SequentialHooks,
)
from haive.agents.react.agent import ReactAgent


# Structured output models for code analysis
class CodeIssue(BaseModel):
    """A code issue found during analysis."""

    severity: str = Field(
        description="Severity level", pattern="^(critical|high|medium|low)$"
    )
    category: str = Field(
        description="Issue category (bug, performance, security, style)"
    )
    description: str = Field(description="Description of the issue")
    file_path: Optional[str] = Field(
        default=None, description="File where issue was found"
    )
    line_number: Optional[int] = Field(
        default=None, description="Line number if applicable"
    )
    suggestion: str = Field(description="Suggested fix or improvement")


class DependencyInfo(BaseModel):
    """Information about a dependency."""

    name: str = Field(description="Dependency name")
    version: str = Field(description="Current version")
    latest_version: Optional[str] = Field(
        default=None, description="Latest available version"
    )
    security_issues: bool = Field(
        default=False, description="Has known security issues"
    )
    update_recommendation: Optional[str] = Field(default=None)


class CodeAnalysisReport(BaseModel):
    """Comprehensive code analysis report."""

    # Overview
    project_name: str = Field(description="Name of the analyzed project")
    analysis_summary: str = Field(description="Brief summary of the analysis")
    overall_health_score: float = Field(
        description="Overall project health score", ge=0.0, le=10.0
    )

    # Issues found
    issues: List[CodeIssue] = Field(description="List of issues found during analysis")

    critical_issues_count: int = Field(
        description="Number of critical issues requiring immediate attention"
    )

    # Code metrics
    code_metrics: Dict[str, float] = Field(
        description="Code quality metrics",
        examples=[
            {
                "complexity": 5.2,
                "maintainability": 7.8,
                "test_coverage": 85.0,
                "duplication": 3.2,
            }
        ],
    )

    # Dependencies
    dependencies_analyzed: List[DependencyInfo] = Field(
        description="Dependencies analyzed"
    )

    outdated_dependencies: int = Field(description="Number of outdated dependencies")

    # Recommendations
    top_recommendations: List[str] = Field(
        description="Top recommendations for improvement", min_items=3, max_items=5
    )

    # Security
    security_score: str = Field(
        description="Security assessment", pattern="^(excellent|good|fair|poor)$"
    )

    security_recommendations: Optional[List[str]] = Field(
        default=None, description="Security-specific recommendations"
    )

    # Next steps
    immediate_actions: List[str] = Field(description="Actions to take immediately")

    long_term_improvements: List[str] = Field(
        description="Long-term improvement suggestions"
    )


# Mock tools for code analysis
@tool
def analyze_code_structure(project_path: str) -> str:
    """Analyze the structure and organization of the codebase."""
    return """Code structure analysis:
    - Well-organized module structure with clear separation of concerns
    - 15 main modules, 127 total Python files
    - Good use of packages and submodules
    - Some circular dependencies detected in the 'utils' module
    - Average file size: 250 lines (good)
    - Longest file: 1,200 lines (consider splitting)
    """


@tool
def check_code_quality(project_path: str) -> str:
    """Check code quality metrics including complexity and maintainability."""
    return """Code quality metrics:
    - Cyclomatic complexity: 5.2 (moderate)
    - Maintainability index: 72/100 (good)
    - Code duplication: 3.2% (acceptable)
    - Type hint coverage: 87% (very good)
    - Docstring coverage: 65% (needs improvement)
    - Found 3 functions with complexity > 15 (consider refactoring)
    """


@tool
def scan_dependencies(project_path: str) -> str:
    """Scan project dependencies for updates and vulnerabilities."""
    return """Dependency scan results:
    - Total dependencies: 24
    - Outdated dependencies: 5
      * requests: 2.28.0 → 2.31.0 (security update available)
      * pydantic: 1.10.0 → 2.5.0 (major update, breaking changes)
      * pytest: 7.1.0 → 7.4.0 (minor update)
      * numpy: 1.23.0 → 1.26.0 (performance improvements)
      * sqlalchemy: 1.4.0 → 2.0.0 (major update)
    - Security vulnerabilities: 1 (in requests 2.28.0)
    """


@tool
def run_security_check(project_path: str) -> str:
    """Run security analysis on the codebase."""
    return """Security analysis:
    - No hardcoded secrets detected
    - 2 potential SQL injection vulnerabilities (using string formatting)
    - Missing input validation in 3 API endpoints
    - All passwords properly hashed
    - API keys properly stored in environment variables
    - CORS configuration could be more restrictive
    - Rate limiting not implemented on public endpoints
    """


@tool
def analyze_test_coverage(project_path: str) -> str:
    """Analyze test coverage and testing patterns."""
    return """Test coverage analysis:
    - Overall coverage: 78%
    - Critical paths coverage: 92%
    - Unit tests: 156
    - Integration tests: 23
    - No tests for: utils/helpers.py, config/legacy.py
    - Slow tests: 5 tests take > 5 seconds
    - Test quality: Good use of mocks and fixtures
    """


async def analyze_codebase_with_structured_report():
    """Analyze a codebase and generate a structured report."""
    print("\n=== Code Analysis with Structured Report ===\n")

    # Create ReactAgent for code analysis
    react_agent = ReactAgent(
        name="code_analyzer",
        engine=AugLLMConfig(
            temperature=0.3,  # Low temperature for factual analysis
            system_message="""You are an expert code analyst. Use the available tools to thoroughly 
analyze the codebase and identify issues, metrics, and improvements. Be specific and actionable 
in your findings.""",
        ),
        tools=[
            analyze_code_structure,
            check_code_quality,
            scan_dependencies,
            run_security_check,
            analyze_test_coverage,
        ],
        verbose=True,  # Show reasoning process
    )

    # Custom prompt for structuring the report
    report_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a technical report specialist. Transform code analysis findings into a 
comprehensive, structured report that is actionable and prioritized.""",
            ),
            (
                "human",
                """Based on the following code analysis, create a comprehensive structured report:

Analysis Results:
{input_data}

Project Context:
{context}

Create a detailed report with:
- Clear summary and health score
- Categorized issues with severity
- Specific metrics and measurements  
- Actionable recommendations
- Security assessment
- Prioritized next steps

Ensure all findings are accurately represented and properly categorized.""",
            ),
        ]
    )

    # Hooks for custom processing
    def calculate_health_score(report: CodeAnalysisReport) -> CodeAnalysisReport:
        """Post-process to calculate health score based on findings."""
        # Simple health score calculation
        score = 10.0
        score -= report.critical_issues_count * 1.0
        score -= len([i for i in report.issues if i.severity == "high"]) * 0.5
        score -= report.outdated_dependencies * 0.2

        if report.security_score == "poor":
            score -= 2.0
        elif report.security_score == "fair":
            score -= 1.0

        report.overall_health_score = max(0.0, min(10.0, score))
        return report

    hooks = SequentialHooks(post_process=calculate_health_score)

    # Create sequential pattern
    analyzer = SequentialAgentWithStructuredOutput(
        first_agent=react_agent,
        structured_output_model=CodeAnalysisReport,
        structured_output_prompt=report_prompt,
        hooks=hooks,
        name="code_analysis_pipeline",
        debug=True,
    )

    # Run analysis
    result = await analyzer.arun(
        "Analyze the codebase at /home/user/my_project for code quality, security, and dependencies",
        context={
            "project_type": "Python web application",
            "team_size": "5 developers",
            "priority": "security and maintainability",
        },
    )

    # Display results
    print("\n📊 Code Analysis Report"rt")
    print(f"{'='*60}")
    print(f"Project: {result.project_name}")
    print(f"Health Score: {result.overall_health_score:.1f}/10.0")
    print(f"\nSummary: {result.analysis_summary}")

    print("\n🚨 Issues Found:"d:")
    print(f"- Critical: {result.critical_issues_count}")
    print(f"- Total: {len(result.issues)}")

    if result.critical_issues_count > 0:
        print("\nCritical Issues:")
        for issue in [i for i in result.issues if i.severity == "critical"][:3]:
            print(f"  • {issue.category}: {issue.description}")
            print(f"    Fix: {issue.suggestion}")

    print("\n📈 Code Metrics:"s:")
    for metric, value in list(result.code_metrics.items())[:4]:
        print(f"  • {metric}: {value}")

    print(f"\n🔒 Security: {result.security_score}")
    if result.security_recommendations:
        print("Security Recommendations:")
        for rec in result.security_recommendations[:2]:
            print(f"  • {rec}")

    print("\n📦 Dependencies:")
    print(f"  • Total: {len(result.dependencies_analyzed)}")
    print(f"  • Outdated: {result.outdated_dependencies}")

    print("\n⚡ Immediate Actions:")
    for action in result.immediate_actions[:3]:
        print(f"  1. {action}")

    print("\n🎯 Top Recommendations:")
    for i, rec in enumerate(result.top_recommendations[:3], 1):
        print(f"  {i}. {rec}")


if __name__ == "__main__":
    asyncio.run(analyze_codebase_with_structured_report())
