from typing import Annotated
from langgraph.graph import add_messages
#from 
from pydantic import BaseModel,Field
import operator
from typing import Literal, Optional
from haive.agents.document_modifiers.complex_extraction.utils import add_or_overwrite_messages
from langchain_core.messages import AnyMessage
class ComplexExtractionState(BaseModel):
        """
        State for complex extraction.
        """
        messages: Annotated[list, add_or_overwrite_messages] = Field(default_factory=list,description="The messages from the conversation history.")
        attempt_number: Annotated[int, operator.add] = Field(default=0,description="The number of attempts to extract the complex information.")
        initial_num_messages: Optional[int] = Field(default=None,description="The number of messages in the conversation history.")
        input_format: Literal["list", "dict"] = Field(default="list",description="The format of the input to the complex extraction.")
        #extraction_schema: Optional[BaseModel] = Field(default=None,description="The schema of the complex extraction.")
        #extraction_schema_name: Optional[str] = Field(default=None,description="The name of the extraction schema.")
        extracted_data: Optional[list[AnyMessage]] = Field(default=[],description="The data to be extracted from the conversation history.")