from typing import Literal, Optional

from pydantic import Field, ValidationInfo, field_validator

from src.api.models.questions.question_base import Question


class RankQuestion(Question):
    question_type: Literal["rank"] = "rank"
    choices: list[str] = Field(
        min_length=2, description="Rank question must have at least 2 options"
    )
    answer: Optional[list[str]] = None

    @field_validator("answer")
    def validate_answer(cls, v, info: ValidationInfo) -> Optional[list[str]]:
        if v is None:
            return v
        if "choices" in info.data and set(v) != set(info.data["choices"]):
            raise ValueError("answer must be one of the choices")
        return v

    class Config:
        extra = "forbid"
