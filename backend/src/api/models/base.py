from re import UNICODE, match

from pydantic import BaseModel, ConfigDict

EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
SURVEY_CODE_REGEX = r"^\d{6}$"
DIGITS_ONLY_REGEX = r"^\d+$"
USER_GROUP_NAME_REGEX = r"^[\w /-]+$"
KEY_PEM_REGEX = r"-----BEGIN PUBLIC KEY-----(\n|\r|\r\n)([0-9a-zA-Z\+\/=]{64}(\n|\r|\r\n))*([0-9a-zA-Z\+\/=]{1,63}(\n|\r|\r\n))?-----END PUBLIC KEY-----"
FINGERPRINT_REGEX = r"^[0-9a-f]*$"


class Base(BaseModel):
    model_config = ConfigDict(extra="forbid")

    def validate_email(value):
        if value is None:
            raise ValueError("email must be provided")
        if not isinstance(value, str):
            raise ValueError("email must be a string")

        if not match(EMAIL_REGEX, value):
            raise ValueError("invalid email format")
        return value

    def validate_emails(value):
        if value is None:
            raise ValueError("emails must be provided")
        if not isinstance(value, list):
            raise ValueError("emails must be a list")

        if len(value) == 0:
            raise ValueError("emails must be provided")

        for email in value:
            Base.validate_email(email)
        return value

    def validate_survey_code(value):
        if value is None:
            raise ValueError("survey code must be provided")
        if not isinstance(value, str):
            raise ValueError("survey code must be a string")

        if not match(SURVEY_CODE_REGEX, value):
            raise ValueError("survey code must be a string consisting of 6 digits")
        return value

    def validate_digits_only(value):
        if value is None:
            raise ValueError("value must be provided")
        if not isinstance(value, str):
            raise ValueError("value must be a string")

        if not match(DIGITS_ONLY_REGEX, value):
            raise ValueError("value must be a string consisting of digits only")
        return value

    def validate_user_group_name(value):
        if value is None or not isinstance(value, str) or value == "":
            raise ValueError("name must be provided and not empty string")

        if not match(USER_GROUP_NAME_REGEX, value, UNICODE):
            raise ValueError("Invalid group name format")
        return value

    def validate_user_group_names(value):
        if value is None or not isinstance(value, list) or len(value) == 0:
            raise ValueError("names must be provided")

        for name in value:
            Base.validate_user_group_name(name)
        return value

    def validate_pem_key(value):
        if value is None or not isinstance(value, str) or value == "":
            raise ValueError("public key must be provided")

        if not match(KEY_PEM_REGEX, value):
            raise ValueError("invalid public key format")
        return value

    def validate_fingerprint(value):
        if value is None or not isinstance(value, str) or value == "":
            raise ValueError("key fingerprint must be provided")

        if not match(FINGERPRINT_REGEX, value):
            raise ValueError("invalid fingerprint format")
        return value
