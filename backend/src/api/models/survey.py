from pydantic import BaseModel, Field


class Question(BaseModel):
    required: bool
    question: str


class SingleQuestionBody(BaseModel):
    choices: list[str] = Field(
        min_length=2, description="SingleQuestion must have at least 2 choices"
    )


class SingleQuestion(Question):
    single: SingleQuestionBody


class MultiQuestionBody(BaseModel):
    choices: list[str] = Field(
        min_length=2, description="MultiQuestion must have at least 2 choices"
    )


class MultiQuestion(Question):
    multi: MultiQuestionBody


class ScaleQuestionBody(BaseModel):
    pass


class ScaleQuestion(Question):
    scale: ScaleQuestionBody


class SliderQuestionBody(BaseModel):
    min: float
    max: float


class SliderQuestion(Question):
    slider: SliderQuestionBody


class RankQuestionBody(BaseModel):
    choices: list[str] = Field(
        min_length=2, description="RankQuestion must have at least 2 choices"
    )


class RankQuestion(Question):
    rank: RankQuestionBody


class TextQuestionBody(BaseModel):
    details: str


class TextQuestion(Question):
    text: TextQuestionBody


class ListQuestionBody(BaseModel):
    choices: list[str] = Field(
        min_length=2, description="ListQuestion must have at least 2 choices"
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
