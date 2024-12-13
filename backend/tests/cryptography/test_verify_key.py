from src.cryptography.verify_key import verify_key
from tests.common_values import (
    TEST_PUBLIC_KEY_1,
    TEST_ZERO_AS_PUBLIC_KEY,
    TEST_INCORRECT_PUBLIC_KEY
)

def test_verify_happy_path():
    assert verify_key(TEST_PUBLIC_KEY_1)

def test_verify_zero():
    assert not verify_key(TEST_ZERO_AS_PUBLIC_KEY)

def test_verify_incorrect_key():
    assert not verify_key(TEST_INCORRECT_PUBLIC_KEY)
