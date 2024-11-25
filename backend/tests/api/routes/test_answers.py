from fastapi.testclient import TestClient
from test_users import create_user
from test_surveys import create_survey

TEST_VALID_USER_EMAIL_1 = "user1@st.amu.edu.pl"
TEST_VALID_USER_EMAIL_2 = "user2@st.amu.edu.pl"


def test_fetch_survey_answers_user_not_found(client: TestClient):
    # when
    response = client.post(
        "/answers/fetch",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "survey_code": "000000"},
    )

    # then
    assert response.status_code == 400


def test_fetch_survey_answers_survey_not_found(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/answers/fetch",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "survey_code": "000000"},
    )

    # then
    assert response.status_code == 400


def test_fetch_survey_answers_happy_path(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]

    # when
    response = client.post(
        "/answers/fetch",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "survey_code": survey_code},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0


def test_fetch_survey_answers_user_not_allowed(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]

    # when
    response = client.post(
        "/answers/fetch",
        json={"user_email": TEST_VALID_USER_EMAIL_2, "survey_code": survey_code},
    )

    # then
    assert response.status_code == 400


def test_save_survey_answer_public_survey(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]

    # when
    response = client.post(
        "/answers/fill",
        json={
            "survey_code": survey_code,
            "questions": [
                {
                    "question_type": "binary",
                    "required": True,
                    "question": "Is this a test?",
                    "choices": ["Yes", "No"],
                    "answer": "Yes",
                }
            ],
        },
    )

    # then
    assert response.status_code == 200
