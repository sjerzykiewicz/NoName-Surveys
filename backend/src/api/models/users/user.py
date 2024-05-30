import re

from pydantic import BaseModel, ValidationInfo, field_validator


class User(BaseModel):
    user_email: str

    @field_validator("user_email")
    def validate_user_email(cls, v, info: ValidationInfo) -> str:
        if v is None:
            raise ValueError("email must be provided")
        if not re.match(
            r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", v
        ):
            raise ValueError("invalid email format")
        return v

    class Config:
        extra = "forbid"


class CreateUser(User):
    public_key: str

    class Config:
        extra = "forbid"
