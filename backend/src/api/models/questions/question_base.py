from typing import Any

from pydantic import BaseModel


class Question(BaseModel):
    required: bool
    question: str
    answer: Any

    def validate_for_answer(self):
        if self.required and self.answer is None:
            raise ValueError("answer is required")

    def validate_for_draft(self):
        if self.answer is not None:
            raise ValueError("answer is not allowed in draft mode")
