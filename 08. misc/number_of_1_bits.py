'''Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).

Follow up: If this function is called many times, how would you optimize it?
'''

cache = {}


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        m = n

        while m > 0:
            res += m % 2
            m = m // 2

            if m in cache:
                res += cache[m]

                return res

        cache[n] = res  # caching the values for optimization
        return res
