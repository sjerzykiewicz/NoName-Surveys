import pytest
from src.api.models.base import Base


def test_validate_email():
    assert Base.validate_email("test@example.com") == "test@example.com"

    with pytest.raises(ValueError):
        Base.validate_email("invalid-email")

    with pytest.raises(ValueError):
        Base.validate_email(5)

    with pytest.raises(ValueError):
        Base.validate_email(None)


def test_validate_emails():
    assert Base.validate_emails(
        ["test@example.com", "test2@example.com"]
    ) == ["test@example.com", "test2@example.com"]

    with pytest.raises(ValueError):
        Base.validate_emails(["invalid-email"])

    with pytest.raises(ValueError):
        Base.validate_emails(None)

    with pytest.raises(ValueError):
        Base.validate_emails([])

    with pytest.raises(ValueError):
        Base.validate_emails([1, 2, 3, 4])


def test_validate_survey_code():
    assert Base.validate_survey_code("123456") == "123456"

    with pytest.raises(ValueError):
        Base.validate_survey_code("12345")

    with pytest.raises(ValueError):
        Base.validate_survey_code("abcdef")

    with pytest.raises(ValueError):
        Base.validate_survey_code(5)

    with pytest.raises(ValueError):
        Base.validate_survey_code(None)


def test_validate_survey_codes():
    assert Base.validate_survey_codes(["123456", "654321"]) == ["123456", "654321"]

    with pytest.raises(ValueError):
        Base.validate_survey_codes(["12345"])

    with pytest.raises(ValueError):
        Base.validate_survey_codes(None)

    with pytest.raises(ValueError):
        Base.validate_survey_codes([])

    with pytest.raises(ValueError):
        Base.validate_survey_codes([1, 2, 3, 4])


def test_validate_digits_only():
    assert Base.validate_digits_only("123456") == "123456"

    with pytest.raises(ValueError):
        Base.validate_digits_only("12345a")

    with pytest.raises(ValueError):
        Base.validate_digits_only(None)

    with pytest.raises(ValueError):
        Base.validate_digits_only(5)


def test_validate_user_group_name():
    assert Base.validate_user_group_name("Group 1") == "Group 1"

    with pytest.raises(ValueError):
        Base.validate_user_group_name("")

    with pytest.raises(ValueError):
        Base.validate_user_group_name(None)

    with pytest.raises(ValueError):
        Base.validate_user_group_name(5)


def test_validate_user_group_names():
    assert Base.validate_user_group_names(
        ["Group 1", "Group 2"]
    ) == ["Group 1", "Group 2"]

    with pytest.raises(ValueError):
        Base.validate_user_group_names([""])

    with pytest.raises(ValueError):
        Base.validate_user_group_names(None)

    with pytest.raises(ValueError):
        Base.validate_user_group_names([])

    with pytest.raises(ValueError):
        Base.validate_user_group_names([1, 2, 3, 4])


def test_validate_pem_key():
    valid_key = "-----BEGIN PUBLIC KEY-----\n1\n-----END PUBLIC KEY-----"
    assert Base.validate_pem_key(valid_key) == valid_key

    with pytest.raises(ValueError):
        Base.validate_pem_key("invalid-key")

    with pytest.raises(ValueError):
        Base.validate_pem_key(None)

    with pytest.raises(ValueError):
        Base.validate_pem_key("")

    with pytest.raises(ValueError):
        Base.validate_pem_key(5)


def test_validate_fingerprint():
    assert Base.validate_fingerprint("abcdef123456") == "abcdef123456"

    with pytest.raises(ValueError):
        Base.validate_fingerprint("invalid-fingerprint")

    with pytest.raises(ValueError):
        Base.validate_fingerprint(None)

    with pytest.raises(ValueError):
        Base.validate_fingerprint("")

    with pytest.raises(ValueError):
        Base.validate_fingerprint(5)


def test_validate_signature():
    assert Base.validate_signature("123456") == "123456"

    with pytest.raises(ValueError):
        Base.validate_signature("invalid-signature")

    with pytest.raises(ValueError):
        Base.validate_signature(None)

    with pytest.raises(ValueError):
        Base.validate_signature("")

    with pytest.raises(ValueError):
        Base.validate_signature(5)
