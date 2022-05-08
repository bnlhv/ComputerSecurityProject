from enum import Enum


class PasswordConfiguration(Enum):
    """ Configuration class for password validation """
    LAST_PASSWORDS = 3 # other users past password backward amount to check that aren't equal
    MIN_LENGTH = 10
    LOGIN_FAILURE_LIMIT = 3
    MIN_NUMERIC = 1
    MIN_ALPHA = 1
    MIN_SPECIAL = 1
    ALLOWED_SPECIAL_CHARACTERS = "~!@#$%^&*()_+{}\":;'[]"
