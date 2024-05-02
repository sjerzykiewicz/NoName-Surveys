from typing import Literal, Optional

from pydantic import Field, validator

from src.api.models.questions.question_base import Question


class BinaryQuestion(Question):
    question_type: Literal["binary"] = "binary"
    choices: list[str] = Field(
        len=2, description="Binary question must have precisely 2 options"
    )
    answer: Optional[str] = None

    @validator("answer")
    def validate_answer(cls, v, values):
        if not v:
            return v
        if "choices" in values and v not in values["choices"]:
            raise ValueError("answer must be one of the choices")
        return v

    class Config:
        extra = "forbid"
