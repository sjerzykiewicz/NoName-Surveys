from fastapi.testclient import TestClient
import Crypto.Hash.SHA3_256 as SHA256
from datetime import datetime


TEST_VALID_USER_EMAIL_1 = "user1@st.amu.edu.pl"
TEST_VALID_USER_EMAIL_2 = "user2@st.amu.edu.pl"
TEST_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n3\n-----END PUBLIC KEY-----"


def create_user(client: TestClient, email: str):
    return client.post(
        "/users/register",
        json={
            "user_email": email,
        },
    )


def create_users(client: TestClient, emails: list[str]):
    for email in emails:
        create_user(client, email)


def create_user_with_public_key(client: TestClient, email: str):
    create_user(client, email)

    return client.post(
        "/users/update-public-key",
        json={
            "user_email": email,
            "public_key": TEST_PUBLIC_KEY,
            "fingerprint": SHA256.new(TEST_PUBLIC_KEY.encode()).hexdigest(),
        },
    )


def create_users_with_public_keys(client: TestClient, emails: list[str]):
    for email in emails:
        create_user_with_public_key(client, email)


def test_create_user_happy_path(client: TestClient):
    # when
    response = create_user(client, TEST_VALID_USER_EMAIL_1)

    # then
    assert response.status_code == 200


def test_create_user_that_already_exists(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = create_user(client, TEST_VALID_USER_EMAIL_1)

    # then
    assert response.status_code == 400


def test_get_users(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)

    # when
    response = client.get("/users/all")

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert TEST_VALID_USER_EMAIL_1 in data
    assert TEST_VALID_USER_EMAIL_2 in data


def test_get_users_with_keys(client: TestClient):
    # given
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)

    # when
    response = client.get("/users/all-with-public-keys")

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert TEST_VALID_USER_EMAIL_1 in data
    assert TEST_VALID_USER_EMAIL_2 not in data


def test_check_if_user_has_public_key_happy_path(client: TestClient):
    # given
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/users/has-public-key",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, bool)
    assert data


def test_check_if_user_has_public_key_when_user_not_registered(client: TestClient):
    # when
    response = client.post(
        "/users/has-public-key",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 400


def test_check_if_user_has_public_key_when_user_has_no_public_key(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/users/has-public-key",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, bool)
    assert not data


def test_update_public_key_happy_path(client: TestClient):
    # given & when
    response = create_user_with_public_key(client, TEST_VALID_USER_EMAIL_1)

    # then
    assert response.status_code == 200


def test_update_public_key_when_user_not_registered(client: TestClient):
    # when
    response = client.post(
        "/users/update-public-key",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "public_key": TEST_PUBLIC_KEY,
            "fingerprint": "12345",
        },
    )

    # then
    assert response.status_code == 400


def test_update_public_key_with_invalid_fingerprint(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/users/update-public-key",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "public_key": TEST_PUBLIC_KEY,
            "fingerprint": "12345",
        },
    )

    # then
    assert response.status_code == 400


def test_filter_unregistered_users(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/users/filter-unregistered-users",
        json={"emails": [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2]},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert TEST_VALID_USER_EMAIL_2 in data


def test_filter_users_with_no_public_keys(client: TestClient):
    # given
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/users/filter-users-with-no-public-key",
        json={"emails": [TEST_VALID_USER_EMAIL_1, TEST_VALID_USER_EMAIL_2]},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert TEST_VALID_USER_EMAIL_2 in data


def test_validate_user_happy_path(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/users/validate",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, bool)
    assert data


def test_validate_user_when_user_not_registered(client: TestClient):
    # when
    response = client.post(
        "/users/validate",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, bool)
    assert not data

def test_check_creation_date_when_user_not_registered(client: TestClient):
    # when
    response = client.post(
        "/users/key-creation-date",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 400

def test_check_if_key_creation_date_is_none_when_user_has_no_public_key(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/users/key-creation-date",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data is None

def test_get_key_creation_date_happy_path(client: TestClient):
    # given
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/users/key-creation-date",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data is not None
