from typing import Literal

from pydantic import Field

from src.api.models.question_base import Question


class SingleQuestion(Question):
    question_type: Literal["single"] = "single"
    choices: list[str] = Field(
        min_length=2,
        description="Single choice question must have at least 2 options",
    )
