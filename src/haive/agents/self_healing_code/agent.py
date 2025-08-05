import uuid


class SelfHealingCodeAgentConfig(AgentArchitectureConfig):
    state_schema: SelfHealingCodeState


class SelfHealingCodeAgent(AgentArchitecture):
    config: SelfHealingCodeAgentConfig
    state: SelfHealingCodeState

    def bug_report_node(self: SelfHealingCodeState):
        """Generate Bug Report."""
        prompt = ChatPromptTemplate.from_template(
            "You are tasked with generating a bug report for a Python function that raised an error."
            "Function: {function_string}"
            "Error: {error_description}"
            "Your response must be a comprehensive string including only crucial information on the bug report"
        )
        message = HumanMessage(
            content=prompt.format(
                function_string=self.function_string, error_description=self.error_description
            )
        )
        bug_report = llm.invoke([message]).content.strip()

        self.bug_report = bug_report
        return self

    # Digest the bug report using the same template used when saving bug
    # reports to increase the accuracy and relevance of results when querying
    # the vector database.
    def memory_search_node(self: SelfHealingCodeState):
        """Find memories relevant to the current bug report."""
        prompt = ChatPromptTemplate.from_template(
            "You are tasked with archiving a bug report for a Python function that raised an error."
            "Bug Report: {bug_report}."
            "Your response must be a concise string including only crucial information on the bug report for future reference."
            "Format: # function_name ## error_description ### error_analysis"
        )

        message = HumanMessage(content=prompt.format(bug_report=self.bug_report))

        response = llm.invoke([message]).content.strip()

        results = collection.query(query_texts=[response])

        if results["ids"][0]:
            self.memory_search_results = [
                {
                    "id": results["ids"][0][index],
                    "memory": results["documents"][0][index],
                    "distance": results["distances"][0][index],
                }
                for index, id in enumerate(results["ids"][0])
            ]
        else:
            pass

        return self

    # Filter the top 30% of results to ensure the relevance of memories being
    # updated.
    def memory_filter_node(self: SelfHealingCodeState):
        for memory in self.memory_search_results:
            if memory["distance"] < 0.3:
                self.memory_ids_to_update.append(memory["id"])

        if self.memory_ids_to_update:
            pass
        else:
            pass

        return self

    # Condense the bug report before storing it in the vector database.
    def memory_generation_node(self: SelfHealingCodeState):
        """Generate relevant memories based on new bug report."""
        prompt = ChatPromptTemplate.from_template(
            "You are tasked with archiving a bug report for a Python function that raised an error."
            "Bug Report: {bug_report}."
            "Your response must be a concise string including only crucial information on the bug report for future reference."
            "Format: # function_name ## error_description ### error_analysis"
        )

        message = HumanMessage(content=prompt.format(bug_report=self.bug_report))

        response = llm.invoke([message]).content.strip()

        id = str(uuid.uuid4())
        collection.add(ids=[id], documents=[response])
        return self

    # Use the prior memory as well as the current bug report to generate an
    # updated version of it.
    def memory_modification_node(self: SelfHealingCodeState):
        """Modify relevant memories based on new interaction."""
        prompt = ChatPromptTemplate.from_template(
            "Update the following memories based on the new interaction:"
            "Current Bug Report: {bug_report}"
            "Prior Bug Report: {memory_to_update}"
            "Your response must be a concise but cumulative string including only crucial information on the current and prior bug reports for future reference."
            "Format: # function_name ## error_description ### error_analysis"
        )
        memory_to_update_id = self.memory_ids_to_update.pop(0)
        self.memory_search_results.pop(0)
        results = collection.get(ids=[memory_to_update_id])
        memory_to_update = results["documents"][0]
        message = HumanMessage(
            content=prompt.format(bug_report=self.bug_report, memory_to_update=memory_to_update)
        )

        response = llm.invoke([message]).content.strip()

        collection.update(ids=[memory_to_update_id], documents=[response])

        return self

    def setup_workflow(self) -> None:
        self.graph.add_node("code_execution_node", code_execution_node)
        self.graph.add_node("code_update_node", code_update_node)
        self.graph.add_node("code_patching_node", code_patching_node)
        self.graph.add_node("bug_report_node", bug_report_node)
        self.graph.add_node("memory_search_node", memory_search_node)
        self.graph.add_node("memory_filter_node", memory_filter_node)
        self.graph.add_node("memory_modification_node", memory_modification_node)
        self.graph.add_node("memory_generation_node", memory_generation_node)

        # Add edges to the graph
        self.graph.set_entry_point("code_execution_node")
        self.graph.add_conditional_edges("code_execution_node", error_router)
        self.graph.add_edge("bug_report_node", "memory_search_node")
        self.graph.add_conditional_edges("memory_search_node", memory_filter_router)
        self.graph.add_conditional_edges("memory_filter_node", memory_generation_router)
        self.graph.add_edge("memory_generation_node", "code_update_node")
        self.graph.add_conditional_edges("memory_modification_node", memory_update_router)

        self.graph.add_edge("code_update_node", "code_patching_node")
        self.graph.add_edge("code_patching_node", "code_execution_node")

    def code_execution_node(self: SelfHealingCodeState):
        """Run Arbitrary Code."""
        try:
            self.function(*self.arguments)
        except Exception as e:
            self.error = True
            self.error_description = str(e)
        return self

    def code_update_node(self: State):
        """Update Arbitratry Code."""
        prompt = ChatPromptTemplate.from_template(
            "You are tasked with fixing a Python function that raised an error."
            "Function: {function_string}"
            "Error: {error_description}"
            "You must provide a fix for the present error only."
            "The bug fix should handle the thrown error case gracefully by returning an error message."
            "Do not raise an error in your bug fix."
            "The function must use the exact same name and parameters."
            "Your response must contain only the function definition with no additional text."
            "Your response must not contain any additional formatting, such as code delimiters or language declarations."
        )
        message = HumanMessage(
            content=prompt.format(
                function_string=self.function_string, error_description=self.error_description
            )
        )
        new_function_string = llm.invoke([message]).content.strip()

        self.new_function_string = new_function_string
        return self

    def code_patching_node(self: State):
        """Fix Arbitrary Code."""
        try:
            # Store the new function as a string
            new_code = self.new_function_string

            # Create namespace for new function
            namespace = {}

            # Execute new code in namespace
            exec(new_code, namespace)

            # Get function name dynamically
            func_name = self.function.__name__

            # Get the new function using dynamic name
            new_function = namespace[func_name]

            # Update state
            self.function = new_function
            self.error = False

            # Test the new function
            self.function(*self.arguments)

        except Exception:
            pass

        return self
