import functools

import Crypto.Hash.SHA384 as SHA384


class Ring:
    def __init__(self, keys, bit_length: int = 2048) -> None:
        self.keys = keys
        self.bit_length = bit_length
        self.num_keys = len(keys)
        self.q_value = 1 << (bit_length - 1)

    def verify(self, message: str, signature) -> bool:
        self._compute_permutation(message)

        y_values = map(
            lambda index: self._compute_g(
                signature[index + 1], self.keys[index].e, self.keys[index].n
            ),
            range(len(signature) - 1),
        )
        y_values = list(y_values)

        r_value = functools.reduce(
            lambda x, index: self._compute_E(x ^ y_values[index]),
            range(self.num_keys),
            signature[0],
        )
        return r_value == signature[0]

    def _compute_permutation(self, message):
        encoded_message = message.encode("utf-8")
        self.permutation = int(SHA384.new(encoded_message).hexdigest(), 16)

    def _compute_E(self, x):
        encoded_message = f"{x}{self.permutation}".encode("utf-8")
        return int(SHA384.new(encoded_message).hexdigest(), 16)

    def _compute_g(self, x, e, n):
        quotient, remainder = divmod(x, n)
        return (
            quotient * n + pow(remainder, e, n)
            if ((quotient + 1) * n) <= ((1 << self.bit_length) - 1)
            else x
        )
