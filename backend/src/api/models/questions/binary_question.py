from typing import Literal, Optional

from pydantic import Field, ValidationInfo, field_validator

from src.api.models.questions.question_base import Question


class BinaryQuestion(Question):
    question_type: Literal["binary"] = "binary"
    choices: list[str] = Field(
        min_length=2,
        max_length=2,
        description="Binary question must have precisely 2 options",
    )
    answer: Optional[str] = None

    @field_validator("choices")
    def validate_choices(cls, v) -> list[str]:
        if v[0] == v[1]:
            raise ValueError("choices must be unique")
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
            not isinstance(answer, BinaryQuestion)
            or self.required != answer.required
            or self.question != answer.question
            or self.choices != answer.choices
        ):
            raise ValueError("Invalid answer!")

    def get_answer(self):
        return self.answer if self.answer is not None else ""
