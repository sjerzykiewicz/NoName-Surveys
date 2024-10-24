import Crypto.Hash.SHA3_384 as SHA384
import Crypto.Hash.SHAKE256 as SHAKE256
from gmpy2 import add, f_mod, mpz, mul, powmod

# cyclic group parameters
# from RFC 5114
# 2048-bit p, 256-bit q
# G = {g^n mod p | n < q}
P_HEX = "".join(
    (
        "87A8E61DB4B6663CFFBBD19C65195999",
        "8CEEF608660DD0F25D2CEED4435E3B00",
        "E00DF8F1D61957D4FAF7DF4561B2AA30",
        "16C3D91134096FAA3BF4296D830E9A7C",
        "209E0C6497517ABD5A8A9D306BCF67ED",
        "91F9E6725B4758C022E0B1EF4275BF7B",
        "6C5BFC11D45F9088B941F54EB1E59BB8",
        "BC39A0BF12307F5C4FDB70C581B23F76",
        "B63ACAE1CAA6B7902D52526735488A0E",
        "F13C6D9A51BFA4AB3AD8347796524D8E",
        "F6A167B5A41825D967E144E514056425",
        "1CCACB83E6B486F6B3CA3F7971506026",
        "C0B857F689962856DED4010ABD0BE621",
        "C3A3960A54E710C375F26375D7014103",
        "A4B54330C198AF126116D2276E11715F",
        "693877FAD7EF09CADB094AE91E1A1597",
    )
)

Q_HEX = "".join(
    ("8CF83642A709A097B447997640129DA2", "99B1A47D1EB3750BA308B0FE64F5FBD3")
)

R_HEX = "".join(
    (
        "F65B7EA7706034A28A29B9436AF161BB",
        "F3632483671C60AEE9B1A6A496FFF904",
        "FCB09731B6C6E16B551CEC2C063910B0",
        "4E40795D4BEB474DB762E28CC923AE40",
        "FDBAF05BF7501D0314C3CBE4BAD7329D",
        "D473BDF441E7B8B387B402CD0BE7DC53",
        "4FA6D3C039BDAD133F59DC899FD570A6",
        "67C453D08150A35CF5E845087BD9ACFA",
        "8333343375E8EE52965A84C699C59DFE",
        "F852EFB96023BEF0FFB2F99C53AC2D94",
        "CD2969764698B8DDE401DA6AA6BDB3B0",
        "3B5506D287090F8E852C05EC0BDB3C0C",
        "4FBEC1A4AB9FE141E8A7C9EADB17D335",
        "921B673615A7FC0C92384946B9AB6452",
    )
)

G_HEX = "".join(
    (
        "3FB32C9B73134D0B2E77506660EDBD48",
        "4CA7B18F21EF205407F4793A1A0BA125",
        "10DBC15077BE463FFF4FED4AAC0BB555",
        "BE3A6C1B0C6B47B1BC3773BF7E8C6F62",
        "901228F8C28CBB18A55AE31341000A65",
        "0196F931C77A57F2DDF463E5E9EC144B",
        "777DE62AAAB8A8628AC376D282D6ED38",
        "64E67982428EBC831D14348F6F2F9193",
        "B5045AF2767164E1DFC967C1FB3F2E55",
        "A4BD1BFFE83B9C80D052B985D182EA0A",
        "DB2A3B7313D3FE14C8484B1E052588B9",
        "B7D2BBD2DF016199ECD06E1557CD0915",
        "B3353BBB64E0EC377FD028370DF92B52",
        "C7891428CDC67EB6184B523D1DB246C3",
        "2F63078490F00EF8D647D148D4795451",
        "5E2327CFEF98C582664B4C0F6CC41659",
    )
)


p = mpz(P_HEX, 16)
q = mpz(Q_HEX, 16)
r = mpz(R_HEX, 16)
g = mpz(G_HEX, 16)


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


def verify_lrs(message: str, keys: list[mpz], signature: list[mpz]) -> bool:
    concatenated_keys: str = "".join([k.digits() for k in keys])

    h = h2(concatenated_keys)

    y0 = signature[0]

    n = len(signature) - 2

    s = signature[1]
    c = signature[2:]

    prod_y_c = mpz(1)
    sum_c = mpz(0)

    for i in range(n):
        prod_y_c = mul(prod_y_c, powmod(int(keys[i]), c[i], p))
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
