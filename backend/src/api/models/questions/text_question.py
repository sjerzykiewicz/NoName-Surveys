from typing import Literal, Optional

from src.api.models.questions.question_base import Question


class TextQuestion(Question):
    question_type: Literal["text"] = "text"
    details: str
    answer: Optional[str] = None

    class Config:
        extra = "forbid"
