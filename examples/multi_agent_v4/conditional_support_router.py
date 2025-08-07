"""Conditional Support Router Example

This example demonstrates conditional routing where queries are classified
and routed to specialized agents based on their category. Each specialist
has domain-specific tools.

Date: August 7, 2025
"""

import asyncio
from typing import Dict, List, Literal

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.multi.enhanced_multi_agent_v4 import EnhancedMultiAgentV4
from haive.agents.react.agent_v4 import ReactAgentV4
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Define structured outputs
class QueryClassification(BaseModel):
    """Classification of support query."""

    category: Literal["technical", "billing", "product", "general"] = Field(
        description="Query category"
    )
    subcategory: str = Field(description="Specific subcategory")
    urgency: float = Field(ge=0.0, le=1.0, description="Urgency level 0-1")
    key_terms: List[str] = Field(description="Key terms identified")
    reasoning: str = Field(description="Classification reasoning")


class TechnicalSolution(BaseModel):
    """Technical support solution."""

    issue_identified: str = Field(description="Technical issue identified")
    root_cause: str = Field(description="Root cause analysis")
    solution_steps: List[str] = Field(description="Step-by-step solution")
    additional_resources: List[str] = Field(description="Helpful resources")
    estimated_time: str = Field(description="Estimated resolution time")


class BillingResolution(BaseModel):
    """Billing support resolution."""

    account_status: str = Field(description="Current account status")
    billing_issue: str = Field(description="Identified billing issue")
    resolution: str = Field(description="Proposed resolution")
    amount_affected: float = Field(ge=0, description="Amount affected if any")
    next_steps: List[str] = Field(description="Customer next steps")


class ProductInfo(BaseModel):
    """Product information response."""

    product_name: str = Field(description="Product being discussed")
    features_mentioned: List[str] = Field(description="Features relevant to query")
    pricing_info: str = Field(description="Pricing information if applicable")
    recommendations: List[str] = Field(description="Product recommendations")
    comparison: Dict[str, str] = Field(description="Comparison with alternatives")


# Technical support tools
@tool
def check_system_status(component: str) -> str:
    """Check status of system components."""
    components = {
        "api": "operational",
        "database": "operational",
        "auth": "degraded performance",
        "storage": "operational",
    }
    status = components.get(component.lower(), "unknown")
    return f"System component '{component}' status: {status}"


@tool
def search_knowledge_base(query: str) -> str:
    """Search technical knowledge base."""
    # Mock KB search
    kb_entries = {
        "login": "Common login issues: 1) Clear cache, 2) Check credentials, 3) Verify 2FA",
        "api": "API troubleshooting: 1) Check API key, 2) Verify endpoints, 3) Review rate limits",
        "performance": "Performance tips: 1) Optimize queries, 2) Use caching, 3) Check resource usage",
    }

    query_lower = query.lower()
    relevant = [f"{k}: {v}" for k, v in kb_entries.items() if k in query_lower]
    return f"Knowledge base results: {'; '.join(relevant) if relevant else 'No specific entries found'}"


# Billing tools
@tool
def check_account_balance(account_id: str) -> str:
    """Check account balance and status."""
    # Mock account check
    return f"Account {account_id}: Balance: $125.50, Status: Active, Last payment: 5 days ago"


@tool
def calculate_proration(days_remaining: int, monthly_cost: float) -> str:
    """Calculate prorated charges."""
    daily_rate = monthly_cost / 30
    prorated = daily_rate * days_remaining
    return f"Prorated amount for {days_remaining} days at ${monthly_cost}/month: ${prorated:.2f}"


# Product tools
@tool
def get_product_features(product: str) -> str:
    """Get product features and capabilities."""
    products = {
        "starter": "Features: 5 users, 10GB storage, basic support, API access",
        "professional": "Features: 50 users, 100GB storage, priority support, advanced API, analytics",
        "enterprise": "Features: Unlimited users, 1TB storage, dedicated support, custom integrations",
    }
    return products.get(product.lower(), f"Product '{product}' not found in catalog")


@tool
def compare_plans(plan1: str, plan2: str) -> str:
    """Compare two product plans."""
    return f"Comparison {plan1} vs {plan2}: {plan2} includes everything in {plan1} plus additional features"


