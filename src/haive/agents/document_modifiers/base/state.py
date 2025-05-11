from typing import List, Optional

from haive.core.schema import StateSchema
from langchain_core.documents import Document
from pydantic import BaseModel, Field, computed_field, field_validator, model_validator


class DocumentModifierState(StateSchema):
    """
    State for the document modifier agent.
    """

    # pass
    name: Optional[str] = Field(
        default=None, description="The name of the document modifier."
    )
    description: Optional[str] = Field(
        default=None, description="The description of the document modifier."
    )
    documents: List[Document] = Field(
        default_factory=list, description="The documents to process."
    )

    # is_split: bool = Field(default=False,description="Whether the documents are split.")
    # embeded_documents:List[Document] = Field(default_factory=list,description="The embeded documents.")
    # split_documents:List[Document] = Field(default_factory=list,description="The split documents.")
    # transformed_documents:List[Document] = Field(default_factory=list,description="The transformed documents.")
    # annotations:List[Annotation]
    @classmethod
    def from_documents(cls, documents: List[Document]) -> "DocumentModifierState":
        """
        Create a DocumentModifierState from a list of documents.
        """
        return cls(documents=documents)

    @computed_field
    @property
    def documents_text(self) -> str:
        """
        The text of the documents.
        """
        return "\n".join([doc.page_content for doc in self.documents])

    @computed_field
    @property
    def num_documents(self) -> int:
        """
        The number of documents.
        """
        return len(self.documents)

    @model_validator(mode="after")
    def validate_documents(self):
        """
        Validate the documents.
        """
        if self.num_documents == 0:
            raise ValueError("At least one document is required.")
        return self

    @field_validator("documents")
    def validate_documents(cls, v):
        """
        Validate the documents.
        """
        return v

    @classmethod
    def add_document(cls, document: Document) -> "DocumentModifierState":
        """
        Add a document to the state.
        """
        return cls(documents=cls.documents + [document])

    @classmethod
    def add_documents(cls, documents: List[Document]) -> "DocumentModifierState":
        """
        Add a list of documents to the state.
        """
        return cls(documents=cls.documents + documents)

    @classmethod
    def remove_document(cls, document: Document) -> "DocumentModifierState":
        """
        Remove a document from the state.
        """
        return cls(documents=cls.documents - [document])

    @classmethod
    def remove_documents(cls, documents: List[Document]) -> "DocumentModifierState":
        """
        Remove a list of documents from the state.
        """
        return cls(documents=cls.documents - documents)
