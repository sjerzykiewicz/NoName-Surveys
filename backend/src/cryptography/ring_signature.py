import Crypto.Hash.SHA3_384 as SHA384
import Crypto.Hash.SHAKE256 as SHAKE256
from gmpy2 import add, f_mod, mpz, mul, powmod
from pem import PublicKey

from src.cryptography.parameters import g, p, q, r


# h1 : {0,1}* -> Zq/Z
# hash to {0,1}^k, reduce mod q
def h1(x: str):
    encoded = x.encode("utf-8")
    return f_mod(mpz(SHA384.new(encoded).hexdigest(), 16), q)


# h2 : {0,1}* -> <g>
def h2(x: str):
    encoded = x.encode("utf-8")
    # hash to {0,1}^2716
    shake = SHAKE256.new()
    shake.update(encoded)
    hashed = mpz(shake.read(2176).hex(), 16)

    # reduce mod (p-1) -> element of Z(p-1)/Z
    hashed = f_mod(hashed, (p - 1))

    # add 1 -> element of Z*p
    hashed = add(hashed, 1)

    # i^r is an element of <g>
    return powmod(hashed, r, p)


def verify_lrs(message: str, keys: list[str], signature: list[mpz]) -> bool:
    decoded_keys = [mpz(int(PublicKey(k).decoded_payload)) for k in keys]
    concatenated_keys: str = "".join([k.digits() for k in decoded_keys])
    h = h2(concatenated_keys)

    y0 = signature[0]

    n = len(signature) - 2

    s = signature[1]
    c = signature[2:]

    prod_y_c = mpz(1)
    sum_c = mpz(0)

    for i in range(n):
        prod_y_c = mul(prod_y_c, powmod(decoded_keys[i], c[i], p))
        sum_c = f_mod(add(sum_c, c[i]), q)

    g_to_s = powmod(g, s, p)
    h_to_s = powmod(h, s, p)

    for_hashing = (
        concatenated_keys
        + y0.digits()
        + message
        + (f_mod(mul(g_to_s, prod_y_c), p)).digits()
        + (f_mod(mul(h_to_s, powmod(y0, sum_c, p)), p)).digits()
    )
    return sum_c == h1(for_hashing)
