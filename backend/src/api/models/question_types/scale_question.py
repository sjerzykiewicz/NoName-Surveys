from typing import Literal

from src.api.models.question_base import Question


class ScaleQuestion(Question):
    question_type: Literal["scale"] = "scale"
