from typing import Literal, Optional

from pydantic import Field, ValidationInfo, field_validator

from src.api.models.questions.question_base import Question


class SliderQuestion(Question):
    question_type: Literal["slider"] = "slider"
    min_value: float
    max_value: float
    precision: float = Field(default=1)
    answer: Optional[float] = None

    @field_validator("max_value")
    def validate_choices(cls, v, info: ValidationInfo) -> float:
        if v <= info.data["min_value"]:
            raise ValueError("max_value must be greater than min_value")
        return v

    @field_validator("precision")
    def validate_precision(cls, v, info: ValidationInfo) -> float:
        if v > info.data["max_value"] - info.data["min_value"]:
            raise ValueError(
                "precision cannot be greater than the difference between max_value and min_value"  # noqa
            )
        return v

    @field_validator("answer")
    def validate_answer(cls, v, info: ValidationInfo) -> Optional[float]:
        if v is None:
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

    def validate_structure_against(self, answer) -> None:
        if (
            not isinstance(answer, SliderQuestion)
            or self.required != answer.required
            or self.question != answer.question
            or self.min_value != answer.min_value
            or self.max_value != answer.max_value
            or self.precision != answer.precision
        ):
            raise ValueError("Invalid answer!")

    def get_answer(self):
        if self.answer is not None:
            return (
                str(self.answer).rstrip("0").rstrip(".")
                if "." in str(self.answer)
                else str(self.answer)
            )
        return ""
