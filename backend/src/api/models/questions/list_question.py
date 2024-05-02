from typing import Literal, Optional

from pydantic import Field, validator

from src.api.models.questions.question_base import Question


class ListQuestion(Question):
    question_type: Literal["list"] = "list"
    choices: list[str] = Field(
        min_length=2, description="List question must have at least 2 options"
    )
    answer: Optional[list[str]] = None

    @validator("answer")
    def validate_answer(cls, v, values, **kwargs):
        if "choices" in values and any(
            choice not in values["choices"] for choice in v
        ):
            raise ValueError("answer must be one of the choices")
        return v

    class Config:
        extra = "forbid"
