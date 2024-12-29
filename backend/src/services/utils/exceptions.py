class UserNotFoundException(Exception):
    pass


class UserGroupNotFoundException(Exception):
    pass


class SurveyNotFoundException(Exception):
    pass


class SurveyDraftNotFoundException(Exception):
    pass


class InvalidPageNumberException(Exception):
    pass


class UserAccessException(Exception):
    pass


class DuplicateUserException(Exception):
    pass


class LimitExceededException(Exception):
    pass


class InvalidFingerprintException(Exception):
    pass


class UserGroupExistsException(Exception):
    pass


class UserGroupLimitExceededException(Exception):
    pass


class SurveyLimitExceededException(Exception):
    pass


class InvalidSurveyStructureException(Exception):
    pass


class UserGroupMemberException(Exception):
    pass


class SurveyAccessException(Exception):
    pass


class InvalidSignatureException(Exception):
    pass


class DuplicateAnswerException(Exception):
    pass


class UserGroupLimitException(Exception):
    pass
