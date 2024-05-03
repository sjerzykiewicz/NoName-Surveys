from sqlmodel import select

from src.db.base import Session
from src.db.models.survey_draft import SurveyDraft, SurveyDraftBase


def get_survey_drafts(session: Session) -> list[SurveyDraft]:
    drafts = session.exec(select(SurveyDraft)).all()
    return [draft for draft in drafts]


def create_survey_draft(
    survey_draft_create: SurveyDraftBase, session: Session
) -> SurveyDraft:
    survey_draft_create = SurveyDraft.model_validate(survey_draft_create)
    session.add(survey_draft_create)
    session.commit()
    session.refresh(survey_draft_create)
    return survey_draft_create
