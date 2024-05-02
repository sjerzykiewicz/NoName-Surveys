from typing import Literal, Optional

from pydantic import Field, ValidationInfo, field_validator

from src.api.models.questions.question_base import Question


class SingleQuestion(Question):
    question_type: Literal["single"] = "single"
    choices: list[str] = Field(
        min_length=2,
        description="Single choice question must have at least 2 options",
    )
    answer: Optional[str] = None

    @field_validator("answer")
    def validate_answer(cls, v, info: ValidationInfo) -> Optional[str]:
        if not v:
            return v
        if len(v) != 1:
            raise ValueError("answer must be a single choice")
        if "choices" in info.data and v not in info.data["choices"]:
            raise ValueError("answer must be one of the choices")
        return v

    class Config:
        extra = "forbid"
