'''Given an integer n, return the number of prime numbers that are strictly less than n.'''


class Solution:
    def countPrimes(self, n: int) -> int:

        if n == 0 or n == 1:
            return 0

        curr = 2
        all_nums = [x for x in range(n)]

        # Sieve of Eratosthenes
        # loop to the power of curr
        while curr * curr <= n:
            if all_nums[curr]:

                # mark all nums divisible by curr, starting from the square of curr
                for i in range(curr*curr, n, curr):
                    all_nums[i] = 0

            curr += 1

        return len([i for i in all_nums if i and i != 1])
