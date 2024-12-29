
import src.db.crud.ring_member as ring_member_repository
import src.db.crud.survey as survey_repository
import src.db.crud.user as user_repository


def test_get_ring_members_for_survey(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    ring_member_repository.add_ring_member(survey.id, user.email, "public_key_1", session)

    # when
    members = ring_member_repository.get_ring_members_for_survey(survey.id, session)

    # then
    assert len(members) == 1


def test_get_public_keys_for_survey(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    ring_member_repository.add_ring_member(survey.id, user.email, "public_key_1", session)

    # when
    public_keys = ring_member_repository.get_public_keys_for_survey(survey.id, session)

    # then
    assert len(public_keys) == 1
    assert public_keys[0] == "public_key_1"


def test_get_ring_members_for_survey_paginated(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    ring_member_repository.add_ring_member(survey.id, user.email, "public_key_1", session)

    # when
    members = ring_member_repository.get_ring_members_for_survey_paginated(survey.id, 0, 10, session)

    # then
    assert len(members) == 1


def test_get_ring_member_count_for_survey(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    ring_member_repository.add_ring_member(survey.id, user.email, "public_key_1", session)

    # when
    count = ring_member_repository.get_ring_member_count_for_survey(survey.id, session)

    # then
    assert count == 1


def test_add_ring_member(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # when
    ring_member_repository.add_ring_member(survey.id, user.email, "public_key_1", session)
    members = ring_member_repository.get_ring_members_for_survey(survey.id, session)

    # then
    assert len(members) == 1
    assert members[0].public_key == "public_key_1"
