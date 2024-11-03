from sqlalchemy import func
from sqlmodel import select

from src.db.base import Session
from src.db.models.survey_draft import SurveyDraft, SurveyDraftBase


def get_count_of_not_deleted_survey_drafts_for_user(
    user_id: int, session: Session
) -> int:
    statement = select(func.count(SurveyDraft.id)).where(
        (SurveyDraft.creator_id == user_id)
        & (SurveyDraft.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).one()


def get_not_deleted_survey_drafts_for_user(
    user_id: int, offset: int, limit: int, session: Session
) -> list[SurveyDraft]:
    statement = (
        select(SurveyDraft)
        .where(
            (SurveyDraft.creator_id == user_id)
            & (SurveyDraft.is_deleted == False)  # noqa: E712
        )
        .offset(offset)
        .limit(limit)
    )
    drafts = session.exec(statement).all()
    return [draft for draft in drafts]


def get_not_deleted_survey_draft_by_id(
    survey_draft_id: int, session: Session
) -> SurveyDraft:
    statement = select(SurveyDraft).where(
        (SurveyDraft.id == survey_draft_id)
        & (SurveyDraft.is_deleted == False)  # noqa: E712
    )
    survey_draft = session.exec(statement).first()
    return survey_draft


def get_survey_draft_by_id(survey_draft_id: int, session: Session) -> SurveyDraft:
    statement = select(SurveyDraft).where(SurveyDraft.id == survey_draft_id)
    survey_draft = session.exec(statement).first()
    return survey_draft


def delete_survey_draft_by_id(survey_draft_id: int, session: Session) -> SurveyDraft:
    statement = select(SurveyDraft).where(SurveyDraft.id == survey_draft_id)
    survey_draft = session.exec(statement).first()
    survey_draft.is_deleted = True
    session.commit()
    return survey_draft


def create_survey_draft(
    creator_id: int,
    title: str,
    survey_structure: str,
    is_deleted: bool,
    session: Session,
) -> SurveyDraft:
    survey_draft_create = SurveyDraftBase(
        creator_id=creator_id,
        title=title,
        survey_structure=survey_structure,
        is_deleted=is_deleted,
    )
    survey_draft_create = SurveyDraft.model_validate(survey_draft_create)
    session.add(survey_draft_create)
    session.commit()
    session.refresh(survey_draft_create)
    return survey_draft_create
