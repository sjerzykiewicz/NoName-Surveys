from sqlmodel import select

from src.db.base import Session
from src.db.models.survey_draft import SurveyDraft, SurveyDraftBase


def get_survey_drafts_for_user(
    user_id: int, session: Session
) -> list[SurveyDraft]:
    statement = select(SurveyDraft).where(SurveyDraft.creator_id == user_id)
    drafts = session.exec(statement).all()
    return [draft for draft in drafts]


def get_survey_draft_by_id(
    survey_draft_id: int, session: Session
) -> SurveyDraft:
    statement = select(SurveyDraft).where(SurveyDraft.id == survey_draft_id)
    survey_draft = session.exec(statement).first()
    return survey_draft


def create_survey_draft(
    survey_draft_create: SurveyDraftBase, session: Session
) -> SurveyDraft:
    survey_draft_create = SurveyDraft.model_validate(survey_draft_create)
    session.add(survey_draft_create)
    session.commit()
    session.refresh(survey_draft_create)
    return survey_draft_create
