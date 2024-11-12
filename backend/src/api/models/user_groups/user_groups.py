from pydantic import field_validator

from src.api.models.base import Base


class UserGroupCreator(Base):
    user_email: str

    @field_validator("user_email")
    def validate_user_email(cls, v) -> str:
        return Base.validate_email(v)


class UserGroupCreate(UserGroupCreator):
    user_group_name: str
    user_group_members: list[str]

    @field_validator("user_group_name")
    def validate_user_group_name(cls, v) -> str:
        return Base.validate_user_group_name(v)

    @field_validator("user_group_members")
    def validate_user_group_members(cls, v) -> str:
        return Base.validate_emails(v)


class UserGroupAction(UserGroupCreator):
    name: str

    @field_validator("name")
    def validate_user_group_name(cls, v) -> str:
        return Base.validate_user_group_name(v)


class UserGroupMultipleActions(UserGroupCreator):
    names: list[str]

    @field_validator("names")
    def validate_user_group_names(cls, v) -> str:
        return Base.validate_user_group_names(v)


class UserGroupNameUpdate(UserGroupAction):
    new_name: str

    @field_validator("new_name")
    def validate_new_user_group_name(cls, v) -> str:
        return Base.validate_user_group_name(v)


class UserGroupUsersActions(UserGroupAction):
    users: list[str]

    @field_validator("users")
    def validate_user_emails(cls, v) -> str:
        return Base.validate_emails(v)


class AllUserGroupsOutput(Base):
    user_group_name: str
    all_members_have_public_keys: bool


class UserGroupMembersOutput(Base):
    email: str
    has_public_key: bool
