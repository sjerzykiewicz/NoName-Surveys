import re
from typing import Optional, Union

from pydantic import BaseModel, Field, ValidationInfo, field_validator

from src.api.models.questions.binary_question import BinaryQuestion
from src.api.models.questions.list_question import ListQuestion
from src.api.models.questions.multi_question import MultiQuestion
from src.api.models.questions.rank_question import RankQuestion
from src.api.models.questions.scale_question import ScaleQuestion
from src.api.models.questions.single_question import SingleQuestion
from src.api.models.questions.slider_question import SliderQuestion
from src.api.models.questions.text_question import TextQuestion


class SurveyAnswerBase(BaseModel):
    survey_code: str
    questions: list[
        Union[
            BinaryQuestion,
            ListQuestion,
            MultiQuestion,
            RankQuestion,
            ScaleQuestion,
            SingleQuestion,
            SliderQuestion,
            TextQuestion,
        ]
    ] = Field(
        min_length=1,
        description="Questions list must have at least 1 element",
    )
    signature: list[int] = Field(default=[])
    y0: Optional[str] = Field(default="")

    @field_validator("survey_code")
    def validate_survey_join_code(cls, v, info: ValidationInfo) -> str:
        if v is None:
            raise ValueError("survey code must be provided")
        if not re.match(r"^\d{6}$", v):
            raise ValueError(
                "survey code must be a string consisting of 6 digits"
            )
        return v

    @field_validator("y0")
    def validate_y0(cls, v, info: ValidationInfo) -> str:
        if v is None or v == "":
            return v
        if not re.match(r"^[0-9]+$", v):
            raise ValueError("invalid y0 format")
        return v

    def validate(self) -> None:
        for question in self.questions:
            question.validate_for_answer()

    class Config:
        extra = "forbid"


class SurveyAnswersFetchInput(BaseModel):
    user_email: str
    survey_code: str

    @field_validator("survey_code")
    def validate_survey_join_code(cls, v, info: ValidationInfo) -> str:
        if v is None:
            raise ValueError("survey code must be provided")
        if not re.match(r"^\d{6}$", v):
            raise ValueError(
                "survey code must be a string consisting of 6 digits"
            )
        return v

    class Config:
        extra = "forbid"


class SurveyAnswersFetchOutput(BaseModel):
    title: str
    questions: list[
        Union[
            BinaryQuestion,
            ListQuestion,
            MultiQuestion,
            RankQuestion,
            ScaleQuestion,
            SingleQuestion,
            SliderQuestion,
            TextQuestion,
        ]
    ] = Field(
        min_length=1,
        description="Questions list must have at least 1 element",
    )

    class Config:
        extra = "forbid"
