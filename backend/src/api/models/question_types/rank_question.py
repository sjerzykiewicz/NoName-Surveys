from typing import Literal

from pydantic import Field

from src.api.models.question_base import Question


class RankQuestion(Question):
    question_type: Literal["rank"] = "rank"
    choices: list[str] = Field(
        min_length=2, description="Rank question must have at least 2 options"
    )
