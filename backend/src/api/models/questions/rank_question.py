from typing import Literal, Optional

from pydantic import Field, validator

from src.api.models.questions.question_base import Question


class RankQuestion(Question):
    question_type: Literal["rank"] = "rank"
    choices: list[str] = Field(
        min_length=2, description="Rank question must have at least 2 options"
    )
    answer: Optional[list[str]] = None

    @validator("answer")
    def validate_answer(cls, v, values):
        if not v:
            return v
        if "choices" in values and set(v) != set(values["choices"]):
            raise ValueError("answer must be one of the choices")
        return v

    class Config:
        extra = "forbid"
