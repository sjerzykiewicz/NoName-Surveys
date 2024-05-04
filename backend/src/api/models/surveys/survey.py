import re
from typing import Union

from pydantic import BaseModel, Field, ValidationInfo, field_validator

from src.api.models.questions.binary_question import BinaryQuestion
from src.api.models.questions.list_question import ListQuestion
from src.api.models.questions.multi_question import MultiQuestion
from src.api.models.questions.rank_question import RankQuestion
from src.api.models.questions.scale_question import ScaleQuestion
from src.api.models.questions.single_question import SingleQuestion
from src.api.models.questions.slider_question import SliderQuestion
from src.api.models.questions.text_question import TextQuestion


class Survey(BaseModel):
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

    @field_validator("title")
    def validate_answer(cls, v, info: ValidationInfo) -> str:
        if v is None or v == "":
            raise ValueError("survey title must be provided")
        return v

    class Config:
        extra = "forbid"


class SurveyFetchInput(BaseModel):
    survey_code: str

    @field_validator("survey_code")
    def validate_answer(cls, v, info: ValidationInfo) -> str:
        if v is None:
            raise ValueError("survey code must be provided")
        if not re.match(r"^\d{6}$", v):
            raise ValueError(
                "survey code must be a string consisting of 6 digits"
            )
        return v

    class Config:
        extra = "forbid"


class SurveyFetchOutput(BaseModel):
    survey_structure: Survey
    uses_cryptographic_module: bool
    survey_code: str

    class Config:
        extra = "forbid"


class SurveyGetForUserOutput(BaseModel):
    survey_structure_id: int
    uses_cryptographic_module: bool
    survey_code: str

    class Config:
        extra = "forbid"


class SurveyCreateInput(BaseModel):
    creator: int
    survey_structure: Survey
    deadline: str
    uses_cryptographic_module: bool

    class Config:
        extra = "forbid"


class SurveyCreateOutput(BaseModel):
    creator: int
    survey_structure_id: int
    uses_cryptographic_module: bool
    survey_code: str

    class Config:
        extra = "forbid"
