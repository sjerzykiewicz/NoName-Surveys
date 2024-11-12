from typing import Literal, Optional

from pydantic import Field, ValidationInfo, field_validator

from src.api.models.questions.question_base import Question


class RankQuestion(Question):
    question_type: Literal["rank"] = "rank"
    choices: list[str] = Field(
        min_length=2, description="Rank question must have at least 2 options"
    )
    answer: Optional[list[str]] = None

    @field_validator("choices")
    def validate_choices(cls, v) -> list[str]:
        if len(set(v)) != len(v):
            raise ValueError("all choices must be unique")
        return v

    @field_validator("answer")
    def validate_answer(cls, v, info: ValidationInfo) -> Optional[list[str]]:
        if v is None:
            return v
        if "choices" in info.data and set(v) != set(info.data["choices"]):
            raise ValueError("answer must be one of the choices")
        return v

    def validate_structure_against(self, answer) -> None:
        if (
            not isinstance(answer, RankQuestion)
            or self.required != answer.required
            or self.question != answer.question
            or self.choices != answer.choices
        ):
            raise ValueError("Invalid answer!")
