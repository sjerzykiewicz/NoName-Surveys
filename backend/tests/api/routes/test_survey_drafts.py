from fastapi.testclient import TestClient
from test_users import create_user


TEST_VALID_USER_EMAIL_1 = "user1@st.amu.edu.pl"
TEST_VALID_USER_EMAIL_2 = "user2@st.amu.edu.pl"
TEST_SURVEY_DRAFT_TITLE = "Test Survey Draft"
TEST_SURVEY_DRAFT_STRUCTURE = {
    "questions": [
        {
            "question_type": "binary",
            "required": True,
            "question": "Is this a test draft?",
            "choices": ["Yes", "No"]
        }
    ]
}

def create_survey_draft(client: TestClient, email: str):
    return client.post(
        "/survey-drafts/create",
        json={
            "user_email": email,
            "title": TEST_SURVEY_DRAFT_TITLE,
            "survey_structure": TEST_SURVEY_DRAFT_STRUCTURE,
        },
    )


def test_create_survey_draft_user_not_found(client: TestClient):
    # when
    response = create_survey_draft(client, TEST_VALID_USER_EMAIL_1)

    # then
    assert response.status_code == 400


def test_create_survey_draft_happy_path(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = create_survey_draft(client, TEST_VALID_USER_EMAIL_1)

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, int)


def test_get_survey_drafts(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_survey_draft(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/survey-drafts/all/0",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == TEST_SURVEY_DRAFT_TITLE


def test_get_survey_drafts_user_is_not_creator(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_survey_draft_response = create_survey_draft(client, TEST_VALID_USER_EMAIL_1)
    survey_draft_id = create_survey_draft_response.json()

    # when
    response = client.post(
        "/survey-drafts/fetch",
        json={"user_email": TEST_VALID_USER_EMAIL_2, "id": survey_draft_id},
    )

    # then
    assert response.status_code == 403


def test_get_survey_draft(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_survey_draft_response = create_survey_draft(client, TEST_VALID_USER_EMAIL_1)
    survey_draft_id = create_survey_draft_response.json()

    # when
    response = client.post(
        "/survey-drafts/fetch",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "id": survey_draft_id},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == TEST_SURVEY_DRAFT_TITLE


def test_delete_survey_draft(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_survey_draft_response = create_survey_draft(client, TEST_VALID_USER_EMAIL_1)
    survey_draft_id = create_survey_draft_response.json()

    # when
    response = client.post(
        "/survey-drafts/delete",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "ids": [survey_draft_id]},
    )

    # then
    assert response.status_code == 200
    response = client.post(
        "/survey-drafts/count",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    assert response.status_code == 200
    data = response.json()
    assert data == 0


def test_count_survey_drafts(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_survey_draft(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/survey-drafts/count",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data == 1
