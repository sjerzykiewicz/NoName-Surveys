import re

from pydantic import BaseModel, ValidationInfo, field_validator


class User(BaseModel):
    user_email: str

    @field_validator("user_email")
    def validate_user_email(cls, v, info: ValidationInfo) -> str:
        if v is None:
            raise ValueError("email must be provided")
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", v):
            raise ValueError("invalid email format")
        return v

    class Config:
        extra = "forbid"


class UserFilterOthers(BaseModel):
    emails: list[str]

    @field_validator("emails")
    def validate_users(cls, v, info: ValidationInfo) -> list[str]:
        for email in v:
            if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                raise ValueError("invalid email format")
        return v


class UserUpdatePublicKey(User):
    public_key: str

    @field_validator("public_key")
    def validate_user_public_key(cls, v, info: ValidationInfo) -> str:
        if v is None or v == "":
            raise ValueError("public key must be provided")
        if not re.match(r"^[1-9][0-9]*$", v):
            raise ValueError("invalid public key format")
        return v

    class Config:
        extra = "forbid"
