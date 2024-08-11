'''The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.'''

# ----------- Version 1 -----------


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y

        # Count the number of 1s which gives the number of differing bits
        return bin(diff).count('1')

# ----------- Version 2 -----------


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def get_32bit_bin_repr(num) -> str:
            # pad to a width of 32 with leading zeros in binary format
            return f'{num:032b}'

        distance = 0

        bin1, bin2 = get_32bit_bin_repr(x), get_32bit_bin_repr(y)

        for i in range(len(bin1)):
            if bin1[i] != bin2[i]:
                distance += 1

        return distance
