from fastapi.testclient import TestClient
from test_users import create_user, create_user_with_public_key

TEST_VALID_USER_EMAIL_1 = "user1@st.amu.edu.pl"
TEST_VALID_USER_EMAIL_2 = "user2@st.amu.edu.pl"
TEST_VALID_USER_EMAIL_3 = "user3@st.amu.edu.pl"
TEST_SURVEY_TITLE = "Test Survey"
TEST_SURVEY_STRUCTURE = {
    "questions": [
        {
            "question_type": "binary",
            "required": True,
            "question": "Is this a test?",
            "choices": ["Yes", "No"]
        }
    ]
}


def create_survey(
    client: TestClient,
    email: str,
    uses_cryptographic_module: bool = False,
    ring_members: list[str] = []
):
    return client.post(
        "/surveys/create",
        json={
            "user_email": email,
            "title": TEST_SURVEY_TITLE,
            "survey_structure": TEST_SURVEY_STRUCTURE,
            "uses_cryptographic_module": uses_cryptographic_module,
            "ring_members": ring_members,
        },
    )


def test_count_surveys_for_user(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/surveys/count",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data == 0


def test_count_surveys_for_user_with_surveys(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_survey(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/surveys/count",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data == 1


def test_create_survey_happy_path(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = create_survey(client, TEST_VALID_USER_EMAIL_1)

    # then
    assert response.status_code == 200
    data = response.json()
    assert "survey_code" in data


def test_create_survey_user_not_registered(client: TestClient):
    # when
    response = create_survey(client, TEST_VALID_USER_EMAIL_1)

    # then
    assert response.status_code == 400


def test_create_survey_with_cryptographic_module(client: TestClient):
    # given
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_1)
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_2)

    # when
    response = create_survey(
        client,
        TEST_VALID_USER_EMAIL_1,
        True,
        [TEST_VALID_USER_EMAIL_2]
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert "survey_code" in data


def test_create_survey_with_invalid_ring_members(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = create_survey(
        client,
        TEST_VALID_USER_EMAIL_1,
        True,
        [TEST_VALID_USER_EMAIL_2]
    )

    # then
    assert response.status_code == 400


def test_get_surveys_for_user(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_survey(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/surveys/all/0",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == TEST_SURVEY_TITLE


def test_get_survey_by_code(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]

    # when
    response = client.post(
        "/surveys/fetch",
        json={"survey_code": survey_code},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == TEST_SURVEY_TITLE


def test_count_survey_respondents(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]

    # when
    response = client.post(
        "/surveys/respondents-count",
        json={"survey_code": survey_code},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data == 0


def test_count_survey_respondents_safe_survey(client: TestClient):
    # given
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_1)
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_2)
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_3)
    create_survey_response = create_survey(
        client,
        TEST_VALID_USER_EMAIL_1,
        True,
        [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2, TEST_VALID_USER_EMAIL_3]
    )
    survey_code = create_survey_response.json()["survey_code"]

    # when
    response = client.post(
        "/surveys/respondents-count",
        json={"survey_code": survey_code},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data == 3


def test_get_respondents_by_code(client: TestClient):
    # given
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_1)
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_2)
    create_survey_response = create_survey(
        client,
        TEST_VALID_USER_EMAIL_1,
        True,
        [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2]
    )
    survey_code = create_survey_response.json()["survey_code"]

    # when
    response = client.post(
        "/surveys/respondents/0",
        json={"survey_code": survey_code},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert TEST_VALID_USER_EMAIL_1 in data
    assert TEST_VALID_USER_EMAIL_2 in data


def test_delete_survey(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]

    # when
    response = client.post(
        "/surveys/delete",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "survey_codes": [survey_code]},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "survey deleted successfully"


def test_get_count_of_users_with_access_to_surveys(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]
    client.post(
        "/surveys/give-access",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
            "user_emails": [TEST_VALID_USER_EMAIL_2],
        },
    )

    # when
    response = client.post(
        "/surveys/all-with-access-count",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
        },
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data == 2


def test_get_all_users_without_access_to_surveys(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_user(client, TEST_VALID_USER_EMAIL_3)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]
    client.post(
        "/surveys/give-access",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
            "user_emails": [TEST_VALID_USER_EMAIL_2],
        },
    )

    # when
    response = client.post(
        "/surveys/all-without-access",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
        },
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert TEST_VALID_USER_EMAIL_3 in data


def test_give_access_to_surveys(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]

    # when
    response = client.post(
        "/surveys/give-access",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
            "user_emails": [TEST_VALID_USER_EMAIL_2],
        },
    )

    # then
    assert response.status_code == 200

    response = client.post(
        "/surveys/all-with-access-count",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data == 2


def test_take_away_access_to_surveys(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]
    client.post(
        "/surveys/give-access",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
            "user_emails": [TEST_VALID_USER_EMAIL_2],
        },
    )

    # when
    response = client.post(
        "/surveys/take-away-access",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
            "user_emails": [TEST_VALID_USER_EMAIL_2],
        },
    )

    # then
    assert response.status_code == 200

    response = client.post(
        "/surveys/all-with-access-count",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data == 1


def test_check_access_to_surveys(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]
    client.post(
        "/surveys/give-access",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
            "user_emails": [TEST_VALID_USER_EMAIL_2],
        },
    )

    # when
    response = client.post(
        "/surveys/get-all-with-access/0",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
        },
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2


def test_reject_access_to_surveys(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_survey_response = create_survey(client, TEST_VALID_USER_EMAIL_1)
    survey_code = create_survey_response.json()["survey_code"]
    client.post(
        "/surveys/give-access",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
            "user_emails": [TEST_VALID_USER_EMAIL_2],
        },
    )

    # when
    response = client.post(
        "/surveys/reject-access",
        json={
            "user_email": TEST_VALID_USER_EMAIL_2,
            "survey_codes": [survey_code],
        },
    )

    # then
    assert response.status_code == 200

    response = client.post(
        "/surveys/get-all-with-access/0",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "survey_code": survey_code,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1  # Only the owner should have access now
