'''You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. 
You should minimize the number of calls to the API.'''


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    # some implementation
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:

        first_bad = None
        start, end = 1, n
        mid = (start + end) // 2

        while start <= end:

            if start == end:
                if isBadVersion(start):
                    return start
                else:
                    return first_bad

            mid = (end + start) // 2

            if not isBadVersion(mid):
                start = mid + 1

            elif isBadVersion(mid):
                if mid == start:
                    return start if isBadVersion(start) else first_bad

                end = mid - 1
                first_bad = mid
