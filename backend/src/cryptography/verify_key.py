from pem import PublicKey

from src.cryptography.parameters import p, q


def verify_key(pem_key: str) -> bool:
    decoded_key = int(PublicKey(pem_key).decoded_payload)
    if decoded_key <= 0 or decoded_key >= p or pow(decoded_key, q, p) != 1:
        return False
    return True
