from pydantic import BaseModel
from src.api.models.question_base import Question, subclass_registry


class Survey(BaseModel):
    title: str
    questions: list[Question] = []

    # this funky method allows us to instantiate the correct subclass of Question
    def __init__(self, **kwargs):
        for index in range(len(kwargs["questions"])):
            cur_question = kwargs["questions"][index]
            if isinstance(cur_question, dict):
                item_question_keys = sorted(cur_question.keys())
                assigned_subclass = False
                for _, subclass in subclass_registry.items():
                    registry_question_keys = sorted(subclass.__fields__.keys())
                    if item_question_keys == registry_question_keys:
                        cur_question = subclass(**cur_question)
                        assigned_subclass = True
                        break
                if not assigned_subclass:
                    raise ValueError(f"Question {cur_question} does not match any known question types")
                kwargs["questions"][index] = cur_question
            else:
                raise ValueError("Questions must be a list of dictionaries")

        super().__init__(**kwargs)
