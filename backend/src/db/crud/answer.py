from sqlmodel import select

from src.db.base import Session
from src.db.models.answer import Answer, AnswerBase


def get_answers_by_survey_id(survey_id: int, session: Session) -> Answer:
    statement = select(Answer).where(Answer.survey_id == survey_id)
    return [answer for answer in session.exec(statement).all()]


def save_answer(answer: AnswerBase, session: Session) -> None:
    answer = Answer.model_validate(answer)
    session.add(answer)
    session.commit()
    session.refresh(answer)
