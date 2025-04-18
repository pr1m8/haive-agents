from typing import List, Optional
from typing_extensions import TypedDict


from pydantic import Field
class BBox(TypedDict):
    """Bounding box for the action to take"""
    x: float = Field(...,description="The x coordinate of the bounding box")
    y: float = Field(...,description="The y coordinate of the bounding box")
    text: str = Field(...,description="The text of the bounding box")
    type: str = Field(...,description="The type of the bounding box")
    ariaLabel: str = Field(...,description="The aria label of the bounding box")


from pydantic import BaseModel, Field
from typing import List

from pydantic import BaseModel, Field, validator
from typing import List, Any, Dict, Union

from pydantic import BaseModel, Field
from typing import List

class Prediction(BaseModel):
    thought: str = Field(..., description="Agent's reasoning for choosing the action")
    action: str = Field(..., description="The selected action")
    args: List[str] = Field(
        ...,
        description="Arguments for the action",
        json_schema_extra={
            "type": "array",
            "items": {"type": "string"}
        }
    )
