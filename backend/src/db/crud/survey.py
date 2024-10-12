from sqlmodel import select

from src.db.base import Session
from src.db.models.access_to_view_results import AccessToViewResults
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


def get_all_surveys_user_has_ownership_over(
    user_id: int, session: Session
) -> list[Survey]:
    statement = select(Survey).where(
        (Survey.creator_id == user_id) & (Survey.is_deleted == False)  # noqa: E712
    )
    return [survey for survey in session.exec(statement).all()]


def get_count_of_active_surveys_of_user(user_id: int, session: Session) -> int:
    statement = select(Survey).where(
        (Survey.creator_id == user_id) & (Survey.is_deleted == False)  # noqa: E712
    )
    return len(session.exec(statement).all())


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


def give_survey_access(survey_id: int, user_id: int, session: Session) -> None:
    survey_access = session.exec(
        select(AccessToViewResults).where(
            (AccessToViewResults.survey_id == survey_id)
            & (AccessToViewResults.user_id == user_id)
        )
    ).first()
    if survey_access:
        survey_access.is_deleted = False
        session.commit()
        return

    access = AccessToViewResults(survey_id=survey_id, user_id=user_id)
    session.add(access)
    session.commit()
    session.refresh(access)


def take_away_survey_access(survey_id: int, user_id: int, session: Session) -> None:
    survey_access = session.exec(
        select(AccessToViewResults).where(
            (AccessToViewResults.survey_id == survey_id)
            & (AccessToViewResults.user_id == user_id)
        )
    ).first()
    if survey_access:
        survey_access.is_deleted = True
        session.commit()
        return


def get_all_surveys_user_can_view(
    user_id: int, session: Session
) -> list[tuple[Survey, bool]]:
    statement = select(AccessToViewResults).where(
        (AccessToViewResults.user_id == user_id)
        & (AccessToViewResults.is_deleted == False)  # noqa: E712
    )
    survey_accesses = [access for access in session.exec(statement).all()]

    surveys = [
        session.exec(
            select(Survey).where(
                (Survey.id == access.survey_id)
                & (Survey.is_deleted == False)  # noqa: E712
            )
        ).first()
        for access in survey_accesses
    ]

    return [(survey, survey.creator_id == user_id) for survey in surveys if survey]


def get_all_users_with_access_to_survey(
    survey_id: int, session: Session
) -> list[AccessToViewResults]:
    statement = select(AccessToViewResults).where(
        (AccessToViewResults.survey_id == survey_id)
        & (AccessToViewResults.is_deleted == False)  # noqa: E712
    )
    return [access for access in session.exec(statement).all()]


def user_has_access_to_survey(user_id: int, survey_id: int, session: Session) -> bool:
    statement = select(AccessToViewResults).where(
        (AccessToViewResults.user_id == user_id)
        & (AccessToViewResults.survey_id == survey_id)
        & (AccessToViewResults.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).first() is not None
