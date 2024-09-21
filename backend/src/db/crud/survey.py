from sqlmodel import select

from src.db.base import Session
from src.db.models.survey import Survey, SurveyBase


def get_survey_by_code(survey_code: str, session: Session) -> Survey:
    statement = select(Survey).where(
        (Survey.survey_code == survey_code) & (Survey.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).first()


def delete_survey_by_code(survey_code: str, session: Session) -> Survey:
    statement = select(Survey).where(Survey.survey_code == survey_code)
    survey = session.exec(statement).first()
    survey.is_deleted = True
    session.commit()
    return survey


def get_all_surveys_for_user(user_id: int, session: Session) -> list[Survey]:
    statement = select(Survey).where(
        (Survey.creator_id == user_id) & (Survey.is_deleted == False)  # noqa: E712
    )
    return [survey for survey in session.exec(statement).all()]


def survey_code_taken(survey_code: str, session: Session) -> bool:
    statement = select(Survey).where(
        (Survey.survey_code == survey_code) & (Survey.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).first() is not None


def create_survey(survey_create: SurveyBase, session: Session) -> Survey:
    survey_create = Survey.model_validate(survey_create)
    session.add(survey_create)
    session.commit()
    session.refresh(survey_create)
    return survey_create
