from typing import Literal

from src.api.models.questions.question_base import Question


class SliderQuestion(Question):
    question_type: Literal["slider"] = "slider"
    min_value: float
    max_value: float

    class Config:
        extra = "forbid"
