from typing import Any, Literal
from pydantic import BaseModel

subclass_registry = {}


class Question(BaseModel):
    required: bool
    question: str

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        subclass_registry[cls.__name__] = cls
    
    class Config:
        extra = "allow"
        
    def __str__(self):
        return self.question


class TextQuestion(Question):
    question_type: Literal["text"] = "text"
    details: str

class SliderQuestion(Question):
    question_type: Literal["slider"] = "slider"
    min_value: float
    max_value: float
