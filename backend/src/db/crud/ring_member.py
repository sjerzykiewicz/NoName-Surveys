from sqlalchemy import func
from sqlmodel import select

from src.db.base import Session
from src.db.models.ring_member import RingMember, RingMemberBase


def get_ring_members_for_survey(
    survey_id: int, session: Session
) -> list[RingMemberBase]:
    statement = select(RingMember).where(RingMember.survey_id == survey_id)
    ring_members = session.exec(statement).all()
    return [ring_member for ring_member in ring_members]


def get_ring_members_for_survey_paginated(
    survey_id: int, offset: int, limit: int, session: Session
) -> list[RingMemberBase]:
    statement = (
        select(RingMember)
        .where(RingMember.survey_id == survey_id)
        .order_by(RingMember.user_email.asc())
        .offset(offset)
        .limit(limit)
    )
    ring_members = session.exec(statement).all()
    return [ring_member for ring_member in ring_members]


def get_ring_member_count_for_survey(survey_id: int, session: Session) -> int:
    statement = select(func.count(RingMember.id)).where(
        RingMember.survey_id == survey_id
    )
    return session.exec(statement).one()


def add_ring_member(
    survey_id: int, user_email: str, public_key: str, session: Session
) -> None:
    ring_member = RingMember(
        survey_id=survey_id, user_email=user_email, public_key=public_key
    )
    session.add(ring_member)
    session.commit()
    session.refresh(ring_member)
