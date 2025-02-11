from sqlmodel import select

from src.db.base import Session
from src.db.models.answer import Answer


def find_by_survey_id(survey_id: int, session: Session) -> list[Answer]:
    statement = select(Answer).where(Answer.survey_id == survey_id)
    return session.exec(statement).all()


def is_signature_present(survey_id: int, y0: str, session: Session) -> bool:
    statement = (
        select(Answer).where(Answer.survey_id == survey_id).where(Answer.y0 == y0)
    )
    result = session.exec(statement).first()
    return result is not None


def save(survey_id: int, answer: str, y0: str, session: Session) -> None:
    answer = Answer(
        survey_id=survey_id,
        answer=answer,
        y0=y0,
    )
    answer = Answer.model_validate(answer)
    session.add(answer)
    session.commit()
    session.refresh(answer)
