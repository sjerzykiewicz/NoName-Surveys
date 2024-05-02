from typing import Literal, Optional

from pydantic import Field, validator

from src.api.models.questions.question_base import Question


class SingleQuestion(Question):
    question_type: Literal["single"] = "single"
    choices: list[str] = Field(
        min_length=2,
        description="Single choice question must have at least 2 options",
    )
    answer: Optional[str] = None

    @validator("answer")
    def validate_answer(cls, v, values):
        if len(v) != 1:
            raise ValueError("answer must be a single choice")
        if "choices" in values and v not in values["choices"]:
            raise ValueError("answer must be one of the choices")
        return v

    class Config:
        extra = "forbid"
