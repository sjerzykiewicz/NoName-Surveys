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

    @field_validator("choices")
    def validate_choices(cls, v, info: ValidationInfo) -> list[str]:
        if len(set(v)) != len(v):
            raise ValueError("all choices must be unique")
        return v

    @field_validator("answer")
    def validate_answer(cls, v, info: ValidationInfo) -> Optional[str]:
        if v is None:
            return v
        if "choices" in info.data and v not in info.data["choices"]:
            raise ValueError("answer must be one of the choices")
        return v

    def validate_structure_against(self, answer) -> None:
        if (
            not isinstance(answer, SingleQuestion)
            or self.required != answer.required
            or self.question != answer.question
            or self.choices != answer.choices
        ):
            raise ValueError("Invalid answer!")

    class Config:
        extra = "forbid"
