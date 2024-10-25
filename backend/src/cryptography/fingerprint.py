import Crypto.Hash.SHA3_256 as SHA256


def verify(m: str, fingerprint: str):
    encoded = m.encode("utf-8")
    hash = SHA256.new(encoded).hexdigest()
    return fingerprint == hash
