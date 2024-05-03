from pydantic import BaseModel


class Question(BaseModel):
    required: bool
    question: str