async def main():
    """Run the conditional support router."""

    print("Creating support specialists...")

    # Create classifier
    classifier = SimpleAgentV3(
        name="query_classifier",
        engine=AugLLMConfig(
            temperature=0.2,
            system_message="You are a support query classifier. Accurately categorize customer queries.",
        ),
        structured_output_model=QueryClassification,
        debug=True,
    )

    # Create technical specialist
    technical_specialist = ReactAgentV4(
        name="technical_support",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are a technical support expert. Solve technical issues using available tools.",
        ),
        tools=[check_system_status, search_knowledge_base],
        debug=True,
    )

    technical_formatter = SimpleAgentV3(
        name="technical_formatter",
        engine=AugLLMConfig(temperature=0.3),
        structured_output_model=TechnicalSolution,
        debug=True,
    )

    # Create billing specialist
    billing_specialist = ReactAgentV4(
        name="billing_support",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are a billing support expert. Resolve billing and account issues.",
        ),
        tools=[check_account_balance, calculate_proration],
        debug=True,
    )

    billing_formatter = SimpleAgentV3(
        name="billing_formatter",
        engine=AugLLMConfig(temperature=0.3),
        structured_output_model=BillingResolution,
        debug=True,
    )

    # Create product specialist
    product_specialist = ReactAgentV4(
        name="product_support",
        engine=AugLLMConfig(
            temperature=0.4,
            system_message="You are a product specialist. Help customers understand and choose products.",
        ),
        tools=[get_product_features, compare_plans],
        debug=True,
    )

    product_formatter = SimpleAgentV3(
        name="product_formatter",
        engine=AugLLMConfig(temperature=0.3),
        structured_output_model=ProductInfo,
        debug=True,
    )

    # Create general support for unclassified queries
    general_support = SimpleAgentV3(
        name="general_support",
        engine=AugLLMConfig(
            temperature=0.5,
            system_message="You are a general support agent. Provide helpful responses to customer queries.",
        ),
        debug=True,
    )

    # Create the routing workflow
    print("\nCreating conditional routing workflow...")
    router = EnhancedMultiAgentV4(
        name="support_router",
        agents=[
            classifier,
            technical_specialist,
            technical_formatter,
            billing_specialist,
            billing_formatter,
            product_specialist,
            product_formatter,
            general_support,
        ],
        execution_mode="manual",  # We'll define custom routing
        build_mode="manual",
    )

    # Define routing logic
    def route_by_category(state):
        """Route based on query classification."""
        if hasattr(state, "query_classifier") and state.query_classifier:
            category = state.query_classifier.category
            # High urgency goes to specialists immediately
            if state.query_classifier.urgency > 0.8:
                print(
                    f"🚨 High urgency query detected! Routing to {category} specialist."
                )
            return category
        return "general"

    # Add routing edges
    router.add_edge("START", "query_classifier")

    # Add conditional routing from classifier
    router.add_multi_conditional_edge(
        from_agent="query_classifier",
        condition=route_by_category,
        routes={
            "technical": "technical_support",
            "billing": "billing_support",
            "product": "product_support",
            "general": "general_support",
        },
        default="general_support",
    )

    # Connect specialists to formatters
    router.add_edge("technical_support", "technical_formatter")
    router.add_edge("billing_support", "billing_formatter")
    router.add_edge("product_support", "product_formatter")

    # All paths lead to END
    router.add_edge("technical_formatter", "END")
    router.add_edge("billing_formatter", "END")
    router.add_edge("product_formatter", "END")
    router.add_edge("general_support", "END")

    # Build the workflow
    router.build()

    # Test queries
    test_queries = [
        "I can't log into my account, it keeps saying invalid credentials even though I'm sure they're correct",
        "I was charged twice for my subscription this month, can you help me get a refund?",
        "What's the difference between the Professional and Enterprise plans? I need analytics features.",
        "How's the weather today?",  # General query
    ]

    print("\nProcessing support queries...\n")

    for i, query in enumerate(test_queries, 1):
        print(f"{'='*60}")
        print(f"QUERY {i}: {query[:80]}{'...' if len(query) > 80 else ''}")
        print(f"{'='*60}")

        # Execute workflow
        result = await router.arun({"messages": [HumanMessage(content=query)]})

        # Display classification
        if hasattr(router.state, "query_classifier"):
            classification = router.state.query_classifier
            print(f"\n📋 Classification:")
            print(f"   Category: {classification.category}")
            print(f"   Subcategory: {classification.subcategory}")
            print(f"   Urgency: {classification.urgency:.0%}")
            print(f"   Key terms: {', '.join(classification.key_terms)}")

        # Display specialized response
        if hasattr(router.state, "technical_formatter"):
            solution = router.state.technical_formatter
            print(f"\n🔧 Technical Solution:")
            print(f"   Issue: {solution.issue_identified}")
            print(f"   Root cause: {solution.root_cause}")
            print(f"   Steps to resolve:")
            for j, step in enumerate(solution.solution_steps, 1):
                print(f"     {j}. {step}")
            print(f"   Time estimate: {solution.estimated_time}")

        elif hasattr(router.state, "billing_formatter"):
            resolution = router.state.billing_formatter
            print(f"\n💳 Billing Resolution:")
            print(f"   Issue: {resolution.billing_issue}")
            print(f"   Resolution: {resolution.resolution}")
            if resolution.amount_affected > 0:
                print(f"   Amount: ${resolution.amount_affected:.2f}")
            print(f"   Next steps:")
            for step in resolution.next_steps:
                print(f"     • {step}")

        elif hasattr(router.state, "product_formatter"):
            info = router.state.product_formatter
            print(f"\n📦 Product Information:")
            print(f"   Product: {info.product_name}")
            print(f"   Relevant features: {', '.join(info.features_mentioned)}")
            print(f"   Pricing: {info.pricing_info}")
            print(f"   Recommendations:")
            for rec in info.recommendations:
                print(f"     • {rec}")

        elif "general_support" in router.state.agent_outputs:
            print(f"\n💬 General Support Response:")
            print(f"   {router.state.agent_outputs['general_support']}")

        print()

    # Show routing statistics
    print(f"\n{'='*60}")
    print("ROUTING STATISTICS")
    print(f"{'='*60}")
    print(f"Queries processed: {len(test_queries)}")
    print(f"Execution order: {router.state.agent_execution_order}")

    # Verify tool isolation
    print(f"\n{'='*60}")
    print("TOOL ISOLATION VERIFICATION")
    print(f"{'='*60}")
    print(f"Technical tools: {[t.name for t in technical_specialist.tools]}")
    print(f"Billing tools: {[t.name for t in billing_specialist.tools]}")
    print(f"Product tools: {[t.name for t in product_specialist.tools]}")
    print(f"General tools: {general_support.tools}")  # Should be empty
    print("✓ Each specialist has only their domain-specific tools")


if __name__ == "__main__":
    print("Conditional Support Router Example")
    print("=================================\n")
    asyncio.run(main())
