from sqlalchemy import func
from sqlmodel import select

from src.db.base import Session
from src.db.models.access_to_view_results import AccessToViewResults
from src.db.models.survey import Survey
from src.db.models.user import User


def get_count_of_not_deleted_surveys_for_user(user_id: int, session: Session) -> int:
    statement = (
        select(func.count(Survey.id))
        .where(Survey.creator_id == user_id)
        .where(Survey.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).one()


def get_survey_by_code(survey_code: str, session: Session) -> Survey:
    statement = (
        select(Survey)
        .where(Survey.survey_code == survey_code)
        .where(Survey.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).first()


def get_active_survey_by_code(survey_code: str, session: Session) -> Survey:
    statement = (
        select(Survey)
        .where(Survey.survey_code == survey_code)
        .where(Survey.is_deleted == False)  # noqa: E712
        .where(Survey.is_enabled == True)  # noqa: E712
    )
    return session.exec(statement).first()


def delete_surveys(
    user_id: int, survey_codes: list[str], session: Session
) -> list[Survey]:
    statement = (
        select(Survey)
        .where(Survey.creator_id == user_id)
        .where(Survey.survey_code.in_(survey_codes))
        .where(Survey.is_deleted == False)  # noqa: E712
    )
    surveys = session.exec(statement).all()
    for survey in surveys:
        survey.is_deleted = True
    session.commit()
    return surveys


def get_all_surveys_user_has_ownership_over(
    user_id: int, session: Session
) -> list[Survey]:
    statement = (
        select(Survey)
        .where(Survey.creator_id == user_id)
        .where(Survey.is_deleted == False)  # noqa: E712
        .order_by(Survey.id.desc())
    )
    return session.exec(statement).all()


def get_count_of_active_surveys_of_user(user_id: int, session: Session) -> int:
    statement = (
        select(func.count(Survey.id))
        .where(Survey.creator_id == user_id)
        .where(Survey.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).one()


def survey_code_taken(survey_code: str, session: Session) -> bool:
    statement = (
        select(Survey)
        .where(Survey.survey_code == survey_code)
        .where(Survey.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).first() is not None


def create_survey(
    creator_id: int,
    uses_cryptographic_module: bool,
    survey_structure_id: int,
    survey_code: str,
    session: Session,
) -> Survey:
    survey_create = Survey(
        creator_id=creator_id,
        uses_cryptographic_module=uses_cryptographic_module,
        survey_structure_id=survey_structure_id,
        survey_code=survey_code,
    )
    survey_create = Survey.model_validate(survey_create)
    session.add(survey_create)
    session.commit()
    session.refresh(survey_create)
    return survey_create


def give_survey_access(survey_id: int, user_id: int, session: Session) -> None:
    survey_access = session.exec(
        select(AccessToViewResults)
        .where(AccessToViewResults.survey_id == survey_id)
        .where(AccessToViewResults.user_id == user_id)
    ).first()

    if survey_access:
        survey_access.is_deleted = False
    else:
        survey_access = AccessToViewResults(
            survey_id=survey_id,
            user_id=user_id,
        )

    session.add(survey_access)
    session.commit()
    session.refresh(survey_access)


def take_away_survey_access(
    owner: int, survey_id: int, users_ids: list[int], session: Session
) -> list[AccessToViewResults]:
    statement = (
        select(AccessToViewResults)
        .where(AccessToViewResults.user_id != owner)
        .where(AccessToViewResults.survey_id == survey_id)
        .where(AccessToViewResults.user_id.in_(users_ids))
        .where(AccessToViewResults.is_deleted == False)  # noqa: E712
    )
    accesses = session.exec(statement).all()
    for access in accesses:
        access.is_deleted = True
    session.commit()
    return accesses


def reject_access_to_surveys(
    user_id: int, survey_codes: list[str], session: Session
) -> list[AccessToViewResults]:
    statement = (
        select(AccessToViewResults)
        .join(Survey)
        .where(AccessToViewResults.user_id == user_id)
        .where(AccessToViewResults.survey_id == Survey.id)
        .where(Survey.survey_code.in_(survey_codes))
        .where(Survey.creator_id != user_id)
        .where(AccessToViewResults.is_deleted == False)  # noqa: E712
    )
    accesses = session.exec(statement).all()
    for access in accesses:
        access.is_deleted = True
    session.commit()
    return accesses


def get_all_surveys_user_can_view(
    user_id: int, offset: int, limit: int, session: Session
) -> list[tuple[Survey, bool]]:
    statement = (
        select(AccessToViewResults.survey_id)
        .where(AccessToViewResults.user_id == user_id)
        .where(AccessToViewResults.is_deleted == False)  # noqa: E712
    )
    survey_accesses_ids = session.exec(statement).all()

    surveys = session.exec(
        select(Survey)
        .where(Survey.id.in_(survey_accesses_ids))
        .where(Survey.is_deleted == False)  # noqa: E712
        .order_by(Survey.id.desc())
        .offset(offset)
        .limit(limit)
    ).all()

    return [(survey, survey.creator_id == user_id) for survey in surveys if survey]


def get_all_users_with_access_to_survey_count(survey_id: int, session: Session) -> int:
    statement = (
        select(func.count(AccessToViewResults.id))
        .where(AccessToViewResults.survey_id == survey_id)
        .where(AccessToViewResults.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).one()


def get_all_users_with_no_access_to_survey(
    survey_id: int, session: Session
) -> list[str]:
    statement = select(User.email).where(
        User.id.notin_(
            select(AccessToViewResults.user_id)
            .where(AccessToViewResults.survey_id == survey_id)
            .where(AccessToViewResults.is_deleted == False)  # noqa: E712
            .distinct()
        )
    )
    return session.exec(statement).all()


def get_all_users_with_access_to_survey(
    survey_id: int, offset: int, limit: int, session: Session
) -> list[AccessToViewResults]:
    statement = (
        select(AccessToViewResults)
        .join(User, AccessToViewResults.user_id == User.id)
        .where(AccessToViewResults.survey_id == survey_id)
        .where(AccessToViewResults.is_deleted == False)  # noqa: E712
        .order_by(User.email.asc())
        .offset(offset)
        .limit(limit)
    )
    return session.exec(statement).all()


def user_has_access_to_survey(user_id: int, survey_id: int, session: Session) -> bool:
    statement = (
        select(AccessToViewResults)
        .where(AccessToViewResults.user_id == user_id)
        .where(AccessToViewResults.survey_id == survey_id)
        .where(AccessToViewResults.is_deleted == False)  # noqa: E712
    )
    return session.exec(statement).first() is not None


def enable_or_disable_survey(
    survey_id: int, is_enabled: bool, session: Session
) -> None:
    survey = session.exec(select(Survey).where(Survey.id == survey_id)).first()
    survey.is_enabled = is_enabled
    session.commit()
    session.refresh(survey)
    return survey
