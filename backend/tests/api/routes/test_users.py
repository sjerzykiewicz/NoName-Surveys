from fastapi.testclient import TestClient
import Crypto.Hash.SHA3_256 as SHA256


TEST_VALID_USER_EMAIL_1 = "user1@st.amu.edu.pl"
TEST_VALID_USER_EMAIL_2 = "user2@st.amu.edu.pl"
TEST_PUBLIC_KEY = "".join(
    (
        "-----BEGIN PUBLIC KEY-----\n",
        "MTcwNDAzNTg4MzkyMjE3NTU2MDQyMjE4MDk2MDMwMDc1MzcxMzUxODM1NjI4Mzgz\n",
        "MDIwNTU3MTM0ODkwMTIyNzQ2MTQ3NTg1NzM1OTg5Mzk3MTI3MDc0OTc0Njk1MDIy\n",
        "NTUyODkxMTE0NzUwMjA1OTcxMDg3ODgwODY0MjU3NzI4OTk4MTIzOTU4OTA5MzE4\n",
        "ODg0NDQ3MDM2MzY0Mzg3MjY3Mjk0MzIzMzIzMTM1MzAxODY1MTUyNDk2ODAwNDA1\n",
        "MzM4ODk5MDg3NTk3MTk3OTc2OTkwMzc3ODg4NzQ0MjQyODQwMTUzNTU2NzM2ODg4\n",
        "MTQxMDc0NzIwNzYwNjg2ODU1MzA5MDk0MTkwMDU3MzMwOTAxNTI1ODI1NDE5MTY4\n",
        "NDQwNzIxOTQ3NzE0MjIyNzQ5OTUyMTYxNjA0MDQ4NTgwNzIyNzYxODAxMTk3MjI0\n",
        "Mjg3MDU1NDQ0MTg5MTI2MzQyMTE5MTc0MTA0MTg5NDgxODA5NTk3MTYyMTUyMTIy\n",
        "MDczODEyNTM3MTk3MzA5NzQ0MTUzNTYzNjEwODUwNjg4Mzg2NDQ2NzQ2MDQwMTI3\n",
        "MDcxMjE2NjQ2OTQxMDYxNzUxMzQ0MDQ2ODU5OTkxNjYwNDgzOTE3MDA1OTUxNDQ2\n",
        "OTc3MTM0MjY1ODUwNjcwMTAzMzgyMDQ4NDI2NjYxMzc3MDAyMTY5MDk2Mjg2ODAy\n",
        "NTg2NTcyMDE1MzIzMjY4NzMyMTQwMjEwMjkwMTkxODU2MjI0MDAwMjU3ODIxNzg2\n",
        "OTEyNTI0NzM3MjI5NDU2Mzg5NTYxNTc0MjE2MjgzNzE2NTc2NjM0NTU=\n",
        "-----END PUBLIC KEY-----"
    )
)

TEST_PUBLIC_KEY_2 = "".join(
    (
        "-----BEGIN PUBLIC KEY-----\n",
        "MTUxNzQ0OTMxOTkzNTkwNjc0NTIzODA3OTk3NzcyODMzNzg4NDU1Mjg2ODM3Mzk4\n",
        "NTE4NDA5ODI5MDc3OTM1MjY2MDIxMTI3ODY4MzcyMDU3NTMwOTAyNTgxNDIyODUz\n",
        "NTU1NzkxNzUyODc0OTExMjI2NTU3MjIzNTgxMjU1MzUwMzA5MDA1NzYwMDE3NDk1\n",
        "MjQ3NDY4OTg0OTkzMTU1ODkzNDM5MTMzMTQxNTgzNTYyNDE3NzA1ODYwODQzMzcy\n",
        "ODg4MzQyNDU0Njc4NjIyOTAzNDYyOTcxNjIwMDQxMTE5MTg5NDI1MzUxNzkyODEx\n",
        "ODQzMDE3NzYwMTI5MzAwNjA4NTExNDEzMTI0MTQ2Nzc0MzAyNTI0OTY4NTY5MjYx\n",
        "MTQ0Njc4NjQ4Njg4MjkzNzA5Njg4NjM3MTIyMjUyNTI4NzYxNDgyMTgwMDY4ODE1\n",
        "MzMzNzc3ODY2OTE2NjkwNzc5NTgzODQ1OTE0MjM1ODkzOTg5NDQxMzE3NjA2NTQx\n",
        "NDA4OTQ4MTI3NzU1MDEzMjUzMzUyNzg3NzU4OTU2OTk3Mjg0MDU0ODAzMDgxMzY4\n",
        "ODE3MTEyNDIwOTEzNTM4MDE3NzI0NDI1OTY4NjQxMDIyMTk4NzY0NzY2NjU4ODE5\n",
        "MDAwODgzNTU0NzUyMTAxMjM1MTIyODE2OTk3MDg2MTYxOTE1NDQyNTQ3MzA1NjU5\n",
        "OTAzMDAyMDA1NzU4NDk1MTEwNjA0NTU1NTUxMzAyMDEwMTU0ODI0NjMzMzkyMjQy\n",
        "MjUxMDI2OTg5NDk5NDI4MTk4MDI3NTk3OTkxMjUxMjE4MDc2ODk3Nzk=\n",
        "-----END PUBLIC KEY-----"
    )
)

TEST_ZERO_AS_PUBLIC_KEY = ("-----BEGIN PUBLIC KEY-----\nMA==\n-----END PUBLIC KEY-----")

TEST_INCORRECT_PUBLIC_KEY = "".join(
    (
        "-----BEGIN PUBLIC KEY-----\n",
        "MTUxNzQ0OTMxOTkzNTkwNjc0NTIzODA3OTk3NzcyODMzNzg4NDU1Mjg2ODM3Mzk4\n",
        "-----END PUBLIC KEY-----"
    )
)

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
    # given
    response = create_user_with_public_key(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/users/update-public-key",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "public_key": TEST_PUBLIC_KEY_2,
            "fingerprint": SHA256.new(TEST_PUBLIC_KEY_2.encode()).hexdigest(),
        },
    )

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


def test_update_public_key_with_zero_as_key(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/users/update-public-key",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "public_key": TEST_ZERO_AS_PUBLIC_KEY,
            "fingerprint": SHA256.new(TEST_ZERO_AS_PUBLIC_KEY.encode()).hexdigest(),
        },
    )

    # then
    assert response.status_code == 422


def test_update_public_key_with_incorrect_value(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = client.post(
        "/users/update-public-key",
        json={
            "user_email": TEST_VALID_USER_EMAIL_1,
            "public_key": TEST_INCORRECT_PUBLIC_KEY,
            "fingerprint": SHA256.new(TEST_INCORRECT_PUBLIC_KEY.encode()).hexdigest(),
        },
    )

    # then
    assert response.status_code == 422

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

def test_check_if_key_creation_date_is_none_when_user_has_no_public_key(
    client: TestClient
    ):
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
