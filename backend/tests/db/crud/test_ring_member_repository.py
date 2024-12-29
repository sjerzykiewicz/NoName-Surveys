import src.db.crud.ring_member as ring_member_repository
import src.db.crud.survey as survey_repository
import src.db.crud.user as user_repository


def test_get_ring_members_for_survey(session):
    # given
    user_1 = user_repository.create("test1@example.com", session)
    user_2 = user_repository.create("test2@example.com", session)
    survey = survey_repository.create_survey(user_1.id, False, 1, "survey1", session)
    ring_member_repository.add_ring_member(
        survey.id, user_1.email, "public_key_1", session
    )
    ring_member_repository.add_ring_member(
        survey.id, user_2.email, "public_key_2", session
    )

    # when
    members = ring_member_repository.get_ring_members_for_survey(survey.id, session)

    # then
    assert len(members) == 2


def test_get_public_keys_for_survey(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, True, 1, "survey1", session)
    ring_member_repository.add_ring_member(
        survey.id, user.email, "public_key_1", session
    )

    # when
    public_keys = ring_member_repository.get_public_keys_for_survey(survey.id, session)

    # then
    assert len(public_keys) == 1
    assert public_keys[0] == "public_key_1"


def test_get_public_keys_for_survey_multiple_keys(session):
    # given
    user_1 = user_repository.create("test1@example.com", session)
    user_2 = user_repository.create("test2@example.com", session)
    survey = survey_repository.create_survey(user_1.id, True, 1, "survey1", session)
    ring_member_repository.add_ring_member(
        survey.id, user_1.email, "public_key_1", session
    )
    ring_member_repository.add_ring_member(
        survey.id, user_2.email, "public_key_2", session
    )

    # when
    public_keys = ring_member_repository.get_public_keys_for_survey(survey.id, session)

    # then
    assert len(public_keys) == 2
    assert "public_key_1" in public_keys
    assert "public_key_2" in public_keys


def test_get_ring_members_for_survey_paginated(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, True, 1, "survey1", session)
    ring_member_repository.add_ring_member(
        survey.id, user.email, "public_key_1", session
    )

    # when
    members = ring_member_repository.get_ring_members_for_survey_paginated(
        survey.id, 0, 10, session
    )

    # then
    assert len(members) == 1
    assert members[0] == user.email


def test_get_ring_members_for_survey_paginated_second_page(session):
    # given
    user_1 = user_repository.create("test1@example.com", session)
    user_2 = user_repository.create("test2@example.com", session)
    survey = survey_repository.create_survey(user_1.id, True, 1, "survey1", session)
    ring_member_repository.add_ring_member(
        survey.id, user_1.email, "public_key_1", session
    )
    ring_member_repository.add_ring_member(
        survey.id, user_2.email, "public_key_2", session
    )

    # when
    members = ring_member_repository.get_ring_members_for_survey_paginated(
        survey.id, 1, 1, session
    )

    # then
    assert len(members) == 1
    assert members[0] == user_2.email


def test_get_ring_members_for_survey_paginated_out_of_range(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, True, 1, "survey1", session)
    ring_member_repository.add_ring_member(
        survey.id, user.email, "public_key_1", session
    )

    # when
    members = ring_member_repository.get_ring_members_for_survey_paginated(
        survey.id, 1, 10, session
    )

    # then
    assert len(members) == 0


def test_get_ring_member_count_for_survey(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)
    ring_member_repository.add_ring_member(
        survey.id, user.email, "public_key_1", session
    )

    # when
    result = ring_member_repository.get_ring_member_count_for_survey(survey.id, session)

    # then
    assert result == 1


def test_add_ring_member(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey = survey_repository.create_survey(user.id, False, 1, "survey1", session)

    # when
    ring_member_repository.add_ring_member(
        survey.id, user.email, "public_key_1", session
    )
    members = ring_member_repository.get_ring_members_for_survey(survey.id, session)

    # then
    assert len(members) == 1
    assert members[0].public_key == "public_key_1"
