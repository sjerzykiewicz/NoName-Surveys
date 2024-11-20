from typing import Literal, Optional

from pydantic import ValidationInfo, field_validator

from src.api.models.questions.question_base import Question


class TextQuestion(Question):
    question_type: Literal["text"] = "text"
    details: str
    answer: Optional[str] = None

    @field_validator("answer")
    def validate_answer(cls, v, info: ValidationInfo) -> Optional[float]:
        if v is None:
            return v
        if "required" in info.data and info.data["required"] and len(v) == 0:
            raise ValueError("answer is required")
        return v

    def validate_structure_against(self, answer) -> None:
        if (
            not isinstance(answer, TextQuestion)
            or self.required != answer.required
            or self.question != answer.question
            or self.details != answer.details
        ):
            raise ValueError("Invalid answer!")

    def get_answer(self):
        return self.answer if self.answer is not None else ""
