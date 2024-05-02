from typing import Literal, Optional

from pydantic import Field, ValidationInfo, field_validator

from src.api.models.questions.question_base import Question


class BinaryQuestion(Question):
    question_type: Literal["binary"] = "binary"
    choices: list[str] = Field(
        len=2, description="Binary question must have precisely 2 options"
    )
    answer: Optional[str] = None

    @field_validator("answer")
    def validate_answer(cls, v, info: ValidationInfo) -> Optional[str]:
        if not v:
            return v
        if "choices" in info.data and v not in info.data["choices"]:
            raise ValueError("answer must be one of the choices")
        return v

    class Config:
        extra = "forbid"
