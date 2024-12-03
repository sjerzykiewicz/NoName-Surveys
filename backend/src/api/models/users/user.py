from pydantic import field_validator

from src.api.models.base import Base


class User(Base):
    user_email: str

    @field_validator("user_email")
    def validate_user_email(cls, v) -> str:
        return Base.validate_email(v)


class UserFilterOthers(Base):
    emails: list[str]

    @field_validator("emails")
    def validate_users(cls, v) -> list[str]:
        return Base.validate_emails(v)


class UserUpdatePublicKey(User):
    public_key: str
    fingerprint: str

    @field_validator("public_key")
    def validate_user_public_key(cls, v) -> str:
        return Base.validate_pem_key(v) and Base.validate_key_correctness(v)

    @field_validator("fingerprint")
    def validate_fingerprint(cls, v) -> str:
        return Base.validate_fingerprint(v)
