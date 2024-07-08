'''Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.'''

# Version 1: use set to keep track of duplicates


class Solution:
    def containsDuplicate(self, nums):
        duplicates = set()

        for i in range(len(nums)):
            if nums[i] in duplicates:
                return True

            duplicates.add(nums[i])

        return False


# Version 2: sort the array first

class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False
