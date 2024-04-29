from typing import Literal

from src.api.models.questions.question_base import Question


class ScaleQuestion(Question):
    question_type: Literal["scale"] = "scale"
    min_value: float
    max_value: float

    class Config:
        extra = "forbid"
