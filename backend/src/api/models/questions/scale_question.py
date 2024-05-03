from typing import Literal, Optional

from pydantic import ValidationInfo, field_validator

from src.api.models.questions.question_base import Question


class ScaleQuestion(Question):
    question_type: Literal["scale"] = "scale"
    answer: Optional[int] = None

    @field_validator("answer")
    def validate_answer(cls, v, info: ValidationInfo) -> Optional[float]:
        if v is None:
            return v
        if not 1 <= v <= 5:
            raise ValueError("scale answer must be between 1 and 5")
        return v

    class Config:
        extra = "forbid"
