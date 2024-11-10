from typing import Union

from pydantic import Field, field_validator

from src.api.models.base import Base
from src.api.models.questions.binary_question import BinaryQuestion
from src.api.models.questions.list_question import ListQuestion
from src.api.models.questions.multi_question import MultiQuestion
from src.api.models.questions.number_question import NumberQuestion
from src.api.models.questions.rank_question import RankQuestion
from src.api.models.questions.scale_question import ScaleQuestion
from src.api.models.questions.single_question import SingleQuestion
from src.api.models.questions.slider_question import SliderQuestion
from src.api.models.questions.text_question import TextQuestion


class SurveyAnswerBase(Base):
    survey_code: str
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
        ]
    ] = Field(
        min_length=1,
        description="Questions list must have at least 1 element",
    )
    signature: list[str] = Field(default=[])

    @field_validator("survey_code")
    def validate_survey_join_code(cls, v) -> str:
        return Base.validate_survey_code(v)

    @field_validator("signature")
    def validate_signature(cls, v) -> list[str]:
        for signature in v:
            Base.validate_signature(signature)
        return v

    def validate(self) -> None:
        for question in self.questions:
            question.validate_for_answer()


class SurveyAnswersFetchInput(Base):
    user_email: str
    survey_code: str

    @field_validator("user_email")
    def validate_user_email(cls, v) -> str:
        return Base.validate_email(v)

    @field_validator("survey_code")
    def validate_survey_join_code(cls, v) -> str:
        return Base.validate_survey_code(v)


class SurveyAnswersFetchOutput(Base):
    title: str
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
        ]
    ] = Field(
        min_length=1,
        description="Questions list must have at least 1 element",
    )
