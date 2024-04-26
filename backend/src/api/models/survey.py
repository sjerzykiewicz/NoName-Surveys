from pydantic import BaseModel, Field


class Question(BaseModel):
    required: bool
    question: str


class SingleQuestionBody(BaseModel):
    choices: list[str] = Field(
        min_length=2,
        description="Single choice question must have at least 2 options",
    )


class SingleQuestion(Question):
    single: SingleQuestionBody


class MultiQuestionBody(BaseModel):
    choices: list[str] = Field(
        min_length=2,
        description="Multiple choice question must have at least 2 options",
    )


class MultiQuestion(Question):
    multi: MultiQuestionBody


class ScaleQuestionBody(BaseModel):
    pass


class ScaleQuestion(Question):
    scale: ScaleQuestionBody


class SliderQuestionBody(BaseModel):
    min_value: float
    max_value: float


class SliderQuestion(Question):
    slider: SliderQuestionBody


class RankQuestionBody(BaseModel):
    choices: list[str] = Field(
        min_length=2, description="Rank question must have at least 2 options"
    )


class RankQuestion(Question):
    rank: RankQuestionBody


class TextQuestionBody(BaseModel):
    details: str


class TextQuestion(Question):
    text: TextQuestionBody


class ListQuestionBody(BaseModel):
    choices: list[str] = Field(
        min_length=2, description="List question must have at least 2 options"
    )


class ListQuestion(Question):
    list: ListQuestionBody


class Survey(BaseModel):
    title: str
    questions: list[
        SingleQuestion
        | MultiQuestion
        | ScaleQuestion
        | RankQuestion
        | TextQuestion
        | SliderQuestion
        | ListQuestion
    ] = []
