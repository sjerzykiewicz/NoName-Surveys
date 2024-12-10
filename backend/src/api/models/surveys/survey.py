from datetime import datetime
from typing import Optional, Union

from pydantic import Field, ValidationInfo, field_validator

from src.api.models.base import Base
from src.api.models.metadata.subtitle import Subtitle
from src.api.models.questions.binary_question import BinaryQuestion
from src.api.models.questions.list_question import ListQuestion
from src.api.models.questions.multi_question import MultiQuestion
from src.api.models.questions.number_question import NumberQuestion
from src.api.models.questions.rank_question import RankQuestion
from src.api.models.questions.scale_question import ScaleQuestion
from src.api.models.questions.single_question import SingleQuestion
from src.api.models.questions.slider_question import SliderQuestion
from src.api.models.questions.text_question import TextQuestion


class SurveyStructure(Base):
    questions: list[
        Union[
            BinaryQuestion,
            ListQuestion,
            MultiQuestion,
            NumberQuestion,
            RankQuestion,
            ScaleQuestion,
            SingleQuestion,
            SliderQuestion,
            TextQuestion,
            Subtitle,
        ]
    ] = Field(
        min_length=1,
        description="Questions list must have at least 1 element",
    )

    def validate(self):
        for question in self.questions:
            question.validate_for_draft()


class SurveyBase(Base):
    title: str

    @field_validator("title")
    def validate_survey_title(cls, v) -> str:
        if v is None or v == "":
            raise ValueError("survey title must be provided")
        return v


class SurveyHeadersOutput(Base):
    title: str
    survey_code: str
    creation_date: datetime
    uses_cryptographic_module: bool
    is_owned_by_user: bool
    group_size: int
    is_enabled: bool


class SurveyInfoFetchInput(Base):
    survey_code: str

    @field_validator("survey_code")
    def validate_survey_join_code(cls, v) -> str:
        return Base.validate_survey_code(v)


class SurveyStructureFetchOutput(Base):
    title: str
    survey_structure: SurveyStructure
    survey_code: str
    uses_cryptographic_module: bool
    public_keys: Optional[list[str]] = Field(default=[])


class SurveyStructureCreateInput(SurveyBase):
    user_email: str
    survey_structure: SurveyStructure
    uses_cryptographic_module: bool
    ring_members: Optional[list[str]] = Field(default=[])

    @field_validator("user_email")
    def validate_user_email(cls, v) -> str:
        return Base.validate_email(v)

    @field_validator("ring_members")
    def validate_emails(cls, v, info: ValidationInfo) -> str:
        if not info.data["uses_cryptographic_module"]:
            return v
        return Base.validate_emails(v)


class SurveyStructureCreateOutput(Base):
    survey_code: str


class SurveyUserAction(Base):
    user_email: str

    @field_validator("user_email")
    def validate_user_email(cls, v) -> str:
        return Base.validate_email(v)


class SurveyUserActions(SurveyUserAction):
    survey_code: str

    @field_validator("survey_code")
    def validate_survey_code(cls, v) -> str:
        return Base.validate_survey_code(v)


class SurveyEnableDisableAction(SurveyUserActions):
    is_enabled: bool


class SurveyUserDeleteAction(SurveyUserAction):
    survey_codes: list[str]

    @field_validator("survey_codes")
    def validate_survey_code(cls, v) -> str:
        return Base.validate_survey_codes(v)


class ShareSurveyActions(SurveyUserActions):
    user_emails: list[str]

    @field_validator("user_emails")
    def validate_emails(cls, v) -> str:
        return Base.validate_emails(v)
