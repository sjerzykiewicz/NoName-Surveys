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


class SurveyStructure(BaseModel):
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
    def validate_survey_title(cls, v, info: ValidationInfo) -> str:
        if v is None or v == "":
            raise ValueError("survey title must be provided")
        return v

    def validate(self):
        for question in self.questions:
            question.validate_for_draft()

    class Config:
        extra = "forbid"


class SurveyHeadersOutput(BaseModel):
    title: str
    survey_code: str
    creation_date: str


class SurveyStructureFetchInput(BaseModel):
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


class SurveyStructureFetchOutput(BaseModel):
    survey_structure: SurveyStructure
    survey_code: str
    uses_cryptographic_module: bool

    class Config:
        extra = "forbid"


class SurveyStructureCreateInput(BaseModel):
    user_email: str
    survey_structure: SurveyStructure
    uses_cryptographic_module: bool
    ring_members: Optional[list[str]] = Field(default=[])

    @field_validator("ring_members")
    def validate_emails(cls, v, info: ValidationInfo) -> str:
        if not info.data["uses_cryptographic_module"]:
            return v
        if v is None or len(v) == 0:
            raise ValueError(
                "emails must be provided for cryptographic module"
            )
        for email in v:
            if not re.match(
                r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email
            ):
                raise ValueError("invalid email format")
        return v

    class Config:
        extra = "forbid"


class SurveyStructureCreateOutput(BaseModel):
    survey_code: str

    class Config:
        extra = "forbid"
