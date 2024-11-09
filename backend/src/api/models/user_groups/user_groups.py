import re

from pydantic import ValidationInfo, field_validator

from src.api.models.base import Base


class UserGroupCreator(Base):
    user_email: str

    @field_validator("user_email")
    def validate_user_email(cls, v, info: ValidationInfo) -> str:
        if v is None:
            raise ValueError("email must be provided")
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", v):
            raise ValueError("invalid email format")
        return v


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


class UserGroupAction(UserGroupCreator):
    name: str

    @field_validator("name")
    def validate_user_public_key(cls, v, info: ValidationInfo) -> str:
        if v is None or v == "":
            raise ValueError("name must be provided")
        if not re.match(r"^[\w /-]+$", v, re.UNICODE):
            raise ValueError("Invalid group name format")
        return v


class UserGroupMultipleActions(UserGroupCreator):
    names: list[str]

    @field_validator("names")
    def validate_user_public_key(cls, v, info: ValidationInfo) -> str:
        if v is None or len(v) == 0:
            raise ValueError("names must be provided")
        for name in v:
            if not re.match(r"^[\w /-]+$", name, re.UNICODE):
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


class AllUserGroupsOutput(Base):
    user_group_name: str
    all_members_have_public_keys: bool


class UserGroupMembersOutput(Base):
    email: str
    has_public_key: bool
