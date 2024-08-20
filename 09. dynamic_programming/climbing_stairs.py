'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''


class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {1: 1, 2: 2}

        def recursive(m: int, memo=cache) -> int:

            if m in memo:
                return memo[m]

            memo[m] = recursive(m-1) + recursive(m-2)
            return memo[m]

        return recursive(n)
