from pytest import raises
from src.services.utils.exceptions import InvalidPageNumberException, UserAccessException
import src.services.utils.helpers as helpers


def test_validate_page_for_pagination_negative_number():
    # given
    page = -1

    # when & then
    with raises(InvalidPageNumberException) as exception:
        helpers.validate_page_for_pagination(page)


def test_validate_page_for_pagination_zero():
    # given
    page = 0

    # when
    helpers.validate_page_for_pagination(page)

    # then
    # no exception is raised


def test_check_if_user_has_access_positive():
    # given
    user_id = 1

    # when
    result = helpers.check_if_user_has_access(user_id, user_id)

    # then
    assert result is None


def test_check_if_user_has_access_negative():
    # given
    user_id = 1
    other_user_id = 2

    # when & then
    with raises(UserAccessException):
        helpers.check_if_user_has_access(user_id, other_user_id)
