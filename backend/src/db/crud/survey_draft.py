from src.db.base import Session
from src.db.models.survey_draft import SurveyDraft, SurveyDraftBase


def get_survey_drafts_for_user(
    user_id: int, session: Session
) -> list[SurveyDraft]:
    drafts = (
        session.query(SurveyDraft).filter(SurveyDraft.creator == user_id).all()
    )
    return [draft for draft in drafts]


def get_survey_draft_by_id(
    survey_draft_id: int, session: Session
) -> SurveyDraft:
    survey_draft = (
        session.query(SurveyDraft)
        .filter(SurveyDraft.id == survey_draft_id)
        .first()
    )
    return survey_draft


def create_survey_draft(
    survey_draft_create: SurveyDraftBase, session: Session
) -> SurveyDraft:
    survey_draft_create = SurveyDraft.model_validate(survey_draft_create)
    session.add(survey_draft_create)
    session.commit()
    session.refresh(survey_draft_create)
    return survey_draft_create
