"""Join Step - Automatic DAG and Parallelization with Auto-detection.

Inspired by haive.core.common.structures.tree, this implements a JoinStep that
automatically detects parallel branches and creates join points for DAG execution.

Similar to AutoTree's pattern of automatically detecting BaseModel relationships,
JoinStep automatically detects step dependencies and creates optimal join points
for parallel execution.
"""

from enum import Enum
from typing import Any

from pydantic import Field, computed_field

from .steps import AbstractStep


class JoinStrategy(str, Enum):
    """Strategies for joining parallel branches."""

    WAIT_ALL = "wait_all"  # Wait for all inputs to complete
    WAIT_ANY = "wait_any"  # Continue when any input completes
    WAIT_MAJORITY = "wait_majority"  # Wait for majority of inputs
    WAIT_CRITICAL = "wait_critical"  # Wait only for critical path inputs


class JoinStep(AbstractStep):
    """A step that automatically creates join points for parallel execution.

    Like AutoTree automatically detects BaseModel relationships, JoinStep
    automatically detects dependency patterns and creates optimal join points.

    This enables automatic DAG creation where parallel branches are automatically
    detected and joined at the optimal points.
    """

    # Core join configuration
    join_strategy: JoinStrategy = Field(
        default=JoinStrategy.WAIT_ALL,
        description="Strategy for joining parallel inputs",
    )

    # Auto-detected parallel inputs (computed automatically)
    parallel_inputs: list[str] = Field(
        default_factory=list, description="Automatically detected parallel input steps"
    )

    # Auto-detected join metadata
    join_metadata: dict[str, Any] = Field(
        default_factory=dict, description="Metadata about the join operation"
    )

    # Results from parallel branches
    parallel_results: dict[str, Any] = Field(
        default_factory=dict, description="Results from each parallel input"
    )

    # Join function to combine results
    join_function: str | None = Field(
        default=None, description="Function name to combine parallel results"
    )

    # Computed fields (automatic detection like AutoTree)
    @computed_field
    @property
    def is_join_point(self) -> bool:
        """Whether this step is a join point (has multiple dependencies)."""
        return len(self.depends_on) > 1

    @computed_field
    @property
    def parallel_branch_count(self) -> int:
        """Number of parallel branches this step joins."""
        return (
            len(self.parallel_inputs) if self.parallel_inputs else len(self.depends_on)
        )

    @computed_field
    @property
    def join_complexity(self) -> str:
        """Complexity classification of the join operation."""
        if self.parallel_branch_count <= 1:
            return "sequential"
        if self.parallel_branch_count <= 3:
            return "simple_parallel"
        if self.parallel_branch_count <= 6:
            return "moderate_parallel"
        return "complex_parallel"

    @computed_field
    @property
    def estimated_wait_time(self) -> float:
        """Estimated wait time based on join strategy and branch count."""
        base_time = self.parallel_branch_count * 0.5  # Base scaling

        strategy_multipliers = {
            JoinStrategy.WAIT_ALL: 1.0,  # Longest path
            JoinStrategy.WAIT_ANY: 0.3,  # Shortest path
            JoinStrategy.WAIT_MAJORITY: 0.7,  # Middle paths
            JoinStrategy.WAIT_CRITICAL: 0.8,  # Critical path
        }

        return base_time * strategy_multipliers.get(self.join_strategy, 1.0)

    @computed_field
    @property
    def can_optimize_parallel(self) -> bool:
        """Whether this join can be optimized for parallel execution."""
        return (
            self.is_join_point
            and self.join_strategy
            in [JoinStrategy.WAIT_ANY, JoinStrategy.WAIT_MAJORITY]
            and self.parallel_branch_count >= 2
        )

    def __init__(self, **data) -> None:
        super().__init__(**data)
        self._auto_detect_parallel_structure()

    def _auto_detect_parallel_structure(self):
        """Auto-detect parallel structure like AutoTree detects BaseModel relationships.

        This method analyzes the dependency structure and automatically identifies:
        - Parallel input branches
        - Critical path dependencies
        - Optimal join strategies
        - Execution metadata
        """
        if not self.depends_on:
            return

        # Auto-detect parallel inputs (all dependencies are potential parallel inputs)
        self.parallel_inputs = list(self.depends_on)

        # Auto-generate join metadata
        self.join_metadata = {
            "auto_detected": True,
            "detection_time": "init",
            "parallel_inputs": self.parallel_inputs,
            "join_type": "automatic",
            "optimization_hints": self._generate_optimization_hints(),
        }

        # Auto-suggest join function based on dependency count
        if not self.join_function:
            self.join_function = self._suggest_join_function()

    def _generate_optimization_hints(self) -> dict[str, Any]:
        """Generate optimization hints based on detected structure."""
        hints = {
            "can_use_futures": self.parallel_branch_count > 1,
            "recommended_timeout": self.estimated_wait_time * 2,
            "suggested_strategy": self._suggest_optimal_strategy(),
            "parallelization_benefit": self._estimate_parallelization_benefit(),
        }

        return hints

    def _suggest_optimal_strategy(self) -> JoinStrategy:
        """Suggest optimal join strategy based on structure."""
        if self.parallel_branch_count <= 2:
            return JoinStrategy.WAIT_ALL
        if self.parallel_branch_count <= 4:
            return JoinStrategy.WAIT_MAJORITY
        return JoinStrategy.WAIT_CRITICAL

    def _estimate_parallelization_benefit(self) -> float:
        """Estimate benefit of parallelization (0.0 to 1.0)."""
        if self.parallel_branch_count <= 1:
            return 0.0

        # More branches = higher benefit, but with diminishing returns
        benefit = 1.0 - (1.0 / self.parallel_branch_count)
        return min(benefit, 0.9)  # Cap at 90% benefit

    def _suggest_join_function(self) -> str:
        """Suggest appropriate join function based on structure."""
        if self.parallel_branch_count <= 1:
            return "passthrough"
        if self.parallel_branch_count == 2:
            return "merge_two"
        if self.parallel_branch_count <= 4:
            return "merge_multiple"
        return "reduce_complex"

    # Dependency analysis methods (inspired by AutoTree's type detection)
    def analyze_dependency_patterns(
        self, all_steps: list[AbstractStep]
    ) -> dict[str, Any]:
        """Analyze dependency patterns across all steps to detect DAG structure.

        Similar to how AutoTree analyzes type relationships, this analyzes
        step dependency relationships to detect optimal parallelization.
        """
        step_map = {step.id: step for step in all_steps}

        analysis = {
            "dependency_depth": self._calculate_dependency_depth(step_map),
            "fan_in_degree": len(self.depends_on),
            "parallel_opportunities": self._detect_parallel_opportunities(step_map),
            "critical_path_members": self._identify_critical_path_members(step_map),
            "suggested_optimizations": self._suggest_dag_optimizations(step_map),
        }

        return analysis

    def _calculate_dependency_depth(self, step_map: dict[str, AbstractStep]) -> int:
        """Calculate maximum dependency depth for this step."""

        def get_depth(step_id: str, visited: set[str] | None = None) -> int:
            if visited is None:
                visited = set()

            if step_id in visited:
                return 0  # Avoid cycles

            visited.add(step_id)
            step = step_map.get(step_id)
            if not step or not step.depends_on:
                return 0

            max_depth = 0
            for dep_id in step.depends_on:
                depth = get_depth(dep_id, visited.copy())
                max_depth = max(max_depth, depth + 1)

            return max_depth

        return get_depth(self.id)

    def _detect_parallel_opportunities(
        self, step_map: dict[str, AbstractStep]
    ) -> list[dict[str, Any]]:
        """Detect opportunities for parallel execution."""
        opportunities = []

        # Look for steps with no interdependencies
        independent_deps = []
        for dep_id in self.depends_on:
            dep_step = step_map.get(dep_id)
            if dep_step:
                # Check if this dependency is independent of other dependencies
                is_independent = True
                for other_dep_id in self.depends_on:
                    if other_dep_id != dep_id:
                        other_dep = step_map.get(other_dep_id)
                        if other_dep and self._has_dependency_path(
                            dep_step, other_dep, step_map
                        ):
                            is_independent = False
                            break

                if is_independent:
                    independent_deps.append(dep_id)

        if len(independent_deps) > 1:
            opportunities.append(
                {
                    "type": "independent_parallel",
                    "steps": independent_deps,
                    "benefit": len(independent_deps) / len(self.depends_on),
                }
            )

        return opportunities

    def _has_dependency_path(
        self,
        from_step: AbstractStep,
        to_step: AbstractStep,
        step_map: dict[str, AbstractStep],
    ) -> bool:
        """Check if there's a dependency path from one step to another."""

        def dfs(current_id: str, target_id: str, visited: set[str]) -> bool:
            if current_id == target_id:
                return True

            if current_id in visited:
                return False

            visited.add(current_id)
            current_step = step_map.get(current_id)
            if not current_step:
                return False

            return any(
                dfs(dep_id, target_id, visited.copy())
                for dep_id in current_step.depends_on
            )

        return dfs(from_step.id, to_step.id, set())

    def _identify_critical_path_members(
        self, step_map: dict[str, AbstractStep]
    ) -> list[str]:
        """Identify which dependencies are on the critical path."""
        critical_members = []

        for dep_id in self.depends_on:
            dep_step = step_map.get(dep_id)
            if dep_step:
                # A dependency is critical if it has the longest path to completion
                depth = self._calculate_dependency_depth({dep_id: dep_step})
                if depth >= len(self.depends_on) - 1:  # Heuristic for critical path
                    critical_members.append(dep_id)

        return critical_members

    def _suggest_dag_optimizations(
        self, step_map: dict[str, AbstractStep]
    ) -> list[dict[str, Any]]:
        """Suggest DAG-level optimizations."""
        optimizations = []

        # Suggest strategy based on analysis
        if self.parallel_branch_count > 3:
            optimizations.append(
                {
                    "type": "strategy_optimization",
                    "suggestion": "Consider WAIT_MAJORITY or WAIT_CRITICAL strategy",
                    "reason": f"High branch count ({self.parallel_branch_count})",
                }
            )

        # Suggest parallel execution
        parallel_ops = self._detect_parallel_opportunities(step_map)
        if parallel_ops:
            optimizations.append(
                {
                    "type": "parallelization",
                    "suggestion": "Use concurrent execution for independent branches",
                    "opportunities": parallel_ops,
                }
            )

        return optimizations

    # Execution methods
    def can_execute(self, completed_steps: set[str]) -> bool:
        """Check if this join step can execute based on strategy."""
        if not self.depends_on:
            return True

        completed_deps = [dep for dep in self.depends_on if dep in completed_steps]

        if self.join_strategy == JoinStrategy.WAIT_ALL:
            return len(completed_deps) == len(self.depends_on)
        if self.join_strategy == JoinStrategy.WAIT_ANY:
            return len(completed_deps) >= 1
        if self.join_strategy == JoinStrategy.WAIT_MAJORITY:
            return len(completed_deps) >= (len(self.depends_on) + 1) // 2
        if self.join_strategy == JoinStrategy.WAIT_CRITICAL:
            # For now, treat as wait_all - could be enhanced with critical path detection
            return len(completed_deps) == len(self.depends_on)

        return False

    def execute(self, context: dict[str, Any]) -> Any:
        """Execute the join operation."""
        if not self.can_execute(context.get("completed_steps", set())):
            raise ValueError("Join step cannot execute - strategy requirements not met")

        # Collect results from parallel branches
        step_results = context.get("step_results", {})
        for dep_id in self.depends_on:
            if dep_id in step_results:
                self.parallel_results[dep_id] = step_results[dep_id]

        # Execute join function
        if self.join_function == "passthrough":
            result = (
                next(iter(self.parallel_results.values()))
                if self.parallel_results
                else None
            )
        elif self.join_function == "merge_two":
            result = self._merge_two_results()
        elif self.join_function == "merge_multiple":
            result = self._merge_multiple_results()
        elif self.join_function == "reduce_complex":
            result = self._reduce_complex_results()
        else:
            # Default: collect all results
            result = {
                "joined_results": self.parallel_results,
                "join_metadata": self.join_metadata,
                "strategy_used": self.join_strategy,
            }

        return result

    def _merge_two_results(self) -> Any:
        """Merge exactly two results."""
        values = list(self.parallel_results.values())
        if len(values) >= 2:
            return {"merged": values[:2], "strategy": "two_way_merge"}
        return values[0] if values else None

    def _merge_multiple_results(self) -> Any:
        """Merge multiple results efficiently."""
        return {
            "merged_count": len(self.parallel_results),
            "combined_results": list(self.parallel_results.values()),
            "strategy": "multi_way_merge",
        }

    def _reduce_complex_results(self) -> Any:
        """Reduce complex parallel results."""
        return {
            "reduced_from": len(self.parallel_results),
            "summary": f"Reduced {len(self.parallel_results)} parallel results",
            "strategy": "complex_reduction",
        }

    # Utility methods
    def get_join_info(self) -> dict[str, Any]:
        """Get comprehensive information about this join step."""
        return {
            "step_id": self.id,
            "description": self.description,
            "join_strategy": self.join_strategy,
            "is_join_point": self.is_join_point,
            "parallel_branch_count": self.parallel_branch_count,
            "join_complexity": self.join_complexity,
            "estimated_wait_time": self.estimated_wait_time,
            "can_optimize_parallel": self.can_optimize_parallel,
            "parallel_inputs": self.parallel_inputs,
            "join_metadata": self.join_metadata,
            "optimization_hints": self.join_metadata.get("optimization_hints", {}),
        }

    @classmethod
    def create_auto_join(
        cls,
        description: str,
        dependencies: list[str],
        strategy: JoinStrategy = JoinStrategy.WAIT_ALL,
        **kwargs,
    ) -> "JoinStep":
        """Factory method to create a JoinStep with automatic detection."""
        return cls(
            description=description,
            depends_on=dependencies,
            join_strategy=strategy,
            **kwargs,
        )

    @classmethod
    def analyze_dag_structure(cls, steps: list[AbstractStep]) -> dict[str, Any]:
        """Analyze entire DAG structure and suggest join optimizations.

        Like AutoTree's tree analysis, this provides DAG-wide analysis.
        """
        join_points = []
        parallel_opportunities = []

        for step in steps:
            if len(step.depends_on) > 1:
                # This is a potential join point
                if isinstance(step, JoinStep):
                    join_points.append(step)
                else:
                    # Suggest converting to JoinStep
                    parallel_opportunities.append(
                        {
                            "step_id": step.id,
                            "dependencies": step.depends_on,
                            "suggested_strategy": JoinStrategy.WAIT_ALL,
                            "potential_benefit": len(step.depends_on) * 0.2,
                        }
                    )

        return {
            "total_steps": len(steps),
            "existing_join_points": len(join_points),
            "potential_join_points": len(parallel_opportunities),
            "suggested_conversions": parallel_opportunities,
            "dag_complexity": cls._calculate_dag_complexity(steps),
            "parallelization_score": cls._calculate_parallelization_score(steps),
        }

    @classmethod
    def _calculate_dag_complexity(cls, steps: list[AbstractStep]) -> str:
        """Calculate overall DAG complexity."""
        total_deps = sum(len(step.depends_on) for step in steps)
        avg_deps = total_deps / len(steps) if steps else 0

        if avg_deps < 1:
            return "linear"
        if avg_deps < 2:
            return "simple_dag"
        if avg_deps < 3:
            return "moderate_dag"
        return "complex_dag"

    @classmethod
    def _calculate_parallelization_score(cls, steps: list[AbstractStep]) -> float:
        """Calculate potential parallelization benefit (0.0 to 1.0)."""
        if not steps:
            return 0.0

        parallel_potential = 0
        for step in steps:
            if len(step.depends_on) > 1:
                parallel_potential += len(step.depends_on) - 1

        max_potential = len(steps) * 2  # Rough maximum
        return (
            min(parallel_potential / max_potential, 1.0) if max_potential > 0 else 0.0
        )
