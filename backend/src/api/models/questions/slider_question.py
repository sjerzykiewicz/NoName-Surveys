from typing import Literal, Optional

from pydantic import validator

from src.api.models.questions.question_base import Question


class SliderQuestion(Question):
    question_type: Literal["slider"] = "slider"
    min_value: float
    max_value: float
    answer: Optional[float] = None

    @validator("answer")
    def validate_answer(cls, v, values):
        if (
            "min_value" in values
            and "max_value" in values
            and values["min_value"] <= v <= values["max_value"]
        ):
            raise ValueError(
                "answer must be between minimum and maximum possible values"
            )
        return v

    class Config:
        extra = "forbid"
