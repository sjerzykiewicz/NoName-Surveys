from typing import Literal

from pydantic import Field

from src.api.models.question_base import Question


class ListQuestion(Question):
    question_type: Literal["list"] = "list"
    choices: list[str] = Field(
        min_length=2, description="List question must have at least 2 options"
    )
