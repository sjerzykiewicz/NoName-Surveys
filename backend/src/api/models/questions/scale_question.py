from typing import Literal, Optional

from pydantic import field_validator

from src.api.models.questions.question_base import Question


class ScaleQuestion(Question):
    question_type: Literal["scale"] = "scale"
    answer: Optional[int] = None

    @field_validator("answer")
    def validate_answer(cls, v) -> Optional[float]:
        if v is None:
            return v
        if not 1 <= v <= 5:
            raise ValueError("scale answer must be between 1 and 5")
        return v

    def validate_structure_against(self, answer) -> None:
        if (
            not isinstance(answer, ScaleQuestion)
            or self.required != answer.required
            or self.question != answer.question
        ):
            raise ValueError("Invalid answer!")

    def get_answer(self):
        return str(self.answer) if self.answer is not None else ""
