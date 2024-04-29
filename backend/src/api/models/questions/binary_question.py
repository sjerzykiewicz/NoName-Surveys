from typing import Literal

from pydantic import Field

from src.api.models.questions.question_base import Question


class BinaryQuestion(Question):
    question_type: Literal["binary"] = "binary"
    choices: list[str] = Field(
        len=2, description="Binary question must have precisely 2 options"
    )

    class Config:
        extra = "forbid"
