from typing import Literal

from pydantic import Field

from src.api.models.questions.question_base import Question


class MultiQuestion(Question):
    question_type: Literal["multi"] = "multi"
    choices: list[str] = Field(
        min_length=2,
        description="Multiple choice question must have at least 2 options",
    )

    class Config:
        extra = "forbid"
