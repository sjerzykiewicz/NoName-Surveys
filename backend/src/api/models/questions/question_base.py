from typing import Any

from src.api.models.base import Base


class Question(Base):
    required: bool
    question: str
    answer: Any

    def validate_for_answer(self) -> None:
        if self.required and self.answer is None:
            raise ValueError("answer is required")

    def validate_for_draft(self) -> None:
        if self.answer is not None:
            raise ValueError("answer is not allowed in draft mode")

    def validate_structure_against(self, answer) -> None:
        pass
