from src.db.base import Session
from src.db.models.answer import Answer, AnswerBase


def get_answers_by_survey_id(survey_id: int, session: Session) -> Answer:
    survey = session.query(Answer).filter(Answer.survey_id == survey_id).all()
    return survey


def save_answer(answer: AnswerBase, session: Session) -> None:
    answer = Answer.model_validate(answer)
    session.add(answer)
    session.commit()
    session.refresh(answer)
