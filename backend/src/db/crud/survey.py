from sqlmodel import select

from src.db.base import Session
from src.db.crud.survey_draft import get_survey_drafts_for_user
from src.db.models.survey import Survey, SurveyBase


def get_survey_by_code(survey_code: str, session: Session) -> Survey:
    survey = (
        session.query(Survey).filter(Survey.survey_code == survey_code).first()
    )
    return survey


def get_surveys_for_user(user_id: int, session: Session) -> list[Survey]:
    survey_drafts_ids = {
        draft.id for draft in get_survey_drafts_for_user(user_id, session)
    }
    surveys = session.exec(select(Survey)).all()
    return [
        survey
        for survey in surveys
        if survey.survey_structure_id in survey_drafts_ids
    ]


def create_survey_draft(survey_create: SurveyBase, session: Session) -> Survey:
    survey_create = Survey.model_validate(survey_create)
    session.add(survey_create)
    session.commit()
    session.refresh(survey_create)
    return survey_create
