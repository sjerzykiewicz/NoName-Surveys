from fastapi.testclient import TestClient

from test_users import create_user, create_user_with_public_key

TEST_VALID_USER_EMAIL_1 = "user1@st.amu.edu.pl"
TEST_VALID_USER_EMAIL_2 = "user2@st.amu.edu.pl"
TEST_VALID_USER_EMAIL_3 = "user3@st.amu.edu.pl"
TEST_USER_GROUP_NAME = "Test Group"


def create_user_group(client: TestClient, email: str, group_name: str, members: list[str]):
    return client.post(
        "/user_groups/create",
        json={
            "user_email": email,
            "user_group_name": group_name,
            "user_group_members": members,
        },
    )


def test_create_user_group_happy_path(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)

    # when
    response = create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME, [TEST_VALID_USER_EMAIL_2])

    # then
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "user group created successfully"


def test_create_user_group_user_not_registered(client: TestClient):
    # when
    response = create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME, [TEST_VALID_USER_EMAIL_2])

    # then
    assert response.status_code == 400


def test_create_user_group_with_unregistered_members(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)

    # when
    response = create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME, [TEST_VALID_USER_EMAIL_2])

    # then
    assert response.status_code == 400


def test_get_user_groups_count(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user_groups/count",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data == 1


def test_get_user_groups(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user_groups/all/0",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["user_group_name"] == TEST_USER_GROUP_NAME


def test_get_user_groups_with_members_having_public_keys(client: TestClient):
    # given
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_1)
    create_user_with_public_key(client, TEST_VALID_USER_EMAIL_2)
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user_groups/all-with-public-keys",
        json={"user_email": TEST_VALID_USER_EMAIL_1},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0] == TEST_USER_GROUP_NAME


def test_get_user_group_members_count(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user_groups/group_members_count",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "name": TEST_USER_GROUP_NAME},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data == 1


def test_get_user_group(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user_groups/fetch/0",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "name": TEST_USER_GROUP_NAME},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["email"] == TEST_VALID_USER_EMAIL_2


def test_rename_user_group(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME, [TEST_VALID_USER_EMAIL_2])
    new_group_name = "New Group Name"

    # when
    response = client.post(
        "/user_groups/rename",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "name": TEST_USER_GROUP_NAME, "new_name": new_group_name},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "user group updated successfully"


def test_delete_user_group(client: TestClient):
    # given
    create_user(client, TEST_VALID_USER_EMAIL_1)
    create_user(client, TEST_VALID_USER_EMAIL_2)
    create_user_group(client, TEST_VALID_USER_EMAIL_1, TEST_USER_GROUP_NAME, [TEST_VALID_USER_EMAIL_2])

    # when
    response = client.post(
        "/user_groups/delete",
        json={"user_email": TEST_VALID_USER_EMAIL_1, "names": [TEST_USER_GROUP_NAME]},
    )

    # then
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "user group deleted successfully"
