'''Reverse bits of a given 32 bits unsigned integer.'''


# ----------- Version 1 -----------

class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        # iterate through each bit
        for i in range(32):
            # extract the last bit of n
            # Bitwise AND -> Result bit 1, if both operand bits are 1; otherwise results bit 0.
            last_bit = n & 1

            # shift result to the left
            result = (result << 1) | last_bit

            # Shifts the bits of the number to the right and fills 0 on voids left
            n >>= 1

        return result


# ----------- Version 2 -----------
cache = {}


class Solution:
    def reverseBits(self, n: int) -> int:

        if n in cache:
            return cache[n]

        binary_str = bin(n)[2:].zfill(32)
        reversed_binary_str = binary_str[::-1]
        reversed_int = int(reversed_binary_str, 2)

        cache[n] = reversed_int  # cache for optimization

        return reversed_int
