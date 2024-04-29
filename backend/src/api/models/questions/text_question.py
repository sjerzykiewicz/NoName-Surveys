from typing import Literal

from src.api.models.questions.question_base import Question


class TextQuestion(Question):
    question_type: Literal["text"] = "text"
    details: str

    class Config:
        extra = "forbid"
