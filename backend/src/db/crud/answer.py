from sqlmodel import select

from src.db.base import Session
from src.db.models.answer import Answer, AnswerBase


def get_answers_by_survey_id(survey_id: int, session: Session) -> Answer:
    statement = select(Answer).where(Answer.survey_id == survey_id)
    return [answer for answer in session.exec(statement).all()]


def user_already_answered_survey(
    survey_id: str, y0: str, session: Session
) -> bool:
    statement = select(Answer).where(
        (Answer.survey_id == survey_id) & (Answer.y0 == y0)
    )
    return session.exec(statement).first() is not None


def save_answer(answer: AnswerBase, session: Session) -> None:
    answer = Answer.model_validate(answer)
    session.add(answer)
    session.commit()
    session.refresh(answer)
