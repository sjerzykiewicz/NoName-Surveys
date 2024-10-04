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


def get_ring_member_count_for_survey(survey_id: int, session: Session) -> int:
    statement = select(func.count(RingMember.id)).where(
        RingMember.survey_id == survey_id
    )
    member_count = session.exec(statement).one()
    return member_count


def add_ring_member(ring_member: RingMemberBase, session: Session) -> None:
    ring_member = RingMember.model_validate(ring_member)
    session.add(ring_member)
    session.commit()
    session.refresh(ring_member)
