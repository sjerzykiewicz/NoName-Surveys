from typing import Literal, Optional

from pydantic import Field, ValidationInfo, field_validator

from src.api.models.questions.question_base import Question


class ListQuestion(Question):
    question_type: Literal["list"] = "list"
    choices: list[str] = Field(
        min_length=2, description="List question must have at least 2 options"
    )
    answer: Optional[str] = None

    @field_validator("answer")
    def validate_answer(cls, v, info: ValidationInfo) -> Optional[str]:
        if v is None:
            return v
        if "choices" in info.data and v not in info.data["choices"]:
            raise ValueError("answer must be one of the choices")
        return v

    class Config:
        extra = "forbid"
