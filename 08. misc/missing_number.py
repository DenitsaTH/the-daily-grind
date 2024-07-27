'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.'''


class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        s = set(nums)

        for num in range(n + 1):
            if num not in s:
                return num
