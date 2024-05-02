from typing import Literal, Optional

from pydantic import ValidationInfo, field_validator

from src.api.models.questions.question_base import Question


class SliderQuestion(Question):
    question_type: Literal["slider"] = "slider"
    min_value: float
    max_value: float
    answer: Optional[float] = None

    @field_validator("answer")
    def validate_answer(cls, v, info: ValidationInfo) -> Optional[float]:
        if not v:
            return v
        if (
            "min_value" in info.data
            and "max_value" in info.data
            and not info.data["min_value"] <= v <= info.data["max_value"]
        ):
            raise ValueError(
                "answer must be between minimum and maximum possible values"
            )
        return v

    class Config:
        extra = "forbid"
