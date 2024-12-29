import src.db.crud.survey_draft as survey_draft_repository
import src.db.crud.user as user_repository

DRAFT_NAME = "Draft 1"
DRAFT_STRUCTURE = "{}"

def test_get_count_of_not_deleted_survey_drafts_for_user(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey_draft_repository.create_survey_draft(user.id, DRAFT_NAME, DRAFT_STRUCTURE, False, session)

    # when
    count = survey_draft_repository.get_count_of_not_deleted_survey_drafts_for_user(user.id, session)

    # then
    assert count == 1


def test_get_not_deleted_survey_drafts_for_user(session):
    # given
    user = user_repository.create("test@example.com", session)
    survey_draft_repository.create_survey_draft(user.id, DRAFT_NAME, DRAFT_STRUCTURE, False, session)

    # when
    drafts = survey_draft_repository.get_not_deleted_survey_drafts_for_user(user.id, 0, 10, session)

    # then
    assert len(drafts) == 1


def test_find_not_deleted_by_id(session):
    # given
    user = user_repository.create("test@example.com", session)
    draft = survey_draft_repository.create_survey_draft(user.id, DRAFT_NAME, DRAFT_STRUCTURE, False, session)

    # when
    found_draft = survey_draft_repository.find_not_deleted_by_id(draft.id, session)

    # then
    assert found_draft is not None
    assert found_draft.id == draft.id


def test_find_by_id(session):
    # given
    user = user_repository.create("test@example.com", session)
    draft = survey_draft_repository.create_survey_draft(user.id, DRAFT_NAME, DRAFT_STRUCTURE, False, session)

    # when
    found_draft = survey_draft_repository.find_by_id(draft.id, session)

    # then
    assert found_draft is not None
    assert found_draft.id == draft.id


def test_delete_survey_drafts(session):
    # given
    user = user_repository.create("test@example.com", session)
    draft = survey_draft_repository.create_survey_draft(user.id, DRAFT_NAME, DRAFT_STRUCTURE, False, session)

    # when
    drafts = survey_draft_repository.delete_survey_drafts(user.id, [draft.id], session)

    # then
    assert len(drafts) == 1
    assert drafts[0].is_deleted


def test_create_survey_draft(session):
    # given
    user = user_repository.create("test@example.com", session)

    # when
    draft = survey_draft_repository.create_survey_draft(user.id, DRAFT_NAME, DRAFT_STRUCTURE, False, session)

    # then
    assert draft.title == DRAFT_NAME
    assert draft.survey_structure == DRAFT_STRUCTURE
    assert not draft.is_deleted
