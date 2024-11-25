from src.cryptography.fingerprint import verify
import Crypto.Hash.SHA3_256 as SHA256


def test_verify_happy_path():
    # given
    message = "test message"

    # when
    fingerprint = SHA256.new(message.encode("utf-8")).hexdigest()

    # then
    assert verify(message, fingerprint)


def test_verify_wrong_fingerprint():
    # given
    message = "test message"

    # when
    fingerprint = SHA256.new("different message".encode("utf-8")).hexdigest()

    # then
    assert not verify(message, fingerprint)
