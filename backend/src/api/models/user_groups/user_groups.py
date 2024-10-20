import re

from pydantic import BaseModel, ValidationInfo, field_validator


class UserGroupCreator(BaseModel):
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


class UserGroupCreate(UserGroupCreator):
    user_group_name: str
    user_group_members: list[str]

    @field_validator("user_group_name")
    def validate_user_group_name(cls, v, info: ValidationInfo) -> str:
        if v is None or v == "":
            raise ValueError("name must be provided and not empty")
        if not re.match(r"^[\w /-]+$", v, re.UNICODE):
            raise ValueError("Invalid group name format")
        return v

    @field_validator("user_group_members")
    def validate_user_group_members(cls, v, info: ValidationInfo) -> str:
        if v is None or len(v) == 0:
            raise ValueError("cannot create a user group without any members")
        for email in v:
            if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                raise ValueError("invalid email format")
        return v

    class Config:
        extra = "forbid"


class UserGroupAction(UserGroupCreator):
    name: str

    @field_validator("name")
    def validate_user_public_key(cls, v, info: ValidationInfo) -> str:
        if v is None or v == "":
            raise ValueError("name must be provided")
        if not re.match(r"^[\w /-]+$", v, re.UNICODE):
            raise ValueError("Invalid group name format")
        return v


class UserGroupNameUpdate(UserGroupAction):
    new_name: str

    @field_validator("new_name")
    def validate_user_public_key(cls, v, info: ValidationInfo) -> str:
        if v is None or v == "":
            raise ValueError("new name must be provided")
        if not re.match(r"^[\w /-]+$", v, re.UNICODE):
            raise ValueError("Invalid group name format")
        return v

    class Config:
        extra = "forbid"
