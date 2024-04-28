from typing import Literal

from src.api.models.question_base import Question


class BinaryQuestion(Question):
    question_type: Literal["binary"] = "binary"
